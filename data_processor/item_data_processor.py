from interface.data_processor import Data_Processor
from entity.item import Item
from entity.order import Order
from interface.endpoint_data_retrieval import Endpoint_Data_Retrieval
from data.item_data_retrieval import Item_Data_Retrieval

class Item_Data_Processor(Data_Processor):

    item_data_retrieval: Endpoint_Data_Retrieval = Item_Data_Retrieval()

    def process_data(self, item_id: str, item_object: Item) -> Item:
        # process item data list based on one order number in the unique order number list
        if item_object != None:
            item_data_object_from_fake_store_api: Item = self.__create_item_from_fake_store_api(item_id)
            return self.__merge_item_data_object(item_object, item_data_object_from_fake_store_api)
        
        return None

    def __merge_item_data_object(self, item_object_one: Item, item_object_two: Item) -> Item:
        
        if item_object_one.item_name == '' and item_object_one.price == '':
            item_object_one.item_name = item_object_two.item_name
            item_object_one.price = item_object_two.price
    
            return item_object_one
            
        elif item_object_two.item_name == '' and item_object_two.price == '':
            item_object_two.item_name = item_object_one.item_name
            item_object_two.price = item_object_one.price
    
            return item_object_two

    def __create_item_from_fake_store_api(self, id: str) -> Item:
        new_item_object: Item = self.item_data_retrieval.retrieve_data(id)
        
        return new_item_object

        
