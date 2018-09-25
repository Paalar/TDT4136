class AStar:
    __init__(self, start, goal, board):
        this.start = start
        this.goal = goal
        this.board = board
        this.start.gScore = 0
        this.start.fScore = manhattanDistance(start,goal)
        this.openSet = [start]
        this.closedSet = []
        this.cameFrom = {}


    def run():
        while openSet:
            current = heapq.heappop(openSet)
            if current == goal
                return reconstruct_path(cameFrom, current)

            heapq.heappush(closedSet, current)

            for neighbor in current.neighbors:
                if neighbor in closedSet:
                    continue

                tentative_gScore = current.gScore + 1 # All distances are 1 in this version of A*

                if neighbor not in openSet:
                    heapq.heappush(openSet, neighbor)
                elif tentative_gScore >= neighbor.gScore:
                    continue

                cameFrom[neighbor] = current
                neighbor.gScore = tentative_gScore
                neighbor.updateHeuristic(manhattanDistance(neighbor, goal))

