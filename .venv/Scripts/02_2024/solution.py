def fun1(input):
    answer = 0
    with open(input) as lines:
        for line in lines:
            line = line.rstrip().split()
            line = [int(i) for i in line]
            inc = all(i < j for i, j in zip(line, line[1:]))
            dec = res = all(i > j for i, j in zip(line, line[1:]))
            if inc or dec:
                diff = all(1 <= abs(i-j) <= 3 for i, j in zip(line, line[1:]))
                if diff:
                    answer += 1
    print(answer)

def check_safe(line, answer):
    inc = all(i < j for i, j in zip(line, line[1:]))
    dec = res = all(i > j for i, j in zip(line, line[1:]))
    if inc or dec:
        diff = all(1 <= abs(i - j) <= 3 for i, j in zip(line, line[1:]))
        if diff:
            answer[0] += 1
            return True
    return False

def fun2(input):
    answer = [0]
    with open(input) as lines:
        for line in lines:
            line = line.rstrip().split()
            line = [int(i) for i in line]
            if check_safe(line, answer):
                continue
            for i, data in enumerate(line):
                cp = line[:]
                del cp[i]
                if check_safe(cp, answer):
                    break

    print(answer[0])

input = "input.txt"
fun1(input)
fun2(input)


