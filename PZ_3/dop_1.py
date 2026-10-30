#Условие: Ввести 2 числа. Если их произведение отрицательно, умножить его на 8, в противном случае увеличить его в 1.5 раза.

a, b = input("Введите первое число: "), input("Введите второе число: ")

while type(a) != int and type(a) != float:  # обработка исключений
    try:
        if "." in a:
            a = float(a)
        else:
            a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите первое число: ")

while type(b) != int and type(b) != float:  # обработка исключений
    try:
        if "." in b:
            b = float(b)
        else:
            b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите второе число: ")

product = a * b

if product < 0:
    product *= 8
else:
    product *= 1.5

print("Результат =", product)