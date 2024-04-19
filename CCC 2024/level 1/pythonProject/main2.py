from collections import deque


def validate_and_generate_path(cols, rows, lawn, path, visited, start_x, start_y):
    directions = {'W': (0, -1), 'A': (-1, 0), 'S': (0, 1), 'D': (1, 0)}
    directions_rev = {(0, -1): 'W', (-1, 0): 'A', (0, 1): 'S', (1, 0): 'D'}
    stack = deque([(start_x, start_y)])

    while stack:
        x, y = stack.pop()

        if x < 0 or x >= cols or y < 0 or y >= rows or lawn[y * cols + x] == 'X' or (x, y) in visited:
            continue

        visited.append((x, y))

        if len(visited) >= 2:
            diff = (visited[-1][0] - visited[-2][0], visited[-1][1] - visited[-2][1])
            print(diff)
            path.append((x, y))

        if len(visited) == cols * rows - lawn.count('X'):
            return True

        for dir in directions.keys():
            new_x, new_y = x + directions[dir][0], y + directions[dir][1]
            stack.append((new_x, new_y))

    visited.remove((start_x, start_y))
    path.pop()

    return False


def read_input():
    for i in range(0, 1):
        with open(f'input4/level4_{i}.in') as f:
            n_lawns = int(f.readline())

            paths = []

            for j in range(n_lawns):
                cols, rows = map(int, f.readline().split())

                lawn = [f.readline().strip() for _ in range(rows)]
                lawn = [cell for row in lawn for cell in row]

                path = []
                visited = []

                for x in range(cols):
                    for y in range(rows):
                        if lawn[y * cols + x] != 'X' and not visited and validate_and_generate_path(cols, rows, lawn, path, visited, x, y):
                            break

                print(path)

                result = ' '.join(str(x) + " " + str(y) for x, y in path)

                paths.append(result)

            with open(f'output4/level4_{i}.out', 'w') as fo:
                for line in paths:
                    fo.write(line + '\n')

read_input()