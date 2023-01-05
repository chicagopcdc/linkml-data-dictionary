# Auto generated from data_dictionary.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-01-05T10:52:11
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
from linkml_runtime.linkml_model.types import Integer, String

metamodel_version = "1.7.0"
version = "0.0.1"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
EX = CurieNamespace('ex', 'https://example.org/linkml/hello-world/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NCIT = CurieNamespace('ncit', 'https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=')
SCHEMA = CurieNamespace('schema', 'https://schema.org/')
DEFAULT_ = CurieNamespace('', 'https://w3id.org/pcdc/model/')


# Types

# Class references
class SubjectsHonestBrokerSubjectId(extended_str):
    pass


@dataclass
class Demographic(YAMLRoot):
    """
    demographic information about an individual
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Demographic
    class_class_curie: ClassVar[str] = "schema:Demographic"
    class_name: ClassVar[str] = "Demographic"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/Demographic")

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


@dataclass
class FamilyMedicalHistory(YAMLRoot):
    """
    prior cancer information of a first-degree relative
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.FamilyMedicalHistory
    class_class_curie: ClassVar[str] = "schema:FamilyMedicalHistory"
    class_name: ClassVar[str] = "FamilyMedicalHistory"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/FamilyMedicalHistory")

    prior_cancer: Union[str, "YesNoUnknownNotReportedEnum"] = None
    relation: Optional[Union[str, "RelationEnum"]] = None
    prior_cancer_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.prior_cancer):
            self.MissingRequiredField("prior_cancer")
        if not isinstance(self.prior_cancer, YesNoUnknownNotReportedEnum):
            self.prior_cancer = YesNoUnknownNotReportedEnum(self.prior_cancer)

        if self.relation is not None and not isinstance(self.relation, RelationEnum):
            self.relation = RelationEnum(self.relation)

        if self.prior_cancer_type is not None and not isinstance(self.prior_cancer_type, str):
            self.prior_cancer_type = str(self.prior_cancer_type)

        super().__post_init__(**kwargs)


@dataclass
class Subjects(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Subjects
    class_class_curie: ClassVar[str] = "schema:Subjects"
    class_name: ClassVar[str] = "Subjects"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/Subjects")

    honest_broker_subject_id: Union[str, SubjectsHonestBrokerSubjectId] = None
    consortium: Optional[Union[str, "ConsortiumEnum"]] = None
    data_contributor_id: Optional[Union[str, "DataContributorIdEnum"]] = None
    study_id: Optional[Union[str, "StudyIdEnum"]] = None
    age_at_enrollment: Optional[int] = None
    year_at_enrollment: Optional[int] = None
    treatment_arm: Optional[Union[str, "TreatmentArmEnum"]] = None
    enrolled_status: Optional[Union[str, "EnrolledStatusEnum"]] = None
    efs_censor_status: Optional[Union[str, "CensorStatusEnum"]] = None
    age_at_censor_status: Optional[int] = None
    data_source: Optional[Union[str, "DataSourceEnum"]] = None
    randomized_status: Optional[Union[str, "RandomizedStatusEnum"]] = None
    study_phase: Optional[Union[str, "StudyPhaseEnum"]] = None
    study_type: Optional[Union[str, "StudyTypeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.honest_broker_subject_id):
            self.MissingRequiredField("honest_broker_subject_id")
        if not isinstance(self.honest_broker_subject_id, SubjectsHonestBrokerSubjectId):
            self.honest_broker_subject_id = SubjectsHonestBrokerSubjectId(self.honest_broker_subject_id)

        if self.consortium is not None and not isinstance(self.consortium, ConsortiumEnum):
            self.consortium = ConsortiumEnum(self.consortium)

        if self.data_contributor_id is not None and not isinstance(self.data_contributor_id, DataContributorIdEnum):
            self.data_contributor_id = DataContributorIdEnum(self.data_contributor_id)

        if self.study_id is not None and not isinstance(self.study_id, StudyIdEnum):
            self.study_id = StudyIdEnum(self.study_id)

        if self.age_at_enrollment is not None and not isinstance(self.age_at_enrollment, int):
            self.age_at_enrollment = int(self.age_at_enrollment)

        if self.year_at_enrollment is not None and not isinstance(self.year_at_enrollment, int):
            self.year_at_enrollment = int(self.year_at_enrollment)

        if self.treatment_arm is not None and not isinstance(self.treatment_arm, TreatmentArmEnum):
            self.treatment_arm = TreatmentArmEnum(self.treatment_arm)

        if self.enrolled_status is not None and not isinstance(self.enrolled_status, EnrolledStatusEnum):
            self.enrolled_status = EnrolledStatusEnum(self.enrolled_status)

        if self.efs_censor_status is not None and not isinstance(self.efs_censor_status, CensorStatusEnum):
            self.efs_censor_status = CensorStatusEnum(self.efs_censor_status)

        if self.age_at_censor_status is not None and not isinstance(self.age_at_censor_status, int):
            self.age_at_censor_status = int(self.age_at_censor_status)

        if self.data_source is not None and not isinstance(self.data_source, DataSourceEnum):
            self.data_source = DataSourceEnum(self.data_source)

        if self.randomized_status is not None and not isinstance(self.randomized_status, RandomizedStatusEnum):
            self.randomized_status = RandomizedStatusEnum(self.randomized_status)

        if self.study_phase is not None and not isinstance(self.study_phase, StudyPhaseEnum):
            self.study_phase = StudyPhaseEnum(self.study_phase)

        if self.study_type is not None and not isinstance(self.study_type, StudyTypeEnum):
            self.study_type = StudyTypeEnum(self.study_type)

        super().__post_init__(**kwargs)


# Enumerations
class SexEnum(EnumDefinitionImpl):

    Male = PermissibleValue(text="Male",
                               description="A person who belongs to the sex that normally produces sperm. The term is used to indicate biological sex distinctions, cultural gender role distinctions, or both.",
                               meaning=NCIT.C20197)
    Female = PermissibleValue(text="Female",
                                   description="A person who belongs to the sex that normally produces ova. The term is used to indicate biological sex distinctions, or cultural gender role distinctions, or both.",
                                   meaning=NCIT.C16576)
    Undifferentiated = PermissibleValue(text="Undifferentiated",
                                                       description="Sex could not be determined; not uniquely defined; undifferentiated.",
                                                       meaning=NCIT.C41438)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="SexEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class RaceEnum(EnumDefinitionImpl):

    Asian = PermissibleValue(text="Asian",
                                 description="A person having origins in any of the original peoples of the Far East, Southeast Asia, or the Indian subcontinent, including for example, Cambodia, China, India, Japan, Korea, Malaysia, Pakistan, the Philippine Islands, Thailand, and Vietnam. (OMB)",
                                 meaning=NCIT.C41260)
    Multiracial = PermissibleValue(text="Multiracial",
                                             description="Having ancestors of several or various races.",
                                             meaning=NCIT.C67109)
    White = PermissibleValue(text="White",
                                 description="A person having origins in any of the original peoples of Europe, the Middle East, or North Africa. (OMB)",
                                 meaning=NCIT.C41261)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="RaceEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "American Indian or Alaska Native",
                PermissibleValue(text="American Indian or Alaska Native",
                                 description="A person having origins in any of the original peoples of North and South America (including Central America) and who maintains tribal affiliation or community attachment. (OMB)",
                                 meaning=NCIT.C41259) )
        setattr(cls, "Black or African American",
                PermissibleValue(text="Black or African American",
                                 description="A person having origins in any of the Black racial groups of Africa. Terms such as "Haitian" or "Negro" can be used in addition to "Black or African American". (OMB)",
                                 meaning=NCIT.C16352) )
        setattr(cls, "Native Hawaiian or Other Pacific Islander",
                PermissibleValue(text="Native Hawaiian or Other Pacific Islander",
                                 description="A person having origins in any of the original peoples of Hawaii, Guam, Samoa, or other Pacific Islands. (OMB)",
                                 meaning=NCIT.C41219) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class EthnicityEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="EthnicityEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Hispanic or Latino",
                PermissibleValue(text="Hispanic or Latino",
                                 description="A person of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin, regardless of race. The term, "Spanish origin," can be used in addition to "Hispanic or Latino." (OMB)",
                                 meaning=NCIT.C17459) )
        setattr(cls, "Not Hispanic or Latino",
                PermissibleValue(text="Not Hispanic or Latino",
                                 description="A person not of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin, regardless of race.",
                                 meaning=NCIT.C41222) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class YesNoUnknownNotReportedEnum(EnumDefinitionImpl):

    Yes = PermissibleValue(text="Yes",
                             description="The affirmative response to a question.",
                             meaning=NCIT.C49488)
    No = PermissibleValue(text="No",
                           description="The non-affirmative response to a question.",
                           meaning=NCIT.C49487)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="YesNoUnknownNotReportedEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class RelationEnum(EnumDefinitionImpl):

    Father = PermissibleValue(text="Father",
                                   description="A male who contributes to the genetic makeup of his offspring through the fertilization of an ovum by his sperm.",
                                   meaning=NCIT.C96572)
    Mother = PermissibleValue(text="Mother",
                                   description="A female who contributes to the genetic makeup of her offspring from the fertilization of her ovum.",
                                   meaning=NCIT.C96580)
    Brother = PermissibleValue(text="Brother",
                                     description="A male who shares with his sibling the genetic makeup inherited from one or both of their shared biological parents.",
                                     meaning=NCIT.C96570)
    Sister = PermissibleValue(text="Sister",
                                   description="A female who shares with her sibling the genetic makeup inherited from one or both of their shared biological parents.",
                                   meaning=NCIT.C96586)
    Son = PermissibleValue(text="Son",
                             description="A male progeny with genetic makeup inherited from the parent.",
                             meaning=NCIT.C150888)
    Daughter = PermissibleValue(text="Daughter",
                                       description="A female progeny with genetic makeup inherited from the parent.",
                                       meaning=NCIT.C150887)

    _defn = EnumDefinition(
        name="RelationEnum",
    )

class ConsortiumEnum(EnumDefinitionImpl):

    INSTRuCT = PermissibleValue(text="INSTRuCT",
                                       description="International Soft Tissue Sarcoma Consortium (INSTRuCT)")
    MaGIC = PermissibleValue(text="MaGIC",
                                 description="Malignant Germ Cell International Consortium (MaGIC)")
    INRG = PermissibleValue(text="INRG",
                               description="International Neuroblastoma Risk Group (INRG)")
    NODAL = PermissibleValue(text="NODAL",
                                 description="Hodgkin Lymphoma Data Collaboration (NODAL)")
    INTERACT = PermissibleValue(text="INTERACT",
                                       description="International Pediatric Acute Myeloid Leukemia Consortium (INTERACT)")
    HIBiSCus = PermissibleValue(text="HIBiSCus",
                                       description="Harmonization International Bone Sarcoma Consortium (HIBiSCus)")
    INSPiRE = PermissibleValue(text="INSPiRE",
                                     description="International Central Nervous System Pediatric Research Consortium (INSPiRE)")
    C3P = PermissibleValue(text="C3P",
                             description="Consortium for Childhood Cancer Predisposition (C3P)")

    _defn = EnumDefinition(
        name="ConsortiumEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Global REACH",
                PermissibleValue(text="Global REACH",
                                 description="Global Retinoblastoma Alliance for Children (Global REACH)") )

class DataContributorIdEnum(EnumDefinitionImpl):

    AIEOP = PermissibleValue(text="AIEOP",
                                 description="Italian Association of Pediatric Hematology and Oncology is a group from Bologna, Italy, comprised mainly of pediatricians, hematologists, oncologists, surgeons, biologists, nurses and psychologists who are devoted to addressing the problems of hematology, oncology and immunology in the child and adolescent.",
                                 meaning=NCIT.C168887)
    COG = PermissibleValue(text="COG",
                             description="Children's Oncology Group. An NCI-supported clinical cooperative group formed by the merger of the four national pediatric cancer research organizations (the Children's Cancer Group, the Intergroup Rhabdomyosarcoma Study Group, the National Wilms Tumor Study Group, and the Pediatric Oncology Group. The primary objective of the organization is to conduct clinical trials of new therapies for childhood and adolescent cancer. COG develops and coordinates clinical trials conducted at the 238 member institutions that include cancer centers of all major universities and teaching hospitals throughout the U.S. and Canada, as well as sites in Europe and Australia. COG members include over 5000 cancer researchers.)",
                             meaning=NCIT.C39353)
    DCOG = PermissibleValue(text="DCOG",
                               description="A collaborating partner in Innovative Therapies for Children with Cancer Consortium (ITCC), a European based consortium to promote the clinical evaluation of new anti-cancer compounds in children with cancer.",
                               meaning=NCIT.C168889)
    MRC = PermissibleValue(text="MRC",
                             description="Medical Research Council. A publicly funded organization that is part of United Kingdom Research and Innovation, and is dedicated to improving human health through world-class medical research.",
                             meaning=NCIT.C168892)

    _defn = EnumDefinition(
        name="DataContributorIdEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "BFM-SG",
                PermissibleValue(text="BFM-SG",
                                 description="A study group formed in 1975 by three individuals, Hansjorg Riehm in Berlin (B), Bernhard Kornhuber in Frankfurt (F) and Gunther Schellong in Munster (M), who initiated the first multicenter BFM trial. The BFM treatment concept was based on an intensive chemotherapeutic approach employing eight different drugs which led to a revolutionary increase in the survival of children and adolescents with acute lymphoblastic leukemia.",
                                 meaning=NCIT.C168888) )

class StudyIdEnum(EnumDefinitionImpl):

    AAML03P1 = PermissibleValue(text="AAML03P1",
                                       meaning=NCIT.C168936)
    AAML0531 = PermissibleValue(text="AAML0531",
                                       meaning=NCIT.C168937)
    AAML1031 = PermissibleValue(text="AAML1031",
                                       meaning=NCIT.C168938)
    AMLBFM2004 = PermissibleValue(text="AMLBFM2004",
                                           meaning=NCIT.C168939)
    AMLBFM2012 = PermissibleValue(text="AMLBFM2012",
                                           meaning=NCIT.C173250)

    _defn = EnumDefinition(
        name="StudyIdEnum",
    )

class TreatmentArmEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="TreatmentArmEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "MAP-GR",
                PermissibleValue(text="MAP-GR",
                                 description="A control arm for patients receiving a regimen of methotrexate, doxorubicin and cisplatin (MAP) after good response to the MAP regimen pre-operatively.",
                                 meaning=NCIT.C186769) )
        setattr(cls, "MAP-IFN-GR",
                PermissibleValue(text="MAP-IFN-GR",
                                 description="An experimental treatment arm for patients receiving a regimen of methotrexate, doxorubicin and cisplatin (MAP) plus interferon (IFN) post-operatively after good response to the MAP regimen pre-operatively.",
                                 meaning=NCIT.C186770) )
        setattr(cls, "MAP-PR",
                PermissibleValue(text="MAP-PR",
                                 description="A control arm for patients receiving a regimen of methotrexate, doxorubicin and cisplatin (MAP) after poor response to the MAP regimen pre-operatively.",
                                 meaning=NCIT.C186771) )
        setattr(cls, "MAP-IE-PR",
                PermissibleValue(text="MAP-IE-PR",
                                 description="An experimental treatment arm for patients receiving a regimen of methotrexate, doxorubicin and cisplatin (MAP) plus a regimen of ifosfamide and etoposide (IE) post-operatively after poor response to the MAP regimen pre-operatively.",
                                 meaning=NCIT.C186772) )
        setattr(cls, "MAP-NR",
                PermissibleValue(text="MAP-NR",
                                 description="A control arm for patients receiving a regimen of methotrexate, doxorubicin and cisplatin (MAP) with no response.",
                                 meaning=NCIT.C186773) )

class EnrolledStatusEnum(EnumDefinitionImpl):

    Enrolled = PermissibleValue(text="Enrolled",
                                       description="The study subject is enrolled.",
                                       meaning=NCIT.C142715)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="EnrolledStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Enrolled",
                PermissibleValue(text="Not Enrolled",
                                 description="The study subject is not enrolled.",
                                 meaning=NCIT.C168929) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class CensorStatusEnum(EnumDefinitionImpl):

    Censored = PermissibleValue(text="Censored",
                                       description="Subject is censored (i.e. has had no events(s))")
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="CensorStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Censored",
                PermissibleValue(text="Not Censored",
                                 description="Subject has had one or more events") )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class DataSourceEnum(EnumDefinitionImpl):

    Registry = PermissibleValue(text="Registry",
                                       description="Cancer registries gather a wide variety of specific information on cancer patients that can be analyzed to identify health disparity trends in cancer incidence, mortality and patient survival.",
                                       meaning=NCIT.C15753)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="DataSourceEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Therapeutic Trial",
                PermissibleValue(text="Therapeutic Trial",
                                 description="A clinical study that involves administering of exposure to the agent/agents to subjects with particular disease to elucidate the most appropriate treatment for a specific medical condition, or to prolong or improve the patient's life.",
                                 meaning=NCIT.C39536) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class RandomizedStatusEnum(EnumDefinitionImpl):

    Randomized = PermissibleValue(text="Randomized",
                                           description="Assignment of subjects by chance to groups that receive different treatments.",
                                           meaning=NCIT.C15417)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="RandomizedStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Non-Randomized",
                PermissibleValue(text="Non-Randomized",
                                 description="A clinical trial in which participants may choose or be assigned into groups by researchers. Their assignment is not random.",
                                 meaning=NCIT.C93043) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class StudyPhaseEnum(EnumDefinitionImpl):

    Pilot = PermissibleValue(text="Pilot",
                                 description="The initial study examining a new method or treatment.",
                                 meaning=NCIT.C15303)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="StudyPhaseEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Phase 1",
                PermissibleValue(text="Phase 1",
                                 description="A clinical research protocol designed to test a new biomedical intervention in a small group of people for the first time. A Phase I trial can be to establish the toxicity of a new treatment with escalating intensity of the treatment administered and/or to determine the side effects of a new treatment for a particular indication in subjects.",
                                 meaning=NCIT.C15600) )
        setattr(cls, "Phase 2",
                PermissibleValue(text="Phase 2",
                                 description="A clinical research protocol designed to study a biomedical or behavioral intervention in a larger group of people (several hundred), to evaluate the drug's effectiveness for a particular indication in patients with the disease or condition under study, and to determine the common short-term side effects and risks associated with the intervention.",
                                 meaning=NCIT.C15601) )
        setattr(cls, "Phase 3",
                PermissibleValue(text="Phase 3",
                                 description="A clinical research protocol designed to investigate the efficacy of the biomedical or behavioral intervention in large groups of human subjects (from several hundred to several thousand), to confirm efficacy, to monitor adverse reactions to the new medication or treatment regimen with respect to long-term use and by comparing the intervention to other standard or experimental interventions as well as to a placebo.",
                                 meaning=NCIT.C15602) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class StudyTypeEnum(EnumDefinitionImpl):

    Frontline = PermissibleValue(text="Frontline",
                                         description="A clinical trial for previously untreated patients that studies the use of a first line of treatment.",
                                         meaning=NCIT.C185306)
    Retrieval = PermissibleValue(text="Retrieval",
                                         description="A trial to assess the efficacy of reinduction therapy.",
                                         meaning=NCIT.C185307)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="StudyTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

# Slots
class slots:
    pass

slots.sex = Slot(uri=DEFAULT_.sex, name="sex", curie=DEFAULT_.curie('sex'),
                   model_uri=DEFAULT_.sex, domain=None, range=Union[str, "SexEnum"])

slots.race = Slot(uri=DEFAULT_.race, name="race", curie=DEFAULT_.curie('race'),
                   model_uri=DEFAULT_.race, domain=None, range=Union[str, "RaceEnum"])

slots.race_other = Slot(uri=DEFAULT_.race_other, name="race_other", curie=DEFAULT_.curie('race_other'),
                   model_uri=DEFAULT_.race_other, domain=None, range=Optional[str])

slots.ethnicity = Slot(uri=DEFAULT_.ethnicity, name="ethnicity", curie=DEFAULT_.curie('ethnicity'),
                   model_uri=DEFAULT_.ethnicity, domain=None, range=Union[str, "EthnicityEnum"])

slots.prior_cancer = Slot(uri=DEFAULT_.prior_cancer, name="prior_cancer", curie=DEFAULT_.curie('prior_cancer'),
                   model_uri=DEFAULT_.prior_cancer, domain=None, range=Union[str, "YesNoUnknownNotReportedEnum"])

slots.relation = Slot(uri=DEFAULT_.relation, name="relation", curie=DEFAULT_.curie('relation'),
                   model_uri=DEFAULT_.relation, domain=None, range=Optional[Union[str, "RelationEnum"]])

slots.prior_cancer_type = Slot(uri=DEFAULT_.prior_cancer_type, name="prior_cancer_type", curie=DEFAULT_.curie('prior_cancer_type'),
                   model_uri=DEFAULT_.prior_cancer_type, domain=None, range=Optional[str])

slots.honest_broker_subject_id = Slot(uri=DEFAULT_.honest_broker_subject_id, name="honest_broker_subject_id", curie=DEFAULT_.curie('honest_broker_subject_id'),
                   model_uri=DEFAULT_.honest_broker_subject_id, domain=None, range=URIRef)

slots.consortium = Slot(uri=DEFAULT_.consortium, name="consortium", curie=DEFAULT_.curie('consortium'),
                   model_uri=DEFAULT_.consortium, domain=None, range=Optional[Union[str, "ConsortiumEnum"]])

slots.data_contributor_id = Slot(uri=DEFAULT_.data_contributor_id, name="data_contributor_id", curie=DEFAULT_.curie('data_contributor_id'),
                   model_uri=DEFAULT_.data_contributor_id, domain=None, range=Optional[Union[str, "DataContributorIdEnum"]])

slots.study_id = Slot(uri=DEFAULT_.study_id, name="study_id", curie=DEFAULT_.curie('study_id'),
                   model_uri=DEFAULT_.study_id, domain=None, range=Optional[Union[str, "StudyIdEnum"]])

slots.age_at_enrollment = Slot(uri=DEFAULT_.age_at_enrollment, name="age_at_enrollment", curie=DEFAULT_.curie('age_at_enrollment'),
                   model_uri=DEFAULT_.age_at_enrollment, domain=None, range=Optional[int])

slots.year_at_enrollment = Slot(uri=DEFAULT_.year_at_enrollment, name="year_at_enrollment", curie=DEFAULT_.curie('year_at_enrollment'),
                   model_uri=DEFAULT_.year_at_enrollment, domain=None, range=Optional[int])

slots.treatment_arm = Slot(uri=DEFAULT_.treatment_arm, name="treatment_arm", curie=DEFAULT_.curie('treatment_arm'),
                   model_uri=DEFAULT_.treatment_arm, domain=None, range=Optional[Union[str, "TreatmentArmEnum"]])

slots.enrolled_status = Slot(uri=DEFAULT_.enrolled_status, name="enrolled_status", curie=DEFAULT_.curie('enrolled_status'),
                   model_uri=DEFAULT_.enrolled_status, domain=None, range=Optional[Union[str, "EnrolledStatusEnum"]])

slots.efs_censor_status = Slot(uri=DEFAULT_.efs_censor_status, name="efs_censor_status", curie=DEFAULT_.curie('efs_censor_status'),
                   model_uri=DEFAULT_.efs_censor_status, domain=None, range=Optional[Union[str, "CensorStatusEnum"]])

slots.age_at_censor_status = Slot(uri=DEFAULT_.age_at_censor_status, name="age_at_censor_status", curie=DEFAULT_.curie('age_at_censor_status'),
                   model_uri=DEFAULT_.age_at_censor_status, domain=None, range=Optional[int])

slots.data_source = Slot(uri=DEFAULT_.data_source, name="data_source", curie=DEFAULT_.curie('data_source'),
                   model_uri=DEFAULT_.data_source, domain=None, range=Optional[Union[str, "DataSourceEnum"]])

slots.randomized_status = Slot(uri=DEFAULT_.randomized_status, name="randomized_status", curie=DEFAULT_.curie('randomized_status'),
                   model_uri=DEFAULT_.randomized_status, domain=None, range=Optional[Union[str, "RandomizedStatusEnum"]])

slots.study_phase = Slot(uri=DEFAULT_.study_phase, name="study_phase", curie=DEFAULT_.curie('study_phase'),
                   model_uri=DEFAULT_.study_phase, domain=None, range=Optional[Union[str, "StudyPhaseEnum"]])

slots.study_type = Slot(uri=DEFAULT_.study_type, name="study_type", curie=DEFAULT_.curie('study_type'),
                   model_uri=DEFAULT_.study_type, domain=None, range=Optional[Union[str, "StudyTypeEnum"]])
