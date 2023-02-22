# https://contest.yandex.ru/contest/23758/problems/I/

class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def push(self, x):
        if self.size < self.max_n:
            self.queue[self.tail] = x
            self.tail += 1
            if self.tail >= self.max_n:
                self.tail = 0
            self.size += 1
        else:
            print('error')

    def pop(self):
        if self.size == 0 or len(self.queue) == 0:
            print('None')
        else:
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.head += 1
            if self.head >= self.max_n:
                self.head = 0
            self.size -= 1
            print(x)

    def peek(self):
        if self.size == 0 or len(self.queue) == 0:
            print('None')
        else:
            print(self.queue[self.head])

    def sz(self):
        print(self.size)


def read_input():
    n = int(input())
    szq = int(input())
    queue = Queue(szq)

    arr = []
    for _ in range(n):
        arr.append(input().split())

    for st in arr:
        if st[0] == 'push':
            queue.push(int(st[1]))
        elif st[0] == 'pop':
            queue.pop()
        elif st[0] == 'peek':
            queue.peek()
        elif st[0] == 'size':
            queue.sz()


def main():
    read_input()


if __name__ == "__main__":
    main()
