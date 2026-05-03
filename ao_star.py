PROGRAM 3: AO* Search Algorithm

import heapq

class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def parse_graph_input():
    graph = {}
    num_edges = int(input("Enter the number of edges: "))

    for _ in range(num_edges):
        u, v, cost = input("Enter an edge (format: u v cost): ").split()
        cost = float(cost)

        if u not in graph:
            graph[u] = []

        graph[u].append((v, cost))

    return graph


def heuristic(state, goal_state):
    heuristic_values = {
        'A': 5,
        'B': 3,
        'C': 2,
        'D': 1,
        'E': 2,
        'G': 0
    }
    return heuristic_values.get(state, float('inf'))


def ao_star_search(start_state, goal_state, graph):
    frontier = []

    heap
