import json
import yaml


def load_from_json():
    # todo get automated connection to github setup to pull json automatically
    f = open("./test_json_data/ALL.json")
    data = json.load(f)
    f.close()

    python_linkml_struct = {"test": "blah"}
    write_filename = f"output_linkml_yaml/data_dictionary_spreadsheet_{data['meta']['spreadsheet_id']}"

    # is it ok to version thee data_dictionaries by spreadsheet id

    with open(write_filename, "w") as f:
        data = yaml.dump(python_linkml_struct, f, sort_keys=False)


def get_base_linkml_struct():
    """
    Establish the baseline python dictionary that contains the constant linkml
    attributes that will not change from version to version of data dictionaries.
    """
    base_struct = {
        "id": "https://w3id.org/pcdc/model",
        "title": "LinkML Data Dictionary Model",
        "name": "data-dictionary",
        "license": 
    }
    return base_struct


if __name__ == "__main__":
    load_from_json()
