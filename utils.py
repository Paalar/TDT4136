from node import Node

def findStartAndEnd(nodes):
    start = None
    end = None
    index = 0
    while not start and not end:
        if nodes[index].nodeType == "A":
            start = nodes[index]
        elif nodes[index].nodeType == "B":
            end = nodes[index]
    return start, end

def textToNodes(txt,xLength = 0):
    nodes = []
    x = 0
    y = 0
    for letter in txt:
        if x < xLength or letter != "\n":
            x += 1
        else:
            x = 0
            y += 1
        if letter != "\n":
            nodes.append(Node(letter,[x,y]))
    return nodes


def readTextFromFile(txtUrl):
    file_object = open(txtUrl,"r")
    return file_object.read()

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
    for xAxis in stage:
        print(" ".join(xAxis))

def manhattanDistance(start,end):
    return abs(end.x - start.x) + abs(end.y + start.y)
