import sys

def fun1(input):
    answer = 0
    file_system = []
    index = 0
    with open(input) as lines:
        for line in lines:
            line = line.rstrip()
            line = list(line)
            for i, num in enumerate(line):
                num = int(num)
                if i % 2 == 0:
                    for _ in range(num):
                        file_system.append(str(index))
                    index += 1
                else:
                    for _ in range(num):
                        file_system.append(".")

    sort_file(file_system)

    for i, x in enumerate(file_system):
        if x == ".":
            break
        answer += i * int(x)

    print(answer)

def sort_file(file_system):
    left = 0
    right = len(file_system) - 1
    while left < right:
        if file_system[left] == ".":
            if file_system[right] != ".":
                file_system[left] = file_system[right]
                file_system[right] = "."
            else:
                right -= 1
        else:
            left += 1


def fun2(input):
    answer = 0
    file_system = []
    index = 0
    num_map = dict()
    dots_map = []
    with open(input) as lines:
        for line in lines:
            line = line.rstrip()
            line = list(line)
            for i, num in enumerate(line):
                num = int(num)
                if i % 2 == 0:
                    map_index = []
                    for _ in range(num):
                        file_system.append(str(index))
                        map_index.append(len(file_system) - 1)
                    num_map[index] = map_index
                    index += 1
                else:
                    map_index = []
                    for _ in range(num):
                        file_system.append(".")
                        map_index.append(len(file_system) - 1)
                    dots_map.append((len(map_index), map_index))

    move_file(file_system, num_map, dots_map)

    for i, x in enumerate(file_system):
        if x == ".":
            continue
        answer += i * int(x)

    print(answer)

def move_file(file_system, num_map, dots_map):
    for num in reversed(num_map.keys()):
        indexes = num_map.get(num)
        num_len = len(indexes)
        for x, (space_len, space_index) in enumerate(dots_map):
            if space_len >= num_len:
                for _ in range(num_len):
                    file_system[space_index[0]] = str(num)
                    space_index.remove(space_index[0])
                for i in indexes:
                    file_system[i] = "."
                dots_map[x] = (len(space_index), space_index)
                break

def fun3(input):
    total = 0
    for line in open(input):
        report = [list(x for x in line.split())]
        while len([n for n in report[-1] if n == 0]) < len(report[-1]):
            report.append([report[-1][i + 1] - report[-1][i] for i in range(len(str(report[-1][-1])) - 1)])
        for i in range(len(report) - 2, -1, -1):
            report[i].append(report[i][-1] + report[i + 1][-1])
        total += report[0][-1]
    print(total)

lol = "input.txt"
fun1(lol)
fun2(lol)