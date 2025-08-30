def knapsack_dynamic_programming(values,weights,capacity):
    res = {}
    return knapsack_memo(values,weights,capacity,len(weights),res)
def knapsack_memo(values,weights,capacity,n,res):
    if (n,capacity) in res:
        return res[(n,capacity)]
    if n == 0 or capacity == 0:
        return 0
    if weights[n-1] > capacity:
        result =  knapsack_memo(values,weights,capacity,n-1,res)
        res[(n,capacity)] = result
        return result
    else:
        include = values[n-1]+knapsack_memo(values,weights,capacity-weights[n-1],n-1,res)
        exclude = knapsack_memo(values,weights,capacity,n-1,res)
        result= max(include,exclude)
        res[(n,capacity)] = result
        return result

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
max_val = knapsack_dynamic_programming(values,weights,capacity)
print(max_val)

