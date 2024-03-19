import os
from changeVersion import projectVersion

types = ['Refactoring', 'Feature', 'Changes', 'Hotfix']

changeType = projectVersion()
print('\nПечатаем статус Git')
os.system('git status')
print('\nДобавляем все файлы для коммита\n')
os.system('git add --all')
os.system(f'git commit -m "[WFT] {types[changeType]}: {input("Сообщение коммита: ")}"')
print('\nКоммит создан успешно.')
os.system('pause')
