import random


def rndm_lst(a, b, c):
    lst = []
    for i in range(a):
        lst.append(random.randint(b, c))
    print(lst)
    return lst


def fnd_ndx(my_list, number):
    if number in my_list:
        print(f"You number index will be {abc.index(find_index)}")
    else:
        print("This number not in list!")


length_list = int(input("Write length of your list?: "))
first_number_list = int(input("From what number will began your list?: "))
second_number_list = int(input("Number of the end of your list?: "))
abc = rndm_lst(length_list, first_number_list, second_number_list)

find_index = int(input("What index of number your want to find?: "))
fnd_ndx(abc, find_index)



#Со списками познакомились. Пора бы и начать делать с ними некие операции, как считаете?
#Сгенерируйте случайных список натуральных чисел до 10 включительно. После этого, создайте функцию, которая будет искать конкретное число в этом списке и выводить в консоль его номер по порядку.
#Например, есть список в[1,5,7,6,1,10,8,3,9,4] котором мы хотим найти чсило "6". Результатом поиска должно быть сообщение в консоль формата "число 6 находится в списке под номером 3". Мы ведь знаем, что в программировании отсчет стартует с 0, верно?
