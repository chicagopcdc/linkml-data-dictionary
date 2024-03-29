import json
from typing import Dict, Tuple
import yaml

# characters that cannot be used in the naming schemes and need to be parsed out
disallowed_vals_in_name = ["%", "?"]


def load_from_json(
    json_data: str = "linkml_data_dictionary/data_ingestion_to_linkml/test_json_data/Aggregated.json",
) -> None:
    """
    Load data from a json file that contains all data dicitonary data and
    create corresponding LinkML classes, enums and slots so that a YAML
    file for LinkML can be generated. From the YAML, Python classes and
    Markdown can be generated to do data validation and document the
    structure of the data.

    Inputs:
        json_data (str): filename for the json data being processed
    """
    f = open(json_data)
    data = json.load(f)
    f.close()

    python_linkml_struct = get_base_linkml_struct()

    """
    Pull subject characteristics and timings out of data['domains']['protocol']
    Pull person and out of data['demographics']['demographics']
    Everything else is named the same as its key in the json
    (under protocol, demographics, testing, etc.)
    """
    subject = data["domains"]["Protocol"]["Subject Characteristics"]
    person = data["domains"]["Demographics"]["Demographics"]

    data_class_mapping = {
        "Person": person,
        "Subject": subject,
    }

    manually_named = [
        "Subject Characteristics",
        "Demographics",
    ]

    for key in data["domains"]:
        for child_key in data["domains"][key]:
            if child_key not in manually_named:
                classname = "".join(el.title() for el in child_key.split("_"))
                data_class_mapping[classname] = data["domains"][key][child_key]

    for key in data_class_mapping.keys():
        python_linkml_struct = create_class(
            python_linkml_struct, key, data_class_mapping[key]
        )
        if key == "Subject":
            python_linkml_struct["classes"]["Subject"]["attributes"][
                "persons"
            ] = {
                "range": "Person",
                "required": True,
            }

    write_filename = f"linkml_data_dictionary/data_ingestion_to_linkml/output_linkml_yaml/data_dictionary_spreadsheet_{data['meta']['sheet_id']}_{data['meta']['timestamp']}.yaml"
    with open(write_filename, "w") as f:
        data = yaml.dump(python_linkml_struct, f, sort_keys=False)


def get_base_linkml_struct() -> Dict:
    """
    Establish the baseline python dictionary that contains the constant linkml
    attributes that will not change from version to version of data dictionary.

    Output:
        base_struct (dict): templated dictionary with all of the unchanging information
    """
    # TODO: figure out a versioning scheme so everything isn't 0.0.1
    # TODO: locate ICDO endpoint that will allow for code lookup when it exists (currently just points to WHO page)
    base_struct = {
        "id": "https://w3id.org/pcdc/model",
        "title": "LinkML Data Dictionary Model",
        "name": "data-dictionary",
        "license": "https://creativecommons.org/licenses/by-nc/4.0/",
        "version": "0.0.1",
        "prefixes": {
            "linkml": "https://w3id.org/linkml/",
            "ncit": "https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=",
            "pcdc": "https://w3id.org/pcdc/model",
            "HGNC": "https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:",
            "SO": "http://www.sequenceontology.org/browser/current_release/term/SO:",
            "icdo": "https://www.who.int/standards/classifications/other-classifications/international-classification-of-diseases-for-oncology/",
        },
        "default_curi_maps": [
            "semweb_context",
        ],
        "default_range": "string",
        "imports": "linkml:types",
        "subsets": {},
        "classes": {
            "Thing": {"abstract": True, "slots": ["submitter_id", "type"]},
        },
        "slots": {
            "submitter_id": {
                "description": "PCDC internal event ID",
                "required": True,
            },
            "type": {
                "description": "Default system-assigned property for each node",
                "required": True,
            },
            "subjects": {
                "multivalued": False,
                "range": "Subject",
                "required": True,
            },
            "time_periods": {"range": "Time Period", "required": False},
        },
        "enums": {},
    }
    return base_struct


def create_class(base_struct: Dict, classname: str, data: Dict) -> Dict:
    """
    Set up base structure from the template, and define anything
    that is not explicit in the incoming json data.

    Inputs:
        base_struct (dict): linkml template to start with
        classname (str): classname to be added
        data (dict): data associated with the given class

    Outputs:
        dictionary with new classes and slot, enum info added
    """
    base_struct["classes"][classname] = {
        "is_a": "Thing",
        "description": "",
        "slots": [],
        "slot_usage": {},
        "attributes": {},
    }

    # all classes take a slot for subjects except for this group
    non_subject_classes = ["Thing", "Person", "Subject"]

    # these keys in json should not be turned into slots, they are represented
    # through other objects and self referencing
    unused_slots = ["protocol", "submitter_id", "parent_submitter_id"]

    for key in data.keys():
        slot_name = key.lower()
        valid_slot_name = True

        # Check that the name is valid and does not contain strange characters (like ? or %)
        for char in disallowed_vals_in_name:
            if char in slot_name:
                valid_slot_name = False
        if (
            slot_name not in base_struct["slots"].keys()
            and slot_name not in unused_slots
            and slot_name != "time_period_submitter_id"
            and valid_slot_name
        ):
            new_slot = create_slot(base_struct, slot_name, data[key])
            base_struct["slots"][slot_name] = new_slot
        elif slot_name == "time_period_submitter_id":
            slot_name = "time_periods"
        if slot_name not in unused_slots and valid_slot_name:
            base_struct["classes"][classname]["slots"].append(slot_name)

    # Need to manually add subjects slot for fmh and timing
    if classname == "Time Period":
        base_struct["classes"][classname]["slots"].append("time_periods")

    if classname not in non_subject_classes:
        base_struct["classes"][classname]["slots"].append("subjects")

    return base_struct


def create_slot(base_struct: Dict, slot_name: str, slot_data: Dict) -> Dict:
    """
    Creates a slot if there and formats associated data.
    Creates or uses existing enum if non-default data type is needed.

    Inputs:
        base_struct (dict): running template
        slot_name (str): initial class-specific slot name (from json)
        slot_data (dict): data associated with the slot (with permissible values)

    Outputs:
        slot_dict (dict): information associated with the new slot
    """
    new_slot_dict = {}
    if "permissible_values" in slot_data.keys():
        enum_start = "".join(el.title() for el in slot_name.split("_"))
        enum_name = f"{enum_start}Enum"
        new_enum_name = create_enum(
            base_struct, enum_name, slot_data["permissible_values"]
        )
        new_slot_dict["range"] = new_enum_name
    else:
        if slot_data["type"].lower() != "string":
            new_slot_dict["range"] = slot_data["type"].lower()
    new_slot_dict["description"] = slot_data["description"]
    return new_slot_dict


def create_enum(
    base_struct: Dict, enum_name: str, permissible_values: Dict
) -> str:
    """
    Creates an enum that uses the permissible values and associates the code and description.
    Makes sure that there are not other existing enums with the same permissible values.
    If there are, then make sure there is an enum with a generalized name that can be
    used across classes and slots that refer to the same values and rename any existing slots
    that have class-specific enum naming schemes.

    Inputs:
        base_struct (dict): linkml struct to add to
        enum_name (str): initial enum name to assign
        permissible_values (dict): unique values associated with the enum

    Outputs:
        enum_name (str): old enum name or new one if enum name was reassigned
    """
    enum_dict = {"permissible_values": {}}
    if enum_name in base_struct["enums"].keys():
        # an enum already exists with the same name, make sure that it has the same values
        existing_enum = base_struct["enums"][enum_name][
            "permissible_values"
        ].keys()
        diff = list(
            set(existing_enum).symmetric_difference(
                set(permissible_values.keys())
            )
        )
        if len(diff) > 0:
            raise (
                ValueError,
                f"you have two value ranges with different values but the same variable name: {enum_name}",
            )
        else:
            return enum_name

    else:
        # check if enum already exists with same permissible_values
        match_exists, new_name = compare_enum_vals(
            base_struct, permissible_values, enum_name
        )
        if not match_exists:
            enum_dict = parse_description_and_meaning(
                enum_dict, permissible_values
            )
            base_struct["enums"][enum_name] = enum_dict
            return enum_name
        else:
            return new_name


def parse_description_and_meaning(enum_dict, permissible_values):
    for key in permissible_values.keys():
        desc = permissible_values[key]["description"]
        # TODO need to figure out how LINKML handles multiple codes
        # in the meaning section, doesnt seem to want to handle a group when converting to python
        # for now take the first ncit code if present, otherwise take the first code
        meaning = permissible_values[key]["codes"].split("|")
        if len(meaning) == 0:
            meaning = ""
        elif len(meaning) == 1:
            meaning = meaning[0]
        else:  # multiple codes, pick first ncit otherwise
            selected_code = meaning[0]
            for opt in meaning:
                if opt[0:4] == "ncit":
                    selected_code = opt
                    break
            meaning = selected_code

        # need to handle case of typo in ncit/nict
        if len(meaning) > 4:
            if meaning[0:4] == "nict":
                meaning = "ncit" + meaning[4:]
        if desc == "" and meaning == "":
            continue
        elif meaning == "":
            enum_dict["permissible_values"][str(key)] = {"description": desc}
        elif desc == "":
            enum_dict["permissible_values"][str(key)] = {
                "meaning": meaning,
            }
        else:
            enum_dict["permissible_values"][str(key)] = {
                "description": desc,
                "meaning": meaning,
            }
    return enum_dict


def compare_enum_vals(
    base_struct: Dict, permissible_values: Dict, enum_name: str
) -> Tuple[bool, str]:
    """
    Compare the existing enums to make sure that others don't
    already exist with the same permissible values, if they do,
    create a new name for the enum so it is not class specific.
    If it is renamed, for now it makes a new name by concatenating all
    of the permissible values together and truncates it so that erros will
    not arise when generating Python classes from the names.

    Inputs:
        base_struct (dict): base linkml template to add to and check from
        permissible_values (dict): set of values to be added
        enum_name (str): currrent class-specific enum name

    Outputs:
        found_match (bool): whethere an enum with matching values was found
        enum_name (str): old enum name or new one if enum name was reassigned
    """
    found = False
    comparison_values = set(permissible_values.keys())
    iterkeys = list(base_struct["enums"].keys())
    for enum in iterkeys:
        existing_enum = set(
            base_struct["enums"][enum]["permissible_values"].keys()
        )
        if len(existing_enum) == len(comparison_values):
            diff = list(existing_enum.symmetric_difference(comparison_values))
            if (
                len(diff) == 0
            ):  # there are no differences between an existing enum and the new one, rename and re-refrence
                sorted_vals = sorted(comparison_values)
                for dis in disallowed_vals_in_name:
                    if dis in sorted_vals:
                        sorted_vals.pop(sorted_vals.index(dis))
                # crop to 100 characters so the name doesn't get too long
                new_enum_name = (
                    "".join("".join(el.split()).title() for el in sorted_vals)[
                        :100
                    ]
                    + "Enum"
                )
                reassign = base_struct["enums"].pop(enum)
                base_struct["enums"][new_enum_name] = reassign

                slot_keys = list(base_struct["slots"].keys())
                for slot in slot_keys:
                    if "range" in base_struct["slots"][slot]:
                        if base_struct["slots"][slot]["range"] == enum:
                            base_struct["slots"][slot]["range"] = new_enum_name
                            found = True
                enum_name = new_enum_name
    return found, enum_name


if __name__ == "__main__":
    load_from_json()
