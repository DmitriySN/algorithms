# https://contest.yandex.ru/contest/23758/problems/F/

class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        return str(self.items.append(item))

    def pop(self):
        if len(self.items) == 0:
            return 'error'
        return str(self.items.pop())

    def get_max(self):
        if len(self.items) == 0:
            return 'None'
        return str(max(self.items))


def read_input():
    stack = StackMax()
    n = int(input())
    for _ in range(n):
        st = input().split()
        if st[0] == 'push':
            _ = stack.push(int(st[1]))
        elif st[0] == 'pop':
            if stack.pop() == 'error':
                print('error')
        elif st[0] == 'get_max':
            print(stack.get_max())


def main():
    read_input()


if __name__ == "__main__":
    main()
