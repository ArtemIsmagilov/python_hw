n = int(input('Введите число N: '))
res = 1
print(f'{n} ->', end=' ')
while n >= res * 2:
    res *= 2
    print(res, end=' ')
