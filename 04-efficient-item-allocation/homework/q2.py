import random
import copy
import sys

class Item:
    def __init__(self, id:int, value:int):
        self.id = id
        self.value = value

    def __str__(self):
        return f"Item{self.id}: {self.value}"

class Player:
    def __init__(self, id:int):
        self.id = id
        self.items = []
    
    def add_item(self, item:Item):
        self.items.append(item)

    def get_sum_of_values(self):
        sum = 0
        for item in self.items:
            sum += item.value
        return sum

    def __str__(self):
        return f"Player{self.id}: {list(str(item) for item in self.items)}"


def greedy_allocation(players:list[Player], items:list[Item]):
    num_of_players = len(players)
    index = 0
    for item in items:
        players[index].add_item(item)
        index = (index + 1) % num_of_players 

def get_max_list_value(players: list[Player]):
    max_list = 0
    for player in players:
        p_list = player.get_sum_of_values()
        if p_list > max_list:
            max_list = p_list
    
    return max_list

def random_allocation(players: list[Player], items: list[Item]):
    num_of_players = len(players)
    index = 0
    for item in items:
        players[index].add_item(item)
        index = (index + 1) % num_of_players 

    return players

def optimal_allocation(players: list[Player], items: list[Item]):
    ITERATIONS = 1000
    optimal_players = []
    min_value = sys.maxsize
    for t in range(ITERATIONS):
        players_copy = copy.deepcopy(players)
        items_copy = copy.deepcopy(items)
        random.shuffle(items_copy)
        temp_min_value = get_max_list_value(random_allocation(players_copy, items_copy))
        if temp_min_value < min_value:
            min_value = temp_min_value
            optimal_players = copy.deepcopy(players_copy)
    
    return optimal_players

def items_generator(size:int):
    items = []
    for i in range(1, size+1):
        item_name = "item" + str(i)
        item_name = Item(i, i*10)
        items.append(item_name)

    return items

def players_generator(size: int):
    players = []
    for i in range(1, size+1):
        player_name = "player" + str(i)
        player_name = Player(i)
        players.append(player_name)

    return players

def simulation(iterations: int):
    total_ratio = 0
    for t in range (1, iterations + 1):
        # generates random values in range 1-9
        num_of_items = random.randint(1, 9)
        num_of_players = random.randint(1, 9)
        
        # genrates items and players
        items = items_generator(num_of_items)
        players = players_generator(num_of_players)
        
        # runs the greedy algo
        greedy_allocation(players, items)
        greedy_value = get_max_list_value(players)

        # runs the optimal algo
        optimal_list = optimal_allocation(players, items)
        optimal_value = get_max_list_value(optimal_list)

        # calculates the approximation ratio
        approximation_ratio = greedy_value / optimal_value
        print("approximation ratio: ", "%.2f" %approximation_ratio)
        
        # calculates the total ratio
        total_ratio += approximation_ratio

    # calculates the average ratio
    avg_ratio = total_ratio / iterations
    print("---------------------------")
    print("average ratio: ", "%.2f" %avg_ratio)


def main():
    simulation(10)


if __name__ == "__main__":
    main()