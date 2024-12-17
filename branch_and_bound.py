knapsack_weight = 16
knapsack_amount = 4
knapsack = [ ['n1', 40, 2], ['n2', 30, 5], ['n3', 50, 10], ['n4', 10, 5] ]

class Node:
    def __init__(self, profit, weight, level, bound, items):
        self.profit = profit
        self.weight = weight
        self.level = level
        self.bound = bound
        self.items = items

def get_bound(profit, weight, level):
    if weight >= knapsack_weight:
        return 0
    
    bound = profit
    index = level + 1
    space = knapsack_weight

    while index < knapsack_amount:
        if knapsack[index][2] <= space:
            bound += knapsack[index][1]
            space -= knapsack[index][2]
            index += 1
        else:
            fraction = space / knapsack[index][2]
            bound += knapsack[index][1] * fraction
            break

    return bound



print(get_bound(0, 0, -1))
