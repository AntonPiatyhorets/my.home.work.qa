def while_we_together(a, b, c):
    while a < b:
        a += c
        print(f'Number {a} don\'t bigger than {b}')
    print(f'Finally your first number began bigger than {b}')


first_number = int(input("Write first number: "))
second_number = int(input("Write second number: "))
third_number = int(input("Write third number: "))
while_we_together(first_number, second_number, third_number)


#Пора познакомиться с радостью познания while, потому что все циклично!
#Создаем функцию, которая будет принимать три аргумента (а,б,в).
#Фуункция сравнивает А и Б. Если А меньше Б, то функция прибавляет А к В и повторно сравнивает А и Б. Цикл повторяется до тех пор, пока А не станет больше, чем Б.
#Когда А станет больше, чем Б - в консоль вывести следующую информацию:
#Все результаты сравнения А и Б
#Финальный результат с каким-то радостным текстом!
