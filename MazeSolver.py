file_infos = []
resMatrix = [[0 for x in range(17)] for y in range(17)]
exits = []
starts = []

def readFiles():
    tempStr = []
    # Read the file's content
    tempMap = open("./test.txt", "r").readlines()

    for line in range(0, len(tempMap)):
        tempMap[line] = tempMap[line].replace("\n", "")
        tempStr.append(list(tempMap[line]))

    for line in range(0, len(tempStr)):
        for case in range(0, len(tempStr[line])):
            tempStr[line][case] = float(tempStr[line][case])

    return tempStr


# Function to locate both START and END positions from the "map"
# 2 – start position
# exit is a zero at the edge
def locateStartEnd(map):
    for line in range(17):

        for case in range(17):

            if map[line][case] == 2:
                # Save the X and Y coordinates of the START position
                starts.append((case, line))

            # If the current case of the END position
            if map[line][case] == 0 and (line == 0 or line == 16 or case == 0 or case == 16):
                # Save the X and Y coordinates of the END position
                exits.append((case, line))

def createManX(file_infos):
    manhat = []

    # Loop through all the lines of the "map"
    for line in range(0, len(file_infos["map"])):
        row = []

        for case in range(0, len(file_infos["map"][line])):
            # Fill each case with |X1 - X2| + |Y1 - Y2|
            row.append((abs(case - file_infos["endPos"]["x"]) + abs(line - file_infos["endPos"]["y"])))
        manhat.append(row)

    file_infos["ManX"] = manhat
    return file_infos


# Function that initializes the Fx map
def createFx(file_infos):
    Fx = []

    # Loop through all the lines of the "map"
    for line in range(0, len(file_infos["map"])):
        row = []

        for case in range(0, len(file_infos["map"][line])):

            # Insert -1 at the starting position coordinates in "Fx"
            if case == file_infos["startPos"]["x"] and line == file_infos["startPos"]["y"]:
                row.append(-1.0)

            # Insert FALSE everywhere else
            else:
                row.append(False)
        Fx.append(row)

    file_infos["Fx"] = Fx
    return file_infos


# Function that initializes the aGx map
def createaGx(a, file_infos):
    aGx = []

    for line in range(0, len(file_infos["map"])):
        row = []

        for case in range(0, len(file_infos["map"][line])):

            # Insert "alpha" * the value of "Fx" at the starting position in "aGx"
            if case == file_infos["startPos"]["x"] and line == file_infos["startPos"]["y"]:
                row.append(a * file_infos["ManX"][line][case])

            # Insert FALSE everywhere else
            else:
                row.append(False)
        aGx.append(row)

    file_infos["aGx"] = aGx

    return file_infos


# Function to go from the starting point, move around following our heuristic
def moveAround(a, file_infos):
    steps = 0
    minimum = {"x": "", "y": "", "value": ""}

    # Check if the case to the left is a valid case
    def getLeft(file_infos):
        if file_infos["map"][minimum["y"]][minimum["x"] - 1] != 1.0 and file_infos["aGx"][minimum["y"]][
            minimum["x"] - 1] == False:
            if file_infos["Fx"][minimum["y"]][minimum["x"]] == - 1:
                file_infos["Fx"][minimum["y"]][minimum["x"] - 1] = file_infos["Fx"][minimum["y"]][minimum["x"]] + 2
            else:
                file_infos["Fx"][minimum["y"]][minimum["x"] - 1] = file_infos["Fx"][minimum["y"]][minimum["x"]] + 1
            file_infos["aGx"][minimum["y"]][minimum["x"] - 1] = (a * file_infos["ManX"][minimum["y"]][
                minimum["x"] - 1]) + (file_infos["Fx"][minimum["y"]][minimum["x"] - 1])

    # Check if the case to the right is a valid case
    def getRight(file_infos):
        if file_infos["map"][minimum["y"]][minimum["x"] + 1] != 1.0 and file_infos["aGx"][minimum["y"]][
            minimum["x"] + 1] == False:
            if file_infos["Fx"][minimum["y"]][minimum["x"]] == - 1:
                file_infos["Fx"][minimum["y"]][minimum["x"] + 1] = file_infos["Fx"][minimum["y"]][minimum["x"]] + 2
            else:
                file_infos["Fx"][minimum["y"]][minimum["x"] + 1] = file_infos["Fx"][minimum["y"]][minimum["x"]] + 1
            file_infos["aGx"][minimum["y"]][minimum["x"] + 1] = (a * file_infos["ManX"][minimum["y"]][
                minimum["x"] + 1]) + (file_infos["Fx"][minimum["y"]][minimum["x"] + 1])

    # Check if the case on top is a valid case
    def getUp(file_infos):
        if file_infos["map"][minimum["y"] - 1][minimum["x"]] != 1.0 and file_infos["aGx"][minimum["y"] - 1][
            minimum["x"]] == False:
            if file_infos["Fx"][minimum["y"]][minimum["x"]] == - 1:
                file_infos["Fx"][minimum["y"] - 1][minimum["x"]] = file_infos["Fx"][minimum["y"]][minimum["x"]] + 2
            else:
                file_infos["Fx"][minimum["y"] - 1][minimum["x"]] = file_infos["Fx"][minimum["y"]][minimum["x"]] + 1
            file_infos["aGx"][minimum["y"] - 1][minimum["x"]] = (a * file_infos["ManX"][minimum["y"] - 1][
                minimum["x"]]) + (file_infos["Fx"][minimum["y"] - 1][minimum["x"]])

    # Check if the case on the bottom is a valid case
    def getDown(file_infos):
        if file_infos["map"][minimum["y"] + 1][minimum["x"]] != 1.0 and file_infos["aGx"][minimum["y"] + 1][
            minimum["x"]] == False:
            if file_infos["Fx"][minimum["y"]][minimum["x"]] == - 1:
                file_infos["Fx"][minimum["y"] + 1][minimum["x"]] = file_infos["Fx"][minimum["y"]][minimum["x"]] + 2
            else:
                file_infos["Fx"][minimum["y"] + 1][minimum["x"]] = file_infos["Fx"][minimum["y"]][minimum["x"]] + 1
            file_infos["aGx"][minimum["y"] + 1][minimum["x"]] = (a * file_infos["ManX"][minimum["y"] + 1][
                minimum["x"]]) + (file_infos["Fx"][minimum["y"] + 1][minimum["x"]])

    # While we're not on the end position, keep going
    while not file_infos["aGx"][file_infos["endPos"]["y"]][file_infos["endPos"]["x"]]:

        minimum = {"x": "", "y": "", "value": ""}

        for line in range(0, len(file_infos["map"])):

            for case in range(0, len(file_infos["map"][line])):

                # Check if current case is a number
                if isinstance(file_infos["aGx"][line][case], float):

                    # If we don't already have a minimum value, take the first one we find
                    if minimum["value"] == "":
                        minimum.update({"x": case, "y": line, "value": file_infos["aGx"][line][case]})

                    # If we already have one, check if the value is smaller that our minimum
                    elif file_infos["aGx"][line][case] < minimum["value"]:

                        # If it is, make it our new minimum
                        minimum.update({"x": case, "y": line, "value": file_infos["aGx"][line][case]})

        # If we don't have a minimum, it means that we're stuck and the map is IMPOSSIBLE
        if minimum["value"] == "":
            file_infos["numberSteps"] = "IMPOSSIBLE"
            file_infos["reverseWinningPath"] = "IMPOSSIBLE"
            return
        steps += 1

        # If the current case is in the middle columns
        if 0 < minimum["x"] < len(file_infos["map"][0]) - 1:
            getLeft(file_infos)
            getRight(file_infos)

        # If the current case is in the first column
        elif minimum["x"] == 0:
            getRight(file_infos)

        # Id the current case is on the last column
        else:
            getLeft(file_infos)

        # If the current case is on the middle rows
        if 0 < minimum["y"] < len(file_infos["map"]) - 1:
            getUp(file_infos)
            getDown(file_infos)

        # If the current case is on the first row
        elif minimum["y"] == 0:
            getDown(file_infos)

        # If the current case is on the last row
        else:
            getUp(file_infos)

        # The case we were previously on, becomes TRUE
        file_infos["aGx"][minimum["y"]][minimum["x"]] = True

    # Store the amount of steps required to find the exit in the "numberSteps" property of file_infos
    file_infos["numberSteps"] = steps
    return file_infos


# Function to go from the END to the START using the shortest path possible
def trackBack(file_infos):
    currentPosition = {"x": file_infos["endPos"]["x"], "y": file_infos["endPos"]["y"],
                       "value": file_infos["Fx"][file_infos["endPos"]["y"]][file_infos["endPos"]["x"]]}
    while True:

        # If current file is IMPOSSIBLE, stop here
        if currentPosition["value"] == - 1 or file_infos["numberSteps"] == "IMPOSSIBLE":
            break
        minimum = {"x": "", "y": "", "value": ""}

        # If current position is not on first row
        if currentPosition["y"] != 0 and file_infos["aGx"][currentPosition["y"] - 1][currentPosition["x"]]:

            # If we don't already have a minimum value, take the first one we see
            if minimum["value"] == "":
                minimum.update({"x": currentPosition["x"], "y": currentPosition["y"] - 1,
                                "value": file_infos["Fx"][currentPosition["y"] - 1][currentPosition["x"]]})

            # If we already have one, check if the value is smaller that our minimum
            elif file_infos["Fx"][currentPosition["y"] - 1][currentPosition["x"]] < minimum["value"]:
                minimum.update({"x": currentPosition["x"], "y": currentPosition["y"] - 1,
                                "value": file_infos["Fx"][currentPosition["y"] - 1][currentPosition["x"]]})

        # If current position is not on the first column
        if currentPosition["x"] != 0 and file_infos["aGx"][currentPosition["y"]][currentPosition["x"] - 1]:

            # If we don't already have a minimum value, take the first one we see
            if minimum["value"] == "":
                minimum.update({"x": currentPosition["x"] - 1, "y": currentPosition["y"],
                                "value": file_infos["Fx"][currentPosition["y"]][currentPosition["x"] - 1]})

            # If we already have one, check if the value is smaller that our minimum
            elif file_infos["Fx"][currentPosition["y"]][currentPosition["x"] - 1] < minimum["value"]:
                minimum.update({"x": currentPosition["x"] - 1, "y": currentPosition["y"],
                                "value": file_infos["Fx"][currentPosition["y"]][currentPosition["x"] - 1]})

        if currentPosition["x"] < (len(file_infos["map"][0]) - 1) and file_infos["aGx"][currentPosition["y"]][
            currentPosition["x"] + 1]:

            # If we don't already have a minimum value, take the first one we see
            if minimum["value"] == "":
                minimum.update({"x": currentPosition["x"] + 1, "y": currentPosition["y"],
                                "value": file_infos["Fx"][currentPosition["y"]][currentPosition["x"] + 1]})

            # If we already have one, check if the value is smaller that our minimum
            elif file_infos["Fx"][currentPosition["y"]][currentPosition["x"] + 1] < minimum["value"]:
                minimum.update({"x": currentPosition["x"] + 1, "y": currentPosition["y"],
                                "value": file_infos["Fx"][currentPosition["y"]][currentPosition["x"] + 1]})

        if currentPosition["y"] < (len(file_infos["map"]) - 1) and file_infos["aGx"][currentPosition["y"] + 1][
            currentPosition["x"]]:

            # If we don't already have a minimum value, take the first one we see
            if minimum["value"] == "":
                minimum.update({"x": currentPosition["x"], "y": currentPosition["y"] + 1,
                                "value": file_infos["Fx"][currentPosition["y"] + 1][currentPosition["x"]]})

            # If we already have one, check if the value is smaller that our minimum
            elif file_infos["Fx"][currentPosition["y"] + 1][currentPosition["x"]] < minimum["value"]:
                minimum.update({"x": currentPosition["x"], "y": currentPosition["y"] + 1,
                                "value": file_infos["Fx"][currentPosition["y"] + 1][currentPosition["x"]]})

        # Add the opposite direction to the "reverseWinningPath" proprety of file_infos
        if currentPosition["x"] < minimum["x"]:
            file_infos["reverseWinningPath"].append("W")
        elif currentPosition["x"] > minimum["x"]:
            file_infos["reverseWinningPath"].append("E")
        elif currentPosition["y"] > minimum["y"]:
            file_infos["reverseWinningPath"].append("S")
        else:
            file_infos["reverseWinningPath"].append("N")

        global resMatrix

        resMatrix[currentPosition["y"]][currentPosition["x"]] = 1

        currentPosition = minimum


def main():
    global file_infos, resMatrix, exits

    a = 1.0

    map = readFiles()
    locateStartEnd(map)

    for i in range(len(starts)):
        file_infos.append([])

    for j in range(len(starts)):
        for i in range(len(exits)):
            file_infos[j].append(
                {"map": map, "startPos": {"x": starts[j][0], "y": starts[j][1]}, "endPos": {"x": exits[i][0], "y": exits[i][1]}, "Fx": [], "ManX": [],
                 "aGx": [], "amountSteps": "", "reverseWinningPath": []})
            file_infos[j][i] = createManX(file_infos[j][i])
            file_infos[j][i] = createFx(file_infos[j][i])
            file_infos[j][i] = createaGx(a, file_infos[j][i])
            file_infos[j][i] = moveAround(a, file_infos[j][i])

    minIndex = []
    for j in range(len(starts)):
        minIndex.append(-1)
        min = 0x100000000
        for i in range(len(exits)):

            same = False
            for k in range(len(minIndex)):
                if minIndex[k] == i:
                    same = True
            if same:
                continue

            if file_infos[j][i]["numberSteps"] < min:
                min = file_infos[j][i]["numberSteps"]
                minIndex[j] = i

    resMatrix = [[0 for x in range(17)] for y in range(17)]
    for i in range(len(starts)):
        resMatrix[file_infos[i][minIndex[i]]["startPos"]['x']][file_infos[i][minIndex[i]]["startPos"]['y']] = 1
        trackBack(file_infos[i][minIndex[i]])

    print("\n result \n")
    for line in resMatrix:
        print(str(line) + "\n")


if __name__ == "__main__":
    main()
