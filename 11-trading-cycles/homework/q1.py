from typing import Union
import networkx as nx
import matplotlib.pyplot as plt

class PlayerNode:
    last_id = 0
    def __init__(self):
        self.id = PlayerNode.last_id + 1
        PlayerNode.last_id = self.id
        self.next = None

    def set_next(self, next_node):
        self.next = next_node

    def __str__(self):
        next_id = self.next.id if self.next != None else 'homeless'
        return f'p{self.id}'

class HouseNode:
    last_id = 0
    def __init__(self):
        self.id = HouseNode.last_id - 1
        HouseNode.last_id = self.id
        self.next = None

    def set_next(self, next_node):
        self.next = next_node

    def __str__(self):
        next_id = self.next.id if self.next != None else 'unoccupied'
        return f'h{self.id}'

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


def main():
    graph = Graph()
    p1 = PlayerNode()
    h1 = HouseNode()
    p2 = PlayerNode()
    h2 = HouseNode()
    graph.add_node(p1)
    graph.add_node(h1)
    graph.add_node(p2)
    graph.add_node(h2)
    graph.add_desire_house(p1, h1)
    graph.add_desire_house(p2, h1)
    graph.add_tenant(h1, p1)
    graph.draw()


if __name__ == '__main__':
    main()