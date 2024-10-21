import networkx as nx
import matplotlib.pyplot as plt
from graph import graph

G = graph()
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold', edge_color='gray')
edge_labels = nx.get_edge_attributes(G, 'weight') # weight
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Internet Nertwork")
plt.show()
# Dijkstra Algo. (Edsger Wybe Dijkstra)
shortest_paths = dict(nx.all_pairs_dijkstra_path(G))
# All Short Paths
for start_node in shortest_paths:
    print(f"The Shortest Path From {start_node}:")
    for end_node, path in shortest_paths[start_node].items():
        print(f"  From {end_node}: Path - {path}")
