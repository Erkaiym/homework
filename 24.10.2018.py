#Задание 1
class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def get_phone_info(self):
        return f'Телефон {self.brand} {self.model} стоит {self.price} сомов.'

if __name__ == '__main__':
    print('Задание № 1')
    brand = input('Введите марку телефона: ')
    model = input('Введите модель телефона: ')
    try:
        price = input('Введите стоимость телефона: ')
    except ValueError:
        print('Вводите только цифры.')
    new_phone = Phone(brand, model, price)
    print(new_phone.get_phone_info())


#Задание 2
class CoffeeMachine:
    def __init__(self, coffee, sugar, milk):
        self.coffee = 1000
        self.sugar = 1000
        self.milk = 1000

    def __subtract_coffee(self, used_coffee):
            self.coffee -= used_coffee

    def __subtract_sugar(self, used_sugar):
            self.sugar -= used_sugar

    def __subtract_milk(self, used_milk):
            self.milk -= used_milk

    def make_coffee(self, used_coffee, used_sugar, used_milk):
        if self.coffee < used_coffee:
            print(f'Пополните запаса кофе на {used_coffee - self.coffee} гр.')
        if self.sugar < used_sugar:
            print(f'Пополните запаса сахара на {used_sugar - self.sugar} гр.')
        if self.milk < used_milk:
           print(f'Пополните запаса молока на {used_milk - self.milk} мл.')
        else:
            self.__subtract_coffee(used_coffee)
            self.__subtract_sugar(used_sugar)
            self.__subtract_milk(used_milk)
            print('Вот Ваш кофе! Приятного аппетита!')

if __name__ == '__main__':
    print('\nЗадание № 2\nКофемашина \'Melitta Caffeo Solo\' готова к старту!')
    try:
        coffee = int(input('Введите требуемое количество кофе: '))
        sugar = int(input('Введите требуемое количество сахара: '))
        milk = int(input('Введите требуемое количество молока: '))
    except ValueError:
        print('Вводите только числа!')
    drink = CoffeeMachine(coffee, sugar, milk)
    print('Кофемашина самостоятельно прогонит горячую воду под требуемым давлением, чтобы сделать для Вас чашечку бодрящего напитка. \nНо для начала...')
    print(drink.make_coffee(coffee, sugar, milk))