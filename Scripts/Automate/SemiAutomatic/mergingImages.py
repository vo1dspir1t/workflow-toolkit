from Engine.mergingImages import mergeImages

dir=input("Введите путь к директории с изображениями (относительно /Downloads): ")
direction = input("Склеить изображения по вертикали(y)/горизнотали(x)?: ") or "y"

mergeImages(dirPath=dir, direction=direction)