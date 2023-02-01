input_list = list(map(int, input('Введите список чисел: ').split()))
print('%s -> %s' % (input_list, sum(i for i in input_list[1::2])))
