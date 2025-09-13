def peaks_and_valleys(arr):
    maxi = 0
    for i in range(0,len(arr),2): # for i in range(1,len(arr),2) for odd peaks:
        maxi = biggest_index(arr,i-1,i,i+1)
        if maxi != i:
            arr[maxi],arr[i] = arr[i],arr[maxi]
    return arr

def biggest_index(arr,i,j,k):
    a = arr[i] if 0<=i<len(arr) else float('-inf')
    b = arr[j] if 0<=j<len(arr) else float('-inf')
    c = arr[k] if 0<=k<len(arr) else float('-inf')

    if a > b and a > c:
        return i
    elif b > c and b > a:
        return j
    return k

arr = [5, 3, 1, 2, 3]
print(peaks_and_valleys(arr))

