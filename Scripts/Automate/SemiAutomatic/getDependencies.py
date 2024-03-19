import os

os.chdir('./')

dependencies = open("dependencies.lst", "r").read().splitlines()

for dependency in dependencies:
    print(f"Устанавливаем зависимость {dependency}")
    os.system(f"pip install {dependency}")
    
input("Установка зависимостей завершена. Нажмите Enter, чтобы завершить работу с зависимостями.")