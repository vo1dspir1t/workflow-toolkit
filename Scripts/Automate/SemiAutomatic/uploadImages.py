import shutil
import os
from sys import argv
from ftplib import FTP
from hashlib import md5
from time import time

import configparser
config = configparser.ConfigParser()
config.read("settings.ini")

downloadPath = config["Filesystem"]["workdir"]

while True:
    try:
        print("Подключаемся к удалённому серверу...")
        ftp = FTP(host=config['FTP']['host'], timeout=600)
        ftp.port = 21
        ftp.login(user=config['FTP']['username'], passwd=config['FTP']['password'])
        print("Подключение успешно установлено!")
    except TimeoutError:
        print("Не удалось соединиться с сервером. Проверьте ваше подключение.")
        input("Попробовать подключиться снова?")
        continue
    break

def uploadImage(param):
    ftpUploader(param)

def ftpUploader(option):
    if option == "changes":
        dirPath = "OtherImages\\Changes\\"
        os.system("explorer "+downloadPath+dirPath)
        input("Загрузите файлы замен в директорию, после чего, нажмите Enter.")
        os.chdir(downloadPath+dirPath)
        for index, file in enumerate(os.listdir(downloadPath+dirPath)):
            if file.endswith(".jpg"):
                os.rename(file, "103b79ae27b2c177271584efe36286be.jpg")
                ftpstorBinary(dirPath, "103b79ae27b2c177271584efe36286be.jpg")
                shutil.move("103b79ae27b2c177271584efe36286be.jpg", "Stored\\103b79ae27b2c177271584efe36286be.jpg")
    if option == "vacancies":
        dirPath = "OtherImages\\Vacancies\\"
        constFileNames = ["8c99db44a6c67eb2fed348df9a193a61.jpg", "e8479276529b62721188f60537f538ac.jpg"]
        os.system("explorer "+downloadPath+dirPath)
        input("Загрузите файлы вакансий в директорию, после чего, нажмите Enter.")
        os.chdir(downloadPath+dirPath)
        for index, file in enumerate(os.listdir(downloadPath+dirPath)):
            if file.endswith(".jpg"):
                os.rename(file, constFileNames[index])
                ftpstorBinary(dirPath, constFileNames[index])
                shutil.move(constFileNames[index], "Stored\\"+constFileNames[index])
    if option == "other":
        dirPath = "OtherImages\\Other\\"
        os.system("explorer "+downloadPath+dirPath)
        input("Загрузите файлы в директорию, после чего, нажмите Enter.")
        os.chdir(downloadPath+dirPath)
        for index, file in enumerate(os.listdir(downloadPath+dirPath)):
            if file == "Stored":
                continue
            fileName = input("Новое имя для файла "+file+": ")
            if not fileName:
                fileName = file
                if input("Хешировать имя файла? (y/n):") == "y":
                    fileName = md5((file+str(time())).encode()).hexdigest()+"."+file.split(".")[1]
                    print("Файл будет загружен с именем: "+fileName)
            os.rename(file, fileName)
            ftpstorBinary(dirPath, fileName)
            shutil.move(fileName, "Stored\\"+fileName)
        
def ftpstorBinary(pathName, fileName):
    try:
        path = downloadPath+pathName
        print(f"\nОтправляем {fileName} на сервер...")
        with open(path+fileName, "rb") as ftpFile:
            ftp.storbinary("STOR "+fileName, ftpFile)
        print('Публикация: Файл успешно выгружен.')
    except FileNotFoundError:
        print("Публикация: Файл не найден.")
    except TimeoutError:
        print("При публикации файла произошла ошибка. Не установлено соединение с сервером.")
        
uploadImage(argv[1])