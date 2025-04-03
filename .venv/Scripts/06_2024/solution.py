rotation_dict = {'^': (-1, 0, '>'),
                 '>': (0, 1, 'v'),
                 'v': (1, 0, '<'),
                 '<': (0, -1, '^'),}
save_X = []

def fun1(input):
    answer = 0
    with open(input) as f:
        guard_y = 0
        guard_x = 0
        garden = []
        for y, line in enumerate(f):
            garden.append(list(line.rstrip()))
            if "^" in line:
                guard_y = y
                guard_x = line.index("^")

        while True:
            guard_y,guard_x, out_of_range = move_guard(garden, guard_y,guard_x)
            if out_of_range:
                garden[guard_y][guard_x] = "X"
                break
        for g in garden:
            answer += g.count("X")

    print(answer)

def move_guard(garden, y, x):
    poss = garden[y][x]
    add_y, add_x, new_poss = rotation_dict.get(poss)
    new_y = y + add_y
    new_x = x + add_x

    while garden[new_y][new_x] != "#":
        garden[y][x] = "X"
        save_X.append((y,x))
        garden[new_y][new_x] = poss

        y,x = new_y, new_x
        add_y, add_x, new_poss = rotation_dict.get(poss)
        new_y = y + add_y
        new_x = x + add_x
        if new_y >= len(garden) or new_x >= len(garden[0]) or new_y < 0 or new_x < 0:
            return y,x, True
    garden[y][x] = new_poss

    return y, x, False


def fun2(input):
    answer = 0
    with open(input) as f:
        basic_y = 0
        basic_x = 0
        garden = []
        for y, line in enumerate(f):
            garden.append(list(line.rstrip()))
            if "^" in line:
                basic_y = y
                basic_x = line.index("^")

        while True:
            for (Y,X) in save_X:
                guard_y = basic_y
                guard_x = basic_x
                garden[guard_y][guard_x] = "^"
                copy_garden = garden[:]
                if copy_garden[Y][X] != ".":
                    continue
                copy_garden[Y][X] = "#"
                visited = []
                while True:
                    guard_y, guard_x, visited, out_of_range = move_guard2(garden, guard_y, guard_x, visited)
                    if out_of_range:
                        if guard_y == 0:
                            garden[guard_y][guard_x] = "X"
                            break
                        else:
                            answer += 1
                            break
                copy_garden[Y][X] = "."
        for g in garden:
            print(g)

    print(answer)

def move_guard2(garden, y, x, visited):
    poss = garden[y][x]
    add_y, add_x, new_poss = rotation_dict.get(poss)
    new_y = y + add_y
    new_x = x + add_x
    if new_y >= len(garden) or new_x >= len(garden[0]) or new_y < 0 or new_x < 0:
        return y, x, visited, True

    while garden[new_y][new_x] != "#":
        garden[y][x] = "X"
        garden[new_y][new_x] = poss
        if [(new_y,new_x), (y,x)] in visited:
            return 1,0, visited, True
        visited.append([(new_y,new_x), (y,x)])

        y,x = new_y, new_x
        add_y, add_x, new_poss = rotation_dict.get(poss)
        new_y = y + add_y
        new_x = x + add_x

        if new_y >= len(garden) or new_x >= len(garden[0]) or new_y < 0 or new_x < 0:
            return y,x, visited, True
    garden[y][x] = new_poss

    return y, x, visited, False

def try_loop(garden, y, x, poss, vstoupily):
    add_y, add_x, new_poss = rotation_dict.get(poss)
    new_y = y + add_y
    new_x = x + add_x

    garden[new_y][new_x] = "#"

input = "input.txt"
fun1(input)
fun2(input)