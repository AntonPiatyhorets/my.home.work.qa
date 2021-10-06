import random


def fnd_and_chng(a, b, c):
    lst = []
    for i in range(a):
        lst.append(random.randint(b, c))
    print(f'Your random list: {lst}')
    f_and_chg = int(input("Write index you want to change from [0] to [20]: "))
    lst[f_and_chg] = f_and_chg
    print(f'Your new list :{lst}')
    pass


fnd_and_chng(10, 0, 20)

# def fnd_and_chng(a):
#     lst = [int(i) for i in a]
#     print(lst)
#     f_and_chg = int(input("Write index you want to change: "))
#     lst[f_and_chg] = f_and_chg
#     print(lst)
#     pass
#
#
# u_number = input('Write your number: ')
# fnd_and_chng(u_number)




#Необходимо создать функцию, которая будет генерировать список, выводить его в консоль.
#После чего, просить пользователя ввести число от 0 до максимального значения спика (номера по порядку последнего элемента списка) и заменять этот элемент списка на введеное число.
#Пример:
#Сгенерирован список [1.4.5.84.145.7.5.64.14]
#Введено число 3
#"84" из списка заменяется на "3"
