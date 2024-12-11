from page import page


def create_page(string_input, rules_book) -> page:
    numbers = string_input.split("|")
    possible_new_page = numbers[0]
    for single_page in rules_book:
        first_number = single_page.get_page_number()
        if first_number == possible_new_page:
            single_page.add_page_rule(numbers[1])

    return page(int(numbers[0]),int(numbers[1]))

def create_page_rules(lines):
    split_lines = lines.splitlines()
    rules_book = []
    for line in split_lines:
        rules_book.append(create_page(line, rules_book))
    return rules_book
