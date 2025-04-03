from itertools import combinations

# Define basic logic gates
def logic_gate_AND(a, b):
    return a & b

def logic_gate_OR(a, b):
    return a | b

def logic_gate_XOR(a, b):
    return a ^ b

# Read input file and return as list of strings
def load_input_data(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]

# Process the input lines into wire values and gate instructions
def process_input_data(file_path):
    wire_values = {}
    gate_operations = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if ":" in line:
            wire, value = line.split(": ")
            wire_values[wire] = int(value)
        elif "->" in line:
            operation, output_wire = line.split(" -> ")
            if " AND " in operation:
                input1, input2 = operation.split(" AND ")
                gate_operations.append((logic_gate_AND, input1, input2, output_wire))
            elif " OR " in operation:
                input1, input2 = operation.split(" OR ")
                gate_operations.append((logic_gate_OR, input1, input2, output_wire))
            elif " XOR " in operation:
                input1, input2 = operation.split(" XOR ")
                gate_operations.append((logic_gate_XOR, input1, input2, output_wire))

    return wire_values, gate_operations

# Simulate the circuit based on gate operations and initial wire values
def simulate_circuit(initial_values, gates):
    current_values = initial_values.copy()

    while True:
        changes = False
        for gate in gates:
            gate_function, input1, input2, output = gate
            if output not in current_values and input1 in current_values and input2 in current_values:
                current_values[output] = gate_function(current_values[input1], current_values[input2])
                changes = True

        if not changes:
            break

    return current_values

# Find the output wire for a given pair of input wires and gate type
def locate_gate_output(input_wire1, input_wire2, gate_type, circuit):
    gate_pattern_1 = f'{input_wire1} {gate_type} {input_wire2} -> '
    gate_pattern_2 = f'{input_wire2} {gate_type} {input_wire1} -> '

    for config in circuit:
        if gate_pattern_1 in config or gate_pattern_2 in config:
            return config.split(' -> ')[-1]

# Swap the output wires of two gates
def swap_gate_outputs(wire1, wire2, circuit):
    updated_circuit = []

    for gate in circuit:
        inputs, output = gate.split(' -> ')
        if output == wire1:
            updated_circuit.append(f'{inputs} -> {wire2}')
        elif output == wire2:
            updated_circuit.append(f'{inputs} -> {wire1}')
        else:
            updated_circuit.append(gate)

    return updated_circuit

# Identify parallel adder gates and find any swapped gates
def identify_parallel_adders(circuit):
    carry_wire = None
    swapped_gates = []
    bit_index = 0

    while True:
        wire_x = f'x{bit_index:02d}'
        wire_y = f'y{bit_index:02d}'
        wire_z = f'z{bit_index:02d}'

        if bit_index == 0:
            carry_wire = locate_gate_output(wire_x, wire_y, 'AND', circuit)
        else:
            xor_gate = locate_gate_output(wire_x, wire_y, 'XOR', circuit)
            and_gate = locate_gate_output(wire_x, wire_y, 'AND', circuit)

            cin_xor_gate = locate_gate_output(xor_gate, carry_wire, 'XOR', circuit)
            if cin_xor_gate is None:
                swapped_gates.append(xor_gate)
                swapped_gates.append(and_gate)
                circuit = swap_gate_outputs(xor_gate, and_gate, circuit)
                bit_index = 0
                continue

            if cin_xor_gate != wire_z:
                swapped_gates.append(cin_xor_gate)
                swapped_gates.append(wire_z)
                circuit = swap_gate_outputs(cin_xor_gate, wire_z, circuit)
                bit_index = 0
                continue

            cin_and_gate = locate_gate_output(xor_gate, carry_wire, 'AND', circuit)
            carry_gate = locate_gate_output(and_gate, cin_and_gate, 'OR', circuit)
            carry_wire = carry_gate

        bit_index += 1
        if bit_index >= 45:
            break

    return swapped_gates

# Main function to solve the puzzle
def solve_puzzle(lines):
    divider_index = lines.index('')
    circuit = lines[divider_index + 1:]

    swapped_gates = identify_parallel_adders(circuit)
    print(','.join(sorted(swapped_gates)))

# Execute the solution with input file
lines = load_input_data("input.txt")
solve_puzzle(lines)
