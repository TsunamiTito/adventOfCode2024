class page:
    page_number:int

    def __init__(self,x, y):
        self.page_number = x
        self.page_rule = [y]

    def get_page_number(self):
        return self.page_number

    def add_page_rule(self):
        self.page_rule.append()

