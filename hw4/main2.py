n = int(input('Введите кол-во кустов: '))
crop = list(i for i in range(1, n+1))
print(f'{n} ->', *crop)
result = sum(i for i in list(reversed(crop))[:2])
print(result)
