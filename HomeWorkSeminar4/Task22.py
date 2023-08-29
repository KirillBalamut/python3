#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n – кол – во элементов первого  множества. m – кол – во элементов второго множества.
#Затем пользователь вводит сами элементы множеств. (Попробуйте использовать множества и их пересечение).
"""
n=(int(input("Введите количество чисел в первом списке: ")))
NumberList1=[]
for i in range(n):
    num = (int(input("Введите числo через enter: ")))
    NumberList1.append(num)



m=(int(input("Введите количество чисел в втором списке: ")))
NumberList2 = []
for i in range(m):
    num = (int(input("ведите числo через enter: ")))
    NumberList2.append(num)
    
print()
print(NumberList1)
print ()
print(NumberList2)

NumberList3 = NumberList1+NumberList2
checked_nums_list = []
for i in set(NumberList3):
    if NumberList3.count(i) > 1:
        print (i, end=' , ')
"""
from random import randint
NumberList1 = set (randint(1, 20) for i in range(int(input("Введите кол-во элементов первого множества: "))))
print(NumberList1)
NumberList2 = set(randint(1, 20) for i in range(int(input("Введите кол-во элементов второго множества: "))))
print(NumberList2)
SortedList = sorted(NumberList1.intersection(NumberList2))
print(SortedList)