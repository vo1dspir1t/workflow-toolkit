import os

import configparser
config = configparser.ConfigParser()
config.read("settings.ini")

path = config["Filesystem"]["workdir"]

os.chdir(path)

if not os.path.exists("Backups"):
    os.mkdir("Backups")
if not os.path.exists("ConvertDocs"):
    os.makedirs("ConvertDocs\\Moved")
    os.makedirs("ConvertDocs\\Output")
if not os.path.exists("OtherImages"):
    os.makedirs("OtherImages\\Changes\\Stored")
    os.makedirs("OtherImages\\Other\\Stored")
    os.makedirs("OtherImages\\Vacancies\\Stored")
    
print("Все директории успешно созданы!")