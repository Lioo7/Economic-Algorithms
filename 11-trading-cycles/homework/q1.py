from PlayerNode import PlayerNode
from HouseNode import HouseNode
from Graph import Graph

def swap_houses(desired_house:int, current_player:int, current_house:int, tenant_in_desired_house:int):
    """
    The function swap houses between two players
    """
    # update the owner of the desired house to be the current player
    current_owner[desired_house] = current_player
    # update the owner the previous house of the current owenr to be the previous tenant in the desured house 
    current_owner[current_house] = tenant_in_desired_house

def remove_players(preferences, players_to_remove):
    """
    The function remove all the players from players_to_remove list from the preferences list
    """
    for i in sorted(players_to_remove, reverse=True):
        preferences[i] = []
    return preferences

def remove_houses(preferences, houses_to_remove):
    """
    The function remove all the houses from houses_to_remove list from the inner lists in the preferences list
    """
    for lst in preferences:
        for house in houses_to_remove:
            if house in lst:
                lst.remove(house)
    return preferences

def find_trading_cycle(preferences: list[list[int]]):
    """
    The function find a cycle in the tarding houses graph,
    when all the players have strong preferences
    """
    print('preferences:', preferences)
    n = len(preferences)
    # create a dictionary to store the current owner of each house
    global current_owner
    # {house_id: player_id}
    current_owner = {i: i for i in range(n)}

    # create a dictionary to store the next desired house of each player
    next_desired_house = {i: preferences[i][0] for i in range(n) if preferences[i]}

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

def top_trading_cycle(preferences: list[list[int]]):
    trading_list = []
    while len(preferences) > 0:
        nodes_to_remove = find_trading_cycle(preferences)
        print('nodes_to_remove:', nodes_to_remove)
        if nodes_to_remove == None:
            print('done!')
            break
        else:
            trading_list.extend(nodes_to_remove)
            players_to_remove = nodes_to_remove[:-1]
            # add all the values in a list at odd indexes
            houses_to_remove = nodes_to_remove[1:]

        # remove the players from the preferences
        preferences = remove_players(preferences, players_to_remove)
        # remove the houses from the preferences
        preferences = remove_houses(preferences, houses_to_remove)

    return trading_list


def test_find_trading_cycle():
    preferences = [[2, 1, 0], [1, 0, 2], [0, 2, 1]]
    expected_result = [0, 2, 0]
    print(find_trading_cycle(preferences))
    assert find_trading_cycle(preferences) == expected_result

    preferences = [[3, 2, 1, 0], [1, 2, 3, 0], [2, 3, 0, 1], [0, 1, 2, 3]]
    expected_result = [0, 3, 0]
    print(find_trading_cycle(preferences))
    assert find_trading_cycle(preferences) == expected_result

    preferences = [[0, 1], [0, 1]]
    expected_result = [0]
    print(find_trading_cycle(preferences))
    assert find_trading_cycle(preferences) == expected_result


def main():
    # test_find_trading_cycle()
    
    # test1
    preferences = [[2, 1, 0], [1, 0, 2], [0, 2, 1]]
    expected_result = [0, 2, 0]
    print(top_trading_cycle(preferences))

    # test2
    preferences = [[0, 2, 3, 1], [0, 2, 3, 1], [1, 3, 2, 0], [1, 2, 3, 0]]
    expected_result = [0, 2, 0]
    print(top_trading_cycle(preferences))

if __name__ == '__main__':
    main()