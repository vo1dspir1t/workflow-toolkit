import os
from Libs.logo import printLogo
from Controllers.automateController import printAUMenu
from Controllers.semiController import printSAMenu
from Controllers.initializeController import printInitMenu
from configparser import ConfigParser

config = ConfigParser()
config.read("settings.ini")

def checkConfig():
    if not os.path.exists("settings.ini"):
        os.system('py .\\Scripts\\Automate\\initializeProject.py')
        os.system("pause")

def printMainMenu():
    checkConfig()
    os.system("cls")
    printLogo()
    print(open('./Sources/main_menu.txt', 'r', encoding='utf-8').read())
    print(f'\nВерсия продукта {open("version.ini").read()}\n')
    toolController(input("Инструмент: "))
    
def toolController(input):
    if input == "0":
        printSAMenu()
    if input == "1":
        printAUMenu()
    if input == "P":
        os.system(f'explorer .')
    if input == "M":
        os.system(f'explorer {config["Filesystem"]["mgrFolder"]}')
    if input == "O":
        os.system(f'explorer {config["Filesystem"]["workdir"]}')
    if input == "i":
        printInitMenu()
    if input == "C":
        os.system('start cmd /k py .\\Scripts\\Git\\commitChanges.py')
    if input == "R":
        os.system('.\\main.py')
        exit()
    if input in ["q", "Q"]:
        exit()
    printMainMenu()