from data.item_data_retrieval import Item_Data_Retrieval
from interface.endpoint_data_retrieval import Endpoint_Data_Retrieval



def main():
    #Data_Transformation_Driver.execute()

    endpoint_data_retrieval: Endpoint_Data_Retrieval = Item_Data_Retrieval()
    endpoint_data_retrieval.retrieve_data(1)

    #file_processor: File_Processor = CSV_File_Processor()
    #file_processor.read_file()




if __name__ == "__main__":
    main()



