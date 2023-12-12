from interface.data_processor import Data_Processor
from data_processor.order_data_processor import Order_Data_Processor
import multiprocessing
from entity.order import Order
import json

class Order_List_Data_Processor(Data_Processor):
    csv_data_dictionary: dict
    grouped_order_number_data_dictionary: dict
    unique_order_number_dict: dict
    order_dict: dict

    order_data_processor: Data_Processor

    def __init__(self):
        self.csv_data_dictionary = {}
        self.grouped_order_number_data_dictionary = {}
        self.unique_order_number_dict = {}
        self.order_dict = {}

        self.order_data_processor = Order_Data_Processor()

    
    def process_data(self, csv_data_dictionary: dict) -> dict:
        self.csv_data_dictionary = csv_data_dictionary

        self.__prepare_list_of_unique_order_number()

        for record in self.unique_order_number_dict.keys():
           
            self.__filter_dictionary_according_to_order_number(record)

        self.__create_order_data_list()

        return self.order_dict

    def __prepare_list_of_unique_order_number(self) -> None:
        for data in self.csv_data_dictionary.values():
            self.unique_order_number_dict[data["order_number"]] = data["order_number"]

    def __create_order_data_list(self) -> None:

        for dictionary in self.grouped_order_number_data_dictionary.values():
            
            order_data_object: Order = self.order_data_processor.process_data(dictionary)
            
            self.order_dict[order_data_object.order_number] = order_data_object
        

    # group data that are relevant to one order_number

    #def __group_records_with_order_number() -> None:

        #create all tasks
    # processes = [multiprocessing.Process(target=)]
        
    
    def __filter_dictionary_according_to_order_number(self, order_number: str) -> None:
        
        filtered_dictionary_key_list_by_order_number: list[str] = []
        for key, data in self.csv_data_dictionary.items():
            if data["order_number"] == order_number:
                filtered_dictionary_key_list_by_order_number.append(key)
        
        self.__create_new_dictionary_by_dictionary_key_list_and_order_number(order_number, filtered_dictionary_key_list_by_order_number)


    
    def __create_new_dictionary_by_dictionary_key_list_and_order_number(self, order_number: str, dictionary_key_list: list[str]) -> None:
        new_dictionary: dict = {}
        index: int = 0
        for dictionary_key in dictionary_key_list:
            new_dictionary[index] = self.csv_data_dictionary[dictionary_key]
            index = index + 1

       
        self.grouped_order_number_data_dictionary[order_number] = new_dictionary    
   
        