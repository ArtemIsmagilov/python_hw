def my_pow(n1, n2, count=0, result=1):
    if count == abs(n2):
        if n2 > 0:
            return result
        return -result
    result *= n1
    return my_pow(n1, n2, count + 1, result)


a, b = map(int, input().split())
print(my_pow(a, b))
