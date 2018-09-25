import os
from utils import *
from astar import AStar

directoryPath = "boards/"
boardDirectory = {}

def iterateDirectory(directoryPath):
    directoryPath = os.fsencode(directoryPath)
    num = 1
    for file in os.listdir(directoryPath):
        filename = os.fsdecode(file)
        boardDirectory[num] = filename
        num += 1

def getBoard():
    print("Choose a board by entering a number\n")
    for key, value in sorted(boardDirectory.items()):
        print("[{0}] \t {1}".format(key, value))
    index = int(input("Input:\t"))
    return boardDirectory.get(index)

iterateDirectory(directoryPath)
filePath = getBoard()
textFile = readTextFromFile(directoryPath, filePath)
nodeList = textToNodes(textFile)
#printStage(nodeList)
start, goal = findStartAndEnd()
initHeuristic(nodeList, goal)
currentAStar = AStar(start, goal, nodeList)
realMap = currentAStar.run()
printStage(nodeList)
