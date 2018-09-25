from node import Node

def readTextFromFile(directoryPath, filePath):
    txtUrl = "{0}{1}".format(directoryPath, filePath)
    file_object = open(txtUrl,"r")
    return file_object.read()

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
