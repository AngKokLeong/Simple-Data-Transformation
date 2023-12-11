from interface.data_processor import Data_Processor
from data_processor.order_data_processor import Order_Data_Processor
from entity.item import Item
from entity.order import Order


def main():
    #Data_Transformation_Driver.execute()


    file_processor: File_Processor = CSV_File_Processor()
    data = file_processor.read_file()
    print(data)

    #data_processor: Data_Processor = Order_Data_Processor()
    #result_order_object: Order = data_processor.process_data(order_one)

    #print(result_order_object.total_price)
    #print(result_order_object.unique_items)

if __name__ == "__main__":
    main()



