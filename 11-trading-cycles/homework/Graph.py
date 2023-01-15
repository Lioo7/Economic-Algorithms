from typing import Union
import networkx as nx
import matplotlib.pyplot as plt
from PlayerNode import PlayerNode
from HouseNode import HouseNode

class Graph:
    def __init__(self):
        self.G = nx.DiGraph()
    
    def add_node(self, node: Union[PlayerNode, HouseNode]):
        self.G.add_node(node.id)

    def add_desire_house(self, src_node: PlayerNode, dest_node: HouseNode):
        self.G.add_edge(src_node.id, dest_node.id)

    def add_tenant(self, src_node: HouseNode, dest_node: PlayerNode):
        self.G.add_edge(src_node.id, dest_node.id)

    def connect(self, node1: Union[PlayerNode, HouseNode], node2: Union[PlayerNode, HouseNode]):
        self.G.add_edge(node1.id, node2.id)
    
    def draw(self):
        nx.draw(self.G, with_labels=True, arrows=True)
        plt.show()