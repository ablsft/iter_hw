class FlatIterator:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
    
    def __iter__(self):
        self.flat_list = []
        self.index = 0
        for list in self.list_of_lists:
            self.flat_list += list
        return self
    
    def __next__(self):
        if self.index > len(self.flat_list) - 1:
            raise StopIteration
        item = self.flat_list[self.index]
        self.index += 1
        return item
    
def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()