knapsack_weight = 20
knapsack_amount = 3
knapsack = [['n1', 25, 15], ['n2', 24, 13], ['n3', 15, 5]]

# function
def sort_knapsack(ks):
    sorted_knapsack = sorted(ks, key=lambda x: x[1] / x[2], reverse=True)
    return sorted_knapsack

def put_knapsack(sks):
    result = []
    space = knapsack_weight
    for i in range(knapsack_amount):
        if sks[i][2] <= space:
            result.append(f'{sorted_knapsack[i][0]} x1')
            space -= sks[i][2]
        else:
            fraction = space / sks[i][2]
            result.append(f'{sorted_knapsack[i][0]} x{fraction:.2f}')
            space = 0
    return result

# main program
sorted_knapsack = sort_knapsack(knapsack)
solution = put_knapsack(sorted_knapsack)

print(solution)
