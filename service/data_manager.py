from data_builder.data_builder import Data_Builder

class Data_Manager(object):

    data_builder: Data_Builder

    def __init__(self):
        self.data_builder = Data_Builder()


    def generate_json(self) -> None:
        self.data_builder.build()
        self.data_builder.generate_json()
        