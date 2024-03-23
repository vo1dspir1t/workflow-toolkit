import os

def printListOfDependencies(index, dependencyName):
    print("[{}]: {}".format(index, dependencyName))

def readDependenciesList():
    with open('dependencies.lst') as dependencies:
        return dependencies.read().split()
    
def installDependency():
    dependenciesList = readDependenciesList()
    [printListOfDependencies(index, dependencyName) for index, dependencyName in enumerate(dependenciesList)]
    number = int(input("Установить зависимость: "))
    print("Начинаем устанавливать {}...".format(dependenciesList[number]))
    os.system('pip install {}'.format(dependenciesList[number]))

installDependency()