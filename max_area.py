def max_area(arr):
    left = 0
    right = len(arr)-1
    max_a = 0
    while left < right:
        width = right - left
        height = min(arr[left], arr[right])
        max_a = max(max_a, width * height)
        if arr[left] < arr[right]:
            left+=1
        else:
            right-=1
    return max_a

print(max_area([1,8,6,2,5,4,8,3,7]))