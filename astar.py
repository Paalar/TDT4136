from utils import manhattanDistance, printStage, getAllIterations
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

    # Iterate through the best parents for every node from goal to start and mark as path.
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
            # If the algorithm reached the goal, end algorithm and backtrace route.
            if current == self.goal:
                return self.reconstruct_path(self.cameFrom, current)

            # Mark visited node.
            current.wasVisited()

            # Print all choices if this is toggled in utils.
            if getAllIterations():
                print("----ITERATION----")
                printStage(self.board)
                print("\n")

            # Add current node to set of finished nodes.
            self.closedSet.append(current)

            # Iterate over neighbors and look for best paths
            for neighbor in current.neighbors:
                
                # If this neighbor has already been walked through, skip it.
                if neighbor in self.closedSet:
                    continue

                # Score to reach this neighbor
                tentative_gScore = current.gScore + 1 # All distances are 1 in this version of A*

                # If it already has a better score, skip neighbor
                if tentative_gScore >= neighbor.gScore:
                    continue

                # Mark as checked and updated neighbor
                neighbor.wasChecked()

                # Add parent to neighbor as current
                self.cameFrom[neighbor] = current

                # Update amount of cost it took to get to neighbor
                neighbor.gScore = tentative_gScore

                # If new neighbor detected, add as possibility
                if neighbor not in self.openSet:
                    self.openSet.append(neighbor)

            # Sort set by fScore to get next best
            self.openSet.sort(reverse=True, key=lambda a: (a.getFScore()))
