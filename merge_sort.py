def merge(arr,left,middle,right):
    larr = arr[left:middle+1]
    rarr = arr[middle+1:right+1]
    i = 0
    j = 0
    k = left
    while i < len(larr) and j < len(rarr):
        if larr[i] <= rarr[j]:
            arr[k] = larr[i]
            i=i+1
        else:
            arr[k] = rarr[j]
            j = j + 1
        k+=1
    while i < len(larr):
        arr[k] = larr[i]
        i = i + 1
        k=k+1
    while j < len(rarr):
        arr[k] = rarr[j]
        k=k+1
        j=j+1

def merge_sort(arr,left,right):
    if left >= right:
        return
    middle = (left+right)//2
    merge_sort(arr,left,middle)
    merge_sort(arr,middle+1,right)
    merge(arr,left,middle,right)

arr = [5,4,3,2,1]
n = len(arr)
merge_sort(arr,0,n-1)
print(arr)