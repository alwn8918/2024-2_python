knapsack_weight = 13
knapsack_amount = 4
knapsack = [['1', 5, 5], ['2', 4, 6], ['3', 7, 8], ['4', 7, 4]]

knapsack.sort(key=lambda x: x[1] / x[2], reverse=True)

class Node:
    def __init__(self, profit, weight, level, bound, items):
        self.profit = profit
        self.weight = weight
        self.level = level
        self.bound = bound
        self.items = items

def get_bound(node):
    if node.weight >= knapsack_weight: