from utils import manhattanDistance, printStage
import heapq

class AStar:
    def __init__(self, start, goal, board):
        self.start = start
        self.goal = goal
        self.board = board
        self.start.gScore = 0
        self.openSet = [start]
        self.closedSet = [start]
        self.cameFrom = {}

    def reconstruct_path(self, cameFrom, current):
        total_path = []
        while current in cameFrom.keys():
            current = cameFrom[current]
            if current != self.start:
                current.isPath()
            total_path.append(current)
        return total_path

    def run(self):
        while self.openSet:
            current = self.openSet.pop()
            if current == self.goal:
                return self.reconstruct_path(self.cameFrom, current)
            current.wasVisited()
            print("----ITERATION----")
            printStage(self.board)
            print("\n")

            self.closedSet.append(current)
            for neighbor in current.neighbors:
                
                if neighbor in self.closedSet:
                    continue

                tentative_gScore = current.gScore + 1 # All distances are 1 in this version of A*

                
                if tentative_gScore >= neighbor.gScore:
                    continue

                neighbor.wasChecked()
                self.cameFrom[neighbor] = current
                neighbor.gScore = tentative_gScore
                neighbor.updateHeuristic(manhattanDistance(neighbor, self.goal))
                if neighbor not in self.openSet:
                    self.openSet.append(neighbor)
                    neighbor.initialQueuePlace = len(self.openSet)
            self.openSet.sort(reverse=True, key=lambda a: (a.getFScore(), -1 * a.initialQueuePlace))
