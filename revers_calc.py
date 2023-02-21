# ID 79952217

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def calc(b, a, sign):
    mt = {
        '+': lambda a, b: a + b,
        '*': lambda a, b: a * b,
        '-': lambda a, b: a - b,
        '/': lambda a, b: a // b,
    }
    return mt[sign](a, b)


def read_input():
    expr = input().split()
    stack = Stack()
    for el in expr:
        try:
            stack.push(int(el))
        except ValueError:
            e = calc(int(stack.pop()), int(stack.pop()), el)
            stack.push(e)
            continue
    print(stack.pop())


def main():
    read_input()


if __name__ == "__main__":
    main()
