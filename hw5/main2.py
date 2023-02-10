def my_sum(n1, n2, result=0):
    if result == n1 + n2:
        return result
    return my_sum(n1, n2, result=result + 1)


a, b = map(int, input().split())
print(my_sum(a, b))
