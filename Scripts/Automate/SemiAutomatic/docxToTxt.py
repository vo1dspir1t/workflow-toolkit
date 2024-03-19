import os
from Engine.docxToTxt import convertDocToTxt

dirPath = ""

userPath = input("Введите вашу директорию или пропустите ввод: ")
if not userPath:
    dirPath = input("Введите имя директории относительно /Downloads: ")
    
filename = ""

if dirPath: 
    path = dirPath 
else: 
    path=userPath 

for file in os.listdir(path):
    if file.endswith("docx"):
        isThisFile = input(f"{file} искомый файл? (Yes/No/Custom): ")
        if isThisFile in ["y", "yes"]:
            filename = file.split(".")[0]
            break
        elif isThisFile in ["c", "custom"]:
            break
            
if not filename:
    filename = input("Введите имя документа (.docx): ")

convertDocToTxt(dirPath=dirPath, fileName=filename, userPath=userPath)