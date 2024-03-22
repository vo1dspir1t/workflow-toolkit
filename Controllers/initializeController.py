import os
from Libs.logo import printLogo

def printInitMenu():
    os.system("cls")
    printLogo()
    print(open('./Sources/initialize_menu.txt', 'r', encoding='utf-8').read())
    toolController(input("Инструмент: "))
    
def toolController(input):
    if (input == "0"):
        os.system('start cmd /k py .\\Scripts\\Automate\\SemiAutomatic\\getDependencies.py')
    if (input == "1"):
        os.system('start cmd /k py .\\Scripts\\Automate\\SemiAutomatic\\createFolders.py')
    if (input == "2"):
        os.system('start cmd /k py .\\Scripts\\Automate\\SemiAutomatic\\cleanDirectories.py')
    if (input == "3"):
        os.system('start cmd /k py .\\Scripts\\Automate\\SemiAutomatic\\createConfig.py')
    if (input == "F"):
        os.system('start cmd /k py .\\Scripts\\Automate\\initializeProject.py')
    if (input == "S"):
        os.system('start cmd /k py .\\Scripts\\Automate\\SemiAutomatic\\showConfig.py')
    if (input == "D"):
        os.system('start cmd /k py .\\Scripts\\Automate\\SemiAutomatic\\installDependencyFromFile.py')
    