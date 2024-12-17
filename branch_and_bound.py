knapsack_weight = 16
knapsack_amount = 4
knapsack = [['n1', 40, 2], ['n2', 30, 5], ['n3', 50, 10], ['n4', 10, 5]]

knapsack = [['n1', 40, 2], ['n2', 30, 5], ['n3', 50, 10], ['n4', 10, 5]]

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

def branch_and_bound():
    root = Node(profit=0, weight=0, level=-1, bound=0, items=[])
    root.bound = get_bound(root)

    PQ = [root]
    max_profit = 0
    best_items = []

    while PQ:
        PQ.sort(key=lambda x: x.bound, reverse=True)
        node = PQ.pop(0)

        if node.bound > max_profit:
            # 왼쪽 자식 노드
            left_node = Node(profit = node.profit + knapsack[node.level+1][1],
                             weight = node.weight + knapsack[node.level+1][2],
                             level = node.level + 1,
                             bound = 0,
                             items = node.items + [knapsack[node.level+1][0]])
            left_node.bound = get_bound(left_node)

            if left_node.profit > max_profit and left_node.weight <= knapsack_weight:
                max_profit = left_node.profit
                best_items = left_node.items
            if left_node.bound > max_profit:
                PQ.append(left_node)

            # 오른쪽 자식 노드
            right_node = Node(profit = node.profit,
                              weight = node.weight,
                              level = node.level + 1,
                              bound = 0,
                              items = node.items)
            right_node.bound = get_bound(right_node)

            if right_node.bound > max_profit:
                PQ.append(right_node)

    return max_profit, best_items

# main program
max_profit, best_items = branch_and_bound()
print(f'최대 이익: {max_profit}')
print(f'선택 아이템: {best_items}')
