from interface.data_processor import Data_Processor
from data_processor.order_data_processor import Order_Data_Processor
from entity.item import Item
from entity.order import Order


def main():
    #Data_Transformation_Driver.execute()

    order_one: Order = Order("4269010", "Daisy Duck", "156389", [Item("7", "White Gold Plated Princess", 9.99, 1), Item("17", "Rain Jacket Women Windbreaker Striped Climbing", 39.99, 3)], 0.0, 0)
    

    data_processor: Data_Processor = Order_Data_Processor()
    result_order_object: Order = data_processor.process_data(order_one)

    print(result_order_object.total_price)
    print(result_order_object.unique_items)

if __name__ == "__main__":
    main()



