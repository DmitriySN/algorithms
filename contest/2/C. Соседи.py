# https://contest.yandex.ru/contest/23389/problems/C/

from typing import List, Tuple

def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    # Здесь реализация вашего решения
    buf = []

    if row != 0:
        buf.append(matrix[row-1][col])

    if col > 0:
        buf.append(matrix[row][col-1])
    try:
        buf.append(matrix[row+1][col])
    except IndexError:
        pass
    try:
        buf.append(matrix[row][col+1])
    except IndexError:
        pass
    buf.sort()
    return buf

def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col

matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
