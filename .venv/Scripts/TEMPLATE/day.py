def fun1(input):
    answer = 0
    current = 0
    with open(input) as lines:
        for line in lines:
            line = line.rstrip()
            if line == "":
                answer = max(current, answer)
                current = 0
            else:
                current += int(line)
        answer = max(current, answer)

    print(answer)

def fun2(input):
    answer = [0,0,0]
    current = 0
    with open(input) as lines:
        for line in lines:
            line = line.rstrip()
            print(line)
            if line == "":
                print(f"current: {current}")
                if current > min(answer):
                    answer.remove(min(answer))
                    answer.append(current)
                current = 0
            else:
                current += int(line)
        print(f"current: {current}")
        if current > min(answer):
            answer.remove(min(answer))
            answer.append(current)

    print(sum(answer))

input = "input.txt"
fun1(input)
fun2(input)