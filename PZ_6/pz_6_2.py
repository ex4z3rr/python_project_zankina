#Дано число R и список A размера N.
# Найти элемент списка, который наиболее близок к числу R
# (то есть такой элемент AK, для которого величина |AK - R| является минимальной).
import random


while True:  # обработка исключений
    try:
        n = int(input("Введите размер списка N: "))
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        print("Неправильно ввели! N должно быть положительным целым числом.")

while True:  # обработка исключений
    try:
        r = float(input("Введите число R: "))
        break
    except ValueError:
        print("Неправильно ввели! Введите число.")

a = []
i = 0
while i < n:
    a.append(random.randint(-50, 50))
    i += 1

print("Исходный список:", a)

closest_element = a[0]
min_diff = abs(a[0] - r)

i = 1
while i < n:
    diff = abs(a[i] - r)
    if diff < min_diff:
        min_diff = diff
        closest_element = a[i]
    i += 1

print("Наиболее близкий к R элемент:", closest_element)
