from getpass import getpass
import configparser
import os

config = configparser.ConfigParser()

if os.path.exists('settings.ini'):
    config.read("settings.ini")

print("Настраиваем файловую систему\n")
config['Filesystem'] = {
    "workdir" : str(input("Введите путь на рабочую директорию (C:\Example): ")) or config['Filesystem']['workdir'],
    "mgrfolder": str(input("Введите путь на директорию контент-менеджера (C:\Example): ")) or config['Filesystem']['mgrfolder']
}

print("\nНастраиваем File Transfer Protocol\n")
config['FTP'] = {
    "host": str(input("Введите хост (example.host.dev): ")) or config['FTP']['host'],
    "username": str(input("Введите имя пользователя (username): ")) or config['FTP']['username'],
    "password": str(getpass("Введите пароль (password): ")) or config['FTP']['password']
}

print("\nНастраиваем Web\n")
config['Web'] = {
    "uploadpath": str(input("Введите абсолютный путь к хранилищу файлов на сервере (http://example.dev/upload): ")) or config['Web']['uploadpath']
}

if not os.path.exists(config["Filesystem"]["workdir"]):
    os.makedirs(config["Filesystem"]["workdir"])
    
if not os.path.exists(config["Filesystem"]["mgrfolder"]):
    os.makedirs(config["Filesystem"]["mgrfolder"])

with open('settings.ini', 'w') as settings:
    config.write(settings)
    settings.close()
print("Конфигурационный файл успешно создан.")