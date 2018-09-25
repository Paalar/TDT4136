import os
from utils import *

directoryPath = "boards/"
boardDirectory = {}

def iterateDirectory(directoryPath):
    directoryPath = os.fsencode(directoryPath)
    num = 0
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
stage = createStage(nodeList)
printStage(stage)
