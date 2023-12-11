from interface.data_processor import Data_Processor
from entity.item import Item
from collections import ChainMap

class Item_Data_Processor(Data_Processor):

    def merge_data(self, item_object_one: Item, item_object_two: Item) -> Item:
        
            if item_object_one.item_name == '' and item_object_one.price == '':
                item_object_one.item_name = item_object_two.item_name
                item_object_one.price = item_object_two.price
    
                return item_object_one
            
            elif item_object_two.item_name == '' and item_object_two.price == '':
                item_object_two.item_name = item_object_one.item_name
                item_object_two.price = item_object_one.price
    
                return item_object_two



        

