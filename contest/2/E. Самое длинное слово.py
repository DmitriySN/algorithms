# https://contest.yandex.ru/contest/23389/problems/E/

def get_longest_word(line: str) -> str:
    strings = list(map(str, line.split()))
    buf = 0
    pos = 0
    for istr in range(len(strings)):
        if len(strings[istr]) > buf:
            buf = len(strings[istr])
            pos = istr
    return(strings[pos])

def read_input() -> str:
    _ = input()
    line = input().strip()
    return line

def print_result(result: str) -> None:
    print(result)
    print(len(result))

print_result(get_longest_word(read_input()))
