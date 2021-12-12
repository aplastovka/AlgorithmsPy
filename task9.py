#9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a, b, c = int(input()), int(input()), int(input())
max_num = max(a, b, c)
min_num = min(a, b, c)
mid_num = (a + b + c) - max_num - min_num
print(mid_num)
