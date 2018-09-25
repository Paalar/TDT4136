from node import Node

def textToMap(txt, xLength):
    nodes = []
    x = 0
    y = 0
    for letter in txt:
        if x < xLength:
            x += 1
        else:
            x = 0
            y += 1
        nodes.append(Node(letter,[x,y]))
    return nodes


def readTextFromFile(txtUrl):
    file_object = open(txtUrl,"r")
    return file_object.read()
