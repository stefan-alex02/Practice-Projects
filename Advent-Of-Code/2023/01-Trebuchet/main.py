
# PART ONE
def part_one():
    example_file = 'example_part_one.txt'
    test_file = 'test.txt'

    with open(test_file) as f:
        sum = 0
        for line in f.readlines() :
            first_digit = ord(next((i for i in line if i.isdigit()), 0)) - ord('0')
            second_digit = ord(next((i for i in line[::-1] if i.isdigit()), 0)) - ord('0')
            sum += first_digit * 10 + second_digit
        print(sum)


numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def search_digit(line: str, reverse: bool) -> int:
    if not reverse:
        i = 0
        step = 1
    else:
        i = len(line) - 1
        step = -1

    match = None
    while match is None:
        if line[i].isdigit():
            return ord(line[i]) - ord('0')
        j = i
        remaining = numbers.keys()
        while match is None and remaining and j < len(line):
            remaining = [n for n in remaining if n.startswith(line[i:j + 1])]
            match = next((n for n in remaining if n == line[i:j + 1]), None)
            j += 1
        i += step
    return numbers[match]


def find_number_in_line(line: str) -> int:
    first_digit = search_digit(line, False)
    second_digit = search_digit(line, True)
    return first_digit * 10 + second_digit


def part_two():
    example_file = 'example_part_two.txt'
    test_file = 'test.txt'

    with open(test_file) as f:
        sum = 0
        for line in f.readlines() :
            sum += find_number_in_line(line)
        print(sum)

part_one()
part_two()