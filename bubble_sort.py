def bubble_sort(arr):
    swapped = True
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

arr = [2,4,1,7,3,9,8,4]
bubble_sort(arr)
print(arr)
#most optimized is the one above



