from service.data_manager import Data_Manager

class Order_Controller(object):

    data_manager: Data_Manager

    def __init__(self):
        self.data_manager = Data_Manager()


    def generate_json(self):
        self.data_manager.generate_json()