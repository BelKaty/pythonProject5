#4) Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
#числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

numbers = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
with open('numberfile.txt', 'r', encoding='utf-8') as file_one:
    for line in file_one:
        for key in numbers.keys():
            line = line.replace(key, numbers[key])
        with open('newnumberfile.txt', 'a', encoding='utf-8') as file_two:
            print(line, file=file_two)