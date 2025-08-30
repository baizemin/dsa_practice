def knapsack(values,weights,capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity+1)]for _ in range(n+1)]
    for i in range(1,n+1):
        curr_weight = weights[i-1]
        curr_value = values[i-1]
        for w in range(1,capacity+1):
            if curr_weight > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], curr_value+dp[i-1][w-curr_weight])
    return dp[n][capacity]

weights_ = [10, 20, 30]
values_ = [60, 100, 120]
capacity_ = 50
res = knapsack(values_,weights_,capacity_)
print(res)
