n, m = map(int, input('Введите кол-во элементов первого и второго множества: ').split())
set_1 = set(map(int, input('Введите элементы первого множества: ').split()))
set_2 = set(map(int, input('Введите элементы второго множества: ').split()))
print(*sorted(set_1.intersection(set_2)))
