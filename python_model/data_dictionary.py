# Auto generated from data_dictionary.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-01-10T14:50:18
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
class SubjectHonestBrokerSubjectId(extended_str):
    pass


@dataclass
class NamedThing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/NamedThing")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/NamedThing")

    submitter_id: Optional[str] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.submitter_id is not None and not isinstance(self.submitter_id, str):
            self.submitter_id = str(self.submitter_id)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass
class Person(NamedThing):
    """
    demographic information about an individual
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Person
    class_class_curie: ClassVar[str] = "schema:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/Person")

    ethnicity: Union[str, "EthnicityEnum"] = None
    sex: Union[str, "SexEnum"] = None
    race: Union[str, "RaceEnum"] = None
    race_other: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.ethnicity):
            self.MissingRequiredField("ethnicity")
        if not isinstance(self.ethnicity, EthnicityEnum):
            self.ethnicity = EthnicityEnum(self.ethnicity)

        if self._is_empty(self.sex):
            self.MissingRequiredField("sex")
        if not isinstance(self.sex, SexEnum):
            self.sex = SexEnum(self.sex)

        if self._is_empty(self.race):
            self.MissingRequiredField("race")
        if not isinstance(self.race, RaceEnum):
            self.race = RaceEnum(self.race)

        if self.race_other is not None and not isinstance(self.race_other, str):
            self.race_other = str(self.race_other)

        super().__post_init__(**kwargs)


@dataclass
class FamilyMedicalHistory(NamedThing):
    """
    prior cancer information of a first-degree relative
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.FamilyMedicalHistory
    class_class_curie: ClassVar[str] = "schema:FamilyMedicalHistory"
    class_name: ClassVar[str] = "FamilyMedicalHistory"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/FamilyMedicalHistory")

    prior_cancer: Union[str, "YesNoUnknownNotReportedEnum"] = None
    subjects: Union[str, SubjectHonestBrokerSubjectId] = None
    relation: Optional[Union[str, "RelationEnum"]] = None
    prior_cancer_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.prior_cancer):
            self.MissingRequiredField("prior_cancer")
        if not isinstance(self.prior_cancer, YesNoUnknownNotReportedEnum):
            self.prior_cancer = YesNoUnknownNotReportedEnum(self.prior_cancer)

        if self._is_empty(self.subjects):
            self.MissingRequiredField("subjects")
        if not isinstance(self.subjects, SubjectHonestBrokerSubjectId):
            self.subjects = SubjectHonestBrokerSubjectId(self.subjects)

        if self.relation is not None and not isinstance(self.relation, RelationEnum):
            self.relation = RelationEnum(self.relation)

        if self.prior_cancer_type is not None and not isinstance(self.prior_cancer_type, str):
            self.prior_cancer_type = str(self.prior_cancer_type)

        super().__post_init__(**kwargs)


@dataclass
class Subject(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Subject
    class_class_curie: ClassVar[str] = "schema:Subject"
    class_name: ClassVar[str] = "Subject"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/Subject")

    honest_broker_subject_id: Union[str, SubjectHonestBrokerSubjectId] = None
    persons: Union[dict, Person] = None
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
        if not isinstance(self.honest_broker_subject_id, SubjectHonestBrokerSubjectId):
            self.honest_broker_subject_id = SubjectHonestBrokerSubjectId(self.honest_broker_subject_id)

        if self._is_empty(self.persons):
            self.MissingRequiredField("persons")
        if not isinstance(self.persons, Person):
            self.persons = Person(**as_dict(self.persons))

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


@dataclass
class Timing(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Timing
    class_class_curie: ClassVar[str] = "schema:Timing"
    class_name: ClassVar[str] = "Timing"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/Timing")

    subjects: Union[str, SubjectHonestBrokerSubjectId] = None
    age_at_course_anc_500: Optional[int] = None
    age_at_course_end: Optional[int] = None
    age_at_course_start: Optional[int] = None
    age_at_cyle_end: Optional[int] = None
    age_at_cycle_start: Optional[int] = None
    age_at_disease_phase: Optional[int] = None
    age_at_txassign: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    cycle_number: Optional[int] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    timing_type: Optional[str] = None
    timings: Optional[Union[dict, "Timing"]] = None
    year_at_disease_phase: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subjects):
            self.MissingRequiredField("subjects")
        if not isinstance(self.subjects, SubjectHonestBrokerSubjectId):
            self.subjects = SubjectHonestBrokerSubjectId(self.subjects)

        if self.age_at_course_anc_500 is not None and not isinstance(self.age_at_course_anc_500, int):
            self.age_at_course_anc_500 = int(self.age_at_course_anc_500)

        if self.age_at_course_end is not None and not isinstance(self.age_at_course_end, int):
            self.age_at_course_end = int(self.age_at_course_end)

        if self.age_at_course_start is not None and not isinstance(self.age_at_course_start, int):
            self.age_at_course_start = int(self.age_at_course_start)

        if self.age_at_cyle_end is not None and not isinstance(self.age_at_cyle_end, int):
            self.age_at_cyle_end = int(self.age_at_cyle_end)

        if self.age_at_cycle_start is not None and not isinstance(self.age_at_cycle_start, int):
            self.age_at_cycle_start = int(self.age_at_cycle_start)

        if self.age_at_disease_phase is not None and not isinstance(self.age_at_disease_phase, int):
            self.age_at_disease_phase = int(self.age_at_disease_phase)

        if self.age_at_txassign is not None and not isinstance(self.age_at_txassign, int):
            self.age_at_txassign = int(self.age_at_txassign)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.cycle_number is not None and not isinstance(self.cycle_number, int):
            self.cycle_number = int(self.cycle_number)

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.timing_type is not None and not isinstance(self.timing_type, str):
            self.timing_type = str(self.timing_type)

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.year_at_disease_phase is not None and not isinstance(self.year_at_disease_phase, int):
            self.year_at_disease_phase = int(self.year_at_disease_phase)

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

class CourseEnum(EnumDefinitionImpl):

    Prephase = PermissibleValue(text="Prephase",
                                       description="A chemotherapy treatment administered prior to the definitive chemotherapy treatment.",
                                       meaning=NCIT.C168826)
    Induction = PermissibleValue(text="Induction",
                                         description="The first choice of treatment for a particular type of cancer.",
                                         meaning=NCIT.C158876)
    Maintenance = PermissibleValue(text="Maintenance",
                                             description="Continuation of treatment for an extended period of time to prevent relapse.",
                                             meaning=NCIT.C15688)
    Consolidation = PermissibleValue(text="Consolidation",
                                                 description="Treatment that is given after initial therapy to kill any remaining cancer cells.",
                                                 meaning=NCIT.C15679)
    Intensification = PermissibleValue(text="Intensification",
                                                     description="A second round of intense chemotherapy as part of consolidation therapy.",
                                                     meaning=NCIT.C173105)
    Adjuvant = PermissibleValue(text="Adjuvant",
                                       description="Chemotherapy that is administered subsequent to the main treatment plan to minimize or prevent disease recurrence.",
                                       meaning=NCIT.C15360)
    Continuation = PermissibleValue(text="Continuation",
                                               description="A period in a clinical study during which subjects receive continuation therapy. This therapy is usually different from the therapy given during the induction phase and administered over a longer period of time.",
                                               meaning=NCIT.C123452)
    Chemotherapy = PermissibleValue(text="Chemotherapy",
                                               description="The use of synthetic or naturally-occurring chemicals for the treatment of diseases.",
                                               meaning=NCIT.C15632)
    Chemoimmunotherapy = PermissibleValue(text="Chemoimmunotherapy",
                                                           description="Chemotherapy combined with immunotherapy. Chemotherapy uses different drugs to kill or slow the growth of cancer cells; immunotherapy uses treatments to stimulate or restore the ability of the immune system to fight cancer.",
                                                           meaning=NCIT.C94251)
    Immunotherapy = PermissibleValue(text="Immunotherapy",
                                                 description="Therapy designed to induce changes in a patient's immune status in order to treat disease.",
                                                 meaning=NCIT.C15262)

    _defn = EnumDefinition(
        name="CourseEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Neo-Adjuvant",
                PermissibleValue(text="Neo-Adjuvant",
                                 description="Therapy administered prior to the initial therapy.",
                                 meaning=NCIT.C158708) )
        setattr(cls, "Bridge/Preconsolidation",
                PermissibleValue(text="Bridge/Preconsolidation") )
        setattr(cls, "Delayed Intensification",
                PermissibleValue(text="Delayed Intensification",
                                 description="A repeat of the first two months of induction and consolidation chemotherapy in high-risk and very-high-risk ALL protocols with the goal of eliminating residual drug-resistant cells",
                                 meaning=NCIT.C178270) )
        setattr(cls, "Interim Maintenance",
                PermissibleValue(text="Interim Maintenance",
                                 description="A less intense phase of chemotherapy in between each course of delayed intensification.",
                                 meaning=NCIT.C178069) )
        setattr(cls, "Post-Consolidation",
                PermissibleValue(text="Post-Consolidation") )
        setattr(cls, "Palliative Treatment",
                PermissibleValue(text="Palliative Treatment",
                                 description="The patient- and family-centered active holistic care of patients with advanced, progressive disease. Essential components of Palliative Care are:pain and symptom control, communication regarding treatment and alternatives, prognosis, and available services, rehabilitation services, care that addresses treatment and palliative concerns, intellectual, emotional, social, and spiritual needs, terminal care, support in bereavement. The goal of Palliative Care is an achievement of the best quality of life for patients and their families.",
                                 meaning=NCIT.C15292) )
        setattr(cls, "Chemotherapy Window",
                PermissibleValue(text="Chemotherapy Window") )
        setattr(cls, "Stem Cell Transplant Conditioning",
                PermissibleValue(text="Stem Cell Transplant Conditioning",
                                 description="A regimen that can be used as a conditioning regimen for hematopoietic stem cell transplantation (HSCT).",
                                 meaning=NCIT.C168794) )
        setattr(cls, "Chemotherapy Alone",
                PermissibleValue(text="Chemotherapy Alone",
                                 description="The use of synthetic or naturally-occurring chemicals for the treatment of diseases.",
                                 meaning=NCIT.C15632) )
        setattr(cls, "Investigational Agent",
                PermissibleValue(text="Investigational Agent",
                                 description="A new drug or biological drug that is used in a clinical investigation. The term also includes a biological product that is used in vitro for diagnostic purposes.",
                                 meaning=NCIT.C49135) )
        setattr(cls, "Radiation Therapy",
                PermissibleValue(text="Radiation Therapy",
                                 description="Treatment of a disease by means of exposure of the target or the whole body to radiation. Radiation therapy is often used as part of curative therapy and occasionally as a component of palliative treatment for cancer. Other uses include total body irradiation prior to transplantation.",
                                 meaning=NCIT.C15313) )

class DiseasePhaseEnum(EnumDefinitionImpl):

    Relapse = PermissibleValue(text="Relapse",
                                     description="The return of a disease after a period of remission.",
                                     meaning=NCIT.C38155)
    Progression = PermissibleValue(text="Progression",
                                             description="The worsening of a disease over time.",
                                             meaning=NCIT.C17747)
    Refractory = PermissibleValue(text="Refractory",
                                           description="Not responding to treatment.",
                                           meaning=NCIT.C38014)

    _defn = EnumDefinition(
        name="DiseasePhaseEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Initial Diagnosis",
                PermissibleValue(text="Initial Diagnosis",
                                 description="The first diagnosis of the individual's condition.",
                                 meaning=NCIT.C156813) )
        setattr(cls, "Relapse/Progression",
                PermissibleValue(text="Relapse/Progression",
                                 description="Either the return of the disease or the progression of the disease.",
                                 meaning=NCIT.C174991) )

# Slots
class slots:
    pass

slots.submitter_id = Slot(uri=DEFAULT_.submitter_id, name="submitter_id", curie=DEFAULT_.curie('submitter_id'),
                   model_uri=DEFAULT_.submitter_id, domain=None, range=Optional[str])

slots.type = Slot(uri=DEFAULT_.type, name="type", curie=DEFAULT_.curie('type'),
                   model_uri=DEFAULT_.type, domain=None, range=Optional[str])

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

slots.subjects = Slot(uri=DEFAULT_.subjects, name="subjects", curie=DEFAULT_.curie('subjects'),
                   model_uri=DEFAULT_.subjects, domain=None, range=Optional[Union[str, SubjectHonestBrokerSubjectId]])

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

slots.age_at_course_anc_500 = Slot(uri=DEFAULT_.age_at_course_anc_500, name="age_at_course_anc_500", curie=DEFAULT_.curie('age_at_course_anc_500'),
                   model_uri=DEFAULT_.age_at_course_anc_500, domain=None, range=Optional[int])

slots.age_at_course_end = Slot(uri=DEFAULT_.age_at_course_end, name="age_at_course_end", curie=DEFAULT_.curie('age_at_course_end'),
                   model_uri=DEFAULT_.age_at_course_end, domain=None, range=Optional[int])

slots.age_at_course_start = Slot(uri=DEFAULT_.age_at_course_start, name="age_at_course_start", curie=DEFAULT_.curie('age_at_course_start'),
                   model_uri=DEFAULT_.age_at_course_start, domain=None, range=Optional[int])

slots.age_at_cyle_end = Slot(uri=DEFAULT_.age_at_cyle_end, name="age_at_cyle_end", curie=DEFAULT_.curie('age_at_cyle_end'),
                   model_uri=DEFAULT_.age_at_cyle_end, domain=None, range=Optional[int])

slots.age_at_cycle_start = Slot(uri=DEFAULT_.age_at_cycle_start, name="age_at_cycle_start", curie=DEFAULT_.curie('age_at_cycle_start'),
                   model_uri=DEFAULT_.age_at_cycle_start, domain=None, range=Optional[int])

slots.age_at_disease_phase = Slot(uri=DEFAULT_.age_at_disease_phase, name="age_at_disease_phase", curie=DEFAULT_.curie('age_at_disease_phase'),
                   model_uri=DEFAULT_.age_at_disease_phase, domain=None, range=Optional[int])

slots.age_at_txassign = Slot(uri=DEFAULT_.age_at_txassign, name="age_at_txassign", curie=DEFAULT_.curie('age_at_txassign'),
                   model_uri=DEFAULT_.age_at_txassign, domain=None, range=Optional[int])

slots.course = Slot(uri=DEFAULT_.course, name="course", curie=DEFAULT_.curie('course'),
                   model_uri=DEFAULT_.course, domain=None, range=Optional[Union[str, "CourseEnum"]])

slots.course_number = Slot(uri=DEFAULT_.course_number, name="course_number", curie=DEFAULT_.curie('course_number'),
                   model_uri=DEFAULT_.course_number, domain=None, range=Optional[int])

slots.cycle_number = Slot(uri=DEFAULT_.cycle_number, name="cycle_number", curie=DEFAULT_.curie('cycle_number'),
                   model_uri=DEFAULT_.cycle_number, domain=None, range=Optional[int])

slots.disease_phase = Slot(uri=DEFAULT_.disease_phase, name="disease_phase", curie=DEFAULT_.curie('disease_phase'),
                   model_uri=DEFAULT_.disease_phase, domain=None, range=Optional[Union[str, "DiseasePhaseEnum"]])

slots.disease_phase_number = Slot(uri=DEFAULT_.disease_phase_number, name="disease_phase_number", curie=DEFAULT_.curie('disease_phase_number'),
                   model_uri=DEFAULT_.disease_phase_number, domain=None, range=Optional[int])

slots.timing_type = Slot(uri=DEFAULT_.timing_type, name="timing_type", curie=DEFAULT_.curie('timing_type'),
                   model_uri=DEFAULT_.timing_type, domain=None, range=Optional[str])

slots.timings = Slot(uri=DEFAULT_.timings, name="timings", curie=DEFAULT_.curie('timings'),
                   model_uri=DEFAULT_.timings, domain=None, range=Optional[Union[dict, Timing]])

slots.year_at_disease_phase = Slot(uri=DEFAULT_.year_at_disease_phase, name="year_at_disease_phase", curie=DEFAULT_.curie('year_at_disease_phase'),
                   model_uri=DEFAULT_.year_at_disease_phase, domain=None, range=Optional[int])

slots.subject__persons = Slot(uri=DEFAULT_.persons, name="subject__persons", curie=DEFAULT_.curie('persons'),
                   model_uri=DEFAULT_.subject__persons, domain=None, range=Union[dict, Person])

slots.FamilyMedicalHistory_subjects = Slot(uri=DEFAULT_.subjects, name="FamilyMedicalHistory_subjects", curie=DEFAULT_.curie('subjects'),
                   model_uri=DEFAULT_.FamilyMedicalHistory_subjects, domain=FamilyMedicalHistory, range=Union[str, SubjectHonestBrokerSubjectId])

slots.Timing_subjects = Slot(uri=DEFAULT_.subjects, name="Timing_subjects", curie=DEFAULT_.curie('subjects'),
                   model_uri=DEFAULT_.Timing_subjects, domain=Timing, range=Union[str, SubjectHonestBrokerSubjectId])
