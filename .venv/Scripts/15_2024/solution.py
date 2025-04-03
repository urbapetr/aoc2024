movin = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
f = open("my_file.txt", "w")

def fun1(input):
    answer = 0
    map = []
    is_map = True
    movement = ""
    x = -1
    y = -1
    with open(input) as lines:
        for i, line in enumerate(lines):
            line = line.rstrip()
            if line == "":
                is_map = False
                continue
            if is_map:
                map.append(list(line))
                if "@" in line:
                    x = line.index("@")
                    y = i
            else:
                movement += line
        move_robot(map, x, y, movement)
    for y, row in enumerate(map):
        for x, col in enumerate(row):
            if col == "O":
                answer += 100*y+x
    print(answer)

def move_robot(warehouse, x, y, movements):
    for move in movements:
        f.write(f"{move} \n")
        for row in warehouse:
            f.write("".join(row) + "\n")

        f.write(f"----------------------------------------- \n")
        add_x, add_y = movin.get(move)
        if try_move(warehouse, x + add_x, y + add_y, "@", add_x, add_y):
            warehouse[y][x] = "."
            y += add_y
            x += add_x
            warehouse[y][x] = "@"

def try_move(warehouse, x, y, moving_block, add_x, add_y):
    if warehouse[y][x] == ".":
        warehouse[y][x] = moving_block
        return True
    if warehouse[y][x] == "#":
        return False
    if try_move(warehouse, x + add_x, y + add_y, warehouse[y][x], add_x, add_y):
        warehouse[y][x] = moving_block
        return True
    return False


def fun2(input):
    answer = 0
    map = []
    is_map = True
    movement = ""
    x = -1
    y = -1
    with open(input) as lines:
        for i, line in enumerate(lines):
            new_line = ""
            line = line.rstrip()
            if line == "":
                is_map = False
                continue
            if is_map:
                for ch in line:
                    if ch == "#":
                        new_line += "##"
                    elif ch == "O":
                        new_line += "[]"
                    elif ch == "@":
                        new_line += "@."
                    elif ch == ".":
                        new_line += ".."
                map.append(list(new_line))
                if "@" in new_line:
                    x = new_line.index("@")
                    y = i
            else:
                movement += line
        move_robot2(map, x, y, movement)
    for y, row in enumerate(map):
        print("".join(row))
        for x, col in enumerate(row):
            if col == "[":
                answer += 100*y+x
    print(answer)

def force_move(warehouse, x, y, moving_block, add_x, add_y):
    x2 = x
    y2 = y
    if warehouse[y][x] == "[":
        x2 = x + 1
    if warehouse[y][x] == "]":
        x2 = x - 1
    if warehouse[y][x] == ".":
        return True
    if warehouse[y][x] == "#":
        return False
    if (force_move(warehouse, x + add_x, y + add_y, warehouse[y][x], add_x, add_y) and
            force_move(warehouse, x2 + add_x, y2 + add_y, warehouse[y2][x2], add_x, add_y)):
        warehouse[y + add_y][x + add_x] = warehouse[y][x]
        warehouse[y2 + add_y][x2 + add_x] = warehouse[y2][x2]
        warehouse[y][x] = "."
        warehouse[y2][x2] = "."
        return True
    return False

def move_robot2(warehouse, x, y, movements):
    for move in movements:
        if x == 10 and y == 7:
            a = ""
        f.write(f"{move}\n")
        for row in warehouse:
            f.write("".join(row) + "\n")
        f.write(f"----------------------------------------- \n")
        add_x, add_y = movin.get(move)
        up = False
        if move == "v" or move == "^":
            up = True
        if up:
            if try_move2(warehouse, x + add_x, y + add_y, "@", add_x, add_y):
                force_move(warehouse, x + add_x, y + add_y, "@", add_x, add_y)
                warehouse[y][x] = "."
                y += add_y
                x += add_x
                warehouse[y][x] = "@"
        else:
            if try_move(warehouse, x + add_x, y + add_y, "@", add_x, add_y):
                warehouse[y][x] = "."
                y += add_y
                x += add_x
                warehouse[y][x] = "@"

def try_move2(warehouse, x, y, moving_block, add_x, add_y):
    x2 = x
    y2 = y
    if warehouse[y][x] == "[":
        x2 = x + 1
    if warehouse[y][x] == "]":
        x2 = x - 1
    if warehouse[y][x] == ".":
        return True
    if warehouse[y][x] == "#":
        return False
    if (try_move2(warehouse, x + add_x, y + add_y, warehouse[y][x], add_x, add_y) and
            try_move2(warehouse, x2 + add_x, y2 + add_y, warehouse[y][x], add_x, add_y)):
        return True
    return False


input = "input.txt"
#input = "smallinput.txt"
#fun1(input)
input = "input.txt"
#input = "smallinput.txt"
fun2(input)