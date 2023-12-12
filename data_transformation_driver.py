from controller.order_controller import Order_Controller

class Data_Transformation_Driver:

    order_controller: Order_Controller

    def __init__(self):
        self.order_controller = Order_Controller()

    def execute(self):
        self.order_controller.generate_json()