from collections import deque


def validate_and_generate_path(cols, rows, lawn, path, visited, start_x, start_y):
    directions = {'W': (0, -1), 'A': (-1, 0), 'S': (0, 1), 'D': (1, 0)}
    stack = [(start_x, start_y, -1)]

    if (start_x < 0 or start_x >= cols or start_y < 0 or start_y >= rows or lawn[start_y * cols + start_x] == 'X' or
            (start_x, start_y) in visited):
        return False

    visited.append((start_x, start_y))

    while stack:
        x, y, d = stack[-1]

        d += 1
        stack[-1] = (x, y, d)

        if d == 4:
            visited.remove((x, y))
            stack.pop()
            continue

        dir = list(directions.keys())[d]

        new_x, new_y = x + directions[dir][0], y + directions[dir][1]

        stack.append((new_x, new_y, -1))

        print(len(stack))

        if (new_x < 0 or new_x >= cols or new_y < 0 or new_y >= rows or lawn[new_y * cols + new_x] == 'X' or
                (new_x, new_y) in visited):
            stack.pop()
            continue

        if len(visited) == cols * rows - lawn.count('X'):
            return stack

    return []


def convert_coordinates_to_directions(coords):
    directions_map = {(0, -1): 'W', (-1, 0): 'A', (0, 1): 'S', (1, 0): 'D'}
    coords = [int(n) for n in coords.split()]  # Convert string to list of integers
    path = []

    # Iterate over coordinates in pairs
    for i in range(0, len(coords) - 2, 2):
        x1, y1 = coords[i], coords[i + 1]
        x2, y2 = coords[i + 2], coords[i + 3]

        # Calculate the differences to determine the direction
        dx, dy = x2 - x1, y2 - y1
        if (dx, dy) in directions_map:
            path.append(directions_map[(dx, dy)])
        else:
            raise ValueError(f"Invalid step from ({x1}, {y1}) to ({x2}, {y2})")

    return ''.join(path)


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
                        if lawn[y * cols + x] != 'X' and not visited:
                            stack = validate_and_generate_path(cols, rows, lawn, path, visited, x, y)
                            if stack:
                                break


                directions = ['W', 'A', 'S', 'D']
                stack = [directions[d] for (_, _, d) in stack]

                print(''.join(stack))

                paths.append(''.join(stack))

            with open(f'output4/level4_{i}.out', 'w') as fo:
                for line in paths:
                    fo.write(line + '\n')

read_input()