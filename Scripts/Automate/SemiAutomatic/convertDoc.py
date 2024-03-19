from Engine.convertDoc import convertDocument

if input("Какой файл конвертировать? \n[0] Docx \n[1] PDF \nДокумент: ") == "1":
    mode = "pdf"
else:
    mode = "docx"
    
convertDocument(fileMode=mode)