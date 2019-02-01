# search.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
#
# Created by Michael Abir (abir2@illinois.edu) on 08/28/2018
# Modified by Rahul Kunji (rahulsk2@illinois.edu) on 01/16/2019

"""
This is the main entry point for MP1. You should only modify code
within this file -- the unrevised staff files will be used for all other
files and classes when code is run, so be careful to not modify anything else.
"""


# Search should return the path and the number of states explored.
# The path should be a list of tuples in the form (row, col) that correspond
# to the positions of the path taken by your search algorithm.
# Number of states explored should be a number.
# maze is a Maze object based on the maze from the file specified by input filename
# searchMethod is the search method specified by --method flag (bfs,dfs,greedy,astar)

def search(maze, searchMethod):
    return {
        "bfs": bfs,
        "dfs": dfs,
        "greedy": greedy,
        "astar": astar,
    }.get(searchMethod)(maze)


def bfs(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    start = maze.getStart()
    end = maze.getObjectives()[0]

    frontier = [start]
    # store the explored state with its parent state, to save space
    explored = {start: None}
    pathLength = 1
    numExploredStates = 1
    reachedTarget = False

    while not reachedTarget:
        # next nodes to visit with one step further
        # implement queue by list to maintain FIFO ordering
        nextFrontier = []
        pathLength += 1

        for col, row in frontier:
            if reachedTarget:
                break

            numExploredStates += 1
            neighbors = maze.getNeighbors(col, row)

            for neighbor in neighbors:
                if neighbor in explored:
                    continue

                explored[neighbor] = (col, row)

                if neighbor == end:
                    reachedTarget = True
                    break

                nextFrontier.append(neighbor)

        frontier = nextFrontier

    print(explored)
    print('The path length is ' + str(pathLength))

    # trace back to find the path by the special explored set
    reversedPath = []
    curt = end

    while curt:
        reversedPath.append(curt)
        curt = explored[curt]

    return list(reversed(reversedPath)), numExploredStates


def dfs(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    start = maze.getStart()
    end = maze.getObjectives()[0]

    # the difference between BFS is the list here is used as stack to maintain LIFO ordering
    frontier = [start]
    # store the explored state with its parent state, to save space
    # state: the coordinates, node: the coordinates and their parents
    explored = {start: None}
    numExploredStates = 1
    reachedTarget = False

    while not reachedTarget:
        # use the top of the stack to explore and pop it
        curt = frontier.pop()
        neighbors = maze.getNeighbors(curt[0], curt[1])

        for neighbor in neighbors:
            if neighbor in explored:
                continue

            numExploredStates += 1
            explored[neighbor] = curt

            if neighbor == end:
                reachedTarget = True
                break

            frontier.append(neighbor)

    print(explored)

    # trace back to find the path by the special explored set
    reversedPath = []
    curt = end

    while curt:
        reversedPath.append(curt)
        curt = explored[curt]

    return list(reversed(reversedPath)), numExploredStates


def greedy(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    start = maze.getStart()
    end = maze.getObjectives()[0]
    frontier = [start]
    
    explored = {start:None}
    pathLength = 1
    numExploredStates = 1
    reachedTarget = False
    
    while not reachedTarget:
        curt = frontier.pop()
        neighbors = maze.getNeighbors(curt[0], curt[1])
        dist = [(abs(neighbor[0]-end[0])+abs(neighbor[1]-end[1])) for neighbor in neighbors]
        pair_dist_node =[(dist[i], neighbors[i]) for i in range(len(dist))]
        pair_dist_node.sort()
        pair_dist_node.reverse()

        sorted_neighbors = [pair_dist_node[i][1] for i in range(len(pair_dist_node))] 
        
    
        for  neighbor in sorted_neighbors:
            if neighbor in explored:
                continue
            numExploredStates += 1
            explored[neighbor] = curt 
            if neighbor == end:
                reachedTarget = True
                break
                nextFrontier.append(neighbor)

            frontier.append(neighbor)
            
    print('The path length is ' + str(pathLength))
    reversedPath = []
    curt = end

    while curt:
            reversedPath.append(curt)
            curt = explored[curt]
    return list(reversed(reversedPath)), numExploredStates


def astar(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    start = maze.getStart()
    end = maze.getObjectives()[0]
    h_start = abs(end[0]-start[0]) + abs(end[1] - start[1])
    frontier = [(start, h_start)]

    explored = {(start,h_start):None}
    pathLength = 1
    numExploredStates = 1
    reachedTarget = False

    while not reachedTarget:
        nextFrontier = []
        pathLength += 1
        for coords, fn in frontier:
            if reachedTarget:
                break
            numExploredStates += 1
            neighbors = maze.getNeighbors(coords[0], coords[1])
            dist = [pathLength + abs(neighbor[0] - end[0]) + abs(neighbor[1]-end[1]) for neighbor in neighbors]
            pair_dist = [(dist[i], neighbors[i]) for i in range(len(dist))]
            pair_dist.sort()
            explored_coords_dist = {list(explored.keys())[i][0]:list(explored.keys())[i][1] for i in range(len(explored))}
            for dist_n, coords_n in pair_dist:
                if coords_n in list(explored_coords_dist.keys()):
                    if int(dist_n) > int(explored_coords_dist[coords_n]):
                        continue
                explored[(coords_n, dist_n)] = (coords, fn)
                if coords_n == end:
                    reachedTarget = True
                    break
        
                nextFrontier.append((coords_n, dist_n))
        frontier = nextFrontier
    print('The path length is ' + str(pathLength))
    reversedPath = []
    curt = (end, pathLength)

    while curt:
        reversedPath.append(curt[0])
        curt = explored[curt]
    return list(reversed(reversedPath)), numExploredStates
