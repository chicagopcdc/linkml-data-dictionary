from linkml_data_dictionary.python_model.data_dictionary_generated_fixed_quotes import (
    Person,
)
import pandas as pd
from typing import Dict


def create_linkml_obj(data: Dict):
    """
    Take the ingested tsv data and try to map the key-values to instantiate
    the linkml class.

    Could either create some factory to map the type of object
    to the class to instantiate or have scripts for each,
    but that needs to be done to generalize more.
    """
    # assuming all entries have the same columns/keys, get the valid ones for this case:
    matching_attributes = []
    possible_attributes = dir(Person)
    matching_attributes = [
        key_val for key_val in data[0].keys() if key_val in possible_attributes
    ]
    obj_list = []
    for el in data:
        person_instance = Person(
            **{keyval: el[keyval] for keyval in matching_attributes}
        )
        obj_list.append(person_instance)
    return obj_list


def validate_tsv(tsv_filename, fail_fast=False):
    """
    Inputs:
        tsv_filename: file corresponding to a single type of LinkML object, for example: "./linkml_data_dictionary/data_validation/gen3_person_updated_column.tsv"

    Returns:
        list of python objects that have been instantiated
    """
    df = pd.read_csv(
        tsv_filename,
        sep="\t",
    )
    dict_of_obj = df.to_dict(orient="records")
    try:
        objects = create_linkml_obj(dict_of_obj)
    except ValueError as err:
        print("value errors")
        print(err)
        if fail_fast:
            raise (err)

    return objects


validate_tsv(
    "./linkml_data_dictionary/data_validation/gen3_person_updated_column.tsv"
)
