knapsack_weight = 13
knapsack_amount = 4
knapsack = [['n1', 40, 2], ['n2', 30, 5], ['n3', 50, 10], ['n4', 10, 5]]
solution_vector = []

# function
def put_dp_table():
    for i in range(1, knapsack_amount + 1):
        for w in range(1, knapsack_weight + 1):
            if knapsack[i-1][2] <= w:
                P[i][w] = max(
                    P[i-1][w],
                    knapsack[i-1][1] + P[i-1][w - knapsack[i-1][2]]
                )
            else:
                P[i][w] = P[i-1][w]

def get_solution_vector():
    global solution_vector
    solution_vector = [0] * knapsack_amount
    w = knapsack_weight

    for i in range(knapsack_amount, 0, -1):
        if P[i][w] != P[i-1][w]:
            solution_vector[i-1] = 1
            w -= knapsack[i-1][2]

def print_result():
    for row in P:
        print(row)

    print("Maximum profit:", P[knapsack_amount][knapsack_weight])
    print("Solution vector:", solution_vector)

# main program
P = [[0 for _ in range(knapsack_weight + 1)] for _ in range(knapsack_amount + 1)]

put_dp_table()
get_solution_vector()
print_result()
