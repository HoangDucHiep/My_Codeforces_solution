word = input()
upper = 0
lower = 0
for char in word:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
if lower >= upper:
    print(word.lower())
else:
    print(word.upper())
