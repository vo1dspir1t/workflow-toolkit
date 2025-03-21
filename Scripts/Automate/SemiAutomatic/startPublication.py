import os
from configparser import ConfigParser
from datetime import date
from shutil import move

config = ConfigParser()
config.read("settings.ini")

path = config['Filesystem']['mgrfolder']+"Web\\{0}\\{1}\\Ready\\".format(date.today().strftime("%B"), date.today().strftime("%d.%m"))

os.chdir(config['Filesystem']['mgrfolder']+"Web\\")
os.system("explorer story.xlsx")

os.chdir(path)

for dir in os.listdir():
    if os.path.isdir(dir) and dir != "Stored":
        os.system("explorer {0}\\Layout\\Макет.txt".format(dir))
        input("Нажмите Enter, чтобы перейти к следующей новости")
        move(dir, "Stored")

print("Все новости успешно обработаны!")