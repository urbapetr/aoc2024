from collections import deque
from functools import cache

# Definice rozložení numerické klávesnice
numpad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["X", "0", "A"]]
dirpad = [["X", "^", "A"], ["<", "v", ">"]]

numpos, dirpos = dict(), dict()

# Naplnění numpos a dirpos pro mapování znaků na souřadnice
for y, row in enumerate(numpad):
    for x, col in enumerate(row):
        numpos[col] = (x, y)

for y, row in enumerate(dirpad):
    for x, col in enumerate(row):
        dirpos[col] = (x, y)

# Funkce pro uložení nejkratší cesty mezi pozicemi numerické klávesnice
@cache
def numpath(a, b):
    seqs = []
    x, y = numpos[a]
    x1, y1 = numpos[b]
    yseq = ("^" if y > y1 else "v") * abs(y - y1)
    xseq = ("<" if x > x1 else ">") * abs(x - x1)
    if x == x1:
        seqs = ["A" + yseq + "A"]
    elif y == y1:
        seqs = ["A" + xseq + "A"]
    else:
        if numpad[y1][x] != "X":
            seqs.append("A" + yseq + xseq + "A")
        if numpad[y][x1] != "X":
            seqs.append("A" + xseq + yseq + "A")
    return seqs

# Funkce pro uložení nejkratší cesty mezi pozicemi v dirpad
@cache
def dirpath(a, b):
    seqs = []
    x, y = dirpos[a]
    x1, y1 = dirpos[b]
    yseq = ("^" if y > y1 else "v") * abs(y - y1)
    xseq = ("<" if x > x1 else ">") * abs(x - x1)
    if x == x1:
        seqs = ["A" + yseq + "A"]
    elif y == y1:
        seqs = ["A" + xseq + "A"]
    else:
        if dirpad[y1][x] != "X":
            seqs.append("A" + yseq + xseq + "A")
        if dirpad[y][x1] != "X":
            seqs.append("A" + xseq + yseq + "A")
    return seqs

# Funkce pro výpočet nákladů pro více vrstev robotického navigování
@cache
def dircost(seq, depth):
    if depth == 0:
        return len(seq) - 1
    cost = 0
    for i in range(len(seq) - 1):
        cost += min(dircost(subseq, depth - 1) for subseq in dirpath(seq[i], seq[i + 1]))
    return cost

# Funkce pro nalezení cesty robota v sekvenci na numerické klávesnici
def cnc(line, depth):
    l = "A" + line
    cost = 0
    for i in range(len(l) - 1):
        cost += min(dircost(subseq, depth) for subseq in numpath(l[i], l[i + 1]))
    return cost

# Funkce pro výpočet celkové složitosti pro seznam kódů
def compute_complexity(codes, depth):
    moves = [cnc(line, depth) for line in codes]
    nums = [int(l.rstrip("A")) for l in codes]
    return sum(m * n for m, n in zip(moves, nums))

# Příklad použití
codes = ["789A", "540A", "285A", "140A", "189A"]

# Výpočet celkové složitosti pro 2 roboty
total_complexity_2_robots = compute_complexity(codes, 2)
print(f"2 roboti: složitost = {total_complexity_2_robots}")

# Výpočet celkové složitosti pro 25 robotů
total_complexity_25_robots = compute_complexity(codes, 25)
print(f"25 robotů: složitost = {total_complexity_25_robots}")
