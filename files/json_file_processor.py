from interface.file_processor import File_Processor
from entity.order import Order
import os
import json

class JSON_File_Processor(File_Processor):

    JSON_OUTPUT_FILE_PATH: str = os.path.abspath("json_output_file")

    def generate_file(self, order_data: Order) -> None:
        #write the json file based on the file path provided here
        with open(self.apply_file_naming_convention(order_data.order_number), 'w') as order:
            json.dump(order_data.__dict__, order)



        
    def apply_file_naming_convention(self, order_number: str) -> str:
        return self.JSON_OUTPUT_FILE_PATH + str('/') + "order" + str(order_number) + ".json" 
        

    