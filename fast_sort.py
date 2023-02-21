# ID 80482076
class Compare():
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        return (
            (self.a[1] > other.a[1])
            or (self.a[1] == other.a[1] and self.a[2] < other.a[2])
            or (self.a[1] == other.a[1] and self.a[2] == other.a[2]
                and self.a[0] < other.a[0])
        )


def partition(array, start, end):
    pivot = start
    for i in range(start + 1, end + 1):
        one = Compare(array[i])
        two = Compare(array[start])
        if one < two:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]

    array[pivot], array[start] = array[start], array[pivot]
    return pivot


def quick_sort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1

    def _qsort(array, start, end):
        if start >= end:
            return
        pivot = partition(array, start, end)
        _qsort(array, start, pivot - 1)
        _qsort(array, pivot + 1, end)
    return _qsort(array, start, end)


def read_input():
    n = int(input())
    arr = []
    for _ in range(n):
        name, task, penalty = input().split()
        arr.append([name, int(task), int(penalty)])
    quick_sort(arr)
    for user in arr:
        print(user[0])


if __name__ == "__main__":
    read_input()
