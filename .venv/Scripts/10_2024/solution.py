def fun1(input):
    answer = 0
    map = []
    with open(input) as lines:
        for line in lines:
            line = line.rstrip()
            map.append([int(x) for x in list(line)])
        for y, row in enumerate(map):
            for x, start in enumerate(row):
                if start == 0:
                    visited = []
                    answer += check_number(map, 0, visited, y, x)

    print(answer)

def check_number(map, number, visited, y, x):
    if y < 0 or x < 0 or y >= len(map) or x >= len(map[0]):
        return 0
    if map[y][x] != number:
        return 0
    if number == 9:
        return 1

    return check_number(map, number + 1, visited, y + 1, x) + check_number(map, number + 1, visited, y, x + 1) + check_number(map, number + 1, visited, y - 1, x) + check_number(map, number + 1, visited, y, x - 1)

def fun2(input):
    answer = 0
    with open(input) as lines:
        for line in lines:
            line = line.rstrip()

    print(answer)

input = "smallinput.txt"
fun1(input)
fun2(input)