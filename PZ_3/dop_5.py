#Дано два числа. Если их сумма кратна 5, то прибавить 1, иначе вычесть 2.

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

total_sum = a + b

if total_sum % 5 == 0:
    total_sum += 1
else:
    total_sum -= 2

print("Результат =", total_sum)