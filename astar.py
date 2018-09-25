from utils import manhattanDistance, printStage
import heapq

class AStar:
    def __init__(self, start, goal, board):
        self.start = start
        self.goal = goal
        self.board = board
        self.start.gScore = 0
        #self.start.updateHeuristic(manhattanDistance(start,goal))
        self.openSet = [start]
        self.closedSet = [start]
        self.cameFrom = {}

    def reconstruct_path(self, cameFrom, current):
        total_path = []
        while current in cameFrom.keys():
            current = cameFrom[current]
            #if current != self.start:
                #current.isPath()
            total_path.append(current)
        return total_path

    def run(self):
        while self.openSet:
            current = heapq.heappop(self.openSet)
            self.reconstruct_path(self.cameFrom, current)
            if current == self.goal:
                return self.reconstruct_path(self.cameFrom, current)
            current.isPath()
            printStage(self.board)
            print("\n")

            heapq.heappush(self.closedSet, current)
            for neighbor in current.neighbors:
                if neighbor in self.closedSet:
                    print("\n")
                    continue

                tentative_gScore = current.gScore + 1 # All distances are 1 in this version of A*
                print("Tentative score", tentative_gScore)

                if neighbor not in self.openSet:
                    heapq.heappush(self.openSet, neighbor)
                elif tentative_gScore >= neighbor.gScore:
                    continue

                self.cameFrom[neighbor] = current
                neighbor.gScore = tentative_gScore
                neighbor.updateHeuristic(manhattanDistance(neighbor, self.goal))
                print("Neighbor's fScore = ",neighbor.getFScore())
                print("coordinates = ", neighbor.y, neighbor.x)
            print("\n\n\n")
