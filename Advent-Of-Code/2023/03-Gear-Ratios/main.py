from typing import AnyStr


class Point:
    row: int
    column: int
    visited: bool

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.visited = False


class Engine:
    matrix: list[list[AnyStr]]
    rows: int
    columns: int

    def __init__(self, lines: list[AnyStr]):
        self.matrix = [list(l) for l in lines]
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

    def explore_symbol(self, row: int, column: int) -> int:
        points = [Point(row-1, column-1), Point(row-1, column), Point(row-1, column+1), Point(row, column+1),
                  Point(row+1, column+1), Point(row+1, column), Point(row+1, column-1), Point(row, column-1)]
        numbers = []
        for p in points:
            if not p.visited:
                p.visited = True
                if self.matrix[p.row][p.column].isdigit():
                    numbers += [self.explore_number(p.row, p.column, points)]
        if len(numbers) == 2:
            return numbers[0] * numbers[1]
        else:
            return 0

    def explore_number(self, row: int, column: int, points: list[Point]) -> int:
        left = column
        while left > 0 and self.matrix[row][left-1].isdigit():
            left -= 1
            point = next((p for p in points if p.row == row and p.column == left), None)
            if point is not None:
                point.visited = True
        right = column
        while right < self.columns - 1 and self.matrix[row][right+1].isdigit():
            right += 1
            point = next((p for p in points if p.row == row and p.column == right), None)
            if point is not None:
                point.visited = True

        return int(''.join(self.matrix[row][left:right + 1]))


def get_number(string: str) -> (int, int):
    numbers_str = [''.join(string[:i]) for i in range(1, len(string) + 1) if ''.join(string[:i]).isnumeric()]
    if len(numbers_str) == 0:
        return 0, 0
    number_str = max(numbers_str, key=lambda s: len(s))
    return int(number_str), len(number_str)


example_file = "example.txt"
test_file = "test.txt"


def part_one():
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


class Number:
    number: int
    row: int
    left: int
    right: int

    def __int__(self, number, row, left, right):
        self.number = number
        self.row = row
        self.left = left
        self.right = right


def part_two():
    sum = 0
    with open(test_file) as f:
        engine = Engine([line.strip() for line in f.readlines()])
        i = 0
        for line in engine.matrix:
            j = 0
            while j < len(line):
                if engine.matrix[i][j] == '*':
                    sum += engine.explore_symbol(i, j)
                j += 1
            i += 1
        print(sum)


part_two()