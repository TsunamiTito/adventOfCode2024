class Raindeer:
    def __init__(self, x_start, y_start, input_map):
        self.x_position = x_start
        self.y_position = y_start
        self.raindeer_map = input_map

    def take_a_step(self):
        print(self.raindeer_map.get_element(self.y_position,self.x_position))

        if self.raindeer_map.get_element(self.y_position + 1,self.x_position) != "#":
            self.y_position -= 1
