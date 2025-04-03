def fun1(input):
    answer = 0
    antena_map = dict()
    whole_map = []
    nodes = []
    with open(input) as lines:
        for y, line in enumerate(lines):
            line = line.rstrip()
            whole_map.append(list(line))
            for x, ch in enumerate(line):
                if ch != ".":
                    if ch not in antena_map.keys():
                        antena_map[ch] = [(y,x)]
                    else:
                        antena_map.get(ch).append((y,x))

        for key in antena_map.keys():
            for i, antena in enumerate(antena_map.get(key)):
                for additional_antena in antena_map.get(key)[i+1:]:
                    y1, x1 = (2 * antena[0] - additional_antena[0], 2 * antena[1] - additional_antena[1])
                    y2, x2 = (2 * additional_antena[0] - antena[0], 2 * additional_antena[1] - antena[1])
                    if len(whole_map) > y1 >= 0 and len(whole_map[0]) > x1 >= 0:
                        if whole_map[y1][x1] == ".":
                            whole_map[y1][x1] = "#"
                        if (y1,x1) not in nodes:
                            nodes.append((y1,x1))
                            answer += 1
                    if len(whole_map) > y2 >= 0 and len(whole_map[0]) > x2 >= 0:
                        if whole_map[y2][x2] == ".":
                            whole_map[y2][x2] = "#"
                        if (y2, x2) not in nodes:
                            nodes.append((y2, x2))
                            answer += 1

    for X in whole_map:
        print("".join(X))
    print(answer)

def fun2(input):
    answer = 0
    antena_map = dict()
    whole_map = []
    nodes = []
    with open(input) as lines:
        for y, line in enumerate(lines):
            line = line.rstrip()
            whole_map.append(list(line))
            for x, ch in enumerate(line):
                if ch != ".":
                    answer += 1
                    nodes.append((y, x))
                    if ch not in antena_map.keys():
                        antena_map[ch] = [(y, x)]
                    else:
                        antena_map.get(ch).append((y, x))

        for key in antena_map.keys():
            for i, antena in enumerate(antena_map.get(key)):
                for additional_antena in antena_map.get(key)[i + 1:]:
                    edit1 = (antena[0] - additional_antena[0], antena[1] - additional_antena[1])
                    edit2 = (additional_antena[0] - antena[0], additional_antena[1] - antena[1])
                    y1, x1 = (antena[0] + edit1[0], antena[1] + edit1[1])
                    y2, x2 = (additional_antena[0] + edit2[0], additional_antena[1] + edit2[1])
                    while len(whole_map) > y1 >= 0 and len(whole_map[0]) > x1 >= 0:
                        if whole_map[y1][x1] == ".":
                            whole_map[y1][x1] = "#"
                        if (y1, x1) not in nodes:
                            nodes.append((y1, x1))
                            answer += 1
                        y1, x1 = (y1 + edit1[0], x1 + edit1[1])
                    while len(whole_map) > y2 >= 0 and len(whole_map[0]) > x2 >= 0:
                        if whole_map[y2][x2] == ".":
                            whole_map[y2][x2] = "#"
                        if (y2, x2) not in nodes:
                            nodes.append((y2, x2))
                            answer += 1
                        y2, x2 = (y2 + edit2[0], x2 + edit2[1])
    a = 0
    for X in whole_map:
        a += X.count("#")
        print("".join(X))
    print(a)
    print(answer)

input = "input.txt"
#fun1(input)
fun2(input)