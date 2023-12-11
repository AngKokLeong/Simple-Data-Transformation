from entity.item import Item

class Order:

    order_number: str
    customer_name: str
    delivery_postal: str
    item_lines: list[Item] = []
    total_price: float
    unique_items: int

    def __init__(self, order_number: str, customer_name: str, delivery_postal: str, item_lines: list[Item], total_price: float, unique_items: int):
        self.order_number = order_number
        self.customer_name = customer_name
        self.delivery_postal = delivery_postal
        self.item_lines = item_lines
        self.total_price = total_price
        self.unique_items = unique_items

