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

    def __str__(self):
        return f"Player{self.id}: {list(str(item) for item in self.items)}"


def greedy(players:list[Player], items:list[Item]):
    num_of_players = len(players)
    index = 0
    for item in items:
        players[index].add_item(item)
        index = (index + 1) % num_of_players 


def main():
    item1 = Item(1, 10)
    item2 = Item(2, 20)
    item3 = Item(3, 30)
    item4 = Item(4, 40)
    item5 = Item(5, 50)

    items = [item1, item2, item3, item4, item5]
    items.sort(key=lambda x: x.value, reverse=True)

    player1 = Player(1)
    player2 = Player(2)
    
    players = [player1, player2]
    
    greedy(players, items)
    print(list(str(player) for player in players))


if __name__ == "__main__":
    main()