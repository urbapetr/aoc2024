def resultingFileSystemChecksum():
    with open("input.txt") as file:
        con = file.read()

    fileSystem = []
    file = 0

    for i, char in enumerate(con):
        count = int(char)
        fileSystem.append({"file": file if i % 2 == 0 else -1, "count": count})
        if i % 2 == 0:
            file += 1

    reducedFileSystem = []

    for i in range(len(fileSystem)):
        if fileSystem[i]["file"] == -1:
            scan = len(fileSystem) - 1
            while fileSystem[i]["count"] > 0 and scan > i:
                if fileSystem[scan]["file"] != -1 and fileSystem[scan]["count"] <= fileSystem[i]["count"]:
                    reducedFileSystem.append(fileSystem[scan].copy())
                    fileSystem[i]["count"] -= fileSystem[scan]["count"]
                    fileSystem[scan]["file"] = -1
                    scan = len(fileSystem) - 1
                scan -= 1

            if fileSystem[i]["count"] != 0:
                reducedFileSystem.append(fileSystem[i])
        elif fileSystem[i]["count"] != 0:
            reducedFileSystem.append(fileSystem[i].copy())

    index = totalSum = 0
    current = reducedFileSystem.pop(0) if reducedFileSystem else None

    while reducedFileSystem or current:
        if current is None:
            break

        if current["file"] != -1:
            totalSum += current["file"] * index
            index += 1
            current["count"] -= 1
        else:
            index += current["count"]
            current["count"] = 0

        if current["count"] == 0:
            current = reducedFileSystem.pop(0) if reducedFileSystem else None

    print(totalSum)
    return totalSum


resultingFileSystemChecksum()
