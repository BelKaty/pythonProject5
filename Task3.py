#3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее
#10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить
#подсчет средней величины дохода сотрудников.
#Пример файла:
#Иванов 23543.12
#Петров 13749.32

def sal():
    sum = 0
    for i, j in dictionary.items():
        salary = float(j)
        sum += salary
        if salary < 20000:
            print(f'{i} - {j}')
    middle_salary = sum / len(dictionary)
    return middle_salary

file = open('salaryfile.txt', 'r', encoding='utf-8')
content = file.readlines()

dictionary = {}
for i in range(len(content)):
    j = content[i].split()
    dictionary.update({j[0]: j[1]})

print(f'Сотрудники, оклад которых менее 20 тыс:')
print(f'Средняя величина дохода среди всех сотрудников: {sal()}')

file.close()
