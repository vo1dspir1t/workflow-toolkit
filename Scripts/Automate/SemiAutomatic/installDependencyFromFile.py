import os

def installDependency(number: int):
    os.system('pip install {}'.format(dependenciesList[number]))

def printListOfDependencies(index, dependencyName):
    print("[{}]: {}".format(index, dependencyName))

with open('dependencies.lst') as dependencies:
    dependenciesList = dependencies.read().split()
dependencies.close()

for index, dependencyName in enumerate(dependenciesList):
    printListOfDependencies(index, dependencyName)

installDependency(int(input("Установить зависимость: ")))