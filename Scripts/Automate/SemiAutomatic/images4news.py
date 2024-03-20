import os
import hashlib
from ftplib import FTP
from time import time
from shutil import copy
from sys import argv

import configparser
config = configparser.ConfigParser()
config.read("settings.ini")

uploadPath = config['Web']['uploadPath']
hashedArray = []

while True:
    try:
        print("Подключаемся к удалённому серверу...")
        ftp = FTP(host=config['FTP']['host'], timeout=600)
        ftp.port = 21
        ftp.login(user=config['FTP']['username'], passwd=config['FTP']['password'])
        print("Подключение успешно установлено!")
    except TimeoutError:
        print("Не удалось соединиться с сервером. Проверьте ваше подключение.")
        input("Попробовать подключиться снова? ")
        continue
    break

table = '<table border="0" cellpadding="0" cellspacing="0" style="width:800px"><tbody>'
if argv[-1][-1] != '/':
   path = input("Ссылка на корневую директорию новости: ")
else:
    path = argv[-1]

path += '/Images/'
 
os.chdir(path)

with open('links.txt', 'w', encoding='utf-8') as linksFile:
    for count, file in enumerate(os.listdir()):
        if file.endswith(".jpg"):
            fileHash = hashlib.md5((file+str(time())).encode())
            newName = fileHash.hexdigest()+".jpg"
            hashedArray.append(newName)
            table += '<tr><td><img src="'+uploadPath+newName+'" style="width:800px" /></td></tr>'
            if not os.path.exists("Original"):
                os.mkdir("Original")
            if os.path.exists(f"Original\\{file}"):
                os.remove(f"Original\\{file}")
            copy(file, f"Original\\{file}")
                
            os.rename(file, newName)

            linksFile.write(uploadPath+newName+"\n")

            try:
                print(f"\nОтправляем {newName} на сервер...")
                with open(path+newName, "rb") as ftpFile:
                    ftp.storbinary("STOR "+newName, ftpFile)
                print('Публикация: Файл успешно выгружен.')
            except FileNotFoundError:
                print("Публикация: Файл не найден.")

table += '</tbody></table>'

with open('table.txt', 'w', encoding='utf-8') as textFile:
    textFile.write(table)

print("Таблица успешно сформирована.")
input("Нажмите Enter, чтобы завершить работу.")