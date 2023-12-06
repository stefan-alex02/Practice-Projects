from typing import AnyStr


class Engine:
    matrix: list[AnyStr]
    rows: int
    columns: int

    def __init__(self, lines: list[AnyStr]):
        self.matrix = lines
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])

    def inside_matrix(self, i: int, j: int) -> bool:
        return 0 <= i < self.rows and 0 <= j < self.columns

    def is_symbol(self, row: int, column: int) -> bool:
        return self.matrix[row][column] not in ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def is_adjacent_to_symbol(self, row: int, left: int, right: int) -> bool:
        if self.inside_matrix(row, left-1) and self.is_symbol(row, left-1):
            return True
        if self.inside_matrix(row, right+1) and self.is_symbol(row, right+1):
            return True

        for j in range(left - 1, right + 2):
            if self.inside_matrix(row - 1, j) and self.is_symbol(row - 1, j):
                return True
            if self.inside_matrix(row + 1, j) and self.is_symbol(row + 1, j):
                return True

        return False


def get_number(string: str) -> (int, int):
    numbers_str = [string[:i] for i in range(1, len(string) + 1) if string[:i].isnumeric()]
    if len(numbers_str) == 0:
        return 0, 0
    number_str = max(numbers_str, key=lambda s: len(s))
    return int(number_str), len(number_str)


example_file = "example.txt"
test_file = "test.txt"
sum = 0
with open(test_file) as f:
    engine = Engine([line.strip() for line in f.readlines()])
    i = 0
    for line in engine.matrix:
        j = 0
        while j < len(line):
            number, count = get_number(line[j:])
            if count > 0:
                if engine.is_adjacent_to_symbol(i, j, j + count - 1):
                    sum += number
                    # print("Found adjacent number:", number, i, j)
                else:
                    pass
                    # print("Found number:", number)
                j += count
            else:
                j += 1
        i += 1
    print(sum)