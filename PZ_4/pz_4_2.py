#Условие: Дано целое число N (>1). Найти наименьшее целое число K, при котором выполняется неравенство 3^K > N.
n = input("Введите целое число N (>1): ")
while type(n) != int: # обработка исключений
    try:
        n = int(n)
        if n <= 1:
            print("Число должно быть больше 1!")
            n = input("Введите целое число N (>1): ")
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите целое число N (>1): ")
k = 0
power_of_three = 1
while power_of_three <= n:
    power_of_three *= 3
    k += 1

print("Наименьшее целое число K:", k)
print(f"Проверка: 3^{k} = {power_of_three}, что больше {n}")
