
def sum_diagonals(matrix):
   
    primary_sum = sum(matrix[i][i] for i in range(len(matrix)))
    
    
    secondary_sum = sum(matrix[i][len(matrix) - 1 - i] for i in range(len(matrix)))
    
   
    return primary_sum + secondary_sum


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(sum_diagonals(matrix))  
