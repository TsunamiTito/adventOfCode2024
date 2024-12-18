def create_map(unmade_map):
    array_of_lines = unmade_map.splitlines()
    map = []
    for line in array_of_lines:
        row = [int(num) for num in line]
        map += [row]
    return map

def find_trail_head(map):
    x = 0
    y = 0
    for row in map:
        for spot in row:
            if spot == 0:
                target = [x, y]
            y += 1
        x += 1
        y = 0

    return target

def find_next_step(map, start_point):
    current_step = map[start_point[0]][start_point[1]]
    if map[start_point[0]][start_point[1] + 1] == current_step + 1:
        return [start_point[0], start_point[1] + 1]
    if map[start_point[0] - 1][start_point[1]] == current_step + 1:
        return [start_point[0] - 1, start_point[1]]
    if map[start_point[0]][start_point[1] - 1] == current_step + 1:
        return [start_point[0], start_point[1] - 1]
    if map[start_point[0] + 1][start_point[1]] == current_step + 1:
        return [start_point[0] + 1, start_point[1]]

def find_array_bounds(map):
    rows = len(map)
    columns = len(map[0]) if rows > 0 else 0
    return [rows, columns]

def find_trail(map, start_point, target_number, bounds):
    current_step = map[start_point[0]][start_point[1]]
    if start_point[0] != 0:
        if map[start_point[0] - 1][start_point[1]] == current_step + 1:
            if map[start_point[0] - 1][start_point[1]] == target_number:
                return [start_point[0] - 1, start_point[1]]
            return find_trail(map,[start_point[0] - 1, start_point[1]], target_number, bounds)

    if start_point[1] != bounds[1] - 1:
        if map[start_point[0]][start_point[1] + 1] == current_step + 1:
            if map[start_point[0]][start_point[1] + 1] == target_number:
                return [start_point[0],start_point[1] + 1]
            return find_trail(map,[start_point[0],start_point[1] + 1], target_number, bounds)

    if start_point[0] != bounds[0] - 1:
        if map[start_point[0] + 1][start_point[1]] == current_step + 1:
            if map[start_point[0] + 1][start_point[1]] == target_number:
                return [start_point[0] + 1, start_point[1]]
            return find_trail(map, [start_point[0] + 1, start_point[1]], target_number, bounds)

    if start_point[1] != 0:
        if map[start_point[0]][start_point[1] - 1] == current_step + 1:
            if map[start_point[0]][start_point[1] - 1] == target_number:
                return [start_point[0], start_point[1] - 1]
            return find_trail(map,[start_point[0], start_point[1] - 1], target_number, bounds)


