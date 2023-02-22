# https://contest.yandex.ru/contest/23389/problems/G/

def to_binary(number: int) -> str:
    # Здесь реализация вашего решения
    binn = []
    num = number
    while True == True:
        binn.append(num % 2)
        num = int(num / 2)
        if num == 0:
            reversed_string = ''.join(str(x) for x in binn[::-1])
            return reversed_string

def read_input() -> int:
    return int(input().strip())

print(to_binary(read_input()))
