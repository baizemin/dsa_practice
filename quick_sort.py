

# this is a new type easier but costlier involves creating new lists
#and also the pivot position is ignored in this code just appends the pivot element in the middle after partitioning
#has n^2 space complexity worst case linear space complexity why??
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot = arr[-1]
        left = [x for x in arr[:-1] if x < pivot]
        right = [x for x in arr[:-1] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

arr = [1,4,3,6,7,2]
print(quick_sort(arr))

# this is lamuto type partitioning
def lamuto(arr,low,high):
    piv = arr[high]
    i = low-1
    for j in range(low,high):
        if arr[j] < piv:
            i=i+1
            arr[i] , arr[j] = arr[j],arr[i]
    arr[high],arr[i+1] = arr[i+1],arr[high]
    return i+1

def quick_sort(arr,low,high):
    if low < high:
        p = lamuto(arr,low,high)
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)


arr = [3,4,2,7,9,1]
quick_sort(arr,0,len(arr)-1)
print(arr)

#this is hoare's type partitioning
def hoare(arr, low, high):
    pivot = arr[low]  # low or high works fine
    i = low - 1
    j = high + 1

    while True:

        while True:
            i = i + 1
            if pivot <= arr[i]:
                break

        while True:
            j -= 1
            if arr[j] <= pivot:
                break
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr, low, high):
    if low < high:
        p = hoare(arr, low, high)
        quick_sort(arr, low, p)
        quick_sort(arr, p + 1, high)


arr = [7, 6, 5, 4, 3, 2, 1]
quick_sort(arr, 0, len(arr) - 1)
print(arr)

#finally is hoare's used for it's less swaps does better work in large databases
#lomuto's used for it's simplicity
#also the lomuto is semi stable
