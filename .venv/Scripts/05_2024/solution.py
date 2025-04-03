import re
from collections import defaultdict

one = []
two = []
def get_input():
    with open("input.txt", "r") as f:
        contents = f.read()
        rules = defaultdict(list)
        for line in contents.split("\n\n")[0].split("\n"):
            rule = line.split("|")
            rules[int(rule[1])].append(int(rule[0]))

        updates = []
        for line in contents.split("\n\n")[1].split("\n"):
            if not line:
                break
            updates.append([int(x) for x in line.split(",")])
        return rules, updates


def part_one(rules, updates):
    total = 0
    for update in updates:
        if update == [26, 33, 69, 31, 58, 88, 11, 96, 54, 23, 87]:
            a = ""
        valid = True
        for idx, num in enumerate(update):
            for num_rule in rules[num]:
                # Each number in the rules list must be before num
                if num_rule in update[idx:]:
                    valid = False
                    break
            if not valid:
                break
        else:
            one.append(update)
            total += update[len(update) // 2]
    return total

def fun1(input):
    answer = []
    with open(input) as f:
        rules, upgrades = f.read().split("\n\n")
        rules = "".join(rules)
        upgrades = upgrades.split("\n")

        for upgrade in upgrades:
            upgrade = upgrade.split(",")
            reachable = []
            failed = False
            for i, page in enumerate(upgrade):
                if i == 0:
                    r = add_reach(upgrade, i, page, rules)
                    if not r:
                        failed = True
                        break
                    reachable += r
                elif page in reachable:
                    r = add_reach(upgrade, i, page, rules)
                    if not r:
                        failed = True
                        break
                    reachable += r
                else:
                    failed = True
                    break
            if not failed:
                two.append(upgrade)
                answer.append(upgrade)

    count = 0
    for upgrade in answer:
        count += int(upgrade[len(upgrade) // 2])
    print(count)

def add_reach(upgrade, i, page, inp):
    if upgrade == ["53", "44", "51", "25", "95", "68", "55", "37", "47", "62", "31"]:
        a=""
    rules = re.findall(f"{page}\|[0-9]*", inp)
    all_reach = []
    for rule in rules:
        _, reach = rule.split("|")
        if reach in upgrade[:i]:
            return False
        all_reach.append(reach)
    return all_reach


def fun2(input):
    answer = 0
    with open(input) as f:
        rules, upgrades = f.read().split("\n\n")
        rules = "".join(rules)
        upgrades = upgrades.split("\n")
        for update in upgrades:
            update = update.split(",")
            update = [int(x) for x in update]
            ever_invalid = False
            valid = False
            while not valid:
                valid = True
                for idx, num in enumerate(update):
                    for rule in re.findall(f"[0-9]*\|{num}", rules):
                        # Each number in the rules list must be BEFORE num
                        rule_num = int(rule.split("|")[1])

                        if rule_num in update[idx:]:
                            valid = False
                            ever_invalid = True
                            rule_num_idx = update.index(rule_num)
                            # Swap the two numbers
                            update[idx], update[rule_num_idx] = update[rule_num_idx], update[idx]
            if ever_invalid:
                total += update[len(update) // 2]

    print(answer)

def part_two(rules, updates):
    total = 0
    for update in updates:
        ever_invalid = False
        valid = False
        while not valid:
            valid = True
            for idx, num in enumerate(update):
                for rule_num in rules[num]:
                    # Each number in the rules list must be BEFORE num
                    if rule_num in update[idx:]:
                        valid = False
                        ever_invalid = True
                        rule_num_idx = update.index(rule_num)
                        # Swap the two numbers
                        update[idx], update[rule_num_idx] = update[rule_num_idx], update[idx]
        if ever_invalid:
            total += update[len(update) // 2]
    return total

input = "input.txt"
print(part_two(*get_input()))