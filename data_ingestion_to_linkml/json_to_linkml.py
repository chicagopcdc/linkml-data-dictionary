import copy
import json
import yaml
from typing import Dict


def load_from_json():
    # todo get automated connection to github setup to pull json automatically
    f = open("data_ingestion_to_linkml/test_json_data/master.json")
    data = json.load(f)
    f.close()

    python_linkml_struct = get_base_linkml_struct()

    """
    Pull subject characteristics and timings out of data['domains']['protocol']
    Pull person out of data['demographics']['demographics']
    TBD on where to get Family Medical History from 
    """
    subject = data["domains"]["protocol"]["subject_characteristics"]
    timing = {
        **data["domains"]["protocol"]["disease_phase_timing"],
        **data["domains"]["protocol"]["course_timing"],
    }
    person = data["domains"]["demographics"]["demographics"]
    family_medical_history = data["domains"]["demographics"]["family_medical_history"]

    data_class_mapping = {
        "Person": person,
        "FamilyMedicalHistory": family_medical_history,
        "Subject": subject,
        "Timing": timing,
    }

    for key in data_class_mapping.keys():
        python_linkml_struct = create_class(
            python_linkml_struct, key, data_class_mapping[key]
        )
        if key == "Subject":
            python_linkml_struct["classes"]["Subject"]["attributes"]["persons"] = {
                "range": "Person",
                "required": True,
            }

    # will need to check that same version doesn't already exist before writing
    write_filename = f"data_ingestion_to_linkml/output_linkml_yaml/data_dictionary_spreadsheet_{data['meta']['spreadsheet_id']}.yaml"
    with open(write_filename, "w") as f:
        data = yaml.dump(python_linkml_struct, f, sort_keys=False)


def get_base_linkml_struct():
    """
    Establish the baseline python dictionary that contains the constant linkml
    attributes that will not change from version to version of data dictionaries.
    """
    # TODO: figure out a versioning scheme so everything isn't 0.0.1
    base_class = {
        "is_a": "Thing",
        "description": "",
        "slots": [],
        "slot_usage": {},
        "attributes": {},
    }
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
        },
        "default_curi_maps": [
            "semweb_context",
        ],
        "default_range": "string",
        "imports": "linkml:types",
        "subsets": {},  # subsets onward are filled in from parsing the json
        "classes": {
            "Thing": {"abstract": True, "slots": ["submitter_id", "type"]},
            "Person": copy.deepcopy(base_class),
            "FamilyMedicalHistory": copy.deepcopy(base_class),
            "Subject": copy.deepcopy(base_class),
            "Timing": copy.deepcopy(base_class),
        },
        "slots": {
            "submitter_id": {"description": "PCDC internal event ID", "required": True},
            "type": {
                "description": "Default system-assigned property for each node",
                "required": True,
            },
            "subjects": {
                "multivalued": True,
                "range": "Subject",
                "required": True,
            },
        },
        "enums": {},
    }
    return base_struct


def create_class(base_struct: Dict, classname: str, data):
    for key in data.keys():
        slot_name = key.lower()
        if slot_name not in base_struct["slots"].keys() and slot_name != "protocol":
            new_slot = create_slot(base_struct, slot_name, data[key])
            base_struct["slots"][slot_name] = new_slot
        if (
            slot_name != "protocol"
        ):  # TODO create a list of slotnames we don't want to include if there are others
            base_struct["classes"][classname]["slots"].append(slot_name)
    # Need to manually add subjects slot for fmh and timing
    if classname == "FamilyMedicalHistory" or classname == "Timing":
        base_struct["classes"][classname]["slots"].append("subjects")
    return base_struct


def create_slot(base_struct: Dict, slot_name: str, slot_data: Dict) -> Dict:
    new_slot_dict = {}
    if "permissible_values" in slot_data.keys():
        enum_start = "".join(el.title() for el in slot_name.split("_"))
        enum_name = f"{enum_start}Enum"
        create_enum(base_struct, enum_name, slot_data["permissible_values"])

        # TODO check if permissible values match and change enum name if they don't
        # match use common name if they do match (parse together permissible
        # values and rename, and update any references that type of enum)
        new_slot_dict["range"] = enum_name
    else:
        if slot_data["data_type"].lower() != "string":
            new_slot_dict["range"] = slot_data["data_type"].lower()
    new_slot_dict["description"] = slot_data["variable_description"]
    return new_slot_dict


def create_enum(base_struct: Dict, enum_name: str, permissible_values: Dict):
    enum_dict = {"permissible_values": {}}
    if enum_name in base_struct["enums"].keys():
        # an enum already exists with the same name, make sure that they contain the same values
        existing_enum = base_struct["enums"][enum_name]["permissible_values"].keys()
        diff = list(
            set(existing_enum).symmetric_difference(set(permissible_values.keys()))
        )
        if len(diff) > 0:
            raise (
                ValueError,
                f"you have two value ranges with different values but the same variable name: {enum_name}",
            )
        else:
            return

    else:
        # check if enum already exists with same permissible_values:
        match_exists = compare_enum_vals(base_struct, permissible_values)
        if not match_exists:
            for key in permissible_values.keys():
                desc = permissible_values[key]["value_description"]
                meaning = permissible_values[key]["value_code"][0]
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
            base_struct["enums"][enum_name] = enum_dict


def compare_enum_vals(base_struct: Dict, permissible_values: Dict) -> bool:
    comparison_values = set(permissible_values.keys())
    for enum in base_struct["enums"].keys():
        existing_enum = set(base_struct["enums"][enum]["permissible_values"].keys())
        if len(existing_enum) == len(comparison_values):
            diff = list(existing_enum.symmetric_difference(comparison_values))
            if (
                len(diff) == 0
            ):  # there are no differences between an existing enum and the new one, rename and re-refrence
                new_enum_name = (
                    "".join(
                        "".join(el.split()).title() for el in sorted(comparison_values)
                    )
                    + "Enum"
                )
                reassign = base_struct["enums"].pop(enum)
                base_struct[new_enum_name] = reassign
                for slot in base_struct["slots"].keys():
                    if base_struct["slots"][slot]["range"] == enum:
                        base_struct["slots"][slot]["range"] == new_enum_name
                return True
    return False


if __name__ == "__main__":
    load_from_json()
