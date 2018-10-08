#05.10.2018
print('Задача № 1')

import math
def hypotenuse(a, b):
    return 'Hypotenuse of the right-angle triangle is equal to ' + str(math.sqrt( a ** 2 + b ** 2)) + ' cm'
a = float(input('Please, enter the length of the first cathetus: '))
b = float(input('Please, enter the length of the second cathetus: '))
print(hypotenuse(a, b))


print('\nЗадача № 2')

def sphere(r):
    return 'The volume of the sphere is equal to ' + str(4 / 3 * 3.14 * r **3) + ' cm\u00b3'
r = float(input('Please, enter sphere\'s radius: '))
print(sphere(r))

print('\nЗадача № 3')

def cube(a):
	return 'The volume of the cube is equal to ' + str(a ** 3) + ' cm\u00b3'
a = float(input('Please, enter cube\'s rib: '))
print(cube(a))


print('\nЗадача № 4')

def parallelepiped(a, b, c):
	return 'The volume of the parallelepiped is equal to ' + str(a * b * c) + ' cm\u00b3'
a = float(input('Please, enter the length of the first parallelepiped\'s side: '))
b = float(input('Please, enter the length of the second parallelepiped\'s side: '))
c = float(input('Please, enter the length of the third parallelepiped\'s side: '))
print(parallelepiped(a, b, c))


print('\nЗадача № 5')

def cylinder(r, h):
	return 'The volume of the parallelepiped is equal to ' + str(3.14 * r ** 2 * h) + ' cm\u00b3'
r = float(input('Please, enter the length of the cylinder\'s radius: '))
h = float(input('Please, enter the length of the cylinder\'s height: '))
print(cylinder(r, h))