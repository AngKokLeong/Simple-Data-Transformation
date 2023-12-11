from interface.data_processor import Data_Processor
from data_processor.order_data_processor import Order_Data_Processor
from entity.item import Item
from entity.order import Order


def main():
    #Data_Transformation_Driver.execute()

    sample_dictionary: dict = {}
    sample_dictionary["0"] = {"line_type": "Header", "order_number": "4496569", "data": "James", "data_two": "156389"}
    sample_dictionary["1"] = {"line_type": "Line", "order_number": "4496569", "data": "3", "data_two": "2"}
    sample_dictionary["2"] = {"line_type": "Line", "order_number": "4496569", "data": "15", "data_two": "4"}
    sample_dictionary["3"] = {"line_type": "Line", "order_number": "4496569", "data": "8", "data_two": "1"}
    sample_dictionary["4"] = {"line_type": "Line", "order_number": "4496569", "data": "9", "data_two": "2"}

    order_data_processor: Data_Processor = Order_Data_Processor()
    
    order_data: Order = order_data_processor.process_data(sample_dictionary)

    print(f'Order Number: {order_data.order_number}')
    print(f'Customer Name: {order_data.customer_name}')
    print(f'Delivery Postal: {order_data.delivery_postal}')
    for item in order_data.item_lines:
        print(f'item_id: {item.item_id}  item_name: {item.item_name}  price: {item.price}  quantity: {item.quantity} ')

    print(f'Total Price: {order_data.total_price}')
    print(f'Number of Unique Items: {order_data.unique_items}')

if __name__ == "__main__":
    main()



