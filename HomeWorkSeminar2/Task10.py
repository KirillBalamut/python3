"""
    На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
    чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
"""

import random
from random import randint



try: 
    amount_coin = int(input('введите количество монет: '))
except:
    print("Ввели неверные данные")
print()

eagle = 0
tails = 0
coins = [0, 1]
for i in range(amount_coin):
    random.shuffle(coins)
    print(f'все монеты{coins}')
    if int(coins[0]) == 0:
        tails += 1
    if int(coins[0]) == 1:
        eagle+= 1
print()

print(f'количество монет выпавшик гербом: {eagle}, количество монеты выпавшие решкой: {tails}')
if eagle > tails:
    answer = tails
else:
    answer = eagle
print()
print(f"минимальное количество монет, которые нужно перевернуть:   {answer}")