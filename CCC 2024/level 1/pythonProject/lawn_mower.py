

def get_width_and_height(line):

    crt_height = 0
    max_height = 0
    min_height = 0

    crt_width = 0
    max_width = 0
    min_width = 0

    line = line.strip()
    for direction in line:
        if direction == "W":
            crt_height += 1
        if direction == "D":
            crt_width += 1
        if direction == "S":
            crt_height -= 1
        if direction == "A":
            crt_width -= 1

        if crt_height > max_height:
            max_height = crt_height
        if crt_height < min_height:
            min_height = crt_height
        if crt_width > max_width:
            max_width = crt_width
        if crt_width < min_width:
            min_width = crt_width

    return max_width - min_width + 1, max_height - min_height + 1


def validate_path(width, height, lawn, path, initial_coordinate):
    def copy_coordinate(coordinate):
        return [x for x in coordinate]

    if len(path) != width * height - 2:
        return False

    coordinate_list = [initial_coordinate]
    for direction in path:
        crt_coordinate = copy_coordinate(coordinate_list[-1])
        if direction == "W":
            crt_coordinate[0] -= 1
        if direction == "D":
            crt_coordinate[1] += 1
        if direction == "S":
            crt_coordinate[0] += 1
        if direction == "A":
            crt_coordinate[1] -= 1
        x = crt_coordinate[0]
        y = crt_coordinate[1]
        if crt_coordinate in coordinate_list:
            return False
        if x < 0 or y < 0 or x >= height or y >= width:
            return False
        if lawn[x][y] == 'X':
            return False
        coordinate_list.append(crt_coordinate)
    return True


def validate_path_unknown_start(width, height, lawn, path):
    i = 0
    while i < height:
        j = 0
        while j < width:
            if validate_path(width, height, lawn, path, [i, j]):
                return True
            j += 1
        i += 1
    return False


def get_tree_coordinate(width, height, lawn):
    i = 0
    while i < height:
        j = 0
        while j < width:
            if lawn[i][j] == 'X':
                return [i, j]
            j += 1
        i += 1
    return [0, 0]


def rotate_clockwise_and_get_tree(width, height, tree_coordinate):
    y = height - tree_coordinate[0] - 1
    x = tree_coordinate[1]
    return [x, y]


def rotate_clockwise_path(path):
    s1 = path.replace('W', 'i')
    s2 = s1.replace('D', 'l')
    s3 = s2.replace('S', 'k')
    s4 = s3.replace('A', 'j')

    s5 = s4.replace('i', 'D')
    s6 = s5.replace('l', 'S')
    s7 = s6.replace('k', 'A')
    s8 = s7.replace('j', 'W')

    return s8


def rotate_counter_clockwise_and_get_tree(width, height, tree_coordinate):
    y = tree_coordinate[0]
    x = width - tree_coordinate[1] - 1
    return [x, y]


def plan_c(width, height, lawn):
    return "Nu se mai poate in stilul asta!"


def plan_b(width, height, lawn):
    tree_coordinate = get_tree_coordinate(width, height, lawn)

    number_of_right_turns = 0

    while tree_coordinate[0] % 2 == 1 or tree_coordinate[1] % 2 == 1 or (width - tree_coordinate[1]) % 2 == 0:
        tree_coordinate = rotate_clockwise_and_get_tree(width, height, tree_coordinate)
        width, height = height, width
        number_of_right_turns += 1

        if number_of_right_turns == 4:
            return plan_c(width, height, lawn)

    tree_x = tree_coordinate[0]
    tree_y = tree_coordinate[1]
    x = tree_x
    y = tree_y + 1

    coordinate_list = [[x, y]]

    while y + 1 < width:
        y += 1
        coordinate_list.append([x, y])

    if tree_x % 2 == 0:
        while y > tree_y:
            while x > 0:
                x -= 1
                coordinate_list.append([x, y])
            y -= 1
            coordinate_list.append([x, y])
            while x + 1 < tree_x:
                x += 1
                coordinate_list.append([x, y])
            y -= 1
            coordinate_list.append([x, y])

        while x > 0:
            x -= 1
            coordinate_list.append([x, y])

        x_increment = -1
        while x - 1 < tree_x:
            if x_increment == -1:
                while y > 0:
                    y -= 1
                    coordinate_list.append([x, y])
                x += 1
                coordinate_list.append([x, y])
            else:
                while y + 1 < tree_y:
                    y += 1
                    coordinate_list.append([x, y])
                x += 1
                coordinate_list.append([x, y])
            x_increment *= -1

        while x < height:
            while y + 1 < width:
                y += 1
                coordinate_list.append([x, y])
            x += 1
            coordinate_list.append([x, y])
            while y > 0:
                y -= 1
                coordinate_list.append([x, y])
            x += 1
            coordinate_list.append([x, y])
    else:
        pass

    target_length = width * height - 1
    while len(coordinate_list) > target_length:
        coordinate_list.pop()

    path = ""

    i = 1
    while i < len(coordinate_list):
        if coordinate_list[i][0] < coordinate_list[i - 1][0]:
            path += 'W'
        if coordinate_list[i][1] > coordinate_list[i - 1][1]:
            path += 'D'
        if coordinate_list[i][0] > coordinate_list[i - 1][0]:
            path += 'S'
        if coordinate_list[i][1] < coordinate_list[i - 1][1]:
            path += 'A'
        i += 1

    while number_of_right_turns % 4 != 0:
        number_of_right_turns += 1
        path = rotate_clockwise_path(path)

    return path


def generate_path(width, height, lawn):
    tree_coordinate = get_tree_coordinate(width, height, lawn)

    number_of_right_turns = 0

    while tree_coordinate[0] % 2 == 0 or tree_coordinate[1] % 2 == 0:
        tree_coordinate = rotate_clockwise_and_get_tree(width, height, tree_coordinate)
        width, height = height, width
        number_of_right_turns += 1

        if number_of_right_turns == 4:
            return plan_b(width, height, lawn)

    tree_x = tree_coordinate[0]
    tree_y = tree_coordinate[1]
    x = tree_x + 1
    y = tree_y

    coordinate_list = [[x, y]]

    while x + 1 < height:
        x += 1
        coordinate_list.append([x, y])

    if tree_y % 2 == 1:
        y -= 1
        coordinate_list.append([x, y])
        while x > 1:
            x -= 1
            coordinate_list.append([x, y])
        while y - 1 >= 0:
            y -= 1
            coordinate_list.append([x, y])
            while x + 1 < height:
                x += 1
                coordinate_list.append([x, y])
            y -= 1
            coordinate_list.append([x, y])
            while x > 1:
                x -= 1
                coordinate_list.append([x, y])
        x -= 1
        coordinate_list.append([x, y])
        while y < tree_y:
            y += 1
            coordinate_list.append([x, y])

        if tree_x % 2 == 1:
            while y + 1 < width:
                y += 1
                coordinate_list.append([x, y])
            x += 1
            coordinate_list.append([x, y])
            while x < tree_x:
                while y > tree_y:
                    y -= 1
                    coordinate_list.append([x, y])
                x += 1
                coordinate_list.append([x, y])
                while y + 1 < width:
                    y += 1
                    coordinate_list.append([x, y])
                x += 1
                coordinate_list.append([x, y])

            y_increment = -1
            while x < height:
                if y_increment == -1:
                    while y + y_increment > tree_y:
                        y += y_increment
                        coordinate_list.append([x, y])
                    x += 1
                    coordinate_list.append([x, y])
                else:
                    while y + 1 < width:
                        y += 1
                        coordinate_list.append([x, y])
                    x += 1
                    coordinate_list.append([x, y])
                y_increment *= -1
        else:
            pass
    else:
        pass

    target_length = width * height - 1
    while len(coordinate_list) > target_length:
        coordinate_list.pop()

    path = ""

    i = 1
    while i < len(coordinate_list):
        if coordinate_list[i][0] < coordinate_list[i - 1][0]:
            path += 'W'
        if coordinate_list[i][1] > coordinate_list[i - 1][1]:
            path += 'D'
        if coordinate_list[i][0] > coordinate_list[i - 1][0]:
            path += 'S'
        if coordinate_list[i][1] < coordinate_list[i - 1][1]:
            path += 'A'
        i += 1

    while number_of_right_turns % 4 != 0:
        number_of_right_turns += 1
        path = rotate_clockwise_path(path)

    return path


def run():
    for i in range(6):
        with open(f'output4/level4_{i}.out', 'w') as output:
            with open(f'input4/level4_{i}.in', 'r') as input:
                no_lines = int(input.readline())

                i = 0
                while i < no_lines:
                    line = input.readline()
                    w_h = line.strip().split()
                    w = int(w_h[0])
                    h = int(w_h[1])

                    lawn = []

                    j = 0
                    while j < h:
                        lawn_row = input.readline().strip()
                        lawn_row_data = [ch for ch in lawn_row]
                        lawn.append(lawn_row_data)
                        j += 1

                    path = generate_path(w, h, lawn)

                    output.write(path + "\n")

                    i += 1


run()
