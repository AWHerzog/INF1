def min_domino_rotations(top, bottom):
    def check(x):
        rotations_top = rotations_bottom = 0
        for i in range(len(top)):
            if top[i] != x and bottom[i] != x:
                return -1
            elif top[i] != x:
                rotations_top += 1
            elif bottom[i] != x:
                rotations_bottom += 1
        return min(rotations_top, rotations_bottom)
    
    return check(top[0]) if (check(top[0]) != -1 or top[0] == bottom[0]) else check(bottom[0])


# The following line calls the function which will print # value to the Console.
# This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!

print(min_domino_rotations([2, 6, 2, 1, 2, 2], [5, 2, 4, 2, 3, 2]))
print(min_domino_rotations([3, 5, 1, 2, 6], [3, 6, 3, 3, 6]))