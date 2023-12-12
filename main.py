from service.data_builder import Data_Builder
from entity.item import Item
from entity.order import Order


def main():
    #Data_Transformation_Driver.execute()

    data_builder: Data_Builder = Data_Builder()
    order_data_object_dict: dict = data_builder.build()


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



