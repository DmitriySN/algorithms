# https://contest.yandex.ru/contest/24734/problems/B/

d = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
NEW_COMB = ''
ESTIMATED_LENGTH = 0
len_comb = 0

def comb_generator(list_n, len_n, prefix=''):
    '''Генератор комбинаций.'''
    global len_comb, NEW_COMB, ESTIMATED_LENGTH
    if len_n == 0:
        len_comb += len(prefix + ' ')
        print(prefix + ' ', end='')
        # NEW_COMB += prefix + ' '
        # if len(NEW_COMB) == ESTIMATED_LENGTH:
        #     print(NEW_COMB)
        if len_comb == ESTIMATED_LENGTH:
            return
    else:
        letters = d[list_n[0]]
        for let in letters:
            comb_generator(list_n[1:], len_n-1, prefix + let)


def read_input():
    global ESTIMATED_LENGTH
    n = input().strip()
    estimated_length = 1
    for num in n:
        estimated_length *= len(d[num])
    ESTIMATED_LENGTH = estimated_length * len(n) + estimated_length
    comb_generator(n, len(n))


def main():
    read_input()


if __name__ == '__main__':
    main()
