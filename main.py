from interface.file_processor import File_Processor
from files.json_file_processor import JSON_File_Processor
from entity.order import Order

def main():
    #Data_Transformation_Driver.execute()

    order_data: Order = Order('456789', 'asdasd', '123456', [], 56, 3)


    file_processor: File_Processor = JSON_File_Processor()
    file_processor.generate_file(order_data)




if __name__ == "__main__":
    main()



