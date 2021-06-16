import matplotlib.pyplot as plt
import networkx as nx

from logic.path.path_finder import path_finder
from logic.hierarchy import hierarchy_pos


def tree():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (2, 7), (3, 8), (3, 9), (4, 10),
                      (5, 11), (5, 12), (6, 13)])
    pos = hierarchy_pos(G, 1)
    node_color = ['red', 'blue', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']
    nx.draw(G, pos=pos, with_labels=True, node_color=node_color)
    plt.show()


