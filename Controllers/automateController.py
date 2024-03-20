import os
from Libs.logo import printLogo

def printAUMenu():
    os.system("cls")
    printLogo()
    print(open('./Sources/automate_menu.txt', 'r', encoding='utf-8').read())
    toolController(input("Инструмент: "))
    
def toolController(input):
    if (input == "0"):
        os.system("start cmd /k py .\\Scripts\\Automate\\automateChanges.py")
    if (input == "1"):
        os.system("start cmd /k py .\\Scripts\\Automate\\automateNews.py")
