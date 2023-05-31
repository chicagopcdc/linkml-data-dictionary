"""
This script tests ingesting different types of data to see how the linkml model objects 
can be created from them and what errors/validation can arise.
"""
import json
from linkml_data_dictionary.python_model.data_dictionary_generated_fixed_quotes import (
    Person,
)
import pandas as pd
from typing import Dict


# TODO generalize to all classes, test on other classes
def create_people(json_data: Dict):
    # assuming all entries have the same columns/keys, get the valid ones for this case:
    matching_attributes = []
    possible_attributes = dir(Person)
    matching_attributes = [
        key_val
        for key_val in json_data[0].keys()
        if key_val in possible_attributes
    ]
    person_list = []
    for el in json_data:
        person_instance = Person(
            **{keyval: el[keyval] for keyval in matching_attributes}
        )
        person_list.append(person_instance)
    return person_list


def test_json():
    # success case
    # load 'data_validation/gen3_person_renamed_keys.json' and convert to Person object
    # there are 8 entries so there should be 8 person objects created
    f = open(
        "./linkml_data_dictionary/data_validation/gen3_person_renamed_keys.json",
        "r",
    )
    good_test_data = json.loads(f.read())
    f.close()
    success_list = create_people(good_test_data)

    # bad case w/ incorrect slot values provided ex. "ethnicity" = "InvalidEthnicity"
    # load 'data_validation/gen3_person_w_bad_data.json' and try to convert to Person
    # of 10 input objects, 8 are valid and 2 are invalid
    f_bad = open(
        "./linkml_data_dictionary/data_validation/gen3_person_w_bad_data.json",
        "r",
    )
    bad_test_data = json.loads(f_bad.read())
    f_bad.close()

    try:
        fail_list_slot_values = create_people(bad_test_data)
    except ValueError as err:
        print("value errors")
        print(err)

    # bad case w/ incorrect slot keys provided ex. "InvalidSlot" = "Not Hispanic or Latino"
    # load 'data_validation/gen3_person_invalid_slot_names.json' and try to convert to Person
    # if it was able to succeed it would have 8 results
    f_bad_slot = open(
        "./linkml_data_dictionary/data_validation/gen3_person_invalid_slot_names.json",
        "r",
    )
    bad_slot_test_data = json.loads(f_bad_slot.read())
    f_bad_slot.close()
    try:
        fail_list_slot_keys = create_people(bad_slot_test_data)
    except ValueError as err:
        print("key errors")
        print(err)

    # check https://linkml.io/linkml/data/validating-data.html#validation-of-json-documents python validation

    # ideal behavior
    # create script to feed tsv in (one tsv (should be in file name) relates to one object type but can require input for the first pass)
    # have an option to either fail on first mismatch (either keyvalue wrong or supplied value wrong) or proceed after failure
    # create linkml python objects


def test_tsv():
    # this passes
    good_df = pd.read_csv(
        "./linkml_data_dictionary/data_validation/gen3_person_updated_column.tsv",
        sep="\t",
    )
    good_dict_of_people = good_df.to_dict(orient="records")
    try:
        people = create_people(good_dict_of_people)
    except ValueError as err:
        print("value errors")
        print(err)

    # this fails on submitter id column name


test_tsv()
