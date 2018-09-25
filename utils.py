from node import Node

startNode = None
endNode = None

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

def printStage(stage):
    nodeTypes = []
    for scene in stage:
        for node in scene:
            nodeTypes.append(node.nodeType)
        print(" ".join(nodeTypes))
        nodeTypes = []

def initHeuristic(stage, goalNode):
    nodeTypes = []
    for scene in stage:
        for node in scene:
            node.updateHeuristic(manhattanDistance(node, goalNode))

def manhattanDistance(start,end):
    return abs(end.x - start.x) + abs(end.y - start.y)
