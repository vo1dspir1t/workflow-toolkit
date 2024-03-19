import os
from PIL import Image
import math

import configparser
config = configparser.ConfigParser()
config.read("settings.ini")

def cutImages(
  mode = "semi", 
  xCount = 1,
  yCount = 1,
  dirPath = ""
):
    path = config["Filesystem"]["workdir"]
    
    fullPath = path+dirPath+"\\"

    cutHeight = 0
    cutWidth = 0

    height = 0
    width = 0

    for image in os.listdir(fullPath):
        if image.endswith("jpg"):
            img = Image.open(fullPath+image)
            countParts = 0
            height = img.height
            width = img.width
            if not os.path.exists(fullPath+"Cutted"):
                os.mkdir(fullPath+"Cutted")
            cutHeight = math.floor(height / yCount)
            cutWidth = math.floor(width / xCount)
            for y in range(0, yCount):
                for x in range(0, xCount):
                    countParts += 1
                    cuttedImage = img.crop((x*cutWidth, y*cutHeight, x*cutWidth+cutWidth, y*cutHeight+cutHeight))
                    cuttedImage.save(fullPath+"Cutted\\"+image.split(".")[0]+"_"+str(countParts)+".jpg")

    if mode == "semi":
        os.system("explorer "+fullPath+"Cutted\\")
    print("Резка фотографий завершена.")
