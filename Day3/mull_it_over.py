import re

def find_mul(input):
    mul = re.findall("mul[(]+[0-9]{1,3},[0-9]{1,3}[)]", input)
    return mul



def perfrom_multiplication(input):
    result = 0
    for case in input:
        int_array = re.findall("[0-9]{1,3}", case)
        result += int(int_array[0]) * int(int_array[1])

    return result

def mull_over_main(input):
    all_muls = find_mul(input)
    total = perfrom_multiplication(all_muls)
    return total