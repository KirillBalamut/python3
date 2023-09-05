# Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input("введите число: "))
d1 = int(input("введите шаг: "))
n1 = int(input("введите количество элементов:"))

def Ar_Progress (a, d, n):
    i=0 
    print (a)
    for i in range(n-1):
        n= a+d
        print (n)
        a=n

ar_progress = Ar_Progress(a1, d1, n1)
print ( ar_progress)
    
for i in range(n1):
    print(a1 + i * d1, end=' ')
    
