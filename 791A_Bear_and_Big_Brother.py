Limak, Bob = map(int, input().split())
years = 0
while Limak <= Bob:
    Limak *= 3
    Bob *= 2
    years += 1
print(years)
