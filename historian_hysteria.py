def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total


def difference_betwee_both_two_sorted_inputs(left, right):
    sorted_left = left.sort()
    sorted_right = right.sort()

    difference = 0
    index = 0
    for count in sorted_left:
        difference += find_difference_between_left_and_right(sorted_left[index],sorted_right[index])
        index += 1

    return difference


def find_difference_between_left_and_right(left, right):

    if left > right:
        return left - right
    elif right > left:
        return right - left
    else:
        return 0

def take_one_line_and_split_into_two_arrays(input):
    output = input.split("   ")
    return output

def take_string_and_transform_into_int_array(input):
    int_array = [int(num) for num in input]
    return int_array

def find_difference_one_line(input):
    split_line = take_one_line_and_split_into_two_arrays(input)
    left = take_string_and_transform_into_int_array(split_line[0])
    right = take_string_and_transform_into_int_array(split_line[1])

    return difference_betwee_both_two_sorted_inputs(left,right)

def split_lines(input):
    lines = input.splitlines()
    return lines

def the_whole_thing(input):
    list_of_lines = split_lines(input)
    count = 0

    for list in list_of_lines:
        count += find_difference_one_line(list)

    return count