from shutil import copy, move
from SemiAutomatic.Engine.changes import makeChanges
from SemiAutomatic.Engine.convertDoc import convertDocument
from SemiAutomatic.Engine.mergingImages import mergeImages
from Supporting.waitingFile import waitingFile

import configparser
config = configparser.ConfigParser()
config.read("settings.ini")

path = config['Filesystem']['workdir']

foundFile = waitingFile(fileExt=input("По какому расширению файла ищем? (jpg/docx) :"), path=path).split(".")
    
fileName = foundFile[0]
fileExtension = "."
fileExtension += foundFile[1]

if fileExtension == ".jpg":
    makeChanges(fileName)
    exit()

try:
    copy(path+fileName+fileExtension, path+"ConvertDocs")
except FileNotFoundError:
    print("Не найден документ в директории /Downloads.")
    exit()

convertDocument("auto", docxFile=fileName+fileExtension)

mergeImages("auto", dirPath="ConvertDocs/Output/"+fileName)

move(path+"ConvertDocs\\Output\\"+fileName+"\\merged.jpg", path+fileName+".jpg")

makeChanges(fileName)