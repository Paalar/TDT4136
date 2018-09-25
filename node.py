import math

class Node:
    def __init__(self, nodeType, coordinates, heuristic = math.inf):
        self.nodeType = nodeType
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.gScore = math.inf
        self.fScore = self.gScore + heuristic

    def isPath():
        self.nodeType = "O"

    def updateHeuristic(heuristic):
        self.fScore = self.gScore + heuristic
