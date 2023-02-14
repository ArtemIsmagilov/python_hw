n, m = sorted(map(int, input('Задайте диапазон для массива через пробел: ').split()))
arr = list(map(int, input('Введите числа массива: ').split()))
print([i for i in range(len(arr)) if n <= arr[i] <= m])
