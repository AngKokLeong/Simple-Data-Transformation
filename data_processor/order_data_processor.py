from interface.data_processor import Data_Processor
from entity.order import Order
from entity.item import Item


class Order_Data_Processor(Data_Processor):
    
    def process_data(self, order_data_object: Order) -> Order:
        
        order_data_object.total_price = self.__calculate_total_price_of_ordered_amount(order_data_object)
        order_data_object.unique_items = self.__calculate_number_of_unique_items(order_data_object)

        return order_data_object
        

    def __calculate_total_price_of_ordered_amount(self, order_data_object: Order) -> float:

        total_amount: float = 0.0

        if order_data_object.item_lines != None or len(order_data_object.item_lines) > 0:
            
            for item in order_data_object.item_lines:
                total_amount += (item.price * item.quantity)

        return total_amount    

    def __calculate_number_of_unique_items(self, order_data_object: Order) -> int:
        
        number_of_unique_items: int = 0

        if order_data_object.item_lines != None or len(order_data_object.item_lines) > 0:
            number_of_unique_items = len(order_data_object.item_lines)

        return number_of_unique_items