def insertion_sort(arr):
    for i in range(1, len(arr)):
        # Set key:
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            # Swap:
            arr[j + 1] = arr[j]
            arr[j] = key
            # Decrement 'j':
            j -= 1
    return arr

list_to_sort = [1,3,44,5,0,4,801,9,1000,0]
print(insertion_sort(list_to_sort))