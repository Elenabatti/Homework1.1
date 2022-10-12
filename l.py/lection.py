#  Управляющие конструкции
# if, if-else
# Задача нахождения максимума из 2х чисел
#a = int(input('a = '))
#b = int(input('b = '))
#if a > b:
 #   print(a)
#else:
 #   print(b)#
 #Это логический оператор. Используем при решении задач
#username = input('Введите имя: ')
#if username == 'Mary':
 #   print('Ура это Mary!')
#elif username == 'Марина':
 #   print(' Я ждал Вас Марина')
#elif username ==  'Ильнар':
 #   print ('Ильнар гуд')
#else:
 #   print ('Привет,', username)

 #Управляющие конструкции While
# Переворачиваем число
#original = 237
#inverted = 0
#while original !=0:
#    inverted = inverted *10 +(original % 10)
#    original //=10
#print(inverted)    
 # Конструкция while-else выполняется в том случае, когда основное тело перестаёт работать
original = 237
inverted = 0
while original !=0:
     inverted = inverted *10 +(original % 10)
     original //=10
else:
    print('Пожалуй \nхватит')
    #print('хватит')     
print(inverted)    