def read_split_line(line):
    target, right= line.split(": ")
    values = right.split(" ")
    list_of_numbers = []
    for num in values:
        number = int(num)
        list_of_numbers.append(number)
    return [int(target), list_of_numbers]

def is_line_true(bridge):
    target = bridge[0]
    numbers = bridge[1]

    first_value = numbers[0]

    result = []

    for num in numbers[1:]:
        result.append(num * first_value)
        result.append(num + first_value)

    if target in result:
        return True

    return False