def fun1(input):
    answer = 0
    with open(input) as lines:
        cases = []
        for line in lines:
            line = line.rstrip()
            cases.append(line.split(":"))
        for case in cases:
            vysledek = int(case[0])
            priklad = case[1].lstrip().split(" ")
            for i, c in enumerate(priklad):
                priklad[i] = int(c)
            if find_equation(vysledek, priklad, priklad[0], 1):
                answer += vysledek

    print(answer)

def find_equation(cil, priklad, vysledek, possition):
    if possition == len(priklad):
        if vysledek == cil:
            return True
        else:
            return False

    return find_equation(cil, priklad, vysledek + priklad[possition], possition + 1) or find_equation(cil, priklad, vysledek * priklad[possition], possition + 1)



def fun2(input):
    answer = 0
    with open(input) as lines:
        cases = []
        for line in lines:
            line = line.rstrip()
            cases.append(line.split(":"))
        for case in cases:
            vysledek = int(case[0])
            priklad = case[1].lstrip().split(" ")
            for i, c in enumerate(priklad):
                priklad[i] = int(c)
            if find_equation2(vysledek, priklad, priklad[0], 1):
                answer += vysledek

    print(answer)

def find_equation2(cil, priklad, vysledek, possition):
    if possition == len(priklad):
        if vysledek == cil:
            return True
        else:
            return False

    return (find_equation2(cil, priklad, vysledek + priklad[possition], possition + 1) or
            find_equation2(cil, priklad, vysledek * priklad[possition], possition + 1) or
            find_equation2(cil, priklad, int(str(vysledek) + str(priklad[possition])), possition + 1))


input = "input.txt"
fun1(input)
fun2(input)