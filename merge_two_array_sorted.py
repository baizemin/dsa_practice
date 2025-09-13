def merge_two_arrays(l1, l2):
    length = len(l1) + len(l2)
    res = [None]*length
    i,j,k = 0,0,0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            res[k] = l1[i]
            k+=1
            i+=1
        else:
            res[k] = l2[j]
            j+=1
            i+=1
        while i < len(l1):
            res[k] = l1[i]
            k+=1
            i+=1
        while j < len(l2):
            res[k] = l2[j]
            k+=1
            j+=1
    return res
arr1 = [1,2,3,4]
arr2 = [5,6,7,8]
print(merge_two_arrays(arr1, arr2))

