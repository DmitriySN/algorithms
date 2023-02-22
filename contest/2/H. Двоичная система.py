# https://contest.yandex.ru/contest/23389/problems/H/

from typing import Tuple

def get_sum(first_number: str, second_number: str) -> str:
    # Здесь реализация вашего решения

    first_number = first_number[::-1]
    second_number = second_number[::-1]
    n = max(len(second_number), len(first_number))

    first_number += [0] * (n - len(first_number))
    second_number += [0] * (n - len(second_number))

    buf = []
    over = 0
    for i in range(n):
        try:
            if int(first_number[i]) + int(second_number[i]) + over == 0:
                over = 0
                buf.append(0)
            elif int(first_number[i]) + int(second_number[i]) + over == 1:
                over = 0
                buf.append(1)
            elif int(first_number[i]) + int(second_number[i]) + over == 2:
                over = 1
                buf.append(0)
            elif int(first_number[i]) + int(second_number[i]) + over == 3:
                over = 1
                buf.append(1)

        except IndexError:
            pass
    if over == 1:
        buf.append(1)

    return ''.join(str(x) for x in buf[::-1])

def read_input() -> Tuple[str, str]:
    first_number = [*map(int, input().strip())]
    second_number = [*map(int, input().strip())]
    return first_number, second_number

first_number, second_number = read_input()
print(get_sum(first_number, second_number))
