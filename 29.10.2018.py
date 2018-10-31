class University:
    departments = {}
    def __init__(self, university_name):
        self.name = university_name

    def add_department(self, departments_name):
        University.departments.update({departments_name : []})

    def add_student(self, departments_name, Student):
        if departments_name in University.departments.keys():
            University.departments.get(departments_name).append(Student)

class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def __repr__(self):
        return f'{self.firstname} {self.lastname}'

if __name__ == '__main__':
    Uni = University('MIT')

    student1 = Student('Sam', 'Lee')
    student2 = Student('Paul', 'Black')
    student3 = Student('Hannibal', 'Lecter')
    student4 = Student('Vincent', 'Van Gogh')


    Uni.add_department('Architecture')
    Uni.add_department('Physics')
    Uni.add_student('Architecture', student1)
    Uni.add_student('Physics', student2)
    Uni.add_student('Physics', student3)
    Uni.add_student('Architecture', student4)
    print(Uni.departments)

#Задание 1
def abb(x):
    words = x.split()
    letters = [word[0] for word in words]
    return ''.join(letters)

x = (input('Type any phrase: '))
print(abb(x))

# Задания 2-4
class Subscriber:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return f'{self.firstname} {self.lastname}'

class Provider:
    def __init__(self, provider_name):
        self.name = provider_name
        self.subscribers = []
        self.payments = {}

    def add_subscriber(self, Subscriber):
        self.subscribers.append(Subscriber)

    def register_payments(self, Subscriber, amount):
        if Subscriber in self.subscribers:
            self.payments.update({Subscriber:amount})
        else:
            raise ValueError('Ошибка!')
    
    def __repr__(self):
        return f'{self.name}'

class Terminal:
    def __init__(self):
        self.amount = 0
        self.providers = []

    def register(self, Provider):
        self.providers.append(Provider)

    def pay(self, Provider, Subscriber, amount):
        Provider.register_payments(Subscriber, amount)
        self.amount += amount

    

if __name__ == '__main__':
    subscriber1 = Subscriber('Michael', 'Jordan')
    subscriber2 = Subscriber('Bob', 'Lanier')
    provider = Provider('NBA')
    terminal = Terminal()

    #print(subscriber1, subscriber2)
    provider.add_subscriber(subscriber1)
    provider.add_subscriber(subscriber2)
    terminal.register(provider)
    provider.register_payments(subscriber1, 500)
    provider.register_payments(subscriber2, 600)
    terminal.pay(provider, subscriber1, 500)
    terminal.pay(provider, subscriber2, 600)

    print('Subscribers are ' + str(provider.subscribers))
    print('Provider is ' + str(terminal.providers))
    print('Payments are ' + str(provider.payments))
    print('Provider\'s account has ' +  str(terminal.amount) + ' million USD')

#Задания 5 - 7
class Cow:
    def make_sound(self):
        return 'Мууууу!'

class Cat:
    def make_sound(self):
        return 'Мяу!'

class Dog:
    def make_sound(self):
        return 'Авав!'

cow = Cow()
print(cow.make_sound())

cat = Cat()
print(cat.make_sound())

dog = Dog()
print(dog.make_sound())


#Задание 8
def word_check(x):
    x = x.lower()
    for i in x:
        if x.count(i) > 1:
            return (x, False)
        else:
            return (x, True)

x = (input('Type any word to check if it\'s an isogram: '))
print(word_check(x))

#Задание 9
phrase = (input('Type any phrase: '))
lst = phrase.split()

def repeat(lst):
    return {word:lst.count(word) for word in lst}

print(lst)
print(repeat(lst))

#Задание 10
def chat(x):
    if x.endswith('?'):
        return 'Конечно!'
    elif x.isupper():
        return 'Успокойся!'
    elif x == '':
        return 'Как классно, когда ты молчишь. Продолжай в том же духе!'
    else:
        return 'Ну и что'

x = (input('Поговорите с ботом: '))
print(chat(x))