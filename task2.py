'''2. Посчитать четные и нечетные цифры введенного натурального числа.
 Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).'''

a = int(input('Введите число: '))
#print(len(str(a))) - проверка на кол-ва символов
count1 = 0 #четные
count2 = 0 #нечетные

while a > 0:
    a = a // 10
    if a%2 == 0:
        count1 +=1
    else:
        count2 +=1


print(f'Четные: %d, Нечетные: %d' % (count1, count2))
