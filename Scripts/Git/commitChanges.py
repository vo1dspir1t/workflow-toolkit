import os
from changeVersion import projectVersion

types = ['Refactoring', 'Feature', 'Changes', 'Hotfix']

print('\nПечатаем статус Git')
os.system('git status')
changeType = projectVersion()
print('\nДобавляем все файлы для коммита\n')
os.system('git add --all')
os.system('git commit -m "[WFT] {}: {}"'.format(types[changeType], input("Сообщение коммита: ").replace("\"", "\'")))
print('\nКоммит создан успешно.')
os.system('pause')
