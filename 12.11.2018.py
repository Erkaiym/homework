print('Задание 1\n')
from abc import ABC, abstractmethod

class Camera(ABC):
    @abstractmethod
    def shoot(self):
        print('Снято!')


class PhotoCam(Camera):
    def shoot(self):
        super().shoot()
        print('Фото сохранено!')


class VideoCam(Camera):
    def shoot(self):
        super().shoot()
        print('Видео сохранено!')

photo = PhotoCam()
video = VideoCam()
photo.shoot()
video.shoot()

print('\nЗадание 2\n')

class FarmAnimal(ABC):
    @abstractmethod
    def go_to_farm(self):
        print('go to the farm')


class Pig(FarmAnimal):
    def go_to_farm(self):
        super().go_to_farm()
        print('pigs')


class Dog(FarmAnimal):
    def go_to_farm(self):
        super().go_to_farm()
        print('dogs')


class Sheep(FarmAnimal):
    def go_to_farm(self):
        super().go_to_farm()
        print('sheep')


class Horse(FarmAnimal):
    def go_to_farm(self):
        super().go_to_farm()
        print('horse')


class Farmer:
    animals_to_gather = []
    def add_animal(self, pig_obj, dog_obj, sheep_obj, horse_obj):
        Farmer.animals_to_gather.append([pig_obj, dog_obj, sheep_obj, horse_obj])
        print('Животные собраны: ' + str(*Farmer.animals_to_gather)[1:-1])

    def __repr__(self):
        print(f'{self.go_to_farm}')


pig = Pig()
dog = Dog()
sheep = Sheep()
horse = Horse()
farmer = Farmer()

pig.go_to_farm()
dog.go_to_farm()
sheep.go_to_farm()
horse.go_to_farm()

farmer.add_animal(pig, dog, sheep, horse)


print('\nЗадание 3\n')

class Computer(ABC):
    @abstractmethod
    def connect_to_projector(self):
        print('Соединение проектора установлено')


class Laptop(Computer):
    def connect_to_projector(self):
        super().connect_to_projector()
        print('С ноутбуком')
        

class Desktop(Computer):
    def connect_to_projector(self):
        super().connect_to_projector()
        print('С компьютером')


class Projector:
    def connect(self, laptop_obj, desktop_obj):
        if isinstance(Laptop(), Laptop):
            laptop_obj.connect_to_projector()
            print('\nПроектор подсоединен к ноутбуку')
        else:
            print('Неверный тип для соединения')

laptop = Laptop()
desktop = Desktop()
projector = Projector()

desktop.connect_to_projector()
projector.connect(laptop, desktop)