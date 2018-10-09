#08.10.2018
print('Задача № 1')
numbers = [1, 4, 8, 10, 25]
new_numbers = []
for x in numbers:
    if x % 2 == 0:
        new_numbers.append(x*10)

print('исходный список ' + str(numbers))
print('преобразованный список ' + str(new_numbers))

print('\nЗадача № 2')
menu = {
    'beefstrogonoff': 350,
    'burger': 200,
    'meatloaf': 500,
    'chicken pot pie': 400,
    'beefshteks': 650}

new_menu = {k : v + 50 for (k, v) in menu.items()}

print('старое меню ' + str(menu))
print('обновленное меню ' + str(new_menu))

print('\nЗадача № 3')
from my_module import average
a = float(input('Введите первое число: '))
b = float(input('Второе число: '))
c = float(input('Третье число: '))
d = float(input('Четвертое число: '))
e = float(input('Пятое число: '))

print('Среднее арифметическое от введенных чисел составяет ' + str(average(a, b, c, d, e)))
