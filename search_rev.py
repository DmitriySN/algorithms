# ID 80481729
def broken_search(nums, target) -> int:
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (end + start) // 2
        if target == nums[mid]:
            return mid

        if nums[start] <= nums[mid]:
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


def test():
    _ = input()
    n = int(input())
    arr = list(map(int, input().split()))
    print(broken_search(arr, n))


if __name__ == "__main__":
    test()
