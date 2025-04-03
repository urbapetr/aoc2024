def can_create_design(towel_patterns, designs):
    # Convert the towel patterns into a set for faster lookup
    towel_set = set(towel_patterns)

    results = []
    for design in designs:
        # dp[i] will be True if we can create the first i characters of the design
        dp = [False] * (len(design) + 1)
        dp[0] = True

        for i in range(1, len(design) + 1):
            for j in range(i):
                if dp[j] and design[j:i] in towel_set:
                    dp[i] = True
                    break

        if dp[len(design)]:
            results.append("possible")
        else:
            results.append("impossible")

    return results


# Example input

input = "input.txt"
towel_patterns = []
designs = []
with open(input) as lines:
    patterns = True
    for line in lines:
        line = line.rstrip()
        if line == "":
            patterns = False
            continue
        if patterns:
            towel_patterns = line.split(", ")
        else:
            designs.append(line)


# Call the function
results = can_create_design(towel_patterns, designs)

# Output results
print(results.count("possible"))

def count_ways_to_create_design(towel_patterns, designs):
    # Convert the towel patterns into a set for faster lookup
    towel_set = set(towel_patterns)

    total_ways = 0
    for design in designs:
        # dp[i] will be the number of ways to create the first i characters of the design
        dp = [0] * (len(design) + 1)
        dp[0] = 1  # There's one way to form the empty prefix of the design

        # Fill the dp array for this design
        for i in range(1, len(design) + 1):
            for j in range(i):
                if design[j:i] in towel_set:
                    dp[i] += dp[j]

        # Add the number of ways to form the entire design
        total_ways += dp[len(design)]

    return total_ways


# Call the function
total_ways = count_ways_to_create_design(towel_patterns, designs)

# Output result
print(total_ways)
