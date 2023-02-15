# Auto generated from data_dictionary_spreadsheet_1k2m4oAX3JdfYN2lIbpBiWFUNKZwXnQCiuns0e3Wid9o.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-02-15T12:30:11
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
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NCIT = CurieNamespace('ncit', 'https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=')
PCDC = CurieNamespace('pcdc', 'https://w3id.org/pcdc/model')
DEFAULT_ = CurieNamespace('', 'https://w3id.org/pcdc/model/')


# Types

# Class references



@dataclass
class Thing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/Thing"]
    class_class_curie: ClassVar[str] = "pcdc:/Thing"
    class_name: ClassVar[str] = "Thing"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/Thing")

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


@dataclass
class Person(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/Person"]
    class_class_curie: ClassVar[str] = "pcdc:/Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/Person")

    submitter_id: str = None
    type: str = None
    sex: Optional[Union[str, "SexEnum"]] = None
    race: Optional[Union[str, "RaceEnum"]] = None
    race_other: Optional[str] = None
    ethnicity: Optional[Union[str, "EthnicityEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sex is not None and not isinstance(self.sex, SexEnum):
            self.sex = SexEnum(self.sex)

        if self.race is not None and not isinstance(self.race, RaceEnum):
            self.race = RaceEnum(self.race)

        if self.race_other is not None and not isinstance(self.race_other, str):
            self.race_other = str(self.race_other)

        if self.ethnicity is not None and not isinstance(self.ethnicity, EthnicityEnum):
            self.ethnicity = EthnicityEnum(self.ethnicity)

        super().__post_init__(**kwargs)


@dataclass
class FamilyMedicalHistory(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/FamilyMedicalHistory"]
    class_class_curie: ClassVar[str] = "pcdc:/FamilyMedicalHistory"
    class_name: ClassVar[str] = "FamilyMedicalHistory"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/FamilyMedicalHistory")

    submitter_id: str = None
    type: str = None
    prior_cancer: Optional[Union[str, "PriorCancerEnum"]] = None
    relation: Optional[Union[str, "RelationEnum"]] = None
    prior_cancer_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.prior_cancer is not None and not isinstance(self.prior_cancer, PriorCancerEnum):
            self.prior_cancer = PriorCancerEnum(self.prior_cancer)

        if self.relation is not None and not isinstance(self.relation, RelationEnum):
            self.relation = RelationEnum(self.relation)

        if self.prior_cancer_type is not None and not isinstance(self.prior_cancer_type, str):
            self.prior_cancer_type = str(self.prior_cancer_type)

        super().__post_init__(**kwargs)


@dataclass
class Subject(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/Subject"]
    class_class_curie: ClassVar[str] = "pcdc:/Subject"
    class_name: ClassVar[str] = "Subject"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/Subject")

    submitter_id: str = None
    type: str = None
    honest_broker_subject_id: Optional[str] = None
    consortium: Optional[Union[str, "ConsortiumEnum"]] = None
    data_contributor_id: Optional[Union[str, "DataContributorIdEnum"]] = None
    study_id: Optional[Union[str, "StudyIdEnum"]] = None
    age_at_enrollment: Optional[int] = None
    year_at_enrollment: Optional[int] = None
    treatment_arm: Optional[Union[str, "TreatmentArmEnum"]] = None
    enrolled_status: Optional[Union[str, "EnrolledStatusEnum"]] = None
    efs_censor_status: Optional[Union[str, "EfsCensorStatusEnum"]] = None
    age_at_censor_status: Optional[int] = None
    data_source: Optional[Union[str, "DataSourceEnum"]] = None
    randomized_status: Optional[Union[str, "RandomizedStatusEnum"]] = None
    study_phase: Optional[Union[str, "StudyPhaseEnum"]] = None
    study_type: Optional[Union[str, "StudyTypeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.honest_broker_subject_id is not None and not isinstance(self.honest_broker_subject_id, str):
            self.honest_broker_subject_id = str(self.honest_broker_subject_id)

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

        if self.efs_censor_status is not None and not isinstance(self.efs_censor_status, EfsCensorStatusEnum):
            self.efs_censor_status = EfsCensorStatusEnum(self.efs_censor_status)

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
class Timing(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/Timing"]
    class_class_curie: ClassVar[str] = "pcdc:/Timing"
    class_name: ClassVar[str] = "Timing"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/Timing")

    submitter_id: str = None
    type: str = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    age_at_disease_phase: Optional[int] = None
    year_at_disease_phase: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    age_at_course_start: Optional[int] = None
    age_at_course_end: Optional[int] = None
    age_at_txassign: Optional[int] = None
    age_at_course_anc_500: Optional[int] = None
    cycle_number: Optional[int] = None
    age_at_cycle_start: Optional[int] = None
    age_at_cycle_end: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.age_at_disease_phase is not None and not isinstance(self.age_at_disease_phase, int):
            self.age_at_disease_phase = int(self.age_at_disease_phase)

        if self.year_at_disease_phase is not None and not isinstance(self.year_at_disease_phase, int):
            self.year_at_disease_phase = int(self.year_at_disease_phase)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.age_at_course_start is not None and not isinstance(self.age_at_course_start, int):
            self.age_at_course_start = int(self.age_at_course_start)

        if self.age_at_course_end is not None and not isinstance(self.age_at_course_end, int):
            self.age_at_course_end = int(self.age_at_course_end)

        if self.age_at_txassign is not None and not isinstance(self.age_at_txassign, int):
            self.age_at_txassign = int(self.age_at_txassign)

        if self.age_at_course_anc_500 is not None and not isinstance(self.age_at_course_anc_500, int):
            self.age_at_course_anc_500 = int(self.age_at_course_anc_500)

        if self.cycle_number is not None and not isinstance(self.cycle_number, int):
            self.cycle_number = int(self.cycle_number)

        if self.age_at_cycle_start is not None and not isinstance(self.age_at_cycle_start, int):
            self.age_at_cycle_start = int(self.age_at_cycle_start)

        if self.age_at_cycle_end is not None and not isinstance(self.age_at_cycle_end, int):
            self.age_at_cycle_end = int(self.age_at_cycle_end)

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

class PriorCancerEnum(EnumDefinitionImpl):

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
        name="PriorCancerEnum",
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
                             description="Consortium for Childhood Cancer Predisposition")

    _defn = EnumDefinition(
        name="ConsortiumEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Global REACH",
                PermissibleValue(text="Global REACH",
                                 description="Global Retinoblastoma Alliance for Children") )

class DataContributorIdEnum(EnumDefinitionImpl):

    AIEOP = PermissibleValue(text="AIEOP",
                                 description="è l'Associazione Italiana di Ematologia e Oncologia Pediatrica is a group from Bologna, Italy, comprised mainly of pediatricians, hematologists, oncologists, surgeons, biologists, nurses and psychologists who are devoted to addressing the problems of hematology, oncology and immunology in the child and adolescent.",
                                 meaning=NCIT.C168887)
    COG = PermissibleValue(text="COG",
                             description="Children's Oncology Group. An NCI-supported clinical cooperative group formed by the merger of the four national pediatric cancer research organizations: the Children's Cancer Group, the Intergroup Rhabdomyosarcoma Study Group, the National Wilms Tumor Study Group, and the Pediatric Oncology Group. The primary objective of the organization is to conduct clinical trials of new therapies for childhood and adolescent cancer. COG develops and coordinates clinical trials conducted at the 238 member institutions that include cancer centers of all major universities and teaching hospitals throughout the U.S. and Canada, as well as sites in Europe and Australia. COG members include over 5000 cancer researchers.",
                             meaning=NCIT.C39353)
    DCOG = PermissibleValue(text="DCOG",
                               description="A collaborating partner in Innovative Therapies for Children with Cancer Consortium (ITCC), a European based consortium to promote the clinical evaluation of new anti-cancer compounds in children with cancer.",
                               meaning=NCIT.C168889)
    MRC = PermissibleValue(text="MRC",
                             description="Medical Research Council. A publicly funded organization that is part of United Kingdom Research and Innovation, and is dedicated to improving human health through world-class medical research.",
                             meaning=NCIT.C168892)
    NOPHO = PermissibleValue(text="NOPHO",
                                 description="A collaborative group formed in 1984 with members from Denmark, Finland, Iceland, Lithuania, Norway and Sweden and whose goal was to secure that all Nordic children suffering from leukemia would receive optimal therapy wherever they lived.",
                                 meaning=NCIT.C168893)
    PPLLSG = PermissibleValue(text="PPLLSG",
                                   description="A collaborative group established in 1974 that had the original goal of implementing unified protocols with standardized diagnostic criteria and therapy regimens for Hodgkin's disease and acute lymphoblastic leukemia. The prospects were widened to include non-Hodgkin's lymphomas and acute myelogenous leukemia in 1983.",
                                   meaning=NCIT.C168894)
    SJCRH = PermissibleValue(text="SJCRH",
                                 description="The Saint Jude Children's Research Hospital received its NCI designation in 1977 and was awarded status as a comprehensive cancer center by NCI in 2008. Research is focused specifically on childhood cancers, acquired and inherited immunodeficiencies and genetic disorders.",
                                 meaning=NCIT.C39510)
    CCLG = PermissibleValue(text="CCLG",
                               description="A children's cancer charity and United Kingdom and Ireland's professional association for those involved in the treatment and care of children with cancer.",
                               meaning=NCIT.C177327)
    GPOH = PermissibleValue(text="GPOH",
                               description="German Pediatric Oncology-Hematology Society. A research organization in Germany involved in the understanding, diagnosis, treatment and prognosis of pediatric cancers.",
                               meaning=NCIT.C174960)
    SSG = PermissibleValue(text="SSG",
                             description="Scandinavian Sarcoma Group. A research organization in Scandinavia involved in the understanding, diagnosis, treatment and prognosis of sarcoma in children and adolescents.",
                             meaning=NCIT.C174961)
    FSG = PermissibleValue(text="FSG",
                             description="French Sarcoma Group. A research organization in France involved in the understanding, diagnosis, treatment and prognosis of sarcoma in children and adolescents.",
                             meaning=NCIT.C174962)
    UK = PermissibleValue(text="UK",
                           description="United Kingdom Sarcoma Registry. An information system in the United Kingdom designed for the collection, storage, and management of data on persons with sarcoma.",
                           meaning=NCIT.C174963)
    ISG = PermissibleValue(text="ISG",
                             description="Italian Sarcoma Group. A independent, scientific non-profit association formed in 2002 with the purpose of improving the quality of treatment for sarcoma.",
                             meaning=NCIT.C174965)
    CRCTU = PermissibleValue(text="CRCTU",
                                 description="Cancer Research Clinical Trials Unit. A research organization in the United Kingdom specializing in the design and delivery of every aspect of clinical trials of all phases in adults and children, from concept to publication.",
                                 meaning=NCIT.C174966)
    JACLS = PermissibleValue(text="JACLS",
                                 description="A study group in Japan investigating childhood leukemia.",
                                 meaning=NCIT.C168890)
    JPLSG = PermissibleValue(text="JPLSG",
                                 description="A study group in Japan investigating pediatric leukemia and lymphoma.",
                                 meaning=NCIT.C168891)
    SFCE = PermissibleValue(text="SFCE",
                               description="Société Française de Lutte contre les Cancers et Leucémies de l'Enfant et de l'Adolescent",
                               meaning=NCIT.C177328)
    SOPOBE = PermissibleValue(text="SOPOBE",
                                   description="Brazilian Society of Pediatric Oncology",
                                   meaning=NCIT.C177329)
    DFCI = PermissibleValue(text="DFCI",
                               description="Dana Farber Cancer Institute",
                               meaning=NCIT.C177330)
    JCCG = PermissibleValue(text="JCCG",
                               description="Neuroblastoma Committee of Japan Children’s Cancer Group")
    JINCS = PermissibleValue(text="JINCS",
                                 description="Japanese Infantile Neuroblastoma Co-operative Study Group")
    SIOPEN = PermissibleValue(text="SIOPEN",
                                   description="Society of Paediatric Oncology Europe Neuroblastoma Group")
    JNBSG = PermissibleValue(text="JNBSG",
                                 description="Japan Neuroblatoma Study Group")
    EpSSG = PermissibleValue(text="EpSSG",
                                 description="European Paediatric Soft Tissue Sarcoma Study Group")
    ICG = PermissibleValue(text="ICG",
                             description="Italian Cooperative Group")
    CWS = PermissibleValue(text="CWS",
                             description="Cooperative Weichteilsarkom Studiengruppe")
    STSC = PermissibleValue(text="STSC",
                               description="AIEOP Soft Tissue Sarcoma Committee")
    ARST0331 = PermissibleValue(text="ARST0331")
    ARST0431 = PermissibleValue(text="ARST0431")
    ARST0531 = PermissibleValue(text="ARST0531")
    ARST08P1 = PermissibleValue(text="ARST08P1")
    D9602 = PermissibleValue(text="D9602")
    D9802 = PermissibleValue(text="D9802")
    D9803 = PermissibleValue(text="D9803")
    RMS2005 = PermissibleValue(text="RMS2005")
    MTS2008 = PermissibleValue(text="MTS2008")
    CWS2002P = PermissibleValue(text="CWS2002P")
    CWS91 = PermissibleValue(text="CWS91")
    CWS96 = PermissibleValue(text="CWS96")
    MMT95 = PermissibleValue(text="MMT95")
    BOCG = PermissibleValue(text="BOCG",
                               description="Brazilian Group and Scandinavian Group. A cooperative group of individuals working with pediatric osteosarcoma.",
                               meaning=NCIT.C180373)
    GEIS = PermissibleValue(text="GEIS",
                               description="Spanish Sarcoma Group. A scientific society formed by professionals from more than sixty medical centers across Spain. This group includes surgeons, pediatricians, oncologic radiation therapy specialists, pathologists and molecular researchers.",
                               meaning=NCIT.C180341)
    UCL = PermissibleValue(text="UCL",
                             description="University College of London. A public research university located in London, England.",
                             meaning=NCIT.C174967)

    _defn = EnumDefinition(
        name="DataContributorIdEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "BFM-SG",
                PermissibleValue(text="BFM-SG",
                                 description="A study group formed in 1975 by three individuals, Hansjorg Riehm in Berlin (B), Bernhard Kornhuber in Frankfurt (F) and Gunther Schellong in Munster (M), who initiated the first multicenter BFM trial. The BFM treatment concept was based on an intensive chemotherapeutic approach employing eight different drugs which led to a revolutionary increase in the survival of children and adolescents with acute lymphoblastic leukemia.",
                                 meaning=NCIT.C168888) )
        setattr(cls, "NRG-Oncology",
                PermissibleValue(text="NRG-Oncology",
                                 description="A leading protocol organization within the National Clinical Trials Network that seeks to improve the lives of cancer patients by conducting practice-changing, multi-institutional clinical and translational research.",
                                 meaning=NCIT.C168950) )
        setattr(cls, "EURO-EWING",
                PermissibleValue(text="EURO-EWING",
                                 description="A coalition of clinical study groups bringing together active clinicians and scientists in Europe dedicated to improving survival from Ewing sarcoma.",
                                 meaning=NCIT.C174964) )
        setattr(cls, "University College of London",
                PermissibleValue(text="University College of London",
                                 description="A public research university located in London, England.",
                                 meaning=NCIT.C174967) )
        setattr(cls, "SIOP MMT",
                PermissibleValue(text="SIOP MMT",
                                 description="Society of Paediatric Oncology Malignant Mesenchymal Tumour Committee ") )
        setattr(cls, "ICG RMS96",
                PermissibleValue(text="ICG RMS96") )
        setattr(cls, "RMS 4.99",
                PermissibleValue(text="RMS 4.99") )
        setattr(cls, "CWS-IV-2002",
                PermissibleValue(text="CWS-IV-2002") )
        setattr(cls, "COSS-GPOH",
                PermissibleValue(text="COSS-GPOH",
                                 description="Cooperative German-Austrian-Swiss Osteosarcoma Study Group (COSS) of the German Pediatric Oncology-Hematology Society (GPOH). The section of the German Society of Pediatric Oncology and Hematology dedicated to the study of osteosarcoma.",
                                 meaning=NCIT.C186743) )

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
    AMLBFMRegistry2017 = PermissibleValue(text="AMLBFMRegistry2017",
                                                           meaning=NCIT.C182031)
    AMLBFM1998 = PermissibleValue(text="AMLBFM1998",
                                           meaning=NCIT.C182032)
    SJCRHAML02 = PermissibleValue(text="SJCRHAML02",
                                           meaning=NCIT.C168940)
    JPLSGAML05 = PermissibleValue(text="JPLSGAML05",
                                           meaning=NCIT.C168941)
    AEIOPAML2002 = PermissibleValue(text="AEIOPAML2002",
                                               meaning=NCIT.C168942)
    JACLSAML99 = PermissibleValue(text="JACLSAML99",
                                           meaning=NCIT.C168943)
    DBAML01 = PermissibleValue(text="DBAML01",
                                     meaning=NCIT.C168944)
    MRCAML12 = PermissibleValue(text="MRCAML12",
                                       meaning=NCIT.C168945)
    MRCAML15 = PermissibleValue(text="MRCAML15",
                                       meaning=NCIT.C173252)
    NOPHOAML2004 = PermissibleValue(text="NOPHOAML2004",
                                               meaning=NCIT.C168946)
    NOPHOAML2012 = PermissibleValue(text="NOPHOAML2012",
                                               meaning=NCIT.C173253)
    PPLLSGAML98 = PermissibleValue(text="PPLLSGAML98",
                                             meaning=NCIT.C173254)
    AIEOPLAM92 = PermissibleValue(text="AIEOPLAM92",
                                           meaning=NCIT.C173255)
    SCFEELAM02 = PermissibleValue(text="SCFEELAM02",
                                           meaning=NCIT.C168947)
    AHOD0831 = PermissibleValue(text="AHOD0831",
                                       meaning=NCIT.C185308)
    AHOD0431 = PermissibleValue(text="AHOD0431",
                                       meaning=NCIT.C185310)
    AHOD0031 = PermissibleValue(text="AHOD0031",
                                       meaning=NCIT.C185311)
    AHOD1331 = PermissibleValue(text="AHOD1331",
                                       meaning=NCIT.C185312)
    AHOD1221 = PermissibleValue(text="AHOD1221",
                                       meaning=NCIT.C185313)
    AHOD03P1 = PermissibleValue(text="AHOD03P1",
                                       meaning=NCIT.C185314)
    AEWS1221 = PermissibleValue(text="AEWS1221",
                                       meaning=NCIT.C174968)
    AEWS0331 = PermissibleValue(text="AEWS0331",
                                       meaning=NCIT.C174969)
    AEWS0031 = PermissibleValue(text="AEWS0031",
                                       meaning=NCIT.C174970)
    AEWS1031 = PermissibleValue(text="AEWS1031",
                                       meaning=NCIT.C174971)
    EE99 = PermissibleValue(text="EE99",
                               meaning=NCIT.C174972)
    EICESS92 = PermissibleValue(text="EICESS92",
                                       meaning=NCIT.C174973)
    AEWS07P1 = PermissibleValue(text="AEWS07P1",
                                       meaning=NCIT.C174974)
    AALL0331 = PermissibleValue(text="AALL0331",
                                       description="Standard Risk B-precursor Acute Lymphoblastic Leukemia (ALL) is a COG study from 2003-2011",
                                       meaning=NCIT.C178095)
    AALL0232 = PermissibleValue(text="AALL0232",
                                       description="High Risk B-precursor Acute Lymphoblastic Leukemia (ALL) is a COG study from 2003-2011",
                                       meaning=NCIT.C178065)
    AALL0434 = PermissibleValue(text="AALL0434",
                                       description="Intensified Methotrexate, Nelarabine (Compound 506U78; IND # 52611) and Augmented BFM Therapy for Children and Young Adults with Newly Diagnosed T-cell Acute Lymphoblastic Leukemia(ALL)or T-cell LymphoblasticLymphoma is a COG study from 2007-2014",
                                       meaning=NCIT.C178066)
    AALL08B1 = PermissibleValue(text="AALL08B1",
                                       description="Classification of Newly Diagnosed Acute Lymphoblastic Leukemia (ALL) is a COG study from 2010-2018",
                                       meaning=NCIT.C178067)
    AALL03B1 = PermissibleValue(text="AALL03B1",
                                       description="Classification of Acute Lymphoblastic Leukemia is a COG study from 2003-2011",
                                       meaning=NCIT.C178068)
    TGM85 = PermissibleValue(text="TGM85",
                                 meaning=NCIT.C177332)
    TGM90 = PermissibleValue(text="TGM90",
                                 meaning=NCIT.C177333)
    TGM95 = PermissibleValue(text="TGM95",
                                 meaning=NCIT.C177334)
    GC1 = PermissibleValue(text="GC1",
                             meaning=NCIT.C113593)
    GC2 = PermissibleValue(text="GC2",
                             meaning=NCIT.C177336)
    GOG0078 = PermissibleValue(text="GOG0078",
                                     meaning=NCIT.C177337)
    GOG0090 = PermissibleValue(text="GOG0090",
                                     meaning=NCIT.C177338)
    GOG0116 = PermissibleValue(text="GOG0116",
                                     meaning=NCIT.C177339)
    P9749 = PermissibleValue(text="P9749",
                                 meaning=NCIT.C177340)
    POG9049 = PermissibleValue(text="POG9049",
                                     meaning=NCIT.C177341)
    AGCT01P1 = PermissibleValue(text="AGCT01P1",
                                       meaning=NCIT.C177342)
    AGCT0132 = PermissibleValue(text="AGCT0132",
                                       meaning=NCIT.C177343)
    AGCT0521 = PermissibleValue(text="AGCT0521",
                                       meaning=NCIT.C177344)
    TE04 = PermissibleValue(text="TE04",
                               meaning=NCIT.C20299)
    TE05 = PermissibleValue(text="TE05",
                               meaning=NCIT.C177346)
    TE08 = PermissibleValue(text="TE08",
                               meaning=NCIT.C177347)
    TE22 = PermissibleValue(text="TE22",
                               meaning=NCIT.C177348)
    TE09 = PermissibleValue(text="TE09",
                               meaning=NCIT.C177349)
    TE13 = PermissibleValue(text="TE13",
                               meaning=NCIT.C177350)
    TE20 = PermissibleValue(text="TE20",
                               meaning=NCIT.C177351)
    TIP = PermissibleValue(text="TIP",
                             meaning=NCIT.C90069)
    TCGM2004 = PermissibleValue(text="TCGM2004",
                                       meaning=NCIT.C187201)
    MMT89 = PermissibleValue(text="MMT89")
    MMT95 = PermissibleValue(text="MMT95")
    EpSSG05 = PermissibleValue(text="EpSSG05")
    Bernie = PermissibleValue(text="Bernie")
    OS2006 = PermissibleValue(text="OS2006",
                                   meaning=NCIT.C180367)
    REGOBONE = PermissibleValue(text="REGOBONE",
                                       description="A Randomized Phase II, placebo-controlled , multicenterstudy evaluating efficacy and safety of regorafenib inpatients with metastatic bone sarcomas",
                                       meaning=NCIT.C180369)
    P9754 = PermissibleValue(text="P9754",
                                 meaning=NCIT.C180368)
    INT133 = PermissibleValue(text="INT133",
                                   description="Trial of Adriamycin, Cisplatin and Methotrexate With and Without Ifosfamide, With and Without Muramyl Tripeptide Phosphatidyl Ethanolamine (MTP-PE) for Treatment of Osteogenic Sarcoma",
                                   meaning=NCIT.C180366)
    AOST0221 = PermissibleValue(text="AOST0221",
                                       meaning=NCIT.C180360)
    AOST0121 = PermissibleValue(text="AOST0121",
                                       meaning=NCIT.C180358)
    AOST01P1 = PermissibleValue(text="AOST01P1",
                                       meaning=NCIT.C180359)
    AOST1321 = PermissibleValue(text="AOST1321",
                                       meaning=NCIT.C180362)
    AOST1421 = PermissibleValue(text="AOST1421",
                                       meaning=NCIT.C180363)

    _defn = EnumDefinition(
        name="StudyIdEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "AMLBFM-Registry2012",
                PermissibleValue(text="AMLBFM-Registry2012",
                                 meaning=NCIT.C173251) )
        setattr(cls, "St. Jude's Trials",
                PermissibleValue(text="St. Jude's Trials") )
        setattr(cls, "AOST0331/EURAMOS1",
                PermissibleValue(text="AOST0331/EURAMOS1",
                                 meaning=NCIT.C180361) )
        setattr(cls, "Sarcome13/OS2016",
                PermissibleValue(text="Sarcome13/OS2016",
                                 description="A Multicentre, Randomised, Open-label, Phase II trial of MEPACT combined with post-operative chemotherapy for newly diagnosed high risk osteosarcoma patients (metastatic osteosarcoma at diagnosis or localized disease with poor histological response)",
                                 meaning=NCIT.C180370) )
        setattr(cls, "CCG-7942",
                PermissibleValue(text="CCG-7942",
                                 meaning=NCIT.C180365) )
        setattr(cls, "CCG-782",
                PermissibleValue(text="CCG-782",
                                 meaning=NCIT.C180364) )

class TreatmentArmEnum(EnumDefinitionImpl):

    MAP = PermissibleValue(text="MAP",
                             description="A regimen consisting of cisplatin, doxorubicin, and methotrexate that can be used in the treatment of osteosarcoma.",
                             meaning=NCIT.C67339)
    CHEMO = PermissibleValue(text="CHEMO",
                                 description="The use of synthetic or naturally-occurring chemicals for the treatment of diseases.",
                                 meaning=NCIT.C15632)
    DOX = PermissibleValue(text="DOX",
                             description="The hydrochloride salt of doxorubicin, an anthracycline antibiotic with antineoplastic activity. Doxorubicin, isolated from the bacterium Streptomyces peucetius var. caesius, is the hydroxylated congener of daunorubicin. Doxorubicin intercalates between base pairs in the DNA helix, thereby preventing DNA replication and ultimately inhibiting protein synthesis. Additionally, doxorubicin inhibits topoisomerase II which results in an increased and stabilized cleavable enzyme-DNA linked complex during DNA replication and subsequently prevents the ligation of the nucleotide strand after double-strand breakage. Doxorubicin also forms oxygen free radicals resulting in cytotoxicity secondary to lipid peroxidation of cell membrane lipids; the formation of oxygen free radicals also contributes to the toxicity of the anthracycline antibiotics, namely the cardiac and cutaneous vascular effects.",
                             meaning=NCIT.C1326)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

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
        setattr(cls, "POSTOP-CHEMO",
                PermissibleValue(text="POSTOP-CHEMO",
                                 description="A treatment arm for patients receiving postoperative chemotherapy.",
                                 meaning=NCIT.C186775) )
        setattr(cls, "POSTOP-CHEMO-MIF",
                PermissibleValue(text="POSTOP-CHEMO-MIF",
                                 description="A treatment arm for patients receiving mifepristone as part of the postoperative chemotherapy.",
                                 meaning=NCIT.C1867763) )
        setattr(cls, "CHEMO-ZOL",
                PermissibleValue(text="CHEMO-ZOL",
                                 description="A treatment arm for patients receiving chemotherapy in combination with zoledronic acid.",
                                 meaning=NCIT.C186777) )
        setattr(cls, "REG-ACTIVE",
                PermissibleValue(text="REG-ACTIVE",
                                 description="An experimental treatment arm for patients receiving regorafenib as the active drug.",
                                 meaning=NCIT.C186778) )
        setattr(cls, "REG-PLACEBO",
                PermissibleValue(text="REG-PLACEBO",
                                 description="A control arm for patients receiving placebo instead of the experimental drug regorafenib.",
                                 meaning=NCIT.C186779) )
        setattr(cls, "DOX-IFOS",
                PermissibleValue(text="DOX-IFOS",
                                 description="A regimen consisting of doxorubicin and ifosfamide used for the treatment of unresectable soft tissue sarcoma.",
                                 meaning=NCIT.C63686) )
        setattr(cls, "AAML1031:Arm A HR",
                PermissibleValue(text="AAML1031:Arm A HR") )
        setattr(cls, "AAML1031:Arm A LR",
                PermissibleValue(text="AAML1031:Arm A LR") )
        setattr(cls, "AAML1031:Arm B HR",
                PermissibleValue(text="AAML1031:Arm B HR") )
        setattr(cls, "AAML1031:Arm B LR",
                PermissibleValue(text="AAML1031:Arm B LR") )
        setattr(cls, "AAML1031:Arm C",
                PermissibleValue(text="AAML1031:Arm C") )
        setattr(cls, "AEIOP LAM 2002:ICE-ICE-AVE-HAM- HD-AraC/SR",
                PermissibleValue(text="AEIOP LAM 2002:ICE-ICE-AVE-HAM- HD-AraC/SR") )
        setattr(cls, "AEIOP LAM 2002:ICE-ICE-AVE-HAM-SCT/HR",
                PermissibleValue(text="AEIOP LAM 2002:ICE-ICE-AVE-HAM-SCT/HR") )
        setattr(cls, "AAML0531:HR",
                PermissibleValue(text="AAML0531:HR") )
        setattr(cls, "AAML0531:LR",
                PermissibleValue(text="AAML0531:LR") )
        setattr(cls, "AAML0531:Arm A HR",
                PermissibleValue(text="AAML0531:Arm A HR") )
        setattr(cls, "AAML0531:Arm A LR",
                PermissibleValue(text="AAML0531:Arm A LR") )
        setattr(cls, "AAML0531:Arm B HR",
                PermissibleValue(text="AAML0531:Arm B HR") )
        setattr(cls, "AAML0531:Arm B LR",
                PermissibleValue(text="AAML0531:Arm B LR") )
        setattr(cls, "MRC AML12:ADE-ADE-MACE-CLASP-MidAC",
                PermissibleValue(text="MRC AML12:ADE-ADE-MACE-CLASP-MidAC") )
        setattr(cls, "MRC AML12:ADE-ADE-MACE-CLASP-SCT",
                PermissibleValue(text="MRC AML12:ADE-ADE-MACE-CLASP-SCT") )
        setattr(cls, "MRC AML12:ADE-ADE-MACE-MidAC",
                PermissibleValue(text="MRC AML12:ADE-ADE-MACE-MidAC") )
        setattr(cls, "MRC AML12:ADE-ADE-MACE-SCT",
                PermissibleValue(text="MRC AML12:ADE-ADE-MACE-SCT") )
        setattr(cls, "MRC AML12:ADE-ADE-off trial",
                PermissibleValue(text="MRC AML12:ADE-ADE-off trial") )
        setattr(cls, "MRC AML12:MAE-MAE-MACE-CLASP-MidAC",
                PermissibleValue(text="MRC AML12:MAE-MAE-MACE-CLASP-MidAC") )
        setattr(cls, "MRC AML12:MAE-MAE-MACE-CLASP-SCT",
                PermissibleValue(text="MRC AML12:MAE-MAE-MACE-CLASP-SCT") )
        setattr(cls, "MRC AML12:MAE-MAE-MACE-MidAC",
                PermissibleValue(text="MRC AML12:MAE-MAE-MACE-MidAC") )
        setattr(cls, "MRC AML12:MAE-MAE-MACE-SCT",
                PermissibleValue(text="MRC AML12:MAE-MAE-MACE-SCT") )
        setattr(cls, "MRC AML12:MAE-MAE-off trial",
                PermissibleValue(text="MRC AML12:MAE-MAE-off trial") )
        setattr(cls, "MRC AML15:ADE-ADE-MACE-MidAC-AraC",
                PermissibleValue(text="MRC AML15:ADE-ADE-MACE-MidAC-AraC") )
        setattr(cls, "MRC AML15:ADE-ADE-MACE-MidAC-No further",
                PermissibleValue(text="MRC AML15:ADE-ADE-MACE-MidAC-No further") )
        setattr(cls, "MRC AML15:ADE-ADE-MACE/Mytolarg-MidAC-AraC",
                PermissibleValue(text="MRC AML15:ADE-ADE-MACE/Mytolarg-MidAC-AraC") )
        setattr(cls, "MRC AML15:ADE-ADE-MACE/Mytolarg-MidAC-No further",
                PermissibleValue(text="MRC AML15:ADE-ADE-MACE/Mytolarg-MidAC-No further") )
        setattr(cls, "MRC AML15:ADE/Mytolarg-ADE-MACE-MidAC-AraC",
                PermissibleValue(text="MRC AML15:ADE/Mytolarg-ADE-MACE-MidAC-AraC") )
        setattr(cls, "MRC AML15:ADE/Mytolarg-ADE-MACE-MidAC-No further",
                PermissibleValue(text="MRC AML15:ADE/Mytolarg-ADE-MACE-MidAC-No further") )
        setattr(cls, "MRC AML15:ADE/Mytolarg-ADE-MACE/Mytolarg-MidAC-AraC",
                PermissibleValue(text="MRC AML15:ADE/Mytolarg-ADE-MACE/Mytolarg-MidAC-AraC") )
        setattr(cls, "MRC AML15:ADE/Mytolarg-ADE-MACE/Mytolarg-MidAC-No further",
                PermissibleValue(text="MRC AML15:ADE/Mytolarg-ADE-MACE/Mytolarg-MidAC-No further") )
        setattr(cls, "MRC AML15:ADE-ADE-AraC3g-AraC3g-AraC",
                PermissibleValue(text="MRC AML15:ADE-ADE-AraC3g-AraC3g-AraC") )
        setattr(cls, "MRC AML15:ADE-ADE-AraC3g-AraC3g-No further",
                PermissibleValue(text="MRC AML15:ADE-ADE-AraC3g-AraC3g-No further") )
        setattr(cls, "MRC AML15:ADE-ADE-AraC3g/Mytolarg-AraC3g-AraC",
                PermissibleValue(text="MRC AML15:ADE-ADE-AraC3g/Mytolarg-AraC3g-AraC") )
        setattr(cls, "MRC AML15:ADE-ADE-AraC3g/Mytolarg-AraC3g-No further",
                PermissibleValue(text="MRC AML15:ADE-ADE-AraC3g/Mytolarg-AraC3g-No further") )
        setattr(cls, "MRC AML15:ADE/Mytolarg-ADE-AraC3g-AraC3g-AraC",
                PermissibleValue(text="MRC AML15:ADE/Mytolarg-ADE-AraC3g-AraC3g-AraC") )
        setattr(cls, "MRC AML15:ADE/Mytolarg-ADE-AraC3g-AraC3g-No further",
                PermissibleValue(text="MRC AML15:ADE/Mytolarg-ADE-AraC3g-AraC3g-No further") )
        setattr(cls, "MRC AML15:ADE/Mytolarg-ADE-AraC3g/Mytolarg-AraC3g-AraC",
                PermissibleValue(text="MRC AML15:ADE/Mytolarg-ADE-AraC3g/Mytolarg-AraC3g-AraC") )
        setattr(cls, "MRC AML15:ADE/Mytolarg-ADE-AraC3g/Mytolarg-AraC3g-No further",
                PermissibleValue(text="MRC AML15:ADE/Mytolarg-ADE-AraC3g/Mytolarg-AraC3g-No further") )
        setattr(cls, "MRC AML15:FLAGIda-FLAGIda-MACE-MidAC-AraC",
                PermissibleValue(text="MRC AML15:FLAGIda-FLAGIda-MACE-MidAC-AraC") )
        setattr(cls, "MRC AML15:FLAGIda-FLAGIda-MACE-MidAC-No further",
                PermissibleValue(text="MRC AML15:FLAGIda-FLAGIda-MACE-MidAC-No further") )
        setattr(cls, "MRC AML15:FLAGIda-FLAGIda-MACE/Mytolarg-MidAC-AraC",
                PermissibleValue(text="MRC AML15:FLAGIda-FLAGIda-MACE/Mytolarg-MidAC-AraC") )
        setattr(cls, "MRC AML15:FLAGIda-FLAGIda-MACE/Mytolarg-MidAC-No further",
                PermissibleValue(text="MRC AML15:FLAGIda-FLAGIda-MACE/Mytolarg-MidAC-No further") )
        setattr(cls, "MRC AML15:FLAGIda/Mytolarg-FLAGIda-MACE-MidAC-AraC",
                PermissibleValue(text="MRC AML15:FLAGIda/Mytolarg-FLAGIda-MACE-MidAC-AraC") )
        setattr(cls, "MRC AML15:FLAGIda/Mytolarg-FLAGIda-MACE-MidAC-No further",
                PermissibleValue(text="MRC AML15:FLAGIda/Mytolarg-FLAGIda-MACE-MidAC-No further") )
        setattr(cls, "MRC AML15:FLAGIda/Mytolarg-FLAGIda-MACE/Mytolarg-MidAC-AraC",
                PermissibleValue(text="MRC AML15:FLAGIda/Mytolarg-FLAGIda-MACE/Mytolarg-MidAC-AraC") )
        setattr(cls, "MRC AML15:FLAGIda/Mytolarg-FLAGIda-MACE/Mytolarg-MidAC-No further",
                PermissibleValue(text="MRC AML15:FLAGIda/Mytolarg-FLAGIda-MACE/Mytolarg-MidAC-No further") )
        setattr(cls, "MRC AML15:FLAGIda-FLAGIda-AraC3g-AraC3g-AraC",
                PermissibleValue(text="MRC AML15:FLAGIda-FLAGIda-AraC3g-AraC3g-AraC") )
        setattr(cls, "MRC AML15:FLAGIda-FLAGIda-AraC3g-AraC3g-No further",
                PermissibleValue(text="MRC AML15:FLAGIda-FLAGIda-AraC3g-AraC3g-No further") )
        setattr(cls, "MRC AML15:FLAGIda-FLAGIda-AraC3g/Mytolarg-AraC3g-AraC",
                PermissibleValue(text="MRC AML15:FLAGIda-FLAGIda-AraC3g/Mytolarg-AraC3g-AraC") )
        setattr(cls, "MRC AML15:FLAGIda-FLAGIda-AraC3g/Mytolarg-AraC3g-No further",
                PermissibleValue(text="MRC AML15:FLAGIda-FLAGIda-AraC3g/Mytolarg-AraC3g-No further") )
        setattr(cls, "MRC AML15:FLAGIda/Mytolarg-FLAGIda-AraC3g-AraC3g-AraC",
                PermissibleValue(text="MRC AML15:FLAGIda/Mytolarg-FLAGIda-AraC3g-AraC3g-AraC") )
        setattr(cls, "MRC AML15:FLAGIda/Mytolarg-FLAGIda-AraC3g-AraC3g-No further",
                PermissibleValue(text="MRC AML15:FLAGIda/Mytolarg-FLAGIda-AraC3g-AraC3g-No further") )
        setattr(cls, "MRC AML15:FLAGIda/Mytolarg-FLAGIda-AraC3g/Mytolarg-AraC3g-AraC",
                PermissibleValue(text="MRC AML15:FLAGIda/Mytolarg-FLAGIda-AraC3g/Mytolarg-AraC3g-AraC") )
        setattr(cls, "MRC AML15:FLAGIda/Mytolarg-FLAGIda-AraC3g/Mytolarg-AraC3g-No further",
                PermissibleValue(text="MRC AML15:FLAGIda/Mytolarg-FLAGIda-AraC3g/Mytolarg-AraC3g-No further") )
        setattr(cls, "NOPHO AML 2004:AIET-AM-HA1M-HA2E-HA3-HA2E + gemtuzumab ozagamicin",
                PermissibleValue(text="NOPHO AML 2004:AIET-AM-HA1M-HA2E-HA3-HA2E + gemtuzumab ozagamicin") )
        setattr(cls, "NOPHO AML 2004:AIET-AM-HA1M-HA2E-HA3-HA2E  + no further therapy",
                PermissibleValue(text="NOPHO AML 2004:AIET-AM-HA1M-HA2E-HA3-HA2E  + no further therapy") )
        setattr(cls, "NOPHO AML 2012:MEC-ADE-HAM-HA3E-FLA",
                PermissibleValue(text="NOPHO AML 2012:MEC-ADE-HAM-HA3E-FLA") )
        setattr(cls, "NOPHO AML 2012:DEC-ADE-HAM-HA3E-FLA",
                PermissibleValue(text="NOPHO AML 2012:DEC-ADE-HAM-HA3E-FLA") )
        setattr(cls, "NOPHO AML 2012:MEC-FLAD-HAM-HA3E-FLA",
                PermissibleValue(text="NOPHO AML 2012:MEC-FLAD-HAM-HA3E-FLA") )
        setattr(cls, "NOPHO AML 2012:DEC -FLAD-HAM-HA3E-FLA",
                PermissibleValue(text="NOPHO AML 2012:DEC -FLAD-HAM-HA3E-FLA") )
        setattr(cls, "NOPHO AML 2012:MEC-ADE-HA3E-FLA (low risk)",
                PermissibleValue(text="NOPHO AML 2012:MEC-ADE-HA3E-FLA (low risk)") )
        setattr(cls, "NOPHO AML 2012:DEC -ADE-HA3E-FLA (low risk)",
                PermissibleValue(text="NOPHO AML 2012:DEC -ADE-HA3E-FLA (low risk)") )
        setattr(cls, "NOPHO AML 2012:MEC-FLAD-HA3E-FLA (low risk)",
                PermissibleValue(text="NOPHO AML 2012:MEC-FLAD-HA3E-FLA (low risk)") )
        setattr(cls, "NOPHO AML 2012:DEC -FLAD-HA3E-FLA (low risk)",
                PermissibleValue(text="NOPHO AML 2012:DEC -FLAD-HA3E-FLA (low risk)") )
        setattr(cls, "NOPHO AML 2012:MEC-ADE-HAM + SCT (high risk 1)",
                PermissibleValue(text="NOPHO AML 2012:MEC-ADE-HAM + SCT (high risk 1)") )
        setattr(cls, "NOPHO AML 2012:DEC -ADE-HAM + SCT (high risk 1)",
                PermissibleValue(text="NOPHO AML 2012:DEC -ADE-HAM + SCT (high risk 1)") )
        setattr(cls, "NOPHO AML 2012:MEC-FLAD-HAM + SCT (high risk 1)",
                PermissibleValue(text="NOPHO AML 2012:MEC-FLAD-HAM + SCT (high risk 1)") )
        setattr(cls, "NOPHO AML 2012:DEC -FLAD-HAM + SCT (high risk 1)",
                PermissibleValue(text="NOPHO AML 2012:DEC -FLAD-HAM + SCT (high risk 1)") )
        setattr(cls, "NOPHO AML 2012:MEC-ADE-HAM-HA3E + SCT (high risk 2)",
                PermissibleValue(text="NOPHO AML 2012:MEC-ADE-HAM-HA3E + SCT (high risk 2)") )
        setattr(cls, "NOPHO AML 2012:DEC -ADE-HAM-HA3E+ SCT (high risk 2)",
                PermissibleValue(text="NOPHO AML 2012:DEC -ADE-HAM-HA3E+ SCT (high risk 2)") )
        setattr(cls, "NOPHO AML 2012:MEC-FLAD-HAM-HA3E+ SCT (high risk 2)",
                PermissibleValue(text="NOPHO AML 2012:MEC-FLAD-HAM-HA3E+ SCT (high risk 2)") )
        setattr(cls, "NOPHO AML 2012:DEC -FLAD-HAM-HA3E+ SCT (high risk 2)",
                PermissibleValue(text="NOPHO AML 2012:DEC -FLAD-HAM-HA3E+ SCT (high risk 2)") )
        setattr(cls, "NOPHO AML 2012:MEC-ADE-HAM-HA3E-FLA + SCT (high risk 3)",
                PermissibleValue(text="NOPHO AML 2012:MEC-ADE-HAM-HA3E-FLA + SCT (high risk 3)") )
        setattr(cls, "NOPHO AML 2012:DEC -ADE-HAM-HA3E-FLA + SCT (high risk 3)",
                PermissibleValue(text="NOPHO AML 2012:DEC -ADE-HAM-HA3E-FLA + SCT (high risk 3)") )
        setattr(cls, "NOPHO AML 2012:MEC-FLAD-HAM-HA3E-FLA + SCT (high risk 3)",
                PermissibleValue(text="NOPHO AML 2012:MEC-FLAD-HAM-HA3E-FLA + SCT (high risk 3)") )
        setattr(cls, "NOPHO AML 2012:DEC -FLAD-HAM-HA3E-FLA + SCT (high risk 3)",
                PermissibleValue(text="NOPHO AML 2012:DEC -FLAD-HAM-HA3E-FLA + SCT (high risk 3)") )
        setattr(cls, "NOPHO AML 2012:MEC-ADE-Off protocol",
                PermissibleValue(text="NOPHO AML 2012:MEC-ADE-Off protocol") )
        setattr(cls, "NOPHO AML 2012:DEC -ADE-Off protocol",
                PermissibleValue(text="NOPHO AML 2012:DEC -ADE-Off protocol") )
        setattr(cls, "NOPHO AML 2012:MEC-FLAD- Off protocol",
                PermissibleValue(text="NOPHO AML 2012:MEC-FLAD- Off protocol") )
        setattr(cls, "NOPHO AML 2012:DEC -FLAD-Off protocol",
                PermissibleValue(text="NOPHO AML 2012:DEC -FLAD-Off protocol") )
        setattr(cls, "DB - AML01:AIET-Post recovery AM-HA2E+HA3+HA2E",
                PermissibleValue(text="DB - AML01:AIET-Post recovery AM-HA2E+HA3+HA2E") )
        setattr(cls, "DB - AML01:AIET-Post recovery FLA/Dnx-HA2E+HA3+HA2E",
                PermissibleValue(text="DB - AML01:AIET-Post recovery FLA/Dnx-HA2E+HA3+HA2E") )
        setattr(cls, "DB - AML01:AIET-Post recovery AM-Off protocl",
                PermissibleValue(text="DB - AML01:AIET-Post recovery AM-Off protocl") )
        setattr(cls, "DB - AML01:AIET-Post recovery FLA/Dnx-Off protocol",
                PermissibleValue(text="DB - AML01:AIET-Post recovery FLA/Dnx-Off protocol") )
        setattr(cls, "DB - AML01:AIET-Immediate AM-HA2E+HA3+HA2E",
                PermissibleValue(text="DB - AML01:AIET-Immediate AM-HA2E+HA3+HA2E") )
        setattr(cls, "DB - AML01:AIET-Immediate  FLA/Dnx-HA2E+HA3+HA2E",
                PermissibleValue(text="DB - AML01:AIET-Immediate  FLA/Dnx-HA2E+HA3+HA2E") )
        setattr(cls, "DB - AML01:AIET-Immediate  AM-Off protocol",
                PermissibleValue(text="DB - AML01:AIET-Immediate  AM-Off protocol") )
        setattr(cls, "DB - AML01:AIET-Immediate  FLA/Dnx-Off protocol",
                PermissibleValue(text="DB - AML01:AIET-Immediate  FLA/Dnx-Off protocol") )
        setattr(cls, "AIEOP LAM 92:ICE(3+5+10) + ICE(3+5+10) + Consolidation",
                PermissibleValue(text="AIEOP LAM 92:ICE(3+5+10) + ICE(3+5+10) + Consolidation") )
        setattr(cls, "AIEOP LAM 92:ICE(3+5+10) + ICE(2+3+7) + Consolidation",
                PermissibleValue(text="AIEOP LAM 92:ICE(3+5+10) + ICE(2+3+7) + Consolidation") )
        setattr(cls, "AIEOP LAM 92:ICE(3+5+10) + ICE(3+5+10) + Consolidation + AUTO/ALLO SCT",
                PermissibleValue(text="AIEOP LAM 92:ICE(3+5+10) + ICE(3+5+10) + Consolidation + AUTO/ALLO SCT") )
        setattr(cls, "AIEOP LAM 92:ICE(3+5+10) + ICE(2+3+7) + Consolidation + AUTO/ALLO SCT",
                PermissibleValue(text="AIEOP LAM 92:ICE(3+5+10) + ICE(2+3+7) + Consolidation + AUTO/ALLO SCT") )
        setattr(cls, "AIEOP LAM 92:ICE(3+5+10) + ICE(3+5+10) + AUTO/ALLO SCT",
                PermissibleValue(text="AIEOP LAM 92:ICE(3+5+10) + ICE(3+5+10) + AUTO/ALLO SCT") )
        setattr(cls, "AIEOP LAM 92:ICE(3+5+10) + ICE(2+3+7) + AUTO/ALLO SCT",
                PermissibleValue(text="AIEOP LAM 92:ICE(3+5+10) + ICE(2+3+7) + AUTO/ALLO SCT") )
        setattr(cls, "SCFE ELAM02:Induction + consolidation 1 + consolidation 2 + consolidation 3",
                PermissibleValue(text="SCFE ELAM02:Induction + consolidation 1 + consolidation 2 + consolidation 3") )
        setattr(cls, "SCFE ELAM02:Induction + consolidation 1 + consolidation 2 + consolidation 3 + IL2 maintenance",
                PermissibleValue(text="SCFE ELAM02:Induction + consolidation 1 + consolidation 2 + consolidation 3 + IL2 maintenance") )
        setattr(cls, "SCFE ELAM02:Induction + consolidation 1 + allo HSCT",
                PermissibleValue(text="SCFE ELAM02:Induction + consolidation 1 + allo HSCT") )
        setattr(cls, "AML-BFM 2004:ADxE- AI-haM-HAE- Standard maintenance, 12 Gy (Standard Risk arm)",
                PermissibleValue(text="AML-BFM 2004:ADxE- AI-haM-HAE- Standard maintenance, 12 Gy (Standard Risk arm)") )
        setattr(cls, "AML-BFM 2004:ADxE- AI-haM-HAE- Standard maintenance, 18 Gy(Standard Risk arm)",
                PermissibleValue(text="AML-BFM 2004:ADxE- AI-haM-HAE- Standard maintenance, 18 Gy(Standard Risk arm)") )
        setattr(cls, "AML-BFM 2004:ADxE-HAM- AI/2CDA-haM, HAE- Standard maintenance, 12 Gy (High Risk arm)",
                PermissibleValue(text="AML-BFM 2004:ADxE-HAM- AI/2CDA-haM, HAE- Standard maintenance, 12 Gy (High Risk arm)") )
        setattr(cls, "AML-BFM 2004:ADxE-HAM- AI/2CDA-haM, HAE- Standard maintenance, 18 Gy (High Risk arm)",
                PermissibleValue(text="AML-BFM 2004:ADxE-HAM- AI/2CDA-haM, HAE- Standard maintenance, 18 Gy (High Risk arm)") )
        setattr(cls, "AML-BFM 2004:ADxE-HAM- AI-haM, HAE- Standard maintenance, 12 Gy (High Risk arm)",
                PermissibleValue(text="AML-BFM 2004:ADxE-HAM- AI-haM, HAE- Standard maintenance, 12 Gy (High Risk arm)") )
        setattr(cls, "AML-BFM 2004:ADxE-HAM- AI-haM, HAE- Standard maintenance, 18 Gy (High Risk arm)",
                PermissibleValue(text="AML-BFM 2004:ADxE-HAM- AI-haM, HAE- Standard maintenance, 18 Gy (High Risk arm)") )
        setattr(cls, "AML-BFM 2004:AIE- AI-haM-HAE- Standard maintenance, 12 Gy (Standard Risk arm)",
                PermissibleValue(text="AML-BFM 2004:AIE- AI-haM-HAE- Standard maintenance, 12 Gy (Standard Risk arm)") )
        setattr(cls, "AML-BFM 2004:AIE- AI-haM-HAE- Standard maintenance, 18 Gy(Standard Risk arm)",
                PermissibleValue(text="AML-BFM 2004:AIE- AI-haM-HAE- Standard maintenance, 18 Gy(Standard Risk arm)") )
        setattr(cls, "AML-BFM 2004:AIE-HAM- AI/2CDA-haM, HAE- Standard maintenance, 12 Gy (High Risk arm)",
                PermissibleValue(text="AML-BFM 2004:AIE-HAM- AI/2CDA-haM, HAE- Standard maintenance, 12 Gy (High Risk arm)") )
        setattr(cls, "AML-BFM 2004:AIE-HAM- AI/2CDA-haM, HAE- Standard maintenance, 18 Gy (High Risk arm)",
                PermissibleValue(text="AML-BFM 2004:AIE-HAM- AI/2CDA-haM, HAE- Standard maintenance, 18 Gy (High Risk arm)") )
        setattr(cls, "AML-BFM 2004:AIE-HAM- AI-haM, HAE- Standard maintenance, 12 Gy (High Risk arm)",
                PermissibleValue(text="AML-BFM 2004:AIE-HAM- AI-haM, HAE- Standard maintenance, 12 Gy (High Risk arm)") )
        setattr(cls, "AML-BFM 2004:AIE-HAM- AI-haM, HAE- Standard maintenance, 18 Gy (High Risk arm)",
                PermissibleValue(text="AML-BFM 2004:AIE-HAM- AI-haM, HAE- Standard maintenance, 18 Gy (High Risk arm)") )
        setattr(cls, "AML-BFM 2004:AIE-HAM- AI-haM, SCT",
                PermissibleValue(text="AML-BFM 2004:AIE-HAM- AI-haM, SCT") )
        setattr(cls, "AML-BFM 2004:AIE-HAM- AI/2CDA-haM, SCT",
                PermissibleValue(text="AML-BFM 2004:AIE-HAM- AI/2CDA-haM, SCT") )
        setattr(cls, "AML-BFM 2004:ADxE-HAM- AI-haM, SCT",
                PermissibleValue(text="AML-BFM 2004:ADxE-HAM- AI-haM, SCT") )
        setattr(cls, "AML-BFM 2004:ADxE-HAM- AI/2CDA-haM, SCT",
                PermissibleValue(text="AML-BFM 2004:ADxE-HAM- AI/2CDA-haM, SCT") )
        setattr(cls, "AML BFM Registry 2012:ADxE- AI-haM-HAE- Standard maintenance (Standard Risk arm)",
                PermissibleValue(text="AML BFM Registry 2012:ADxE- AI-haM-HAE- Standard maintenance (Standard Risk arm)") )
        setattr(cls, "AML BFM Registry 2012:ADxE-HAM- AI-haM, HAE- Standard maintenance (Intermediate Risk arm)",
                PermissibleValue(text="AML BFM Registry 2012:ADxE-HAM- AI-haM, HAE- Standard maintenance (Intermediate Risk arm)") )
        setattr(cls, "AML BFM Registry 2012:ADxE-HAM- AI-haM, SCT (High risk arm)",
                PermissibleValue(text="AML BFM Registry 2012:ADxE-HAM- AI-haM, SCT (High risk arm)") )
        setattr(cls, "AML BFM 2012:CDxA- AI-haM, AI- HAE -short maintenance (Standard Risk arm)",
                PermissibleValue(text="AML BFM 2012:CDxA- AI-haM, AI- HAE -short maintenance (Standard Risk arm)") )
        setattr(cls, "AML BFM 2012:CDxA- AI-haM, AI- HAE - standard maintenance(Standard Risk arm)",
                PermissibleValue(text="AML BFM 2012:CDxA- AI-haM, AI- HAE - standard maintenance(Standard Risk arm)") )
        setattr(cls, "AML BFM 2012:CDxA- HAM- AI- haM-HAE -short maintenance (Standard Risk arm)",
                PermissibleValue(text="AML BFM 2012:CDxA- HAM- AI- haM-HAE -short maintenance (Standard Risk arm)") )
        setattr(cls, "AML BFM 2012:CDxA- HAM- AI- haM-HAE -standard maintenance(Standard Risk arm)",
                PermissibleValue(text="AML BFM 2012:CDxA- HAM- AI- haM-HAE -standard maintenance(Standard Risk arm)") )
        setattr(cls, "AML BFM 2012:ADxE - AI-haM, AI- HAE -short maintenance (Standard Risk arm)",
                PermissibleValue(text="AML BFM 2012:ADxE - AI-haM, AI- HAE -short maintenance (Standard Risk arm)") )
        setattr(cls, "AML BFM 2012:ADxE - AI-haM, AI- HAE - standard maintenance(Standard Risk arm)",
                PermissibleValue(text="AML BFM 2012:ADxE - AI-haM, AI- HAE - standard maintenance(Standard Risk arm)") )
        setattr(cls, "AML BFM 2012:ADxE - HAM- AI- haM-HAE -short maintenance (Standard Risk arm)",
                PermissibleValue(text="AML BFM 2012:ADxE - HAM- AI- haM-HAE -short maintenance (Standard Risk arm)") )
        setattr(cls, "AML BFM 2012:ADxE - HAM- AI- haM-HAE -standard maintenance(Standard Risk arm)",
                PermissibleValue(text="AML BFM 2012:ADxE - HAM- AI- haM-HAE -standard maintenance(Standard Risk arm)") )
        setattr(cls, "AML BFM 2012:CDxA-HAM- AI-haM- HAE-short maintenance (Intermediate Risk arm)",
                PermissibleValue(text="AML BFM 2012:CDxA-HAM- AI-haM- HAE-short maintenance (Intermediate Risk arm)") )
        setattr(cls, "AML BFM 2012:CDxA-HAM- AI-haM- HAE -standard maintenance (Intermediate Risk arm)",
                PermissibleValue(text="AML BFM 2012:CDxA-HAM- AI-haM- HAE -standard maintenance (Intermediate Risk arm)") )
        setattr(cls, "AML BFM 2012:ADxE- HAM- AI-haM- HAE-short maintenance (Intermediate Risk arm)",
                PermissibleValue(text="AML BFM 2012:ADxE- HAM- AI-haM- HAE-short maintenance (Intermediate Risk arm)") )
        setattr(cls, "AML BFM 2012:ADxE- HAM- AI-haM- HAE-standard maintenance (Intermediate Risk arm)",
                PermissibleValue(text="AML BFM 2012:ADxE- HAM- AI-haM- HAE-standard maintenance (Intermediate Risk arm)") )
        setattr(cls, "AML BFM 2012:CDxA- HAM Sorafenib, AI Sorafenib, haM Sorafenib, short maintenance (Intermediate Risk arm)",
                PermissibleValue(text="AML BFM 2012:CDxA- HAM Sorafenib, AI Sorafenib, haM Sorafenib, short maintenance (Intermediate Risk arm)") )
        setattr(cls, "AML BFM 2012:CDxA- HAM Sorafenib, AI Sorafenib, haM Sorafenib, standard maintenance (Intermediate Risk arm)",
                PermissibleValue(text="AML BFM 2012:CDxA- HAM Sorafenib, AI Sorafenib, haM Sorafenib, standard maintenance (Intermediate Risk arm)") )
        setattr(cls, "AML BFM 2012:CDxA- HAM Sorafenib, AI Sorafenib, haM Sorafenib, Stem Cell Transplantation (High Risk arm)",
                PermissibleValue(text="AML BFM 2012:CDxA- HAM Sorafenib, AI Sorafenib, haM Sorafenib, Stem Cell Transplantation (High Risk arm)") )
        setattr(cls, "AML BFM 2012:CDxA-HAM, AI, haM, Stem Cell Transplantation(High Risk arm)",
                PermissibleValue(text="AML BFM 2012:CDxA-HAM, AI, haM, Stem Cell Transplantation(High Risk arm)") )
        setattr(cls, "AML BFM 2012:ADxE- HAM Sorafenib, AI Sorafenib, haM Sorafenib, Stem Cell Transplantation (High Risk arm)",
                PermissibleValue(text="AML BFM 2012:ADxE- HAM Sorafenib, AI Sorafenib, haM Sorafenib, Stem Cell Transplantation (High Risk arm)") )
        setattr(cls, "AML BFM 2012:ADxE- HAM, AI, haM, Stem Cell Transplantation(High Risk arm)",
                PermissibleValue(text="AML BFM 2012:ADxE- HAM, AI, haM, Stem Cell Transplantation(High Risk arm)") )
        setattr(cls, "SJCRH AML02:HDAC-ADE+GO-C1-C2-C3",
                PermissibleValue(text="SJCRH AML02:HDAC-ADE+GO-C1-C2-C3",
                                 description="Rubnitz et al, 2010") )
        setattr(cls, "SJCRH AML02:HDAC-ADE-C1-C2-C3",
                PermissibleValue(text="SJCRH AML02:HDAC-ADE-C1-C2-C3",
                                 description="Rubnitz et al, 2010") )
        setattr(cls, "SJCRH AML02:HDAC-ADE+GO-SCT",
                PermissibleValue(text="SJCRH AML02:HDAC-ADE+GO-SCT",
                                 description="Rubnitz et al, 2010") )
        setattr(cls, "SJCRH AML02:HDAC-ADE-SCT",
                PermissibleValue(text="SJCRH AML02:HDAC-ADE-SCT",
                                 description="Rubnitz et al, 2010") )
        setattr(cls, "SJCRH AML02:LDAC-ADE+GO-C1-C2-C3",
                PermissibleValue(text="SJCRH AML02:LDAC-ADE+GO-C1-C2-C3",
                                 description="Rubnitz et al, 2010") )
        setattr(cls, "SJCRH AML02:LDAC-ADE-C1-C2-C3",
                PermissibleValue(text="SJCRH AML02:LDAC-ADE-C1-C2-C3",
                                 description="Rubnitz et al, 2010") )
        setattr(cls, "SJCRH AML02:LDAC-ADE+GO-SCT",
                PermissibleValue(text="SJCRH AML02:LDAC-ADE+GO-SCT",
                                 description="Rubnitz et al, 2010") )
        setattr(cls, "SJCRH AML02:LDAC-ADE-SCT",
                PermissibleValue(text="SJCRH AML02:LDAC-ADE-SCT",
                                 description="Rubnitz et al, 2010") )
        setattr(cls, "PPLLSG AML-98:SR",
                PermissibleValue(text="PPLLSG AML-98:SR",
                                 description="Dluzniewska et al, 2005") )
        setattr(cls, "PPLLSG AML-98:HR",
                PermissibleValue(text="PPLLSG AML-98:HR",
                                 description="Dluzniewska et al, 2005") )
        setattr(cls, "JPLSG AML99:JACLS",
                PermissibleValue(text="JPLSG AML99:JACLS",
                                 description="Tsukimoto et al, 2009") )
        setattr(cls, "JPLSG AML05:JACLS",
                PermissibleValue(text="JPLSG AML05:JACLS",
                                 description="Tomizawa et al, 2013") )
        setattr(cls, "AEWS0031:3W-VDC-MESNA+IFO-GCSF",
                PermissibleValue(text="AEWS0031:3W-VDC-MESNA+IFO-GCSF",
                                 description="Regimen A",
                                 meaning=NCIT.C174975) )
        setattr(cls, "AEWS0031:2W-VDC-MESNA+IFO-GCSF",
                PermissibleValue(text="AEWS0031:2W-VDC-MESNA+IFO-GCSF",
                                 description="Regimen B",
                                 meaning=NCIT.C174976) )
        setattr(cls, "AEWS1221:VDC/IE",
                PermissibleValue(text="AEWS1221:VDC/IE",
                                 description="Regimen A",
                                 meaning=NCIT.C174977) )
        setattr(cls, "AEWS1221:VDC/IE+Ganitumab",
                PermissibleValue(text="AEWS1221:VDC/IE+Ganitumab",
                                 description="Regimen B",
                                 meaning=NCIT.C174978) )
        setattr(cls, "AEWS0331:VIDE-Surgery-R1-VAI-VAC/VAI",
                PermissibleValue(text="AEWS0331:VIDE-Surgery-R1-VAI-VAC/VAI",
                                 description="Group 1",
                                 meaning=NCIT.C174979) )
        setattr(cls, "AEWS0331:VIDE-Surgery-R2-VAI-VAI/BuMel",
                PermissibleValue(text="AEWS0331:VIDE-Surgery-R2-VAI-VAI/BuMel",
                                 description="Group 2, Arm I",
                                 meaning=NCIT.C174980) )
        setattr(cls, "AEWS0331:VIDE-Surgery-R3-VAI-MEME/TreoMel/BuMel/P2",
                PermissibleValue(text="AEWS0331:VIDE-Surgery-R3-VAI-MEME/TreoMel/BuMel/P2",
                                 description="Group 2, Arm II",
                                 meaning=NCIT.C174981) )
        setattr(cls, "AEWS1031:VIDEC",
                PermissibleValue(text="AEWS1031:VIDEC",
                                 description="Regimen A",
                                 meaning=NCIT.C174982) )
        setattr(cls, "AEWS1031:VIDEC+Topotecan",
                PermissibleValue(text="AEWS1031:VIDEC+Topotecan",
                                 description="Regimen B",
                                 meaning=NCIT.C174983) )
        setattr(cls, "EICESS92:SR/VAIA",
                PermissibleValue(text="EICESS92:SR/VAIA",
                                 description="Regimen A, Arm I",
                                 meaning=NCIT.C174984) )
        setattr(cls, "EICESS92:SR/VACA",
                PermissibleValue(text="EICESS92:SR/VACA",
                                 description="Regimen A, Arm II",
                                 meaning=NCIT.C174985) )
        setattr(cls, "EICESS92:HR/VAIA",
                PermissibleValue(text="EICESS92:HR/VAIA",
                                 description="Regimen B, Arm I",
                                 meaning=NCIT.C174986) )
        setattr(cls, "EICESS92:HR/EVAIA",
                PermissibleValue(text="EICESS92:HR/EVAIA",
                                 description="Regimen B, Arm II",
                                 meaning=NCIT.C174987) )
        setattr(cls, "AEWS07P1:VAIA-VACA",
                PermissibleValue(text="AEWS07P1:VAIA-VACA",
                                 description="Arm A",
                                 meaning=NCIT.C174988) )
        setattr(cls, "AEWS07P1:VAIA-VAIA",
                PermissibleValue(text="AEWS07P1:VAIA-VAIA",
                                 description="Arm B",
                                 meaning=NCIT.C174989) )
        setattr(cls, "AEWS07P1:EVAIA-EVAIA",
                PermissibleValue(text="AEWS07P1:EVAIA-EVAIA",
                                 description="Arm C",
                                 meaning=NCIT.C174990) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

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

class EfsCensorStatusEnum(EnumDefinitionImpl):

    Censored = PermissibleValue(text="Censored",
                                       description="Subject is censored (i.e. has had no events(s))")
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="EfsCensorStatusEnum",
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
        setattr(cls, "Delayed Intensification",
                PermissibleValue(text="Delayed Intensification",
                                 description="A repeat of the first two months of induction and consolidation chemotherapy in high-risk and very-high-risk ALL protocols with the goal of eliminating residual drug-resistant cells",
                                 meaning=NCIT.C178270) )
        setattr(cls, "Interim Maintenance",
                PermissibleValue(text="Interim Maintenance",
                                 description="A less intense phase of chemotherapy in between each course of delayed intensification.",
                                 meaning=NCIT.C178069) )
        setattr(cls, "Post-Consolidation",
                PermissibleValue(text="Post-Consolidation",
                                 description="  ") )
        setattr(cls, "Palliative Treatment",
                PermissibleValue(text="Palliative Treatment",
                                 description="The patient- and family-centered active holistic care of patients with advanced, progressive disease. Essential components of Palliative Care are: pain and symptom control, communication regarding treatment and alternatives, prognosis, and available services, rehabilitation services, care that addresses treatment and palliative concerns, intellectual, emotional, social, and spiritual needs, terminal care, support in bereavement. The goal of Palliative Care is an achievement of the best quality of life for patients and their families.",
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

# Slots
class slots:
    pass

slots.submitter_id = Slot(uri=DEFAULT_.submitter_id, name="submitter_id", curie=DEFAULT_.curie('submitter_id'),
                   model_uri=DEFAULT_.submitter_id, domain=None, range=str)

slots.type = Slot(uri=DEFAULT_.type, name="type", curie=DEFAULT_.curie('type'),
                   model_uri=DEFAULT_.type, domain=None, range=str)

slots.sex = Slot(uri=DEFAULT_.sex, name="sex", curie=DEFAULT_.curie('sex'),
                   model_uri=DEFAULT_.sex, domain=None, range=Optional[Union[str, "SexEnum"]])

slots.race = Slot(uri=DEFAULT_.race, name="race", curie=DEFAULT_.curie('race'),
                   model_uri=DEFAULT_.race, domain=None, range=Optional[Union[str, "RaceEnum"]])

slots.race_other = Slot(uri=DEFAULT_.race_other, name="race_other", curie=DEFAULT_.curie('race_other'),
                   model_uri=DEFAULT_.race_other, domain=None, range=Optional[str])

slots.ethnicity = Slot(uri=DEFAULT_.ethnicity, name="ethnicity", curie=DEFAULT_.curie('ethnicity'),
                   model_uri=DEFAULT_.ethnicity, domain=None, range=Optional[Union[str, "EthnicityEnum"]])

slots.prior_cancer = Slot(uri=DEFAULT_.prior_cancer, name="prior_cancer", curie=DEFAULT_.curie('prior_cancer'),
                   model_uri=DEFAULT_.prior_cancer, domain=None, range=Optional[Union[str, "PriorCancerEnum"]])

slots.relation = Slot(uri=DEFAULT_.relation, name="relation", curie=DEFAULT_.curie('relation'),
                   model_uri=DEFAULT_.relation, domain=None, range=Optional[Union[str, "RelationEnum"]])

slots.prior_cancer_type = Slot(uri=DEFAULT_.prior_cancer_type, name="prior_cancer_type", curie=DEFAULT_.curie('prior_cancer_type'),
                   model_uri=DEFAULT_.prior_cancer_type, domain=None, range=Optional[str])

slots.honest_broker_subject_id = Slot(uri=DEFAULT_.honest_broker_subject_id, name="honest_broker_subject_id", curie=DEFAULT_.curie('honest_broker_subject_id'),
                   model_uri=DEFAULT_.honest_broker_subject_id, domain=None, range=Optional[str])

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
                   model_uri=DEFAULT_.efs_censor_status, domain=None, range=Optional[Union[str, "EfsCensorStatusEnum"]])

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

slots.disease_phase = Slot(uri=DEFAULT_.disease_phase, name="disease_phase", curie=DEFAULT_.curie('disease_phase'),
                   model_uri=DEFAULT_.disease_phase, domain=None, range=Optional[Union[str, "DiseasePhaseEnum"]])

slots.disease_phase_number = Slot(uri=DEFAULT_.disease_phase_number, name="disease_phase_number", curie=DEFAULT_.curie('disease_phase_number'),
                   model_uri=DEFAULT_.disease_phase_number, domain=None, range=Optional[int])

slots.age_at_disease_phase = Slot(uri=DEFAULT_.age_at_disease_phase, name="age_at_disease_phase", curie=DEFAULT_.curie('age_at_disease_phase'),
                   model_uri=DEFAULT_.age_at_disease_phase, domain=None, range=Optional[int])

slots.year_at_disease_phase = Slot(uri=DEFAULT_.year_at_disease_phase, name="year_at_disease_phase", curie=DEFAULT_.curie('year_at_disease_phase'),
                   model_uri=DEFAULT_.year_at_disease_phase, domain=None, range=Optional[int])

slots.course = Slot(uri=DEFAULT_.course, name="course", curie=DEFAULT_.curie('course'),
                   model_uri=DEFAULT_.course, domain=None, range=Optional[Union[str, "CourseEnum"]])

slots.course_number = Slot(uri=DEFAULT_.course_number, name="course_number", curie=DEFAULT_.curie('course_number'),
                   model_uri=DEFAULT_.course_number, domain=None, range=Optional[int])

slots.age_at_course_start = Slot(uri=DEFAULT_.age_at_course_start, name="age_at_course_start", curie=DEFAULT_.curie('age_at_course_start'),
                   model_uri=DEFAULT_.age_at_course_start, domain=None, range=Optional[int])

slots.age_at_course_end = Slot(uri=DEFAULT_.age_at_course_end, name="age_at_course_end", curie=DEFAULT_.curie('age_at_course_end'),
                   model_uri=DEFAULT_.age_at_course_end, domain=None, range=Optional[int])

slots.age_at_txassign = Slot(uri=DEFAULT_.age_at_txassign, name="age_at_txassign", curie=DEFAULT_.curie('age_at_txassign'),
                   model_uri=DEFAULT_.age_at_txassign, domain=None, range=Optional[int])

slots.age_at_course_anc_500 = Slot(uri=DEFAULT_.age_at_course_anc_500, name="age_at_course_anc_500", curie=DEFAULT_.curie('age_at_course_anc_500'),
                   model_uri=DEFAULT_.age_at_course_anc_500, domain=None, range=Optional[int])

slots.cycle_number = Slot(uri=DEFAULT_.cycle_number, name="cycle_number", curie=DEFAULT_.curie('cycle_number'),
                   model_uri=DEFAULT_.cycle_number, domain=None, range=Optional[int])

slots.age_at_cycle_start = Slot(uri=DEFAULT_.age_at_cycle_start, name="age_at_cycle_start", curie=DEFAULT_.curie('age_at_cycle_start'),
                   model_uri=DEFAULT_.age_at_cycle_start, domain=None, range=Optional[int])

slots.age_at_cycle_end = Slot(uri=DEFAULT_.age_at_cycle_end, name="age_at_cycle_end", curie=DEFAULT_.curie('age_at_cycle_end'),
                   model_uri=DEFAULT_.age_at_cycle_end, domain=None, range=Optional[int])
