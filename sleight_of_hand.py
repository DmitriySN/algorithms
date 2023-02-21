# ID 79018639
def get_score(keys: str, gamer_key: int) -> int:
    GAMER_NUM = 2
    gamer_key = gamer_key * GAMER_NUM
    score = 0
    for char in '123456789':
        score += int(0 < keys.count(char) <= gamer_key)
    return score


def read_input() -> str:
    MATRIX = 4
    k = int(input())
    keys = ''
    for i in range(MATRIX):
        keys += str(input().strip().replace('.', ''))[:MATRIX]
    return keys, k


def main():
    keys, k = read_input()
    print(get_score(keys, k))


if __name__ == "__main__":
    main()
