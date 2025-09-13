def trap(arr):
    total = 0
    right = [0]*len(arr)
    left = [0]*len(arr)
    left[0] = arr[0]
    right[-1] = arr[-1]
    for i in range(1,len(arr)):
        left[i] = max(left[i-1],arr[i])
    for i in range(len(arr)-2,-1,-1):
        right[i] = max(right[i+1],arr[i])

    for i in range(len(arr)):
        total += min(left[i],right[i]) - arr[i]
    return total
arr = [0, 1, 2, 0, 1, 2]
print(trap(arr))

def trap_two_pointer(arr):
    water = 0
    left_max,right_max = 0,0
    left,right = 0,len(arr)-1
    while left < right:
        if arr[left] < arr[right]:
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                water += left_max - arr[left]
            left+=1
        else:
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                water += right_max - arr[right]
            right-=1
    return water
arr = [0, 1, 2, 0, 1, 2]
print(trap_two_pointer(arr))
