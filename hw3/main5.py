def fibonacci_of(n):
    if n in (0, 1):
        return n
    elif n < 0:
        return 'Число меньше 0! Введите число >= 0'
    else:
        previous, fib_number = 0, 1
        result = [previous,fib_number]
        for _ in range(2, n + 1):
            previous, fib_number = fib_number, previous + fib_number
            if _ % 2 == 0:
                result.append(-fib_number)
            else:
                result.append(fib_number)

        result = list(reversed(result))
        previous, fib_number = 0, 1
        for _ in range(2, n + 1):
            previous, fib_number = fib_number, previous + fib_number
            result.append(fib_number)
        return result


print(fibonacci_of(int(input("Введите число: "))))
