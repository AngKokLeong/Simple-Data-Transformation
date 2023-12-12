from interface.data_processor import Data_Processor
from data_processor.order_list_data_processor import Order_List_Data_Processor
from interface.file_processor import File_Processor
from files.csv_file_processor import CSV_File_Processor
from files.json_file_processor import JSON_File_Processor

class Data_Builder:
    
    __order_data_from_csv: dict
    __processed_order_data: dict

    order_list_data_processor: Data_Processor
    csv_file_processor: File_Processor 
    json_file_processor: File_Processor

    def __init__(self):
        self.order_list_data_processor = Order_List_Data_Processor()
        self.csv_file_processor = CSV_File_Processor()
        self.json_file_processor = JSON_File_Processor()
        self.__processed_order_data = {}
        self.__order_data_from_csv = {}



    def prepare_data_from_csv(self) -> None:
        self.__order_data_from_csv = self.csv_file_processor.read_file()

    def prepare_order_data_dict(self) -> None:
        self.__processed_order_data = self.order_list_data_processor.process_data(self.__order_data_from_csv)


    def build(self) -> dict:
       
        self.prepare_data_from_csv()
        self.prepare_order_data_dict()

        return self.__processed_order_data


    def generate_json(self) -> None:

        try:
            for order_data in self.__processed_order_data.values():
                self.json_file_processor.generate_file(order_data)
                
        except IOError:
            print("Unable to write files into the directory")
