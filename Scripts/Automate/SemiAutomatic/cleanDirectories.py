import os
from shutil import rmtree

import configparser
config = configparser.ConfigParser()
config.read("settings.ini")

path = config["Filesystem"]["workdir"]

def clear(dirName):
    
    os.chdir(path+dirName)

    for dir in os.listdir():
        os.chdir(dir)
        for file in os.listdir():
            if os.path.isdir(file):
                if file != "Stored":
                    rmtree(file)
                else:
                    os.chdir(file)
                    for inFile in os.listdir():
                        if os.path.isdir(inFile):
                            rmtree(inFile)
                        else:
                            os.remove(inFile)
                    os.chdir("..")
            else:
                os.remove(file)
        os.chdir("..")
        
clear("ConvertDocs")
clear("OtherImages")
clear("Backups")

print("Все файлы из директорий успешно удалены!")