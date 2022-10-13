text ='Съешь ещё немного этих францухских булок'
#help(text.istitle)
#help(InterruptedError)
#print(len(text)) #  len показывает количество символов в тексте
#print('ещё' in text)# проверить наичие подстроки в строке использовать оператор in
#print(text.isdigit())# проверить являются ли все символы строки числами
#print(text.islower())# являются ли все символы строки символами нижнего регистра
#print(text.replace('ещё', 'ЕЩЁ'))# заменить что-то в тексте
#for c in text:
#    print(c)# вывести текст вертикально
#print(text[0]) #C
#print(text[1]) #Ъ
# print(text[len(text)]) # index error
#print(text[len(text)-1]) # k
#print(text[-5]) #б
#print(text[:]) # от первого до последнего символа, как от 0, len
#print(text[:])# если требуетсвзять символы от 2 до 5го, то можно написать [2:5]
#print(text[len(text)-2:])# ok
#print(text[2:9])# ешь ещё
#print(text[6:-18])# ещё немного этих
#print(text[0:len(text):6])# Семэрсу
#print(text[::6])# Семэрсу
#text = text[2:9] + text[-5] + text[:2]