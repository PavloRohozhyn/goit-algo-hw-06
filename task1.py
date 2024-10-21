import matplotlib.pyplot as plt
import networkx as nx
from graph import graph


G = graph()
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold', edge_color='gray')
plt.title("Internet Network")
plt.show()
print(f"Count Of Nodes: {G.number_of_nodes()}")
print(f"Count Of Edges: {G.number_of_edges()}")
print("Degree of vertices:", dict(G.degree()))
