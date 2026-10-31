#Условие: Дано целое число N (>0). Найти произведение 1.1 \cdot 1.2 \cdot 1.3 \cdot \dots (N сомножителей).
n = input("Введите целое число N (>0): ")
while type(n) != int: # обработка исключений
    try:
        n = int(n)
        if n <= 0:
            print("Число должно быть больше 0!")
            n = input("Введите целое число N (>0): ")
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите целое число N (>0): ")

product = 1.0
current_factor = 1.1
i = 1

while i <= n:
    product *= current_factor
    current_factor += 0.1
    i += 1
print("Произведение равно:", product)
