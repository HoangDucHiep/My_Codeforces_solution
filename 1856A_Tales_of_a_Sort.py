num_of_tests = int(input())
for i in range(0,num_of_tests):
    size = int(input())
    arr = list(map(int, input().split()))
    index = size - 1
    while index > 0 and arr[index - 1] <= arr[index]:
        index -= 1
    if index == 0:
        print(0)
    else:
        print(max(arr[:index]))
