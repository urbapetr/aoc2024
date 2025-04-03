from pathlib import Path
from collections import deque, defaultdict

def parse_input(input_data: str):
    """
    Process the racetrack layout, marking start, end, and trackable positions.

    Args:
        input_data (str): The raw input string representing the racetrack.

    Returns:
        tuple: Starting position, ending position, and a set of accessible points.
    """
    start_pos, end_pos = 0j, 0j
    track_positions = set()
    for y, row in enumerate(input_data.splitlines()):
        for x, char in enumerate(row):
            position = complex(x, y)
            if char == "S":
                start_pos = position
            elif char == "E":
                end_pos = position
            if char != "#":
                track_positions.add(position)
    return start_pos, end_pos, track_positions

def calculate_distances(start, track):
    """
    Determine shortest paths from the start point to all reachable positions.

    Args:
        start (complex): The starting coordinate.
        track (set[complex]): Accessible points on the racetrack.

    Returns:
        dict: A dictionary of positions and their respective distances from the start.
    """
    queue = deque([(start, 0)])
    distances = {start: 0}

    while queue:
        current, dist = queue.popleft()
        for neighbor in (current + 1, current - 1, current + 1j, current - 1j):
            if neighbor in track and neighbor not in distances:
                distances[neighbor] = dist + 1
                queue.append((neighbor, dist + 1))
    return distances

def solve_part1(min_saving, start, end, track):
    """
    Calculate the number of shortcuts that save at least the specified time.

    Args:
        min_saving (int): The minimum time savings required.
        start (complex): Starting position.
        end (complex): Ending position.
        track (set[complex]): Accessible points on the racetrack.

    Returns:
        int: The number of valid shortcuts.
    """
    forward_distances = calculate_distances(start, track)
    reverse_distances = calculate_distances(end, track)
    base_time = forward_distances[end]
    shortcuts = defaultdict(int)

    for point in forward_distances:
        for direction in (1, -1, 1j, -1j):
            next_point = point + direction
            skip_point = point + 2 * direction

            if skip_point in reverse_distances and next_point not in track:
                shortcut_time = forward_distances[point] + 2 + reverse_distances[skip_point]
                if shortcut_time < base_time:
                    time_saved = base_time - shortcut_time
                    shortcuts[time_saved] += 1

    return sum(count for time_saved, count in shortcuts.items() if time_saved >= min_saving)

def generate_cheat_offsets(max_distance):
    """
    Generate valid cheat moves within a specified distance.

    Args:
        max_distance (int): Maximum allowed distance for a cheat move.

    Returns:
        dict: A dictionary of offsets and their respective costs.
    """
    offsets = {}
    for y in range(-max_distance, max_distance + 1):
        for x in range(-max_distance, max_distance + 1):
            manhattan_distance = abs(x) + abs(y)
            if 2 <= manhattan_distance <= max_distance:
                offsets[complex(x, y)] = manhattan_distance
    return offsets

def solve_part2(min_saving, max_distance, start, end, track):
    """
    Calculate the number of shortcuts with additional distance constraints.

    Args:
        min_saving (int): The minimum time savings required.
        max_distance (int): The maximum allowed distance for shortcuts.
        start (complex): Starting position.
        end (complex): Ending position.
        track (set[complex]): Accessible points on the racetrack.

    Returns:
        int: The number of valid shortcuts.
    """
    forward_distances = calculate_distances(start, track)
    reverse_distances = calculate_distances(end, track)
    base_time = forward_distances[end]
    cheat_offsets = generate_cheat_offsets(max_distance)
    shortcuts = defaultdict(int)

    for point in (p for p in forward_distances if forward_distances[p] < base_time - min_saving):
        for offset, cost in cheat_offsets.items():
            target = point + offset
            if target in reverse_distances:
                shortcut_time = forward_distances[point] + cost + reverse_distances[target]
                if shortcut_time < base_time:
                    time_saved = base_time - shortcut_time
                    shortcuts[time_saved] += 1

    return sum(count for time_saved, count in shortcuts.items() if time_saved >= min_saving)

if __name__ == "__main__":
    file_content = Path("input.txt").read_text()
    start, end, track = parse_input(file_content)

    part1_result = solve_part1(100, start, end, track)
    print(f"Part 1 result: {part1_result:,}")

    part2_result = solve_part2(100, 20, start, end, track)
    print(f"Part 2 result: {part2_result:,}")
