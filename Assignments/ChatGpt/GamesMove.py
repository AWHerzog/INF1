
def move(state,direction):

    acceptable_character = ['#', ' ', 'o']

    for row in state: #checking wether state consist of the correct characters
        for char in row:
            if char not in acceptable_character:
                raise Warning("Some characters in state are not allowed")
    
    row_length = len(state[0])
    for row in state:
        if len(row) != row_length:
            raise Warning("Row lengths are inconsistent")
    
    def find_player(state):
        for y, row in enumerate(state):
            x = row.find('o')
            if x != -1:
                return x,y  
        else:
            raise Warning("Player not found") 
    
    moves = {
        "left": (-1, 0),
        "right": (1, 0),
        "up": (0, -1,),
        "down": (0, 1)
    }

    x, y = find_player(state)

    if direction not in moves:
        raise Warning("Invalid move direction")

    dx, dy = moves[direction]

    new_x = x + dx
    new_y = y + dy

    if not (0 <= new_x < len(state[0]) and 0 <= new_y < len(state)):
        raise Warning("Move leads out of bounds")

    if state[new_y][new_x] == '#':
        raise Warning("Move leads to a wall")

try:
    # Test Case 1: Basic Valid Move
    state = (
        "#####",
        "# o #",
        "#   #",
        "#####"
    )
    direction = "right"
    new_state = move(state, direction)
    print("Test Case 1 Passed:", new_state == (
        "#####",
        "#  o#",
        "#   #",
        "#####"
    ))

    # Test Case 2: Move into a Wall
    state = (
        "#####",
        "#o  #",
        "#####"
    )
    direction = "left"
    try:
        move(state, direction)
        print("Test Case 2 Failed: No Warning Raised")
    except Warning as e:
        print("Test Case 2 Passed:", str(e) == "Move leads to a wall")

    # Add similar blocks for the other test cases

except Exception as e:
    print("An error occurred during testing:", e)






