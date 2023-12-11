from interface.file_processor import File_Processor
from entity.order import Order
from entity.item import Item
import io
import os

class CSV_File_Processor(File_Processor):
    
    CSV_FILE_PATH: str = os.path.abspath('Order Details.csv')
    
    data_storage: dict = {}

    def read_file(self) -> dict:

        with open(self.CSV_FILE_PATH, mode='r') as data_set:
            index: int = 0
            for data in data_set:
                line_type, order_number, data, data_two = data.split(',')
                self.data_storage[index] = {"line_type": line_type, "order_number": order_number, "data": data, "data_two": data_two} 

                index = index + 1

        return self.data_storage


