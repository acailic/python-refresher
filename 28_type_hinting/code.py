from typing import List # tuple set and etc


def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)


list_avg((123, 1))


# type hinting

class Book:
    pass


class BookShelf:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count

        """
        def hardcover(cls, name:str, page_weight:int)-> "BookShelf"
        def hardcover(cls, name:str, page_weight:int)-> Book
        """
