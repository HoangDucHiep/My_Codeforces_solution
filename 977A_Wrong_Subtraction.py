num, times = map(int, input().split())
for i in range(0, times):
    last_dit = num%10
    if last_dit == 0:
        num = num//10
    else:
        num -= 1
print(num)
