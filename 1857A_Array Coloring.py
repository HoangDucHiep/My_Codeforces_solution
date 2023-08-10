num_of_tests = int(input())
for i in range(num_of_tests):
    size = int(input())
    arr = list(map(int, input().split()))
    if sum(arr)%2==0:
        print("YES")
    else:
        print("NO")
