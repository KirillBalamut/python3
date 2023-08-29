"""
    Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его 
list_1 = [1, 2, 3, 4, 5]
k = 6
# 5
"""
list_1 = [1, 2, 3, 4, 5]
k = 6
ans = list_1[0]
for elem in list_1:
    if abs(elem-k)<abs(ans-k):
        ans = elem
#print(f'самое ближайшее число: {ans}')
print(ans)


m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
#print(f'самое ближайшее число: {number}')
print (number)