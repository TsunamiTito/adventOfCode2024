import re

def check_safety_levels(input):
    count = 0
    inputarray = input.splitlines()
    index = 0
    for line in inputarray:
        safety = True
        reactor_level = interprate_row(line)
        if check_only_ascending_or_descending_or_zero(reactor_level):
            if is_ascending(reactor_level):
                if check_safe_ascending(reactor_level):
                    count += 1
            elif check_safe_descending(reactor_level):
                count +=1
    return count

def is_ascending(list):
    if list[1] - list[0] > 0:
        return True

def interprate_row(line):
    line_no_spaces = re.findall(r'\d{1,2}', line)

    array = [int(value) for value in line_no_spaces]
    return array

def check_only_ascending_or_descending_or_zero(line):
    if line[1] - line[0] > 0:
        direction = "ascending"
    elif line[1] - line[0] < 0:
        direction = "descending"
    else:
        direction = "same"

    count = 2

    for place in line[:-2]:
        if line[count] - line[count-1] > 0:
            new_direction = "ascending"
        elif line[count] - line[count-1] < 0:
            new_direction = "descending"
        else:
            new_direction = "same"



        if direction != new_direction:
            return False

        count+=1

    return True

def check_safe_ascending(line):
    last = line[0]
    for number in line[1:]:
        if number - last > 3:
            return False

        last = number
    return True

def check_safe_descending(line):
    last = line[0]
    for number in line[1:]:
        if number - last < -3:
            return False
        last = number
    return True