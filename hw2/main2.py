import math
S, P = map(int, input('Введите сумму и произведение чисел: ').split())
a, b, c = 1, -S, P
D = b**2 -4*a*c
x1 = (-b + D)/(2*a)
x2 = (-b + D)/(2*a)
print(f'{S}, {P} -> {x1}, {x2}')
