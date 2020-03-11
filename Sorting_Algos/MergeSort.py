def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        # Recursive call on each half to further divide the halves
        merge_sort(left)
        merge_sort(right)
        # Two iterators for traversing the two halves
        l = 0
        r = 0
        # Iterator for the main list
        m = 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
              # The value from the left half has been used
              arr[m] = left[l]
              # Move the iterator forward
              l += 1
            else:
                arr[m] = right[r]
                r += 1
            # Move to the next slot
            m += 1
        # For all the remaining values
        while l < len(left):
            arr[m] = left[l]
            l += 1
            m += 1
        while r < len(right):
            arr[m]=right[r]
            r += 1
            m += 1
    return(arr)

list_to_sort = [1,3,44,5,0,4,801,9,1000,0]
print(merge_sort(list_to_sort))
