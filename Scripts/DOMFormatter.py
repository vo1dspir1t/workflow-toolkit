import os

path = input("Ссылка на корневую директорию новости: ")+"/"
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
                content += "<p style='text-align: right;'><strong><i>"+line.strip()+"</i></strong></p>"
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
                os.system('py ./Scripts/imagesUploader.py')
            else:
                break
    
with open(path+'Макет.txt', 'w', encoding='utf-8') as textFile:
    textFile.write(content)
textFile.close()

print("Создание макета завершено.")
input("Нажмите Enter чтобы закончить выполнение скрипта.")