# Auto generated from data_dictionary_spreadsheet_1sTygI0GtyaT2C0iZ9YzXTKRnAcELuV2BblaLGPG0EPc.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-01-31T14:49:46
# Schema: data-dictionary
#
# id: https://w3id.org/pcdc/model
# description:
# license: https://creativecommons.org/licenses/by-nc/4.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = "0.0.1"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NCIT = CurieNamespace('ncit', 'https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=')
PCDC = CurieNamespace('pcdc', 'https://w3id.org/pcdc/model')
DEFAULT_ = CurieNamespace('', 'https://w3id.org/pcdc/model/')


# Types

# Class references



@dataclass
class NamedThing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/NamedThing"]
    class_class_curie: ClassVar[str] = "pcdc:/NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/NamedThing")

    submitter_id: str = None
    type: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.submitter_id):
            self.MissingRequiredField("submitter_id")
        if not isinstance(self.submitter_id, str):
            self.submitter_id = str(self.submitter_id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


class Person(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/Person"]
    class_class_curie: ClassVar[str] = "pcdc:/Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/Person")


class FamilyMedicalHistory(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/FamilyMedicalHistory"]
    class_class_curie: ClassVar[str] = "pcdc:/FamilyMedicalHistory"
    class_name: ClassVar[str] = "FamilyMedicalHistory"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/FamilyMedicalHistory")


class Subject(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/Subject"]
    class_class_curie: ClassVar[str] = "pcdc:/Subject"
    class_name: ClassVar[str] = "Subject"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/Subject")


class Timing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/Timing"]
    class_class_curie: ClassVar[str] = "pcdc:/Timing"
    class_name: ClassVar[str] = "Timing"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/Timing")


# Enumerations


# Slots
class slots:
    pass

slots.submitter_id = Slot(uri=DEFAULT_.submitter_id, name="submitter_id", curie=DEFAULT_.curie('submitter_id'),
                   model_uri=DEFAULT_.submitter_id, domain=None, range=str)

slots.type = Slot(uri=DEFAULT_.type, name="type", curie=DEFAULT_.curie('type'),
                   model_uri=DEFAULT_.type, domain=None, range=str)
