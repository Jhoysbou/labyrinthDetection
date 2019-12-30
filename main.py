 # some stuff
from collections import deque

maze = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1],
        [1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1],
        [1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1],
        [1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1],
        [1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1],
        [0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1],
        [1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0],
        [1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1],
        [1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


def getPath(maze):
    global start_y, start_x

    for i in maze:
        for j in maze[i]:
            if maze[i][j] == 2:
                start_x = i
                start_y = j
            elif maze[i][j] == 0:
                path.append((i, j))


def search(x,y):
    frontier.append((x, y))
    solution[x,y] = x,y

    while len(frontier) > 0:          # exit while loop when frontier queue equals zero
        x, y = frontier.popleft()     # pop next entry in the frontier queue an assign to x and y location

        if(x - 24, y) in path and (x - 24, y) not in visited:  # check the cell on the left
            cell = (x - 24, y)
            solution[cell] = x, y    # backtracking routine [cell] is the previous cell. x, y is the current cell
            #blue.goto(cell)        # identify frontier cells
            #blue.stamp()
            frontier.append(cell)   # add cell to frontier list
            visited.add((x-24, y))  # add cell to visited list

        if (x, y - 24) in path and (x, y - 24) not in visited:  # check the cell down
            cell = (x, y - 24)
            solution[cell] = x, y
            #blue.goto(cell)
            #blue.stamp()
            frontier.append(cell)
            visited.add((x, y - 24))
            print(solution)

        if(x + 24, y) in path and (x + 24, y) not in visited:   # check the cell on the  right
            cell = (x + 24, y)
            solution[cell] = x, y
            #blue.goto(cell)
            #blue.stamp()
            frontier.append(cell)
            visited.add((x + 24, y))

        if(x, y + 24) in path and (x, y + 24) not in visited:  # check the cell up
            cell = (x, y + 24)
            solution[cell] = x, y
            #blue.goto(cell)
            #blue.stamp()
            frontier.append(cell)
            visited.add((x, y + 24))
        green.goto(x,y)
        green.stamp()

              # "key value" now becomes the new key

start_x = 1
start_y = 1


# setup lists
walls = []
path = []
visited = set()
frontier = deque()
solution = {}                           # solution dictionary
