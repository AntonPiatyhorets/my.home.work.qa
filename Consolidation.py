import random

def rndm_lst(a, b, c):
        lst1 = []
        lst2 = []
        for i in range(a):
            lst1.append(random.randint(b, c))
            lst2.append(random.randint(b, c))
        print(f'First list: {lst1}')
        print(f'Second list: {lst2}')

        lst3 = list(set(lst1) & set(lst2))
        print(f'New list with repeated index: {lst3}')


rndm_lst(10, -5, 15)



#Создать функцию, которая будет случайным образом генерировать два списка случайным образом, после чего сравнивать элементы этих двух списков и выводить в консоль новый список, который будет состоять из элементов, которые есть в обоих оригинальных списках.


