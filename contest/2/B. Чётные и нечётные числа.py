# https://contest.yandex.ru/contest/23389/problems/B/

def check_parity(a: int, b: int, c: int) -> bool:
    # Здесь реализация вашего решения
    if a%2 == 0 and b%2 == 0 and c%2 == 0:
        return True
    elif a%2 != 0 and b%2 != 0 and c%2 != 0:
        return True
    return False


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")

a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
