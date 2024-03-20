import os
from changeVersion import projectVersion

types = ['Refactoring', 'Feature', 'Changes', 'Hotfix']

print('\nПечатаем статус Git')
os.system('git status')
print('\nДобавляем все файлы для коммита\n')
os.system('git add --all')
changeType = projectVersion()
os.system(f'git commit -m "[WFT] {types[changeType]}: {input("Сообщение коммита: ")}"')
print('\nКоммит создан успешно.')
os.system('pause')
