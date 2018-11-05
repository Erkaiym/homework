#Задание 1
class Publication:
    def __init__(self, name, date, pages, library, typee):
        self.name = name
        self.date = date
        self.pages = pages
        self.library = library
        self.typee = typee

    def __repr__(self):
        return f'{self.typee} \'{self.name}\' was published {self.date} within {self.pages} pages. It\'s stored in {self.library}.'

    def get_code_in_library(self):
        return ''.join(self.library[:2] + self.typee[:2] + self.name[:2] + ''.join(list(str(self.pages))[:2]) + self.date[:2])


class Book(Publication):
    def __init__(self, name, date, pages, library):
        Publication.__init__(self, name, date, pages, library, 'Book')


class Magazine(Publication):
    def __init__(self, name, date, pages, library):
        Publication.__init__(self, name, date, pages, library, 'Magazine')
    

class Newspaper(Publication):
    def __init__(self, name, date, pages, library):
        Publication.__init__(self, name, date, pages, library, 'Newspaper')
      
if __name__ == '__main__':
    book = Book('Jamelia', '20.10.1958', 350, 'National Library')
    magazine = Magazine('International Affairs', '15.05.2010', 210, 'IA Archive')
    newspaper = Newspaper('Boston Globe', '01.01.2018', 16, 'BG Archive')

    print(book, '-', book.get_code_in_library())
    print(magazine, '-', magazine.get_code_in_library())
    print(newspaper, '-', newspaper.get_code_in_library())


#Задание 2
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return f'{firstname} {lastname}'


class Teacher(Person):
    def __init__(self, firstname, lastname, subject_name):
        Person.__init__(self, firstname, lastname, subject_name)
        self.subject_name = subject_name

    def __repr__(self):
        return f'{self.firstname} {self.lastname} teaches {subject_name}'

class Student(Person):
    def __init__(self, firstname, lastname):
        Person.__init__(self, firstname, lastname)


class Basketball_team_member(Student):
    def __init__(self, firstname, lastname, term): #term of being in a team
        Student.__init__(self, firstname, lastname, term)


if __name__ == '__main__':
    student = Student('Paul', 'Anderson', )
    teacher = Teacher('Michael', 'Rise', 'Physics')


    print(teacher)
    print(student)