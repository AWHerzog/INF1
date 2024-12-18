def draw(size, instructions):
    if not isinstance(size, int) or size < 1:
        raise ValueError("Size must be an integer greater than or equal to 1.")
    
    canvas = [[' ' for _ in range(size)] for _ in range(size)]

    for x, y, char in instructions:
        if not (0 <= x < size) or not (0 <= y < size):
            raise IndexError(f"Coordinate ({x}, {y}) is out of bounds.")
        if not (isinstance(char, str) and len(char) == 1):
            raise ValueError(f"Invalid character '{char}'.")
        
        canvas[y][x] = char

    return '\n'.join(''.join(row) for row in canvas)



print(draw(3, [(0, 0, 'A'), (1, 1, 'B'), (2, 2, 'C')]))