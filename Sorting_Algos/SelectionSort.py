def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

list_to_sort = [1,3,44,5,0,4,801,9,1000,0]
print(selection_sort(list_to_sort))