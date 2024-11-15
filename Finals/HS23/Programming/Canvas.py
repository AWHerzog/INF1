class Canvas:
    def __init__(self, width, height):
        # A canvas consists of *height* number of rows, so for example,
        # ... self.rows[0][0] refers to the top-left pixel
        # ... self.rows[3][5] refers to the 6th pixel on the fourth row
        self.rows = []
        for row in range(height):
            self.rows.append([" "] * width)
        # print(self.rows) given width=5 and height=2 would show:
        # [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]
        # and __str__ would return:
        #  -----
        # |     |
        # |     |
        #  -----
        # showing a canvas with two rows and 5 pixels in each row.
        # the border added by __str__ is decorative and not part of the canvas

    def __str__(self):
        # returns the canvas surrounded by a border
        return " " + "-" * len(self.rows[0]) + " \n|" + \
               "|\n|".join(''.join(row) for row in self.rows) + \
               "|\n " + "-" * len(self.rows[0]) + " "

    def pixel(self, x, y, char):
        x = x % len(self.rows[0])
        y = y % len(self.rows)
        self.rows[y][x] = char

    def draw(self, x, y, path="", char="â–ˆ"):
        if not isinstance(x, int) or \
            not isinstance(y, int) or \
            not isinstance(path, str) or \
            not isinstance(char, str) or \
            len(char) != 1:
            raise Exception
        path = path.lower()
        self.pixel(x, y, char)
        for move in path:
            move = move
            if move == "u": y -= 1
            if move == "d": y += 1
            if move == "l": x -= 1
            if move == "r": x += 1
            self.pixel(x, y, char)
