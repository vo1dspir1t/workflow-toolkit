import os
from shutil import move
from PIL import Image

import configparser
config = configparser.ConfigParser()
config.read("settings.ini")

path = config['Filesystem']['workdir']+"ConvertDocs\\"


os.chdir(path)

image = ""

os.system(f'explorer .')
input("Загрузите необходимые изображения в директорию и нажмите Enter.")

for file in os.listdir():
    if file.endswith("jpg"):
        isThisFile = input(f"{file} искомый файл? (Yes/No/Custom): ")
        if isThisFile in ["y", "yes"]:
            image = file
            break
        elif isThisFile in ["c", "custom"]:
            break
        
if not image:
    image = input("Введите имя изображения (.jpg): ")+".jpg"

fileName = image.split(".")[0]

if not os.path.exists("Output\\{0}\\".format(fileName)):
    os.mkdir("Output\\{0}\\".format(fileName))

Image.open(image).save("Output\\{0}\\{0}.pdf".format(fileName), "pdf")

if os.path.exists("Moved\\"+file):
    os.remove("Moved\\"+file)
move(image, "Moved\\")

print("Конвертация изображения завершена!")
os.system("explorer Output\\{0}\\".format(fileName))