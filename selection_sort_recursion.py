def prefix_max(arr,i):
    if i == 0:
        return 0
    j = prefix_max(arr,i-1)
    if arr[i] < arr[j]:
        return j
    return i

def selection_sort(arr,n):
    if n == 0:
        return 0
    j = prefix_max(arr,n-1)
    arr[j], arr[n-1] = arr[n-1], arr[j]
    selection_sort(arr,n-1)

arr = [2,4,1,7,3,9,8,4]
selection_sort(arr,len(arr))
print(arr)

