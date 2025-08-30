def knapsack(values,weights,capacity):
    item = []
    for i in range(len(values)):
        ratio = values[i]/weights[i]
        item.append((ratio,values[i],weights[i]))
    item.sort(key=lambda x:x[0],reverse=True)
    tot = 0.0
    for ratio,value,weight in item:
        if capacity >= weight:
            capacity -= weight
            tot+=value
        else:
            fraction = capacity/weight
            tot += fraction*value
            capacity = 0
            break
    return tot

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print(knapsack(values,weights,capacity))