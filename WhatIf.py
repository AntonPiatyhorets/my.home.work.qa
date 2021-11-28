def calc_function(a, b):
    if first_number > second_number:
        print(f'Your first number [{first_number}] bigger than your second number [{second_number}]')
    elif first_number < second_number:
        print(f'Your first number [{first_number}] smaller than your second number [{second_number}]')
    else:
        print(f'Your first number [{first_number}] equal to your second number [{second_number}]')


first_number = int(input('Write first number: '))
second_number = int(input('Write second number: '))

calc_function(first_number, second_number)

1

#Вы задумывались, а что если?..
 
#Необходимо познакомиться с прекрасным IF!
#Пишем функцию, которая будет принимать два аргумента (а, б).
#Функция сравнивает А с Б. Если А больше, то функция выводит сообщение: А больше.
#Если А меньше Б - сообщени, что А меньше
#Если аргументы равны - сообщение об этом
