from operator import length_hint


class Maze:
    def __init__(self, input):
        self.maze = []

        with open(input) as f:
            lines = [line.rstrip() for line in f]

        for space in lines:
            self.maze.append(list(space))

    def get_element(self, row, col):
        print("x length" + str(len(self.maze)))
        print("y length" + str(len(self.maze[0])))

        if row < 0:
            return None
        if row >= len(self.maze):
            return None
        if col < 0:
            return None
        if col >= len(self.maze[0]):
            return None
        return self.maze[row][col]

    def print_maze(self):
        for i in range(len(self.maze)):
            print("".join(self.maze[i]))