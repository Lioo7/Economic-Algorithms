import doctest
import matplotlib.pyplot as plt
import networkx as nx
from PlayerNode import PlayerNode
from HouseNode import HouseNode
from Graph import Graph


def swap_houses(desired_house:int, current_player:int, current_house:int, tenant_in_desired_house:int):
    """
    A utility function that swap houses between two players.
    """
    # update the owner of the desired house to be the current player
    current_owner[desired_house] = current_player
    # update the owner the previous house of the current owenr to be the previous tenant in the desured house 
    current_owner[current_house] = tenant_in_desired_house

def remove_players(preferences, players_to_remove):
    """
    A utility function that remove all the players from players_to_remove list from the preferences list.
    """
    for i in sorted(players_to_remove, reverse=True):
        preferences[i] = []
    return preferences

def remove_houses(preferences, houses_to_remove):
    """
    A utility function that remove all the houses from houses_to_remove list from the inner lists in the preferences list.
    """
    for lst in preferences:
        for house in houses_to_remove:
            if house in lst:
                lst.remove(house)
    return preferences

def build_graph_from_input(n, current_owner, next_desired_house):
    G = Graph()

    # create nodes for each player and house
    player_nodes = [PlayerNode(str(i)) for i in range(n)]
    house_nodes = [HouseNode('-' + str(i)) for i in range(n)]

    # iterates over current_owner dict and adds an edge from each key (house) to its value (player/tenant)
    for key, value in current_owner.items():
        G.add_tenant(house_nodes[key], player_nodes[value])

    # iterates over next_desired_house dict and adds an edge from each key (player) to its value (desired house)
    for key, value in next_desired_house.items():
        G.add_desire_house(player_nodes[key], house_nodes[value])
    
    
    plt.title('Input Graph')
    plt.cla() # clear
    nx.draw(G.G, with_labels=True)
    plt.savefig('img/input-graph')
    

def build_graph_from_output(trading_list):
    G = Graph()

    unique = set()
    [unique.add(i) for i in trading_list]
    n = len(unique)

    # create nodes for each player and house
    player_nodes = [PlayerNode(str(i)) for i in range(n)]
    house_nodes = [HouseNode('-' + str(i)) for i in range(n)]

    # iterates over trading_list and adds an edge from each player to its house
    for i in range(len(trading_list)-1):
        player_index = trading_list[i]
        house_index = trading_list[i+1]
        G.add_tenant(house_nodes[house_index], player_nodes[player_index])
    
    plt.title('Output Graph')
    plt.cla() # clear
    nx.draw(G.G, with_labels=True)
    plt.savefig('img/output-graph')

def find_trading_cycle(preferences: list[list[int]], iteration_number=None, save_graphs=False):
    """
    A utility function that find a cycle in the tarding houses graph,
    when all the players have strong preferences.

    Test #1
    >>> preferences = [[2, 1, 0], [1, 0, 2], [0, 2, 1]]
    >>> find_trading_cycle(preferences)
    [0, 2, 0]

    Test #2
    >>> preferences = [[3, 2, 1, 0], [1, 2, 3, 0], [2, 3, 0, 1], [0, 1, 2, 3]]
    >>> find_trading_cycle(preferences)
    [0, 3, 0]

    Test #3
    >>> preferences = [[0, 1], [0, 1]]
    >>> find_trading_cycle(preferences)
    [0, 0]
    """
    n = len(preferences)
    # create a dictionary to store the current owner of each house
    global current_owner
    # {house_id: player_id}
    current_owner = {i: i for i in range(n)}

    # create a dictionary to store the next desired house of each player
    next_desired_house = {i: preferences[i][0] for i in range(n) if preferences[i]}

    # prints the grpahs if the option is activated
    if save_graphs == True and iteration_number == 0:
        build_graph_from_input(n, current_owner, next_desired_house)

    # create a set to store the visited players
    visited = set()
    # start the search from the first player (that is still in the game)
    current_player = None
    for i, preference in enumerate(preferences):
        if preference:
            current_player = i
            break

    # create a list to store the trading cycle
    trading_cycle = []

    while True:
        # add the current player to the visited set
        visited.add(current_player)
        # add the current player to the trading cycle
        trading_cycle.append(current_player)
        # find the current house of the current player
        # current_house = next(key for key, value in current_owner.items() if value == current_player)
        if current_player in current_owner.values():
            current_house = next(key for key, value in current_owner.items() if value == current_player)
        else:
            break

        # find the desired house of the current player
        # desired_house = next_desired_house[current_player]
        if current_player in next_desired_house:
            desired_house = next_desired_house[current_player]
        else:
            break

        # find the current tenant in the desired house of the current player
        # tenant_in_desired_house = current_owner[desired_house]
        if desired_house in current_owner:
            tenant_in_desired_house = current_owner[desired_house]
        else:
            tenant_in_desired_house = None

        if current_house != desired_house:
            swap_houses(desired_house, current_player, current_house, tenant_in_desired_house)

        # update the next desired house of the current player
        # next_desired_house[current_player] = preferences[current_player][preferences[current_player].index(desired_house) + 1]
        if preferences[current_player] and preferences[current_player].index(desired_house) + 1 < len(preferences[current_player]):
            next_desired_house[current_player] = preferences[current_player][preferences[current_player].index(desired_house) + 1]
        else:
            next_desired_house[current_player] = None
    
        # move to the next player
        current_player = tenant_in_desired_house

        # if the current player has been visited before, we have found a trading cycle
        if current_player in visited:
            # if len(trading_cycle) > 1:
            trading_cycle.append(desired_house)
            return trading_cycle

def top_trading_cycle(preferences: list[list[int]], save_graphs=False):
    """ 
    Top trading cycle (TTC) is an algorithm for trading indivisible items without using money. 
    It was developed by David Gale and published by Herbert Scarf and Lloyd Shapley.

    The function gets as an input a list of lists called 'preferences' where each list 
    inside the main list represents the preferences of a player. 
    The function finds a cycle in the trading houses graph.
    The output of the function is a list of integers that describes the circle. 

    For example if the function return the list [11, 15, 17, 11], 
    it means that person 11 receives house 15, person 15 receives house 17, and person 17 receives house 11.

    Note: The function assumes that the preferences are strong and that there is no indifference among the players.

    References:
    https://en.wikipedia.org/wiki/Top_trading_cycle#:~:text=Top%20trading%20cycle%20(TTC)%20is,Herbert%20Scarf%20and%20Lloyd%20Shapley.
    Video with examples: https://www.youtube.com/watch?v=6G8dJXNfr4A

    Test #1
    >>> preferences = [[2, 1, 0], [1, 0, 2], [0, 2, 1]]
    >>> top_trading_cycle(preferences)
    [0, 2, 0, 1, 1]

    Test #2 (from the video above)
    >>> preferences = [[0, 2, 3, 1], [0, 2, 3, 1], [1, 3, 2, 0], [1, 2, 3, 0]]
    >>> top_trading_cycle(preferences)
    [0, 0, 1, 2, 1, 3, 3]

    Test #3
    >>> preferences = [[1, 2, 0], [2, 0, 1], [0, 1, 2]]
    >>> top_trading_cycle(preferences)
    [0, 1, 2, 0]
    """
    iteration_number = 0
    trading_list = []
    while len(preferences) > 0:
        nodes_to_remove = find_trading_cycle(preferences, iteration_number, save_graphs)
        iteration_number += 1
        if nodes_to_remove == None:
            break
        else:
            trading_list.extend(nodes_to_remove)
            players_to_remove = nodes_to_remove[:-1]
            houses_to_remove = nodes_to_remove[1:]

        # remove the players from the preferences
        preferences = remove_players(preferences, players_to_remove)
        # remove the houses from the preferences
        preferences = remove_houses(preferences, houses_to_remove)

    # prints the grpahs if the option is activated
    if save_graphs == True:
        build_graph_from_output(trading_list)

    return trading_list


def main():
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))

    # preferences = [[2, 1, 0], [1, 0, 2], [0, 2, 1]]
    # ans = top_trading_cycle(preferences, save_graphs=True)
    # print(ans)
    # # expected [0, 2, 0, 1, 1]

    # preferences = [[0, 2, 3, 1], [0, 2, 3, 1], [1, 3, 2, 0], [1, 2, 3, 0]]
    # ans = top_trading_cycle(preferences, save_graphs=True)
    # print(ans)
    # # expected [0, 0, 1, 2, 1, 3, 3]
    # # [0:0, 1:2, 2:1, 3:3] p:h

    preferences = [[1, 2, 0], [2, 0, 1], [0, 1, 2]]
    ans = top_trading_cycle(preferences, save_graphs=True)
    print(ans)
    # expected [0,1,2,0]

if __name__ == '__main__':
    main()