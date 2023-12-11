from interface.data_processor import Data_Processor
from data_processor.item_data_processor import Item_Data_Processor
from entity.item import Item



def main():
    #Data_Transformation_Driver.execute()

    item_data_processor: Data_Processor = Item_Data_Processor()
    
    result_item_object: Item = item_data_processor.process_data("1", Item(17, "", "", 3))

    print(result_item_object.item_id)
    print(result_item_object.item_name)
    print(result_item_object.price)
    print(result_item_object.quantity)

if __name__ == "__main__":
    main()



