count = 0

def knapsack(capacity, weights, values, lookup_table=None):
    global count

    def sackknap(pos, selected):
        global count
        count += 1
        
        # Calculate total value and weight of selected items
        total_value = 0
        total_weight = 0
        for i in selected:
            total_value += values[i]
            total_weight += weights[i]

        # Base case: Stop if overweight
        if total_weight > capacity:
            return 0  # Invalid selection, return value as 0

        # Base case: No items left
        if pos >= len(weights):
            return total_value

        # Recursive case
        ans1 = sackknap(pos + 1, selected + [pos])  # Include current item
        ans2 = sackknap(pos + 1, selected)          # Exclude current item

        return max(ans1, ans2)

    # Start recursion from position 0 with an empty selection
    max_value = sackknap(0, [])
    return max_value

if __name__ == "__main__":
    # The following lines call the function and print the return value to the console.
    result = knapsack(50, (10, 20, 30), (60, 100, 120))
    print("The maximum value in the knapsack is:", result)
    print("Number of function calls:", count)
