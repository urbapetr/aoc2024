def load_input(file):
    with open(file) as f:
        return [list(line.strip()) for line in f]

def check(grid, iM, iA, iS, jM, jA, jS):
    rows, cols = len(grid), len(grid[0])
    if all(0 <= x < rows and 0 <= y < cols for x, y in [(iM, jM), (iA, jA), (iS, jS)]):
        return grid[iM][jM] == "M" and grid[iA][jA] == "A" and grid[iS][jS] == "S"
    return 0

def fun1(grid):
    rows, cols = len(grid), len(grid[0])
    answer = sum(
        check(grid, i, i, i, j-1, j-2, j-3) +
        check(grid, i-1, i-2, i-3, j-1, j-2, j-3) +
        check(grid, i-1, i-2, i-3, j, j, j) +
        check(grid, i+1, i+2, i+3, j-1, j-2, j-3) +
        check(grid, i, i, i, j+1, j+2, j+3) +
        check(grid, i+1, i+2, i+3, j+1, j+2, j+3) +
        check(grid, i+1, i+2, i+3, j, j, j) +
        check(grid, i-1, i-2, i-3, j+1, j+2, j+3)
        for i in range(rows) for j in range(cols) if grid[i][j] == "X"
    )
    print(answer)

def check_X(grid, i1, i2, j1, j2):
    rows, cols = len(grid), len(grid[0])
    if all(0 <= x < rows and 0 <= y < cols for x, y in [(i1, j1), (i2, j2)]):
        mas1 = [grid[i1][j1], grid[i2][j2]]
        mas2 = [grid[i1][j2], grid[i2][j1]]
        return (mas1 in [["M", "S"], ["S", "M"]]) and (mas2 in [["M", "S"], ["S", "M"]])
    return 0

def fun2(grid):
    rows, cols = len(grid), len(grid[0])
    answer = sum(
        check_X(grid, i-1, i+1, j-1, j+1)
        for i in range(rows) for j in range(cols) if grid[i][j] == "A"
    )
    print(answer)

grid = load_input("input.txt")
fun1(grid)
fun2(grid)
