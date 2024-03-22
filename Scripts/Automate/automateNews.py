import os
import datetime
import configparser
import docx2txt
import hashlib
from ftplib import FTP
from time import time, sleep
from subprocess import Popen
from itertools import count
from shutil import copy, move
from SemiAutomatic.startPublication import startPublicating

config = configparser.ConfigParser()
config.read("settings.ini")

while True:
    try:
        print("Подключаемся к удалённому серверу...")
        ftp = FTP(host=config['FTP']['host'], timeout=1600)
        ftp.port = 21
        ftp.login(user=config['FTP']['username'], passwd=config['FTP']['password'])
        print("Подключение успешно установлено!")
    except TimeoutError:
        print("Не удалось соединиться с сервером. Проверьте ваше подключение.")
        input("Попробовать подключиться снова? ")
        continue
    break

def getActualDirectory():
    return config['Filesystem']['mgrfolder']+"Web\\{0}\\{1}\\".format(datetime.date.today().strftime("%B"), datetime.date.today().strftime("%d.%m"))

def foldersStatus():
    actualDir = getActualDirectory()
    
    if not os.path.exists(actualDir):
        os.makedirs(actualDir+'Ready/Stored')
    
    Popen(['explorer', actualDir])
    print("Открываем сегодняшнюю директорию новостей...")
    sleep(5)

def waitingDir():  
    
    msg = [
        f"Ожидаем новую директорию .*..",
        f"Ожидаем новую директорию ..*.",
        f"Ожидаем новую директорию ...*",
        f"Ожидаем новую директорию *..."
    ]
    
    os.chdir(getActualDirectory())

    for index in count(3, 1):
        os.system("cls")
        print(msg[index % 4])
        for dir in os.listdir():
            if os.path.isdir(dir) and dir != "Ready":
                print("Начинаем работать с директорией {0}...".format(dir))
                return dir
        sleep(3)
        
def convertDocxToTXT(foundDir):
    os.chdir(foundDir)
    for file in os.listdir():
        if file.endswith("docx") and not os.path.exists(file.split('.')[0]+".txt"):
            print("Начинаем преобразование {0} в {1}".format(file, file.split('.')[0]+".txt"))
            txtFile = docx2txt.process(file)
            with open(file.split('.')[0]+".txt", "wb") as convertedFile:
                convertedFile.write(txtFile.encode())
            convertedFile.close()
            print("Преобразование {0} в {1} завершено".format(file, file.split('.')[0]+".txt"))
            os.system("explorer "+file.split('.')[0]+".txt")
            input("Завершите разметку файла, после чего, нажмите Enter.")

def uploadImagesOnServer():
    if not os.path.exists("Images"):
        print("Пропускаем выгрузку изображений, директория Images не найдена.")
        return
    
    if not len(os.listdir("Images")):
        print("Пропускаем выгрузку изображений, директория Images пустая.")
        return
        
    if not os.path.exists("Images\\table.txt"):
    
        os.chdir("Images")
        
        hashedArray = []
        uploadPath = config['Web']['uploadpath']
        
        table = '<table border="0" cellpadding="0" cellspacing="0" style="width:800px"><tbody>'
        
        with open('links.txt', 'w', encoding='utf-8') as linksFile:
            for file in os.listdir():
                if file.endswith(".jpg"):
                    print("\nГотовим {0} к выгрузке".format(file))
                    print("Хешируем имя...")
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
                        with open(newName, "rb") as ftpFile:
                            ftp.storbinary("STOR "+newName, ftpFile)
                        print('Публикация: Файл успешно выгружен.')
                    except FileNotFoundError:
                        print("Публикация: Файл не найден.")

        table += '</tbody></table>'

        with open('table.txt', 'w', encoding='utf-8') as textFile:
            textFile.write(table)
        print("Таблица успешно сформирована.")
        os.chdir('..')

def formattingNews():
    content = ""
    symbols = ['«', '»']
    
    for txtFile in os.listdir():
        if txtFile.endswith("txt") and input("{0} необходимый файл? ".format(txtFile)) in ["y", "yes"]: 
            with open(txtFile, 'r', encoding="utf-8") as file:
                text = file.readlines()
                line_count = sum(1 for line in text)
                for index, line in enumerate(text):
                    if (index == line_count-1):
                        content += "<p style='text-align: right;'><strong><i>"+line.strip()+"</i></strong></p><br>"
                    elif len(line.strip()) > 0:
                        content += "<p style='text-align: justify;'>&ensp;&ensp;&ensp;&ensp;&ensp;"+line.strip()+"</p>"
            file.close()

            for symbol in symbols:
                content = content.replace(symbol, '"')
                
            try:
                with open('Images/table.txt', 'r') as tableFile:
                    table = tableFile.read()
                    
                content += table
            except FileNotFoundError:
                print("Не найдена таблица изображений.")
                
            if not os.path.exists("Layout"):
                os.mkdir("Layout")
            
            with open('Layout\\Макет.txt', 'w', encoding='utf-8') as textFile:
                textFile.write(content)
            
            textFile.close()
            print("Создание макета завершено.")
    os.chdir("..")

def moveFolderToReady(foundDir):
    move(foundDir, "Ready")
    os.chdir("..\\..")
    for xlsx in os.listdir():
        if xlsx.endswith("xlsx"):
            Popen(['explorer', xlsx])
    
def AutomateNews():
    foundDir = waitingDir()
    convertDocxToTXT(foundDir)
    uploadImagesOnServer()
    formattingNews()
    moveFolderToReady(foundDir)
    startPublicating()
    AutomateNews()

foldersStatus()
if __name__ == "__main__":
    AutomateNews()