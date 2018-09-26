from node import Node
import math

startNode = None
endNode = None
allIterationsWanted = False

# Function for getting start and end in other files.
def findStartAndEnd():
    global startNode
    global endNode
    return startNode, endNode
    """
    start = None
    end = None
    index = 0
    while not start or not end:
        if nodes[index].nodeType == "A":
            start = nodes[index]
        elif nodes[index].nodeType == "B":
            end = nodes[index]
        index += 1
    return start, end
    """

def readTextFromFile(directoryPath, filePath):
    txtUrl = "{0}{1}".format(directoryPath, filePath)
    file_object = open(txtUrl,"r")
    return file_object.read()

def getAllIterations():
    global allIterationsWanted
    return allIterationsWanted

# Creates a 2d-list with node objects, sets neighbors and ignores walls & linebreaks.
def textToNodes(txt):
    global startNode
    global endNode
    nodes = []
    x = 0
    y = 0
    nestedNodes = []
    for letter in txt:
        if letter == "\n":
            x = 0
            y += 1
            nodes.append(nestedNodes)
            nestedNodes = []
            continue

        newNode = Node(letter, [x,y])
        if letter == "A":
            startNode = newNode
        elif letter == "B":
            endNode = newNode

        neighborNode = None

        # Adds itself as neighbor to earlier nodes
        # and adds earlier nodes as it's own neighbors
        if x:
            neighborNode = nestedNodes[x-1]
            if neighborNode.nodeType != "#" and newNode.nodeType != "#":
                newNode.addNeighbor(neighborNode)
                neighborNode.addNeighbor(newNode)

        if y:
            neighborNode = nodes[y-1][x]
            if neighborNode.nodeType != "#" and newNode.nodeType != "#":
                newNode.addNeighbor(neighborNode)
                neighborNode.addNeighbor(newNode)

        nestedNodes.append(newNode)
        x += 1

    return nodes

# Unused?
'''
def createStage(stageResult):
    yAxis = []
    xAxis = []
    y = 0
    for node in stageResult:
        if (node.y > y):
            y += 1
            yAxis.append(xAxis)
            xAxis = []

        xAxis.append(node.nodeType)
    return yAxis
'''

# Print stage from node types.
def printStage(stage):
    nodeTypes = []
    for scene in stage:
        for node in scene:
            nodeTypes.append(node.nodeType)
        print(" ".join(nodeTypes))
        nodeTypes = []

# Sets heuristic to all nodes after initialising stage
# since start and end might not be available before the stage is complete.
def initHeuristic(stage, goalNode):
    nodeTypes = []
    for scene in stage:
        for node in scene:
            node.updateHeuristic(manhattanDistance(node, goalNode))

# Calculates the manhattan distance of the start coordinates and end coordinates
# Best choice for 4-connected grid with no weight as it gives the most correct length.
def manhattanDistance(start,end):
    return abs(end.x - start.x) + abs(end.y - start.y)

# Calculates the euclidean distance of the start coordinates and end coordinates
# Might underestimate in a 4-connected grid with no weight due to the pythagorean theorem.
def euclideanDistance(start,end):
    return math.sqrt( ((end.x - start.x)**2) + ((end.y - start.y)**2) )
