import utils
import settings

class StoreItem:
    def __init__(self, name : str | None, pricePerItem : int, quantity : int = 1) -> None:
        self.name = name if name else utils.getItemName()
        self.price = pricePerItem
        self.id = utils.getItemId() # Generate a random id unless one is provided
        self.quantity = quantity >= 0 and quantity or 0 # cannot have negative quantity
        
    def __str__(self) -> str:
        return f"{self.name} - {self.price}{settings.CURRENCY_SYMBOL} - {self.id}"