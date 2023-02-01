input_list = list(map(int, input('Введите список чисел: ').split()))
len_list = len(input_list)
len_center = len_list // 2

result = list()
for i in range(len_center + 1):
    len_list -= 1
    result.append(input_list[i] * input_list[len_list])

print(f'- {input_list} -> {result}')
