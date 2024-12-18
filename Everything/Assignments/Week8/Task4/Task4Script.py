
def move(state, direction):
    def find_player(state):
        for y, row in enumerate(state):
            x = row.find('o')
            if x != -1:
                return x, y
        return None

    def is_valid_position(x, y, state):
        return 0 <= y < len(state) and 0 <= x < len(state[0]) and state[y][x] == ' '

    if not all(char in ('#', ' ', 'o') for row in state for char in row):
        raise Warning("Invalid character in game state")
    if len(set(len(row) for row in state)) != 1:
        raise Warning("Inconsistent row lengths in game state")
    if sum(row.count('o') for row in state) != 1:
        raise Warning("Invalid number of players in game state")
    if len(state) == 0 or len(state[0]) == 0:
        raise Warning("Invalid game world size")

    player_x, player_y = find_player(state)
    if player_x is None:
        raise Warning("Player not found in game state")

    moves = {'left': (-1, 0), 'right': (1, 0), 'up': (0, -1), 'down': (0, 1)}
    if direction not in moves:
        raise Warning("Invalid move direction")
    dx, dy = moves[direction]
    new_x, new_y = player_x + dx, player_y + dy

    if not (0 <= new_x < len(state[0]) and 0 <= new_y < len(state)):
        raise Warning("Move leads out of bounds")
    if not is_valid_position(new_x, new_y, state):
        raise Warning("Move leads to an invalid position")

    new_state = list(map(list, state))  
    new_state[player_y][player_x] = ' '  
    new_state[new_y][new_x] = 'o'        
    new_state = tuple(''.join(row) for row in new_state)  

   
    possible_moves = [dir for dir, (dx, dy) in moves.items() if is_valid_position(new_x + dx, new_y + dy, new_state)]

    return new_state, tuple(sorted(possible_moves))