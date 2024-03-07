import os
from Libs.logo import printLogo

def printMMenu():
    print(open('./Sources/main_menu.txt', 'r', encoding='utf-8').read())

def printMainMenu():
    printLogo()
    printMMenu()
    toolController(input("Инструмент: "))
    
def toolController(input):
    os.system('cls')
    if (int(input) == 0):
        os.system('start cmd /k py .\Scripts\changes.py')
    if (int(input) == 1):
        os.system('start cmd /k py .\Scripts\imagesUploader.py')
    if (int(input) == 2):
        os.system('start cmd /k py .\Scripts\DOMFormatter.py')
    if (input == "q"):
        exit()
    printMainMenu()