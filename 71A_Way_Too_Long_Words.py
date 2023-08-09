num = int(input())
for i in range(0, num):
    word = input()
    length = len(word)
    if length <= 10:
        print(word)
    else:
        print(f"{word[0]}{len(word[1:-1])}{word[-1]}")
