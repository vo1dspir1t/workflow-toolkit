def projectVersion():
    print("\n[0]: Major - крупные изменения, либо изменения несовместимые с предыдущей версией;\n[1]: Minor - добавление функционала без нарушения совместимости;\n[2]: Maintenance - исправления.")
    changesType = int(input("Тип изменений: ").strip() or "2")

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