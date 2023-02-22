# https://contest.yandex.ru/contest/24734/problems/H/

_ = input()
arr = input().split()
first = []

for i in range(len(arr) - 1):
    for j in range(0, len(arr)-i-1):
        var1 = arr[j] + arr[j+1]
        var2 = arr[j + 1] + arr[j]
        if var1 < var2:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("".join(arr))
