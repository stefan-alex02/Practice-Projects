example_file = "example.txt"
test_file = "test.txt"

def part_one():
    r = 12
    g = 13
    b = 14
    ids_sum = 0
    with open(test_file) as f:
        id = 0
        for line in [l.strip() for l in f]:
            id += 1
            max_r = max_g = max_b = 0
            possible = True
            game = line.split(':')[1]
            for round in [r.strip() for r in game.split(';')]:
                for cube in [c.strip() for c in round.split(',')]:
                    count, cube_name = int(cube.split(' ')[0]), cube.split(' ')[1]
                    match cube_name:
                        case 'red':
                            max_r = max(max_r, count)
                        case 'green':
                            max_g = max(max_g, count)
                        case 'blue':
                            max_b = max(max_b, count)
                if max_r > r or max_g > g or max_b > b:
                    possible = False
                    break
            if possible:
                ids_sum += id
        print(ids_sum)

def part_two():
    sum = 0
    with open(test_file) as f:
        id = 0
        for line in [l.strip() for l in f]:
            id += 1
            max_r = max_g = max_b = 0
            game = line.split(':')[1]
            for round in [r.strip() for r in game.split(';')]:
                for cube in [c.strip() for c in round.split(',')]:
                    count, cube_name = int(cube.split(' ')[0]), cube.split(' ')[1]
                    match cube_name:
                        case 'red':
                            max_r = max(max_r, count)
                        case 'green':
                            max_g = max(max_g, count)
                        case 'blue':
                            max_b = max(max_b, count)
            power = max_r * max_g * max_b
            sum += power
        print(sum)

part_two()