def draw_rectangle(grid, top_left, dimensions):
    
    x, y = len(grid), len(grid[0])
    
    start_row, start_col = top_left
    
    height, width = dimensions
    
    for i in range(start_row, min(start_row + height, x)):
        for j in range(start_col, min(start_col + width, y)):
            grid[i][j] = '#'
    
    return grid    





# Example usage:
grid = [['.' for _ in range(10)] for _ in range(5)]  # 5x10 grid of '.'
top_left = (1, 2)  # Rectangle starts at row 1, column 2
dimensions = (3, 5)  # Rectangle height is 3, width is 5

result = draw_rectangle(grid, top_left, dimensions)
for row in result:
    print(''.join(row))