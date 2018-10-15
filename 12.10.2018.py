print('Задача № 1')
#first way
file = open('kyrgyzstan.txt', 'w')
file.write('Kyrgyzstan, country of Central Asia. It is bounded by Kazakhstan on the northwest and north, by China on the east and south, and by Tajikistan and Uzbekistan on the south and west. Most of Kyrgyzstan’s borders run along mountain crests. The capital is Bishkek (known from 1862 to 1926 as Pishpek and from 1926 to 1991 as Frunze).')
file.close()
file = open('kyrgyzstan.txt', 'r')
print('Файл записан. \nВ данном файле ' + str(len(file.read())) + ' символов.')
file.close()

#second way
with open('kyrgyzstan.txt', 'w') as file:
    file.write('Kyrgyzstan, country of Central Asia. It is bounded by Kazakhstan on the northwest and north, by China on the east and south, and by Tajikistan and Uzbekistan on the south and west. Most of Kyrgyzstan’s borders run along mountain crests. The capital is Bishkek (known from 1862 to 1926 as Pishpek and from 1926 to 1991 as Frunze).')
with open('kyrgyzstan.txt', 'r') as file:
    print('Файл записан. \nВ данном файле ' + str(len(file.read())) + ' символов.')


print('\nЗадача № 2')
#first way
file1 = open('kyrgyzstan.txt', 'r')
file2 = open('wikipedia.txt', 'w')
text = file1.read()
file2.write(text)
file1.close()
file2.close()
print('Копирование завершено.')

file3 = open('wikipedia.txt', 'a')
file3.write('The Kyrgyz, a Muslim Turkic people, constitute more than half the population. The history of the Kyrgyz in what is now Kyrgyzstan dates at least to the 17th century. Kyrgyzstan, known under Russian and Soviet rule as Kirgiziya, was conquered by tsarist Russian forces in the 19th century. Formerly a constituent (union) republic of the U.S.S.R., Kyrgyzstan declared its independence on August 31, 1991.')
file3.close()
print('Файл дополнен.')

file4 = open('wikipedia.txt', 'r')
print(file4.read())
file4.close()

#second way
with open('kyrgyzstan.txt', 'r') as file1:
    with open('wikipedia.txt', 'w') as file2:
        file2.write(file1.read())
print('Копирование завершено.')

with open('wikipedia.txt', 'a') as file3:
    file3.write('The Kyrgyz, a Muslim Turkic people, constitute more than half the population. The history of the Kyrgyz in what is now Kyrgyzstan dates at least to the 17th century. Kyrgyzstan, known under Russian and Soviet rule as Kirgiziya, was conquered by tsarist Russian forces in the 19th century. Formerly a constituent (union) republic of the U.S.S.R., Kyrgyzstan declared its independence on August 31, 1991.')
print('Файл дополнен.')

with open('wikipedia.txt', 'r') as file4:
    print(file4.read())


print('\nЗадача № 3')
file1 = open('conor.jpg', 'rb')
file2 = open('chicken.jpg', 'wb')
file2.write(file1.read())
file1.close()
file2.close()
print('Копиравание завершено.')

#second way
with open('conor.jpg', 'rb') as file1:
    with open('chicken.jpg', 'wb') as file2:
        file2.write(file1.read())
print('Копиравание завершено.')
