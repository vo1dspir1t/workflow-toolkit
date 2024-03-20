def projectVersion():
    print("\n[0]: Глобальные изменения\n[1]: Добавление функции\n[2]: Изменение функции\n[3]: Фикс ошибок")
    changesType = int(input("Тип изменений: ").strip() or "3")

    with open("version.ini", 'r+') as file:
        outdatedVersion = file.read().split(".")
        outdatedVersion[changesType] = str(int(outdatedVersion[changesType])+1)
        for number in range(changesType+1, len(outdatedVersion)):
            outdatedVersion[number] = "0"
        file.seek(0)
        file.write('.'.join(outdatedVersion))
    file.close()
    print("Версия приложения обновлена до {0}".format('.'.join(outdatedVersion)))
    return changesType