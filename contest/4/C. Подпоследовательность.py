# https://contest.yandex.ru/contest/24734/problems/C/

s1 = input()
s2 = input()

num = 0
for i in s2:
    if i == s1[num]:
        num += 1
    if num == len(s1):
        break
if num == len(s1):
    print('True')
else:
    print('False')
