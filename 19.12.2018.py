import re
#Практика
#1
"""Написать программу с использованием регулярного выражения,
которая найдет строковое значение, в котором есть буква ‘w’."""

pattern = r'w'
text1 = "The quick brown fox jumps over the lazy dog." # match object 
text2 = "Python Exercises." # None
res1 = re.search(pattern, text)
res2 = re.search(pattern, text2)

if res1:
	print('Match!')
	print('\'w\' index position is ' + str(res.start()))
else:
	print('Not a match!')

print(res1, res2)

#2
"""Написать программу с использованием регулярного выражения, 
которая найдет строковое значение, в котором есть буква ‘w’ 
только не в начале слова и не в конце."""

attern = r'\Bw\B'
text1 = "wonderful" # None
text2 = "owner" # match object
res1 = re.findall(pattern, text)
res2 = re.findall(pattern,text2)

print(res1, res2)

#3
"""Написать программу с использованием регулярного выражения,
которая найдет слово, начинающееся на цифру 42."""

pattern = r'42'
text1 = "23 street" # None
text2 = "42 meaning of life" # match object

res1 = re.match(pattern, text1)
res2 = re.match(pattern, text2)
print(res1, text2)

#4
"""Написать программу с использованием регулярного выражения,
которая заменит нули в начале телефонного номера на +996
0770775596 -> +996770775596"""

pattern = r'\b0'
start = r'+996'
number = '0770775596'

res = re.sub(pattern, start, number)
print(res)

#5
"""Ловим путь в URL с помощью регулярных выражений.
Из URL localhost:8888/ilovepython извлекаем ilovepython"""

pattern = r'/'
url = 'localhost:8888/ilovepython'

res = re.split(pattern, url)
print(res[1])




#Домашка
#1
"""
Написать программу с использованием регулярного выражения, которая 
заменит пробелы пустоту
" Python    Exercises " должен превратиться в "PythonExercises"
"""
pattern = r' '
pattern2 = r''
text = ' Python    Exercises '
print(text)

res = re.sub(pattern, pattern2, text)
print(res)

#2
"""
Написать валидатор пароля: в пароле должен быть как минимум один 
Заглавный символ, одна цифра, один символ $%!@#^&* и общяя длина 
должна быть не менее 8 символов"""

^[A-Z0-9$%!@#^&*]{8,}$