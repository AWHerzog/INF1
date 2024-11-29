def evolve(world, steps):

    def validate_world(world):
        if not isinstance(world, tuple):
            raise Warning("World is formatted wrong")
        
        allowed_char = {"-", "|", "#", " "}
        row_length = len(world[0])

        for idx, row in enumerate(world):
            if not isinstance(row, str):
                raise Warning(f"Row {idx} is not a string")
        if len(row) != row_length:
            raise Warning(f"Row {idx} has inconsistent length")
        
        for char in row:
            if char not in allowed_char:
                return Warning(f"Invalid character '{char}' found in row {idx}")








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