import copy
from typing import List


def combo(num, registers):
    if num <= 3:
        return num
    elif num == 4:
        return registers['A']
    elif num == 5:
        return registers['B']
    elif num == 6:
        return registers['C']


def adv(num, registers, instr, outputs):
    registers['A'] = registers['A'] // (2 ** combo(num, registers))
    return registers, instr + 2, outputs


def bxl(num, registers, instr, outputs):
    registers['B'] = registers['B'] ^ num
    return registers, instr + 2, outputs


def bst(num, registers, instr, outputs):
    registers['B'] = combo(num, registers) % 8
    return registers, instr + 2, outputs


def jnz(num, registers, instr, outputs):
    if registers['A'] == 0:
        return registers, instr + 2, outputs
    else:
        return registers, num, outputs


def bxc(num, registers, instr, outputs):
    registers['B'] = registers['B'] ^ registers['C']
    return registers, instr + 2, outputs


def out(num, registers, instr, outputs):
    outputs.append(combo(num, registers) % 8)
    return registers, instr + 2, outputs


def bdv(num, registers, instr, outputs):
    registers['B'] = registers['A'] // (2 ** combo(num, registers))
    return registers, instr + 2, outputs


def cdv(num, registers, instr, outputs):
    registers['C'] = registers['A'] // (2 ** combo(num, registers))
    return registers, instr + 2, outputs


def get_output(a, registers_original, programs):
    outputs = []
    registers = copy.deepcopy(registers_original)
    registers['A'] = a
    length = len(programs)
    instr = 0
    while instr < length:
        opcode = programs[instr]
        function = [adv, bxl, bst, jnz, bxc, out, bdv, cdv][opcode]
        num = programs[instr + 1]
        registers, instr, outputs = function(num, registers, instr, outputs)
    return outputs


def find_initial_a(registers_original, programs):
    valid = [0]
    for length in range(1, len(programs) + 1):
        oldvalid = valid
        valid = []
        for num in oldvalid:
            for offset in range(8):
                newnum = 8 * num + offset
                output = get_output(newnum, registers_original, programs)

                print(f"Testing A={newnum}, Output={output}, Target={programs[-length:]}")  # Ladicí výstup

                if output == programs[-length:]:
                    valid.append(newnum)

        if not valid:
            print("No valid values found in this iteration!")

    if valid:
        return min(valid)
    else:
        raise ValueError("No valid values for A found.")


def fun1(input):
    lines: List[str] = []
    with open(input) as f:
        for line in f:
            line = line.strip()
            lines.append(line)

    register_a = int(lines[0].split(": ")[-1])
    register_b = int(lines[1].split(": ")[-1])
    register_c = int(lines[2].split(": ")[-1])
    program = [int(v) for v in lines[4].split(": ")[-1].split(",")]

    pc = 0
    out = []
    while pc < len(program):
        opcode = program[pc]
        operand = program[pc + 1]
        combo_operand = combo(operand, {'A': register_a, 'B': register_b, 'C': register_c})

        if opcode == 0:
            register_a = register_a // pow(2, combo_operand)
        elif opcode == 1:
            register_b = register_b ^ operand
        elif opcode == 2:
            register_b = combo_operand % 8
        elif opcode == 3:
            if register_a != 0:
                pc = operand
                continue
        elif opcode == 4:
            register_b = register_b ^ register_c
        elif opcode == 5:
            out.append(f"{combo_operand % 8}")
        elif opcode == 6:
            register_b = register_a // pow(2, combo_operand)
        elif opcode == 7:
            register_c = register_a // pow(2, combo_operand)

        pc += 2

    answer = ",".join(out)
    print("Výstup pro část 1:", answer)


def fun2(input):
    lines: List[str] = []
    with open(input) as f:
        for line in f:
            line = line.strip()
            lines.append(line)

    program = [int(v) for v in lines[4].split(": ")[-1].split(",")]

    try:
        answer = find_initial_a({'A': 0, 'B': 0, 'C': 0}, program)
        print("Výstup pro část 2:", answer)
    except ValueError as e:
        print("Chyba:", e)


input = "input.txt"
fun1(input)
fun2(input)
