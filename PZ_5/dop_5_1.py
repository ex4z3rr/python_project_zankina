#Даны три целых числа. Определить, у какого числа больше сумма цифр.
#Вывод результата предусмотреть в основной программе. Расчет суммы цифр оформить в функции.

def digit_sum(number):
    """Возвращает сумму цифр целого числа."""
    number = abs(number)  # учитываем отрицательные числа
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total


def input_int(prompt):
    """Запрашивает целое число с обработкой исключений."""
    value = input(prompt)
    while type(value) is not int:  # обработка исключений
        try:
            value = int(value)
        except ValueError:
            print("Неправильно ввели!")
            value = input(prompt)
    return value


num1 = input_int("Введите первое целое число: ")
num2 = input_int("Введите второе целое число: ")
num3 = input_int("Введите третье целое число: ")

sum1 = digit_sum(num1)
sum2 = digit_sum(num2)
sum3 = digit_sum(num3)

max_sum = max(sum1, sum2, sum3)

if sum1 == sum2 == sum3:
    print(f"У всех трех чисел одинаковая сумма цифр: {max_sum}")
else:
    print(f"Наибольшая сумма цифр ({max_sum}) у числа(ел):", end=" ")
    if sum1 == max_sum:
        print(num1, end=" ")
    if sum2 == max_sum:
        print(num2, end=" ")
    if sum3 == max_sum:
        print(num3, end=" ")
    print()
