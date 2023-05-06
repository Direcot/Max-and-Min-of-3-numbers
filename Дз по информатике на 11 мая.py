#Вводим переменные
a = float(input("Введите первое число:"))
b = float(input("Введите второе число:"))
c = float(input("Введите третье число:"))
max = a
min = a
#Ищем наибольшее из чисел
if b < a > c:
    max = a
if a < b > c:
    max = b
if a < c > b:
    max = c
#Ищем наименьшее из чисел
if b > a < c:
    min = a
if a > b < c:
    min = b
if a > c < b:
    min = c
#Выводим результат
print("Максимальное из трёх чисел:", max)
print("Минимальное из трёх чисел:", min)