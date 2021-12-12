'''4. Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число; случайное вещественное число; случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.'''

from random import random

case = int(input('Напиши 1, если ищем случайное целое число; '
                 '2 - если ищем случайное вещественное число; '
                 '3 - если ищем случайный символ: '))
if case == 1:
    left_boundary = int(input('Введите левую границу диапазона: '))
    right_boundary = int(input('Введите правую границу диапазона: '))
    print(int(random() * (right_boundary - left_boundary + 1) + left_boundary))
if case == 2:
    left_boundary = float(input('Введите левую границу диапазона: '))
    right_boundary = float(input('Введите правую границу диапазона: '))
    print(float(random() * (right_boundary - left_boundary + 1) + left_boundary))
if case == 3:
    left_boundary = input(('Введите левую границу диапазона: '))
    right_boundary = input(('Введите правую границу диапазона: '))
    print(chr(int((random() * (ord(right_boundary) - 96 - (ord(left_boundary) - 96) + 1) + ord(left_boundary) - 96) + 96)))