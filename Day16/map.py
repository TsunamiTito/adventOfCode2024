from operator import length_hint


class Maze:
    def __init__(self, input):
        self.maze = []

        with open(input) as f:
            lines = [line.rstrip() for line in f]

        for space in lines:
            self.maze.append(list(space))

    def get_element(self, row, col):
        return self.maze[row][col]

    def print_maze(self):
        for i in range(len(self.maze)):
            print("".join(self.maze[i]))