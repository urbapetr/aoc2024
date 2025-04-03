import re


def fun1(input):
    answer = 0
    with open(input) as lines:
        muls = []
        for line in lines:
            muls += re.findall("mul\([0-9]+,[0-9]+\)", line)
        for mul in muls:
            num = re.findall("[0-9]+", mul)
            answer += int(num[0]) * int(num[1])
    print(answer)

def fun2(input):
    answer = 0
    with open(input) as lines:
        all_lines = ""
        muls = []
        for line in lines:
            all_lines += line
        all_lines = all_lines.split("do()")
        l = 0
        for yes in all_lines:
            yes = yes.split("don't()")
            muls = re.findall("mul\([0-9]+,[0-9]+\)", yes[0])
            for mul in muls:
                num = re.findall("[0-9]+", mul)
                answer += int(num[0]) * int(num[1])

    print(answer)
input = "input.txt"
fun1(input)
fun2(input)


