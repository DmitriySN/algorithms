# https://contest.yandex.ru/contest/23389/problems/F/

import re
def is_palindrome(line: str) -> bool:
    # Здесь реализация вашего решения
    res = re.sub('[^A-Za-z0-9]+', '', line)
    st = res.lower()
    buf = True
    for i in range(int(len(st)/2)):
        b = len(st)-1
        if st[i] != st[b-i]:
            return False
    return buf

print(is_palindrome(input().strip()))
