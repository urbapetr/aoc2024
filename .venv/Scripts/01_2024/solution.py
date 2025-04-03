def insertionSort(arr):
    n = len(arr)  # Get the length of the array

    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j + 1] = key  # Insert the key in the correct position

def fun1(input):
    answer = 0
    left = []
    right = []
    with open(input) as lines:
        for line in lines:
            line = line.rstrip().split()
            left.append(line[0])
            right.append(line[1])

    insertionSort(left)
    insertionSort(right)
    for i, l in enumerate(left):
        answer += abs(int(right[i]) - int(l))
    print(answer)

def fun2(input):
    answer = 0
    left = []
    right = []
    with open(input) as lines:
        for line in lines:
            line = line.rstrip().split()
            left.append(line[0])
            right.append(line[1])

    insertionSort(left)
    for i, l in enumerate(left):
        c = right.count(l)
        answer += c * int(l)
    print(answer)

input = "input.txt"
fun1(input)
fun2(input)


