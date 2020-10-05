import json


def load_data_list_from_json():
    result_data = []
    with open("data_list.json") as data_list:
        result_data = json.load(data_list)

    return result_data


def load_data_object_from_json():
    result_data = None
    with open("data.json") as data:
        result_data = json.load(data)
    return result_data



if __name__ == "__main__":
    data_list_json =  load_data_list_from_json()
    print("    Data list from json    ")
    print(data_list_json)
    data_object =load_data_object_from_json()
    print("    Data  from json    ")
    print(data_object)


