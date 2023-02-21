# ID 79953003
class ListEmptyError(Exception):
    ...


class ListMaxSizeError(Exception):
    ...


class Queue:
    """ Класс реализующий Дек очереди. """
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return (self.size == 0 or len(self.queue) == 0)

    def push_back(self, x):
        """ Добавление элемента в конец очереди. """

        if self.size < self.max_n:
            self.queue[self.tail] = x
            self.tail += 1
            if self.tail >= self.max_n:
                self.tail = 0
            self.size += 1
        else:
            raise ListMaxSizeError('Переполнение очереди')

    def push_front(self, x):
        """ Добавление элемента в начало очереди. """

        if self.size < self.max_n:
            self.head -= 1
            if self.head < 0:
                self.head = self.max_n - 1
            self.queue[self.head] = x
            self.size += 1
        else:
            raise ListMaxSizeError('Переполнение очереди')

    def pop_back(self):
        """ Удаление последнего элемента из очереди. """

        if self.is_empty():
            raise ListEmptyError('Пустой список')
        else:
            self.tail -= 1
            if self.tail < 0:
                self.tail = self.max_n - 1
            x = self.queue[self.tail]
            self.queue[self.tail] = None
            self.size -= 1
            return x

    def pop_front(self):
        """ Удаление первого элемента из очереди. """

        if self.is_empty():
            raise ListEmptyError('Пустой список')
        else:
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.head += 1
            if self.head >= self.max_n:
                self.head = 0
            self.size -= 1
            return x


def read_input():
    n = int(input())
    szq = int(input())
    queue = Queue(szq)

    arr = []
    for _ in range(n):
        arr.append(input().split())

    for st in arr:
        action = getattr(queue, st[0])
        try:
            print(action()) if len(st) == 1 else action(int(st[1]))
        except (ListEmptyError, ListMaxSizeError):
            print('error')


def main():
    read_input()


if __name__ == "__main__":
    main()
