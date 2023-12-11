from interface.file_processor import File_Processor
from files.csv_file_processor import CSV_File_Processor


def main():
    #Data_Transformation_Driver.execute()

    file_processor: File_Processor = CSV_File_Processor()
    data = file_processor.read_file()
    print(data)



if __name__ == "__main__":
    main()



