def move_snake(grid, x, y, path, trail_char="*"):
    
    grid_height = len(grid)
    grid_width = len(grid[0])
    
    
    x %= grid_width
    y %= grid_height

    
    grid[y][x] = trail_char
    
    
    for move in path.lower():
        if move == "u":  
            y = (y - 1) % grid_height
        elif move == "d":  
            y = (y + 1) % grid_height
        elif move == "l":  
            x = (x - 1) % grid_width
        elif move == "r":  
            x = (x + 1) % grid_width
        else:
            continue 
        
        
        grid[y][x] = trail_char
    
    return grid


grid = [[" " for _ in range(10)] for _ in range(5)]  
x, y = 3, 5  
path = "uurrdll"  


result = move_snake(grid, x, y, path)


for row in result:
    print("".join(row))
