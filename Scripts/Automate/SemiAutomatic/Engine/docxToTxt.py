import docx2txt
import os

import configparser
config = configparser.ConfigParser()
config.read("settings.ini")

def convertDocToTxt(
    dirPath = "",
    fileName = "",
    userPath = ""
):
    path = config["Filesystem"]["workdir"]
    if dirPath:
        dirPath += "\\"
    if userPath:
        fullPath = userPath+"\\"
    else:
        fullPath = path+dirPath

    docxFilename = fullPath+fileName+".docx"
    txt = docx2txt.process(docxFilename)
    with open(fullPath+fileName+".txt", "wb") as file:
        file.write(txt.encode())
        file.close()
    print("Конвертирование файла завершено. Отредактируйте файл, после чего, работа программы будет завершена.")
    os.system(f'"%s.txt"' %(fullPath+fileName))