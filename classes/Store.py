from classes.Item import StoreItem
from classes.User import StoreUser

class Store:
    def __init__(self, name : str) -> None:
        self.name = name
        self.inventory : list[StoreItem] = []
        self.users : list[StoreUser] = []
        pass
