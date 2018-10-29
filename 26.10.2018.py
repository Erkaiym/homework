# Задание № 1
import datetime
class Birthday:
    def __init__(self, name, year, month, day):
        self.name = name
        self.year = year
        self.month = month
        self.day = day

    def get_age(self):
        birth_date = datetime.date(self.year, self.month, self.day)
        return datetime.date(2018, 12, 31).year - birth_date.year

    def __str__(self):
        return f'На момент 31 декабря 2018 года возраст {name} будет {self.get_age()}.'

if __name__ == '__main__':
    name = input('Введите имя: ')
    try:
        year = int(input('Введите год рождения (YYYY): '))
        month = int(input('Введите месяц рождения: '))
        day = int(input('Введите день рождения: '))
    except ValueError:
        print('Вводите только числа!')

    person = Birthday(name, year, month, day)
    print(person)


# Задание № 2
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        return f'Вам на счет поступило {self.amount} {self.currency}'

    def __str__(self):
        return f'Вам на счет поступило {self.amount} {self.currency}'

    def __add__(self, other_money):
        if self.currency != other_money.currency:
            return str(round(self.amount + other_money.amount / 69, 2)) + ' USD' if self.currency == 'USD' else str(self.amount + other_money.amount * 69) + ' KGS'
        else:
            return str(self.amount + other_money.amount) + self.currency

    def __sub__(self, other_money):
        if self.currency != other_money.currency:
            return str(round(self.amount - other_money.amount / 69, 2)) + ' USD' if self.currency == 'USD' else str(self.amount - other_money.amount * 69) + ' KGS'
        else:
            return str(self.amount - other_money.amount) + ' ' + self.currency

    def __lt__(self, other_money):
        if self.currency != other_money.currency:
            return self.amount < other_money.amount / 69 if self.currency == 'USD' else self.amount < other_money.amount * 69
        else:
            return self.amount < other_money.amount

    def __le__(self, other_money):
        if self.currency != other_money.currency:
            return self.amount <= other_money.amount / 69 if self.currency == 'USD' else self.amount <= other_money.amount * 69
        else:
            return self.amount <= other_money.amount

    def __ne__(self, other_money):
        if self.currency != other_money.currency:
            return self.amount != other_money.amount / 69 if self.currency == 'USD' else self.amount != other_money.amount * 69
        else:
            return self.amount != other_money.amount

    def __gt__(self, other_money):
        if self.currency != other_money.currency:
            return self.amount > other_money.amount / 69 if self.currency == 'USD' else self.amount > other_money.amount * 69
        else:
            return self.amount > other_money.amoun

    def __ge__(self, other_money):
        if self.currency != other_money.currency:
            return self.amount >= other_money.amount / 69 if self.currency == 'USD' else self.amount >= other_money.amount * 69
        else:
            return self.amount >= other_money.amount


if __name__ == '__main__':
    first = Money(100, 'USD')
    second = Money(10, 'USD')
    third = Money(50, 'KG')
    
    print(first)
    print('100 USD + 50 KG = ' + str(first + third), '; 50 KG + 10 USD = ' + str(third + second))
    print('100 USD - 10 USD = ' + str(first - second), '; 10 USD - 50 KG = ' + str(second - third))
    print('50 KGS < 100 USD ' + str(third < first) + '; 100 USD < 10 USD ' + str(first < second))
    print('100 USD <= 50 KGS ' + str(first <= third))
    print('10 USD != 50 KGS ' + str(second != third))
    print('100 USD > 50 KGS ' + str(first > third) + '; 50 KGS > 10 USD ' + str(third > second))
    print('50 KG >= 10 USD ' + str(third >= second))