def bubble_sort(arr):
    # Set a switch to check if the list is sorted
    swapped = False
    for i in range(1, len(arr)):
    # check if the item behind the current item is larger, and if so, swap them and change the switch
        if arr[i-1] > arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            swapped = True
    # If a swap took place, then the list may not be sorted, call the function recursively
    if swapped == True:
        return bubble_sort(arr)
    return(arr)

list_to_sort = [1,3,44,5,0,4,801,9,1000,0]

print(bubble_sort(list_to_sort))

def bubble_sort2(arr):
    i = 1
    while i < len(arr):
        if arr[i-1] > arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i = 1
        i += 1
    return(arr)

print(bubble_sort2(list_to_sort))
