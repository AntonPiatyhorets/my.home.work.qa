def sumofindex(a):
    lst = [int(i) for i in a]
    print(lst)
    print(f'Sum of all index\'s in you number: [{sum(lst)}]')


u_number = input('Write your number: ')
sumofindex(u_number)


#Теперь интересное 
#необходимо написать функцию которая будет считать сумму элементов числа!
 
#Тоесть, Вы вводите в консоль число, например 213.
#Функция разбивает его на элементы: 2 + 1 + 3 и считает сумму! В нашем случае - 6.
#Ответ в консоль 
