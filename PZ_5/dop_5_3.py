#Написать программу, подсчитывающую количество цифр числа, используя для этого функцию.

def count_digits(k):
    """Возвращает количество цифр в целом числе."""
    k = abs(k)
    if k == 0:
        return 1
    count = 0
    while k > 0:
        k //= 10
        count += 1
    return count


int_number = input("Введите целое число: ")

while type(int_number) is not int:  # обработка исключений
    try:
        int_number = int(int_number)
    except ValueError:
        print("Неправильно ввели!")
        int_number = input("Введите целое число: ")

print("Количество цифр в числе:", count_digits(int_number))
