from FP import Pacman as Grinch
from FP import Ghost as Santa
import copy


class dot(object):
    def __init__(self, x, y):
        self.location = x, y

    def location(self):
        return self.location


class maze(object):
    def __init__(self, ogMaze):
        self.maze = copy.deepcopy(ogMaze)
        self.ghost = (1,5)
        self.pacman = (5,1)
        self.dotList = self.createDotList(ogMaze)
        self.height = 7
        self.length = 7
        self.remainingDots = 11

    # even if the ghost moves over the dot, it needs to stay there

    def createDotList(self, maze):
        allDots = []
        for x, a in enumerate(maze):
            for y, b in enumerate(maze[x]):
                if b is '.':
                    allDots.append(dot(x, y))
                if b is ' ':
                    allDots.append(dot(x, y))
        return allDots

    def makeMove(self, past, x, y):
        if isinstance(past, Santa.Ghost):
            maze.ghostMove(self, past, x, y)
        if isinstance(past, Grinch.Pacman):
            maze.pacmanMove(self, past, x, y)

    def ghostMove(self, past, futureX, futureY):
        pastX = past.location[0]
        pastY = past.location[1]
        # if the ghost is going over a dot, it's stored so that the
        # dot can be restored after the ghost moves out of that spot
        self.maze[pastX][pastY] = 'S'
        if past.coveringDot:
            self.maze[pastX][pastY] = '.'
            past.onDot = False
        elif self.maze[futureX][futureY] is '.':
            self.maze[pastX][pastY] = ' '
            past.coveringDot = True
            past.location = pastX, pastY
        else:
            self.maze[pastX][pastY] = ' '
        past.location = pastX, pastY

    def pacmanMove(self, past, futureX, futureY):
        pastX = past.location[0]
        pastY = past.location[1]
        self.maze[pastX][pastY] = 'G'
        self.maze[pastX][pastY] = ' '
        past.location = futureX, futureY
        # if he ate a dot
        if self.maze[pastX][pastY] is '.':
            self.remainingDots -= self.remainingDots
            for dot in self.dotList:
                if dot.location[0] == pastX and dot.location[1] == pastY:
                    self.dotList.remove(dot)
