def evolve(world, steps):

    def validate_world(world):
        # Ensure world is a tuple
        if not isinstance(world, tuple):
            raise Warning("World must be a tuple of strings.")
        
        # Ensure the world has at least 3 rows (frame included)
        if len(world) < 3:
            raise Warning("World must have at least three rows.")

        # Length of the first row to compare with the others
        row_length = len(world[0])

        allowed_chars = {"-", "|", "#", " "}

        for idx, row in enumerate(world):
            # Ensure each row is a string
            if not isinstance(row, str):
                raise Warning(f"Row {idx} is not a string.")
            
            # Ensure all rows have the same length
            if len(row) != row_length:
                raise Warning(f"Row {idx} has inconsistent length.")
            
            # Ensure only allowed characters are present
            for char in row:
                if char not in allowed_chars:
                    raise Warning(f"Invalid character '{char}' found in row {idx}.")

    def count_neighbors(world, row, col):
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),         (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        count = 0
        for dr, dc in directions:
            neighbor_row = row + dr
            neighbor_col = col + dc

            # Ensure we are within the bounds, and that we don't count frame cells
            if 1 <= neighbor_row < len(world) - 1 and 1 <= neighbor_col < len(world[0]) - 1:
                if world[neighbor_row][neighbor_col] == '#':
                    count += 1

        return count

    def apply_rules(world):
        # Create a new list to store the updated world (temporarily)
        new_world = []

        # Iterate over each row, skipping the first and last rows (frame)
        for row_idx in range(1, len(world) - 1):
            new_row = ""

            # Iterate over each column, skipping the first and last columns (frame)
            for col_idx in range(1, len(world[row_idx]) - 1):
                cell = world[row_idx][col_idx]
                neighbors = count_neighbors(world, row_idx, col_idx)

                # Apply the Game of Life rules to determine the new state of the cell
                if cell == '#' and (neighbors < 2 or neighbors > 3):
                    new_row += ' '  # Cell dies
                elif cell == '#' and (2 <= neighbors <= 3):
                    new_row += '#'  # Cell survives
                elif cell == ' ' and neighbors == 3:
                    new_row += '#'  # Cell is born
                else:
                    new_row += ' '  # Cell remains unpopulated

            # Add frame characters to the updated row
            new_row = "|" + new_row + "|"
            new_world.append(new_row)

        # Add the top and bottom frame rows to the new world
        new_world.insert(0, world[0])  # Top frame row
        new_world.append(world[-1])    # Bottom frame row

        return tuple(new_world)



    validate_world(world)
    
    # Validate steps input
    if not isinstance(steps, int) or steps < 1:
        raise Warning("Steps must be a positive integer.")
    
    # Evolution loop
    current_world = world
    for _ in range(steps):
        current_world = apply_rules(current_world)

    # Count alive cells
    alive_cells = sum(row.count('#') for row in current_world)

    return current_world, alive_cells



field = (
    "--------------",
    "|            |",
    "|   ###      |",
    "|   #        |",
    "|    #       |",
    "|            |",
    "--------------"
)
steps = 4

result, alive_cells = evolve(field, steps)
print(f"Game of Life after {steps} moves:")
for row in result:
    print(row)
print(f"{alive_cells} are alive.")