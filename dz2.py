# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет,
# которые нужно перевернуть


import random
n = int(input('введите число монеток: '))
count = 0
k = 0
for i in range(n):
    p = random.randint(0,1)
    print(p, end = ' ')
    if p == 1:
        count += 1
    else: k += 1
if count <= k:
    print(f'\nМинимальное число монеток, которые нужно перевернуть {count}')
else:
    print(f'\nМинимальное число монеток, которые нужно перевернуть {k}')


# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.


s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))
d = s **2 - 4*1*p
y =(s + (s **2 - 4*1*p)**0.5)/2
x = s - y
print(f'x = {x}, y = {y}')


# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.


n = int(input("Введите число: "))
i = 1
while i < n:
    print(i, end =' ')
    i *= 2