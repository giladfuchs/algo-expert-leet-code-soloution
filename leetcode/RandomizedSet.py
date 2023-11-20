from random import choice


class RandomizedSet:
    def __init__(self):
        self.item_to_position = {}
        self.items = []

    def insert(self, item) -> bool:
        if item in self.item_to_position:
            return False
        self.items.append(item)
        self.item_to_position[item] = len(self.items) - 1

        return True

    def remove(self, item) -> bool:
        if item not in self.item_to_position:
            return False
        position = self.item_to_position.pop(item)
        last_item = self.items.pop()
        if position != len(self.items):
            self.items[position] = last_item
            self.item_to_position[last_item] = position
        return True

    def getRandom(self) -> int:
        return choice(self.items)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
