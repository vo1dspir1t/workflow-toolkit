import os
from PIL import Image

import configparser
config = configparser.ConfigParser()
config.read("settings.ini")

def mergeImages(
    mode = "semi",
    dirPath = ""
):
    downloadPath = config["Filesystem"]["workdir"]
    if not dirPath:
        fullPath = downloadPath
    else:
        fullPath = downloadPath+dirPath+"/"

    height = 0
    width = 0

    for index, imageParams in enumerate(os.listdir(fullPath)):
        if imageParams.endswith("jpg"):
            img = Image.open(fullPath+imageParams)
            height = img.height
            width = img.width
        
    mergedImage = Image.new("RGB", (width, height*(index+1)), "white")

    for image in os.listdir(fullPath):
        if image.endswith("jpg"):
            img = Image.open(fullPath+image)
            if (image[-5] == "0"):
                mergedImage.paste(img, (0, 0))
            else:
                mergedImage.paste(img, (0, height))
            
    mergedImage.save(fullPath+'merged.jpg')
    print("Изображение успешно склеено")
    if mode == "semi":
        input("Нажмите Enter, чтобы завершить выполнение программы.")