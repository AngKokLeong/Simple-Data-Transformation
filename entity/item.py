class Item:

    item_id: str
    item_name: str
    price: float
    quantity: int

    def __init__(self, item_id: str, item_name:str, price:float, quantity:int):
        self.item_id = item_id
        self.item_name = item_name
        self.price = price
        self.quantity = quantity