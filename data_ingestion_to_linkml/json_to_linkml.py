import copy
import json
import yaml
from typing import Dict

disallowed_vals_in_name = ["%", "?"]


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
    # all other keys (ex. under protocol, demographics, testing, disease_attributes ...)

    data_class_mapping = {
        "Person": person,
        "FamilyMedicalHistory": family_medical_history,
        "Subject": subject,
        "Timing": timing,
    }

    # todo probably can automate FMH
    manually_named = [
        "subject_charcteristics",
        "disease_phase_timing",
        "course_timing",
        "demographics",
        "family_medical_history",
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
            "hgnc": "https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=",
            "so": "https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=",
        },  # need to figure out correct links for hgnc and so
        "default_curi_maps": [
            "semweb_context",
        ],
        "default_range": "string",
        "imports": "linkml:types",
        "subsets": {},  # subsets onward are filled in from parsing the json
        "classes": {
            "Thing": {"abstract": True, "slots": ["submitter_id", "type"]},
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
            "timings": {"range": "Timing", "required": False},
        },
        "enums": {},
    }
    return base_struct


def create_class(base_struct: Dict, classname: str, data):
    base_struct["classes"][classname] = {
        "is_a": "Thing",
        "description": "",
        "slots": [],
        "slot_usage": {},
        "attributes": {},
    }
    timing_slot_mapping = [
        "disease_phase",
        "disease_phase_number",
        "course",
        "course_number",
        "age_at_disease_phase",
        "year_at_disease_phase",
        "age_at_course_start",
        "age_at_course_end",
        "age_at_tx_assign",
        "age_at_course_anc_500",
        "cycle_number",
        "age_at_cycle_start",
        "age_at_cycle_end",
    ]
    for key in data.keys():
        slot_name = key.lower()
        valid_slot_name = True

        # Check that the name is valid and does not contain strange characters (like ? or %)
        for char in disallowed_vals_in_name:
            if char in slot_name:
                valid_slot_name = False
        if (
            slot_name not in base_struct["slots"].keys()
            and slot_name != "protocol"
            and (slot_name not in timing_slot_mapping or classname == "Timing")
            and valid_slot_name
        ):
            new_slot = create_slot(base_struct, slot_name, data[key])
            base_struct["slots"][slot_name] = new_slot
        elif slot_name in timing_slot_mapping and classname != "Timing":
            if "timings" not in base_struct["classes"][classname]["slots"]:
                base_struct["classes"][classname]["slots"].append("timings")
        if slot_name != "protocol" and valid_slot_name:
            base_struct["classes"][classname]["slots"].append(slot_name)
    # Need to manually add subjects slot for fmh and timing
    if classname == "FamilyMedicalHistory" or classname == "Timing":
        base_struct["classes"][classname]["slots"].append("subjects")
        if classname == "Timing":
            base_struct["classes"][classname]["slots"].append("timings")

    return base_struct


def create_slot(base_struct: Dict, slot_name: str, slot_data: Dict) -> Dict:
    new_slot_dict = {}
    if "permissible_values" in slot_data.keys():
        enum_start = "".join(el.title() for el in slot_name.split("_"))
        enum_name = f"{enum_start}Enum"
        new_enum_name = create_enum(
            base_struct, enum_name, slot_data["permissible_values"]
        )

        # TODO check if permissible values match and change enum name if they don't
        # match use common name if they do match (parse together permissible
        # values and rename, and update any references that type of enum)
        new_slot_dict["range"] = new_enum_name
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
            return enum_name

    else:
        # check if enum already exists with same permissible_values:
        match_exists, new_name = compare_enum_vals(
            base_struct, permissible_values, enum_name
        )
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
            return enum_name
        else:
            return new_name


def compare_enum_vals(base_struct: Dict, permissible_values: Dict, enum_name) -> bool:

    found = False
    comparison_values = set(permissible_values.keys())
    iterkeys = list(base_struct["enums"].keys())
    for enum in iterkeys:
        existing_enum = set(base_struct["enums"][enum]["permissible_values"].keys())
        if len(existing_enum) == len(comparison_values):
            diff = list(existing_enum.symmetric_difference(comparison_values))
            if (
                len(diff) == 0
            ):  # there are no differences between an existing enum and the new one, rename and re-refrence
                sorted_vals = sorted(comparison_values)
                for dis in disallowed_vals_in_name:
                    if dis in sorted_vals:
                        sorted_vals.pop(sorted_vals.index(dis))
                new_enum_name = (
                    "".join("".join(el.split()).title() for el in sorted_vals)[:100]
                    + "Enum"
                )  # crop to 100 characters so the name doesn't get too long
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
