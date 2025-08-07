def insertion_sort(arr):
    length = len(arr)
    swap_counter  = 0
    for i in range(1,length):
        key = arr[i]
        j  = i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            # print(j,j+1)
            # swap_counter += 1
            j = j-1
        arr[j+1] = key
    return swap_counter
arr = [29,10,14,37,14]
print(insertion_sort(arr))
print(arr)