from interface.data_processor import Data_Processor
from data_processor.item_list_data_processor import Item_List_Data_Processor
from entity.item import Item



def main():
    #Data_Transformation_Driver.execute()

    sample_dictionary: dict = {}
    sample_dictionary["0"] = {"line_type": "line_type", "order_number": "4496569", "data": "3", "data_two": "2"}
    sample_dictionary["1"] = {"line_type": "line_type", "order_number": "4496569", "data": "15", "data_two": "4"}
    sample_dictionary["2"] = {"line_type": "line_type", "order_number": "4496569", "data": "8", "data_two": "1"}
    sample_dictionary["3"] = {"line_type": "line_type", "order_number": "4496569", "data": "9", "data_two": "2"}

    item_list_data_processor: Data_Processor = Item_List_Data_Processor()
    
    item_list: list[Item] = item_list_data_processor.process_data(sample_dictionary)



    for item in item_list:
        print(f'item_id: {item.item_id}  item_name: {item.item_name}  price: {item.price}  quantity: {item.quantity} ')

if __name__ == "__main__":
    main()



