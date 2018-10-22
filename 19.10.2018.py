#Задание № 1
class Car:
    def __init__(self, owner, make, model, year):
        self.owner = owner
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.is_going = False

    def go(self, distance):
        self.is_going = True
        self.odometer = self.odometer + distance
        print('Syezdili v Typ')

    def stop(self):
        self.is_going = False

bekzats_car = Car('Bekzat', 'Dodge', 'Charger', 2015)
print(f'{bekzats_car.make} {bekzats_car.model}')
print(bekzats_car.odometer, bekzats_car.is_going)
bekzats_car.go(500)
print(bekzats_car.odometer, bekzats_car.is_going)

#Задание № 2
class Airplane:
    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0
        self.is_flying = False

    def take_off(self):
    	self.is_flying = True

    def fly(self, distance):
    	self.is_flying = True
    	self.odometer = self.odometer + distance

    def land(self):
    	self.is_going = False

my_plane = Airplane('Airbus', 'Airbus A380', 2011, 1020)
print(my_plane.make, my_plane.model, my_plane.year, my_plane.max_speed)
print('Показатель одометра составляет: ' + str(my_plane.odometer))
my_plane.take_off()
my_plane.fly(2989) #Бишкек-Москва
my_plane.land()
print('Показатель одометра составляет: ' + str(my_plane.odometer))
