def sorted_arr(arr):
    c = 0
    for i in range(len(arr)-2,-1,-1):
        if arr[i] > arr[i+1]:
            return False
    return True
arr = [1,2,3,4,5]
print(sorted_arr(arr))

