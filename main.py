from interface.data_processor import Data_Processor
from data_processor.item_data_processor import Item_Data_Processor
from entity.item import Item

from interface.endpoint_data_retrieval import Endpoint_Data_Retrieval
from data.item_data_retrieval import Item_Data_Retrieval

def main():
    #Data_Transformation_Driver.execute()

    endpoint_data_retrieval: Endpoint_Data_Retrieval = Item_Data_Retrieval()


    item_object_from_csv: Item = Item("17", "", "", 3)
    item_object_from_fakestoreapi: Item = endpoint_data_retrieval.retrieve_data(item_object_from_csv.item_id)


    data_processor: Data_Processor = Item_Data_Processor()

    result:Item = data_processor.merge_data(item_object_from_csv, item_object_from_fakestoreapi)

    print(result.item_id)
    print(result.item_name)
    print(result.price)
    print(result.quantity)


if __name__ == "__main__":
    main()



