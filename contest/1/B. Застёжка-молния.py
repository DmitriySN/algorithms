# https://contest.yandex.ru/contest/26365/problems/B/

from typing import List, Tuple

def zipper(a: List[int], b: List[int]) -> List[int]:
    # Здесь реализация вашего решения
    mass = []
    for i in range(0, len(a)):
        mass.append(a[i])
        mass.append(b[i])
    return mass

def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b

a, b = read_input()
print(" ".join(map(str, zipper(a, b))))
