def right_leader(arr):
    if not arr:
        return []
    res = []
    res.append(arr[len(arr)-1])
    max_right = arr[len(arr)-1]
    for i in range(len(arr)-2,-1,-1):
        if arr[i] > max_right:
            res.append(arr[i])
            max_right = arr[i]
    res.reverse()
    return res

arr = [16, 17, 4, 3, 5, 2]
print(right_leader(arr))
