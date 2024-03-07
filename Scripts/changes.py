import os
import time
from ftplib import FTP

def publishImage(path):
    ftp = FTP(host="ftp49.hostland.ru", timeout=300)
    ftp.login(user="host1335833_upload", passwd="larikanik_20062001")

    try:
        with open(path+"103b79ae27b2c177271584efe36286be.jpg", "rb") as file:
            ftp.storbinary("STOR 103b79ae27b2c177271584efe36286be.jpg", file)
        print('Публикация: Файл успешно выгружен.')
    except FileNotFoundError:
        print("Публикация: Файл не найден.")

fileName = input("Имя файла (.jpg): ")

path = "C:/Users/vo1dspirit/Downloads/"

try:
    os.rename(path+fileName+'.jpg', path+'103b79ae27b2c177271584efe36286be.jpg')

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