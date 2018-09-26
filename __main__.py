import os
from utils import *
from astar import AStar

directoryPath = "boards/"
boardDirectory = {}

# Find all boards in folder and sets in boardDirectory
def iterateDirectory(directoryPath):
    directoryPath = os.fsencode(directoryPath)
    num = 1
    for file in os.listdir(directoryPath):
        filename = os.fsdecode(file)
        boardDirectory[num] = filename
        num += 1

# Gets board from user input
def getBoard():
    print("Choose a board by entering a number\n")
    for key, value in sorted(boardDirectory.items()):
        print("[{0}] \t {1}".format(key, value))
    index = int(input("Input:\t"))
    return boardDirectory.get(index)

def main():
    # Find available boards
    iterateDirectory(directoryPath)
    # Get file from user input
    filePath = getBoard()
    # Read text from chosen file
    textFile = readTextFromFile(directoryPath, filePath)
    # Convert text to stage
    nodeList = textToNodes(textFile)
    # Find points
    start, goal = findStartAndEnd()
    # Update heuristics now that goal points are certain
    initHeuristic(nodeList, goal)
    # Initiate A*
    currentAStar = AStar(start, goal, nodeList)
    # Run A*
    realMap = currentAStar.run()
    # Print stage after running.
    printStage(nodeList)

if __name__ == "__main__":
    main()