
# Count the number of recursive calls.
# Not relevant to solve the exercise but just to show the performance improvement.
count = 0

def knapsack(capacity, weights, values, lookup_table=None, index=0):
    global count
    count += 1

    if lookup_table is None:
        lookup_table = {}

    if capacity == 0 or index == len(weights):
        return 0

    if (capacity, index) in lookup_table:
        return lookup_table[(capacity, index)]

    exclude = knapsack(capacity, weights, values, lookup_table, index + 1)

    include = 0
    if weights[index] <= capacity:
        include = values[index] + knapsack(capacity - weights[index], weights, values, lookup_table, index + 1)

    lookup_table[(capacity, index)] = max(include, exclude)

    return lookup_table[(capacity, index)]


if __name__ == "__main__":
    # Test the function
    print("The maximum value in the knapsack is:", knapsack(50, (10, 20, 30), (60, 100, 120)))
    print("Number of function calls:", count)


