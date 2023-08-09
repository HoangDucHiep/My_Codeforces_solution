k, n, w = map(int, input().split())
pay = 0
for i in range(1, w + 1):
    pay += i*k
print(0 if pay < n else pay - n)
