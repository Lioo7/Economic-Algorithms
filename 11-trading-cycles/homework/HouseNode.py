class HouseNode:
    last_id = 0
    def __init__(self):
        self.id = HouseNode.last_id - 1
        HouseNode.last_id = self.id
        self.next = None

    def set_next(self, next_node):
        self.next = next_node

    def __str__(self):
        # next_id = self.next.id if self.next != None else 'unoccupied'
        return f'h{self.id}'