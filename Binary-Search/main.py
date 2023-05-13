import math

arr = [1, 2, 3, 4, 5, 6, 7, 8]
start = 0
end = len(arr) - 1
target = 10

def binary_search(array: list, start: int, end: int, target):
    if start > end:
        return False

    mid_index = math.floor((start + end) / 2)

    if array[mid_index] == target:
        return True
    elif array[mid_index] > target:
        return binary_search(array, start, mid_index - 1, target)
    else:
        return binary_search(array, mid_index + 1, end, target)

# print(binary_search(array=arr, start=start, end=end, target=target))



#Alternative simpler implementation
#Error prone though as an invalid target could make array go out of bound

def binary_search_2(array: list, n: int, target):
    n = len(array)
    low = 0
    high = n - 1

    while low <= high:
        mid = math.floor((low + high) / 2)
        if array[mid] == target:
            return True
        elif array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return False

print(binary_search_2(array=arr, n=8, target=9))