import os
import hashlib
from ftplib import FTP

uploadPath = "https://feopoliteh.ru/assets/uploads/"
hashedArray = []

ftp = FTP(host="ftp49.hostland.ru", timeout=300)
ftp.login(user="host1335833_upload", passwd="larikanik_20062001")

table = '<table border="0" cellpadding="0" cellspacing="0" style="width:800px"><tbody>'
path = input("Ссылка на корневую директорию новости: ")

path += '/Images/'
 
os.chdir(path)

with open('links.txt', 'w', encoding='utf-8') as linksFile:
    for count, file in enumerate(os.listdir()):
        if file.endswith(".jpg"):
            fileHash = hashlib.md5(file.encode())
            newName = fileHash.hexdigest()+".jpg"
            hashedArray.append(newName)
            table += '<tr><td><img src="'+uploadPath+newName+'" style="width:800px" /></td></tr>'

            os.rename(file, newName)

            linksFile.write(uploadPath+newName+"\n")

            try:
                with open(path+newName, "rb") as ftpFile:
                    ftp.storbinary("STOR "+newName, ftpFile)
                print('Публикация: Файл успешно выгружен.')
            except FileNotFoundError:
                print("Публикация: Файл не найден.")

table += '</tbody></table>'

with open('table.txt', 'w', encoding='utf-8') as textFile:
    textFile.write(table)