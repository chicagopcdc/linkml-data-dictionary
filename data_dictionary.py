# Auto generated from data_dictionary.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-12-14T12:45:01
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
EX = CurieNamespace('ex', 'https://example.org/linkml/hello-world/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NCIT = CurieNamespace('ncit', 'https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=')
SCHEMA = CurieNamespace('schema', 'https://schema.org/')
DEFAULT_ = EX


# Types

# Class references



@dataclass
class Demographic(YAMLRoot):
    """
    demographic information about an individual
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Demographic
    class_class_curie: ClassVar[str] = "schema:Demographic"
    class_name: ClassVar[str] = "Demographic"
    class_model_uri: ClassVar[URIRef] = EX.Demographic

    sex: Union[str, "SexEnum"] = None
    race: Union[str, "RaceEnum"] = None
    ethnicity: Union[str, "EthnicityEnum"] = None
    race_other: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sex):
            self.MissingRequiredField("sex")
        if not isinstance(self.sex, SexEnum):
            self.sex = SexEnum(self.sex)

        if self._is_empty(self.race):
            self.MissingRequiredField("race")
        if not isinstance(self.race, RaceEnum):
            self.race = RaceEnum(self.race)

        if self._is_empty(self.ethnicity):
            self.MissingRequiredField("ethnicity")
        if not isinstance(self.ethnicity, EthnicityEnum):
            self.ethnicity = EthnicityEnum(self.ethnicity)

        if self.race_other is not None and not isinstance(self.race_other, str):
            self.race_other = str(self.race_other)

        super().__post_init__(**kwargs)


# Enumerations
class SexEnum(EnumDefinitionImpl):

    MALE = PermissibleValue(text="MALE",
                               description="A person who belongs to the sex that normally produces sperm. The term is used to indicate biological sex distinctions, cultural gender role distinctions, or both.",
                               meaning=NCIT.C20197)
    FEMALE = PermissibleValue(text="FEMALE",
                                   description="A person who belongs to the sex that normally produces ova. The term is used to indicate biological sex distinctions, or cultural gender role distinctions, or both.",
                                   meaning=NCIT.C16576)
    UNDIFFERENTIATED = PermissibleValue(text="UNDIFFERENTIATED",
                                                       description="Sex could not be determined; not uniquely defined; undifferentiated.",
                                                       meaning=NCIT.C41438)
    UNKNOWN = PermissibleValue(text="UNKNOWN",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)
    NOT_REPORTED = PermissibleValue(text="NOT_REPORTED",
                                               description="Not provided or available.",
                                               meaning=NCIT.C43234)

    _defn = EnumDefinition(
        name="SexEnum",
    )

class RaceEnum(EnumDefinitionImpl):

    AMERICAN_INDIAN_OR_ALASKA_NATIVE = PermissibleValue(text="AMERICAN_INDIAN_OR_ALASKA_NATIVE",
                                                                                       description="A person having origins in any of the original peoples of North and South America (including Central America) and who maintains tribal affiliation or community attachment. (OMB)",
                                                                                       meaning=NCIT.C41259)
    ASIAN = PermissibleValue(text="ASIAN",
                                 description="A person having origins in any of the original peoples of the Far East, Southeast Asia, or the Indian subcontinent, including for example, Cambodia, China, India, Japan, Korea, Malaysia, Pakistan, the Philippine Islands, Thailand, and Vietnam. (OMB)",
                                 meaning=NCIT.C41260)
    BLACK_OR_AFRICAN_AMERICAN = PermissibleValue(text="BLACK_OR_AFRICAN_AMERICAN",
                                                                         description="A person having origins in any of the Black racial groups of Africa. Terms such as "Haitian" or "Negro" can be used in addition to "Black or African American". (OMB)",
                                                                         meaning=NCIT.C16352)
    MULTIRACIAL = PermissibleValue(text="MULTIRACIAL",
                                             description="Having ancestors of several or various races.",
                                             meaning=NCIT.C67109)
    NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER = PermissibleValue(text="NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER",
                                                                                                         description="A person having origins in any of the original peoples of Hawaii, Guam, Samoa, or other Pacific Islands. (OMB)",
                                                                                                         meaning=NCIT.C41219)
    WHITE = PermissibleValue(text="WHITE",
                                 description="A person having origins in any of the original peoples of Europe, the Middle East, or North Africa. (OMB)",
                                 meaning=NCIT.C41261)
    OTHER = PermissibleValue(text="OTHER",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    UNKNOWN = PermissibleValue(text="UNKNOWN",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)
    NOT_REPORTED = PermissibleValue(text="NOT_REPORTED",
                                               description="Not provided or available.",
                                               meaning=NCIT.C43234)

    _defn = EnumDefinition(
        name="RaceEnum",
    )

class EthnicityEnum(EnumDefinitionImpl):

    HISPANIC_OR_LATINO = PermissibleValue(text="HISPANIC_OR_LATINO",
                                                           description="A person of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin, regardless of race. The term, "Spanish origin," can be used in addition to "Hispanic or Latino." (OMB)",
                                                           meaning=NCIT.C17459)
    NOT_HISPANIC_OR_LATINO = PermissibleValue(text="NOT_HISPANIC_OR_LATINO",
                                                                   description="A person not of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin, regardless of race.",
                                                                   meaning=NCIT.C41222)
    UNKNOWN = PermissibleValue(text="UNKNOWN",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)
    NOT_REPORTED = PermissibleValue(text="NOT_REPORTED",
                                               description="Not provided or available.",
                                               meaning=NCIT.C43234)

    _defn = EnumDefinition(
        name="EthnicityEnum",
    )

# Slots
class slots:
    pass

slots.sex = Slot(uri=EX.sex, name="sex", curie=EX.curie('sex'),
                   model_uri=EX.sex, domain=None, range=Union[str, "SexEnum"])

slots.race = Slot(uri=EX.race, name="race", curie=EX.curie('race'),
                   model_uri=EX.race, domain=None, range=Union[str, "RaceEnum"])

slots.race_other = Slot(uri=EX.race_other, name="race_other", curie=EX.curie('race_other'),
                   model_uri=EX.race_other, domain=None, range=Optional[str])

slots.ethnicity = Slot(uri=EX.ethnicity, name="ethnicity", curie=EX.curie('ethnicity'),
                   model_uri=EX.ethnicity, domain=None, range=Union[str, "EthnicityEnum"])
