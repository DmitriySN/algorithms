# https://contest.yandex.ru/contest/24734/problems/L/

def read_input():
    n = int(input())
    szq = input().split()
    s = int(input())

    v1 = -1
    v2 = -1
    for i in range(n):
        if int(szq[i]) >= s:
            if v1 > -1:
                v2 = i+1
                print(v1, v2)
                return
            elif v1 == -1:
                v1 = i+1
            s *= 2
    print(v1, v2)


def main():
    read_input()


if __name__ == "__main__":
    main()
