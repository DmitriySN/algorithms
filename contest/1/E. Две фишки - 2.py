# https://contest.yandex.ru/contest/26365/problems/E/

from typing import List, Tuple, Optional

def two_sum(numbers: List[int], X: int) -> Optional[Tuple[int, int]]:
    numbers.sort()

    left = 0
    right = len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == X:
            return numbers[left], numbers[right]
        if current_sum < X:
            left += 1
        else:
            right -= 1
    # Если ничего не нашлось в цикле, значит, нужной пары элементов в массиве нет.
    return None

def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return arr, target_sum

def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        # print(" ".join(map(str, result)))
        print(result[0],result[1])

arr, target_sum = read_input()
print_result(two_sum(arr, target_sum))
