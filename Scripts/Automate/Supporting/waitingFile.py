import os
import time
from itertools import count
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")

def waitingFile(fileExt: str = "docx", path: str = config['Filesystem']['workdir']):
    
    msg = [
        f"Ожидаем файл *.{fileExt} .*..",
        f"Ожидаем файл *.{fileExt} ..*.",
        f"Ожидаем файл *.{fileExt} ...*",
        f"Ожидаем файл *.{fileExt} *..."
    ]

    for index in count(3, 1):
        os.system("cls")
        print(msg[index % 4])
        for file in os.listdir(path):
            if file.endswith(fileExt):
                if input(f"Файл найден. ({file}) Начать с ним работать? ") in ["y", "yes"]:
                    print("Начинаем работать с файлом...")
                    time.sleep(3)
                    return file
        time.sleep(1.5)