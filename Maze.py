import Pacman as Grinch
import Ghost as Santa

class dot(object):
    def __init__(self, x, y):
        self.location = x, y

    def location(self):
        return self.location

class maze(object):
    def __init__(self, ogMaze):
        self.maze = copy.deepcopy(ogMaze)
        self.ghost = (0,0)
        self.pacman = (4,5)
        self.dotList = self.createDotList(ogMaze)
        self.height = 5
        self.length = 4
        self.remainingDots = 16
        return

    #even if the ghost moves over the dot, it needs to stay there
    def createDotList(self, maze):
        allDots = []
        for x, a in enumerate(maze):
            for y, b in enumerate(maze[x]):
                if b is '.':
                    allDots.append(Dot(x, y, False))
                if b is ' ':
                    allDots.append(Dot(x, y, True))
        return allDots


    def makeMove(self, past, x, y):
        if isinstance(past, Santa.Ghost):
            ghostMove(self, past, x, y)
        if isinstance(past, Grinch.Pacman):
            pacmanMove(self, past, x, y)

    def ghostMove(self, past, futureX, futureY):
        pastX = past.location[0]
        pastY = past.location[1]
        #if the ghost is going over a dot, it's stored so that the
        #dot can be restored after the ghost moves out of that spot
        self.maze[x][y] = 'S'
        if past.coveringDot:
            self.maze[pastX][pastY] = '.'
            past.onDot = False
        elif self.maze[futureX][futureY] is '.':
            self.maze[pastX][pastY] = ' '
            past.coveringDot = True
            past.location = x, y
        else:
            self.board[pastX][pastY] = ' '
        past.location = x, y


    def pacmanMove(self, past, futureX, futureY):
        pastX = past.location[0]
        pastY = past.location[1]
        self.maze[x][y] = 'G'
        self.maze[pastX][pastY] = ' '
        past.location = x, y
        #if he ate a dot
        if self.maze[x][y] is '.':
            self.remainingDots -= self.remainingDots
            for dot in self.dotList:
                if dot.location[0] == x and dot.location[1] == y:
                    self.dotList.remove(dot)
