def draw(size, instructions):

    canvas = [[" " for _ in range(size)] for _ in range(size)]

    for x, y, char in instructions:
        if not 0 <= x < size:
            raise IndexError
        
        if not 0 <= y < size:
            raise IndexError
        
        if len(char) != 1:
            raise ValueError
        
        canvas[y][x] = char
    
    return "\n".join("".join(row) for row in canvas)

assert draw(1, [(0, 0, "a")]) == "a"
assert draw(2, [(0, 0, "a"), (1, 1, "b")]) == (
     "a \n"
     " b"
)
assert draw(3, [(1, 0, "a"), (0, 1, "b")]) == (
     " a \n"
     "b  \n"
     "   "
)
assert draw(5, [
  (0, 0, "a"),
  (1, 2, "a"),
  (4, 4, "b"),
  (0, 4, "a"),
  (1, 1, "a"),
  (0, 3, "a")]) == (
    "a    \n"
    " a   \n"
    " a   \n"
    "a    \n"
    "a   b"
)





    
