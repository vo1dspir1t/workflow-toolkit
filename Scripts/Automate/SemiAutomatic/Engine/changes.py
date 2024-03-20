import os
import time
from shutil import move
from ftplib import FTP

import configparser
config = configparser.ConfigParser()
config.read("settings.ini")

def publishImage(path):
    
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

    try:
        print("Отправляем файл на сервер...")
        with open(path+"103b79ae27b2c177271584efe36286be.jpg", "rb") as file:
            ftp.storbinary("STOR 103b79ae27b2c177271584efe36286be.jpg", file)
        print('Публикация: Файл успешно выгружен.')
    except FileNotFoundError:
        print("Публикация: Файл не найден.")

def makeChanges(fileName):
    path = config["Filesystem"]["workdir"]

    try:
        move(path+fileName+'.jpg', path+'103b79ae27b2c177271584efe36286be.jpg')

        try:
            os.remove(path+fileName+'.docx')
        except FileNotFoundError:
            print("Удаление документа невозможно. Файл отсутствует.")

        print("Подготовка замен: Файл успешно сконвертирован.")

        publishImage(path)
        
    except FileNotFoundError:
        print("Подготовка замен: Файл не найден.")
    except PermissionError:
        print("Подготовка замен: Нет доступа для переименования файла.")

    time.sleep(3)