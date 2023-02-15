def quick_sort(arr, start, end):
    if start < end:
        partition_index = partition(arr, start, end)

        #Sorts everything BEFORE the partition index
        quick_sort(arr, start, end=partition_index-1)

        #Sorts everything AFTER the partition index
        quick_sort(arr, start=partition_index+1, end=end)

def partition(sub_arr, start, end):
    pivot = sub_arr[end]
    i = start - 1           #Some might call i a partition index but it was difficult for me to understand

    for j in range(start, end):    #Looping through the entire len of sub_arr: 0, len-1
        if sub_arr[j] <= pivot:
            i += 1  # i becomes position of last sorted + 1

            # Swapping the element at the point of last-sorted+1
            # arr[i] with the current element, arr[j]
            # that is less than the pivot
            temp = sub_arr[i]
            sub_arr[i] = sub_arr[j]
            sub_arr[j] = temp

    temp2 = sub_arr[i+1]           # This swaps the pivot, arr[end] to
    sub_arr[i+1] = sub_arr[end]    # the last-sorted position + 1 as the elements
    sub_arr[end] = temp2           # to the right of i+1 are bigger than the pivot
    return i+1   

my_arr = [10, 80, 30, 90, 40, 50, 70]
print(f"Before: \n{my_arr}")

quick_sort(my_arr, 0, len(my_arr)-1)
print(f"After: \n{my_arr}")