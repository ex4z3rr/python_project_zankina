#Рассчитать и вывести периметр и площадь прямоугольника. Расчеты оформить в функции

def rectangle_ps(width, height):
    """Вычисляет периметр и площадь прямоугольника."""
    perimeter = 2 * (width + height)
    area = width * height
    return perimeter, area


def input_positive_float(prompt):
    """Запрашивает положительное число с обработкой исключений."""
    while True:  # обработка исключений
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Неправильно ввели! Длина стороны должна быть больше нуля.")


a = input_positive_float("Введите длину прямоугольника: ")
b = input_positive_float("Введите ширину прямоугольника: ")

p, s = rectangle_ps(a, b)

print("Периметр прямоугольника:", p)
print("Площадь прямоугольника:", s)
