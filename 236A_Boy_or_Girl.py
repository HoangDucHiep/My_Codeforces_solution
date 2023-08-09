word = input()
filtered = list(set(word))
if len(filtered)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
