from interface.data_processor import Data_Processor
from data_processor.order_list_data_processor import Order_List_Data_Processor
from interface.file_processor import File_Processor
from files.csv_file_processor import CSV_File_Processor
from entity.item import Item
from entity.order import Order


def main():
    #Data_Transformation_Driver.execute()

    order_line_data_processor: Data_Processor = Order_List_Data_Processor()
    csv_file_processor: File_Processor = CSV_File_Processor()
    order_data_from_csv: dict = csv_file_processor.read_file()
    
    order_data_object_dict: dict = order_line_data_processor.process_data(order_data_from_csv)


    for key, order_data in order_data_object_dict.items():
        print(f'Order Number: {order_data.order_number}')
        print(f'Customer Name: {order_data.customer_name}')
        print(f'Delivery Postal: {order_data.delivery_postal}')

        for item in order_data.item_lines:
           print(f'item_id: {item.item_id}  item_name: {item.item_name}  price: {item.price}  quantity: {item.quantity} ')

        print(f'Total Price: {order_data.total_price}')
        print(f'Number of Unique Items: {order_data.unique_items}')
        print(" ")


if __name__ == "__main__":
    main()



