def next_permutation(arr):
    n = len(arr)
    res = -1
    for i in range(n-2,-1,-1):
        if arr[i] < arr[i+1]:
            res = i
            break
    if res == -1 :
        arr.reverse()
        return arr

    for i in range(n-1,res,-1):
        if arr[i] > arr[res]:
            arr[i], arr[res] = arr[res], arr[i]
            break
    reverse_arr(arr,res+1,n-1)


# reversing the array
def reverse_arr(arr,start,end):

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# with the time complexity n!*n
def generate_permutations(res,arr,idx):
   if idx == len(arr):
       res.append(arr[:])
       return
   for i in range(idx,len(arr)):
       arr[idx],arr[i] = arr[i],arr[idx]
       generate_permutations(res,arr,idx+1)
       arr[idx],arr[i] = arr[i],arr[idx]
   return res

arr = [2, 4, 1, 7, 5, 0]
res = []
next_permutation(arr)
print(arr)
#generate_permutations(res,arr,0)
print(res)

