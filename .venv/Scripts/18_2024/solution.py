from math import inf
import heapq

class Vektor2D:
    def __init__(self, place, x, y):
        self.place = place
        self.x = x
        self.y = y
        self.visited = False
        self.best_route = inf

def fun1(input):
    answer = 0
    with open(input) as lines:
        byte_map = []
        for line in lines:
            line = line.rstrip()
            byte_map.append(line.split(","))
        maze, maze_maping = create_maze(byte_map)
        start = (0,0)
        maze_maping.get(start).best_route = 0
        queue = [start]
        while queue:
            x,y = heapq.heappop(queue)
            vektor = maze_maping.get((x,y))
            vektor.visited = True

            for neighbor_x, neighbor_y in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                neighbor_x += x
                neighbor_y += y
                if (neighbor_x, neighbor_y) not in maze_maping or maze_maping.get((neighbor_x, neighbor_y)).place == "#":
                    continue
                neighbor = maze_maping.get((neighbor_x, neighbor_y))
                new_best = vektor.best_route + 1
                if new_best <  neighbor.best_route:
                    neighbor.best_route = new_best
                    heapq.heappush(queue, (neighbor.x,neighbor.y))

    print(maze_maping.get((70,70)).best_route)

def create_maze(byte_map):
    maze_maping = dict()
    maze = [["." for _ in range(71)] for _ in range(71)]
    for i,b in enumerate(byte_map):
        if i == 2876:
            print(b[0] + "," + b[1])
            break
        x, y = int(b[0]), int(b[1])
        maze[y][x] = "#"
    for x, row in enumerate(maze):
        for y, ch in enumerate(row):
            maze_maping[(x,y)] = Vektor2D(ch, x, y)
    return maze, maze_maping

def fun2(input):
    answer = 0
    with open(input) as lines:
        byte_map = []
        for line in lines:
            line = line.rstrip()
            byte_map.append(line.split(","))
        expand = 1024
        while True:
            expand += 1
            maze_maping = dict()
            maze = create_and_expand_maze(byte_map, maze_maping, expand)
            start = (0,0)
            maze_maping.get(start).best_route = 0
            queue = [start]
            while queue:
                x,y = heapq.heappop(queue)
                vektor = maze_maping.get((x,y))
                vektor.visited = True

                for neighbor_x, neighbor_y in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    neighbor_x += x
                    neighbor_y += y
                    if (neighbor_x, neighbor_y) not in maze_maping or maze_maping.get((neighbor_x, neighbor_y)).place == "#":
                        continue
                    neighbor = maze_maping.get((neighbor_x, neighbor_y))
                    new_best = vektor.best_route + 1
                    if new_best < neighbor.best_route:
                        neighbor.best_route = new_best
                        heapq.heappush(queue, (neighbor.x,neighbor.y))
            if maze_maping.get((70,70)).best_route == inf:
                return

    print(maze_maping.get((70,70)).best_route)

def create_and_expand_maze(byte_map, maze_maping, expand):
    maze = [["." for _ in range(71)] for _ in range(71)]
    for i,b in enumerate(byte_map):
        if i == expand:
            break
        x, y = int(b[0]), int(b[1])
        maze[y][x] = "#"
    for x, row in enumerate(maze):
        for y, ch in enumerate(row):
            maze_maping[(x,y)] = Vektor2D(ch, x, y)
    return maze, maze_maping

input = "input.txt"
fun1(input)
#fun2(input)