# https://contest.yandex.ru/contest/23389/problems/A/

def evaluate_function(a: int, b: int, c: int, x: int) -> int:
    # Здесь реализация вашего решения
    y = a*x*x + b*x + c
    return y

a, x, b, c = map(int, input().strip().split())
print(evaluate_function(a, b, c, x))