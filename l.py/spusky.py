#  Списки введение.
# Список- пронумерованная, изменяемая коллекция объектов типов
#numbers = [1,2,3,4,5]
#print(numbers)
#ran = range(1,6)
#print(type(ran))
#numbers = list(ran) #  приведение типа range к типу list
#print(type(numbers))
#print(numbers) # [1,2,3,4,5]
#numbers[0] = 10
#print(f'{len(numbers)} len') # сколько элементов в списке с использованием интерполяции

#print(numbers)
#for i in numbers:
#    i *=2
#    print(i)
#print(numbers)    

#  Расширинный функционал

colors = ['red', 'green', 'blue']

for e in colors:
    print(e) # red green blue

for e in colors:
    print(e*2)  #redred greengreen blueblue

colors.append('gray') # довавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') # del colors[0] #  удалить элемент        













