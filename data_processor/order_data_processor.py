from interface.data_processor import Data_Processor
from entity.order import Order
from entity.item import Item
from data_processor.item_list_data_processor import Item_List_Data_Processor

class Order_Data_Processor(Data_Processor):
    
    HEADER_DATA_TYPE: str = "Header"
    LINE_DATA_TYPE: str = "Line"
    item_list_data_processor: Data_Processor = Item_List_Data_Processor()
    data_storage: dict = {}

    def process_data(self, order_data_storage: dict) -> Order:
        
        self.data_storage = order_data_storage

        order_data_object: Order = self.__extract_order_data_from_dictionary()

        order_data_object.item_lines = self.item_list_data_processor.process_data(self.data_storage)

        order_data_object.total_price = self.__calculate_total_price_of_ordered_amount(order_data_object)
        order_data_object.unique_items = self.__calculate_number_of_unique_items(order_data_object)


        order_data_object.item_lines = self.__convert_list_to_dict(order_data_object.item_lines)

        return order_data_object
        

    def __extract_order_data_from_dictionary(self) -> Order:

        for key, data in self.data_storage.items():
            if data["line_type"] == self.HEADER_DATA_TYPE:
                order_data_object: Order = Order(str(data["order_number"]).strip(), str(data["data"]).strip(), str(data["data_two"]).strip(), [], 0.0, 0)
                self.__remove_record_from_dictionary(key)
                return order_data_object
            
        return None

    def __remove_record_from_dictionary(self, key: any) -> None:
        self.data_storage.pop(key)

    def __convert_list_to_dict(self, item_line: list[Item]) -> list[dict]:
        
        item_line_dict: list[dict] = []
        for item in item_line:
            item_line_dict.append(item.__dict__)
        
        return item_line_dict


    def __calculate_total_price_of_ordered_amount(self, order_data_object: Order) -> float:

        total_amount: float = 0.0

        if order_data_object.item_lines != None or len(order_data_object.item_lines) > 0:
            
            for item in order_data_object.item_lines:
                total_amount += (item.price * float(item.quantity))

        return float(str("{0:.2f}").format(total_amount))   

    def __calculate_number_of_unique_items(self, order_data_object: Order) -> int:
        
        number_of_unique_items: int = 0

        unique_item_found: list = []

        if order_data_object.item_lines != None or len(order_data_object.item_lines) > 0:

            for item in order_data_object.item_lines:
                if item.item_id not in unique_item_found:
                    unique_item_found.append(item.item_id)
                    
            number_of_unique_items = len(unique_item_found)

        return number_of_unique_items