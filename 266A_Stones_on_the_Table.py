length = int(input())
senten = input()
count = 0
buff = senten[0]
for i in range(1, length):
    if senten[i] == buff:
        count += 1
    else:
        buff = senten[i]
 
print(count)
