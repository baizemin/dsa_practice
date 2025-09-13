import sys
def kadane_algo(arr):
    maxi = sys.maxsize-1
    sum =0
    for i in range(len(arr)):
        sum += arr[i]
        if sum < maxi:
            maxi = sum
        # if sum < 0:
        #     sum = 0
    return maxi #if maxi > 0 else 0

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadane_algo(arr))