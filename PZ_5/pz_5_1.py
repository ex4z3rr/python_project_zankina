# Составить функцию, которая напечатает сорок любых символов

def print_symbols(symbol):
    """Выводит на экран строку из 40 переданных символов."""
    print(symbol * 40)

user_symbol = input("Введите любой один символ: ")

while True:  # обработка исключений
    try:
        if len(user_symbol) != 1:
            raise ValueError
        break
    except ValueError:
        print("Неправильно ввели! Нужно ввести ровно один символ.")
        user_symbol = input("Введите любой один символ: ")

print("Результат: ", end="")
print_symbols(user_symbol)
