#5) Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
#подсчитывать сумму чисел в файле и выводить ее на экран.

file = open('sumnumbers.txt', 'w', encoding='utf-8')
sumnum = 0
import random
for i in range(10):
    rannum = random.randint(1, 100)
    sumnum += rannum
    file.write(f'{rannum} ')
file.close()

file = open('sumnumbers.txt', 'r+', encoding='utf-8')
list = file.read().split()
sumnum = 0
for item in list:
    sumnum += float(item)
print(f"Сумма чисел {list} в файле: ", sumnum)
file.write(f'Сумма этих чисел: {sumnum} ')
file.close()
