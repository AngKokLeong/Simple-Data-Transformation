from entity.item import Item

class Order:

    order_number: str
    customer_name: str
    delivery_postal: str
    item_lines: list[Item] = []
    total_price: float
    unique_items: int

    def __init__(self, order_number: str, customer_name: str, delivery_postal: str, item_lines: list[Item], total_price: float, unique_items: int):
        pass

    def calculate_total_price(self) -> float:
        pass

    def calculate_number_of_unique_items(self) -> int:
        pass
