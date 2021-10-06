import random

def rndm_lst(a, b, c):
    lst = []
    for i in range(a):
        lst.append(random.randint(b, c))
    print(lst)


length_list = int(input("Write length of your list?: "))
first_number_list = int(input("From what number will began your list?: "))
second_number_list = int(input("Number of the end of your list?: "))

rndm_lst(length_list, first_number_list, second_number_list)



#Давайте позгнакомимся со списками?
 
#Но не просто так, а путем генерации случайных чисел!
#Необходимо написать функцию, которая будет принмать аргументы (подумайте о том, сколько их нужно!) на основаниии которых она будет генерировать случайный список!
#По умолчанию, я бы хотел, чтобы список был из натуральных числел до девятки, плюс ноль (0-9) и в длину - 10 символов.
#Результат выводим в консоль.


