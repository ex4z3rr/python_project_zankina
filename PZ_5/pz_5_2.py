#Описать функцию SortInc3(A, B, C), меняющую содержимое переменных A, B, C таким образом, чтобы их значения оказались упорядоченными по возрастанию.
# С помощью этой функции упорядочить по возрастанию два данных набора из трех чисел: (A1, B1, C1) и (A2, B2, C2)

def SortInc3(a, b, c):
    """Упорядочивает значения трех переменных по возрастанию."""
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c

def input_float(prompt):
    """Запрашивает вещественное число с обработкой исключений."""
    value = input(prompt)
    while type(value) is not float:  # обработка исключений
        try:
            value = float(value)
        except ValueError:
            print("Неправильно ввели!")
            value = input(prompt)
    return value

print("Введите первый набор из трех чисел:")
a1 = input_float("Введите число A1: ")
b1 = input_float("Введите число B1: ")
c1 = input_float("Введите число C1: ")

print("\nВведите второй набор из трех чисел:")
a2 = input_float("Введите число A2: ")
b2 = input_float("Введите число B2: ")
c2 = input_float("Введите число C2: ")

a1, b1, c1 = SortInc3(a1, b1, c1)
a2, b2, c2 = SortInc3(a2, b2, c2)

print("\nУпорядоченный первый набор:", a1, b1, c1)
print("Упорядоченный второй набор:", a2, b2, c2)
