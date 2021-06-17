import matplotlib.pyplot as plt
import networkx as nx

from logic.path.path_finder import path_finder
from logic.hierarchy import hierarchy_pos


def tree():

    tree_G, tree_color, root = path_finder('demo')

    G = nx.Graph()
    G.add_edges_from(tree_G)
    pos = hierarchy_pos(G, root)
    nx.draw(G, pos=pos, with_labels=True, node_color=tree_color)
    plt.show()


