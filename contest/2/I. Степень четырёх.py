# https://contest.yandex.ru/contest/23389/problems/I/

def is_power_of_four(n: int) -> bool:
    # if n % 4 != 0:
    #     return False
    f = 1
    if f == n:
        return True
    while 1==1:
        f = f * 4
        if f == n:
            return True

        if f > n:
            return False

print(is_power_of_four(int(input())))
