def shell_sort(arr, gap = 0):
    if gap == 0:
        gap = len(arr)
    if gap > 1:
        gap = gap//2
    # go through the list and check if anything to the gap is bigger
        for i in range (gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j - gap]
                j = j-gap
            arr[j] = temp
    # call the function recursively
        return(shell_sort(arr, gap))
    else:
        return arr

list_to_sort = [1,3,44,5,0,4,801,9,1000,0]
print(shell_sort(list_to_sort))