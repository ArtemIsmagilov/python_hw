n, m, k = map(int, input().split())
print('yes' if n * m > k and (k % n == 0 or k % m == 0) else 'no')
