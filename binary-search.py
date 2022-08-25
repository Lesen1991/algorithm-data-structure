numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]


def binary_search(num, target):
    low = 0
    high = len(num) - 1
    while low <= high:
        mid = (low + high) // 2
        if num[mid] == target:
            return mid
        elif num[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


print(binary_search(numbers, 13))
