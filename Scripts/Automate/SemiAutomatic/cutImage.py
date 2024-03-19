from Engine.cutImage import cutImages

dirPath = input("Введите имя директории относительно /Download: ")
xCount = int(input("Количество изображений по горизонтали: ")) or 1
yCount = int(input("Количество изображений по вертикали: ")) or 2

cutImages(xCount=xCount, yCount=yCount, dirPath=dirPath)