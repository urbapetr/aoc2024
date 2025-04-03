import heapq

class Complex(complex):
    __lt__ = lambda s, o: (s.imag, s.real) < (o.imag, o.real)
    __add__ = lambda s, o: Complex(complex(s) + o)

def fun1(input):
    grid = {}
    with open(input) as f:
        for y, row in enumerate(f):
            for x, c in enumerate(row.strip()):
                grid[Complex(x, y)] = c

    start = next(z for z in grid if grid[z] == 'S')
    end = next(z for z in grid if grid[z] == 'E')

    queue = [(0, start, 1, [start])]
    seen = {}
    best = set()
    low = float("inf")

    while queue:
        score, loc, face, path = heapq.heappop(queue)
        if score > low:
            break
        if loc == end:
            if low > score:
                best.clear()
            low = score
            best |= set(path)
        seen[loc, face] = score

        for d in map(Complex, (-1, 1, -1j, 1j)):
            if grid.get(loc + d, '#') == '#':
                continue
            cost = 1001 if d != face else 1
            if seen.get((loc + d, d), float("inf")) > score + cost:
                heapq.heappush(queue, (score + cost, loc + d, d, path + [loc + d]))

    print(low)
    print(len(best))

input = "input.txt"
fun1(input)
