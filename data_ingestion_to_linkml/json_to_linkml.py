import copy
import json
import yaml


def load_from_json():
    # todo get automated connection to github setup to pull json automatically
    f = open("data_ingestion_to_linkml/test_json_data/ALL.json")
    data = json.load(f)
    f.close()

    python_linkml_struct = get_base_linkml_struct()
    write_filename = f"data_ingestion_to_linkml/output_linkml_yaml/data_dictionary_spreadsheet_{data['meta']['spreadsheet_id']}.yaml"

    """
    Pull subject characteristics and timings out of data['domains']['protocol']
    """
    subject = data["domains"]["protocol"]

    # is it ok to version thee data_dictionaries by spreadsheet id,
    # will need to check that same version doesn't already exist before writing

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
        "class_uri": "",
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
        "default_curi_maps": ["semweb_context"],
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
        },
        "enums": {},
        # check if permissible values match and change enum name if they don't match
        # use common name if they do match (parse together permissible values and rename,
        # update references that enum)
    }
    return base_struct


if __name__ == "__main__":
    load_from_json()
