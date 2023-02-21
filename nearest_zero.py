# ID 79787481

def nearest_home(homes_arr) -> str:
    n = len(homes_arr)
    homes = [0] * n
    count = n
    end = n

    for id, value in enumerate(homes_arr):

        if value == '0':
            count = 0
            end = id
        else:
            count += 1
            homes[id] = count

    count = 0
    for p in range(end - 1, -1, -1):

        if homes[p] == 0:
            count = 0
        elif count < homes[p]:
            count += 1
            homes[p] = count
    return homes


def read_input():
    _ = int(input())
    homes_arr = input().split()
    return homes_arr


def main():
    nearest = read_input()
    print(*nearest_home(nearest))


if __name__ == "__main__":
    main()
