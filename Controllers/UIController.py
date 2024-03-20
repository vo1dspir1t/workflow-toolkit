import os
from Libs.logo import printLogo

def printUIMenu():
    os.system("cls")
    printLogo()
    print(open('./Sources/upload_images_menu.txt', 'r', encoding='utf-8').read())
    toolController(input("Инструмент: "))
    
def toolController(input):
    if (input == "1"):
        os.system("start cmd /k py .\\Scripts\\Automate\\SemiAutomatic\\uploadImages.py changes")
    if (input == "2"):
        os.system("start cmd /k py .\\Scripts\\Automate\\SemiAutomatic\\uploadImages.py vacancies")
    if (input == "9"):
        os.system("start cmd /k py .\\Scripts\\Automate\\SemiAutomatic\\uploadImages.py other")