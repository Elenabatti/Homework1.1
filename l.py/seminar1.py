#Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
#*Примеры:*

#- 5, 25 -> да
#- 4, 16 -> да
#- 25, 5 -> да
#- 8,9 -> нет
#number1 = int(input('Введите первое число: '))
#number2 = int(input('Введите второе число: '))
#if number1 * 2== number2 or number2 * 2 == number1:
#    print('Yes')
#else:
#    print('NO')



#2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
#- 1, 4, 8, 7, 5 -> 8
#- 78, 55, 36, 90, 2 -> 90
#from sys import int_info

#number =int(input()) #  первое число вводится
#maxx = number  # говорим, что это максимум
#for i in range(4):  # если i больше не используем, то можно просто написать нижнее подчеркивание. Range  сщздаёт последовательности
#    number = int(input())
#    if number > maxx:
#        maxx = number
#print(maxx)        

# number = int(input())
# maxx = number
# for _ in range(4):
# number = int(input())
# if number > maxx:
# maxx = number
# print(maxx)
#
# some_list = []
# for _ in range(5):
# number = int(input())
# some_list.append(number)
# maxx = some_list[0]
# for element in some_list:
# if element > maxx:
# maxx = element
# print(maxx)

print(max(map(int, input().split())))



