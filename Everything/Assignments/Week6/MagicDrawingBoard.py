class MagicDrawingBoard:
    def __init__(self, x: int, y: int):
        if x < 1 or y < 1:
            raise ValueError("Board dimensions must be at least 1x1")
        self.width = x
        self.height = y
        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def pixel(self, coord: tuple):
        x, y = coord
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise ValueError("Coordinates are out of bounds")
        self.board[y][x] = 1

    def rect(self, start: tuple, end: tuple):
        start_x, start_y = start
        end_x, end_y = end
        if not (0 <= start_x < end_x <= self.width and 0 <= start_y < end_y <= self.height):
            raise ValueError("Invalid rectangle coordinates")
        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                self.board[y][x] = 1

    def img(self) -> str:
        return "\n".join("".join(str(pixel) for pixel in row) for row in self.board)

    def reset(self):
        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]


if __name__ == '__main__':
    db = MagicDrawingBoard(6, 4)
    db.pixel((1, 1))
    db.rect((2, 2), (5, 4))
    img = db.img()
    print(img)
    db.reset()
    print(db.img())
