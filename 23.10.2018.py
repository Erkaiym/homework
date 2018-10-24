#Задание 1
import random
print('Добро пожаловать в игру "Пятерка"!')
print('Попытайтесь угадать число от 1 до 20, загаданное Пятеркой. У Вас будет 5 попыток.')

right_number = random.randint(1, 20)
num_guesses = 0

while num_guesses < 5:
    user_guess = int(input('Введите число: '))
    num_guesses += 1
        if user_guess == right_number:
            print('Вам сопутствует удача! Вы угадали c ' + str(num_guesses) + ' попытки, получите приз.')
            break
        elif user_guess > 20:
	    print('Cлишком много.')
	elif user_guess < 1:
	    print('Cлишком мало.')
	else:
	    print('Ответ неверный.')
print('Игра завершена. Правильное число: ' + str(right_number) + '.')

#Задание 2
class Student:
    def __init__(self, name, lastname, department, year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance

    def get_student_info(self):
        return f'{self.name} {self.lastname} поступил в {self.year_of_entrance} году на факультет: {self.department}'


user1 = Student('Василий', 'Иванов', 'Программирование', 2017)
user2 = Student('Владимир', 'Путин', 'Межународное право', 1970)

print(user1.get_student_info() + '\n' + user2.get_student_info())

#Задание 3
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70

    def drive(self, distance):
    	self.odometer += distance
    	if self.odometer <= (self.fuel * 10):
    	    print('Let’s drive!')
    	    self.__add_distance(0)
    	    self.__subtract_fuel(0)
    	else:
    	    print('Need more fuel, please, fill more!')
        
    def __add_distance(self, distance):
    	self.odometer += distance

    def __subtract_fuel(self, fuel):
    	self.fuel -= (self.odometer / 10)

example = Car('Acura', 'MDX', 2017)
print('Значение одометра - ' + str(example.odometer) + ' км, количество бензина - ' + str(example.fuel) + ' литров')
example.drive(int(input('Type the distance: ')))
print('Значение одометра - ' + str(example.odometer) + ' км, количество бензина - ' + str(example.fuel) + ' литров')
