# https://contest.yandex.ru/contest/23758/problems/G/

class StackMax:
    def __init__(self):
        self.items = []
        self.maxx = []
        self.maxx.append(-9223372036854775808)

    def push(self, item):
        self.items.append(item)
        if self.maxx[-1] <= item:
            self.maxx.append(item)

    def pop(self):
        if len(self.items) == 0:
            print('error')
        else:
            b = self.items.pop()
            if b >= self.maxx[-1]:
                self.maxx.pop()

    def get_max(self):
        if len(self.items) == 0:
            print('None')
        else:
            print(self.maxx[-1])


def read_input():
    stack = StackMax()
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input().split())

    for st in arr:
        if st[0] == 'push':
            stack.push(int(st[1]))
        elif st[0] == 'pop':
            stack.pop()
        elif st[0] == 'get_max':
            stack.get_max()


def main():
    read_input()


if __name__ == "__main__":
    main()
