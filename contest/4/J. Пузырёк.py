# https://contest.yandex.ru/contest/24734/problems/J/

_ = input()
arr = list(map(int, input().split()))
sort = True
for i in range(len(arr)-1):
    n = 0
    max = 0
    for j in range(len(arr)-i-1):

        if arr[j] > arr[j + 1]:
            max = arr[j]
            arr[j], arr[j+1] = arr[j+1], arr[j]
            n = 1
            sort = False
    if n == 0:
        if sort:
            print(*arr)
        break
    print(*arr)
