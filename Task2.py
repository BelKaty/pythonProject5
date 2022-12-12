#2) Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
#количества слов в каждой строке.

file = open("newfile.txt", "r", encoding='utf-8')
inform = file.readlines()
file.close()
print(f'Файла состоит из {len(inform)} строк(и).')

words_of_list = []

for i in range(len(inform)):
    list_element = inform[i].split()
    words_of_list.append(list_element)
    print(f'В строке {i + 1} - {len(words_of_list[i])} слов(о,а).')