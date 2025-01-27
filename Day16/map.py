class Maze:
    def __init__(self, input):
        self.maze = []

        with open(input) as f:
            lines = [line.rstrip() for line in f]

        for line in lines:
            self.maze.append(list(line))

    def print_maze(self):
        for i in range(len(self.maze)):
            print("".join(self.maze[i]))