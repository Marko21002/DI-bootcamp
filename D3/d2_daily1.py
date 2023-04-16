import math

class Pagination:

    def __init__(self, items: list = None, page_size: int = 10) -> None:
        if items is not None:
            self.items = items
        else:
            self.items = []
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        start_idx = self.current_idx * self.page_size
        end_idx = start_idx  + self.page_size
        return self.items[start_idx : end_idx]

    def go_to_page(self, page_num: int):
        
        if page_num > self.total_pages or page_num < 1: 
            raise ValueError(f"Incorrect page number - {page_num}. Available - {self.total_pages}")

        self.current_idx = page_num - 1

    def first_page(self):
        self.go_to_page(1)
        return self
    
    def last_page(self):
        self.go_to_page(self.total_pages)
        return self
    
    def next_page(self):
        self.go_to_page(self.current_idx + 2)
        return self

    def previous_page(self):
        self.go_to_page(self.current_idx)
        return self

    # dunder method - double underscore under method
    def __str__(self) -> str:
        out = ""
        visible_items = self.get_visible_items()
        for item in visible_items:
            out += f'{item}\n'
        return out

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination()

print(p.items)

p.items.extend(alphabetList)
p = Pagination()

print(p.items)


# p_str = str(p)

# print(p_str)

