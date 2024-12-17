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

def get_bound(node):
    if node.weight >= knapsack_weight:
        return 0
    
    bound = node.profit
    index = node.level + 1
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


root = Node(profit=0, weight=0, level=-1, bound=0, items=[])
print(get_bound(root))
