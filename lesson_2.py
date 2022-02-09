# introduction to string
# Индексация и вырезание "кусочков" в строках
greeting = "Hello Python!" # строка - упорядоченная позиция символов (начинается с 0)
# len - длинна строки
greeting_lenght = len(greeting)
print(greeting_lenght)
print(len(greeting))
# Indexing
# получение первого элемента
print(greeting[0])
print(greeting[3])
print(greeting[6])
print(greeting[10])
# индекс с конца строки
print(greeting[-1])
print(greeting[-6])
print(greeting[12])
# Slicing - кусочки строк
print(greeting[2:5])
print(greeting[6:10])
print(greeting[-5:-2]) # нумерация в обратно порядке
print(greeting[2:]) # все что после этого символа
print(greeting[:5]) # выразание с начала строки до символа
print(greeting[:]) # вся строка нет смысла
print(greeting[::2]) # шаг пропуска, перескок
print(greeting[::3])
print(greeting[1::3])
print(greeting[1:10:2])
print(greeting[::-1]) #переворот строки

# HomeWork
#1 Выведите на печать вторую букву l из строки 'Hello Python!'Присвойте строку переменной, затем выведите на печать букву
tmp = "Hello Python!"
print(tmp[3])

#2 Выведите на печать вторую букву l из строки 'Hello Python!'Сделайте это без присваивания строки переменной, в одной строке кода. 
print("Hello Python"[3])

#3 Выведите на печать 'He' из строки 'Hello Python!' минимум двумя способами
tmp = "Hello Python!"
print(tmp[0:2])
print(tmp[-13:-11])
print(tmp[:2])
# print(tmp[0:2:1]) 
# print(tmp[:2:1])
# print(tmp[-13:-11:1])

#4 Создайте новую строку 'Path' из строки 'Hello Python!' путём конкатенации части строки и отсутствующего символа. 
# Выведите новую строку на печать
tmp = "Hello Python!"
print(tmp[6] + "a" + tmp[8:10])
