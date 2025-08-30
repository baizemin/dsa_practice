def kanpsack_naive(values,weights,capacity,n):
    if capacity == 0 or n==0:
        return 0
    if weights[n-1] > capacity:
        return kanpsack_naive(values,weights,capacity,n-1)
    else:
        take = values[n-1]+kanpsack_naive(values,weights,capacity-weights[n-1],n-1)
        no_take = kanpsack_naive(values,weights,capacity,n-1)
        return max(take,no_take)
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
n = len(weights)
print(kanpsack_naive(values,weights,capacity,n))