import os
from Libs.logo import printLogo
from Controllers.UIController import printUIMenu

def printSAMenu():
    os.system("cls")
    printLogo()
    print(open('./Sources/semiautomate_menu.txt', 'r', encoding='utf-8').read())
    toolController(input("Инструмент: "))
    
def toolController(input):
    if (input == "0"):
        os.system('start cmd /k py .\\Scripts\\Automate\\SemiAutomatic\\changes.py')
    if (input == "1"):
        os.system('start cmd /k py .\\Scripts\\Automate\\SemiAutomatic\\DOMFormatter.py')
    if (input == "2"):
        os.system('start cmd /k py .\\Scripts\\Automate\\SemiAutomatic\\createNewsDir.py')
    if (input == "3"):
        os.system('start cmd /k py .\\Scripts\\Automate\\SemiAutomatic\\startPublication.py')
    if (input == "4"):
        os.system('start cmd /k py .\\Scripts\\Automate\\SemiAutomatic\\mergingImages.py')
    if (input == "5"):
        os.system('start cmd /k py .\\Scripts\\Automate\\SemiAutomatic\\cutImage.py')
    if (input == "6"):
        os.system('start cmd /k py .\\Scripts\\Automate\\SemiAutomatic\\images4news.py')
    if (input == "7"):
        printUIMenu()
    if (input == "8"):
        os.system('start cmd /k py .\\Scripts\\Automate\\SemiAutomatic\\convertDoc.py')
    if (input == "9"):
        os.system('start cmd /k py .\\Scripts\\Automate\\SemiAutomatic\\docxtoTxt.py')
    if (input == "10"):
        os.system('start cmd /k py .\\Scripts\\Automate\\SemiAutomatic\\convertImage.py')
    if (input == "11"):
        os.system('start cmd /k py .\\Scripts\\Automate\\SemiAutomatic\\backupFolder.py')