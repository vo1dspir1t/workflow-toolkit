from shutil import make_archive
from configparser import ConfigParser
from datetime import datetime
from subprocess import Popen

import os

config = ConfigParser()
config.read("settings.ini")

if not os.path.exists(config['Filesystem']['workdir']+"Backups"):
    os.mkdir(config['Filesystem']['workdir']+"Backups")

os.chdir(config['Filesystem']['workdir']+"Backups")
print("Начинаем создавать архив...")
make_archive(f'Backup_{datetime.today().strftime("%d_%m_%Y_%H_%M")}', "zip", config['Filesystem']['mgrfolder'])
print("Бэкап успешно создан!")
Popen(['explorer', config['Filesystem']['workdir']+"Backups"])