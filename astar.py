class AStar:
    __init__(self, start, goal, board):
        this.start = start
        this.goal = goal
        this.board = board
        this.start.gScore = 0
        this.start.fScore = manhattanDistance(start,goal)


    def run():

