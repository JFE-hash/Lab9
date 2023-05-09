in_file = open('en-ru.txt', 'r', encoding='UTF-8').readlines()
out_file = open('ru-en.txt', 'w', encoding='UTF-8')
rus_en = []
for i in in_file:
    words = i.rstrip('\n')
    words = words.split(' - ')
    rus_en.append(f'{words[1]} - {words[0]}')
for i in sorted(rus_en):
    out_file.writelines(i + '\n')
