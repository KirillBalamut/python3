'''
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума 
и не больше заданного максимума). Список можно задавать рандомно
На входе : [ 1, 5, 88, 100, 2, -4]
33
200
Ответ: [2, 3]
'''
import random

def Find_Index(list,min,max):
    index=[]
    for i in range(len(list)):
        if list[i]>= min and list[i]<= max:
            index.append(i)
    return index


def  Min():
    while type:
        min =  input (" Введите минимальное чиссло от 0-100:  ")
        try:
            getmin=int(min)
        except ValueError:
            print('Вы напечатали что-то другое')
        else:
            break
    return abs(getmin)
 
 
def Max():
    while True:
        max = input ("введите максимальное число от 0-100  ")
        try:
            getmax = int(max)
            
        except ValueError:
            print('Вы напечатали что-то другое')
        else:
            break
    return abs(getmax)




list = [random.randint(0,100)for _ in range(20)]
min = Min()
max = Max()

result = Find_Index(list,min,max)

print ("списсок :", list)
print ("минимальное значение: ", min)
print (" максимальное значчение: ", max)
print (f"индексы элементов принаделжащие диапазону : ", result )