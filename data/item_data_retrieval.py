from interface.endpoint_data_retrieval import Endpoint_Data_Retrieval 
from entity.item import Item
import requests

class Item_Data_Retrieval(Endpoint_Data_Retrieval):
    
    GET_SINGLE_PRODUCT_ENDPOINT_URL: str = "https://fakestoreapi.com/products/"

    def retrieve_data(self, item_id: str) -> Item:
    
        try:
            response_result: requests.Response = requests.get(self.prepare_endpoint_url(item_id))
            response_json_result = response_result.json()
            
            new_item: Item = Item(response_json_result["id"], response_json_result["title"], response_json_result["price"], 0);

            print(new_item.item_id)
            print(new_item.item_name)
            print(new_item.price)
            #new_item = json.load(response_json_result)

        
        except requests.ConnectionError:
            print("There is a connection error.")

        except requests.HTTPError:
            print("There is a HTTP error")

        except requests.URLRequired:
            print("The endpoint URL is not valid")

        except requests.ReadTimeout:
            print("The server did not send any data in the allotted amount of time.")

        except requests.JSONDecodeError:
            print("There is a problem decoding the text into JSON.")

    
    def prepare_endpoint_url(self, item_id: str) -> str:
        return self.GET_SINGLE_PRODUCT_ENDPOINT_URL + str(item_id)