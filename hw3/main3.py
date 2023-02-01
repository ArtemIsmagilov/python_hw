input_list = list(map(float, input('Введите список чисел: ').split()))
re_list = list(i % 1 for i in input_list)
max_f, min_f = max(re_list), min(re_list)
print(f'{input_list} -> {round(max_f - min_f, 3)}')
