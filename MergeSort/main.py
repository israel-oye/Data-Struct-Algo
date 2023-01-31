import math

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid_index = math.floor(len(arr) / 2)
    left_arr = arr[0 : mid_index] 
    right_arr = arr[mid_index : len(arr)]
    
    return merge(merge_sort(left_arr), merge_sort(right_arr))

def merge(left_arr: list, right_arr: list):
    result_arr = []
    left_index = 0
    right_index = 0

    while(left_index < len(left_arr) and right_index < len(right_arr)):
        if left_arr[left_index] < right_arr[right_index]:
            result_arr.append(left_arr[left_index])
            left_index += 1
        else:
            result_arr.append(right_arr[right_index])
            right_index += 1
    result_arr += left_arr[left_index:] + right_arr[right_index:]
    return right_arr

my_arr = [23, 12, 1, 5, 6]
merge_sort(my_arr)