# https://contest.yandex.ru/contest/24734/problems/A/

n = int(input())

def staples(count, left=0, right=0, st=''):
    if left == count and right == count:
        print(st)
    else:
        if left < count:
            staples(count, left + 1, right, st + '(')
        if right < left:
            staples(count, left, right + 1, st + ')')
staples(n)
