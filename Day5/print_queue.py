from page import page


def create_page(string_input, rules_book) -> page:
    numbers = string_input.split("|")
    possible_new_page = str(numbers[0])
    new_rule = numbers[1]

    if len(rules_book) == 0:
        rules_book[possible_new_page] = [new_rule]
    else:
        if possible_new_page not in rules_book.keys():
            rules_book[possible_new_page] = [new_rule]
        else:
            rules_book[possible_new_page] += [new_rule]

    return rules_book

def create_page_rules(lines):
    split_lines = lines.splitlines()
    rules_book = {}
    for line in split_lines:
        rules_book = create_page(line, rules_book)
    return rules_book
