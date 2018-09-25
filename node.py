import math

class Node:
    def __init__(self, nodeType, coordinates, heuristic = math.inf):
        self.nodeType = nodeType
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.gScore = math.inf
        self.heuristic = heuristic
        self.neighbors = []

    def isPath(self):
        self.nodeType = "O"

    def updateHeuristic(self, heuristic):
        self.heuristic = heuristic

    def getFScore(self):
        return self.gScore + self.heuristic

    def addNeighbor(self, node):
        self.neighbors.append(node)

    def __lt__(self, other):
        return self.getFScore() < other.getFScore()
