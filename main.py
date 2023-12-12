from controller.order_controller import Order_Controller


def main():

    order_controller: Order_Controller = Order_Controller()
    order_controller.generate_json()



if __name__ == "__main__":
    main()



