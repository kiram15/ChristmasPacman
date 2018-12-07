from ChristmasPacman import Ghost as Santa
from ChristmasPacman import Pacman as Grinch
from ChristmasPacman import Maze
import time

class Node:
    def __init__(self, state, f=0, g=0 ,h=0):
        self.state = state
        self.f = f
        self.g = g
        self.h = h
    def __repr__(self):
        return "Node(" + repr(self.state) + ", f=" + repr(self.f) + \
               ", g=" + repr(self.g) + ", h=" + repr(self.h) + ")"

def aStarSearch(startState, actionsF, takeActionF, goalTestF, hF):
    h = hF(startState)
    startNode = Node(state=startState, f=0+h, g=0, h=h)
    return aStarSearchHelper(startNode, actionsF, takeActionF, goalTestF, hF, float('inf'))

def aStarSearchHelper(parentNode, actionsF, takeActionF, goalTestF, hF, fmax):
    if goalTestF(parentNode.state):
        return ([parentNode.state], parentNode.g)
    ## Construct list of children nodes with f, g, and h values
    actions = actionsF(parentNode.state)
    if not actions:
        return ("failure", float('inf'))
    children = []
    for action in actions:
        (childState,stepCost) = takeActionF(parentNode.state, action)
        global gNumNodes
        gNumNodes += 1
        h = hF(childState)
        g = parentNode.g + stepCost
        f = max(h+g, parentNode.f)
        childNode = Node(state=childState, f=f, g=g, h=h)
        children.append(childNode)
    while True:
        # find best child
        children.sort(key = lambda n: n.f) # sort by f value
        bestChild = children[0]
        if bestChild.f > fmax:
            return ("failure",bestChild.f)
        # next lowest f value
        alternativef = children[1].f if len(children) > 1 else float('inf')
        # expand best child, reassign its f value to be returned value
        result,bestChild.f = aStarSearchHelper(bestChild, actionsF, takeActionF, goalTestF,
                                            hF, min(fmax,alternativef))
        if result is not "failure":
            result.insert(0,parentNode.state)
            return (result, bestChild.f)

def runHelperAStar(startState, goalState, heuristic):
    startTime = time.time()
    global gNumNodes
    gNumNodes = 0
    if heuristic is 1:
        h1Path, h1Depth = aStarSearch(startState, Santa.actions, Santa.takeAction, lambda s: Santa.goalTest(s),
                              lambda s: h1(s, goalState))
        endTime = time.time()
        return h1Depth, gNumNodes, endTime-startTime
    elif heuristic is 2:
        h2Path, h2Depth = aStarSearch(startState, Santa.actions, Santa.takeAction, lambda s: Santa.goalTest(s),
                              lambda s: h2(s, goalState))
        endTime = time.time()
        return h2Depth, gNumNodes, endTime-startTime
    else:
        h3Path, h3Depth = aStarSearch(startState, Santa.actions, Santa.takeAction, lambda s: Santa.goalTest(s),
                              lambda s: h3(s, goalState))
        endTime = time.time()
        return h3Depth, gNumNodes, endTime-startTime

def h1(state, goal):
    return 0

def h2(state, goal):
    return 1

def h3(state, goal):
    return manhattanDistance(state, goal)

def manhattanDistance(state, goal):
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


if __name__ == "__main__":

    board = [['X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', ' ', '.', '.', '.', 'G', 'X'],
             ['X', '.', 'X', 'X', 'X', '.', 'X'],
             ['X', ' ', ' ', '.', ' ', ' ', 'X'],
             ['X', '.', 'X', 'X', 'X', '.', 'X'],
             ['X', 'S', '.', '.', '.', ' ', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X']]

    myMaze = Maze.Maze(board)
    myGrinch = Grinch.Pacman(board)
    mySanta = Santa.Ghost(board)
    runHelperAStar(Santa.Ghost.getLocation(mySanta), Grinch.Pacman.getLocation(myGrinch), 1)

    #alive = False
    #has a ghost caught pacman
