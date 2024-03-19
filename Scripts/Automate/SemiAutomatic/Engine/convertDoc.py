import os
from docx2pdf import convert
from shutil import move
from pdf2image import convert_from_path

import configparser
config = configparser.ConfigParser()
config.read("settings.ini")

def convertDocument(
    mode="semi",
    fileType = "1",
    docxFile = "",
    fileMode = "docx"
    ):
    
    path = config["Filesystem"]["workdir"]+"ConvertDocs\\"

    if mode == "semi":
        os.system("explorer "+path)
        input("Загрузите файл в директорию, после чего, нажмите Enter")

        for file in os.listdir(path):
            if file.endswith(fileMode):
                isThisFile = input(f"{file} искомый файл? (Yes/No/Custom): ")
                if isThisFile in ["y", "yes"]:
                    docxFile = file
                    break
                elif isThisFile in ["c", "custom"]:
                    break
                    
        if not docxFile:
            docxFile = input("Введите имя документа (docx/pdf): ")+".docx"
        
        if fileMode == "docx":
            print('[0]: pdf\n[1]: jpg')
            fileType = input("Выберите конечный файл: ") or "0"
    
    if fileMode == "docx":
        convert(path+docxFile)
    
    if (fileType == "0"):
        if fileMode == "docx":
            if os.path.exists(path+"Moved\\"+docxFile):
                os.remove(path+"Moved\\"+docxFile)
            move(path+docxFile, path+"Moved\\")
        if os.path.exists(path+"Output\\"+docxFile.split(".")[0]+".pdf"):
            os.remove(path+"Output\\"+docxFile.split(".")[0]+".pdf")
        move(path+docxFile.split(".")[0]+".pdf", path+"Output\\")
        if mode == "semi":
            input("Конвертирование завершено. Нажмите Enter, чтобы закончить работу.")
            os.system("explorer "+path+"Output\\")
        exit()
        
    images = convert_from_path(path+docxFile.split(".")[0]+".pdf", poppler_path="Libs\\poppler\\Library\\bin")
    
    if not os.path.isdir(path+"Output\\"+docxFile.split(".")[0]):
        os.mkdir(path+"Output\\"+docxFile.split(".")[0])

    for i in range(len(images)):
        images[i].save(path+"Output\\"+docxFile.split(".")[0]+'\\page_'+ str(i) +'.jpg', 'JPEG')
    
<<<<<<< HEAD
    if os.path.exists(path+"Moved\\"+docxFile):
        os.remove(path+docxFile)
    move(path+docxFile, path+"Moved\\")
    
    if os.path.exists(path+"Output\\"+docxFile.split(".")[0]+".pdf"):
        os.remove(path+docxFile.split(".")[0]+".pdf")
=======
    if fileMode == "docx":
        if os.path.exists(path+"Moved\\"+docxFile):
            os.remove(path+"Moved\\"+docxFile)
        move(path+docxFile, path+"Moved\\")
    
    if os.path.exists(path+"Output\\"+docxFile.split(".")[0]+".pdf"):
        os.remove(path+"Output\\"+docxFile.split(".")[0]+".pdf")
>>>>>>> ffa0460cde0c28e06b58e61b372994c66188aed9
    move(path+docxFile.split(".")[0]+".pdf", path+"Output\\")
        
    if mode == "semi":
        input("Конвертирование завершено. Нажмите Enter, чтобы закончить работу.")
        os.system("explorer "+path+"Output\\"+docxFile.split(".")[0])