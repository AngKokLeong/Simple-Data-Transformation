from interface.file_processor import File_Processor
from entity.order import Order
from entity.item import Item
import os

class CSV_File_Processor(File_Processor):
    
    CSV_FILE_PATH: str = os.path.abspath('Order Details.csv')

    def read_file(self) -> list[Order]:
        print(self.CSV_FILE_PATH)
        order_list = list[Order]

        with open(self.CSV_FILE_PATH, mode='r') as orders:

            for order in orders:
                line_type, order_number, data, data_two = order.split(',')
                print(f'{line_type:<10}{order_number:<10}{data:>10}{data_two:>10}')


                

        return order_list        

