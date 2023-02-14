a, d, n = map(int, (input('Введите первый элемент: '), input('Введите разность: '), input('Введите кол-во элементов: ')))
[print(a + (i-1)*d, end=' ') for i in range(1, n+1)]

