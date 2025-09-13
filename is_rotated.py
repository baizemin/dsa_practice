def is_rotated_arr(arr):
    c = 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            c += 1
    if arr[-1] > arr[0]:
        c += 1
    return c<=1
arr = [5,6,1,2,3,4]
print(is_rotated_arr(arr))