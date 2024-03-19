from subprocess import Popen
import os

import configparser
config = configparser.ConfigParser()
config.read("settings.ini")

def openNewsHistory():
    os.chdir(config['Filesystem']['mgrfolder'])

    for file in os.listdir():
        if file.endswith("xlsx"):
            Popen(['explorer', file])
            
path = input("Ссылка на корневую директорию новости: ")+"/"

filename = ""

for file in os.listdir(path):
    if file.endswith("txt"):
        isThisFile = input(f"{file} искомый файл? (Yes/No/Custom): ")
        if isThisFile in ["y", "yes"]:
            filename = file
            break
        elif isThisFile in ["c", "custom"]:
            break
            
if not filename:
    filename = input("Имя файла: ")+".txt"

content = ""
symbols = ['«', '»']

retryLimit = 5

try:
    with open(path+filename, 'r', encoding="utf-8") as file:
        text = file.readlines()
        line_count = sum(1 for line in text)
        for index, line in enumerate(text):
            if (index == line_count-1):
                content += "<p style='text-align: right;'><strong><i>"+line.strip()+"</i></strong></p><br>"
            elif len(line.strip()) > 0:
                content += "<p style='text-align: justify;'>&ensp;&ensp;&ensp;&ensp;&ensp;"+line.strip()+"</p>"
    file.close()
except FileNotFoundError:
    print("Неверно указано имя файла или директория.")
    exit()

for symbol in symbols:
    content = content.replace(symbol, '"')

print("На данном этапе Вы можете добавить таблицу с изображениями.")
print("y - Да (по умолчанию)")
print("n - Нет")
insertTable = input("Добавить?: ")

if insertTable == "y" or insertTable == "":
    for retryCount in range(0, retryLimit):
        try:
            with open(path+'Images/table.txt', 'r') as tableFile:
                table = tableFile.read()
            content += table
            break
        except FileNotFoundError:
            print("Добавить таблицу невозможно. Возможно, она ещё не сформирована?")
            scriptImagesUploading = input("Хотите запустить скрипт загрузки изображений? [y/n]: ")
            if scriptImagesUploading == "y" or scriptImagesUploading == "":
                os.system('cls')
                os.system(f'py ./Scripts/Automate/SemiAutomatic/images4news.py "{path}"')
            else:
                break
    
with open(path+'Макет.txt', 'w', encoding='utf-8') as textFile:
    textFile.write(content)
textFile.close()

print("Создание макета завершено.")
openNewsHistory()
Popen(['explorer', path+"Макет.txt"])
input("Нажмите Enter чтобы закончить выполнение скрипта.")