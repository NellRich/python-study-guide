fffffffffffff
# lesson_1_input
print ("Hello world!") # команда для вывода данных в терминале - параметр передачи
print ("Yana Stupid, Yana Study") # в двойных скобках указывается строка
print('Hello!')
print (123)

# Интерпритируемый, объектно интерпритированный язык программирования (ООП), поддерживает множественное наследование
# Типы данных: строки, числа - строко типизированные
# Динамически типизированнные переменные

# lesson_2_data_types
print(2+2)
print(2-2)
print(2*2)
print(2/2)
print(2//2) # окургляющий оператор деления
print(2**3) # возведение в степень
print(5%3) # остаток от деления

#lesson_3_string
greeting = "Hello World!"
print(greeting)
first_name = "Jack"
last_name = "White"
space = " "
print (first_name + space + last_name)
long_string = "This is the long string"
print(long_string)
# Escaping
some_string = "I'm a programmer"
some_string = 'I\'m a programmer \n' # бэкслеш + перенос строки \n
another_string = 'I want to learn "Python"'
another_string = 'I want to learn \n  \r"Python"' # возвращает в начало строки \r
print(some_string + another_string)
print('1\t2\t3\t4\t5\t6\t7\t8\t9\t0') # табуляция для выравнивания  \t

#Triple quotes
tmp = """ This 'is' "text" """
tmp_1 = ''' This 'is' "text" '''
print(tmp + tmp_1)

#Homework
#1
name = "Yana"
surname = "Fokina"
age = "23"
space = " "
print("Hi! My name is" + space + name + space + surname + space + "\nI'm" + space + age + space + "years old.")

#2
print("""\t\tBaa, baa, black sheep,\n\t\tHave you any wool?\n\t\tYes sir, yes sir,\n\t\tThree bags full
\n\t\tOne for the master,\n\t\tOne for the dame,\n\t\tAnd one for the little boy\n\t\tWho lives down the lane
\n\t\tBaa, baa, black sheep,\n\t\tHave you any wool?\n\t\tYes sir, yes sir,\n\t\tThree bags full""")