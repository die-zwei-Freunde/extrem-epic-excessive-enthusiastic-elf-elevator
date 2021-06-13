import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

import matplotlib.pyplot as plt
import networkx as nx
import random


class MainWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def plot(self):

        def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
            '''
            From Joel's answer at https://stackoverflow.com/a/29597209/2966723.
            Licensed under Creative Commons Attribution-Share Alike

            If the graph is a tree this will return the positions to plot this in a
            hierarchical layout.

            G: the graph (must be a tree)

            root: the root node of current branch
            - if the tree is directed and this is not given,
              the root will be found and used
            - if the tree is directed and this is given, then
              the positions will be just for the descendants of this node.
            - if the tree is undirected and not given,
              then a random choice will be used.

            width: horizontal space allocated for this branch - avoids overlap with other branches

            vert_gap: gap between levels of hierarchy

            vert_loc: vertical location of root

            xcenter: horizontal location of root
            '''
            if not nx.is_tree(G):
                raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

            if root is None:
                if isinstance(G, nx.DiGraph):
                    root = next(iter(nx.topological_sort(G)))  # allows back compatibility with nx version 1.11
                else:
                    root = random.choice(list(G.nodes))

            def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
                '''
                see hierarchy_pos docstring for most arguments

                pos: a dict saying where all nodes go if they have been assigned
                parent: parent of this branch. - only affects it if non-directed

                '''

                if pos is None:
                    pos = {root: (xcenter, vert_loc)}
                else:
                    pos[root] = (xcenter, vert_loc)
                children = list(G.neighbors(root))
                if not isinstance(G, nx.DiGraph) and parent is not None:
                    children.remove(parent)
                if len(children) != 0:
                    dx = width / len(children)
                    nextx = xcenter - width / 2 - dx / 2
                    for child in children:
                        nextx += dx
                        pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                             vert_loc=vert_loc - vert_gap, xcenter=nextx,
                                             pos=pos, parent=root)
                return pos

            return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)

        G = nx.Graph()
        G.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (2, 7), (3, 8), (3, 9), (4, 10),
                          (5, 11), (5, 12), (6, 13)])
        pos = hierarchy_pos(G, 1)
        nx.draw(G, pos=pos, with_labels=True)
        plt.show()


class WindowManager(ScreenManager):
    pass


sm = WindowManager()

kv = Builder.load_file('story_writer.kv')

screens = [MainWindow(name='main')]
for screen in screens:
    sm.add_widget(screen)

sm.current = 'main'


class Story_WriterApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    Story_WriterApp().run()