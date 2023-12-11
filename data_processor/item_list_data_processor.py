from interface.data_processor import Data_Processor
from entity.item import Item
from data_processor.item_data_processor import Item_Data_Processor

class Item_List_Data_Processor(Data_Processor):

    item_list: list[Item] = []
    item_data_processor: Data_Processor = Item_Data_Processor()

    def process_data(self, item_data_dict: dict) -> list[Item]:
        
        for data in item_data_dict.values():

            self.item_list.append(self.__create_item_object_with_csv_data_and_fake_store_api_data(data["data"], self.__create_item_object_from_csv_data(data)))

        return self.item_list

    def __create_item_object_with_csv_data_and_fake_store_api_data(self, item_id: str, item_data_object: Item) -> Item:
        new_item_object: Item = self.item_data_processor.process_data(item_id, item_data_object)
        return new_item_object
        

    def __create_item_object_from_csv_data(self, item_data: dict) -> Item:
        if item_data != None:
            return Item(item_data["data"], "", 0.0, item_data["data_two"])
        
        return None
