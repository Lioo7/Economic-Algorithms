from PlayerNode import PlayerNode
from HouseNode import HouseNode
from Graph import Graph

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