def fun1(input):
    answer = 0
    all_locks = []
    all_keys = []
    with open(input) as lines:
        current = []
        for line in lines:
            line = line.rstrip()
            if line == "":
                if current[0][0] == "#":
                    all_locks.append(current)
                else:
                    all_keys.append(current)
                current = []
            else:
                current.append(list(line))
    tansponse_locks = []
    for lock in all_locks:
        new_lock = []
        transpose(lock, new_lock)
        tansponse_locks.append(new_lock)
    all_locks = tansponse_locks

    tansponse_keys = []
    for key in all_keys:
        new_key = []
        transpose(key, new_key)
        tansponse_keys.append(new_key)
    all_keys = tansponse_keys

    for lock in all_locks:
        for key in all_keys:
            fit = True
            for i in range(len(lock)):
                if lock[i].count("#") + key[i].count("#") > 7:
                    fit = False
                    break
            if fit:
                answer += 1


    print(answer)


def transpose(l1, l2):
    # iterate over list l1 to the length of an item
    for i in range(len(l1[0])):
        # print(i)
        row = []
        for item in l1:
            # appending to new list with values and index positions
            # i contains index position and item contains values
            row.append(item[i])
        l2.append(row)
    return l2

def fun2(input):
    answer = 0
    with open(input) as lines:
        for line in lines:
            line = line.rstrip()

    print(answer)

input = "input.txt"
fun1(input)
fun2(input)