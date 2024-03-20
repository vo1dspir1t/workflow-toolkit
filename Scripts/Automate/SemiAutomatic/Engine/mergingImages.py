import os
from PIL import Image

import configparser
config = configparser.ConfigParser()
config.read("settings.ini")

def mergeImages(
    mode = "semi",
    dirPath = "",
    direction = "y"
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
    
    if direction == "y":
        cortage = (width, height*(index+1))
    else:
        cortage = (width*(index+1), height)
        
    mergedImage = Image.new("RGB", cortage, "white")
    
    imageCounter = 0

    for image in os.listdir(fullPath):
        if image.endswith("jpg"):
            img = Image.open(fullPath+image)
            if direction == "y":
                mergedImage.paste(img, (0, height*imageCounter))
            else:
                mergedImage.paste(img, (width*imageCounter, 0))
            imageCounter += 1
            
    mergedImage.save(fullPath+'merged.jpg')
    print("Изображение успешно склеено")
    if mode == "semi":
        input("Нажмите Enter, чтобы завершить выполнение программы.")