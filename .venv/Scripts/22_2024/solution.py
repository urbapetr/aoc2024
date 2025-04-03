def fun1(input):
    answer = 0
    numbers = []
    with open(input) as lines:
        for line in lines:
            line = line.rstrip()
            numbers.append(int(line))
    for number in numbers:
        count = number
        for i in range(2000):
            count = ((count * 64) ^ count) % 16777216
            count = ((count // 32) ^ count) % 16777216
            count = ((count * 2048) ^ count) % 16777216
        answer += count

    print(answer)

def fun2(input):
    answer = 0
    numbers = []
    bananas = dict()
    with open(input) as lines:
        for line in lines:
            line = line.rstrip()
            numbers.append(int(line))
    for number in numbers:
        count = number
        last_number = count % 10
        last_four_sequence = tuple()
        done_sequence = set()
        for i in range(2000):
            count = ((count * 64) ^ count) % 16777216
            count = ((count // 32) ^ count) % 16777216
            count = ((count * 2048) ^ count) % 16777216
            change = count % 10 - last_number
            last_number = count % 10
            if last_number == 7 and change == 3:
                a= "lol"
            if len(last_four_sequence) == 3:
                last_four_sequence = list(last_four_sequence)
                last_four_sequence.insert(0, change)
                last_four_sequence = tuple(last_four_sequence)
            if len(last_four_sequence) == 4:
                last_four_sequence = list(last_four_sequence)
                last_four_sequence.pop(0)
                last_four_sequence.append(change)
                last_four_sequence = tuple(last_four_sequence)
                if last_four_sequence == (-2, 2, -1, -1):
                    a = "lol"
                if last_four_sequence in done_sequence:
                    continue
                if last_four_sequence in bananas.keys():
                    bananas[last_four_sequence] = bananas.get(last_four_sequence) + last_number
                else:
                    bananas[last_four_sequence] = last_number
                done_sequence.add(last_four_sequence)
            else:
                last_four_sequence = list(last_four_sequence)
                last_four_sequence.append(change)
                last_four_sequence = tuple(last_four_sequence)
    largest = 0
    largest_sequence = "KYS"
    for x in bananas:
        if bananas.get(x) > largest:
            largest = bananas.get(x)
            largest_sequence = x
    print(f"{largest_sequence}: {largest}")

input = "input.txt"
#fun1(input)
fun2(input)