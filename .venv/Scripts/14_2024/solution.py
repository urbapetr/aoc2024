def fun1(input, width, tall):
    answer = 0
    kvartal = [0,0,
               0,0]
    robots = []
    with open(input) as lines:
        for line in lines:
            line = line.rstrip()
            robot, velo = line.split()
            x, y = robot[2:].split(",")
            x = int(x)
            y = int(y)
            vx, vy = velo[2:].split(",")
            vx = int(vx)
            vy = int(vy)
            robots.append([(x,y), (vx, vy)])

        for robot in robots:
            x,y = robot[0]
            vx,vy = robot[1]
            new_x = (x + vx * 100) % width
            new_y = (y + vy * 100) % tall
            if new_x < 0:
                new_x = width + new_x
            if new_y < 0:
                new_y = tall + new_y
            robot[0] = (new_x, new_y)
            if new_x == width // 2 or new_y == tall // 2:
                continue
            if new_x < width // 2 and new_y < tall // 2:
                kvartal[0] += 1
            if new_x > width // 2 and new_y < tall // 2:
                kvartal[1] += 1
            if new_x < width // 2 and new_y > tall // 2:
                kvartal[2] += 1
            if new_x > width // 2 and new_y > tall // 2:
                kvartal[3] += 1

    answer = 1
    for k in kvartal:
        answer *= k
    print(answer)

def fun2(input, width, tall):
    answer = 0
    robots = []
    f = open("my_file.txt", "w")
    with open(input) as lines:
        for line in lines:
            for line in lines:
                line = line.rstrip()
                robot, velo = line.split()
                x, y = robot[2:].split(",")
                x = int(x)
                y = int(y)
                vx, vy = velo[2:].split(",")
                vx = int(vx)
                vy = int(vy)
                robots.append([(x, y), (vx, vy)])

            for i in range(10000):
                map = [[" " for _ in range(width)] for _ in range(tall)]
                for robot in robots:
                    x, y = robot[0]
                    vx, vy = robot[1]
                    new_x = (x + vx) % width
                    new_y = (y + vy) % tall
                    if new_x < 0:
                        new_x = width + new_x
                    if new_y < 0:
                        new_y = tall + new_y
                    robot[0] = (new_x, new_y)
                    map[new_y][new_x] = "X"
                rows = ""
                skip = True
                for row in map:
                    row = "".join(row) + "\n"
                    rows += row
                    if "XXXXXXXXXXXX" in row:
                        skip = False
                if not skip:
                    f.write(f"{i}----------\n")
                    f.write(rows)
    print(answer)

input = "input.txt"
#fun1(input, 101, 103)
fun2(input, 101, 103)