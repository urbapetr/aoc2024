# Define gate operations
from typing import Dict, List, Tuple

def AND(a: int, b: int) -> int:
    return a & b

def OR(a: int, b: int) -> int:
    return a | b

def XOR(a: int, b: int) -> int:
    return a ^ b

# Parse the input to initialize wire values and gates
def parse_input(file_path: str) -> Tuple[Dict[str, int], List[Tuple[str, str, str, str]]]:
    wire_values = {}
    gates = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if ":" in line:  # Initial wire values
            wire, value = line.split(": ")
            wire_values[wire] = int(value)
        elif "->" in line:  # Gate definitions
            parts = line.split(" -> ")
            output = parts[1]
            operation = parts[0].split(" ")

            if len(operation) == 3:  # Binary gate
                input1, gate, input2 = operation
                gates.append((input1, gate, input2, output))

    return wire_values, gates

# Simulate the circuit
def simulate(wire_values: Dict[str, int], gates: List[Tuple[str, str, str, str]]) -> Dict[str, int]:
    operations = {"AND": AND, "OR": OR, "XOR": XOR}

    while gates:
        remaining_gates = []
        for input1, gate, input2, output in gates:
            if input1 in wire_values and input2 in wire_values:
                wire_values[output] = operations[gate](wire_values[input1], wire_values[input2])
            else:
                remaining_gates.append((input1, gate, input2, output))
        gates = remaining_gates

    return wire_values

# Calculate the binary result from "z" wires
def calculate_result(wire_values: Dict[str, int]) -> int:
    z_values = {k: v for k, v in wire_values.items() if k.startswith("z")}
    binary_string = "".join(str(z_values[f"z{i:02}"]) for i in range(len(z_values)))
    return int(binary_string[::-1], 2)  # Convert binary string to decimal

# Identify swapped gates and fix them
def identify_and_fix_swaps(wire_values: Dict[str, int], gates: List[Tuple[str, str, str, str]]) -> List[str]:
    # Perform a brute-force check for swapped wires
    possible_swaps = []
    z_wires = [g[3] for g in gates if g[3].startswith("z")]

    for i in range(len(z_wires)):
        for j in range(i + 1, len(z_wires)):
            swapped_gates = gates[:]

            # Swap outputs of two gates
            for k, (input1, gate, input2, output) in enumerate(swapped_gates):
                if output == z_wires[i]:
                    swapped_gates[k] = (input1, gate, input2, z_wires[j])
                elif output == z_wires[j]:
                    swapped_gates[k] = (input1, gate, input2, z_wires[i])

            # Simulate with swapped gates
            simulated_values = simulate(wire_values.copy(), swapped_gates)
            x_value = calculate_binary_number(simulated_values, "x")
            y_value = calculate_binary_number(simulated_values, "y")
            z_value = calculate_binary_number(simulated_values, "z")

            if x_value + y_value == z_value:
                possible_swaps.append((z_wires[i], z_wires[j]))

    # Flatten and sort swap results
    swapped_wires = sorted(set(w for pair in possible_swaps for w in pair))
    return swapped_wires

# Calculate binary number from wires
def calculate_binary_number(wire_values: Dict[str, int], prefix: str) -> int:
    relevant_wires = {k: v for k, v in wire_values.items() if k.startswith(prefix)}
    binary_string = "".join(str(relevant_wires[f"{prefix}{i:02}"]) for i in range(len(relevant_wires)))
    return int(binary_string[::-1], 2)

# Main execution
def main(file_path: str):
    wire_values, gates = parse_input(file_path)
    final_values = simulate(wire_values, gates)
    part1_result = calculate_result(final_values)
    print("Part 1 Result:", part1_result)

    swapped_wires = identify_and_fix_swaps(wire_values, gates)
    print("Part 2 Swapped Wires:", ",".join(swapped_wires))

# Provide the path to the uploaded file
main("input.txt")
