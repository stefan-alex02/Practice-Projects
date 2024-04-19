def count_directions(line):
    directions = {'W': 0, 'A': 0, 'S': 0, 'D': 0}
    for char in line:
        if char in directions:
            directions[char] += 1
    return list(directions.values())

def validate(cols, rows, lawn, path):
    directions = {'W': (0, -1), 'A': (-1, 0), 'S': (0, 1), 'D': (1, 0)}
    p = (0, 0)
    p_min = (0, 0)
    p_max = (0, 0)
    visited = [p]

    for char in path:
        p = tuple(map(sum, zip(p, directions[char])))

        if p in visited:
            return 'INVALID'

        visited.append(p)

        p_min = tuple(map(min, p, p_min))
        p_max = tuple(map(max, p, p_max))

    x_min, y_min = p_min
    x_max, y_max = p_max

    if cols < x_max - x_min + 1 or rows < y_max - y_min + 1:
        return 'INVALID'

    for i in range(len(visited)):
        x, y = visited[i]
        visited[i] = x - x_min, y - y_min

    for i in range(rows):
        for j in range(cols):
            if (j, i) not in visited and lawn[i][j] != 'X':
                return 'INVALID'
            if lawn[i][j] == 'X' and (j, i) in visited:
                return 'INVALID'

    return 'VALID'


def generate_path_wrapper(cols, rows, lawn, trees):
    for i in range(rows):
        for j in range(cols):
            p = (j, i)

            if lawn[i][j] == 'X':
                continue

            path = generate_path(cols, rows, lawn, [p], [], trees)

            if path:
                return path


def generate_path(cols, rows, lawn, visited, path, trees):
    directions = {'W': (0, -1), 'A': (-1, 0), 'S': (0, 1), 'D': (1, 0)}

    for dir in directions.keys():
        p = tuple(map(sum, zip(visited[-1], directions[dir])))

        if p in visited or p[0] < 0 or p[0] >= cols or p[1] < 0 or p[1] >= rows:
            continue

        if lawn[p[1]][p[0]] == 'X':
            continue

        visited.append(p)
        path.append(dir)

        # print(p, visited, ''.join(path))

        if len(visited) == cols * rows - len(trees):
            return path

        r_path = generate_path(cols, rows, lawn, visited, path, trees)

        if r_path:
            return r_path

        # print('POP', p, visited, r_path)

        visited.pop()
        path.pop()


    return []

def generate_path_better(cols, rows, lawn, visited, path, trees):
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # Up, left, down, right

    while True:
        # Get the current position
        x, y = visited[-1]

        # Find the next direction
        for i in range(len(directions)):
            dx, dy = directions[(i + 1) % len(directions)]
            p = (x + dx, y + dy)

            if p in visited or p[0] < 0 or p[0] >= cols or p[1] < 0 or p[1] >= rows:
                continue

            if lawn[p[1]][p[0]] == 'X':
                continue

            visited.append(p)
            path.append('WASD'[(i + 3) % len(directions)])
            break
        else:
            # No more directions to go, backtrack
            visited.pop()
            path.pop()

            if not visited:
                # All cells have been visited
                return path

    return []

def read_input():
    output = []
    for i in range(0, 1):
        with open(f'input4/level4_{i}.in') as f:
            lines = f.readlines()
            n_lawns = int(lines[0])

            paths = []

            cur_line = 1
            for j in range(n_lawns):
                cols, rows = map(int, lines[cur_line].split())

                lawn = [list(lines[cur_line + k + 1].strip()) for k in range(rows)]

                trees = [(j, i) for i in range(rows) for j in range(cols) if lawn[i][j] == 'X']

                cur_line += rows + 1

                path = generate_path_wrapper(cols, rows, lawn, trees)

                # path = generate_path(cols, rows, lawn, [(0, 0)], [], trees)

                print(path)

                result = validate(cols, rows, lawn, path)

                if result == 'INVALID':
                    print('ERROR')

                paths += [''.join(path)]

            with open(f'output4/level4_{i}.out', 'w') as fo:
                for line in paths:
                    fo.write(line + '\n')


read_input()
