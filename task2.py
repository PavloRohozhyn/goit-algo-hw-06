import networkx as nx
from collections import deque
from graph import graph


# DFS
def dfs_path(graph, start, target, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == target:
        return path
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_path = dfs_path(graph, neighbor, target, path)
            if new_path:
                return new_path
    return None

# BFS
def bfs_path(graph, start, target):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for neighbor in graph.neighbors(vertex):
            if neighbor not in path:
                if neighbor == target:
                    return path + [neighbor]
                else:
                    queue.append((neighbor, path + [neighbor]))
    return None


G = graph()
# case
start_node = 'ISP_1'
target_node = 'User_4'
# DFS
dfs_result = dfs_path(G, start_node, target_node)
# BFS
bfs_result = bfs_path(G, start_node, target_node)
# result
print(f"DFS -> {dfs_result}")
print(f"BFS -> {bfs_result}")
