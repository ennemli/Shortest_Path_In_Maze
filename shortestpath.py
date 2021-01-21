from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.edges: list[Node] = []
        self.parent = None

    def add_edg(self, vertex):
        self.edges.append(vertex)


def neighbors(maze, row, col, start):
    ways = []
    left = maze[row][col + 1:col + 2] if len(maze[row][col + 1:col + 2]) <= 0 else maze[row][col + 1:col + 2][0]
    right = maze[row][col - 1:col] if len(maze[row][col - 1:col]) <= 0 else maze[row][col - 1:col][0]
    top = None
    bottom = None
    if maze[row + 1:row + 2]:
        bottom = maze[row + 1:row + 2][0][col]
    if maze[row - 1:row]:
        top = maze[row - 1:row][0][col]
    if left == start:
        ways.append((row, col + 1))
    if right == start:
        ways.append((row, col - 1))
    if top == start:
        ways.append((row - 1, col))
    if bottom == start:
        ways.append((row + 1, col))
    return ways


MAZE = [[1, 1, 1, 1, 1],
        [1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1]]


def printMaze(maze):
    for row in maze:
        for col in row:
            print(col, end="  ")
        print("")


def fillMaze(maze, des):
    next_node = des
    while next_node:
        maze[next_node.value[0]][next_node.value[1]] = 5
        next_node = next_node.parent


def mazeToNode(maze, src, des):
    visited = []
    start = maze[src.value[0]][src.value[1]]
    q = deque([src])
    while len(q) > 0:
        v = q.popleft()
        if v.value not in visited:
            visited.append(v.value)
        if v.value == des.value:
            fillMaze(maze, v)
            break
        for w in neighbors(maze, v.value[0], v.value[1], start):
            n = Node(w)
            if w not in visited:
                v.add_edg(n)
                q.append(n)
            if not n.parent:
                n.parent = v
    return maze


src = Node((0, 0))
des = Node((2, 1))
printMaze(mazeToNode(MAZE, src, des))
