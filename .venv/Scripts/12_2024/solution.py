def fun1(input):
    answer = 0
    map = []
    main = dict()
    plant_dict = dict()
    with open(input) as lines:
        for line in lines:
            line = line.rstrip()
            map.append(list(line))
        id = 1
        for y, row in enumerate(map):
            for x, plant in enumerate(row):
                id_up = 0
                id_left = 0
                if (y - 1, x, plant) in plant_dict.keys() and (y, x - 1, plant) in plant_dict.keys():
                    id_up = plant_dict.get((y - 1, x, plant))
                    id_left = plant_dict.get((y, x - 1, plant))
                    if id_up != id_left:
                        main[id_up] = main.get(id_up) + main.get(id_left) + [(y, x, plant)]
                        plant_dict[(y, x, plant)] = id_up
                        for X in main.get(id_left):
                            plant_dict[X] = id_up
                        del main[id_left]
                    else:
                        plant_dict[(y, x, plant)] = id_up
                        main.get(id_up).append((y, x, plant))
                    continue

                if (y - 1, x, plant) in plant_dict.keys():
                    id_up = plant_dict.get((y - 1, x, plant))
                    plant_dict[(y, x, plant)] = id_up
                    main.get(id_up).append((y, x, plant))

                if (y, x - 1, plant) in plant_dict.keys():
                    id_left = plant_dict.get((y, x - 1, plant))
                    plant_dict[(y, x, plant)] = id_left
                    main.get(id_left).append((y, x, plant))

                if id_up == 0 and id_left == 0:
                    plant_dict[(y, x, plant)] = id
                    main[id] = [(y, x, plant)]
                    id += 1

        for plants in main.values():
            region = len(plants)
            perimeter = 0
            for (y, x, K) in plants:
                if (y - 1, x, K) not in plants:
                    perimeter += 1
                if (y, x -1, K) not in plants:
                    perimeter += 1
                if (y + 1, x, K) not in plants:
                    perimeter += 1
                if (y, x + 1, K) not in plants:
                    perimeter += 1
            answer += perimeter * region


    print(answer)

def fun2(input):
    answer = 0
    map = []
    main = dict()
    plant_dict = dict()
    with open(input) as lines:
        for line in lines:
            line = line.rstrip()
            map.append(list(line))
        id = 1
        for y, row in enumerate(map):
            for x, plant in enumerate(row):
                id_up = 0
                id_left = 0
                if (y - 1, x, plant) in plant_dict.keys() and (y, x - 1, plant) in plant_dict.keys():
                    id_up = plant_dict.get((y - 1, x, plant))
                    id_left = plant_dict.get((y, x - 1, plant))
                    if id_up != id_left:
                        main[id_up] = main.get(id_up) + main.get(id_left) + [(y, x, plant)]
                        plant_dict[(y, x, plant)] = id_up
                        for X in main.get(id_left):
                            plant_dict[X] = id_up
                        del main[id_left]
                    else:
                        plant_dict[(y, x, plant)] = id_up
                        main.get(id_up).append((y, x, plant))
                    continue

                if (y - 1, x, plant) in plant_dict.keys():
                    id_up = plant_dict.get((y - 1, x, plant))
                    plant_dict[(y, x, plant)] = id_up
                    main.get(id_up).append((y, x, plant))

                if (y, x - 1, plant) in plant_dict.keys():
                    id_left = plant_dict.get((y, x - 1, plant))
                    plant_dict[(y, x, plant)] = id_left
                    main.get(id_left).append((y, x, plant))

                if id_up == 0 and id_left == 0:
                    plant_dict[(y, x, plant)] = id
                    main[id] = [(y, x, plant)]
                    id += 1

        for plants in main.values():
            region = len(plants)
            perimeter = 0
            for (y, x, K) in plants:
                corner_map = [0, 0,
                              0, 0,
                              0, 0,
                              0, 0]
                if (y - 1, x, K) not in plants:
                    if (y, x - 1, K) not in plants or ((y, x - 1, K) in plants and (y - 1, x - 1, K) in plants):
                        corner_map[0] = 1
                    if (y, x + 1, K) not in plants or ((y, x + 1, K) in plants and (y - 1, x + 1, K) in plants):
                        corner_map[1] = 1

                if (y, x - 1, K) not in plants:
                    if (y - 1, x, K) not in plants or ((y - 1, x, K) in plants and (y - 1, x - 1, K) in plants):
                        corner_map[4] = 1
                    if (y + 1, x, K) not in plants or ((y + 1, x, K) in plants and (y + 1, x - 1, K) in plants):
                        corner_map[6] = 1

                if (y + 1, x, K) not in plants:
                    if (y, x + 1, K) not in plants or ((y, x + 1, K) in plants and (y + 1, x + 1, K) in plants):
                        corner_map[3] = 1
                    if (y, x - 1, K) not in plants or ((y, x - 1, K) in plants and (y + 1, x - 1, K) in plants):
                        corner_map[2] = 1

                if (y, x + 1, K) not in plants:
                    if (y - 1, x, K) not in plants or ((y - 1, x, K) in plants and (y - 1, x + 1, K) in plants):
                        corner_map[5] = 1
                    if (y + 1, x, K) not in plants or ((y + 1, x, K) in plants and (y + 1, x + 1, K) in plants):
                        corner_map[7] = 1
                perimeter += sum(corner_map)
            answer += (perimeter//2) * region

    print(answer)

input = "input.txt"
#input = "smallinput.txt" # 1930
#fun1(input)

input = "input.txt"
#input = "smallinput.txt" # 160
fun2(input)