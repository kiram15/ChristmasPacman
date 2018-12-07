#santa
class Ghost:
    def __init__(self, Maze):
        self.location = (1,5)
        self.coveringDot = False
        self.maze = Maze()

    def actions(self):
        walls = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
                 (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
                 (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6),
                 (1, 6), (2, 6), (3, 6), (4, 6), (5, 6),
                 (2, 2), (3, 2), (4, 2),
                 (2, 4), (3, 4), (4, 4)]
        validActions = []
        currentLocation = self.location
        right = (currentLocation[0] + 1, currentLocation[1])
        left = (currentLocation[0] - 1, currentLocation[1])
        up = (currentLocation[0], currentLocation[1] + 1)
        down = (currentLocation[0], currentLocation[1] - 1)
        if right not in walls:
            validActions.append("right")
        if left not in walls:
            validActions.append("left")
        if up not in walls:
            validActions.append("up")
        if down not in walls:
            validActions.append("down")
        return validActions

    def takeAction(self, action):
        tLocation = self.location
        newLocation = ()
        if action == "right":
            newLocation = (tLocation[0]+1, tLocation[1])
        elif action == "left":
            newLocation = (tLocation[0]-1, tLocation[1])
        elif action == "up":
            newLocation = (tLocation[0], tLocation[1]+1)
        elif action == "down":
            newLocation = (tLocation[0], tLocation[1]-1)
        self.maze.makeMove(self, newLocation[0], newLocation[1])
        self.location = newLocation

    def goalTest(self):
        if Ghost.getPacmanLocation(self) == self.location:
            return True
        return False

    def getPacmanLocation(self):
        myMaze = self.maze.maze
        pacmanCoordinates = ()
        for r in range(len(myMaze)):
            for el in range(len(myMaze[0])):
                if myMaze[r][el] == "G":
                    pacmanCoordinates = (r, el)
        return pacmanCoordinates

            # def takeShortest(self): #calls actions, testAction, takeAction
    #     possibleActions = Ghost.actions(self)
    #     shortestDistance = 100
    #     bestAction = ""
    #     for a in possibleActions:
    #         tempDistance = Ghost.testAction(self, a)
    #         if shortestDistance > tempDistance:
    #             shortestDistance = tempDistance
    #             bestAction = a
    #     Ghost.takeAction(self, bestAction)
    #
    # def testAction(self, action):
    #     tempLocation = self.location
    #     if action == "right":
    #         newX = tempLocation[0] + 1
    #         tempLocation = (newX, tempLocation[1])
    #     elif action == "left":
    #         newX = tempLocation[0] - 1
    #         tempLocation = (newX, tempLocation[1])
    #     elif action == "up":
    #         newY = tempLocation[1] + 1
    #         tempLocation = (tempLocation[0], newY)
    #     elif action == "down":
    #         newY = tempLocation[1] - 1
    #         tempLocation = (tempLocation[0], newY)
    #
    #     return Ghost.distance(self, tempLocation, Ghost.getPacmanLocation(self))
    #
    # def distance(self, l1, l2):
    #     return abs(l1[0] - l2[0]) + abs(l1[1] - l2[1])
    #
