import math

class Node:
    def __init__(self, nodeType, coordinates, cost, heuristic = math.inf):
        self.nodeType = nodeType
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.gScore = math.inf
        self.heuristic = heuristic
        self.neighbors = []
        self.initialQueuePlace = 0
        self.cost = cost

    def isPath(self):
        self.nodeType = "X"

    def wasVisited(self):
        self.nodeType = "O"

    def wasChecked(self):
        self.nodeType = "q"

    def updateHeuristic(self, heuristic):
        self.heuristic = heuristic

    def getFScore(self):
        return self.gScore + self.heuristic

    def addNeighbor(self, node):
        self.neighbors.append(node)

    def __lt__(self, other):
        return self.getFScore() < other.getFScore() #   if self.getFScore() != other.getFScore() else self.queuePlace > other.queuePlace
