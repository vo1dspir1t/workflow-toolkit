import os
from shutil import move
from datetime import date
from configparser import ConfigParser

config = ConfigParser()
config.read("settings.ini")

os.chdir(config['Filesystem']['mgrfolder'])

userFolder = input("Введите название директории: ")

os.makedirs('temp\\{0}\\Images'.format(userFolder))
os.system('explorer temp\\{0}'.format(userFolder))
input("Заполните данную директорию контентом, после чего нажмите Enter.")

move(f'temp\\{userFolder}', 'Web\\{0}\\{1}'.format(date.today().strftime("%B"), date.today().strftime("%d.%m")))
os.rmdir('temp')
print("Директория успешно размещена в каталоге новостей!")