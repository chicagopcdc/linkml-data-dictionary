# Auto generated from data_dictionary_spreadsheet_1k2m4oAX3JdfYN2lIbpBiWFUNKZwXnQCiuns0e3Wid9o.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-29T16:21:14
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
from linkml_runtime.linkml_model.types import Decimal, Integer, String
from linkml_runtime.utils.metamodelcore import Decimal

metamodel_version = "1.7.0"
version = "0.0.1"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
HGNC = CurieNamespace('HGNC', 'https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:')
SO = CurieNamespace('SO', 'http://http://www.sequenceontology.org/browser/current_release/term/SO:')
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
class Subject(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/Subject"]
    class_class_curie: ClassVar[str] = "pcdc:/Subject"
    class_name: ClassVar[str] = "Subject"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/Subject")

    submitter_id: str = None
    type: str = None
    persons: Union[dict, Person] = None
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
        if self._is_empty(self.persons):
            self.MissingRequiredField("persons")
        if not isinstance(self.persons, Person):
            self.persons = Person(**as_dict(self.persons))

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
    subjects: Union[Union[dict, Subject], List[Union[dict, Subject]]] = None
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
    timings: Optional[Union[dict, "Timing"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subjects):
            self.MissingRequiredField("subjects")
        self._normalize_inlined_as_dict(slot_name="subjects", slot_type=Subject, key_name="submitter_id", keyed=False)

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

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        super().__post_init__(**kwargs)


@dataclass
class SubjectCharacteristics(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/SubjectCharacteristics"]
    class_class_curie: ClassVar[str] = "pcdc:/SubjectCharacteristics"
    class_name: ClassVar[str] = "SubjectCharacteristics"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/SubjectCharacteristics")

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
class OffProtocolTherapyOrStudy(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/OffProtocolTherapyOrStudy"]
    class_class_curie: ClassVar[str] = "pcdc:/OffProtocolTherapyOrStudy"
    class_name: ClassVar[str] = "OffProtocolTherapyOrStudy"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/OffProtocolTherapyOrStudy")

    submitter_id: str = None
    type: str = None
    age_off: Optional[int] = None
    timings: Optional[Union[dict, Timing]] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    off_type: Optional[Union[str, "OffTypeEnum"]] = None
    reason_off: Optional[Union[str, "ReasonOffEnum"]] = None
    reason_off_other: Optional[str] = None
    another_study: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_off is not None and not isinstance(self.age_off, int):
            self.age_off = int(self.age_off)

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.off_type is not None and not isinstance(self.off_type, OffTypeEnum):
            self.off_type = OffTypeEnum(self.off_type)

        if self.reason_off is not None and not isinstance(self.reason_off, ReasonOffEnum):
            self.reason_off = ReasonOffEnum(self.reason_off)

        if self.reason_off_other is not None and not isinstance(self.reason_off_other, str):
            self.reason_off_other = str(self.reason_off_other)

        if self.another_study is not None and not isinstance(self.another_study, NoNotreportedUnknownYesEnum):
            self.another_study = NoNotreportedUnknownYesEnum(self.another_study)

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
    subjects: Union[Union[dict, Subject], List[Union[dict, Subject]]] = None
    prior_cancer: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    relation: Optional[Union[str, "RelationEnum"]] = None
    prior_cancer_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subjects):
            self.MissingRequiredField("subjects")
        self._normalize_inlined_as_dict(slot_name="subjects", slot_type=Subject, key_name="submitter_id", keyed=False)

        if self.prior_cancer is not None and not isinstance(self.prior_cancer, NoNotreportedUnknownYesEnum):
            self.prior_cancer = NoNotreportedUnknownYesEnum(self.prior_cancer)

        if self.relation is not None and not isinstance(self.relation, RelationEnum):
            self.relation = RelationEnum(self.relation)

        if self.prior_cancer_type is not None and not isinstance(self.prior_cancer_type, str):
            self.prior_cancer_type = str(self.prior_cancer_type)

        super().__post_init__(**kwargs)


@dataclass
class MedicalHistory(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/MedicalHistory"]
    class_class_curie: ClassVar[str] = "pcdc:/MedicalHistory"
    class_name: ClassVar[str] = "MedicalHistory"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/MedicalHistory")

    submitter_id: str = None
    type: str = None
    condition: Optional[Union[str, "ConditionEnum"]] = None
    condition_other: Optional[str] = None
    condition_type: Optional[Union[str, "ConditionTypeEnum"]] = None
    condition_status: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    assisted_conception: Optional[Union[str, "AssistedConceptionEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.condition is not None and not isinstance(self.condition, ConditionEnum):
            self.condition = ConditionEnum(self.condition)

        if self.condition_other is not None and not isinstance(self.condition_other, str):
            self.condition_other = str(self.condition_other)

        if self.condition_type is not None and not isinstance(self.condition_type, ConditionTypeEnum):
            self.condition_type = ConditionTypeEnum(self.condition_type)

        if self.condition_status is not None and not isinstance(self.condition_status, NoNotreportedUnknownYesEnum):
            self.condition_status = NoNotreportedUnknownYesEnum(self.condition_status)

        if self.assisted_conception is not None and not isinstance(self.assisted_conception, AssistedConceptionEnum):
            self.assisted_conception = AssistedConceptionEnum(self.assisted_conception)

        super().__post_init__(**kwargs)


@dataclass
class SurvivalCharacteristics(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/SurvivalCharacteristics"]
    class_class_curie: ClassVar[str] = "pcdc:/SurvivalCharacteristics"
    class_name: ClassVar[str] = "SurvivalCharacteristics"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/SurvivalCharacteristics")

    submitter_id: str = None
    type: str = None
    age_at_lkss: Optional[int] = None
    timings: Optional[Union[dict, Timing]] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    lkss: Optional[Union[str, "LkssEnum"]] = None
    lkss_with_disease: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    age_lost_to_follow_up: Optional[int] = None
    cause_of_death: Optional[Union[str, "CauseOfDeathEnum"]] = None
    trm_type: Optional[Union[str, "TrmTypeEnum"]] = None
    trm_type_other: Optional[str] = None
    cause_of_death_detail: Optional[Union[str, "CauseOfDeathDetailEnum"]] = None
    cause_of_death_detail_other: Optional[str] = None
    cause_of_death_ranking: Optional[Union[str, "CauseOfDeathRankingEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_at_lkss is not None and not isinstance(self.age_at_lkss, int):
            self.age_at_lkss = int(self.age_at_lkss)

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.lkss is not None and not isinstance(self.lkss, LkssEnum):
            self.lkss = LkssEnum(self.lkss)

        if self.lkss_with_disease is not None and not isinstance(self.lkss_with_disease, NoNotreportedUnknownYesEnum):
            self.lkss_with_disease = NoNotreportedUnknownYesEnum(self.lkss_with_disease)

        if self.age_lost_to_follow_up is not None and not isinstance(self.age_lost_to_follow_up, int):
            self.age_lost_to_follow_up = int(self.age_lost_to_follow_up)

        if self.cause_of_death is not None and not isinstance(self.cause_of_death, CauseOfDeathEnum):
            self.cause_of_death = CauseOfDeathEnum(self.cause_of_death)

        if self.trm_type is not None and not isinstance(self.trm_type, TrmTypeEnum):
            self.trm_type = TrmTypeEnum(self.trm_type)

        if self.trm_type_other is not None and not isinstance(self.trm_type_other, str):
            self.trm_type_other = str(self.trm_type_other)

        if self.cause_of_death_detail is not None and not isinstance(self.cause_of_death_detail, CauseOfDeathDetailEnum):
            self.cause_of_death_detail = CauseOfDeathDetailEnum(self.cause_of_death_detail)

        if self.cause_of_death_detail_other is not None and not isinstance(self.cause_of_death_detail_other, str):
            self.cause_of_death_detail_other = str(self.cause_of_death_detail_other)

        if self.cause_of_death_ranking is not None and not isinstance(self.cause_of_death_ranking, CauseOfDeathRankingEnum):
            self.cause_of_death_ranking = CauseOfDeathRankingEnum(self.cause_of_death_ranking)

        super().__post_init__(**kwargs)


@dataclass
class VitalsAndAnthropometrics(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/VitalsAndAnthropometrics"]
    class_class_curie: ClassVar[str] = "pcdc:/VitalsAndAnthropometrics"
    class_name: ClassVar[str] = "VitalsAndAnthropometrics"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/VitalsAndAnthropometrics")

    submitter_id: str = None
    type: str = None
    age_at_measurement: Optional[int] = None
    timings: Optional[Union[dict, Timing]] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    measurement_type: Optional[Union[str, "MeasurementTypeEnum"]] = None
    measurement: Optional[str] = None
    measurement_numeric: Optional[int] = None
    measurement_unit: Optional[Union[str, "MeasurementUnitEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_at_measurement is not None and not isinstance(self.age_at_measurement, int):
            self.age_at_measurement = int(self.age_at_measurement)

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.measurement_type is not None and not isinstance(self.measurement_type, MeasurementTypeEnum):
            self.measurement_type = MeasurementTypeEnum(self.measurement_type)

        if self.measurement is not None and not isinstance(self.measurement, str):
            self.measurement = str(self.measurement)

        if self.measurement_numeric is not None and not isinstance(self.measurement_numeric, int):
            self.measurement_numeric = int(self.measurement_numeric)

        if self.measurement_unit is not None and not isinstance(self.measurement_unit, MeasurementUnitEnum):
            self.measurement_unit = MeasurementUnitEnum(self.measurement_unit)

        super().__post_init__(**kwargs)


@dataclass
class FunctionTest(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/FunctionTest"]
    class_class_curie: ClassVar[str] = "pcdc:/FunctionTest"
    class_name: ClassVar[str] = "FunctionTest"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/FunctionTest")

    submitter_id: str = None
    type: str = None
    age_at_function_test: Optional[int] = None
    timings: Optional[Union[dict, Timing]] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    function_category: Optional[Union[str, "FunctionCategoryEnum"]] = None
    function_test: Optional[Union[str, "FunctionTestEnum"]] = None
    function_result: Optional[str] = None
    function_result_numeric: Optional[int] = None
    function_result_unit: Optional[Union[str, "FunctionResultUnitEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_at_function_test is not None and not isinstance(self.age_at_function_test, int):
            self.age_at_function_test = int(self.age_at_function_test)

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.function_category is not None and not isinstance(self.function_category, FunctionCategoryEnum):
            self.function_category = FunctionCategoryEnum(self.function_category)

        if self.function_test is not None and not isinstance(self.function_test, FunctionTestEnum):
            self.function_test = FunctionTestEnum(self.function_test)

        if self.function_result is not None and not isinstance(self.function_result, str):
            self.function_result = str(self.function_result)

        if self.function_result_numeric is not None and not isinstance(self.function_result_numeric, int):
            self.function_result_numeric = int(self.function_result_numeric)

        if self.function_result_unit is not None and not isinstance(self.function_result_unit, FunctionResultUnitEnum):
            self.function_result_unit = FunctionResultUnitEnum(self.function_result_unit)

        super().__post_init__(**kwargs)


@dataclass
class LaboratoryTest(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/LaboratoryTest"]
    class_class_curie: ClassVar[str] = "pcdc:/LaboratoryTest"
    class_name: ClassVar[str] = "LaboratoryTest"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/LaboratoryTest")

    submitter_id: str = None
    type: str = None
    age_at_lab: Optional[int] = None
    timings: Optional[Union[dict, Timing]] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    lab_category: Optional[Union[str, "LabCategoryEnum"]] = None
    lab_test: Optional[Union[str, "LabTestEnum"]] = None
    lab_test_other: Optional[str] = None
    specimen: Optional[Union[str, "SpecimenEnum"]] = None
    specimen_other: Optional[str] = None
    lab_result: Optional[str] = None
    lab_result_categorical: Optional[Union[str, "LabResultCategoricalEnum"]] = None
    lab_result_numeric: Optional[int] = None
    lab_result_unit: Optional[Union[str, "LabResultUnitEnum"]] = None
    lab_method: Optional[Union[str, "LabMethodEnum"]] = None
    lab_seq_method: Optional[Union[str, "LabSeqMethodEnum"]] = None
    threshold_high: Optional[int] = None
    threshold_low: Optional[int] = None
    pmid_ref: Optional[int] = None
    bm_morphology: Optional[Union[str, "BmMorphologyEnum"]] = None
    traumatic_tap: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_at_lab is not None and not isinstance(self.age_at_lab, int):
            self.age_at_lab = int(self.age_at_lab)

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.lab_category is not None and not isinstance(self.lab_category, LabCategoryEnum):
            self.lab_category = LabCategoryEnum(self.lab_category)

        if self.lab_test is not None and not isinstance(self.lab_test, LabTestEnum):
            self.lab_test = LabTestEnum(self.lab_test)

        if self.lab_test_other is not None and not isinstance(self.lab_test_other, str):
            self.lab_test_other = str(self.lab_test_other)

        if self.specimen is not None and not isinstance(self.specimen, SpecimenEnum):
            self.specimen = SpecimenEnum(self.specimen)

        if self.specimen_other is not None and not isinstance(self.specimen_other, str):
            self.specimen_other = str(self.specimen_other)

        if self.lab_result is not None and not isinstance(self.lab_result, str):
            self.lab_result = str(self.lab_result)

        if self.lab_result_categorical is not None and not isinstance(self.lab_result_categorical, LabResultCategoricalEnum):
            self.lab_result_categorical = LabResultCategoricalEnum(self.lab_result_categorical)

        if self.lab_result_numeric is not None and not isinstance(self.lab_result_numeric, int):
            self.lab_result_numeric = int(self.lab_result_numeric)

        if self.lab_result_unit is not None and not isinstance(self.lab_result_unit, LabResultUnitEnum):
            self.lab_result_unit = LabResultUnitEnum(self.lab_result_unit)

        if self.lab_method is not None and not isinstance(self.lab_method, LabMethodEnum):
            self.lab_method = LabMethodEnum(self.lab_method)

        if self.lab_seq_method is not None and not isinstance(self.lab_seq_method, LabSeqMethodEnum):
            self.lab_seq_method = LabSeqMethodEnum(self.lab_seq_method)

        if self.threshold_high is not None and not isinstance(self.threshold_high, int):
            self.threshold_high = int(self.threshold_high)

        if self.threshold_low is not None and not isinstance(self.threshold_low, int):
            self.threshold_low = int(self.threshold_low)

        if self.pmid_ref is not None and not isinstance(self.pmid_ref, int):
            self.pmid_ref = int(self.pmid_ref)

        if self.bm_morphology is not None and not isinstance(self.bm_morphology, BmMorphologyEnum):
            self.bm_morphology = BmMorphologyEnum(self.bm_morphology)

        if self.traumatic_tap is not None and not isinstance(self.traumatic_tap, NoNotreportedUnknownYesEnum):
            self.traumatic_tap = NoNotreportedUnknownYesEnum(self.traumatic_tap)

        super().__post_init__(**kwargs)


@dataclass
class Imaging(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/Imaging"]
    class_class_curie: ClassVar[str] = "pcdc:/Imaging"
    class_name: ClassVar[str] = "Imaging"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/Imaging")

    submitter_id: str = None
    type: str = None
    age_at_imaging: Optional[int] = None
    timings: Optional[Union[dict, Timing]] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    imaging_method: Optional[Union[str, "ImagingMethodEnum"]] = None
    imaging_result: Optional[Union[str, "ImagingResultEnum"]] = None
    deauville_score: Optional[Union[str, "DeauvilleScoreEnum"]] = None
    qpet_score: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_at_imaging is not None and not isinstance(self.age_at_imaging, int):
            self.age_at_imaging = int(self.age_at_imaging)

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.imaging_method is not None and not isinstance(self.imaging_method, ImagingMethodEnum):
            self.imaging_method = ImagingMethodEnum(self.imaging_method)

        if self.imaging_result is not None and not isinstance(self.imaging_result, ImagingResultEnum):
            self.imaging_result = ImagingResultEnum(self.imaging_result)

        if self.deauville_score is not None and not isinstance(self.deauville_score, DeauvilleScoreEnum):
            self.deauville_score = DeauvilleScoreEnum(self.deauville_score)

        if self.qpet_score is not None and not isinstance(self.qpet_score, int):
            self.qpet_score = int(self.qpet_score)

        super().__post_init__(**kwargs)


@dataclass
class Cytology(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/Cytology"]
    class_class_curie: ClassVar[str] = "pcdc:/Cytology"
    class_name: ClassVar[str] = "Cytology"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/Cytology")

    submitter_id: str = None
    type: str = None
    age_at_cytology: Optional[int] = None
    timings: Optional[Union[dict, Timing]] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    malignant_cells: Optional[Union[str, "AbsentNotreportedPresentUnknownEnum"]] = None
    cytology_spec_type: Optional[Union[str, "CytologySpecTypeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_at_cytology is not None and not isinstance(self.age_at_cytology, int):
            self.age_at_cytology = int(self.age_at_cytology)

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.malignant_cells is not None and not isinstance(self.malignant_cells, AbsentNotreportedPresentUnknownEnum):
            self.malignant_cells = AbsentNotreportedPresentUnknownEnum(self.malignant_cells)

        if self.cytology_spec_type is not None and not isinstance(self.cytology_spec_type, CytologySpecTypeEnum):
            self.cytology_spec_type = CytologySpecTypeEnum(self.cytology_spec_type)

        super().__post_init__(**kwargs)


@dataclass
class Immunohistochemistry(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/Immunohistochemistry"]
    class_class_curie: ClassVar[str] = "pcdc:/Immunohistochemistry"
    class_name: ClassVar[str] = "Immunohistochemistry"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/Immunohistochemistry")

    submitter_id: str = None
    type: str = None
    age_at_ihc: Optional[int] = None
    timings: Optional[Union[dict, Timing]] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    ihc_test: Optional[Union[str, "IhcTestEnum"]] = None
    ihc_spec_type: Optional[Union[str, "IhcSpecTypeEnum"]] = None
    ihc_result: Optional[str] = None
    ihc_result_numeric: Optional[int] = None
    ihc_result_unit: Optional[Union[str, "IhcResultUnitEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_at_ihc is not None and not isinstance(self.age_at_ihc, int):
            self.age_at_ihc = int(self.age_at_ihc)

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.ihc_test is not None and not isinstance(self.ihc_test, IhcTestEnum):
            self.ihc_test = IhcTestEnum(self.ihc_test)

        if self.ihc_spec_type is not None and not isinstance(self.ihc_spec_type, IhcSpecTypeEnum):
            self.ihc_spec_type = IhcSpecTypeEnum(self.ihc_spec_type)

        if self.ihc_result is not None and not isinstance(self.ihc_result, str):
            self.ihc_result = str(self.ihc_result)

        if self.ihc_result_numeric is not None and not isinstance(self.ihc_result_numeric, int):
            self.ihc_result_numeric = int(self.ihc_result_numeric)

        if self.ihc_result_unit is not None and not isinstance(self.ihc_result_unit, IhcResultUnitEnum):
            self.ihc_result_unit = IhcResultUnitEnum(self.ihc_result_unit)

        super().__post_init__(**kwargs)


@dataclass
class GeneticAnalysis(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/GeneticAnalysis"]
    class_class_curie: ClassVar[str] = "pcdc:/GeneticAnalysis"
    class_name: ClassVar[str] = "GeneticAnalysis"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/GeneticAnalysis")

    submitter_id: str = None
    type: str = None
    age_at_genetic_analysis: Optional[int] = None
    timings: Optional[Union[dict, Timing]] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    lesion_classification: Optional[Union[str, "LesionClassificationEnum"]] = None
    method: Optional[Union[str, "MethodEnum"]] = None
    specimen: Optional[Union[str, "SpecimenEnum"]] = None
    genomic_source_class: Optional[Union[str, "GenomicSourceClassEnum"]] = None
    common_name: Optional[Union[str, "CommonNameEnum"]] = None
    status: Optional[Union[str, "StatusEnum"]] = None
    gene: Optional[str] = None
    chromosome: Optional[str] = None
    mutation_type: Optional[Union[str, "MutationTypeEnum"]] = None
    mutation_type_other: Optional[str] = None
    expression_consequence: Optional[Union[str, "ExpressionConsequenceEnum"]] = None
    chromosomal_consequence: Optional[Union[str, "ChromosomalConsequenceEnum"]] = None
    genomic_region: Optional[Union[str, "GenomicRegionEnum"]] = None
    allelic_state: Optional[Union[str, "AllelicStateEnum"]] = None
    inheritance_pattern: Optional[Union[str, "InheritancePatternEnum"]] = None
    parental_status: Optional[Union[str, "ParentalStatusEnum"]] = None
    hgvs_coding: Optional[str] = None
    hgvs_protein: Optional[str] = None
    iscn: Optional[str] = None
    clingen_id: Optional[str] = None
    copy_number_variation: Optional[Union[str, "CopyNumberVariationEnum"]] = None
    copy_number: Optional[int] = None
    amplification: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    allelic_frequency: Optional[int] = None
    gene2: Optional[str] = None
    mosaicism: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    mosaicism_percent: Optional[int] = None
    alt_status: Optional[Union[str, "AltStatusEnum"]] = None
    total_chromosomes: Optional[int] = None
    independent_aberations: Optional[int] = None
    cells_in_metaphase: Optional[int] = None
    karyotype_status: Optional[Union[str, "KaryotypeStatusEnum"]] = None
    dna_index: Optional[Union[str, "DnaIndexEnum"]] = None
    dna_index_numeric: Optional[int] = None
    cytodifferentiation: Optional[Union[str, "CytodifferentiationEnum"]] = None
    mitotic_rate: Optional[Union[str, "MitoticRateEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_at_genetic_analysis is not None and not isinstance(self.age_at_genetic_analysis, int):
            self.age_at_genetic_analysis = int(self.age_at_genetic_analysis)

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.lesion_classification is not None and not isinstance(self.lesion_classification, LesionClassificationEnum):
            self.lesion_classification = LesionClassificationEnum(self.lesion_classification)

        if self.method is not None and not isinstance(self.method, MethodEnum):
            self.method = MethodEnum(self.method)

        if self.specimen is not None and not isinstance(self.specimen, SpecimenEnum):
            self.specimen = SpecimenEnum(self.specimen)

        if self.genomic_source_class is not None and not isinstance(self.genomic_source_class, GenomicSourceClassEnum):
            self.genomic_source_class = GenomicSourceClassEnum(self.genomic_source_class)

        if self.common_name is not None and not isinstance(self.common_name, CommonNameEnum):
            self.common_name = CommonNameEnum(self.common_name)

        if self.status is not None and not isinstance(self.status, StatusEnum):
            self.status = StatusEnum(self.status)

        if self.gene is not None and not isinstance(self.gene, str):
            self.gene = str(self.gene)

        if self.chromosome is not None and not isinstance(self.chromosome, str):
            self.chromosome = str(self.chromosome)

        if self.mutation_type is not None and not isinstance(self.mutation_type, MutationTypeEnum):
            self.mutation_type = MutationTypeEnum(self.mutation_type)

        if self.mutation_type_other is not None and not isinstance(self.mutation_type_other, str):
            self.mutation_type_other = str(self.mutation_type_other)

        if self.expression_consequence is not None and not isinstance(self.expression_consequence, ExpressionConsequenceEnum):
            self.expression_consequence = ExpressionConsequenceEnum(self.expression_consequence)

        if self.chromosomal_consequence is not None and not isinstance(self.chromosomal_consequence, ChromosomalConsequenceEnum):
            self.chromosomal_consequence = ChromosomalConsequenceEnum(self.chromosomal_consequence)

        if self.genomic_region is not None and not isinstance(self.genomic_region, GenomicRegionEnum):
            self.genomic_region = GenomicRegionEnum(self.genomic_region)

        if self.allelic_state is not None and not isinstance(self.allelic_state, AllelicStateEnum):
            self.allelic_state = AllelicStateEnum(self.allelic_state)

        if self.inheritance_pattern is not None and not isinstance(self.inheritance_pattern, InheritancePatternEnum):
            self.inheritance_pattern = InheritancePatternEnum(self.inheritance_pattern)

        if self.parental_status is not None and not isinstance(self.parental_status, ParentalStatusEnum):
            self.parental_status = ParentalStatusEnum(self.parental_status)

        if self.hgvs_coding is not None and not isinstance(self.hgvs_coding, str):
            self.hgvs_coding = str(self.hgvs_coding)

        if self.hgvs_protein is not None and not isinstance(self.hgvs_protein, str):
            self.hgvs_protein = str(self.hgvs_protein)

        if self.iscn is not None and not isinstance(self.iscn, str):
            self.iscn = str(self.iscn)

        if self.clingen_id is not None and not isinstance(self.clingen_id, str):
            self.clingen_id = str(self.clingen_id)

        if self.copy_number_variation is not None and not isinstance(self.copy_number_variation, CopyNumberVariationEnum):
            self.copy_number_variation = CopyNumberVariationEnum(self.copy_number_variation)

        if self.copy_number is not None and not isinstance(self.copy_number, int):
            self.copy_number = int(self.copy_number)

        if self.amplification is not None and not isinstance(self.amplification, NoNotreportedUnknownYesEnum):
            self.amplification = NoNotreportedUnknownYesEnum(self.amplification)

        if self.allelic_frequency is not None and not isinstance(self.allelic_frequency, int):
            self.allelic_frequency = int(self.allelic_frequency)

        if self.gene2 is not None and not isinstance(self.gene2, str):
            self.gene2 = str(self.gene2)

        if self.mosaicism is not None and not isinstance(self.mosaicism, NoNotreportedUnknownYesEnum):
            self.mosaicism = NoNotreportedUnknownYesEnum(self.mosaicism)

        if self.mosaicism_percent is not None and not isinstance(self.mosaicism_percent, int):
            self.mosaicism_percent = int(self.mosaicism_percent)

        if self.alt_status is not None and not isinstance(self.alt_status, AltStatusEnum):
            self.alt_status = AltStatusEnum(self.alt_status)

        if self.total_chromosomes is not None and not isinstance(self.total_chromosomes, int):
            self.total_chromosomes = int(self.total_chromosomes)

        if self.independent_aberations is not None and not isinstance(self.independent_aberations, int):
            self.independent_aberations = int(self.independent_aberations)

        if self.cells_in_metaphase is not None and not isinstance(self.cells_in_metaphase, int):
            self.cells_in_metaphase = int(self.cells_in_metaphase)

        if self.karyotype_status is not None and not isinstance(self.karyotype_status, KaryotypeStatusEnum):
            self.karyotype_status = KaryotypeStatusEnum(self.karyotype_status)

        if self.dna_index is not None and not isinstance(self.dna_index, DnaIndexEnum):
            self.dna_index = DnaIndexEnum(self.dna_index)

        if self.dna_index_numeric is not None and not isinstance(self.dna_index_numeric, int):
            self.dna_index_numeric = int(self.dna_index_numeric)

        if self.cytodifferentiation is not None and not isinstance(self.cytodifferentiation, CytodifferentiationEnum):
            self.cytodifferentiation = CytodifferentiationEnum(self.cytodifferentiation)

        if self.mitotic_rate is not None and not isinstance(self.mitotic_rate, MitoticRateEnum):
            self.mitotic_rate = MitoticRateEnum(self.mitotic_rate)

        super().__post_init__(**kwargs)


@dataclass
class LesionCharacteristics(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/LesionCharacteristics"]
    class_class_curie: ClassVar[str] = "pcdc:/LesionCharacteristics"
    class_name: ClassVar[str] = "LesionCharacteristics"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/LesionCharacteristics")

    submitter_id: str = None
    type: str = None
    age_at_lesion_assessment: Optional[int] = None
    timings: Optional[Union[dict, Timing]] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    lesion_assessment_review: Optional[Union[str, "LesionAssessmentReviewEnum"]] = None
    lesion_state: Optional[Union[str, "LesionStateEnum"]] = None
    detection_method: Optional[Union[str, "DetectionMethodEnum"]] = None
    tissue_type: Optional[Union[str, "BoneNotreportedSofttissueUnknownEnum"]] = None
    lesion_classification: Optional[Union[str, "LesionClassificationEnum"]] = None
    lesion_presentation: Optional[Union[str, "LesionPresentationEnum"]] = None
    lesion_site: Optional[Union[str, "LesionSiteEnum"]] = None
    lesion_site_other: Optional[str] = None
    morph_sno: Optional[str] = None
    icd_o_morph: Optional[str] = None
    morph_txt: Optional[str] = None
    top_sno: Optional[str] = None
    icd_o_top: Optional[str] = None
    top_txt: Optional[str] = None
    lesion_size: Optional[Union[str, "LesionSizeEnum"]] = None
    longest_diam_dim1: Optional[int] = None
    longest_diam_dim2: Optional[int] = None
    longest_diam_dim3: Optional[int] = None
    diam_type: Optional[Union[str, "DiamTypeEnum"]] = None
    lesion_volume: Optional[Union[str, "LesionVolumeEnum"]] = None
    estimated_volume_numeric: Optional[int] = None
    computed_volume_numeric: Optional[int] = None
    depth: Optional[Union[str, "DepthEnum"]] = None
    lesion_bulky: Optional[Union[str, "LesionBulkyEnum"]] = None
    laterality: Optional[Union[str, "LateralityEnum"]] = None
    invasiveness: Optional[Union[str, "InvasivenessEnum"]] = None
    extension_site: Optional[Union[str, "ExtensionSiteEnum"]] = None
    lesion_response: Optional[Union[str, "LesionResponseEnum"]] = None
    lesion_pct_change: Optional[int] = None
    nodal_involvement: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    nodal_site: Optional[Union[str, "NodalSiteEnum"]] = None
    nodal_determination: Optional[Union[str, "NodalDeterminationEnum"]] = None
    nodal_determination_source: Optional[Union[str, "NodalDeterminationSourceEnum"]] = None
    mibg_avidity: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    necrosis: Optional[Union[str, "NecrosisEnum"]] = None
    necrosis_pct: Optional[int] = None
    parameningeal_extension: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    skip_lesion: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    ipsilateral_nodules: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    joint_involvement: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    site_within_bone: Optional[Union[str, "SiteWithinBoneEnum"]] = None
    cartilage_percent: Optional[int] = None
    peritoneal_cytology: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    pleural_cytology: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    peritoneal_effusion: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    pleural_effusion: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    pericardial_effusion: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    e_extension_site: Optional[Union[str, "EExtensionSiteEnum"]] = None
    anaplasia: Optional[Union[str, "AbsentNotreportedPresentUnknownEnum"]] = None
    anaplasia_extent: Optional[Union[str, "AnaplasiaExtentEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_at_lesion_assessment is not None and not isinstance(self.age_at_lesion_assessment, int):
            self.age_at_lesion_assessment = int(self.age_at_lesion_assessment)

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.lesion_assessment_review is not None and not isinstance(self.lesion_assessment_review, LesionAssessmentReviewEnum):
            self.lesion_assessment_review = LesionAssessmentReviewEnum(self.lesion_assessment_review)

        if self.lesion_state is not None and not isinstance(self.lesion_state, LesionStateEnum):
            self.lesion_state = LesionStateEnum(self.lesion_state)

        if self.detection_method is not None and not isinstance(self.detection_method, DetectionMethodEnum):
            self.detection_method = DetectionMethodEnum(self.detection_method)

        if self.tissue_type is not None and not isinstance(self.tissue_type, BoneNotreportedSofttissueUnknownEnum):
            self.tissue_type = BoneNotreportedSofttissueUnknownEnum(self.tissue_type)

        if self.lesion_classification is not None and not isinstance(self.lesion_classification, LesionClassificationEnum):
            self.lesion_classification = LesionClassificationEnum(self.lesion_classification)

        if self.lesion_presentation is not None and not isinstance(self.lesion_presentation, LesionPresentationEnum):
            self.lesion_presentation = LesionPresentationEnum(self.lesion_presentation)

        if self.lesion_site is not None and not isinstance(self.lesion_site, LesionSiteEnum):
            self.lesion_site = LesionSiteEnum(self.lesion_site)

        if self.lesion_site_other is not None and not isinstance(self.lesion_site_other, str):
            self.lesion_site_other = str(self.lesion_site_other)

        if self.morph_sno is not None and not isinstance(self.morph_sno, str):
            self.morph_sno = str(self.morph_sno)

        if self.icd_o_morph is not None and not isinstance(self.icd_o_morph, str):
            self.icd_o_morph = str(self.icd_o_morph)

        if self.morph_txt is not None and not isinstance(self.morph_txt, str):
            self.morph_txt = str(self.morph_txt)

        if self.top_sno is not None and not isinstance(self.top_sno, str):
            self.top_sno = str(self.top_sno)

        if self.icd_o_top is not None and not isinstance(self.icd_o_top, str):
            self.icd_o_top = str(self.icd_o_top)

        if self.top_txt is not None and not isinstance(self.top_txt, str):
            self.top_txt = str(self.top_txt)

        if self.lesion_size is not None and not isinstance(self.lesion_size, LesionSizeEnum):
            self.lesion_size = LesionSizeEnum(self.lesion_size)

        if self.longest_diam_dim1 is not None and not isinstance(self.longest_diam_dim1, int):
            self.longest_diam_dim1 = int(self.longest_diam_dim1)

        if self.longest_diam_dim2 is not None and not isinstance(self.longest_diam_dim2, int):
            self.longest_diam_dim2 = int(self.longest_diam_dim2)

        if self.longest_diam_dim3 is not None and not isinstance(self.longest_diam_dim3, int):
            self.longest_diam_dim3 = int(self.longest_diam_dim3)

        if self.diam_type is not None and not isinstance(self.diam_type, DiamTypeEnum):
            self.diam_type = DiamTypeEnum(self.diam_type)

        if self.lesion_volume is not None and not isinstance(self.lesion_volume, LesionVolumeEnum):
            self.lesion_volume = LesionVolumeEnum(self.lesion_volume)

        if self.estimated_volume_numeric is not None and not isinstance(self.estimated_volume_numeric, int):
            self.estimated_volume_numeric = int(self.estimated_volume_numeric)

        if self.computed_volume_numeric is not None and not isinstance(self.computed_volume_numeric, int):
            self.computed_volume_numeric = int(self.computed_volume_numeric)

        if self.depth is not None and not isinstance(self.depth, DepthEnum):
            self.depth = DepthEnum(self.depth)

        if self.lesion_bulky is not None and not isinstance(self.lesion_bulky, LesionBulkyEnum):
            self.lesion_bulky = LesionBulkyEnum(self.lesion_bulky)

        if self.laterality is not None and not isinstance(self.laterality, LateralityEnum):
            self.laterality = LateralityEnum(self.laterality)

        if self.invasiveness is not None and not isinstance(self.invasiveness, InvasivenessEnum):
            self.invasiveness = InvasivenessEnum(self.invasiveness)

        if self.extension_site is not None and not isinstance(self.extension_site, ExtensionSiteEnum):
            self.extension_site = ExtensionSiteEnum(self.extension_site)

        if self.lesion_response is not None and not isinstance(self.lesion_response, LesionResponseEnum):
            self.lesion_response = LesionResponseEnum(self.lesion_response)

        if self.lesion_pct_change is not None and not isinstance(self.lesion_pct_change, int):
            self.lesion_pct_change = int(self.lesion_pct_change)

        if self.nodal_involvement is not None and not isinstance(self.nodal_involvement, NoNotreportedUnknownYesEnum):
            self.nodal_involvement = NoNotreportedUnknownYesEnum(self.nodal_involvement)

        if self.nodal_site is not None and not isinstance(self.nodal_site, NodalSiteEnum):
            self.nodal_site = NodalSiteEnum(self.nodal_site)

        if self.nodal_determination is not None and not isinstance(self.nodal_determination, NodalDeterminationEnum):
            self.nodal_determination = NodalDeterminationEnum(self.nodal_determination)

        if self.nodal_determination_source is not None and not isinstance(self.nodal_determination_source, NodalDeterminationSourceEnum):
            self.nodal_determination_source = NodalDeterminationSourceEnum(self.nodal_determination_source)

        if self.mibg_avidity is not None and not isinstance(self.mibg_avidity, NoNotreportedUnknownYesEnum):
            self.mibg_avidity = NoNotreportedUnknownYesEnum(self.mibg_avidity)

        if self.necrosis is not None and not isinstance(self.necrosis, NecrosisEnum):
            self.necrosis = NecrosisEnum(self.necrosis)

        if self.necrosis_pct is not None and not isinstance(self.necrosis_pct, int):
            self.necrosis_pct = int(self.necrosis_pct)

        if self.parameningeal_extension is not None and not isinstance(self.parameningeal_extension, NoNotreportedUnknownYesEnum):
            self.parameningeal_extension = NoNotreportedUnknownYesEnum(self.parameningeal_extension)

        if self.skip_lesion is not None and not isinstance(self.skip_lesion, NoNotreportedUnknownYesEnum):
            self.skip_lesion = NoNotreportedUnknownYesEnum(self.skip_lesion)

        if self.ipsilateral_nodules is not None and not isinstance(self.ipsilateral_nodules, NoNotreportedUnknownYesEnum):
            self.ipsilateral_nodules = NoNotreportedUnknownYesEnum(self.ipsilateral_nodules)

        if self.joint_involvement is not None and not isinstance(self.joint_involvement, NoNotreportedUnknownYesEnum):
            self.joint_involvement = NoNotreportedUnknownYesEnum(self.joint_involvement)

        if self.site_within_bone is not None and not isinstance(self.site_within_bone, SiteWithinBoneEnum):
            self.site_within_bone = SiteWithinBoneEnum(self.site_within_bone)

        if self.cartilage_percent is not None and not isinstance(self.cartilage_percent, int):
            self.cartilage_percent = int(self.cartilage_percent)

        if self.peritoneal_cytology is not None and not isinstance(self.peritoneal_cytology, NoNotreportedUnknownYesEnum):
            self.peritoneal_cytology = NoNotreportedUnknownYesEnum(self.peritoneal_cytology)

        if self.pleural_cytology is not None and not isinstance(self.pleural_cytology, NoNotreportedUnknownYesEnum):
            self.pleural_cytology = NoNotreportedUnknownYesEnum(self.pleural_cytology)

        if self.peritoneal_effusion is not None and not isinstance(self.peritoneal_effusion, NoNotreportedUnknownYesEnum):
            self.peritoneal_effusion = NoNotreportedUnknownYesEnum(self.peritoneal_effusion)

        if self.pleural_effusion is not None and not isinstance(self.pleural_effusion, NoNotreportedUnknownYesEnum):
            self.pleural_effusion = NoNotreportedUnknownYesEnum(self.pleural_effusion)

        if self.pericardial_effusion is not None and not isinstance(self.pericardial_effusion, NoNotreportedUnknownYesEnum):
            self.pericardial_effusion = NoNotreportedUnknownYesEnum(self.pericardial_effusion)

        if self.e_extension_site is not None and not isinstance(self.e_extension_site, EExtensionSiteEnum):
            self.e_extension_site = EExtensionSiteEnum(self.e_extension_site)

        if self.anaplasia is not None and not isinstance(self.anaplasia, AbsentNotreportedPresentUnknownEnum):
            self.anaplasia = AbsentNotreportedPresentUnknownEnum(self.anaplasia)

        if self.anaplasia_extent is not None and not isinstance(self.anaplasia_extent, AnaplasiaExtentEnum):
            self.anaplasia_extent = AnaplasiaExtentEnum(self.anaplasia_extent)

        super().__post_init__(**kwargs)


@dataclass
class Staging(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/Staging"]
    class_class_curie: ClassVar[str] = "pcdc:/Staging"
    class_name: ClassVar[str] = "Staging"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/Staging")

    submitter_id: str = None
    type: str = None
    age_at_staging: Optional[int] = None
    timings: Optional[Union[dict, Timing]] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    stage_system: Optional[Union[str, "StageSystemEnum"]] = None
    stage: Optional[Union[str, "StageEnum"]] = None
    ann_arbor_mod_ab: Optional[Union[str, "AnnArborModAbEnum"]] = None
    ann_arbor_mod_e: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    ann_arbor_mod_s: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    tnm_finding: Optional[Union[str, "TnmFindingEnum"]] = None
    irs_group: Optional[Union[str, "IrsGroupEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_at_staging is not None and not isinstance(self.age_at_staging, int):
            self.age_at_staging = int(self.age_at_staging)

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.stage_system is not None and not isinstance(self.stage_system, StageSystemEnum):
            self.stage_system = StageSystemEnum(self.stage_system)

        if self.stage is not None and not isinstance(self.stage, StageEnum):
            self.stage = StageEnum(self.stage)

        if self.ann_arbor_mod_ab is not None and not isinstance(self.ann_arbor_mod_ab, AnnArborModAbEnum):
            self.ann_arbor_mod_ab = AnnArborModAbEnum(self.ann_arbor_mod_ab)

        if self.ann_arbor_mod_e is not None and not isinstance(self.ann_arbor_mod_e, NoNotreportedUnknownYesEnum):
            self.ann_arbor_mod_e = NoNotreportedUnknownYesEnum(self.ann_arbor_mod_e)

        if self.ann_arbor_mod_s is not None and not isinstance(self.ann_arbor_mod_s, NoNotreportedUnknownYesEnum):
            self.ann_arbor_mod_s = NoNotreportedUnknownYesEnum(self.ann_arbor_mod_s)

        if self.tnm_finding is not None and not isinstance(self.tnm_finding, TnmFindingEnum):
            self.tnm_finding = TnmFindingEnum(self.tnm_finding)

        if self.irs_group is not None and not isinstance(self.irs_group, IrsGroupEnum):
            self.irs_group = IrsGroupEnum(self.irs_group)

        super().__post_init__(**kwargs)


@dataclass
class Histology(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/Histology"]
    class_class_curie: ClassVar[str] = "pcdc:/Histology"
    class_name: ClassVar[str] = "Histology"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/Histology")

    submitter_id: str = None
    type: str = None
    age_at_hist_assessment: Optional[int] = None
    timings: Optional[Union[dict, Timing]] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    hist_assessment_review: Optional[Union[str, "HistAssessmentReviewEnum"]] = None
    histology: Optional[Union[str, "HistologyEnum"]] = None
    histology_result: Optional[str] = None
    histology_result_numeric: Optional[int] = None
    histology_result_unit: Optional[Union[str, "NotreportedUnknownEnum"]] = None
    histology_grade: Optional[Union[str, "HistologyGradeEnum"]] = None
    hist_icd_o_morph_code: Optional[str] = None
    mature_glial_implants: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    somatic_malignancy_type: Optional[Union[str, "SomaticMalignancyTypeEnum"]] = None
    histology_inpc: Optional[Union[str, "HistologyInpcEnum"]] = None
    who_aml: Optional[Union[str, "WhoAmlEnum"]] = None
    fab_type: Optional[Union[str, "FabTypeEnum"]] = None
    all_type: Optional[Union[str, "AllTypeEnum"]] = None
    mpal: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    mlds: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    tamds: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    secondary_aml: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_at_hist_assessment is not None and not isinstance(self.age_at_hist_assessment, int):
            self.age_at_hist_assessment = int(self.age_at_hist_assessment)

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.hist_assessment_review is not None and not isinstance(self.hist_assessment_review, HistAssessmentReviewEnum):
            self.hist_assessment_review = HistAssessmentReviewEnum(self.hist_assessment_review)

        if self.histology is not None and not isinstance(self.histology, HistologyEnum):
            self.histology = HistologyEnum(self.histology)

        if self.histology_result is not None and not isinstance(self.histology_result, str):
            self.histology_result = str(self.histology_result)

        if self.histology_result_numeric is not None and not isinstance(self.histology_result_numeric, int):
            self.histology_result_numeric = int(self.histology_result_numeric)

        if self.histology_result_unit is not None and not isinstance(self.histology_result_unit, NotreportedUnknownEnum):
            self.histology_result_unit = NotreportedUnknownEnum(self.histology_result_unit)

        if self.histology_grade is not None and not isinstance(self.histology_grade, HistologyGradeEnum):
            self.histology_grade = HistologyGradeEnum(self.histology_grade)

        if self.hist_icd_o_morph_code is not None and not isinstance(self.hist_icd_o_morph_code, str):
            self.hist_icd_o_morph_code = str(self.hist_icd_o_morph_code)

        if self.mature_glial_implants is not None and not isinstance(self.mature_glial_implants, NoNotreportedUnknownYesEnum):
            self.mature_glial_implants = NoNotreportedUnknownYesEnum(self.mature_glial_implants)

        if self.somatic_malignancy_type is not None and not isinstance(self.somatic_malignancy_type, SomaticMalignancyTypeEnum):
            self.somatic_malignancy_type = SomaticMalignancyTypeEnum(self.somatic_malignancy_type)

        if self.histology_inpc is not None and not isinstance(self.histology_inpc, HistologyInpcEnum):
            self.histology_inpc = HistologyInpcEnum(self.histology_inpc)

        if self.who_aml is not None and not isinstance(self.who_aml, WhoAmlEnum):
            self.who_aml = WhoAmlEnum(self.who_aml)

        if self.fab_type is not None and not isinstance(self.fab_type, FabTypeEnum):
            self.fab_type = FabTypeEnum(self.fab_type)

        if self.all_type is not None and not isinstance(self.all_type, AllTypeEnum):
            self.all_type = AllTypeEnum(self.all_type)

        if self.mpal is not None and not isinstance(self.mpal, NoNotreportedUnknownYesEnum):
            self.mpal = NoNotreportedUnknownYesEnum(self.mpal)

        if self.mlds is not None and not isinstance(self.mlds, NoNotreportedUnknownYesEnum):
            self.mlds = NoNotreportedUnknownYesEnum(self.mlds)

        if self.tamds is not None and not isinstance(self.tamds, NoNotreportedUnknownYesEnum):
            self.tamds = NoNotreportedUnknownYesEnum(self.tamds)

        if self.secondary_aml is not None and not isinstance(self.secondary_aml, NoNotreportedUnknownYesEnum):
            self.secondary_aml = NoNotreportedUnknownYesEnum(self.secondary_aml)

        super().__post_init__(**kwargs)


@dataclass
class DiseaseCharacteristics(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/DiseaseCharacteristics"]
    class_class_curie: ClassVar[str] = "pcdc:/DiseaseCharacteristics"
    class_name: ClassVar[str] = "DiseaseCharacteristics"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/DiseaseCharacteristics")

    submitter_id: str = None
    type: str = None
    timings: Optional[Union[dict, Timing]] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    risk_group_system: Optional[Union[str, "RiskGroupSystemEnum"]] = None
    risk_group: Optional[Union[str, "RiskGroupEnum"]] = None
    mki: Optional[Union[str, "MkiEnum"]] = None
    disease_site: Optional[Union[str, "DiseaseSiteEnum"]] = None
    detection_method: Optional[Union[str, "DetectionMethodEnum"]] = None
    cns_disease_status: Optional[Union[str, "CnsDiseaseStatusEnum"]] = None
    performance_score: Optional[Union[str, "PerformanceScoreEnum"]] = None
    performance_score_system: Optional[Union[str, "PerformanceScoreSystemEnum"]] = None
    gpoh_score: Optional[Union[str, "GpohScoreEnum"]] = None
    prior_steroids_week: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    prior_steroids_month: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    bulk_disease: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    bulk_nodal_aggregate: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    bulk_med_mass: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    med_ratio: Optional[int] = None
    fever: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    night_sweats: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    weight_loss: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    nodular_splenic: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    initial_treatment_category: Optional[Union[str, "InitialTreatmentCategoryEnum"]] = None
    myeloid_sarcoma: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    myeloid_sarcoma_site: Optional[Union[str, "MyeloidSarcomaSiteEnum"]] = None
    gts: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    gts_treatment: Optional[Union[str, "GtsTreatmentEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.risk_group_system is not None and not isinstance(self.risk_group_system, RiskGroupSystemEnum):
            self.risk_group_system = RiskGroupSystemEnum(self.risk_group_system)

        if self.risk_group is not None and not isinstance(self.risk_group, RiskGroupEnum):
            self.risk_group = RiskGroupEnum(self.risk_group)

        if self.mki is not None and not isinstance(self.mki, MkiEnum):
            self.mki = MkiEnum(self.mki)

        if self.disease_site is not None and not isinstance(self.disease_site, DiseaseSiteEnum):
            self.disease_site = DiseaseSiteEnum(self.disease_site)

        if self.detection_method is not None and not isinstance(self.detection_method, DetectionMethodEnum):
            self.detection_method = DetectionMethodEnum(self.detection_method)

        if self.cns_disease_status is not None and not isinstance(self.cns_disease_status, CnsDiseaseStatusEnum):
            self.cns_disease_status = CnsDiseaseStatusEnum(self.cns_disease_status)

        if self.performance_score is not None and not isinstance(self.performance_score, PerformanceScoreEnum):
            self.performance_score = PerformanceScoreEnum(self.performance_score)

        if self.performance_score_system is not None and not isinstance(self.performance_score_system, PerformanceScoreSystemEnum):
            self.performance_score_system = PerformanceScoreSystemEnum(self.performance_score_system)

        if self.gpoh_score is not None and not isinstance(self.gpoh_score, GpohScoreEnum):
            self.gpoh_score = GpohScoreEnum(self.gpoh_score)

        if self.prior_steroids_week is not None and not isinstance(self.prior_steroids_week, NoNotreportedUnknownYesEnum):
            self.prior_steroids_week = NoNotreportedUnknownYesEnum(self.prior_steroids_week)

        if self.prior_steroids_month is not None and not isinstance(self.prior_steroids_month, NoNotreportedUnknownYesEnum):
            self.prior_steroids_month = NoNotreportedUnknownYesEnum(self.prior_steroids_month)

        if self.bulk_disease is not None and not isinstance(self.bulk_disease, NoNotreportedUnknownYesEnum):
            self.bulk_disease = NoNotreportedUnknownYesEnum(self.bulk_disease)

        if self.bulk_nodal_aggregate is not None and not isinstance(self.bulk_nodal_aggregate, NoNotreportedUnknownYesEnum):
            self.bulk_nodal_aggregate = NoNotreportedUnknownYesEnum(self.bulk_nodal_aggregate)

        if self.bulk_med_mass is not None and not isinstance(self.bulk_med_mass, NoNotreportedUnknownYesEnum):
            self.bulk_med_mass = NoNotreportedUnknownYesEnum(self.bulk_med_mass)

        if self.med_ratio is not None and not isinstance(self.med_ratio, int):
            self.med_ratio = int(self.med_ratio)

        if self.fever is not None and not isinstance(self.fever, NoNotreportedUnknownYesEnum):
            self.fever = NoNotreportedUnknownYesEnum(self.fever)

        if self.night_sweats is not None and not isinstance(self.night_sweats, NoNotreportedUnknownYesEnum):
            self.night_sweats = NoNotreportedUnknownYesEnum(self.night_sweats)

        if self.weight_loss is not None and not isinstance(self.weight_loss, NoNotreportedUnknownYesEnum):
            self.weight_loss = NoNotreportedUnknownYesEnum(self.weight_loss)

        if self.nodular_splenic is not None and not isinstance(self.nodular_splenic, NoNotreportedUnknownYesEnum):
            self.nodular_splenic = NoNotreportedUnknownYesEnum(self.nodular_splenic)

        if self.initial_treatment_category is not None and not isinstance(self.initial_treatment_category, InitialTreatmentCategoryEnum):
            self.initial_treatment_category = InitialTreatmentCategoryEnum(self.initial_treatment_category)

        if self.myeloid_sarcoma is not None and not isinstance(self.myeloid_sarcoma, NoNotreportedUnknownYesEnum):
            self.myeloid_sarcoma = NoNotreportedUnknownYesEnum(self.myeloid_sarcoma)

        if self.myeloid_sarcoma_site is not None and not isinstance(self.myeloid_sarcoma_site, MyeloidSarcomaSiteEnum):
            self.myeloid_sarcoma_site = MyeloidSarcomaSiteEnum(self.myeloid_sarcoma_site)

        if self.gts is not None and not isinstance(self.gts, NoNotreportedUnknownYesEnum):
            self.gts = NoNotreportedUnknownYesEnum(self.gts)

        if self.gts_treatment is not None and not isinstance(self.gts_treatment, GtsTreatmentEnum):
            self.gts_treatment = GtsTreatmentEnum(self.gts_treatment)

        super().__post_init__(**kwargs)


@dataclass
class Medication(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/Medication"]
    class_class_curie: ClassVar[str] = "pcdc:/Medication"
    class_name: ClassVar[str] = "Medication"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/Medication")

    submitter_id: str = None
    type: str = None
    age_at_medication_start: Optional[int] = None
    age_at_medication_end: Optional[int] = None
    timings: Optional[Union[dict, Timing]] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    administration_status: Optional[Union[str, "AdministrationStatusEnum"]] = None
    medication: Optional[Union[str, "MedicationEnum"]] = None
    protocol_medication: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    non_protocol_timing: Optional[Union[str, "NonProtocolTimingEnum"]] = None
    non_protocol_reason: Optional[Union[str, "NonProtocolReasonEnum"]] = None
    cycle_number: Optional[int] = None
    route: Optional[Union[str, "RouteEnum"]] = None
    route_detail: Optional[Union[str, "RouteDetailEnum"]] = None
    normalization_basis: Optional[Union[str, "NormalizationBasisEnum"]] = None
    number_doses: Optional[int] = None
    total_dose_administered: Optional[int] = None
    total_dose_intended: Optional[int] = None
    total_dose_units: Optional[Union[str, "TotalDoseUnitsEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_at_medication_start is not None and not isinstance(self.age_at_medication_start, int):
            self.age_at_medication_start = int(self.age_at_medication_start)

        if self.age_at_medication_end is not None and not isinstance(self.age_at_medication_end, int):
            self.age_at_medication_end = int(self.age_at_medication_end)

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.administration_status is not None and not isinstance(self.administration_status, AdministrationStatusEnum):
            self.administration_status = AdministrationStatusEnum(self.administration_status)

        if self.medication is not None and not isinstance(self.medication, MedicationEnum):
            self.medication = MedicationEnum(self.medication)

        if self.protocol_medication is not None and not isinstance(self.protocol_medication, NoNotreportedUnknownYesEnum):
            self.protocol_medication = NoNotreportedUnknownYesEnum(self.protocol_medication)

        if self.non_protocol_timing is not None and not isinstance(self.non_protocol_timing, NonProtocolTimingEnum):
            self.non_protocol_timing = NonProtocolTimingEnum(self.non_protocol_timing)

        if self.non_protocol_reason is not None and not isinstance(self.non_protocol_reason, NonProtocolReasonEnum):
            self.non_protocol_reason = NonProtocolReasonEnum(self.non_protocol_reason)

        if self.cycle_number is not None and not isinstance(self.cycle_number, int):
            self.cycle_number = int(self.cycle_number)

        if self.route is not None and not isinstance(self.route, RouteEnum):
            self.route = RouteEnum(self.route)

        if self.route_detail is not None and not isinstance(self.route_detail, RouteDetailEnum):
            self.route_detail = RouteDetailEnum(self.route_detail)

        if self.normalization_basis is not None and not isinstance(self.normalization_basis, NormalizationBasisEnum):
            self.normalization_basis = NormalizationBasisEnum(self.normalization_basis)

        if self.number_doses is not None and not isinstance(self.number_doses, int):
            self.number_doses = int(self.number_doses)

        if self.total_dose_administered is not None and not isinstance(self.total_dose_administered, int):
            self.total_dose_administered = int(self.total_dose_administered)

        if self.total_dose_intended is not None and not isinstance(self.total_dose_intended, int):
            self.total_dose_intended = int(self.total_dose_intended)

        if self.total_dose_units is not None and not isinstance(self.total_dose_units, TotalDoseUnitsEnum):
            self.total_dose_units = TotalDoseUnitsEnum(self.total_dose_units)

        super().__post_init__(**kwargs)


@dataclass
class ProtocolTreatmentModifications(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/ProtocolTreatmentModifications"]
    class_class_curie: ClassVar[str] = "pcdc:/ProtocolTreatmentModifications"
    class_name: ClassVar[str] = "ProtocolTreatmentModifications"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/ProtocolTreatmentModifications")

    submitter_id: str = None
    type: str = None
    age_at_mod: Optional[int] = None
    timings: Optional[Union[dict, Timing]] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    mod_type: Optional[Union[str, "ModTypeEnum"]] = None
    mod_rationale: Optional[Union[str, "ModRationaleEnum"]] = None
    mod_reason: Optional[Union[str, "ModReasonEnum"]] = None
    toxicity_detail: Optional[Union[str, "ToxicityDetailEnum"]] = None
    toxicity_immune: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    toxicity_infusion: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    original_agent: Optional[Union[str, "BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum"]] = None
    sub_agent: Optional[Union[str, "BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_at_mod is not None and not isinstance(self.age_at_mod, int):
            self.age_at_mod = int(self.age_at_mod)

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.mod_type is not None and not isinstance(self.mod_type, ModTypeEnum):
            self.mod_type = ModTypeEnum(self.mod_type)

        if self.mod_rationale is not None and not isinstance(self.mod_rationale, ModRationaleEnum):
            self.mod_rationale = ModRationaleEnum(self.mod_rationale)

        if self.mod_reason is not None and not isinstance(self.mod_reason, ModReasonEnum):
            self.mod_reason = ModReasonEnum(self.mod_reason)

        if self.toxicity_detail is not None and not isinstance(self.toxicity_detail, ToxicityDetailEnum):
            self.toxicity_detail = ToxicityDetailEnum(self.toxicity_detail)

        if self.toxicity_immune is not None and not isinstance(self.toxicity_immune, NoNotreportedUnknownYesEnum):
            self.toxicity_immune = NoNotreportedUnknownYesEnum(self.toxicity_immune)

        if self.toxicity_infusion is not None and not isinstance(self.toxicity_infusion, NoNotreportedUnknownYesEnum):
            self.toxicity_infusion = NoNotreportedUnknownYesEnum(self.toxicity_infusion)

        if self.original_agent is not None and not isinstance(self.original_agent, BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum):
            self.original_agent = BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum(self.original_agent)

        if self.sub_agent is not None and not isinstance(self.sub_agent, BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum):
            self.sub_agent = BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum(self.sub_agent)

        super().__post_init__(**kwargs)


@dataclass
class RadiationTherapy(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/RadiationTherapy"]
    class_class_curie: ClassVar[str] = "pcdc:/RadiationTherapy"
    class_name: ClassVar[str] = "RadiationTherapy"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/RadiationTherapy")

    submitter_id: str = None
    type: str = None
    age_at_rt_start: Optional[int] = None
    age_at_rt_end: Optional[int] = None
    timings: Optional[Union[dict, Timing]] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    protocol_radiation_therapy: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    non_protocol_timing: Optional[Union[str, "NonProtocolTimingEnum"]] = None
    tumor_classification: Optional[Union[str, "TumorClassificationEnum"]] = None
    tumor_tissue_type: Optional[Union[str, "BoneNotreportedSofttissueUnknownEnum"]] = None
    rt_site: Optional[Union[str, "RtSiteEnum"]] = None
    laterality: Optional[Union[str, "LateralityEnum"]] = None
    energy_type: Optional[Union[str, "EnergyTypeEnum"]] = None
    rt_dose: Optional[int] = None
    rt_unit: Optional[Union[str, "RtUnitEnum"]] = None
    boost: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    boost_dose: Optional[int] = None
    num_fraction: Optional[int] = None
    transposition_organ: Optional[Union[str, "TranspositionOrganEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_at_rt_start is not None and not isinstance(self.age_at_rt_start, int):
            self.age_at_rt_start = int(self.age_at_rt_start)

        if self.age_at_rt_end is not None and not isinstance(self.age_at_rt_end, int):
            self.age_at_rt_end = int(self.age_at_rt_end)

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.protocol_radiation_therapy is not None and not isinstance(self.protocol_radiation_therapy, NoNotreportedUnknownYesEnum):
            self.protocol_radiation_therapy = NoNotreportedUnknownYesEnum(self.protocol_radiation_therapy)

        if self.non_protocol_timing is not None and not isinstance(self.non_protocol_timing, NonProtocolTimingEnum):
            self.non_protocol_timing = NonProtocolTimingEnum(self.non_protocol_timing)

        if self.tumor_classification is not None and not isinstance(self.tumor_classification, TumorClassificationEnum):
            self.tumor_classification = TumorClassificationEnum(self.tumor_classification)

        if self.tumor_tissue_type is not None and not isinstance(self.tumor_tissue_type, BoneNotreportedSofttissueUnknownEnum):
            self.tumor_tissue_type = BoneNotreportedSofttissueUnknownEnum(self.tumor_tissue_type)

        if self.rt_site is not None and not isinstance(self.rt_site, RtSiteEnum):
            self.rt_site = RtSiteEnum(self.rt_site)

        if self.laterality is not None and not isinstance(self.laterality, LateralityEnum):
            self.laterality = LateralityEnum(self.laterality)

        if self.energy_type is not None and not isinstance(self.energy_type, EnergyTypeEnum):
            self.energy_type = EnergyTypeEnum(self.energy_type)

        if self.rt_dose is not None and not isinstance(self.rt_dose, int):
            self.rt_dose = int(self.rt_dose)

        if self.rt_unit is not None and not isinstance(self.rt_unit, RtUnitEnum):
            self.rt_unit = RtUnitEnum(self.rt_unit)

        if self.boost is not None and not isinstance(self.boost, NoNotreportedUnknownYesEnum):
            self.boost = NoNotreportedUnknownYesEnum(self.boost)

        if self.boost_dose is not None and not isinstance(self.boost_dose, int):
            self.boost_dose = int(self.boost_dose)

        if self.num_fraction is not None and not isinstance(self.num_fraction, int):
            self.num_fraction = int(self.num_fraction)

        if self.transposition_organ is not None and not isinstance(self.transposition_organ, TranspositionOrganEnum):
            self.transposition_organ = TranspositionOrganEnum(self.transposition_organ)

        super().__post_init__(**kwargs)


@dataclass
class BiopsyAndSurgicalProcedures(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/BiopsyAndSurgicalProcedures"]
    class_class_curie: ClassVar[str] = "pcdc:/BiopsyAndSurgicalProcedures"
    class_name: ClassVar[str] = "BiopsyAndSurgicalProcedures"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/BiopsyAndSurgicalProcedures")

    submitter_id: str = None
    type: str = None
    age_at_procedure: Optional[int] = None
    timings: Optional[Union[dict, Timing]] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    protocol_procedure: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    non_protocol_timing: Optional[Union[str, "NonProtocolTimingEnum"]] = None
    tumor_classification: Optional[Union[str, "TumorClassificationEnum"]] = None
    tumor_tissue_type: Optional[Union[str, "BoneNotreportedSofttissueUnknownEnum"]] = None
    procedure_site: Optional[Union[str, "ProcedureSiteEnum"]] = None
    procedure_laterality: Optional[Union[str, "ProcedureLateralityEnum"]] = None
    procedure_type: Optional[Union[str, "ProcedureTypeEnum"]] = None
    surgery_type_limb: Optional[Union[str, "SurgeryTypeLimbEnum"]] = None
    amputation_type: Optional[Union[str, "AmputationTypeEnum"]] = None
    resection_type: Optional[Union[str, "ResectionTypeEnum"]] = None
    surgery_type_limb_salvage: Optional[Union[str, "SurgeryTypeLimbSalvageEnum"]] = None
    reconstruction_type: Optional[Union[str, "ReconstructionTypeEnum"]] = None
    procedure_extent: Optional[Union[str, "ProcedureExtentEnum"]] = None
    margins: Optional[Union[str, "MarginsEnum"]] = None
    biopsy_type: Optional[Union[str, "BiopsyTypeEnum"]] = None
    met_non_lung_mgmt: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    met_lung_mgmt: Optional[Union[str, "MetLungMgmtEnum"]] = None
    localization_technique: Optional[Union[str, "LocalizationTechniqueEnum"]] = None
    distance_margin_tumor: Optional[int] = None
    pelvic_involvement: Optional[Union[str, "PelvicInvolvementEnum"]] = None
    surgery: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    number_nodes: Optional[Union[str, "NumberNodesEnum"]] = None
    number_nodes_numeric: Optional[int] = None
    procedure_purpose: Optional[Union[str, "ProcedurePurposeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_at_procedure is not None and not isinstance(self.age_at_procedure, int):
            self.age_at_procedure = int(self.age_at_procedure)

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.protocol_procedure is not None and not isinstance(self.protocol_procedure, NoNotreportedUnknownYesEnum):
            self.protocol_procedure = NoNotreportedUnknownYesEnum(self.protocol_procedure)

        if self.non_protocol_timing is not None and not isinstance(self.non_protocol_timing, NonProtocolTimingEnum):
            self.non_protocol_timing = NonProtocolTimingEnum(self.non_protocol_timing)

        if self.tumor_classification is not None and not isinstance(self.tumor_classification, TumorClassificationEnum):
            self.tumor_classification = TumorClassificationEnum(self.tumor_classification)

        if self.tumor_tissue_type is not None and not isinstance(self.tumor_tissue_type, BoneNotreportedSofttissueUnknownEnum):
            self.tumor_tissue_type = BoneNotreportedSofttissueUnknownEnum(self.tumor_tissue_type)

        if self.procedure_site is not None and not isinstance(self.procedure_site, ProcedureSiteEnum):
            self.procedure_site = ProcedureSiteEnum(self.procedure_site)

        if self.procedure_laterality is not None and not isinstance(self.procedure_laterality, ProcedureLateralityEnum):
            self.procedure_laterality = ProcedureLateralityEnum(self.procedure_laterality)

        if self.procedure_type is not None and not isinstance(self.procedure_type, ProcedureTypeEnum):
            self.procedure_type = ProcedureTypeEnum(self.procedure_type)

        if self.surgery_type_limb is not None and not isinstance(self.surgery_type_limb, SurgeryTypeLimbEnum):
            self.surgery_type_limb = SurgeryTypeLimbEnum(self.surgery_type_limb)

        if self.amputation_type is not None and not isinstance(self.amputation_type, AmputationTypeEnum):
            self.amputation_type = AmputationTypeEnum(self.amputation_type)

        if self.resection_type is not None and not isinstance(self.resection_type, ResectionTypeEnum):
            self.resection_type = ResectionTypeEnum(self.resection_type)

        if self.surgery_type_limb_salvage is not None and not isinstance(self.surgery_type_limb_salvage, SurgeryTypeLimbSalvageEnum):
            self.surgery_type_limb_salvage = SurgeryTypeLimbSalvageEnum(self.surgery_type_limb_salvage)

        if self.reconstruction_type is not None and not isinstance(self.reconstruction_type, ReconstructionTypeEnum):
            self.reconstruction_type = ReconstructionTypeEnum(self.reconstruction_type)

        if self.procedure_extent is not None and not isinstance(self.procedure_extent, ProcedureExtentEnum):
            self.procedure_extent = ProcedureExtentEnum(self.procedure_extent)

        if self.margins is not None and not isinstance(self.margins, MarginsEnum):
            self.margins = MarginsEnum(self.margins)

        if self.biopsy_type is not None and not isinstance(self.biopsy_type, BiopsyTypeEnum):
            self.biopsy_type = BiopsyTypeEnum(self.biopsy_type)

        if self.met_non_lung_mgmt is not None and not isinstance(self.met_non_lung_mgmt, NoNotreportedUnknownYesEnum):
            self.met_non_lung_mgmt = NoNotreportedUnknownYesEnum(self.met_non_lung_mgmt)

        if self.met_lung_mgmt is not None and not isinstance(self.met_lung_mgmt, MetLungMgmtEnum):
            self.met_lung_mgmt = MetLungMgmtEnum(self.met_lung_mgmt)

        if self.localization_technique is not None and not isinstance(self.localization_technique, LocalizationTechniqueEnum):
            self.localization_technique = LocalizationTechniqueEnum(self.localization_technique)

        if self.distance_margin_tumor is not None and not isinstance(self.distance_margin_tumor, int):
            self.distance_margin_tumor = int(self.distance_margin_tumor)

        if self.pelvic_involvement is not None and not isinstance(self.pelvic_involvement, PelvicInvolvementEnum):
            self.pelvic_involvement = PelvicInvolvementEnum(self.pelvic_involvement)

        if self.surgery is not None and not isinstance(self.surgery, NoNotreportedUnknownYesEnum):
            self.surgery = NoNotreportedUnknownYesEnum(self.surgery)

        if self.number_nodes is not None and not isinstance(self.number_nodes, NumberNodesEnum):
            self.number_nodes = NumberNodesEnum(self.number_nodes)

        if self.number_nodes_numeric is not None and not isinstance(self.number_nodes_numeric, int):
            self.number_nodes_numeric = int(self.number_nodes_numeric)

        if self.procedure_purpose is not None and not isinstance(self.procedure_purpose, ProcedurePurposeEnum):
            self.procedure_purpose = ProcedurePurposeEnum(self.procedure_purpose)

        super().__post_init__(**kwargs)


@dataclass
class TransfusionMedicineProcedure(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/TransfusionMedicineProcedure"]
    class_class_curie: ClassVar[str] = "pcdc:/TransfusionMedicineProcedure"
    class_name: ClassVar[str] = "TransfusionMedicineProcedure"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/TransfusionMedicineProcedure")

    submitter_id: str = None
    type: str = None
    age_at_tmp_start: Optional[int] = None
    timings: Optional[Union[dict, Timing]] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    protocol_transfusion: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    non_protocol_timing: Optional[Union[str, "NonProtocolTimingEnum"]] = None
    tmp_type: Optional[Union[str, "TmpTypeEnum"]] = None
    tmp_product: Optional[Union[str, "TmpProductEnum"]] = None
    tmp_product_type: Optional[Union[str, "TmpProductTypeEnum"]] = None
    tmp_number_units: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_at_tmp_start is not None and not isinstance(self.age_at_tmp_start, int):
            self.age_at_tmp_start = int(self.age_at_tmp_start)

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.protocol_transfusion is not None and not isinstance(self.protocol_transfusion, NoNotreportedUnknownYesEnum):
            self.protocol_transfusion = NoNotreportedUnknownYesEnum(self.protocol_transfusion)

        if self.non_protocol_timing is not None and not isinstance(self.non_protocol_timing, NonProtocolTimingEnum):
            self.non_protocol_timing = NonProtocolTimingEnum(self.non_protocol_timing)

        if self.tmp_type is not None and not isinstance(self.tmp_type, TmpTypeEnum):
            self.tmp_type = TmpTypeEnum(self.tmp_type)

        if self.tmp_product is not None and not isinstance(self.tmp_product, TmpProductEnum):
            self.tmp_product = TmpProductEnum(self.tmp_product)

        if self.tmp_product_type is not None and not isinstance(self.tmp_product_type, TmpProductTypeEnum):
            self.tmp_product_type = TmpProductTypeEnum(self.tmp_product_type)

        if self.tmp_number_units is not None and not isinstance(self.tmp_number_units, int):
            self.tmp_number_units = int(self.tmp_number_units)

        super().__post_init__(**kwargs)


@dataclass
class CellularImmunotherapy(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/CellularImmunotherapy"]
    class_class_curie: ClassVar[str] = "pcdc:/CellularImmunotherapy"
    class_name: ClassVar[str] = "CellularImmunotherapy"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/CellularImmunotherapy")

    submitter_id: str = None
    type: str = None
    age_at_cimt_start: Optional[int] = None
    timings: Optional[Union[dict, Timing]] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    protocol_cimt: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    non_protocol_timing: Optional[Union[str, "NonProtocolTimingEnum"]] = None
    cimt_type: Optional[Union[str, "CimtTypeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_at_cimt_start is not None and not isinstance(self.age_at_cimt_start, int):
            self.age_at_cimt_start = int(self.age_at_cimt_start)

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.protocol_cimt is not None and not isinstance(self.protocol_cimt, NoNotreportedUnknownYesEnum):
            self.protocol_cimt = NoNotreportedUnknownYesEnum(self.protocol_cimt)

        if self.non_protocol_timing is not None and not isinstance(self.non_protocol_timing, NonProtocolTimingEnum):
            self.non_protocol_timing = NonProtocolTimingEnum(self.non_protocol_timing)

        if self.cimt_type is not None and not isinstance(self.cimt_type, CimtTypeEnum):
            self.cimt_type = CimtTypeEnum(self.cimt_type)

        super().__post_init__(**kwargs)


@dataclass
class StemCellTransplant(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/StemCellTransplant"]
    class_class_curie: ClassVar[str] = "pcdc:/StemCellTransplant"
    class_name: ClassVar[str] = "StemCellTransplant"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/StemCellTransplant")

    submitter_id: str = None
    type: str = None
    age_at_sct: Optional[int] = None
    timings: Optional[Union[dict, Timing]] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    protocol_sct: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    non_protocol_timing: Optional[Union[str, "NonProtocolTimingEnum"]] = None
    sct_type: Optional[Union[str, "SctTypeEnum"]] = None
    sct_source: Optional[Union[str, "SctSourceEnum"]] = None
    sct_donor_relationship: Optional[Union[str, "SctDonorRelationshipEnum"]] = None
    hla_match: Optional[Union[str, "HlaMatchEnum"]] = None
    number_hla: Optional[int] = None
    number_matches: Optional[int] = None
    hla_a_result: Optional[Union[str, "BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum"]] = None
    hla_b_result: Optional[Union[str, "BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum"]] = None
    hla_c_result: Optional[Union[str, "BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum"]] = None
    hla_drb1_result: Optional[Union[str, "BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum"]] = None
    hla_dq_result: Optional[Union[str, "BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum"]] = None
    sct_conditioning_type: Optional[Union[str, "SctConditioningTypeEnum"]] = None
    sct_tbi: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    sct_cycles: Optional[Decimal] = None
    sct_cd34_coll: Optional[Decimal] = None
    sct_cd34_transplant: Optional[Decimal] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_at_sct is not None and not isinstance(self.age_at_sct, int):
            self.age_at_sct = int(self.age_at_sct)

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.protocol_sct is not None and not isinstance(self.protocol_sct, NoNotreportedUnknownYesEnum):
            self.protocol_sct = NoNotreportedUnknownYesEnum(self.protocol_sct)

        if self.non_protocol_timing is not None and not isinstance(self.non_protocol_timing, NonProtocolTimingEnum):
            self.non_protocol_timing = NonProtocolTimingEnum(self.non_protocol_timing)

        if self.sct_type is not None and not isinstance(self.sct_type, SctTypeEnum):
            self.sct_type = SctTypeEnum(self.sct_type)

        if self.sct_source is not None and not isinstance(self.sct_source, SctSourceEnum):
            self.sct_source = SctSourceEnum(self.sct_source)

        if self.sct_donor_relationship is not None and not isinstance(self.sct_donor_relationship, SctDonorRelationshipEnum):
            self.sct_donor_relationship = SctDonorRelationshipEnum(self.sct_donor_relationship)

        if self.hla_match is not None and not isinstance(self.hla_match, HlaMatchEnum):
            self.hla_match = HlaMatchEnum(self.hla_match)

        if self.number_hla is not None and not isinstance(self.number_hla, int):
            self.number_hla = int(self.number_hla)

        if self.number_matches is not None and not isinstance(self.number_matches, int):
            self.number_matches = int(self.number_matches)

        if self.hla_a_result is not None and not isinstance(self.hla_a_result, BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum):
            self.hla_a_result = BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum(self.hla_a_result)

        if self.hla_b_result is not None and not isinstance(self.hla_b_result, BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum):
            self.hla_b_result = BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum(self.hla_b_result)

        if self.hla_c_result is not None and not isinstance(self.hla_c_result, BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum):
            self.hla_c_result = BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum(self.hla_c_result)

        if self.hla_drb1_result is not None and not isinstance(self.hla_drb1_result, BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum):
            self.hla_drb1_result = BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum(self.hla_drb1_result)

        if self.hla_dq_result is not None and not isinstance(self.hla_dq_result, BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum):
            self.hla_dq_result = BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum(self.hla_dq_result)

        if self.sct_conditioning_type is not None and not isinstance(self.sct_conditioning_type, SctConditioningTypeEnum):
            self.sct_conditioning_type = SctConditioningTypeEnum(self.sct_conditioning_type)

        if self.sct_tbi is not None and not isinstance(self.sct_tbi, NoNotreportedUnknownYesEnum):
            self.sct_tbi = NoNotreportedUnknownYesEnum(self.sct_tbi)

        if self.sct_cycles is not None and not isinstance(self.sct_cycles, Decimal):
            self.sct_cycles = Decimal(self.sct_cycles)

        if self.sct_cd34_coll is not None and not isinstance(self.sct_cd34_coll, Decimal):
            self.sct_cd34_coll = Decimal(self.sct_cd34_coll)

        if self.sct_cd34_transplant is not None and not isinstance(self.sct_cd34_transplant, Decimal):
            self.sct_cd34_transplant = Decimal(self.sct_cd34_transplant)

        super().__post_init__(**kwargs)


@dataclass
class SubjectResponse(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/SubjectResponse"]
    class_class_curie: ClassVar[str] = "pcdc:/SubjectResponse"
    class_name: ClassVar[str] = "SubjectResponse"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/SubjectResponse")

    submitter_id: str = None
    type: str = None
    age_at_response: Optional[int] = None
    timings: Optional[Union[dict, Timing]] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    response_category: Optional[Union[str, "ResponseCategoryEnum"]] = None
    tx_prior_response: Optional[Union[str, "TxPriorResponseEnum"]] = None
    interim_response: Optional[Union[str, "InterimResponseEnum"]] = None
    response: Optional[Union[str, "ResponseEnum"]] = None
    response_method: Optional[Union[str, "ResponseMethodEnum"]] = None
    response_system: Optional[Union[str, "ResponseSystemEnum"]] = None
    response_system_version: Optional[str] = None
    necrosis: Optional[Union[str, "NecrosisEnum"]] = None
    necrosis_pct: Optional[int] = None
    bm_pct_blasts_at_response: Optional[int] = None
    bm_analysis_method_at_response: Optional[Union[str, "BmAnalysisMethodAtResponseEnum"]] = None
    anc_at_response: Optional[int] = None
    anc_threshold_at_response: Optional[int] = None
    platelet_count_at_response: Optional[int] = None
    platelet_threshold_at_response: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    symptoms: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    palpable_nodes: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    nodular_splenic: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_at_response is not None and not isinstance(self.age_at_response, int):
            self.age_at_response = int(self.age_at_response)

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.response_category is not None and not isinstance(self.response_category, ResponseCategoryEnum):
            self.response_category = ResponseCategoryEnum(self.response_category)

        if self.tx_prior_response is not None and not isinstance(self.tx_prior_response, TxPriorResponseEnum):
            self.tx_prior_response = TxPriorResponseEnum(self.tx_prior_response)

        if self.interim_response is not None and not isinstance(self.interim_response, InterimResponseEnum):
            self.interim_response = InterimResponseEnum(self.interim_response)

        if self.response is not None and not isinstance(self.response, ResponseEnum):
            self.response = ResponseEnum(self.response)

        if self.response_method is not None and not isinstance(self.response_method, ResponseMethodEnum):
            self.response_method = ResponseMethodEnum(self.response_method)

        if self.response_system is not None and not isinstance(self.response_system, ResponseSystemEnum):
            self.response_system = ResponseSystemEnum(self.response_system)

        if self.response_system_version is not None and not isinstance(self.response_system_version, str):
            self.response_system_version = str(self.response_system_version)

        if self.necrosis is not None and not isinstance(self.necrosis, NecrosisEnum):
            self.necrosis = NecrosisEnum(self.necrosis)

        if self.necrosis_pct is not None and not isinstance(self.necrosis_pct, int):
            self.necrosis_pct = int(self.necrosis_pct)

        if self.bm_pct_blasts_at_response is not None and not isinstance(self.bm_pct_blasts_at_response, int):
            self.bm_pct_blasts_at_response = int(self.bm_pct_blasts_at_response)

        if self.bm_analysis_method_at_response is not None and not isinstance(self.bm_analysis_method_at_response, BmAnalysisMethodAtResponseEnum):
            self.bm_analysis_method_at_response = BmAnalysisMethodAtResponseEnum(self.bm_analysis_method_at_response)

        if self.anc_at_response is not None and not isinstance(self.anc_at_response, int):
            self.anc_at_response = int(self.anc_at_response)

        if self.anc_threshold_at_response is not None and not isinstance(self.anc_threshold_at_response, int):
            self.anc_threshold_at_response = int(self.anc_threshold_at_response)

        if self.platelet_count_at_response is not None and not isinstance(self.platelet_count_at_response, int):
            self.platelet_count_at_response = int(self.platelet_count_at_response)

        if self.platelet_threshold_at_response is not None and not isinstance(self.platelet_threshold_at_response, NoNotreportedUnknownYesEnum):
            self.platelet_threshold_at_response = NoNotreportedUnknownYesEnum(self.platelet_threshold_at_response)

        if self.symptoms is not None and not isinstance(self.symptoms, NoNotreportedUnknownYesEnum):
            self.symptoms = NoNotreportedUnknownYesEnum(self.symptoms)

        if self.palpable_nodes is not None and not isinstance(self.palpable_nodes, NoNotreportedUnknownYesEnum):
            self.palpable_nodes = NoNotreportedUnknownYesEnum(self.palpable_nodes)

        if self.nodular_splenic is not None and not isinstance(self.nodular_splenic, NoNotreportedUnknownYesEnum):
            self.nodular_splenic = NoNotreportedUnknownYesEnum(self.nodular_splenic)

        super().__post_init__(**kwargs)


@dataclass
class MinimalResidualDisease(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/MinimalResidualDisease"]
    class_class_curie: ClassVar[str] = "pcdc:/MinimalResidualDisease"
    class_name: ClassVar[str] = "MinimalResidualDisease"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/MinimalResidualDisease")

    submitter_id: str = None
    type: str = None
    age_at_mrd_assessment: Optional[int] = None
    timings: Optional[Union[dict, Timing]] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    mrd_method: Optional[Union[str, "MrdMethodEnum"]] = None
    flow_cytometry_type: Optional[Union[str, "FlowCytometryTypeEnum"]] = None
    mrd_result: Optional[str] = None
    mrd_result_numeric: Optional[int] = None
    mrd_result_unit: Optional[Union[str, "NotreportedUnknownEnum"]] = None
    mrd_sensitivty: Optional[int] = None
    mrd_sample_source: Optional[Union[str, "MrdSampleSourceEnum"]] = None
    mrd_molecular_markers: Optional[Union[str, "MrdMolecularMarkersEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_at_mrd_assessment is not None and not isinstance(self.age_at_mrd_assessment, int):
            self.age_at_mrd_assessment = int(self.age_at_mrd_assessment)

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.mrd_method is not None and not isinstance(self.mrd_method, MrdMethodEnum):
            self.mrd_method = MrdMethodEnum(self.mrd_method)

        if self.flow_cytometry_type is not None and not isinstance(self.flow_cytometry_type, FlowCytometryTypeEnum):
            self.flow_cytometry_type = FlowCytometryTypeEnum(self.flow_cytometry_type)

        if self.mrd_result is not None and not isinstance(self.mrd_result, str):
            self.mrd_result = str(self.mrd_result)

        if self.mrd_result_numeric is not None and not isinstance(self.mrd_result_numeric, int):
            self.mrd_result_numeric = int(self.mrd_result_numeric)

        if self.mrd_result_unit is not None and not isinstance(self.mrd_result_unit, NotreportedUnknownEnum):
            self.mrd_result_unit = NotreportedUnknownEnum(self.mrd_result_unit)

        if self.mrd_sensitivty is not None and not isinstance(self.mrd_sensitivty, int):
            self.mrd_sensitivty = int(self.mrd_sensitivty)

        if self.mrd_sample_source is not None and not isinstance(self.mrd_sample_source, MrdSampleSourceEnum):
            self.mrd_sample_source = MrdSampleSourceEnum(self.mrd_sample_source)

        if self.mrd_molecular_markers is not None and not isinstance(self.mrd_molecular_markers, MrdMolecularMarkersEnum):
            self.mrd_molecular_markers = MrdMolecularMarkersEnum(self.mrd_molecular_markers)

        super().__post_init__(**kwargs)


@dataclass
class AdverseEvents(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/AdverseEvents"]
    class_class_curie: ClassVar[str] = "pcdc:/AdverseEvents"
    class_name: ClassVar[str] = "AdverseEvents"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/AdverseEvents")

    submitter_id: str = None
    type: str = None
    age_at_ae: Optional[int] = None
    age_at_ae_resolved: Optional[int] = None
    timings: Optional[Union[dict, Timing]] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    adverse_event: Optional[Union[str, "AdverseEventEnum"]] = None
    ae_immune: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    ae_infusion: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    ae_code: Optional[str] = None
    ae_grade_system: Optional[Union[str, "AeGradeSystemEnum"]] = None
    ae_system_version: Optional[str] = None
    ae_grade: Optional[Union[str, "AeGradeEnum"]] = None
    ae_reported: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    ae_attribution: Optional[Union[str, "AeAttributionEnum"]] = None
    ae_outcome: Optional[Union[str, "AeOutcomeEnum"]] = None
    avn_joint: Optional[Union[str, "AvnJointEnum"]] = None
    avn_joint_laterality: Optional[Union[str, "AvnJointLateralityEnum"]] = None
    avn_method: Optional[Union[str, "AvnMethodEnum"]] = None
    orthopedic_procedure: Optional[Union[str, "OrthopedicProcedureEnum"]] = None
    ae_expected: Optional[Union[str, "AeExpectedEnum"]] = None
    ae_tx_mod: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    ae_hospitalization: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    ae_icu: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    ae_medication: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    ae_intervention: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    ae_intervention_detail: Optional[Union[str, "AeInterventionDetailEnum"]] = None
    ae_pathogen: Optional[Union[str, "AePathogenEnum"]] = None
    ae_pathogen_confirmation: Optional[Union[str, "AePathogenConfirmationEnum"]] = None
    infection_classification: Optional[Union[str, "InfectionClassificationEnum"]] = None
    gvhd_acuity: Optional[Union[str, "GvhdAcuityEnum"]] = None
    gvhd_organ: Optional[Union[str, "GvhdOrganEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_at_ae is not None and not isinstance(self.age_at_ae, int):
            self.age_at_ae = int(self.age_at_ae)

        if self.age_at_ae_resolved is not None and not isinstance(self.age_at_ae_resolved, int):
            self.age_at_ae_resolved = int(self.age_at_ae_resolved)

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.adverse_event is not None and not isinstance(self.adverse_event, AdverseEventEnum):
            self.adverse_event = AdverseEventEnum(self.adverse_event)

        if self.ae_immune is not None and not isinstance(self.ae_immune, NoNotreportedUnknownYesEnum):
            self.ae_immune = NoNotreportedUnknownYesEnum(self.ae_immune)

        if self.ae_infusion is not None and not isinstance(self.ae_infusion, NoNotreportedUnknownYesEnum):
            self.ae_infusion = NoNotreportedUnknownYesEnum(self.ae_infusion)

        if self.ae_code is not None and not isinstance(self.ae_code, str):
            self.ae_code = str(self.ae_code)

        if self.ae_grade_system is not None and not isinstance(self.ae_grade_system, AeGradeSystemEnum):
            self.ae_grade_system = AeGradeSystemEnum(self.ae_grade_system)

        if self.ae_system_version is not None and not isinstance(self.ae_system_version, str):
            self.ae_system_version = str(self.ae_system_version)

        if self.ae_grade is not None and not isinstance(self.ae_grade, AeGradeEnum):
            self.ae_grade = AeGradeEnum(self.ae_grade)

        if self.ae_reported is not None and not isinstance(self.ae_reported, NoNotreportedUnknownYesEnum):
            self.ae_reported = NoNotreportedUnknownYesEnum(self.ae_reported)

        if self.ae_attribution is not None and not isinstance(self.ae_attribution, AeAttributionEnum):
            self.ae_attribution = AeAttributionEnum(self.ae_attribution)

        if self.ae_outcome is not None and not isinstance(self.ae_outcome, AeOutcomeEnum):
            self.ae_outcome = AeOutcomeEnum(self.ae_outcome)

        if self.avn_joint is not None and not isinstance(self.avn_joint, AvnJointEnum):
            self.avn_joint = AvnJointEnum(self.avn_joint)

        if self.avn_joint_laterality is not None and not isinstance(self.avn_joint_laterality, AvnJointLateralityEnum):
            self.avn_joint_laterality = AvnJointLateralityEnum(self.avn_joint_laterality)

        if self.avn_method is not None and not isinstance(self.avn_method, AvnMethodEnum):
            self.avn_method = AvnMethodEnum(self.avn_method)

        if self.orthopedic_procedure is not None and not isinstance(self.orthopedic_procedure, OrthopedicProcedureEnum):
            self.orthopedic_procedure = OrthopedicProcedureEnum(self.orthopedic_procedure)

        if self.ae_expected is not None and not isinstance(self.ae_expected, AeExpectedEnum):
            self.ae_expected = AeExpectedEnum(self.ae_expected)

        if self.ae_tx_mod is not None and not isinstance(self.ae_tx_mod, NoNotreportedUnknownYesEnum):
            self.ae_tx_mod = NoNotreportedUnknownYesEnum(self.ae_tx_mod)

        if self.ae_hospitalization is not None and not isinstance(self.ae_hospitalization, NoNotreportedUnknownYesEnum):
            self.ae_hospitalization = NoNotreportedUnknownYesEnum(self.ae_hospitalization)

        if self.ae_icu is not None and not isinstance(self.ae_icu, NoNotreportedUnknownYesEnum):
            self.ae_icu = NoNotreportedUnknownYesEnum(self.ae_icu)

        if self.ae_medication is not None and not isinstance(self.ae_medication, NoNotreportedUnknownYesEnum):
            self.ae_medication = NoNotreportedUnknownYesEnum(self.ae_medication)

        if self.ae_intervention is not None and not isinstance(self.ae_intervention, NoNotreportedUnknownYesEnum):
            self.ae_intervention = NoNotreportedUnknownYesEnum(self.ae_intervention)

        if self.ae_intervention_detail is not None and not isinstance(self.ae_intervention_detail, AeInterventionDetailEnum):
            self.ae_intervention_detail = AeInterventionDetailEnum(self.ae_intervention_detail)

        if self.ae_pathogen is not None and not isinstance(self.ae_pathogen, AePathogenEnum):
            self.ae_pathogen = AePathogenEnum(self.ae_pathogen)

        if self.ae_pathogen_confirmation is not None and not isinstance(self.ae_pathogen_confirmation, AePathogenConfirmationEnum):
            self.ae_pathogen_confirmation = AePathogenConfirmationEnum(self.ae_pathogen_confirmation)

        if self.infection_classification is not None and not isinstance(self.infection_classification, InfectionClassificationEnum):
            self.infection_classification = InfectionClassificationEnum(self.infection_classification)

        if self.gvhd_acuity is not None and not isinstance(self.gvhd_acuity, GvhdAcuityEnum):
            self.gvhd_acuity = GvhdAcuityEnum(self.gvhd_acuity)

        if self.gvhd_organ is not None and not isinstance(self.gvhd_organ, GvhdOrganEnum):
            self.gvhd_organ = GvhdOrganEnum(self.gvhd_organ)

        super().__post_init__(**kwargs)


@dataclass
class LateEffects(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/LateEffects"]
    class_class_curie: ClassVar[str] = "pcdc:/LateEffects"
    class_name: ClassVar[str] = "LateEffects"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/LateEffects")

    submitter_id: str = None
    type: str = None
    age_at_le_eval: Optional[int] = None
    le: Optional[Union[str, "LeEnum"]] = None
    le_detail: Optional[Union[str, "LeDetailEnum"]] = None
    le_sub_detail: Optional[Union[str, "LeSubDetailEnum"]] = None
    le_severity_grade: Optional[Union[str, "LeSeverityGradeEnum"]] = None
    le_ctcae_version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_at_le_eval is not None and not isinstance(self.age_at_le_eval, int):
            self.age_at_le_eval = int(self.age_at_le_eval)

        if self.le is not None and not isinstance(self.le, LeEnum):
            self.le = LeEnum(self.le)

        if self.le_detail is not None and not isinstance(self.le_detail, LeDetailEnum):
            self.le_detail = LeDetailEnum(self.le_detail)

        if self.le_sub_detail is not None and not isinstance(self.le_sub_detail, LeSubDetailEnum):
            self.le_sub_detail = LeSubDetailEnum(self.le_sub_detail)

        if self.le_severity_grade is not None and not isinstance(self.le_severity_grade, LeSeverityGradeEnum):
            self.le_severity_grade = LeSeverityGradeEnum(self.le_severity_grade)

        if self.le_ctcae_version is not None and not isinstance(self.le_ctcae_version, str):
            self.le_ctcae_version = str(self.le_ctcae_version)

        super().__post_init__(**kwargs)


@dataclass
class SecondaryMalignantNeoplasm(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/SecondaryMalignantNeoplasm"]
    class_class_curie: ClassVar[str] = "pcdc:/SecondaryMalignantNeoplasm"
    class_name: ClassVar[str] = "SecondaryMalignantNeoplasm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/SecondaryMalignantNeoplasm")

    submitter_id: str = None
    type: str = None
    age_at_smn: Optional[int] = None
    timings: Optional[Union[dict, Timing]] = None
    disease_phase: Optional[Union[str, "DiseasePhaseEnum"]] = None
    disease_phase_number: Optional[int] = None
    course: Optional[Union[str, "CourseEnum"]] = None
    course_number: Optional[int] = None
    smn_status: Optional[Union[str, "NoNotreportedUnknownYesEnum"]] = None
    smn_morph_sno: Optional[str] = None
    smn_icd_o_morph: Optional[str] = None
    snm_morph_txt: Optional[str] = None
    smn_top_sno: Optional[str] = None
    smn_icd_o_top: Optional[str] = None
    smn_top_txt: Optional[str] = None
    smn_site: Optional[Union[str, "SmnSiteEnum"]] = None
    smn_type: Optional[Union[str, "SmnTypeEnum"]] = None
    smn_field: Optional[Union[str, "SmnFieldEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_at_smn is not None and not isinstance(self.age_at_smn, int):
            self.age_at_smn = int(self.age_at_smn)

        if self.timings is not None and not isinstance(self.timings, Timing):
            self.timings = Timing(**as_dict(self.timings))

        if self.disease_phase is not None and not isinstance(self.disease_phase, DiseasePhaseEnum):
            self.disease_phase = DiseasePhaseEnum(self.disease_phase)

        if self.disease_phase_number is not None and not isinstance(self.disease_phase_number, int):
            self.disease_phase_number = int(self.disease_phase_number)

        if self.course is not None and not isinstance(self.course, CourseEnum):
            self.course = CourseEnum(self.course)

        if self.course_number is not None and not isinstance(self.course_number, int):
            self.course_number = int(self.course_number)

        if self.smn_status is not None and not isinstance(self.smn_status, NoNotreportedUnknownYesEnum):
            self.smn_status = NoNotreportedUnknownYesEnum(self.smn_status)

        if self.smn_morph_sno is not None and not isinstance(self.smn_morph_sno, str):
            self.smn_morph_sno = str(self.smn_morph_sno)

        if self.smn_icd_o_morph is not None and not isinstance(self.smn_icd_o_morph, str):
            self.smn_icd_o_morph = str(self.smn_icd_o_morph)

        if self.snm_morph_txt is not None and not isinstance(self.snm_morph_txt, str):
            self.snm_morph_txt = str(self.snm_morph_txt)

        if self.smn_top_sno is not None and not isinstance(self.smn_top_sno, str):
            self.smn_top_sno = str(self.smn_top_sno)

        if self.smn_icd_o_top is not None and not isinstance(self.smn_icd_o_top, str):
            self.smn_icd_o_top = str(self.smn_icd_o_top)

        if self.smn_top_txt is not None and not isinstance(self.smn_top_txt, str):
            self.smn_top_txt = str(self.smn_top_txt)

        if self.smn_site is not None and not isinstance(self.smn_site, SmnSiteEnum):
            self.smn_site = SmnSiteEnum(self.smn_site)

        if self.smn_type is not None and not isinstance(self.smn_type, SmnTypeEnum):
            self.smn_type = SmnTypeEnum(self.smn_type)

        if self.smn_field is not None and not isinstance(self.smn_field, SmnFieldEnum):
            self.smn_field = SmnFieldEnum(self.smn_field)

        super().__post_init__(**kwargs)


@dataclass
class PatientReportedOutcomesMetadata(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PCDC["/PatientReportedOutcomesMetadata"]
    class_class_curie: ClassVar[str] = "pcdc:/PatientReportedOutcomesMetadata"
    class_name: ClassVar[str] = "PatientReportedOutcomesMetadata"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/pcdc/model/PatientReportedOutcomesMetadata")

    submitter_id: str = None
    type: str = None
    study_id: Optional[Union[str, "StudyIdEnum"]] = None
    pro_measures: Optional[Union[str, "ProMeasuresEnum"]] = None
    pro_measurement_type: Optional[Union[str, "ProMeasurementTypeEnum"]] = None
    raters: Optional[Union[str, "RatersEnum"]] = None
    eligible_age_lower: Optional[int] = None
    eligible_age_upper: Optional[int] = None
    time_point: Optional[Union[str, "TimePointEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.study_id is not None and not isinstance(self.study_id, StudyIdEnum):
            self.study_id = StudyIdEnum(self.study_id)

        if self.pro_measures is not None and not isinstance(self.pro_measures, ProMeasuresEnum):
            self.pro_measures = ProMeasuresEnum(self.pro_measures)

        if self.pro_measurement_type is not None and not isinstance(self.pro_measurement_type, ProMeasurementTypeEnum):
            self.pro_measurement_type = ProMeasurementTypeEnum(self.pro_measurement_type)

        if self.raters is not None and not isinstance(self.raters, RatersEnum):
            self.raters = RatersEnum(self.raters)

        if self.eligible_age_lower is not None and not isinstance(self.eligible_age_lower, int):
            self.eligible_age_lower = int(self.eligible_age_lower)

        if self.eligible_age_upper is not None and not isinstance(self.eligible_age_upper, int):
            self.eligible_age_upper = int(self.eligible_age_upper)

        if self.time_point is not None and not isinstance(self.time_point, TimePointEnum):
            self.time_point = TimePointEnum(self.time_point)

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

class OffTypeEnum(EnumDefinitionImpl):

    Study = PermissibleValue(text="Study",
                                 description="No longer participating in a study; not being followed and will not be retreated.",
                                 meaning=NCIT.C29851)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="OffTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Protocol Therapy",
                PermissibleValue(text="Protocol Therapy",
                                 description="No longer receiving protocol therapy.",
                                 meaning=NCIT.C173257) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class ReasonOffEnum(EnumDefinitionImpl):

    Death = PermissibleValue(text="Death",
                                 description="Specifies whether the life of an entity has ceased.",
                                 meaning=NCIT.C93546)
    Ineligible = PermissibleValue(text="Ineligible",
                                           description="The state or quality of being disqualified by law, rule, or provision.",
                                           meaning=NCIT.C40412)
    Relapse = PermissibleValue(text="Relapse",
                                     description="The return of a disease after a period of remission.",
                                     meaning=NCIT.C38155)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="ReasonOffEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Lost to Follow-Up",
                PermissibleValue(text="Lost to Follow-Up",
                                 description="The subject was not available for follow-up procedures.",
                                 meaning=NCIT.C70740) )
        setattr(cls, "Completion of Follow-Up",
                PermissibleValue(text="Completion of Follow-Up",
                                 description="The follow-up protocols were completed.",
                                 meaning=NCIT.C178071) )
        setattr(cls, "Completion of Planned Therapy",
                PermissibleValue(text="Completion of Planned Therapy",
                                 description="The end of the planned treatment.",
                                 meaning=NCIT.C168935) )
        setattr(cls, "Physician Decision",
                PermissibleValue(text="Physician Decision",
                                 description="A position, opinion or judgment reached after consideration by a physician with reference to subject.",
                                 meaning=NCIT.C48250) )
        setattr(cls, "Withdrawal of Consent",
                PermissibleValue(text="Withdrawal of Consent",
                                 description="When the permission to do something is rescinded or withdrawn.",
                                 meaning=NCIT.C48271) )
        setattr(cls, "Subject/Guardian Refused Further Treatment",
                PermissibleValue(text="Subject/Guardian Refused Further Treatment",
                                 description="The subject or their guardian has refused further treatment.",
                                 meaning=NCIT.C91752) )
        setattr(cls, "Subject Non-Compliance",
                PermissibleValue(text="Subject Non-Compliance",
                                 description="The subject or their guardian has refused further treatment.",
                                 meaning=NCIT.C168934) )
        setattr(cls, "Disease Progression",
                PermissibleValue(text="Disease Progression",
                                 description="The worsening of a disease over time.",
                                 meaning=NCIT.C17747) )
        setattr(cls, "Adverse Event",
                PermissibleValue(text="Adverse Event",
                                 description="Any unfavorable or unintended disease, sign, or symptom (including an abnormal laboratory finding) that is temporally associated with the use of a medical treatment or procedure, and that may or may not be considered related to the medical treatment or procedure. Such events can be related to the intervention, dose, route of administration, patient, or caused by an interaction with another drug(s) or procedure(s).",
                                 meaning=NCIT.C41331) )
        setattr(cls, "Secondary Malignancy",
                PermissibleValue(text="Secondary Malignancy",
                                 description="A malignant neoplasm that arises from a pre-existing lower grade lesion, or as a result of a primary lesion that has spread to secondary sites, or due to a complication of a cancer treatment.",
                                 meaning=NCIT.C4968) )
        setattr(cls, "Study Discontinuation",
                PermissibleValue(text="Study Discontinuation",
                                 description="The act of concluding participation by an enrolled subject prior to completion of all protocol-required elements in a trial. NOTE: Four categories of discontinuation are distinguished: a) dropout: Active discontinuation by a subject (also a noun referring to such a discontinued subject); b) investigator initiated discontinuation (e.g., for cause); c) loss to follow-up: cessation of participation without notice or action by the subject; d) sponsor initiated discontinuation. Note that subject discontinuation does not necessarily imply exclusion of subject data from analysis. "Termination of subject" has a history of synonymous use, but is now considered nonstandard. [After ICH E3, section 10.1 and FDA Guidance for Industry: Submission of Abbreviated Reports & Synopses in Support of Marketing Applications, IV A]",
                                 meaning=NCIT.C142444) )
        setattr(cls, "Failure to Attain Remission",
                PermissibleValue(text="Failure to Attain Remission",
                                 description="Remission status was not attained.",
                                 meaning=NCIT.C178072) )
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

class ConditionEnum(EnumDefinitionImpl):

    Hemihypertrophy = PermissibleValue(text="Hemihypertrophy",
                                                     description="A finding indicating the presence of greater than normal asymmetry between the right and left sides of the body. The asymmetry may be manifested in the entire side or part of it.",
                                                     meaning=NCIT.C88541)
    Psoriasis = PermissibleValue(text="Psoriasis",
                                         description="An autoimmune condition characterized by red, well-delineated plaques with silvery scales that are usually on the extensor surfaces and scalp. They can occasionally present with these manifestations: pustules; erythema and scaling in intertriginous areas, and erythroderma, that are often distributed on extensor surfaces and scalp.",
                                         meaning=NCIT.C3346)
    Scleroderma = PermissibleValue(text="Scleroderma",
                                             description="A localized or systemic chronic and progressive autoimmune disorder characterized by thickening of the skin and the connective tissues. Localized scleroderma affects only the skin. Systemic scleroderma affects internal organs, including the heart, lungs, gastrointestinal tract, and kidneys.",
                                             meaning=NCIT.C26746)
    Vitiligo = PermissibleValue(text="Vitiligo",
                                       description="Generalized well circumscribed patches of leukoderma that are generally distributed over symmetric body locations and is due to autoimmune destruction of melanocytes.",
                                       meaning=NCIT.C26915)
    Clubfoot = PermissibleValue(text="Clubfoot",
                                       description="The most common congenital deformation of the foot, occurring in 1 of 1,000 live births. The most common form is talipes equinovarus, where the deformed foot is turned downward and inward sharply.",
                                       meaning=NCIT.C84641)
    Gastroschisis = PermissibleValue(text="Gastroschisis",
                                                 description="A congenital birth defect characterized by the exposure of the fetal intestines outside the abdominal wall through an abdominal wall opening.",
                                                 meaning=NCIT.C84725)
    Cherubism = PermissibleValue(text="Cherubism",
                                         description="A rare autosomal dominant inherited disorder usually caused by mutations in the SH3BP2 gene. It is characterized by a prominent lower part of the face due to bilateral replacement of the mandibular or maxillary bones by lesions. The lesions contain osteoclast-like cells admixed with spindle-shaped mononuclear stromal cells. With time, the lesions become more fibrotic and less osteoclast-rich.",
                                         meaning=NCIT.C84630)
    Retinoblastoma = PermissibleValue(text="Retinoblastoma",
                                                   description="A malignant tumor that originates in the nuclear layer of the retina. As the most common primary tumor of the eye in children, retinoblastoma is still relatively uncommon, accounting for only 1% of all malignant tumors in pediatric patients. Approximately 95% of cases are diagnosed before age 5. These tumors may be multifocal, bilateral, congenital, inherited, or acquired. Seventy-five percent of retinoblastomas are unilateral; 60% occur sporadically. A predisposition to retinoblastoma has been associated with 13q14 cytogenetic abnormalities. Patients with the inherited form also appear to be at increased risk for secondary nonocular malignancies such as osteosarcoma, malignant fibrous histiocytoma, and fibrosarcoma.",
                                                   meaning=NCIT.C7541)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="ConditionEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Adenomatous Polyposis Coli",
                PermissibleValue(text="Adenomatous Polyposis Coli",
                                 description="Adenomatous polyposis coli protein (2843 aa, ~312 kDa) is encoded by the human APC gene. This protein is involved in both tumor suppression and the inhibition of the Wnt signaling pathway.",
                                 meaning=NCIT.C17687) )
        setattr(cls, "Costello Syndrome",
                PermissibleValue(text="Costello Syndrome",
                                 description="A genetic syndrome caused by mutations in the HRAS gene. It is characterized by developmental delay, mental retardation, loose skin folds, cardiomyopathy, tachycardia, and structural heart defects. Patients are at an increased risk of developing benign or malignant neoplasms.",
                                 meaning=NCIT.C84652) )
        setattr(cls, "DICER1 Syndrome",
                PermissibleValue(text="DICER1 Syndrome",
                                 description="A rare, autosomal dominant inherited syndrome caused by mutations in the DICER1 gene. People with this syndrome are at an increased risk of developing pleuropulmonary blastoma, cystic nephroma, Sertoli-Leydig cell tumor of the ovary, and multinodular goiter.",
                                 meaning=NCIT.C123317) )
        setattr(cls, "Li-Fraumeni Syndrome",
                PermissibleValue(text="Li-Fraumeni Syndrome",
                                 description="An autosomal dominant cancer predisposition syndrome caused by germline mutations of the TP53 gene. It is characterized by the development of malignant neoplasms at various anatomic sites. The malignant neoplasms associated with Li-Fraumeni syndrome include breast carcinoma, choroid plexus carcinoma, adrenal cortex carcinoma, gastric carcinoma, colorectal carcinoma, thyroid gland carcinoma, kidney carcinoma, prostate carcinoma, astrocytic tumors, medulloblastoma, osteosarcoma, soft tissue sarcoma, leukemia, and non-Hodgkin lymphoma.",
                                 meaning=NCIT.C3476) )
        setattr(cls, "Neurofibromatosis Type 1",
                PermissibleValue(text="Neurofibromatosis Type 1",
                                 description="The most common type of neurofibromatosis. It is characterized clinically by cutaneous and subcutaneous tumors with patches of hyperpigmentation. The hyperpigmented skin areas, are present from birth and found anywhere on the body surface. They can vary markedly in size and color. The dark brown areas are called cafe-au-lait spots. The multiple cutaneous and subcutaneous tumors are nerve sheath tumors, called neurofibromas. They can develop anywhere along the peripheral nerve fibers. Neurofibromas can become quite large, causing a major disfigurement, eroding bone, and compressing various peripheral nerve structures. Type 1 neurofibromatosis has dominant inheritance, with a gene locus on the proximal long arm of chromosome 17.",
                                 meaning=NCIT.C3273) )
        setattr(cls, "RB Transcriptional Corepressor 1",
                PermissibleValue(text="RB Transcriptional Corepressor 1",
                                 description="The protein encoded by this gene is a negative regulator of the cell cycle and was the first tumor suppressor gene found. The encoded protein also stabilizes constitutive heterochromatin to maintain the overall chromatin structure. The active, hypophosphorylated form of the protein binds transcription factor E2F1. Defects in this gene are a cause of childhood cancer retinoblastoma (RB), bladder cancer, and osteogenic sarcoma.",
                                 meaning=HGNC["9884"]) )
        setattr(cls, "Secondary Malignancy",
                PermissibleValue(text="Secondary Malignancy",
                                 description="A malignant neoplasm that arises from a pre-existing lower grade lesion, or as a result of a primary lesion that has spread to secondary sites, or due to a complication of a cancer treatment.",
                                 meaning=NCIT.C4968) )
        setattr(cls, "Trisomy 21",
                PermissibleValue(text="Trisomy 21",
                                 description="A chromosomal abnormality consisting of the presence of a third copy of chromosome 21 in somatic cells.",
                                 meaning=NCIT.C43224) )
        setattr(cls, "Trisomy 21 Mosaicism",
                PermissibleValue(text="Trisomy 21 Mosaicism",
                                 description="The presence of cells with and without three copies of chromosome 21 in either somatic or germinal tissue.",
                                 meaning=NCIT.C142099) )
        setattr(cls, "Turner Syndrome",
                PermissibleValue(text="Turner Syndrome",
                                 description="A gonadal dysgenesis syndrome occurring in phenotypic females, characterized by the absence of a part or all of one of the sex chromosomes. Signs and symptoms include short stature, webbing of neck, low-set ears, hypogonadism, and sterility.",
                                 meaning=NCIT.C26900) )
        setattr(cls, "Klinerfelter Syndrome",
                PermissibleValue(text="Klinerfelter Syndrome",
                                 description="A sex chromosome disorder caused by the presence of an extra X chromosome in the male karyotype. Affected individuals are infertile and have a small penis and testes. They tend to have tall stature and long legs and may have difficulties with speech and language development. Gynecomastia may be present.",
                                 meaning=NCIT.C34752) )
        setattr(cls, "Swyer Syndrome",
                PermissibleValue(text="Swyer Syndrome",
                                 description="A rare syndrome characterized by the presence of a small lung as a result of unilateral post-infectious bronchiolitis obliterans.",
                                 meaning=NCIT.C85178) )
        setattr(cls, "Frasier Syndrome",
                PermissibleValue(text="Frasier Syndrome",
                                 description="A condition, which typically presents during adolescence, that is caused by WT-1 mutation, and is characterized by a developmental sex disorder, FSGS, and may be associated with gonadoblastoma.",
                                 meaning=NCIT.C122805) )
        setattr(cls, "Gonadal Dysgenesis",
                PermissibleValue(text="Gonadal Dysgenesis",
                                 description="A congenital disorder characterized by the presence of extremely hypoplastic gonads preventing the development of secondary sex characteristics",
                                 meaning=NCIT.C61420) )
        setattr(cls, "Fanconi Anemia",
                PermissibleValue(text="Fanconi Anemia",
                                 description="An autosomal recessive genetic disorder characterized by bone marrow failure, skeletal abnormalities, and an increase incidence of development of neoplasias.",
                                 meaning=NCIT.C62505) )
        setattr(cls, "Lynch Syndrome",
                PermissibleValue(text="Lynch Syndrome",
                                 description="An autosomal dominant hereditary neoplastic syndrome characterized by the development of colorectal carcinoma and a high risk of developing endometrial carcinoma, gastric carcinoma, ovarian carcinoma, renal pelvis carcinoma, and small intestinal carcinoma. Patients often develop colorectal carcinomas at an early age (mean, 45 years). In the majority of the cases the lesions arise from the proximal colon. At the molecular level, high-frequency microsatellite instability is present.",
                                 meaning=NCIT.C8494) )
        setattr(cls, "Breast and Ovarian Cancer",
                PermissibleValue(text="Breast and Ovarian Cancer",
                                 description="An autosomal dominant inherited syndrome caused by mutations in the BRCA1 or BRCA2 genes. Patients are at high risk of developing breast cancer, particularly before the age of fifty, high risk of developing a second primary breast cancer, and high risk of developing both breast and ovarian cancer.",
                                 meaning=NCIT.C8493) )
        setattr(cls, "Beckwith-Wiedemann Syndrome",
                PermissibleValue(text="Beckwith-Wiedemann Syndrome",
                                 description="A genetic syndrome caused by abnormalities in chromosome 11. It is characterized by large birth weight, macroglossia, umbilical hernia, ear abnormalities, and hypoglycemia. Patients with this syndrome have an increased risk of developing embryonal tumors (gonadoblastoma, hepatoblastoma, Wilms tumor, Rhabdomyosarcoma) and adrenal cortex carcinomas.",
                                 meaning=NCIT.C34415) )
        setattr(cls, "Central Hypoventilation Syndrome",
                PermissibleValue(text="Central Hypoventilation Syndrome",
                                 description="A disorder characterized by hypoventilation and hypoxemia. It appears early in life and is not associated with cardiopulmonary or neuromuscular abnormalities.",
                                 meaning=NCIT.C98889) )
        setattr(cls, "Cushings Syndrome",
                PermissibleValue(text="Cushings Syndrome",
                                 description="A syndrome caused by high levels of cortisol in the blood either due to excessive production and secretion of corticosteroids secondary to pituitary or adrenocortical neoplasms, or intake of glucocorticoid drugs. Signs and symptoms include a round face, upper body obesity, fragile and thin skin, purple stretch marks in the skin, fatigue, muscle weakness, hypertension, diabetes mellitus, hypertrichosis and amenorrhea in women, impotence in men, and osteoporosis.",
                                 meaning=NCIT.C2969) )
        setattr(cls, "Denys-Drash Syndrome",
                PermissibleValue(text="Denys-Drash Syndrome",
                                 description="A rare congenital syndrome caused by mutations in the WT1 gene. It is characterized by the presence of congenital nephropathy (diffuse mesangial sclerosis), Wilms tumor, and intersex disorders.",
                                 meaning=NCIT.C84668) )
        setattr(cls, "Down Syndrome",
                PermissibleValue(text="Down Syndrome",
                                 description="A chromosomal dysgenesis syndrome resulting from a triplication or translocation of chromosome 21. Down syndrome occurs in approximately 1:700 live births. Abnormalities are variable from individual to individual and may include mental retardation, retarded growth, flat hypoplastic face with short nose, prominent epicanthic skin folds, small low-set ears with prominent antihelix, fissured and thickened tongue, laxness of joint ligaments, pelvic dysplasia, broad hands and feet, stubby fingers, transverse palmar crease, lenticular opacities and heart disease. Patients with Down syndrome have an estimated 10 to 30-fold increased risk for leukemia; most have symptoms of Alzheimer's disease by age 40. Also known as trisomy 21 syndrome.",
                                 meaning=NCIT.C2993) )
        setattr(cls, "Gorlin Syndrome",
                PermissibleValue(text="Gorlin Syndrome",
                                 description="An autosomal dominant genetic syndrome caused by abnormalities in the PTCH gene. It is characterized by multiple basal cell carcinomas at a young age, odontogenic keratocysts, and skeletal defects (bifurcated and splayed ribs, fusion of vertebrae, spinal bifida). Patients with this syndrome may also develop medulloblastomas and ovarian fibromas.",
                                 meaning=NCIT.C2892) )
        setattr(cls, "Heretidary Retinoblastoma",
                PermissibleValue(text="Heretidary Retinoblastoma",
                                 description="An inherited malignant tumor that originates in the nuclear layer of the retina. A predisposition to retinoblastoma has been associated with 13q14 cytogenetic abnormalities. Patients with the inherited form appear to be at increased risk for secondary nonocular malignancies such as osteosarcoma, malignant fibrous histiocytoma, and fibrosarcoma.",
                                 meaning=NCIT.C8495) )
        setattr(cls, "Hirschprung Disease",
                PermissibleValue(text="Hirschprung Disease",
                                 description="A congenital disorder characterized by the absence of myenteric ganglion cells in the distal colon. It results in a functional stenosis of the distal colon and a massive distention of the proximal colon.",
                                 meaning=NCIT.C34700) )
        setattr(cls, "Noonan Syndrome",
                PermissibleValue(text="Noonan Syndrome",
                                 description="A genetic syndrome caused by mutations in the PTPN11 gene (over 50% of the cases) or less frequently mutations in the SOS1, RAF1, or KRAS genes. It is characterized by short stature, webbed neck, hypertelorism, low-set ears, deafness, and thrombocytopenia or abnormal platelet function.",
                                 meaning=NCIT.C34854) )
        setattr(cls, "WAGR Syndrome",
                PermissibleValue(text="WAGR Syndrome",
                                 description="A very rare congenital condition involving the complex of Wilms tumor, aniridia, genitourinary abnormalities, and mental retardation. Wilms Tumor-Aniridia-Genitourinary Anomalies-Mental Retardation (WAGR) syndrome involves deletions of several adjacent genes in chromosome region 11p13. Two or more of the four conditions must be present for an individual to be diagnosed with WAGR Syndrome. The clinical picture varies, depending upon the combination of abnormalities.",
                                 meaning=NCIT.C3718) )
        setattr(cls, "Werner Syndrome",
                PermissibleValue(text="Werner Syndrome",
                                 description="A rare, autosomal recessive syndrome caused by mutations in the WRN gene. It is characterized by the appearance of accelerated aging following puberty. It is associated with the development of diabetes mellitus, atherosclerosis, cataracts, and cancer.",
                                 meaning=NCIT.C3447) )
        setattr(cls, "Celiac Disease",
                PermissibleValue(text="Celiac Disease",
                                 description="An autoimmune genetic disorder with an unknown pattern of inheritance that primarily affects the digestive tract. It is caused by intolerance to dietary gluten. Consumption of gluten protein triggers an immune response which damages small intestinal villi and prevents adequate absorption of nutrients. Clinical signs include abdominal cramping, diarrhea or constipation and weight loss. If untreated, the clinical course may progress to malnutrition, anemia, osteoporosis and an increased risk of intestinal malignancies. However, the prognosis is favorable with successful avoidance of gluten in the diet.",
                                 meaning=NCIT.C26714) )
        setattr(cls, "Diabetes Mellitus (Type I)",
                PermissibleValue(text="Diabetes Mellitus (Type I)",
                                 description="A chronic condition characterized by minimal or absent production of insulin by the pancreas.",
                                 meaning=NCIT.C2986) )
        setattr(cls, "Goodpasture's Syndrome",
                PermissibleValue(text="Goodpasture's Syndrome",
                                 description="An autoimmune disorder characterized by pulmonary hemorrhage and glomerulonephritis. It is a hypersensitivity reaction resulting in the formation of antibodies against the pulmonary alveoli and the basement membrane of the glomeruli.",
                                 meaning=NCIT.C34649) )
        setattr(cls, "Graves' Disease",
                PermissibleValue(text="Graves' Disease",
                                 description="Hyperthyroidism associated with diffuse hyperplasia of the thyroid gland (goiter), resulting from production of antibodies that are directed against the thyrotropin receptor complex of the follicular epithelial cells. As a result, the thyroid gland enlarges and secrets increased amounts of thyroid hormones.",
                                 meaning=NCIT.C3071) )
        setattr(cls, "Hashimoto's Thyroiditis",
                PermissibleValue(text="Hashimoto's Thyroiditis",
                                 description="An autoimmune disorder caused by the production of autoantibodies against thyroid tissue. There is progressive destruction of the thyroid follicles leading to hypothyroidism.",
                                 meaning=NCIT.C27191) )
        setattr(cls, "Inflammatory Bowel Disease",
                PermissibleValue(text="Inflammatory Bowel Disease",
                                 description="A spectrum of small and large bowel inflammatory diseases of unknown etiology. It includes Crohn's disease, ulcerative colitis, and colitis of indeterminate type.",
                                 meaning=NCIT.C3138) )
        setattr(cls, "Juvenile Idiopathic Arthritis",
                PermissibleValue(text="Juvenile Idiopathic Arthritis",
                                 description="A group of chronic, inflammatory childhood disorders of unknown etiology that primarily involve joints.",
                                 meaning=NCIT.C114357) )
        setattr(cls, "Multiple Sclerosis",
                PermissibleValue(text="Multiple Sclerosis",
                                 description="A progressive autoimmune disorder affecting the central nervous system resulting in demyelination. Patients develop physical and cognitive impairments that correspond with the affected nerve fibers.",
                                 meaning=NCIT.C3243) )
        setattr(cls, "Systematic Lupus Erythematosus",
                PermissibleValue(text="Systematic Lupus Erythematosus",
                                 description="An autoimmune multi-organ disease typically associated with vasculopathy and autoantibody production. Most patients have antinuclear antibodies (ANA). The presence of anti-dsDNA or anti-Smith antibodies are highly-specific.",
                                 meaning=NCIT.C3201) )
        setattr(cls, "Cleft Lip",
                PermissibleValue(text="Cleft Lip",
                                 description="A congenital abnormality consisting of one or more clefts (splits) in the upper lip, which may be accompanied by a cleft palate; it is the result of the failure of the embryonic parts of the lip to fuse.",
                                 meaning=NCIT.C87175) )
        setattr(cls, "Cleft Palate",
                PermissibleValue(text="Cleft Palate",
                                 description="A congenital abnormality consisting of a fissure in the midline of the hard and/or soft palate; it is the result of the failure of the two sides of the palate to fuse during embryonic development.",
                                 meaning=NCIT.C87069) )
        setattr(cls, "Heart Defect",
                PermissibleValue(text="Heart Defect",
                                 description="Genetic anomalies and collections of malformations that are known to cluster together that can be associated with congenital heart defects.",
                                 meaning=NCIT.C168217) )
        setattr(cls, "Mixed Connective Tissue Disease",
                PermissibleValue(text="Mixed Connective Tissue Disease",
                                 description="An autoimmune overlap syndrome characterized by the presence of symptoms of systemic lupus erythematosus, systemic scleroderma, and polymyositis.",
                                 meaning=NCIT.C84892) )
        setattr(cls, "Neurofibromatosis Type 2",
                PermissibleValue(text="Neurofibromatosis Type 2",
                                 description="An autosomal dominant disorder caused by mutations in the NF2 tumor suppressor gene. It is characterized by the development of peripheral and central nervous system tumors including acoustic schwannomas, neurofibromas, gliomas, and meningiomas.",
                                 meaning=NCIT.C3274) )
        setattr(cls, "Bloom Syndrome",
                PermissibleValue(text="Bloom Syndrome",
                                 description="An autosomal dominant inherited syndrome caused by mutations in the BRCA1 or BRCA2 genes. Patients are at high risk of developing breast cancer, particularly before the age of fifty, high risk of developing a second primary breast cancer, and high risk of developing both breast and ovarian cancer.",
                                 meaning=NCIT.C8493) )
        setattr(cls, "Ollier Disease",
                PermissibleValue(text="Ollier Disease",
                                 description="A rare benign disorder characterized by lack of normal endochondral ossification, and the growth of multiple enchondromas. It primarily affects the bones of the hand, in children and young adults. Extent of the disease varies; in some cases, neoplastic involvement may be widespread causing considerable deformity.",
                                 meaning=NCIT.C3008) )
        setattr(cls, "Maffucci Syndrome",
                PermissibleValue(text="Maffucci Syndrome",
                                 description="A rare non-inherited disorder primarily affecting the skin and skeletal system. It is classified as a mesodermal dysplasia. Clinical signs appear within the first decade and are characterized by multiple soft tissue hemiangiomas and enchondromas leading to skeletal deformities. Clinical course is progressive with variable development of associated malignancies.",
                                 meaning=NCIT.C3213) )
        setattr(cls, "Multiple Osteochondromas",
                PermissibleValue(text="Multiple Osteochondromas",
                                 description="An autosomal dominant neoplastic chondrogenic process affecting multiple sites. It is caused by mutations in the EXT1 or EXT2 genes. Grossly and microscopically, the lesions resemble an osteochondroma.",
                                 meaning=NCIT.C53457) )
        setattr(cls, "McCune-Albright Syndrome",
                PermissibleValue(text="McCune-Albright Syndrome",
                                 description="A syndrome characterized by the presence of polyostotic fibrous dysplasia, cafe-au-lait skin lesions, and sexual precocity. It is caused by mutations within the GNAS genetic locus.",
                                 meaning=NCIT.C48627) )
        setattr(cls, "Rothmund-Thomson Syndrome",
                PermissibleValue(text="Rothmund-Thomson Syndrome",
                                 description="An autosomal recessive inherited syndrome usually caused by mutations in the RECQL4 gene. It is characterized by poikilodermatous skin changes, sparse hair, cataracts, small stature, skeletal abnormalities, and an increased predisposition to cancer, particularly osteosarcoma.",
                                 meaning=NCIT.C3335) )
        setattr(cls, "Paget Disease",
                PermissibleValue(text="Paget Disease",
                                 description="A malignant neoplasm composed of large cells with large nuclei, prominent nucleoli, and abundant pale cytoplasm (Paget cells). Paget cell neoplasms include Paget disease of the nipple and extramammary Paget disease which may affect the vulva, penis, anus, skin and scrotum.",
                                 meaning=NCIT.C7073) )
        setattr(cls, "Gardner Syndrome",
                PermissibleValue(text="Gardner Syndrome",
                                 description="A variant of familial adenomatous polyposis. It is an autosomal dominant syndrome characterized by multiple colonic polyps predisposing to carcinoma of the colon, osteomas of the skull, epidermoid cysts, and fibromas. It is associated with mutation of the APC gene.",
                                 meaning=NCIT.C6728) )
        setattr(cls, "Diamond-Blackfan Anemia",
                PermissibleValue(text="Diamond-Blackfan Anemia",
                                 description="An inherited condition characterized by aplasia of the erythroid series only. The white cells and platelets are not affected. Patients develop anemia usually in infancy.",
                                 meaning=NCIT.C61236) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class ConditionTypeEnum(EnumDefinitionImpl):

    Cancer = PermissibleValue(text="Cancer",
                                   description="Diseases involving abnormal cell growth with the potential to invade or spread to other parts of the body.",
                                   meaning=NCIT.C9305)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="ConditionTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Genetic Syndrome",
                PermissibleValue(text="Genetic Syndrome",
                                 description="Genetic diseases are diseases in which inherited genes predispose to increased risk. The genetic disorders associated with cancer often result from an alteration or mutation in a single gene. The diseases range from rare dominant cancer family syndrome to familial tendencies in which low-penetrance genes may interact with other genes or environmental factors to induce cancer. Research may involve clinical, epidemiologic, and laboratory studies of persons, families, and populations at high risk of these disorders.",
                                 meaning=NCIT.C3101) )
        setattr(cls, "Autoimmune Disease",
                PermissibleValue(text="Autoimmune Disease",
                                 description="A disorder resulting from loss of function or tissue destruction of an organ or multiple organs, arising from humoral or cellular immune responses of the individual to his own tissue constituents. It may be systemic (e.g., systemic lupus erythematosus), or organ specific, (e.g., thyroiditis).",
                                 meaning=NCIT.C2889) )
        setattr(cls, "Congenital Anomaly",
                PermissibleValue(text="Congenital Anomaly",
                                 description="Any abnormality, anatomical or biochemical, evident at birth or during the neonatal period.",
                                 meaning=NCIT.C2849) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class AssistedConceptionEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Not known, observed, recorded; or reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="AssistedConceptionEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "In Vitro Fertilization",
                PermissibleValue(text="In Vitro Fertilization",
                                 description="Fertilization of an ovum outside of the body.",
                                 meaning=NCIT.C16580) )
        setattr(cls, "Intracytoplasmic Sperm Injection",
                PermissibleValue(text="Intracytoplasmic Sperm Injection",
                                 description="Injecting a single sperm into the center of an egg.",
                                 meaning=NCIT.C185482) )
        setattr(cls, "Not reported",
                PermissibleValue(text="Not reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class LkssEnum(EnumDefinitionImpl):

    Alive = PermissibleValue(text="Alive",
                                 description="Showing characteristics of life; displaying signs of life.",
                                 meaning=NCIT.C37987)
    Dead = PermissibleValue(text="Dead",
                               description="The cessation of life.",
                               meaning=NCIT.C28554)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="LkssEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C28554) )

class CauseOfDeathEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="CauseOfDeathEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Disease Progression",
                PermissibleValue(text="Disease Progression",
                                 description="An indication that the subject has died due to the progression of their disease.",
                                 meaning=NCIT.C168970) )
        setattr(cls, "Pre-Treatment Disease Complications",
                PermissibleValue(text="Pre-Treatment Disease Complications",
                                 description="A complication of the disease that existed prior to treatment.",
                                 meaning=NCIT.C168876) )
        setattr(cls, "Post-Treatment Disease Complications",
                PermissibleValue(text="Post-Treatment Disease Complications",
                                 description="A complication of the disease that occurred after treatment.",
                                 meaning=NCIT.C168877) )
        setattr(cls, "Treatment-Related Mortality",
                PermissibleValue(text="Treatment-Related Mortality",
                                 description="A death that is considered to be causally linked to a treatment.",
                                 meaning=NCIT.C166165) )
        setattr(cls, "Secondary Malignancy",
                PermissibleValue(text="Secondary Malignancy",
                                 description="A malignant neoplasm that arises from a pre-existing lower grade lesion, or as a result of a primary lesion that has spread to secondary sites, or due to a complication of a cancer treatment.",
                                 meaning=NCIT.C4968) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class TrmTypeEnum(EnumDefinitionImpl):

    Immunotherapy = PermissibleValue(text="Immunotherapy",
                                                 description="Therapy designed to induce changes in a patient's immune status in order to treat disease.",
                                                 meaning=NCIT["C15262 "])
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="TrmTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Stem Cell Transplant",
                PermissibleValue(text="Stem Cell Transplant",
                                 description="A therapeutic procedure that involves the transplantation of hematopoietic stem cells, either with the patient as their own donor or from a donor to a patient. This can be used for treatment of malignant and non-malignant diseases.",
                                 meaning=NCIT["C15431 "]) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class CauseOfDeathDetailEnum(EnumDefinitionImpl):

    Hemorrhage = PermissibleValue(text="Hemorrhage",
                                           description="In medicine, loss of blood from damaged blood vessels. A hemorrhage may be internal or external, and usually involves a lot of bleeding in a short time.",
                                           meaning=NCIT.C26791)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="CauseOfDeathDetailEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Acute Respiratory Distress Syndrome",
                PermissibleValue(text="Acute Respiratory Distress Syndrome",
                                 description="Progressive and life-threatening pulmonary distress in the absence of an underlying pulmonary condition, usually following major trauma or surgery. Cases of neonatal respiratory distress syndrome are not included in this definition.",
                                 meaning=NCIT.C3353) )
        setattr(cls, "Bacterial Infection",
                PermissibleValue(text="Bacterial Infection",
                                 description="An acute infectious disorder that is caused by gram positive or gram negative bacteria; representative examples include pneumococcal, streptococcal, salmonella, and meningeal infections.",
                                 meaning=NCIT.C2890) )
        setattr(cls, "Cardiac Disease",
                PermissibleValue(text="Cardiac Disease",
                                 description="A non-neoplastic or neoplastic disorder that affects the heart and/or the pericardium. Representative examples include endocarditis, pericarditis, atrial myxoma, cardiac myeloid sarcoma, and pericardial malignant mesothelioma.",
                                 meaning=NCIT.C3079) )
        setattr(cls, "Cardiac Failure",
                PermissibleValue(text="Cardiac Failure",
                                 description="Inability of the heart to pump blood at an adequate rate to meet tissue metabolic requirements. Clinical symptoms of heart failure include: unusual dyspnea on light exertion, recurrent dyspnea occurring in the supine position, fluid retention or rales, jugular venous distension, pulmonary edema on physical exam, or pulmonary edema on chest x-ray presumed to be cardiac dysfunction.",
                                 meaning=NCIT.C50577) )
        setattr(cls, "Fungal Infection",
                PermissibleValue(text="Fungal Infection",
                                 description="An infection caused by a fungus.",
                                 meaning=NCIT.C3245) )
        setattr(cls, "Graft Versus Host Disease",
                PermissibleValue(text="Graft Versus Host Disease",
                                 description="A reaction, which may be fatal, in an immunocompromised subject (host) who has received an antigenically incompatible tissue transplant (graft) from an immunocompetent donor. The reaction is secondary to the activation of the transplanted cells against those host tissues that express an antigen not expressed by the donor, and is seen most commonly following bone marrow transplantation; acute disease is seen after 5-40 days, and chronic disease occurs weeks to months after transplantation.",
                                 meaning=NCIT.C3063) )
        setattr(cls, "Infection, NOS",
                PermissibleValue(text="Infection, NOS",
                                 description="The invasion of an organism's body tissues by disease-causing agents and their multiplication, as well as the reaction by the host to these organisms and/or toxins that the organisms produce.",
                                 meaning=NCIT.C128320) )
        setattr(cls, "Multi-Organ Failure",
                PermissibleValue(text="Multi-Organ Failure",
                                 description="Complete impairment of two or more organs or organ systems.",
                                 meaning=NCIT.C75568) )
        setattr(cls, "Organ Failure, NOS",
                PermissibleValue(text="Organ Failure, NOS",
                                 description="The failure of an essential system in the body.",
                                 meaning=NCIT.C185320) )
        setattr(cls, "Pulmonary Disease",
                PermissibleValue(text="Pulmonary Disease",
                                 description="A non-neoplastic or neoplastic disorder affecting the lung. Representative examples of non-neoplastic disorders include chronic obstructive pulmonary disease and pneumonia. Representative examples of neoplastic disorders include benign processes (e.g., respiratory papilloma) and malignant processes (e.g., lung carcinoma and metastatic cancer to the lung).",
                                 meaning=NCIT.C3198) )
        setattr(cls, "Sinusoidal Obstruction Syndrome",
                PermissibleValue(text="Sinusoidal Obstruction Syndrome",
                                 description="A disorder characterized by inflammation and damage of the hepatic sinusoidal endothelial cells of the hepatic venules that leads to venular occlusion and hepatocellular necrosis. It is most often a conditioning-related toxicity that results as a complication of hematopoietic stem cell transplantation (HSCT). It has also been described in populations of individuals who have ingested pyrrolizidine plant alkaloids. The clinical signs and symptoms include hyperbilirubinemia, hepatomegaly, and fluid retention.",
                                 meaning=NCIT.C26793) )
        setattr(cls, "Surgical Complication",
                PermissibleValue(text="Surgical Complication",
                                 description="A disease or disorder that occurs during, soon after or as a result of a surgical procedure.",
                                 meaning=NCIT.C164157) )
        setattr(cls, "Viral Infection",
                PermissibleValue(text="Viral Infection",
                                 description="Any disease caused by a virus.",
                                 meaning=NCIT.C3439) )
        setattr(cls, "Immunotherapy-Related",
                PermissibleValue(text="Immunotherapy-Related",
                                 description="An observation that a situation is related to immunotherapy received.",
                                 meaning=NCIT.C168874) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class CauseOfDeathRankingEnum(EnumDefinitionImpl):

    Primary = PermissibleValue(text="Primary",
                                     description="The first significant event which ultimately led to death.",
                                     meaning=NCIT.C99531)
    Contributory = PermissibleValue(text="Contributory",
                                               description="Any adverse event contributing to the cause of death.",
                                               meaning=NCIT.C168948)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="CauseOfDeathRankingEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class MeasurementTypeEnum(EnumDefinitionImpl):

    Weight = PermissibleValue(text="Weight",
                                   description="The weight of a subject.",
                                   meaning=NCIT.C81328)
    Height = PermissibleValue(text="Height",
                                   description="The vertical measurement or distance from the base to the top of a subject or participant.",
                                   meaning=NCIT.C164634)
    Pulse = PermissibleValue(text="Pulse",
                                 description="The rhythmic wave within the arteries occurring with each contraction of the left ventricle.",
                                 meaning=NCIT.C25749)
    Temperature = PermissibleValue(text="Temperature",
                                             description="A measure of the average kinetic energy of a system of particles. Temperature may be quantified, in the context of thermodynamics, as the potential of one system to transfer thermal energy to another system until both systems reach a state of thermal equilibrium.",
                                             meaning=NCIT.C25206)
    BMI = PermissibleValue(text="BMI",
                             description="The result of a body mass index measurement.",
                             meaning=NCIT.C138901)
    BSA = PermissibleValue(text="BSA",
                             description="A measure of the 2-dimensional extent of the body surface (i.e., the skin). Body surface area (BSA) can be calculated by mathematical formula or from a chart that relates height to weight. BSA is often an important factor in dosing.",
                             meaning=NCIT.C25157)

    _defn = EnumDefinition(
        name="MeasurementTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Systolic Blood Pressure",
                PermissibleValue(text="Systolic Blood Pressure",
                                 description="The maximum pressure exerted into the systemic arterial circulation during the contraction of the left ventricle of the heart.",
                                 meaning=NCIT.C25298) )
        setattr(cls, "Diastolic Blood Pressure",
                PermissibleValue(text="Diastolic Blood Pressure",
                                 description="The minimum pressure exerted into the systemic arterial circulation during cardiac ventricular relaxation and filling.",
                                 meaning=NCIT.C25299) )
        setattr(cls, "Respiratory Rate",
                PermissibleValue(text="Respiratory Rate",
                                 description="The rate of breathing (inhalation and exhalation) measured within in a unit time, usually expressed as breaths per minute.",
                                 meaning=NCIT.C49678) )

class MeasurementUnitEnum(EnumDefinitionImpl):

    kg = PermissibleValue(text="kg",
                           description="A basic SI unit of mass. It is defined as the mass of an international prototype in the form of a platinum-iridium cylinder kept at Sevres in France. A kilogram is equal to 1,000 grams and 2.204 622 6 pounds.",
                           meaning=NCIT.C28252)
    cm = PermissibleValue(text="cm",
                           description="A basic unit of length in the former CGS version of metric system, equal to one hundredth of a meter or approximately 0.393 700 787 inch",
                           meaning=NCIT.C49668)
    m2 = PermissibleValue(text="m2",
                           description="A SI unit of area measurement equal to a square whose sides are one meter long. Square meter is equal to 10,000 square centimeters; 0.01 are; 1.196 square yards; 10.76 square feet; 1550 square inches.",
                           meaning=NCIT.C42569)
    mmHg = PermissibleValue(text="mmHg",
                               description="A non-SI unit of pressure equal to 133,332 Pa or 1.316E10-3 standard atmosphere. Use of this unit is generally deprecated by ISO and IUPAC.",
                               meaning=NCIT.C49670)
    C = PermissibleValue(text="C",
                         description="A unit of temperature of the temperature scale designed so that the freezing point of water is 0 degrees and the boiling point is 100 degrees at standard atmospheric pressure. The current official definition of the Celsius sets 0.01 C to be at the triple point of water and a degree to be 1/273.16 of the difference in temperature between the triple point of water and absolute zero. One degree Celsius represents the same temperature difference as one Kelvin.",
                         meaning=NCIT.C42559)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="MeasurementUnitEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "beat/min",
                PermissibleValue(text="beat/min",
                                 description="The number of heartbeats measured per minute time.",
                                 meaning=NCIT.C49673) )
        setattr(cls, "kg/m2",
                PermissibleValue(text="kg/m2",
                                 description="The SI derived unit of spread rate of a substance by mass, used also as a measure of area density and as a dose calculation unit.",
                                 meaning=NCIT.C49671) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class FunctionCategoryEnum(EnumDefinitionImpl):

    Echocardiogram = PermissibleValue(text="Echocardiogram",
                                                   description="The first diagnosis of the individual's condition.",
                                                   meaning=NCIT.C156813)
    EKG = PermissibleValue(text="EKG",
                             description="The return of a disease after a period of remission.",
                             meaning=NCIT.C38155)

    _defn = EnumDefinition(
        name="FunctionCategoryEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Pulmonary Function Test",
                PermissibleValue(text="Pulmonary Function Test",
                                 description="A broad range of tests that are performed to assess how well lungs inhale and exhale air and how efficiently they transfer oxygen into the blood.",
                                 meaning=NCIT.C38081) )

class FunctionTestEnum(EnumDefinitionImpl):

    Echocardiography = PermissibleValue(text="Echocardiography",
                                                       description="A test that uses high-frequency sound waves (ultrasound) to create an image of the heart.",
                                                       meaning=NCIT.C16525)
    QTc = PermissibleValue(text="QTc",
                             description="The time interval between the start of the Q wave and the end of the T wave in the cardiac cycle as corrected with a non-specified correction formula.",
                             meaning=NCIT.C100391)
    FVC = PermissibleValue(text="FVC",
                             description="The maximum volume of air that can be exhaled after forced maximum inhalation.",
                             meaning=NCIT.C111361)
    FEV1 = PermissibleValue(text="FEV1",
                               description="A test of lung function, the FEV1 is the volume exhaled during the first second of a forced expiratory maneuver started from the level of total lung capacity. It is the most frequently used index for assessing bronchoconstriction or bronchodilatation.",
                               meaning=NCIT.C38084)
    DLCO = PermissibleValue(text="DLCO",
                               description="A measurement of carbon monoxide (CO) transfer from inspired gas to pulmonary capillary blood. During the test, the subject inspires a gas containing CO and one or more tracer gases to allow determination of the gas exchanging capability of the lungs.",
                               meaning=NCIT.C38083)

    _defn = EnumDefinition(
        name="FunctionTestEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "MUGA Scan",
                PermissibleValue(text="MUGA Scan",
                                 description="A multi-gated acquisition (MUGA) scan and a form of radionuclide imaging that provides a comprehensive look at blood flow and the function of the lower chambers of the heart ventricles.",
                                 meaning=NCIT.C38073) )
        setattr(cls, "Ejection Fraction",
                PermissibleValue(text="Ejection Fraction",
                                 description="The fraction of the left ventricular end diastolic volume ejected with each beat. The left ventricular ejection fraction is equal to the left ventricular stroke volume divided by the left ventricular end diastolic volume.",
                                 meaning=NCIT.C99524) )
        setattr(cls, "Shortening Fraction",
                PermissibleValue(text="Shortening Fraction",
                                 description="The fraction of the left ventricle diastolic dimension that is lost during systole; the measurement is calculated using the following formula: (end-diastolic dimension - end-systolic dimension) / end-diastolic dimension; the quotient is then multiplied by one hundred to be expressed as a percent.",
                                 meaning=NCIT.C38020) )
        setattr(cls, "FEF at 25-75%",
                PermissibleValue(text="FEF at 25-75%",
                                 description="The mean forced expiratory flow rate at 25-75% of the forced vital capacity as a proportion of the predicted normal value.",
                                 meaning=NCIT.C119546) )
        setattr(cls, "Total lung capacity",
                PermissibleValue(text="Total lung capacity",
                                 description="The total volume of air in the lungs after maximum inhalation.",
                                 meaning=NCIT.C111325) )

class FunctionResultUnitEnum(EnumDefinitionImpl):

    mL = PermissibleValue(text="mL",
                           description="A unit of volume equal to one millionth (10E-6) of a cubic meter, one thousandth of a liter, one cubic centimeter, or 0.061023 7 cubic inch. A cubic centimeter is the CGS unit of volume.",
                           meaning=NCIT.C28254)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="FunctionResultUnitEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "%",
                PermissibleValue(text="%",
                                 description="A unit for expressing a number as a fraction of hundred (on the basis of a rate or proportion per hundred).",
                                 meaning=NCIT.C48570) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class LabCategoryEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="LabCategoryEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Peripheral Blood Analysis",
                PermissibleValue(text="Peripheral Blood Analysis",
                                 description="A laboratory analysis of a sample of peripheral blood.",
                                 meaning=NCIT.C173271) )
        setattr(cls, "Cerebrospinal Fluid Analysis",
                PermissibleValue(text="Cerebrospinal Fluid Analysis",
                                 description="A laboratory analysis of a sample of cerebrospinal fluid.",
                                 meaning=NCIT.C173272) )
        setattr(cls, "Bone Marrow Analysis",
                PermissibleValue(text="Bone Marrow Analysis",
                                 description="A laboratory analysis of a sample of bone marrow.",
                                 meaning=NCIT.C173273) )
        setattr(cls, "MicroRNA Sequencing",
                PermissibleValue(text="MicroRNA Sequencing",
                                 description="A next-generation or massively parallel high-throughput DNA sequencing-based procedure that can identify and quantify the microRNA sequences present in a biological sample.",
                                 meaning=NCIT.C156057) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class LabTestEnum(EnumDefinitionImpl):

    Platelets = PermissibleValue(text="Platelets",
                                         description="The determination of the number of platelets in a biospecimen.",
                                         meaning=NCIT.C51951)
    RBC = PermissibleValue(text="RBC",
                             description="The determination of the number of erythrocytes in a biospecimen.",
                             meaning=NCIT.C51946)
    WBC = PermissibleValue(text="WBC",
                             description="A test to determine the number of leukocytes in a biospecimen.",
                             meaning=NCIT.C51948)
    Blasts = PermissibleValue(text="Blasts",
                                   description="The determination of the number of blast cells present in a blood sample.",
                                   meaning=NCIT.C74605)
    Neutrophils = PermissibleValue(text="Neutrophils",
                                             description="A test to determine the number of neutrophils in a sample of blood.",
                                             meaning=NCIT.C51950)
    Lymphocytes = PermissibleValue(text="Lymphocytes",
                                             description="The determination of the number of lymphocytes in a blood sample.",
                                             meaning=NCIT.C12535)
    Monocytes = PermissibleValue(text="Monocytes",
                                         description="The determination of the number of monocytes in a blood sample.",
                                         meaning=NCIT.C64823)
    Eosophinils = PermissibleValue(text="Eosophinils",
                                             description="The determination of the number of eosinophils in a blood sample.",
                                             meaning=NCIT.C64550)
    ANC = PermissibleValue(text="ANC",
                             description="The real number of white blood cells (WBC) that are neutrophils. It is derived by multiplying the WBC count by the percent of neutrophils in the differential WBC count. The normal range for ANC is 1.5 to 8.0 (1,500 to 8,000/mm3).",
                             meaning=NCIT.C63321)
    Hemoglobin = PermissibleValue(text="Hemoglobin",
                                           description="A quantitative measurement of the amount of hemoglobin present in a biospecimen.",
                                           meaning=NCIT.C64848)
    Albumin = PermissibleValue(text="Albumin",
                                     description="A quantitative measurement of albumin present in a sample.",
                                     meaning=NCIT.C64431)
    Leukocytes = PermissibleValue(text="Leukocytes",
                                           description="A test to determine the number of leukocytes in a biospecimen.",
                                           meaning=NCIT.C51948)
    Calcium = PermissibleValue(text="Calcium",
                                     description="A quantitative measurement of the amount of calcium present in a sample.",
                                     meaning=NCIT.C64488)
    Potassium = PermissibleValue(text="Potassium",
                                         description="A quantitative measurement of the amount of potassium present in a sample.",
                                         meaning=NCIT.C64853)
    Sodium = PermissibleValue(text="Sodium",
                                   description="A quantitative measurement of the amount of sodium present in a sample.",
                                   meaning=NCIT.C64809)
    Chloride = PermissibleValue(text="Chloride",
                                       description="A quantitative measurement of the amount of chloride present in a sample.",
                                       meaning=NCIT.C64495)
    Protein = PermissibleValue(text="Protein",
                                     description="A group of complex organic macromolecules composed of one or more chains (linear polymers) of alpha-L-amino acids linked by peptide bonds and ranging in size from a few thousand to over 1 million Daltons. Proteins are fundamental genetically encoded components of living cells with specific structures and functions dictated by amino acid sequence.",
                                     meaning=NCIT.C17021)
    Glucose = PermissibleValue(text="Glucose",
                                     description="The determination of the amount of glucose present in a sample.",
                                     meaning=NCIT.C105585)
    Lipase = PermissibleValue(text="Lipase",
                                   description="The determination of the amount of lipase present in a sample.",
                                   meaning=NCIT.C117748)
    ALP = PermissibleValue(text="ALP",
                             description="A quantitative measurement of alkaline phosphatase present in a sample.",
                             meaning=NCIT.C64432)
    AST = PermissibleValue(text="AST",
                             description="A quantitative measurement of aspartate aminotransferase present in a sample.",
                             meaning=NCIT.C64467)
    ALT = PermissibleValue(text="ALT",
                             description="A quantitative measurement of alanine aminotransferase present in a sample.",
                             meaning=NCIT.C64433)
    GGT = PermissibleValue(text="GGT",
                             description="A quantitative measurement of the amount of gamma glutamyl transpeptidase present in a sample.",
                             meaning=NCIT.C64847)
    TSH = PermissibleValue(text="TSH",
                             description="A quantitative measurement of the amount of thyrotropin present in a sample.",
                             meaning=NCIT.C64813)
    Ferritin = PermissibleValue(text="Ferritin",
                                       description="The determination of the amount of ferritin present in a sample.",
                                       meaning=NCIT.C74737)
    LDH = PermissibleValue(text="LDH",
                             description="A quantitative measurement of the amount of lactate dehydrogenase present in a sample.",
                             meaning=NCIT.C64855)
    ESR = PermissibleValue(text="ESR",
                             description="A quantitative measurement of the distance that red blood cells travel in one hour in a sample of unclotted blood.",
                             meaning=NCIT.C74611)
    AFP = PermissibleValue(text="AFP",
                             description="This gene plays a role in fetal progression.",
                             meaning=NCIT.C21577)
    CRP = PermissibleValue(text="CRP",
                             description="A quantitative measurement of the amount of C-reactive protein present in a sample.",
                             meaning=NCIT.C64548)
    CD34 = PermissibleValue(text="CD34",
                               description="The determination of the amount of CD34 expressing cells present in a sample.",
                               meaning=NCIT.C102260)
    HGB = PermissibleValue(text="HGB",
                             description="A quantitative measurement of the amount of hemoglobin present in a biospecimen.",
                             meaning=NCIT.C64848)
    HCT = PermissibleValue(text="HCT",
                             description="A measure of the volume of red blood cells expressed as a percentage of the total blood volume. Normal in males is 43-49%, in females 37-43%.",
                             meaning=NCIT.C64796)
    PT = PermissibleValue(text="PT",
                           description="A measurement of the clotting time of plasma recalcified in the presence of excess tissue thromboplastin; it is a measure of the extrinsic pathway of coagulation. It is used to determine the clotting tendency of blood, in the measure of warfarin dosage, liver damage and vitamin K status. Factors measured are fibrinogen, prothrombin, and factors V, VII, and X.",
                           meaning=NCIT.C62656)
    PTT = PermissibleValue(text="PTT",
                             description="A measurement of the length of time that it takes for clotting to occur when no activating reagents are added to a biological specimen. The test is partial due to the absence of tissue factor (Factor III) from the reaction mixture.",
                             meaning=NCIT.C178140)
    INR = PermissibleValue(text="INR",
                             description="A measure of the extrinsic pathway of coagulation. The International Normalized Ratio of Prothrombin Time (INR) is the ratio of a patient prothrombin time to a normal (control) sample raised to the power of the International Sensitivity Index (ISI) with a range of 0.8 to 1.2 seconds.",
                             meaning=NCIT.C64805)
    Creatinine = PermissibleValue(text="Creatinine",
                                           description="A quantitative measurement of the amount of creatinine present in a sample.",
                                           meaning=NCIT.C64547)
    cfDNA = PermissibleValue(text="cfDNA",
                                 description="DNA that is found in blood plasma and is not associated with cells in the circulation.",
                                 meaning=NCIT.C128274)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="LabTestEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Absolute Neutrophil Count",
                PermissibleValue(text="Absolute Neutrophil Count",
                                 description="The real number of white blood cells (WBC) that are neutrophils. It is derived by multiplying the WBC count by the percent of neutrophils in the differential WBC count. The normal range for ANC is 1.5 to 8.0 (1,500 to 8,000/mm3).",
                                 meaning=NCIT.C63321) )
        setattr(cls, "Auer Rods",
                PermissibleValue(text="Auer Rods",
                                 description="The determination of the number of Auer rods present in a biospecimen.",
                                 meaning=NCIT.C74657) )
        setattr(cls, "Uric Acid",
                PermissibleValue(text="Uric Acid",
                                 description="A white tasteless odorless crystalline product of protein metabolism, found in the blood and urine, as well as trace amounts found in the various organs of the body. It can build up and form stones or crystals in various disease states.",
                                 meaning=NCIT.C62652) )
        setattr(cls, "5 Prime Nucleotidase",
                PermissibleValue(text="5 Prime Nucleotidase",
                                 description="The determination of the amount of 5 prime nucleotidase present in a sample.",
                                 meaning=NCIT.C79437) )
        setattr(cls, "Total Bilirubin",
                PermissibleValue(text="Total Bilirubin",
                                 description="The measurement of the total amount of bilirubin present in a particular substrate. The substrate most often tested is blood, but other fluids extracted from the body may be used periodically depending on the purpose of the test.",
                                 meaning=NCIT.C38037) )
        setattr(cls, "Direct Bilirubin",
                PermissibleValue(text="Direct Bilirubin",
                                 description="The bilirubin is bound to glucuronide to form conjugated bilirubin (direct bilirubin). Direct Bilirubin measurement is accomplished by a colorimetric method. Direct Bilirubin in biological fluids reacts with sulfanilic acid at acidic pH to produce a red colored complex. The optical density of produced color has a direct relationship with Direct Bilirubin concentration in the solution.",
                                 meaning=NCIT.C64481) )
        setattr(cls, "Free T3",
                PermissibleValue(text="Free T3",
                                 description="The determination of the amount of free triiodothyronine present in a sample.",
                                 meaning=NCIT.C74787) )
        setattr(cls, "Alkaline Phophatase",
                PermissibleValue(text="Alkaline Phophatase",
                                 description="A quantitative measurement of alkaline phosphatase present in a sample.",
                                 meaning=NCIT.C64432) )
        setattr(cls, "Creatinine Clearance",
                PermissibleValue(text="Creatinine Clearance",
                                 description="The determination of the clearance of endogenous creatinine, used for evaluating the glomerular filtration rate.",
                                 meaning=NCIT.C25747) )
        setattr(cls, "Free T4",
                PermissibleValue(text="Free T4",
                                 description="The determination of the amount of free thyroxine present in a sample.",
                                 meaning=NCIT.C74786) )
        setattr(cls, "EBV IgG",
                PermissibleValue(text="EBV IgG",
                                 description="The determination of the amount of Epstein-Barr virus in a biological sample.",
                                 meaning=NCIT.C184675) )
        setattr(cls, "EBV DNA",
                PermissibleValue(text="EBV DNA",
                                 description="The determination of the amount of Epstein-Barr virus DNA present in a sample.",
                                 meaning=NCIT.C166035) )
        setattr(cls, "β-hCG",
                PermissibleValue(text="β-hCG",
                                 description="A determination of the presence of Choriogonadotropin Beta protein.",
                                 meaning=NCIT.C64851) )
        setattr(cls, "miR-371a-3p",
                PermissibleValue(text="miR-371a-3p",
                                 description="The human MIR371A wild-type allele is located in the vicinity of 19q13.42 and is approximately 67 bases in length. This allele, which encodes MIR371A pre-miRNA, may be involved in the regulation of target gene expression. Alteration in the expression of this gene is associated with malignant germ cell tumors.",
                                 meaning=NCIT.C158711) )
        setattr(cls, "miR-372-3p",
                PermissibleValue(text="miR-372-3p",
                                 description="The human MIR372 wild-type allele is located in the vicinity of 19q13.41 and is approximately 66 bases in length. This allele, which encodes MIR372 pre-miRNA, plays a role in the regulation of gene expression. Alteration in the expression of this gene is associated with development of testicular germ cell tumor and non-small cell lung cancer.",
                                 meaning=NCIT.C82190) )
        setattr(cls, "miR-373-3p",
                PermissibleValue(text="miR-373-3p",
                                 description="The human MIR373 wild-type allele is located in the vicinity of 19q13.41 and is approximately 68 bases in length. This allele, which encodes MIR373 pre-miRNA, plays a role in the regulation of gene expression. Alteration in the expression of this gene is associated with development of testicular germ cell tumor and breast cancer.",
                                 meaning=NCIT.C82191) )
        setattr(cls, "miR-367-3p",
                PermissibleValue(text="miR-367-3p",
                                 description="The determination of the amount of human microRNA 367-3p present in a sample.",
                                 meaning=NCIT.C177302) )
        setattr(cls, "miR-375-3p",
                PermissibleValue(text="miR-375-3p",
                                 description="Human MIR375 wild-type allele is located in the vicinity of 2q35 and is approximately 70 bases in length. This allele, which encodes MIR375 pre-miRNA, is involved in the modulation of gene expression.",
                                 meaning=NCIT.C101665) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class SpecimenEnum(EnumDefinitionImpl):

    Blood = PermissibleValue(text="Blood",
                                 description="A small volume of blood removed for testing or storage.",
                                 meaning=NCIT.C17610)
    Serum = PermissibleValue(text="Serum",
                                 description="A sample of serum collected for analysis.",
                                 meaning=NCIT.C178987)
    Plasma = PermissibleValue(text="Plasma",
                                   description="A specimen of plasma.",
                                   meaning=NCIT.C185204)
    Urine = PermissibleValue(text="Urine",
                                 description="The fluid that is excreted by the kidneys. It is stored in the bladder and discharged through the urethra.",
                                 meaning=NCIT.C13283)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="SpecimenEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Cerebrospinal Fluid",
                PermissibleValue(text="Cerebrospinal Fluid",
                                 description="A specimen of cerebrospinal fluid.",
                                 meaning=NCIT.C185194) )
        setattr(cls, "Peritoneal Fluid",
                PermissibleValue(text="Peritoneal Fluid",
                                 description="A specimen of fluid from the peritoneum.",
                                 meaning=NCIT.C185197) )
        setattr(cls, "Bone Marrow",
                PermissibleValue(text="Bone Marrow",
                                 description="A biological sample containing components collected from bone marrow of an experimental subject.",
                                 meaning=NCIT.C164009) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class LabResultCategoricalEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="LabResultCategoricalEnum",
    )

class LabResultUnitEnum(EnumDefinitionImpl):

    seconds = PermissibleValue(text="seconds",
                                     description="A unit of time, one of the seven base units of the International System of Units (Systeme International d'Unites, SI). The second is the duration of 919 263 177 0 periods of the specified light radiation corresponding to the transition between the two hyperfine levels of the caesium 133 atom in its ground state at 0 K. According to the convention, 60 seconds constitute one minute; 3,600 seconds constitute one hour.",
                                     meaning=NCIT.C42535)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="LabResultUnitEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "%",
                PermissibleValue(text="%",
                                 description="A unit for expressing a number as a fraction of hundred (on the basis of a rate or proportion per hundred).",
                                 meaning=NCIT.C48570) )
        setattr(cls, "count/mm3",
                PermissibleValue(text="count/mm3",
                                 description="A count of items per cubic millimeter of sample.",
                                 meaning=NCIT.C173275) )
        setattr(cls, "g/dL",
                PermissibleValue(text="g/dL",
                                 description="A unit of mass concentration defined as the concentration of one gram of a substance per unit volume of the mixture equal to one deciliter (100 milliliters). The concept also refers to the metric unit of mass density (volumic mass) defined as the density of substance which mass equal to one gram occupies the volume one deciliter.",
                                 meaning=NCIT.C64783) )
        setattr(cls, "U/L",
                PermissibleValue(text="U/L",
                                 description="An arbitrary unit of substance concentration equal to the concentration at which one liter of mixture contains one unit of a substance.",
                                 meaning=NCIT.C67456) )
        setattr(cls, "ng/mL",
                PermissibleValue(text="ng/mL",
                                 description="A unit of mass concentration defined as the concentration of one microgram of a substance per unit volume of the mixture equal to one liter. The concept also refers to the unit of mass density (volumetric mass) defined as the density of a substance which mass equal to one microgram occupies the volume of one liter.",
                                 meaning=NCIT.C67306) )
        setattr(cls, "UI/L",
                PermissibleValue(text="UI/L",
                                 description="Unit of arbitrary substance concentration (biologic activity concentration) defined as the concentration of one international unit per one liter of the system volume.",
                                 meaning=NCIT.C67376) )
        setattr(cls, "IU/L",
                PermissibleValue(text="IU/L",
                                 description="Unit of arbitrary substance concentration (biologic activity concentration) defined as the concentration of one international unit per one liter of the system volume.",
                                 meaning=NCIT.C67376) )
        setattr(cls, "mm/h",
                PermissibleValue(text="mm/h",
                                 description="A unit of both speed (scalar) and velocity (vector), defined as the distance of one millimeter travelled per unit time equal to one hour.",
                                 meaning=NCIT.C67419) )
        setattr(cls, "mg/L",
                PermissibleValue(text="mg/L",
                                 description="A metric unit of mass concentration defined as the concentration of one gram of a substance per unit volume of the mixture equal to one cubic meter. The concept also refers to the metric unit of mass density (volumic mass) defined as the density of a substance which mass equal to one gram occupies the volume of one cubic meter.",
                                 meaning=NCIT.C64572) )
        setattr(cls, "uIU/mL",
                PermissibleValue(text="uIU/mL",
                                 description="Unit of arbitrary substance concentration (biologic activity concentration) defined as the concentration of one millionth of international unit per one milliliter of system volume.",
                                 meaning=NCIT.C674505) )
        setattr(cls, "g/L",
                PermissibleValue(text="g/L",
                                 description="A SI derived unit of mass concentration defined as the concentration of one kilogram of a substance per unit volume of the mixture equal to one cubic meter, or the concentration of one milligram of a substance per unit volume of the mixture equal to one milliliter, or one gram of a substance per one liter of the mixture. It is also a unit of mass density (volumic mass) defined as the density of substance which mass equal to one milligram occupies the volume one milliliter.",
                                 meaning=NCIT.C42576) )
        setattr(cls, "umol/L",
                PermissibleValue(text="umol/L",
                                 description="A unit of concentration (molarity unit) equal to one one-millionth of a mole (10E-6 mole) of solute per one liter of solution.",
                                 meaning=NCIT.C48508) )
        setattr(cls, "mUI/L",
                PermissibleValue(text="mUI/L",
                                 description="Unit of arbitrary substance concentration (biologic activity concentration) defined as the concentration of one millionth of international unit per one milliliter of system volume.",
                                 meaning=NCIT.C67405) )
        setattr(cls, "mL/min",
                PermissibleValue(text="mL/min",
                                 description="A metric unit of volumetric flow rate defined as the rate at which one milliliter of matter crosses a given surface during the period of time equal to one minute.",
                                 meaning=NCIT.C64777) )
        setattr(cls, "mcg/mL",
                PermissibleValue(text="mcg/mL",
                                 description="A metric unit of mass concentration defined as the concentration of one gram of a substance per unit volume of the mixture equal to one cubic meter. The concept also refers to the metric unit of mass density (volumic mass) defined as the density of a substance which mass equal to one gram occupies the volume of one cubic meter.",
                                 meaning=NCIT.C64572) )
        setattr(cls, "mmol/L",
                PermissibleValue(text="mmol/L",
                                 description="A unit of concentration (molarity unit) equal to one thousandth of a mole (10E-3 mole) of solute per one liter of solution.",
                                 meaning=NCIT.C64387) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class LabMethodEnum(EnumDefinitionImpl):

    Morphology = PermissibleValue(text="Morphology",
                                           description="The science of the form and structure of organisms (plants, animals, and other forms of life), or of their parts, and the study or science of the same. In pathology, the specific appearance of cells and tissues (normal and abnormal) under the light or electron microscope.",
                                           meaning=NCIT.C17943)
    PCR = PermissibleValue(text="PCR",
                             description="A method for amplifying a DNA base sequence using multiple rounds of heat denaturation of the DNA and annealing of oligonucleotide primers complementary to flanking regions in the presence of a heat-stable polymerase. This results in duplication of the targeted DNA region. Newly synthesized DNA strands can subsequently serve as additional templates for the same primer sequences, so that successive rounds of primer annealing, strand elongation, and dissociation produce rapid and highly specific amplification of the desired sequence. PCR also can be used to detect the existence of the defined sequence in a DNA sample.",
                             meaning=NCIT.C17003)
    qPCR = PermissibleValue(text="qPCR",
                               description="An application of PCR that measures the products generated during each cycle of the polymerase chain reaction process in order to determine the starting amount of template in the reaction.",
                               meaning=NCIT.C51962)
    ddPCR = PermissibleValue(text="ddPCR",
                                 description="A type of digital polymerase chain reaction technique in which the sample is fractionated into thousands of tiny droplets using a water-oil emulsion droplet technology, within which individual PCR reactions occur in each droplet",
                                 meaning=NCIT.C166064)
    Cytology = PermissibleValue(text="Cytology",
                                       description="The light microscopic study of normal and abnormal cells in fine needle aspirates (FNAs), body cavity fluids, and smears.",
                                       meaning=NCIT.C16491)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="LabMethodEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Flow cytometry",
                PermissibleValue(text="Flow cytometry",
                                 description="A technique for counting, examining and sorting microscopic particles suspended in a stream of fluid.",
                                 meaning=NCIT.C16585) )
        setattr(cls, "MicroRNA Sequencing",
                PermissibleValue(text="MicroRNA Sequencing",
                                 description="A next-generation or massively parallel high-throughput DNA sequencing-based procedure that can identify and quantify the microRNA sequences present in a biological sample.",
                                 meaning=NCIT.C156057) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class LabSeqMethodEnum(EnumDefinitionImpl):

    Relative = PermissibleValue(text="Relative",
                                       description="Considered in comparison with something else; dependent on or interconnected with something else; not absolute.",
                                       meaning=NCIT.C45830)
    Absolute = PermissibleValue(text="Absolute",
                                       description="Complete and without restriction or qualification; something that does not depend on anything else; not relative.",
                                       meaning=NCIT.C45829)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="LabSeqMethodEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class BmMorphologyEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="BmMorphologyEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "M1 (less than 5 % blasts)",
                PermissibleValue(text="M1 (less than 5 % blasts)",
                                 description="A semi-quantitative microscopic finding indicating that 5 percent or less of the nucleated cells in a bone marrow sample are immature mononuclear cells.",
                                 meaning=NCIT.C137698) )
        setattr(cls, "M2 (5-25 % blasts)",
                PermissibleValue(text="M2 (5-25 % blasts)",
                                 description="A semi-quantitative microscopic finding indicating that between 5 and 25 percent of the nucleated cells in a bone marrow sample are immature mononuclear cells.",
                                 meaning=NCIT.C146709) )
        setattr(cls, "M3 (greater than 25 % blasts)",
                PermissibleValue(text="M3 (greater than 25 % blasts)",
                                 description="A semi-quantitative microscopic finding indicating that 25 percent or more of the nucleated cells in a bone marrow sample are immature mononuclear cells.",
                                 meaning=NCIT.C140330) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class ImagingMethodEnum(EnumDefinitionImpl):

    PET = PermissibleValue(text="PET",
                             description="A technique for measuring the gamma radiation produced by collisions of electrons and positrons (anti-electrons) within living tissue. In positron emission tomography (PET), a subject is given a dose of a positron-emitting radionuclide attached to a metabolically active substance (for example, 2-fluoro-2-deoxy-D-glucose (FDG), which is similar to a naturally occurring sugar, glucose, with the addition of a radioactive fluorine atom). When living tissue containing the positron emitter is bombarded by electrons, gamma radiation produced by collisions of electrons and positrons is detected by a scanner, revealing in fine detail the tissue location of the metabolically-active substance administered.",
                             meaning=NCIT.C17007)
    Gallium = PermissibleValue(text="Gallium",
                                     description="An element with atomic symbol Ga, atomic number 31, and atomic weight 69.7. A rare silvery (usually trivalent) metallic element; brittle at low temperatures but liquid above room temperature; occurs in trace amounts in bauxite and zinc ores.",
                                     meaning=NCIT.C66798)
    CT = PermissibleValue(text="CT",
                           description="A method of examining structures within the body by scanning them with X rays and using a computer to construct a series of cross-sectional scans along a single axis.",
                           meaning=NCIT.C17204)
    MRI = PermissibleValue(text="MRI",
                             description="Imaging that uses radiofrequency waves and a strong magnetic field rather than x-rays to provide detailed pictures of internal organs and tissues. The technique is valuable for the diagnosis of many pathologic conditions, including cancer, heart and vascular disease, stroke, and joint and musculoskeletal disorders.",
                             meaning=NCIT.C16809)
    Ultrasound = PermissibleValue(text="Ultrasound",
                                           description="High frequency sound, generally with a frequency greater than 20,000 Hz.",
                                           meaning=NCIT.C64384)

    _defn = EnumDefinition(
        name="ImagingMethodEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "PET-CT",
                PermissibleValue(text="PET-CT",
                                 description="An imaging technique that utilizes positron emission tomography and computed tomography in a single machine.",
                                 meaning=NCIT.C103512) )
        setattr(cls, "PET-MRI",
                PermissibleValue(text="PET-MRI",
                                 description="An imaging technique that utilizes positron emission tomography and magnetic resonance imaging in a single machine.",
                                 meaning=NCIT.C103514) )
        setattr(cls, "X-ray",
                PermissibleValue(text="X-ray",
                                 description="A radiographic procedure using the emission of x-rays to form an image of the structure penetrated by the radiation.",
                                 meaning=NCIT.C38101) )
        setattr(cls, "Bone scan",
                PermissibleValue(text="Bone scan",
                                 description="A nuclear imaging method used to evaluate pathological bone metabolism.",
                                 meaning=NCIT.C17646) )

class ImagingResultEnum(EnumDefinitionImpl):

    Positive = PermissibleValue(text="Positive",
                                       description="A finding of abnormality following an examination or observation confirming something, such as the presence of a disease, condition, or microorganism.",
                                       meaning=NCIT.C38758)
    Negative = PermissibleValue(text="Negative",
                                       description="A finding of normality following an examination or investigation looking for the presence of a microorganism, disease, or condition.",
                                       meaning=NCIT.C38757)
    Equivocal = PermissibleValue(text="Equivocal",
                                         description="A laboratory test result that indicates that a specific disease, condition, or attribute being assessed is not clearly present or absent.",
                                         meaning=NCIT.C178921)

    _defn = EnumDefinition(
        name="ImagingResultEnum",
    )

class DeauvilleScoreEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="DeauvilleScoreEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Score 1",
                PermissibleValue(text="Score 1",
                                 description="The results of the positron emission tomography are negative; there is no detectable abnormal tracer uptake.",
                                 meaning=NCIT.C99728) )
        setattr(cls, "Score 2",
                PermissibleValue(text="Score 2",
                                 description="The results of the positron emission tomography are negative; the tracer uptake is less than or equal to the mediastinum.",
                                 meaning=NCIT.C99747) )
        setattr(cls, "Score 3",
                PermissibleValue(text="Score 3",
                                 description="The results of the positron emission tomography are negative; the tracer uptake is greater than the mediastinum but less than or equal to the liver.",
                                 meaning=NCIT.C99748) )
        setattr(cls, "Score 4",
                PermissibleValue(text="Score 4",
                                 description="The results of the positron emission tomography are positive; the tracer uptake is moderately more than the liver uptake, at any disease site.",
                                 meaning=NCIT.C99749) )
        setattr(cls, "Score 5",
                PermissibleValue(text="Score 5",
                                 description="The results of the positron emission tomography are positive; the tracer uptake is markedly increased at any disease site.",
                                 meaning=NCIT.C99750) )

class CytologySpecTypeEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="CytologySpecTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Cerebrospinal Fluid",
                PermissibleValue(text="Cerebrospinal Fluid",
                                 description="The fluid that is contained within the brain ventricles, the subarachnoid space and the central canal of the spinal cord.",
                                 meaning=NCIT.C12692) )
        setattr(cls, "Peritoneal Fluid",
                PermissibleValue(text="Peritoneal Fluid",
                                 description="The small amount of fluid that is generated in the abdominal cavity to lubricate the peritoneum.",
                                 meaning=NCIT.C77612) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class IhcTestEnum(EnumDefinitionImpl):

    CD30 = PermissibleValue(text="CD30",
                               description="Tumor necrosis factor receptor superfamily member 8 (595 aa, ~ 64 kDa) is encoded by the human TNFRSF8 gene. This protein is involved in ligand-mediated signal transduction, the positive regulation of apoptosis and the inhibition of cell proliferation.",
                               meaning=NCIT.C38906)
    GPC3 = PermissibleValue(text="GPC3",
                               description="Glypican-3 (580 aa, ~66 kDa) is encoded by the human GPC3 gene. This protein is involved in the mediation of proteoglycan binding to the cell surface.",
                               meaning=NCIT.C88175)
    CD20 = PermissibleValue(text="CD20",
                               description="B-lymphocyte antigen CD20 (297 aa, ~33 kDa) is encoded by the human MS4A1 gene. This protein plays a role in both the activation and proliferation of B-cells.",
                               meaning=NCIT.C38896)
    LMP1 = PermissibleValue(text="LMP1",
                               description="Latent membrane protein 1 (386 aa, ~42 kDa) is encoded by the Epstein-Barr virus LMP1 gene. This protein is involved in both the activation of nuclear factor-kappa-B family signaling pathways and the inhibition of apoptosis of infected B-lymphocytes.",
                               meaning=NCIT.C18863)
    EBER = PermissibleValue(text="EBER",
                               description="Small non-coding RNA that is encoded by Epstein-Barr virus DNA and transcribed by virally-infected cells throughout the latent cycle. Expression of these oligonucleotides may be associated with the regulation of host ribosome function.",
                               meaning=NCIT.C111618)
    PAS = PermissibleValue(text="PAS",
                             description="This is an all-round useful stain for many things, including glycogen, mucin, mucoprotein, glycoprotein, as well as fungi. The reaction is based on the oxidation of glycol group to aldehydes by periodate. The schiff's reagent selectively stains the aldehydes to a rose pink color. PAS is useful for outlining tissue structures--basement membranes, capsules, blood vessels, etc.",
                             meaning=NCIT.C23019)
    S100 = PermissibleValue(text="S100",
                               description="A family of low molecular weight proteins that are characterized by the presence of two EF-hand calcium binding domains. These proteins form homodimers that localize either in the cytoplasm or nucleus of neural crest-derived cells and are involved in the regulation of many cellular processes such as cell cycle progression and differentiation.",
                               meaning=NCIT.C29924)
    NSE = PermissibleValue(text="NSE",
                             description="Gamma-enolase (434 aa, ~47 kDa) is encoded by the human ENO2 gene. This protein is involved in glycolysis, neurotrophy and neuroprotection.",
                             meaning=NCIT.C62216)
    Vimentin = PermissibleValue(text="Vimentin",
                                       description="Vimentin (466 aa, ~54 kDa) is encoded by the human VIM gene. This protein plays a role in the localization of organelles and other cellular components.",
                                       meaning=NCIT.C48797)
    Desmin = PermissibleValue(text="Desmin",
                                   description="Desmin (470 aa, ~54 kDa) is encoded by the human DES gene. This protein is involved in the regulation of cytoskeletal dynamics in muscle cells.",
                                   meaning=NCIT.C96450)
    CD99 = PermissibleValue(text="CD99",
                               description="CD99 antigen (185 aa, ~19 kDa) is encoded by the human CD99 gene. This protein plays a role in cell adhesion.",
                               meaning=NCIT.C102941)
    CD45 = PermissibleValue(text="CD45",
                               description="Receptor-type tyrosine-protein phosphatase C (1304 aa, ~147 kDa) is encoded by the human PTPRC gene. This protein plays a role in protein dephosphorylation.",
                               meaning=NCIT.C17282)

    _defn = EnumDefinition(
        name="IhcTestEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "beta-catenin",
                PermissibleValue(text="beta-catenin",
                                 description="Catenin beta-1 (781 aa, ~85 kDa) is encoded by the human CTNNB1 gene. This protein is involved in Wnt signaling, adherens junction structure, and the regulation of cell growth.",
                                 meaning=NCIT.C17478) )
        setattr(cls, "FLI-1",
                PermissibleValue(text="FLI-1",
                                 description="Friend leukemia integration 1 transcription factor (452 aa, ~51 kDa) is encoded by the human FLI1 gene. This protein plays a role in the modulation of transcription.",
                                 meaning=NCIT.C18566) )

class IhcSpecTypeEnum(EnumDefinitionImpl):

    Tissue = PermissibleValue(text="Tissue",
                                   description="An anatomical structure consisting of similarly specialized cells and intercellular matrix, aggregated according to genetically determined spatial relationships, performing a specific function.",
                                   meaning=NCIT.C12801)

    _defn = EnumDefinition(
        name="IhcSpecTypeEnum",
    )

class IhcResultUnitEnum(EnumDefinitionImpl):

    Intensity = PermissibleValue(text="Intensity",
                                         description="The degree or magnitude of strength, energy, or feeling.",
                                         meaning=NCIT.C25539)

    _defn = EnumDefinition(
        name="IhcResultUnitEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Number of events",
                PermissibleValue(text="Number of events",
                                 description="A measurement of the total number of events that have occurred.",
                                 meaning=NCIT.C130057) )

class LesionClassificationEnum(EnumDefinitionImpl):

    Primary = PermissibleValue(text="Primary",
                                     description="A tumor at the original site of origin.",
                                     meaning=NCIT.C8509)
    Metastatic = PermissibleValue(text="Metastatic",
                                           description="A term referring to the clinical or pathologic observation of a tumor extension from its original site of growth to another anatomic site.",
                                           meaning=NCIT.C14174)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="LesionClassificationEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class MethodEnum(EnumDefinitionImpl):

    Karyotyping = PermissibleValue(text="Karyotyping",
                                             description="The assessment of the chromosomal morphology and number in somatic cells of an individual.",
                                             meaning=NCIT.C25215)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="MethodEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Fluorescence In Situ Hybridization",
                PermissibleValue(text="Fluorescence In Situ Hybridization",
                                 description="A physical mapping approach that uses fluorescent tags to detect hybridization of probes within metaphase chromosomes or less condensed somatic interphase chromatin. This technique can be used for identification of chromosomal abnormalities and for gene mapping.",
                                 meaning=NCIT.C17563) )
        setattr(cls, "RT-PCR",
                PermissibleValue(text="RT-PCR",
                                 description="A laboratory procedure in which an RNA strand is first transcribed into a DNA complement and then subjected to PCR amplification. Transcribing an RNA strand into a DNA complement is termed reverse transcription and is done by the enzyme reverse transcriptase.",
                                 meaning=NCIT.C18136) )
        setattr(cls, "Sequencing, NOS",
                PermissibleValue(text="Sequencing, NOS",
                                 description="Next Generation Sequencing, should be used as a default value if no other details about the NGS analysis is known.",
                                 meaning=NCIT.C101293) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class GenomicSourceClassEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="GenomicSourceClassEnum",
    )

class CommonNameEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="CommonNameEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class StatusEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="StatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Done",
                PermissibleValue(text="Not Done",
                                 description="Indicates a task, process or examination that has either not been initiated or not been completed.",
                                 meaning=NCIT.C49484) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class MutationTypeEnum(EnumDefinitionImpl):

    Indel = PermissibleValue(text="Indel",
                                 description="A sequence alteration which included an insertion and a deletion, affecting 2 or more bases. (Source: The Sequence Ontology) ",
                                 meaning=SO["1000032"])
    Substitution = PermissibleValue(text="Substitution",
                                               description="A sequence alteration where the length of the change in the variant is the same as that of the reference. (Source: The Sequence Ontology) ",
                                               meaning=SO["1000002"])
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned. ",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor. ",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="MutationTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Deletion, chromosomal",
                PermissibleValue(text="Deletion, chromosomal",
                                 description="An incomplete chromosome. (Source: The Sequence Ontology) ",
                                 meaning=SO["1000029"]) )
        setattr(cls, "Deletion, NOS",
                PermissibleValue(text="Deletion, NOS",
                                 description="The point at which one or more contiguous nucleotides were excised. (Source: The Sequence Ontology) Should be used when the type of deletion is not specified. ",
                                 meaning=SO["0000159"]) )
        setattr(cls, "Duplication, internal tandem",
                PermissibleValue(text="Duplication, internal tandem",
                                 description="A duplication consisting of 2 identical adjacent regions. (Source: The Sequence Ontology) ",
                                 meaning=SO["1000173"]) )
        setattr(cls, "Duplication, chromosomal",
                PermissibleValue(text="Duplication, chromosomal",
                                 description="An extra chromosome. (Source: The Sequence Ontology) ",
                                 meaning=SO["1000037"]) )
        setattr(cls, "Duplication, NOS",
                PermissibleValue(text="Duplication, NOS",
                                 description="An insertion which derives from, or is identical in sequence to, nucleotides present at a known location in the genome. (Source: The Sequence Ontology) ",
                                 meaning=SO["1000035"]) )
        setattr(cls, "Insertion, NOS",
                PermissibleValue(text="Insertion, NOS",
                                 description="The sequence of one or more nucleotides added between two adjacent nucleotides in the sequence. (Source: The Sequence Ontology) ",
                                 meaning=SO["0000667"]) )
        setattr(cls, "Translocation, chromosomal",
                PermissibleValue(text="Translocation, chromosomal",
                                 description="A chromosomal mutation. Rearrangements that alter the pairing of telomeres are classified as translocations. (Source: The Sequence Ontology) ",
                                 meaning=SO["1000044"]) )
        setattr(cls, "Translocation, NOS",
                PermissibleValue(text="Translocation, NOS",
                                 description="A region of nucleotide sequence that has translocated to a new position. The observed adjacency of two previously separated regions. (Source: The Sequence Ontology) ",
                                 meaning=SO["0000199"]) )
        setattr(cls, "Inversion, chromosomal",
                PermissibleValue(text="Inversion, chromosomal",
                                 description="An interchromosomal mutation where a region of the chromosome is inverted with respect to wild type. (Source: The Sequence Ontology) ",
                                 meaning=SO["1000030"]) )
        setattr(cls, "Inversion, NOS",
                PermissibleValue(text="Inversion, NOS",
                                 description="A continuous nucleotide sequence is inverted in the same position. (Source: The Sequence Ontology) ",
                                 meaning=SO["1000036"]) )
        setattr(cls, "Rearrangement, fusion",
                PermissibleValue(text="Rearrangement, fusion",
                                 description="A sequence variant whereby a two genes have become joined. (Source: The Sequence Ontology) ",
                                 meaning=SO["0001565"]) )
        setattr(cls, "SNV, NOS",
                PermissibleValue(text="SNV, NOS",
                                 description="SNVs are single nucleotide positions in genomic DNA at which different sequence alternatives exist. (Source: The Sequence Ontology) ",
                                 meaning=SO["0001483"]) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class ExpressionConsequenceEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="ExpressionConsequenceEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class ChromosomalConsequenceEnum(EnumDefinitionImpl):

    Monosomy = PermissibleValue(text="Monosomy",
                                       description="A chromosomal abnormality consisting of the absence of one chromosome from the normal diploid number.",
                                       meaning=NCIT.C3239)
    Trisomy = PermissibleValue(text="Trisomy",
                                     description="A chromosomal abnormality consisting of the presence of one chromosome in addition to the normal diploid number.",
                                     meaning=NCIT.C3421)
    Nullisomy = PermissibleValue(text="Nullisomy",
                                         description="A chromosomal abnormality where a pair of homologous chromosomes that would normally be present is missing")
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="ChromosomalConsequenceEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class GenomicRegionEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="GenomicRegionEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class AllelicStateEnum(EnumDefinitionImpl):

    Homozygous = PermissibleValue(text="Homozygous",
                                           description="Having two identical allelic forms of a gene, one inherited from each parent, on each of the two homologous chromosomes.")
    Heterozygous = PermissibleValue(text="Heterozygous",
                                               description="Having two different allelic forms of a gene, one inherited from each parent, on each of the two homologous chromosomes.")
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="AllelicStateEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class InheritancePatternEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="InheritancePatternEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class ParentalStatusEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="ParentalStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class CopyNumberVariationEnum(EnumDefinitionImpl):

    Gain = PermissibleValue(text="Gain",
                               description="An increase in the number of copies of the gene.")
    Loss = PermissibleValue(text="Loss",
                               description="A decrease in the number of copies of the gene.")
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="CopyNumberVariationEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class AltStatusEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AltStatusEnum",
    )

class KaryotypeStatusEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="KaryotypeStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Normal Karyotype",
                PermissibleValue(text="Normal Karyotype",
                                 description="The assessment of the karyotype is that it is normal.",
                                 meaning=NCIT.C173277) )
        setattr(cls, "Abnormal Karyotype",
                PermissibleValue(text="Abnormal Karyotype",
                                 description="Any abnormality in the number, length, centromere position, banding pattern or differences between the sex chromosomes that is not representative of a normal set of chromosomes.",
                                 meaning=NCIT.C168875) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class DnaIndexEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="DnaIndexEnum",
    )

class CytodifferentiationEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="CytodifferentiationEnum",
    )

class MitoticRateEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="MitoticRateEnum",
    )

class LesionAssessmentReviewEnum(EnumDefinitionImpl):

    Institutional = PermissibleValue(text="Institutional",
                                                 description="Local institutional review process at treating institution.",
                                                 meaning=NCIT.C185325)
    Central = PermissibleValue(text="Central",
                                     description="Conducts reviews on behalf of all study sites that agree to participate in the centralized review process with imaging experts.",
                                     meaning=NCIT.C185326)

    _defn = EnumDefinition(
        name="LesionAssessmentReviewEnum",
    )

class LesionStateEnum(EnumDefinitionImpl):

    Present = PermissibleValue(text="Present",
                                     meaning=NCIT.C25626)
    Absent = PermissibleValue(text="Absent",
                                   meaning=NCIT.C48190)
    Unknown = PermissibleValue(text="Unknown",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="LesionStateEnum",
    )

class DetectionMethodEnum(EnumDefinitionImpl):

    Biopsy = PermissibleValue(text="Biopsy",
                                   description="The removal of tissue specimens or fluid from the living body for microscopic examination, performed to establish a diagnosis.",
                                   meaning=NCIT.C15189)
    Lymphangiogram = PermissibleValue(text="Lymphangiogram",
                                                   description="An x-ray image of the lymphatic system using a radiopaque imaging agent.",
                                                   meaning=NCIT.C16805)
    Ultrasound = PermissibleValue(text="Ultrasound",
                                           description="High frequency sound, generally with a frequency greater than 20,000 Hz.",
                                           meaning=NCIT.C64384)
    MRI = PermissibleValue(text="MRI",
                             description="Imaging that uses radiofrequency waves and a strong magnetic field rather than x-rays to provide detailed pictures of internal organs and tissues. The technique is valuable for the diagnosis of many pathologic conditions, including cancer, heart and vascular disease, stroke, and joint and musculoskeletal disorders.",
                             meaning=NCIT.C16809)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="DetectionMethodEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Staging Laparotomy",
                PermissibleValue(text="Staging Laparotomy",
                                 description="Creation of a surgical opening into the abdominal cavity.",
                                 meaning=NCIT.C15266) )
        setattr(cls, "Gallium Scan",
                PermissibleValue(text="Gallium Scan",
                                 description="A nuclear imaging procedure in which gallium-67 is used as the radiopharmaceutical. Gallium binds to transferrin, leukocyte lactoferrin, bacterial siderophores and inflammatory proteins and thereby can be used to localize foci of infection. It is also taken up by several tumors, thus gallium scintigraphy can be used for the staging of tumors.",
                                 meaning=NCIT.C38087) )
        setattr(cls, "CT Scan",
                PermissibleValue(text="CT Scan",
                                 description="A method of examining structures within the body by scanning them with X rays and using a computer to construct a series of cross-sectional scans along a single axis.",
                                 meaning=NCIT.C17204) )
        setattr(cls, "PET Scan",
                PermissibleValue(text="PET Scan",
                                 description="A technique for measuring the gamma radiation produced by collisions of electrons and positrons (anti-electrons) within living tissue. In positron emission tomography (PET), a subject is given a dose of a positron-emitting radionuclide attached to a metabolically active substance (for example, 2-fluoro-2-deoxy-D-glucose (FDG), which is similar to a naturally occurring sugar, glucose, with the addition of a radioactive fluorine atom). When living tissue containing the positron emitter is bombarded by electrons, gamma radiation produced by collisions of electrons and positrons is detected by a scanner, revealing in fine detail the tissue location of the metabolically-active substance administered.",
                                 meaning=NCIT.C17007) )
        setattr(cls, "PET-CT",
                PermissibleValue(text="PET-CT",
                                 description="An imaging technique that utilizes positron emission tomography and computed tomography in a single machine.",
                                 meaning=NCIT.C103512) )
        setattr(cls, "PET-MRI",
                PermissibleValue(text="PET-MRI",
                                 description="An imaging technique that utilizes positron emission tomography and magnetic resonance imaging in a single machine.",
                                 meaning=NCIT.C103514) )
        setattr(cls, "X-Ray",
                PermissibleValue(text="X-Ray",
                                 description="A radiographic procedure using the emission of x-rays to form an image of the structure penetrated by the radiation.",
                                 meaning=NCIT.C38101) )
        setattr(cls, "Bone Scan",
                PermissibleValue(text="Bone Scan",
                                 description="A nuclear imaging method used to evaluate pathological bone metabolism.",
                                 meaning=NCIT.C17646) )
        setattr(cls, "Physical Examination",
                PermissibleValue(text="Physical Examination",
                                 description="A systemic evaluation of the body and its functions using visual inspection, palpation, percussion and auscultation. The purpose is to determine the presence or absence of physical signs of disease or abnormality for an individual's health assessment.",
                                 meaning=NCIT.C20989) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class LesionPresentationEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="LesionPresentationEnum",
    )

class LesionSiteEnum(EnumDefinitionImpl):

    Abdomen = PermissibleValue(text="Abdomen",
                                     description="The portion of the body that lies between the thorax and the pelvis.",
                                     meaning=NCIT.C12664)
    Acetabulum = PermissibleValue(text="Acetabulum",
                                           description="Two cup shaped areas, one each on the lateral side of the lower pelvis that house the head of the femur to form the ball and socket joint of the hip.",
                                           meaning=NCIT.C32042)
    Ankle = PermissibleValue(text="Ankle",
                                 description="A gliding joint between the distal ends of the tibia and fibula and the proximal end of the talus.",
                                 meaning=NCIT.C32078)
    Anus = PermissibleValue(text="Anus",
                               description="The lower opening of the digestive tract, lying in the cleft between the buttocks, through which fecal matter is extruded.",
                               meaning=NCIT.C43362)
    Appendix = PermissibleValue(text="Appendix",
                                       description="Small tissue projection existing as a cecal diverticulum with a questionable history of vestigial versus specialized organ.",
                                       meaning=NCIT.C12380)
    Axilla = PermissibleValue(text="Axilla",
                                   description="Any one of the paired bones, 12 on either side, extending from the thoracic vertebrae toward the median line on the ventral aspect of the trunk.",
                                   meaning=NCIT.C12674)
    Basin = PermissibleValue(text="Basin",
                                 description="An organ composed of grey and white matter containing billions of neurons that is the center for intelligence and reasoning. It is protected by the bony cranium.",
                                 meaning=NCIT.C12439)
    Bladder = PermissibleValue(text="Bladder",
                                     description="The distensible sac-like organ that functions as a reservoir of urine, collecting from the kidneys and eliminating via the urethra.",
                                     meaning=NCIT.C12414)
    Bone = PermissibleValue(text="Bone",
                               description="Connective tissue that forms the skeletal components of the body.",
                               meaning=NCIT.C12366)
    Brain = PermissibleValue(text="Brain",
                                 description="An organ composed of grey and white matter containing billions of neurons that is the center for intelligence and reasoning. It is protected by the bony cranium.",
                                 meaning=NCIT.C12439)
    Breast = PermissibleValue(text="Breast",
                                   description="One of two hemispheric projections of variable size situated in the subcutaneous layer over the pectoralis major muscle on either side of the chest.",
                                   meaning=NCIT.C12971)
    Bronchus = PermissibleValue(text="Bronchus",
                                       description="Tubular structure in continuation with the trachea, serving as air passage. It terminates in the lung (terminal bronchiole).",
                                       meaning=NCIT.C12683)
    Buttock = PermissibleValue(text="Buttock",
                                     description="Either of the fleshy mounds in the rear pelvic area of the human body formed by the gluteal muscles.",
                                     meaning=NCIT.C89806)
    Calcaneum = PermissibleValue(text="Calcaneum",
                                         description="The irregular and largest tarsal bone that forms the heel.",
                                         meaning=NCIT.C32250)
    Cervix = PermissibleValue(text="Cervix",
                                   description="The lower part of the uterus occupying the region between the isthmus of the uterus and the vagina. It is divided into supravaginal and vaginal portions.",
                                   meaning=NCIT.C12311)
    Cheek = PermissibleValue(text="Cheek",
                                 description="The fleshy part of the face bounded by the eyes, nose, ear, and jaw line.",
                                 meaning=NCIT.C13070)
    Chest = PermissibleValue(text="Chest",
                                 description="The anterior side of the thorax from the neck to the abdomen. The shape of the chest is often regarded as potential insight into a disease process, as in the case of barrel chest and respiratory dysfunction.",
                                 meaning=NCIT.C25389)
    Clavicle = PermissibleValue(text="Clavicle",
                                       description="The region of the body between the neck and the upper arm.",
                                       meaning=NCIT.C24203)
    Coccyx = PermissibleValue(text="Coccyx",
                                   description="A small bone located at the bottom of the spine. The coccyx is a result of 3-5 fused rudimentary vertebrae.",
                                   meaning=NCIT.C12696)
    Colon = PermissibleValue(text="Colon",
                                 description="The part of the large intestine measured from the cecum to the rectum consisting of ascending, transverse, descending and sigmoid portions. The purpose of the colon is to remove water from digested food prior to excretion.",
                                 meaning=NCIT.C12382)
    Cutaneous = PermissibleValue(text="Cutaneous",
                                         description="Having to do with the skin.",
                                         meaning=NCIT.C13316)
    Duodenum = PermissibleValue(text="Duodenum",
                                       description="A jointed tube 25-30 cm long that connects the stomach to the jejunum.",
                                       meaning=NCIT.C12263)
    Elbow = PermissibleValue(text="Elbow",
                                 description="A type of hinge joint located between the forearm and upper arm.",
                                 meaning=NCIT.C32497)
    Epididymis = PermissibleValue(text="Epididymis",
                                           description="A crescent-like structure located in the upper and posterior surfaces of the testis. It consists of the efferent ductules and the duct of the epididymis. It facilitates the maturation of sperm that is produced in the testis.",
                                           meaning=NCIT.C12328)
    Esophagus = PermissibleValue(text="Esophagus",
                                         description="The portion of the digestive canal between the pharynx and stomach. It is about 25 cm long and consists of three parts: the cervical part, from the cricoid cartilage to the thoracic inlet; thoracic part, from thoracic inlet to the diaphragm; and abdominal part, below the diaphragm to the cardiac opening of the stomach.",
                                         meaning=NCIT.C12389)
    Eyelid = PermissibleValue(text="Eyelid",
                                   description="A thin membrane of skin with the purpose of covering and protecting an eye.",
                                   meaning=NCIT.C12713)
    Face = PermissibleValue(text="Face",
                               description="The anterior portion of the head extending from the forehead to the chin and ear to ear. The facial structures contain the eyes, nose and mouth, cheeks and jaws.",
                               meaning=NCIT.C13071)
    Femur = PermissibleValue(text="Femur",
                                 description="The upper leg bone positioned between the pelvis and the knee.",
                                 meaning=NCIT.C12717)
    Fibula = PermissibleValue(text="Fibula",
                                   description="The small, lateral calf bone extending from the knee to the ankle.",
                                   meaning=NCIT.C12718)
    Finger = PermissibleValue(text="Finger",
                                   description="Any of the digits of the hand.",
                                   meaning=NCIT.C32608)
    Foot = PermissibleValue(text="Foot",
                               description="The structure found below the ankle joint required for locomotion.",
                               meaning=NCIT.C32622)
    Forearm = PermissibleValue(text="Forearm",
                                     description="The structure on the upper limb, between the elbow and the wrist.",
                                     meaning=NCIT.C32628)
    Gallbladder = PermissibleValue(text="Gallbladder",
                                             description="A pear-shaped organ located under the liver that stores and concentrates bile secreted by the liver. From the gallbladder the bile is delivered through the bile ducts into the intestine thereby aiding the digestion of fat-containing foods.",
                                             meaning=NCIT.C12377)
    Groin = PermissibleValue(text="Groin",
                                 description="The lower region of the anterior abdominal wall located laterally to the pubic region.",
                                 meaning=NCIT.C12726)
    Hand = PermissibleValue(text="Hand",
                               description="The distal portion of the upper extremity. It consiRMS of the carpus, metacarpus, and digits.",
                               meaning=NCIT.C32712)
    Head = PermissibleValue(text="Head",
                               description="The anterior and superior part of a human bearing the mouth, the brain and sensory organs.",
                               meaning=NCIT.C12419)
    Heart = PermissibleValue(text="Heart",
                                 description="A hollow organ located slightly to the left of the middle portion of the chest. It is composed of muscle and it is divided by a septum into two sides: the right side which receives de-oxygenated blood from the body and the left side which sends newly oxygenated blood to the body. Each side is composed of two chambers: the atrium (receiving blood) and ventricle (ejecting blood).",
                                 meaning=NCIT.C12727)
    Hip = PermissibleValue(text="Hip",
                             description="The lateral prominence of the pelvis from the waist to the thigh.",
                             meaning=NCIT.C64193)
    Humerus = PermissibleValue(text="Humerus",
                                     description="The upper arm bone between the shoulder and elbow.",
                                     meaning=NCIT.C12731)
    Hypopharynx = PermissibleValue(text="Hypopharynx",
                                             description="The lower part of the pharynx that connects to the esophagus.",
                                             meaning=NCIT.C12246)
    Ilium = PermissibleValue(text="Ilium",
                                 description="The broad, dorsal, upper, and widest of the three principal bones composing either half of the pelvis.",
                                 meaning=NCIT.C32765)
    Intraperitoneal = PermissibleValue(text="Intraperitoneal",
                                                     description="Relating to the peritoneal cavity as the intended site of administration.",
                                                     meaning=NCIT.C13352)
    Intrathoracic = PermissibleValue(text="Intrathoracic",
                                                 description="Within the thoracic cavity.",
                                                 meaning=NCIT.C105579)
    Ischium = PermissibleValue(text="Ischium",
                                     description="The most posterior and ventral bone making up the pelvis.",
                                     meaning=NCIT.C32884)
    Kidney = PermissibleValue(text="Kidney",
                                   description="One of the two bean-shaped organs located on each side of the spine in the retroperitoneum. The right kidney is located below the liver and the left kidney below the diaphragm. The kidneys filter and secrete metabolic products and minerals from the blood, thus maintaining homeostasis. On the superior pole of each kidney there is an adrenal gland. Each kidney and adrenal gland is surrounded by fat.",
                                   meaning=NCIT.C77608)
    Knee = PermissibleValue(text="Knee",
                               description="A joint connecting the lower part of the femur with the upper part of the tibia. The lower part of the femur and the upper part of the tibia are attached to each other by ligaments. Other structures of the knee joint include the upper part of the fibula, located below and parallel to the tibia, and the patella which moves as the knee bends.",
                               meaning=NCIT.C32898)
    Larynx = PermissibleValue(text="Larynx",
                                   description="The cartilaginous structure of the respiratory tract between the pharynx and the trachea. It contains elastic vocal cords required for sound production.",
                                   meaning=NCIT.C12420)
    Leg = PermissibleValue(text="Leg",
                             description="One of the two lower extremities in humans used for locomotion and support.",
                             meaning=NCIT.C32974)
    Liver = PermissibleValue(text="Liver",
                                 description="A triangular-shaped organ located under the diaphragm in the right hypochondrium. It is the largest internal organ of the body, weighting up to 2 kg. Metabolism and bile secretion are its main functions. It is composed of cells which have the ability to regenerate.",
                                 meaning=NCIT.C12392)
    Lung = PermissibleValue(text="Lung",
                               description="One of a pair of viscera occupying the pulmonary cavities of the thorax, the organs of respiration in which aeration of the blood takes place. As a rule, the right lung is slightly larger than the left and is divided into three lobes (an upper, a middle, and a lower or basal), while the left has two lobes (an upper and a lower or basal). Each lung is irregularly conical in shape, presenting a blunt upper extremity (the apex), a concave base following the curve of the diaphragm, an outer convex surface (costal surface), an inner or mediastinal surface (mediastinal surface), a thin and sharp anterior border, and a thick and rounded posterior border.",
                               meaning=NCIT.C12468)
    Mandible = PermissibleValue(text="Mandible",
                                       description="The lower jaw bone holding the lower teeth.",
                                       meaning=NCIT.C12290)
    Maxilla = PermissibleValue(text="Maxilla",
                                     description="The upper jawbone in vertebrates; it is fused to the cranium.",
                                     meaning=NCIT.C26470)
    Mediastinum = PermissibleValue(text="Mediastinum",
                                             description="A group of organs surrounded by loose connective tissue, separating the two pleural sacs, between the sternum anteriorly and the vertebral column posteriorly as well as from the thoracic inlet superiorly to the diaphragm inferiorly. The mediastinum contains the heart and pericardium, the bases of the great vessels, the trachea and bronchi, esophagus, thymus, lymph nodes, thoracic duct, phrenic and vagus nerves, and other structures and tissues.",
                                             meaning=NCIT.C12748)
    Meninges = PermissibleValue(text="Meninges",
                                       description="Any one of three membranes that surround the brain and spinal cord.",
                                       meaning=NCIT.C12348)
    Metacarpus = PermissibleValue(text="Metacarpus",
                                           description="Any of the five bones between the wrist and the fingers that form the skeleton of the palm.",
                                           meaning=NCIT.C12751)
    Metatarsus = PermissibleValue(text="Metatarsus",
                                           description="A bone belonging to the middle part of the foot located between toes and ankle. There are 5 metatarsal bones and they are numbered from the medial side.",
                                           meaning=NCIT.C12752)
    Nasopharynx = PermissibleValue(text="Nasopharynx",
                                             description="The part of the pharynx in the back of the throat, at and above the soft palate. The nasopharynx is continuous with the nasal passages.",
                                             meaning=NCIT.C12423)
    Neck = PermissibleValue(text="Neck",
                               description="The region that connects the head to the rest of the body.",
                               meaning=NCIT.C13063)
    Orbit = PermissibleValue(text="Orbit",
                                 description="The bony cavity of the skull which contains the eye, anterior portion of the optic nerve, ocular muscles and ocular adnexa. Seven bones contribute to the structure of the orbit: the frontal, maxillary, zygomatic, sphenoid, lacrimal, ethmoid, and palatine bones.",
                                 meaning=NCIT.C12347)
    Oropharynx = PermissibleValue(text="Oropharynx",
                                           description="The part of the pharynx between the soft palate and the upper portion of the epiglottis.",
                                           meaning=NCIT.C12762)
    Ovary = PermissibleValue(text="Ovary",
                                 description="One of the paired female reproductive glands containing the ova or germ cells; the ovary's stroma is a vascular connective tissue containing numbers of ovarian follicles enclosing the ova.",
                                 meaning=NCIT.C12404)
    Pancreas = PermissibleValue(text="Pancreas",
                                       description="An organ behind the lower part of the stomach that is the shape of a fish and about the size of a hand. It is a compound gland composed of both exocrine and endocrine tissues. The endocrine pancreas makes insulin so that the body can use glucose (sugar) for energy. The exocrine pancreas makes enzymes that help the body digest food. Spread all over the pancreas are areas called the Islets of Langerhans. The cells in these areas each have a special purpose. The alpha cells make glucagon, which raises the level of glucose in the blood; the beta cells make insulin; the delta cells make somatostatin. There are also PP cells and D1 cells, about which little is known.",
                                       meaning=NCIT.C12393)
    Paraspinal = PermissibleValue(text="Paraspinal",
                                           description="Pertaining to muscles and/or tissue adjacent to the spinal column.",
                                           meaning=NCIT.C129461)
    Paratesticular = PermissibleValue(text="Paratesticular",
                                                   description="A small anatomical compartment that contains the testicular collecting system, and mesothelial and mesenchymal components that represent extensions of the abdominal cavity and retroperitoneum.",
                                                   meaning=NCIT.C162491)
    Parotid = PermissibleValue(text="Parotid",
                                     description="The largest of the three paired salivary glands, located in front of the ear.",
                                     meaning=NCIT.C12427)
    Patella = PermissibleValue(text="Patella",
                                     description="A small flat triangular bone in front of the knee that articulates with the femur and protects the knee joint.",
                                     meaning=NCIT.C33282)
    Pelvis = PermissibleValue(text="Pelvis",
                                   description="The bony, basin-shaped structure formed by the hipbones and the base of the backbone supporting the lower limbs in humans.",
                                   meaning=NCIT.C12767)
    Penis = PermissibleValue(text="Penis",
                                 description="The male organ of urination and copulation.",
                                 meaning=NCIT.C12409)
    Perineum = PermissibleValue(text="Perineum",
                                       description="The area located between the anus and vulva in females, and anus and scrotum in males.",
                                       meaning=NCIT.C33301)
    Peritoneum = PermissibleValue(text="Peritoneum",
                                           description="The tissue that lines the wall of the abdominal cavity, intestine, mesentery, and pelvic organs. It consiRMS of the parietal peritoneum and the visceral peritoneum.",
                                           meaning=NCIT.C12770)
    Pineal = PermissibleValue(text="Pineal",
                                   description="A small endocrine gland in the brain, situated beneath the back part of the corpus callosum, that secretes melatonin.",
                                   meaning=NCIT.C12398)
    Pleura = PermissibleValue(text="Pleura",
                                   description="The tissue that lines the wall of the thoracic cavity and the surface of the lungs.",
                                   meaning=NCIT.C12469)
    Prostate = PermissibleValue(text="Prostate",
                                       description="The walnut shaped accessory sex gland of the male reproductive system. It is located in the pelvis just below the bladder, surrounding the prostatic part of the urethra. The prostate gland secretes a fluid which is part of the semen.",
                                       meaning=NCIT.C12410)
    Rectum = PermissibleValue(text="Rectum",
                                   description="The terminal portion of the gastrointestinal tract, extending from the rectosigmoid junction to the anal canal.",
                                   meaning=NCIT.C12390)
    Retroperitoneum = PermissibleValue(text="Retroperitoneum",
                                                     description="The back of the abdomen where the kidneys lie and the great blood vessels run.",
                                                     meaning=NCIT.C12298)
    Rib = PermissibleValue(text="Rib",
                             description="Any one of the paired bones, 12 on either side, extending from the thoracic vertebrae toward the median line on the ventral aspect of the trunk. The long curved bones which form the rib cage. Generally, ribs 1 to 7 are connected to the sternum by their costal cartilages and are called true ribs, whereas ribs 8 to 12 are termed false ribs.",
                             meaning=NCIT.C12782)
    Sacrum = PermissibleValue(text="Sacrum",
                                   description="The triangular bone, made up of 5 fused bones of the spine, located in the lower area of the spine between the fifth lumbar vertebra and the coccyx.",
                                   meaning=NCIT.C33508)
    Sacrococcygeal = PermissibleValue(text="Sacrococcygeal",
                                                   description="The amphiarthrodial joint between the sacrum and coccyx.",
                                                   meaning=NCIT.C33506)
    Scalp = PermissibleValue(text="Scalp",
                                 description="The skin which covers the top of the head and which is usually covered by hair.",
                                 meaning=NCIT.C89807)
    Scapula = PermissibleValue(text="Scapula",
                                     description="One of the five bones situated between the thoracic vertebrae and the sacrum in the lower part of the spine.",
                                     meaning=NCIT.C12744)
    Shoulder = PermissibleValue(text="Shoulder",
                                       description="The flat triangle-shaped bone that connects the humerus with the clavicle in the back of the shoulder.",
                                       meaning=NCIT.C12783)
    Skin = PermissibleValue(text="Skin",
                               description="An organ that constitutes the external surface of the body. It consiRMS of the epidermis, dermis, and skin appendages.",
                               meaning=NCIT.C12470)
    Skull = PermissibleValue(text="Skull",
                                 description="The bones that form the head, made up of the bones of the braincase and face.",
                                 meaning=NCIT.C12789)
    Spine = PermissibleValue(text="Spine",
                                 description="A series of bones, muscles, tendons, and other tissues reaching from the base of the skull to the tailbone. The vertebral column forms the axis of the skeleton and encloses as well as protects the spinal cord and the fluid surrounding the spinal cord.",
                                 meaning=NCIT.C12998)
    Spleen = PermissibleValue(text="Spleen",
                                   description="An organ that is part of the hematopoietic and immune systems. It is composed of the white pulp and the red pulp and is surrounded by a capsule. It is located in the left hypochondriac region. Its functions include lymphocyte production, blood cell storage, and blood cell destruction.",
                                   meaning=NCIT.C12432)
    Sternum = PermissibleValue(text="Sternum",
                                     description="The total system of structures outside the lungs that move as a part of breathing; it includes all structures from the skin to the parietal pleura.",
                                     meaning=NCIT.C62484)
    Stomach = PermissibleValue(text="Stomach",
                                     description="An organ located under the diaphragm, between the liver and the spleen as well as between the esophagus and the small intestine. The stomach is the primary organ of food digestion.",
                                     meaning=NCIT.C12391)
    Talus = PermissibleValue(text="Talus",
                                 description="The bone of the foot that connects with the tibia and fibula to form the ankle joint.",
                                 meaning=NCIT.C52799)
    Testis = PermissibleValue(text="Testis",
                                   description="Either of the paired male reproductive glands that produce the male germ cells and the male hormones.",
                                   meaning=NCIT.C12412)
    Thalamus = PermissibleValue(text="Thalamus",
                                       description="An ovoid mass composed predominantly of gray substance and associated laminae of white substance. The thalamus is divided into anterior, medial, and lateral parts. The function of the thalamus is to relay sensory impulses and cerebellar and basal ganglia projections to the cerebral cortex. The thalamus is positioned within the posterior part of the diencephalon forming most of each lateral wall of the third ventricle.",
                                       meaning=NCIT.C12459)
    Thigh = PermissibleValue(text="Thigh",
                                 description="A part of the lower limb, located between hip and knee.",
                                 meaning=NCIT.C33763)
    Thorax = PermissibleValue(text="Thorax",
                                   description="The division of the body lying between the neck and the abdomen.",
                                   meaning=NCIT.C12799)
    Thyroid = PermissibleValue(text="Thyroid",
                                     description="An endocrine gland located at the base of the neck that produces and secretes thyroxine and other hormones. Thyroxine is important for metabolic control.",
                                     meaning=NCIT.C12400)
    Tibia = PermissibleValue(text="Tibia",
                                 description="A bone located between the femur and the tarsus, being part of the lower leg.",
                                 meaning=NCIT.C12800)
    Toe = PermissibleValue(text="Toe",
                             description="One of the terminal digits of the foot.",
                             meaning=NCIT.C33788)
    Tonsil = PermissibleValue(text="Tonsil",
                                   description="The two organs situated in the throat on either side of the narrow passage from the mouth to the pharynx. They are composed of lymphoid tissues.",
                                   meaning=NCIT.C12802)
    Trunk = PermissibleValue(text="Trunk",
                                 description="The body excluding the head and neck and limbs.",
                                 meaning=NCIT.C33816)
    Ulna = PermissibleValue(text="Ulna",
                               description="One of the bones that comprise the forearm. The largest aspect articulates with the humerus at the elbow joint and the smallest portion of the ulna articulates with the carpal bones in the wrist.",
                               meaning=NCIT.C12809)
    Ureter = PermissibleValue(text="Ureter",
                                   description="The thick-walled tube that carries urine from each kidney to the bladder.",
                                   meaning=NCIT.C12416)
    Uterus = PermissibleValue(text="Uterus",
                                   description="A hollow, thick-walled, muscular organ located within the pelvic cavity of a woman. Within the uterus the fertilized egg implants and the fetus develops during pregnancy.",
                                   meaning=NCIT.C12405)
    Vagina = PermissibleValue(text="Vagina",
                                   description="The female genital canal, extending from the uterus to the vulva.",
                                   meaning=NCIT.C12407)
    Viscera = PermissibleValue(text="Viscera",
                                     description="Two or more internal organs.",
                                     meaning=NCIT.C28287)
    Vulva = PermissibleValue(text="Vulva",
                                 description="The external, visible part of the female genitalia surrounding the urethral and vaginal opening. The vulva includes the clitoris and inner as well as outer labia.",
                                 meaning=NCIT.C12408)
    Wrist = PermissibleValue(text="Wrist",
                                 description="A joint between the distal end of the radius and the proximal row of carpal bones.",
                                 meaning=NCIT.C33894)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="LesionSiteEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Abdominal Wall",
                PermissibleValue(text="Abdominal Wall",
                                 description="Occurring in, or located in the retroperitoneum.",
                                 meaning=NCIT.C28256) )
        setattr(cls, "Adrenal Gland",
                PermissibleValue(text="Adrenal Gland",
                                 description="A flattened, roughly triangular body resting upon the upper end of each kidney; it is one of the ductless glands furnishing internal secretions (epinephrine and norepinephrine from the medulla and steroid hormones from the cortex).",
                                 meaning=NCIT.C12666) )
        setattr(cls, "Anal/Perianal",
                PermissibleValue(text="Anal/Perianal",
                                 description="The lower opening of the digestive tract, lying in the cleft between the buttocks, through which fecal matter is extruded. | The skin around the anus",
                                 meaning=NCIT.C43362) )
        setattr(cls, "Ankle Joint",
                PermissibleValue(text="Ankle Joint",
                                 description="A gliding joint between the distal ends of the tibia and fibula and the proximal end of the talus.",
                                 meaning=NCIT.C32078) )
        setattr(cls, "Anterior Skull Base",
                PermissibleValue(text="Anterior Skull Base",
                                 description="The portion of the skull that is formed laterally by the orbital plates of the frontal bone, medially by the cribriform palate and crista galli of the ethmoid bone, and posteriorly by the planum sphenoidale and lesser wings of the sphenoid bone.",
                                 meaning=NCIT.C180372) )
        setattr(cls, "Ascitic Fluid",
                PermissibleValue(text="Ascitic Fluid",
                                 description="A biospecimen of ascitic fluid.",
                                 meaning=NCIT.C159203) )
        setattr(cls, "Axillary Nodes",
                PermissibleValue(text="Axillary Nodes",
                                 description="One of approximately 20-30 lymph nodes in chain formation that traverse the concavity of the underarm to the clavicle.",
                                 meaning=NCIT.C12904) )
        setattr(cls, "Bladder/Prostate",
                PermissibleValue(text="Bladder/Prostate",
                                 description="The walnut shaped accessory sex gland of the male reproductive system. It is located in the pelvis just below the bladder, surrounding the prostatic part of the urethra. The prostate gland secretes a fluid which is part of the semen.",
                                 meaning=NCIT.C12410) )
        setattr(cls, "Bone Face",
                PermissibleValue(text="Bone Face",
                                 description="Any bone that contributes to the facial structures, except those bones that are part of the braincase.",
                                 meaning=NCIT.C63706) )
        setattr(cls, "Bone Foot",
                PermissibleValue(text="Bone Foot",
                                 description="One of the seven tarsal, five metatarsal, or 14 phalangeal bones in the foot.",
                                 meaning=NCIT.C13068) )
        setattr(cls, "Bone Marrow",
                PermissibleValue(text="Bone Marrow",
                                 description="The tissue occupying the spaces of bone. It consiRMS of blood vessel sinuses and a network of hematopoietic cells which give rise to the red cells, white cells, and megakaryocytes.",
                                 meaning=NCIT.C12431) )
        setattr(cls, "Bone or Bone Marrow",
                PermissibleValue(text="Bone or Bone Marrow",
                                 description="Connective tissue that forms the skeletal components of the body. | The tissue occupying the spaces of bone. It consiRMS of blood vessel sinuses and a network of hematopoietic cells which give rise to the red cells, white cells, and megakaryocytes.",
                                 meaning=NCIT.C12366) )
        setattr(cls, "Bone Shoulder Girdle",
                PermissibleValue(text="Bone Shoulder Girdle",
                                 description="The bony arch formed by the collarbones and shoulder blades.",
                                 meaning=NCIT.C33547) )
        setattr(cls, "Brain/Leptomeninges",
                PermissibleValue(text="Brain/Leptomeninges",
                                 description="An organ composed of grey and white matter containing billions of neurons that is the center for intelligence and reasoning. It is protected by the bony cranium. | The two innermost layers of tissue that cover the brain and spinal cord, the arachnoid mater and the pia mater.",
                                 meaning=NCIT.C12439) )
        setattr(cls, "Carpal Bone",
                PermissibleValue(text="Carpal Bone",
                                 description="Any of the small bones of the wrist joint, located between the radius and the ulna and the metacarpus.",
                                 meaning=NCIT.C12688) )
        setattr(cls, "Celiac Nodes",
                PermissibleValue(text="Celiac Nodes",
                                 description="A lymph node at the base of the celiac artery.",
                                 meaning=NCIT.C65166) )
        setattr(cls, "Central Nervous System",
                PermissibleValue(text="Central Nervous System",
                                 description="The part of the nervous system that consiRMS of the brain, spinal cord, and meninges.",
                                 meaning=NCIT.C12438) )
        setattr(cls, "Cervical Nodes",
                PermissibleValue(text="Cervical Nodes",
                                 description="Any of the lymph nodes located in the neck.",
                                 meaning=NCIT.C32298) )
        setattr(cls, "Cervical Spine",
                PermissibleValue(text="Cervical Spine",
                                 description="The set of vertebrae immediately caudal to the skull.",
                                 meaning=NCIT.C69313) )
        setattr(cls, "Cervical Vertebra",
                PermissibleValue(text="Cervical Vertebra",
                                 description="One of the two bean-shaped organs located on each side of the spine in the retroperitoneum. The right kidney is located below the liver and the left kidney below the diaphragm. The kidneys filter and secret the metabolic products and minerals from the blood, thus maintaining the homeostasis. On the superior pole of each kidney there is an adrenal gland. Each kidney and adrenal gland is surrounded by fat.",
                                 meaning=NCIT.C12415) )
        setattr(cls, "Chest Wall",
                PermissibleValue(text="Chest Wall",
                                 description="The total system of structures outside the lungs that move as a part of breathing; it includes all structures from the skin to the parietal pleura.",
                                 meaning=NCIT.C62484) )
        setattr(cls, "Cerebrospinal Fluid",
                PermissibleValue(text="Cerebrospinal Fluid",
                                 description="The fluid that is contained within the brain ventricles, the subarachnoid space and the central canal of the spinal cord.",
                                 meaning=NCIT.C12692) )
        setattr(cls, "Dorsal Spine",
                PermissibleValue(text="Dorsal Spine",
                                 description="A spinal curve that originates at the middle of the second thoracic vertebra and terminates at the middle of the last thoracic vertebra.",
                                 meaning=NCIT.C32472) )
        setattr(cls, "Dorsal Vertebra",
                PermissibleValue(text="Dorsal Vertebra",
                                 description="Any one of the seven vertebrae that start with C1, connecting the skull to the spine, and ends with C7, which joins the cervical with the thoracic spine.",
                                 meaning=NCIT.C12693) )
        setattr(cls, "Elbow Joint",
                PermissibleValue(text="Elbow Joint",
                                 description="A type of hinge joint located between the forearm and upper arm.",
                                 meaning=NCIT.C32497) )
        setattr(cls, "Epitrochlear Nodes",
                PermissibleValue(text="Epitrochlear Nodes",
                                 description="A lymph node located above and adjacent to the elbow.",
                                 meaning=NCIT.C98182) )
        setattr(cls, "Ethmoid Bone",
                PermissibleValue(text="Ethmoid Bone",
                                 description="A light and spongy bone that is cubical in shape. This bone is positioned at the anterior part of the cranium, sitting between the two orbits, at the roof of the nose. It consiRMS of four parts: a horizontal or cribriform plate; a perpendicular plate; and two lateral masses or labyrinths.",
                                 meaning=NCIT.C12711) )
        setattr(cls, "Fallopian Tube",
                PermissibleValue(text="Fallopian Tube",
                                 description="One of a pair of tubes that extend from the uterus to each of the ovaries. Following ovulation the egg travels down the fallopian tube to the uterus where fertilization may or may not occur.",
                                 meaning=NCIT.C12403) )
        setattr(cls, "Female Reproductive System Part",
                PermissibleValue(text="Female Reproductive System Part",
                                 description="Any component of the female organs and tissues involved in the production and maturation of gametes and in their union and subsequent development as offspring.",
                                 meaning=NCIT.C13039) )
        setattr(cls, "Fibular Head",
                PermissibleValue(text="Fibular Head",
                                 description="The highest portion of the fibula that articulates with the patella.",
                                 meaning=NCIT.C32719) )
        setattr(cls, "Foot Joint",
                PermissibleValue(text="Foot Joint",
                                 description="The structure found below the ankle joint required for locomotion.",
                                 meaning=NCIT.C32623) )
        setattr(cls, "Foot Phalanges",
                PermissibleValue(text="Foot Phalanges",
                                 description="A bone of the foot.",
                                 meaning=NCIT.C52772) )
        setattr(cls, "Frontal Bone",
                PermissibleValue(text="Frontal Bone",
                                 description="A bone of the skull forming the forehead, root of the nose and the roof of both orbits.",
                                 meaning=NCIT.C32635) )
        setattr(cls, "Frontal Cortex",
                PermissibleValue(text="Frontal Cortex",
                                 description="The part of the brain located anterior to the parietal lobes at the front of each cerebral hemisphere.",
                                 meaning=NCIT.C12352) )
        setattr(cls, "Gastrointestinal Tract",
                PermissibleValue(text="Gastrointestinal Tract",
                                 description="The upper gastrointestinal (GI) tract is comprised of mouth, pharynx, esophagus and stomach while the lower GI tract consists of intestines and anus. The primary function of the GI tract is to ingest, digest, absorb and ultimately excrete food stuff.",
                                 meaning=NCIT.C34082) )
        setattr(cls, "Hand Bone",
                PermissibleValue(text="Hand Bone",
                                 description="A bone of the hand.",
                                 meaning=NCIT.C52771) )
        setattr(cls, "Hand Joint",
                PermissibleValue(text="Hand Joint",
                                 description="The hinge synovial joints between the phalanges of the fingers.",
                                 meaning=NCIT.C32868) )
        setattr(cls, "Hand Phalanges",
                PermissibleValue(text="Hand Phalanges",
                                 description="For oncology, an area of the body generally construed to comprise the base of skull and facial bones, sinuses, orbits, salivary glands, oral cavity, oropharynx, larynx, thyroid, facial and neck musculature and lymph nodes draining these areas.",
                                 meaning=NCIT.C12418) )
        setattr(cls, "Head and Neck",
                PermissibleValue(text="Head and Neck",
                                 description="For oncology, an area of the body generally construed to comprise the base of skull and facial bones, sinuses, orbits, salivary glands, oral cavity, oropharynx, larynx, thyroid, facial and neck musculature and lymph nodes draining these areas.",
                                 meaning=NCIT.C12418) )
        setattr(cls, "Hilar Nodes",
                PermissibleValue(text="Hilar Nodes",
                                 description="A lymph node located in the hilar region of the spleen.",
                                 meaning=NCIT.C33600) )
        setattr(cls, "Hip/Inguinal Region",
                PermissibleValue(text="Hip/Inguinal Region",
                                 description="The lateral prominence of the pelvis from the waist to the thigh. | The lower region of the anterior abdominal wall located laterally to the pubic region.",
                                 meaning=NCIT.C64193) )
        setattr(cls, "Iliac Crest",
                PermissibleValue(text="Iliac Crest",
                                 description="The broad, dorsal, upper, and widest of the three principal bones composing either half of the pelvis.",
                                 meaning=NCIT.C32765) )
        setattr(cls, "Inferior Limb",
                PermissibleValue(text="Inferior Limb",
                                 description="A bone of the leg (lower extremity).",
                                 meaning=NCIT.C12982) )
        setattr(cls, "Infraclavicular Lymph Node",
                PermissibleValue(text="Infraclavicular Lymph Node",
                                 description="A lymph node located in the area below the clavicle.",
                                 meaning=NCIT.C63705) )
        setattr(cls, "Inguinal Nodes",
                PermissibleValue(text="Inguinal Nodes",
                                 description="A superficial or deep lymph node located in the inguinal area.",
                                 meaning=NCIT.C32801) )
        setattr(cls, "Intra-abdominal",
                PermissibleValue(text="Intra-abdominal",
                                 description="The lower region of the anterior abdominal wall located laterally to the pubic region.",
                                 meaning=NCIT.C12726) )
        setattr(cls, "Knee Joint",
                PermissibleValue(text="Knee Joint",
                                 description="A joint connecting the lower part of the femur with the upper part of the tibia. The lower part of the femur and the upper part of the tibia are attached to each other by ligaments. Other structures of the knee joint include the upper part of the fibula, located below and parallel to the tibia, and the patella which moves as the knee bends.",
                                 meaning=NCIT.C32899) )
        setattr(cls, "Lacrimal Bone",
                PermissibleValue(text="Lacrimal Bone",
                                 description="A small rectangular thin plate forming part of the medial orbit wall. It is located posterior to the frontal process of the maxilla and articulates with the inferior nasal concha, ethmoid, frontal, and maxillary bones.",
                                 meaning=NCIT.C32906) )
        setattr(cls, "Liver/Biliary Tract",
                PermissibleValue(text="Liver/Biliary Tract",
                                 description="A triangular-shaped organ located under the diaphragm in the right hypochondrium. It is the largest internal organ of the body, weighting up to 2 kg. Metabolism and bile secretion are its main functions. It is composed of cells which have the ability to regenerate. | The system that transports bile from the hepatocytes in the liver to the small intestine. It is comprised of the intrahepatic bile ducts, hepatic ducts, common bile duct, cystic duct, and the gallbladder.",
                                 meaning=NCIT.C12392) )
        setattr(cls, "Lower Extremity",
                PermissibleValue(text="Lower Extremity",
                                 description="The limb that is composed of the hip, thigh, leg and foot.",
                                 meaning=NCIT.C12742) )
        setattr(cls, "Lower Limb",
                PermissibleValue(text="Lower Limb",
                                 description="The limb that is composed of the hip, thigh, leg and foot.",
                                 meaning=NCIT.C12742) )
        setattr(cls, "Lower Spine",
                PermissibleValue(text="Lower Spine",
                                 description="Those vertebrae between the ribs and the pelvis, L1-L5 in man.",
                                 meaning=NCIT.C69314) )
        setattr(cls, "Lumbar Vertebra",
                PermissibleValue(text="Lumbar Vertebra",
                                 description="Pertaining to the back or upper surface of the body; opposite of ventral.",
                                 meaning=NCIT.C45874) )
        setattr(cls, "Lymph Nodes",
                PermissibleValue(text="Lymph Nodes",
                                 description="A bean-shaped organ surrounded by a connective tissue capsule. It is part of the lymphatic system and is found throughout the body. It is composed predominantly of lymphocytes and its main function is immune protection.",
                                 meaning=NCIT.C12745) )
        setattr(cls, "Mesenteric Nodes",
                PermissibleValue(text="Mesenteric Nodes",
                                 description="A lymph node located in the mesentery.",
                                 meaning=NCIT.C77641) )
        setattr(cls, "Middle Ear",
                PermissibleValue(text="Middle Ear",
                                 description="The part of the ear including the eardrum and ossicles. The middle ear leads to the inner ear.",
                                 meaning=NCIT.C12274) )
        setattr(cls, "Nasal Bone",
                PermissibleValue(text="Nasal Bone",
                                 description="One of two small oblong bones placed side by side at the middle and upper part of the face.",
                                 meaning=NCIT.C33157) )
        setattr(cls, "Nasal Cavity",
                PermissibleValue(text="Nasal Cavity",
                                 description="The proximal portion of the respiratory passages on either side of the nasal septum lying between the floor of the cranium and the roof of the mouth and extending from the face to the pharynx. The nasal cavity is lined with ciliated mucosa, extending from the nares to the pharynx.",
                                 meaning=NCIT.C12424) )
        setattr(cls, "Nasal Cavity and Paranasal Sinuses",
                PermissibleValue(text="Nasal Cavity and Paranasal Sinuses",
                                 description="The proximal portion of the respiratory passages on either side of the nasal septum lying between the floor of the cranium and the roof of the mouth and extending from the face to the pharynx. The nasal cavity is lined with ciliated mucosa, extending from the nares to the pharynx. | Any one of the air-filled spaces within the ethmoid, frontal, maxillary, or sphenoid bones, which communicate with the nasal cavity.",
                                 meaning=NCIT.C12424) )
        setattr(cls, "Nasal Septum",
                PermissibleValue(text="Nasal Septum",
                                 description="The thin wall between the two nasal cavities.",
                                 meaning=NCIT.C33160) )
        setattr(cls, "Occipital Bone",
                PermissibleValue(text="Occipital Bone",
                                 description="The trapezoidal-shaped bone that forms the back and part of the base of the skull.",
                                 meaning=NCIT.C12757) )
        setattr(cls, "Occiptial Cortex",
                PermissibleValue(text="Occiptial Cortex",
                                 description="One of the four regions of cortex in each cerebral hemisphere. It is located posterior to the temporal lobe and inferior to the parietal lobe.",
                                 meaning=NCIT.C12355) )
        setattr(cls, "Omentum/Peritoneum",
                PermissibleValue(text="Omentum/Peritoneum",
                                 description="A fold of peritoneum originating at the stomach and supporting the viscera.",
                                 meaning=NCIT.C33209) )
        setattr(cls, "Oral Cavity",
                PermissibleValue(text="Oral Cavity",
                                 description="The cavity located at the upper end of the alimentary canal, behind the teeth and gums that is bounded on the outside by the lips, above by the hard and soft palates and below by the tongue.",
                                 meaning=NCIT.C12421) )
        setattr(cls, "Paraaortic Lymph Node",
                PermissibleValue(text="Paraaortic Lymph Node",
                                 description="A lymph node located adjacent to the lumbar region of the spine.",
                                 meaning=NCIT.C77643) )
        setattr(cls, "Paranasal Sinuses",
                PermissibleValue(text="Paranasal Sinuses",
                                 description="Any one of the air-filled spaces within the ethmoid, frontal, maxillary, or sphenoid bones, which communicate with the nasal cavity.",
                                 meaning=NCIT.C12763) )
        setattr(cls, "Parietal Bone",
                PermissibleValue(text="Parietal Bone",
                                 description="One of two cranial bones that by their union form the sides and roof of the skull.",
                                 meaning=NCIT.C12766) )
        setattr(cls, "Parietal Cortex",
                PermissibleValue(text="Parietal Cortex",
                                 description="One of the lobes of the cerebral hemisphere located superiorly to the occipital lobe and posteriorly to the frontal lobe. Cognition and visuospatial processing are its main functions.",
                                 meaning=NCIT.C12354) )
        setattr(cls, "Pectoral Nodes",
                PermissibleValue(text="Pectoral Nodes",
                                 description="An axillary lymph node located along the lower edge of the pectoralis minor.",
                                 meaning=NCIT.C120322) )
        setattr(cls, "Pleural Effusion",
                PermissibleValue(text="Pleural Effusion",
                                 description="Increased amounts of fluid within the pleural cavity. Symptoms include shortness of breath, cough, and chest pain. It is usually caused by lung infections, congestive heart failure, pleural and lung tumors, connective tissue disorders, and trauma.",
                                 meaning=NCIT.C3331) )
        setattr(cls, "Popliteal Nodes",
                PermissibleValue(text="Popliteal Nodes",
                                 description="Lymph node located within the fat layer of the knee joint.",
                                 meaning=NCIT.C53146) )
        setattr(cls, "Preauricular Lymph Node",
                PermissibleValue(text="Preauricular Lymph Node",
                                 description="A lymph node located anterior to the auricle of the ear. (NCI)",
                                 meaning=NCIT.C103429) )
        setattr(cls, "Radius Bone",
                PermissibleValue(text="Radius Bone",
                                 description="The long bone of the forearm that extends from the lateral aspect of the elbow to the thumb-side of the wrist.",
                                 meaning=NCIT.C12777) )
        setattr(cls, "Sacral Region",
                PermissibleValue(text="Sacral Region",
                                 description="The triangular bone, made up of 5 fused bones of the spine, located in the lower area of the spine between the fifth lumbar vertebra and the coccyx.",
                                 meaning=NCIT.C33508) )
        setattr(cls, "Salivary Gland",
                PermissibleValue(text="Salivary Gland",
                                 description="An exocrine gland that secretes saliva. Salivary glands are mostly located in and around the oral cavity.",
                                 meaning=NCIT.C12426) )
        setattr(cls, "Shoulder Girdle",
                PermissibleValue(text="Shoulder Girdle",
                                 description="The bony arch formed by the collarbones and shoulder blades.",
                                 meaning=NCIT.C33547) )
        setattr(cls, "Shoulder Joint",
                PermissibleValue(text="Shoulder Joint",
                                 description="A ball-and-socket joint at the upper end of the humerus, located at the junction of humerus and scapula.",
                                 meaning=NCIT.C33548) )
        setattr(cls, "Small Intestine",
                PermissibleValue(text="Small Intestine",
                                 description="The section of the intestines between the pylorus and cecum. The small intestine is approximately 20 feet long and consists of the duodenum, the jejunum, and the ileum. Its main function is to absorb nutrients from food as the food is transported to the large intestine.",
                                 meaning=NCIT.C12386) )
        setattr(cls, "Soft Tissue",
                PermissibleValue(text="Soft Tissue",
                                 description="A general term comprising tissue that is not hardened or calcified; including muscle, fat, blood vessels, nerves, tendons, ligaments and fascia.",
                                 meaning=NCIT.C12471) )
        setattr(cls, "Spheniod Bone",
                PermissibleValue(text="Spheniod Bone",
                                 description="The butterfly-shaped bone located at the base of the skull that helps to form the orbit of the eye.",
                                 meaning=NCIT.C12790) )
        setattr(cls, "Spinal Cord",
                PermissibleValue(text="Spinal Cord",
                                 description="The elongated, approximately cylindrical part of the central nervous system of vertebrates that lies in the vertebral canal and from which the spinal nerves emerge.",
                                 meaning=NCIT.C12464) )
        setattr(cls, "Splenic Hilar Nodes",
                PermissibleValue(text="Splenic Hilar Nodes",
                                 description="A lymph node located in the hilar region of the spleen.",
                                 meaning=NCIT.C33600) )
        setattr(cls, "Superior Maxilla",
                PermissibleValue(text="Superior Maxilla",
                                 description="The facial bone that forms the mediala floor of the orbit.",
                                 meaning=NCIT.C33682) )
        setattr(cls, "Supraclavicular Lymph Node",
                PermissibleValue(text="Supraclavicular Lymph Node",
                                 description="A lymph node which is located above the clavicle.",
                                 meaning=NCIT.C12903) )
        setattr(cls, "Suprasellar/Neurohypophyseal",
                PermissibleValue(text="Suprasellar/Neurohypophyseal",
                                 description="The area above or over the sella turcica.",
                                 meaning=NCIT.C42602) )
        setattr(cls, "Tarsal Bone",
                PermissibleValue(text="Tarsal Bone",
                                 description="Any one of the seven bones forming the instep of the foot.",
                                 meaning=NCIT.C12796) )
        setattr(cls, "Temporal Bone",
                PermissibleValue(text="Temporal Bone",
                                 description="A large irregular bone situated at the base and side of the skull, connected with the mandible via the temporomandibular joint. The temporal bone consiRMS of the squamous, tympanic and petrous parts. The petrous portion of the temporal bone contains the vestibulocochlear organ of the inner ear.",
                                 meaning=NCIT.C12797) )
        setattr(cls, "Temporal Cortex",
                PermissibleValue(text="Temporal Cortex",
                                 description="One of the cerebral lobes. It is located inferior to the frontal and parietal lobes and anterior to the occipital lobe.",
                                 meaning=NCIT.C12353) )
        setattr(cls, "Thoracic Vertebra",
                PermissibleValue(text="Thoracic Vertebra",
                                 description="One of 12 vertebrae in the human vertebral column. The thoracic vertebrae are situated between the seventh cervical vertebra down to the first lumbar vertebra.",
                                 meaning=NCIT.C12798) )
        setattr(cls, "Upper Airway",
                PermissibleValue(text="Upper Airway",
                                 description="The sinuses and those parts of the respiratory system above the trachea. It includes the nares, nasopharynx, oropharynx, larynx, vocal cords, glottis and upper trachea.",
                                 meaning=NCIT.C33839) )
        setattr(cls, "Upper Arm",
                PermissibleValue(text="Upper Arm",
                                 description="The portion of the upper extremity between the shoulder and the elbow. For clinical purposes this term is also used to refer to the whole superior limb.",
                                 meaning=NCIT.C32141) )
        setattr(cls, "Upper Extremity",
                PermissibleValue(text="Upper Extremity",
                                 description="The region of the body that includes the arm, the forearm, and hand.",
                                 meaning=NCIT.C12671) )
        setattr(cls, "Upper Limb",
                PermissibleValue(text="Upper Limb",
                                 description="The region of the body that includes the arm, the forearm, and hand.",
                                 meaning=NCIT.C12671) )
        setattr(cls, "Waldeyer's Ring",
                PermissibleValue(text="Waldeyer's Ring",
                                 description="The ring of lymphoid tissue located in the pharynx, consisting of the pharyngeal, tubal, palatine, and lingual tonsils.",
                                 meaning=NCIT.C73468) )
        setattr(cls, "Wrist Joint",
                PermissibleValue(text="Wrist Joint",
                                 description="A joint between the distal end of the radius and the proximal row of carpal bones.",
                                 meaning=NCIT.C33895) )
        setattr(cls, "Zygomatic Bone",
                PermissibleValue(text="Zygomatic Bone",
                                 description="The union at the zygomaticotemporal suture of the temporal process of the zygomatic one and zygomatic process of the temporal bone.",
                                 meaning=NCIT.C33897) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class LesionSizeEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="LesionSizeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class DiamTypeEnum(EnumDefinitionImpl):

    Transverse = PermissibleValue(text="Transverse",
                                           description="A measure of the transaxial dimension of the tumor.",
                                           meaning=NCIT.C182199)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="DiamTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Cranial-Caudal",
                PermissibleValue(text="Cranial-Caudal",
                                 description="A measure of the craniocaudal dimension of the tumor.",
                                 meaning=NCIT.C182395) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class LesionVolumeEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="LesionVolumeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "<200 mL",
                PermissibleValue(text="<200 mL",
                                 description="A finding of a tumor volume that is less than 200 milliters.",
                                 meaning=NCIT.C175000) )
        setattr(cls, ">=200 mL",
                PermissibleValue(text=">=200 mL",
                                 description="A finding of a tumor volume that is equal to or greater than 200 milliters.",
                                 meaning=NCIT.C175001) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class DepthEnum(EnumDefinitionImpl):

    Superficial = PermissibleValue(text="Superficial",
                                             description="Of little substance or significance; involving only a surface.",
                                             meaning=NCIT.C25239)
    Deep = PermissibleValue(text="Deep",
                               description="Extending relatively far inward.",
                               meaning=NCIT.C25240)
    Surface = PermissibleValue(text="Surface",
                                     description="The extended two-dimensional outer boundary of a three-dimensional object.",
                                     meaning=NCIT.C25245)
    Cortical = PermissibleValue(text="Cortical",
                                       description="The dense or compact outer layer of tissue that covers the bone.",
                                       meaning=NCIT.C52714)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="DepthEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Intra-Medullary",
                PermissibleValue(text="Intra-Medullary",
                                 description="Occurring in, or located within the spinal cord or the marrow space of a bone.",
                                 meaning=NCIT.C96266) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class LesionBulkyEnum(EnumDefinitionImpl):

    Yes = PermissibleValue(text="Yes",
                             description="The affirmative response to a question.",
                             meaning=NCIT.C49488)
    No = PermissibleValue(text="No",
                           description="The non-affirmative response to a question.",
                           meaning=NCIT.C49487)

    _defn = EnumDefinition(
        name="LesionBulkyEnum",
    )

class LateralityEnum(EnumDefinitionImpl):

    Left = PermissibleValue(text="Left",
                               description="A finding indicating the tumor location is on the left side of the specimen.",
                               meaning=NCIT.C160200)
    Right = PermissibleValue(text="Right",
                                 description="A finding indicating the tumor location is on the right side of the specimen.",
                                 meaning=NCIT.C160199)
    Midline = PermissibleValue(text="Midline",
                                     description="A finding indicating the tumor location is on the midline of the specimen.",
                                     meaning=NCIT.C162614)

    _defn = EnumDefinition(
        name="LateralityEnum",
    )

class InvasivenessEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="InvasivenessEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class ExtensionSiteEnum(EnumDefinitionImpl):

    Acetabulum = PermissibleValue(text="Acetabulum",
                                           description="Two cup shaped areas, one each on the lateral side of the lower pelvis that house the head of the femur to form the ball and socket joint of the hip.",
                                           meaning=NCIT.C32042)
    Ankle = PermissibleValue(text="Ankle",
                                 description="A gliding joint between the distal ends of the tibia and fibula and the proximal end of the talus.",
                                 meaning=NCIT.C32078)
    Axilla = PermissibleValue(text="Axilla",
                                   description="The underside concavity where the arm and the shoulder are joined.",
                                   meaning=NCIT.C12674)
    Bone = PermissibleValue(text="Bone",
                               description="Connective tissue that forms the skeletal components of the body.",
                               meaning=NCIT.C12366)
    Buttock = PermissibleValue(text="Buttock",
                                     description="Either of the fleshy mounds in the rear pelvic area of the human body formed by the gluteal muscles.",
                                     meaning=NCIT.C89806)
    Calcaneum = PermissibleValue(text="Calcaneum",
                                         description="The irregular and largest tarsal bone that forms the heel.",
                                         meaning=NCIT.C32250)
    Clavicle = PermissibleValue(text="Clavicle",
                                       description="One of a pair of bones linking the scapula and the sternum. The clavicle is part of the pectoral girdle.",
                                       meaning=NCIT.C12695)
    Cranium = PermissibleValue(text="Cranium",
                                     description="The bones that form the head, made up of the bones of the braincase and face.",
                                     meaning=NCIT.C12789)
    Dermis = PermissibleValue(text="Dermis",
                                   description="The inner layer of the two main layers of the skin. The dermis has connective tissue, blood vessels, oil and sweat glands, nerves, hair follicles, and other structures. It is made up of a thin upper layer called the papillary dermis, and a thick lower layer called the reticular dermis.",
                                   meaning=NCIT.C12701)
    Elbow = PermissibleValue(text="Elbow",
                                 description="A type of hinge joint located between the forearm and upper arm.",
                                 meaning=NCIT.C32497)
    Face = PermissibleValue(text="Face",
                               description="The anterior portion of the head extending from the forehead to the chin and ear to ear. The facial structures contain the eyes, nose and mouth, cheeks and jaws.",
                               meaning=NCIT.C13071)
    Femur = PermissibleValue(text="Femur",
                                 description="The upper leg bone positioned between the pelvis and the knee.",
                                 meaning=NCIT.C12717)
    Fibula = PermissibleValue(text="Fibula",
                                   description="The small, lateral calf bone extending from the knee to the ankle.",
                                   meaning=NCIT.C12718)
    Finger = PermissibleValue(text="Finger",
                                   description="Any of the digits of the hand.",
                                   meaning=NCIT.C32608)
    Foot = PermissibleValue(text="Foot",
                               description="The structure found below the ankle joint required for locomotion.",
                               meaning=NCIT.C32622)
    Forearm = PermissibleValue(text="Forearm",
                                     description="The structure on the upper limb, between the elbow and the wrist.",
                                     meaning=NCIT.C32628)
    Hand = PermissibleValue(text="Hand",
                               description="The distal portion of the upper extremity. It consists of the carpus, metacarpus, and digits.",
                               meaning=NCIT.C32712)
    Hypodermis = PermissibleValue(text="Hypodermis",
                                           description="A tissue sample that contains the epidermis, dermis, and subcutaneous adipose tissue.",
                                           meaning=NCIT.C92441)
    Humerus = PermissibleValue(text="Humerus",
                                     description="The upper arm bone between the shoulder and elbow.",
                                     meaning=NCIT.C12731)
    Intraspinal = PermissibleValue(text="Intraspinal",
                                             description="Within the spine.",
                                             meaning=NCIT.C96908)
    Ischium = PermissibleValue(text="Ischium",
                                     description="The most posterior and ventral bone making up the pelvis.",
                                     meaning=NCIT.C32884)
    Kidney = PermissibleValue(text="Kidney",
                                   description="One of the two bean-shaped organs located on each side of the spine in the retroperitoneum. The right kidney is located below the liver and the left kidney below the diaphragm. The kidneys filter and secret the metabolic products and minerals from the blood, thus maintaining the homeostasis. On the superior pole of each kidney there is an adrenal gland. Each kidney and adrenal gland is surrounded by fat.",
                                   meaning=NCIT.C12415)
    Knee = PermissibleValue(text="Knee",
                               description="A joint connecting the lower part of the femur with the upper part of the tibia. The lower part of the femur and the upper part of the tibia are attached to each other by ligaments. Other structures of the knee joint include the upper part of the fibula, located below and parallel to the tibia, and the patella which moves as the knee bends.",
                               meaning=NCIT.C32898)
    Leg = PermissibleValue(text="Leg",
                             description="One of the two lower extremities in humans used for locomotion and support.",
                             meaning=NCIT.C32974)
    Mandible = PermissibleValue(text="Mandible",
                                       description="The lower jaw bone holding the lower teeth.",
                                       meaning=NCIT.C12290)
    Maxilla = PermissibleValue(text="Maxilla",
                                     description="The upper jawbone in vertebrates; it is fused to the cranium.",
                                     meaning=NCIT.C26470)
    Metacarpus = PermissibleValue(text="Metacarpus",
                                           description="Any of the five bones between the wrist and the fingers that form the skeleton of the palm.",
                                           meaning=NCIT.C12751)
    Metatarsus = PermissibleValue(text="Metatarsus",
                                           description="A bone belonging to the middle part of the foot located between toes and ankle. There are 5 metatarsal bones and they are numbered from the medial side.",
                                           meaning=NCIT.C12752)
    Muscle = PermissibleValue(text="Muscle",
                                   description="One of the contractile organs of the body.",
                                   meaning=NCIT.C13056)
    Neck = PermissibleValue(text="Neck",
                               description="The region that connects the head to the rest of the body.",
                               meaning=NCIT.C1306)
    Pelvis = PermissibleValue(text="Pelvis",
                                   description="The bony, basin-shaped structure formed by the hipbones and the base of the backbone supporting the lower limbs in humans.",
                                   meaning=NCIT.C12767)
    Retroperitoneal = PermissibleValue(text="Retroperitoneal",
                                                     description="The back of the abdomen where the kidneys lie and the great blood vessels run.",
                                                     meaning=NCIT.C28256)
    Rib = PermissibleValue(text="Rib",
                             description="Any one of the paired bones, 12 on either side, extending from the thoracic vertebrae toward the median line on the ventral aspect of the trunk. The long curved bones which form the rib cage. Generally, ribs 1 to 7 are connected to the sternum by their costal cartilages and are called true ribs, whereas ribs 8 to 12 are termed false ribs.",
                             meaning=NCIT.C12782)
    Scalp = PermissibleValue(text="Scalp",
                                 description="The skin which covers the top of the head and which is usually covered by hair.",
                                 meaning=NCIT.C89807)
    Scapula = PermissibleValue(text="Scapula",
                                     description="The flat triangle-shaped bone that connects the humerus with the clavicle in the back of the shoulder.",
                                     meaning=NCIT.C12783)
    Shoulder = PermissibleValue(text="Shoulder",
                                       description="The region of the body between the neck and the upper arm.",
                                       meaning=NCIT.C25203)
    Sternum = PermissibleValue(text="Sternum",
                                     description="The long, flat bone connecting with the cartilages of the first seven ribs and the clavicle.",
                                     meaning=NCIT.C12793)
    Talus = PermissibleValue(text="Talus",
                                 description="The bone of the foot that connects with the tibia and fibula to form the ankle joint.",
                                 meaning=NCIT.C52799)
    Thigh = PermissibleValue(text="Thigh",
                                 description="A part of the lower limb, located between hip and knee.",
                                 meaning=NCIT.C33763)
    Tibia = PermissibleValue(text="Tibia",
                                 description="A bone located between the femur and the tarsus, being part of the lower leg.",
                                 meaning=NCIT.C12800)
    Toe = PermissibleValue(text="Toe",
                             description="One of the terminal digits of the foot.",
                             meaning=NCIT.C33788)
    Ulna = PermissibleValue(text="Ulna",
                               description="One of the bones that comprise the forearm. The largest aspect articulates with the humerus at the elbow joint and the smallest portion of the ulna articulates with the carpal bones in the wrist.",
                               meaning=NCIT.C12809)
    Wrist = PermissibleValue(text="Wrist",
                                 description="A joint between the distal end of the radius and the proximal row of carpal bones.",
                                 meaning=NCIT.C33894)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="ExtensionSiteEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Abdominal Wall",
                PermissibleValue(text="Abdominal Wall",
                                 description="The tissues that surround the organs that are present within the abdominal cavity. The abdominal wall tissue is composed of layers of fat, parietal peritoneum, fascia, and muscles.",
                                 meaning=NCIT.C28256) )
        setattr(cls, "Adjacent Organ",
                PermissibleValue(text="Adjacent Organ",
                                 description="An organ that is next to an organ of interest.",
                                 meaning=NCIT.C180347) )
        setattr(cls, "Carpal Bone",
                PermissibleValue(text="Carpal Bone",
                                 description="Any of the small bones of the wrist joint, located between the radius and the ulna and the metacarpus.",
                                 meaning=NCIT.C12688) )
        setattr(cls, "Cervical Vertebra",
                PermissibleValue(text="Cervical Vertebra",
                                 description="Any one of the seven vertebrae that start with C1, connecting the skull to the spine, and ends with C7, which joins the cervical with the thoracic spine.",
                                 meaning=NCIT.C12693) )
        setattr(cls, "Chest Wall",
                PermissibleValue(text="Chest Wall",
                                 description="The total system of structures outside the lungs that move as a part of breathing; it includes all structures from the skin to the parietal pleura.",
                                 meaning=NCIT.C62484) )
        setattr(cls, "Hip/Inguinal Region",
                PermissibleValue(text="Hip/Inguinal Region",
                                 description="The lateral prominence of the pelvis from the waist to the thigh.",
                                 meaning=NCIT.C64193) )
        setattr(cls, "Intra-abdominal",
                PermissibleValue(text="Intra-abdominal",
                                 description="The lower region of the anterior abdominal wall located laterally to the pubic region.",
                                 meaning=NCIT.C12726) )
        setattr(cls, "Lumbar Vertebra",
                PermissibleValue(text="Lumbar Vertebra",
                                 description="One of the five bones situated between the thoracic vertebrae and the sacrum in the lower part of the spine.",
                                 meaning=NCIT.C12744) )
        setattr(cls, "Radius Bone",
                PermissibleValue(text="Radius Bone",
                                 description="The long bone of the forearm that extends from the lateral aspect of the elbow to the thumb-side of the wrist.",
                                 meaning=NCIT.C12777) )
        setattr(cls, "Sacral Region",
                PermissibleValue(text="Sacral Region",
                                 description="The triangular bone, made up of 5 fused bones of the spine, located in the lower area of the spine between the fifth lumbar vertebra and the coccyx.",
                                 meaning=NCIT.C33508) )
        setattr(cls, "Thoracic Vertebra",
                PermissibleValue(text="Thoracic Vertebra",
                                 description="One of 12 vertebrae in the human vertebral column. The thoracic vertebrae are situated between the seventh cervical vertebra down to the first lumbar vertebra.",
                                 meaning=NCIT.C12798) )
        setattr(cls, "Upper Arm",
                PermissibleValue(text="Upper Arm",
                                 description="The portion of the upper extremity between the shoulder and the elbow. For clinical purposes this term is also used to refer to the whole superior limb.",
                                 meaning=NCIT.C32141) )
        setattr(cls, "Vasculo-Nervous",
                PermissibleValue(text="Vasculo-Nervous",
                                 description="A body structure consisting of nerves traveling together with arteries, veins, and/or lymphatics.",
                                 meaning=NCIT.C74603) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class LesionResponseEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="LesionResponseEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Complete Response",
                PermissibleValue(text="Complete Response",
                                 description="The disappearance of all signs of cancer in response to treatment.",
                                 meaning=NCIT.C4870) )
        setattr(cls, "Complete Response Unconfirmed",
                PermissibleValue(text="Complete Response Unconfirmed",
                                 description="An indication that a finding of complete response to treatment has not been confirmed.",
                                 meaning=NCIT.C165198) )
        setattr(cls, "Partial Response",
                PermissibleValue(text="Partial Response",
                                 description="A finding indicating that there is a decrease in the size and the extent of tissue involvement by a malignant tumor in a patient.",
                                 meaning=NCIT.C18058) )
        setattr(cls, "Stable Disease",
                PermissibleValue(text="Stable Disease",
                                 description="Cancer that is neither decreasing nor increasing in extent or severity.",
                                 meaning=NCIT.C18213) )
        setattr(cls, "Progressive Disease",
                PermissibleValue(text="Progressive Disease",
                                 description="A clinical, pathologic, and/or molecular finding indicating that the course of a disease is worsening in terms of extent or severity.",
                                 meaning=NCIT.C35571) )

class NodalSiteEnum(EnumDefinitionImpl):

    Cervix = PermissibleValue(text="Cervix",
                                   description="The lower part of the uterus occupying the region between the isthmus of the uterus and the vagina. It is divided into supravaginal and vaginal portions.",
                                   meaning=NCIT.C12311)
    Mediastinum = PermissibleValue(text="Mediastinum",
                                             description="A group of organs surrounded by loose connective tissue, separating the two pleural sacs, between the sternum anteriorly and the vertebral column posteriorly as well as from the thoracic inlet superiorly to the diaphragm inferiorly. The mediastinum contains the heart and pericardium, the bases of the great vessels, the trachea and bronchi, esophagus, thymus, lymph nodes, thoracic duct, phrenic and vagus nerves, and other structures and tissues.",
                                             meaning=NCIT.C12748)
    Omentum = PermissibleValue(text="Omentum",
                                     description="A fold of peritoneum originating at the stomach and supporting the viscera.",
                                     meaning=NCIT.C33209)
    Pelvis = PermissibleValue(text="Pelvis",
                                   description="The bony, basin-shaped structure formed by the hipbones and the base of the backbone supporting the lower limbs in humans.",
                                   meaning=NCIT.C12767)
    Retroperitoneum = PermissibleValue(text="Retroperitoneum",
                                                     description="The back of the abdomen where the kidneys lie and the great blood vessels run.",
                                                     meaning=NCIT.C28256)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="NodalSiteEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class NodalDeterminationEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="NodalDeterminationEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class NodalDeterminationSourceEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="NodalDeterminationSourceEnum",
    )

class NecrosisEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="NecrosisEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class SiteWithinBoneEnum(EnumDefinitionImpl):

    Distal = PermissibleValue(text="Distal",
                                   description="Situated farthest from a point of attachment or origin, as of a limb or bone; or directed away from the midline of the body.",
                                   meaning=NCIT.C25237)
    Proximal = PermissibleValue(text="Proximal",
                                       description="Situated nearest to a point of attachment or origin.",
                                       meaning=NCIT.C25236)
    Epiphysis = PermissibleValue(text="Epiphysis",
                                         description="The shaft of a long bone, located between the two epiphyses; it is cylindrical in shape, with walls of compact bone enclosing a central marrow cavity.",
                                         meaning=NCIT.C32460)
    Metaphysis = PermissibleValue(text="Metaphysis",
                                           description="An area of a long bone located at the junction of the diaphysis and epiphysis, which harbors the epiphyseal plate in immature bones.",
                                           meaning=NCIT.C52723)
    Diaphysis = PermissibleValue(text="Diaphysis",
                                         description="The round end of the long bones.",
                                         meaning=NCIT.C32529)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="SiteWithinBoneEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class EExtensionSiteEnum(EnumDefinitionImpl):

    Heart = PermissibleValue(text="Heart",
                                 description="A hollow organ located slightly to the left of the middle portion of the chest. It is composed of muscle and it is divided by a septum into two sides: the right side which receives de-oxygenated blood from the body and the left side which sends newly oxygenated blood to the body. Each side is composed of two chambers: the atrium (receiving blood) and ventricle (ejecting blood).",
                                 meaning=NCIT.C12727)
    Lungs = PermissibleValue(text="Lungs",
                                 description="One of a pair of viscera occupying the pulmonary cavities of the thorax, the organs of respiration in which aeration of the blood takes place. As a rule, the right lung is slightly larger than the left and is divided into three lobes (an upper, a middle, and a lower or basal), while the left has two lobes (an upper and a lower or basal). Each lung is irregularly conical in shape, presenting a blunt upper extremity (the apex), a concave base following the curve of the diaphragm, an outer convex surface (costal surface), an inner or mediastinal surface (mediastinal surface), a thin and sharp anterior border, and a thick and rounded posterior border.",
                                 meaning=NCIT.C12468)
    Bone = PermissibleValue(text="Bone",
                               description="Connective tissue that forms the skeletal components of the body.",
                               meaning=NCIT.C12366)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)

    _defn = EnumDefinition(
        name="EExtensionSiteEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Chest Wall",
                PermissibleValue(text="Chest Wall",
                                 description="The total system of structures outside the lungs that move as a part of breathing; it includes all structures from the skin to the parietal pleura.",
                                 meaning=NCIT.C62484) )
        setattr(cls, "Soft Tissue",
                PermissibleValue(text="Soft Tissue",
                                 description="A general term comprising tissue that is not hardened or calcified; including muscle, fat, blood vessels, nerves, tendons, ligaments and fascia.",
                                 meaning=NCIT.C12471) )

class AbsentNotreportedPresentUnknownEnum(EnumDefinitionImpl):

    Present = PermissibleValue(text="Present",
                                     description="Being or existing in a specified place or at the specified time.",
                                     meaning=NCIT.C25626)
    Absent = PermissibleValue(text="Absent",
                                   description="Not existing in a specified place at a specified time.",
                                   meaning=NCIT.C48190)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="AbsentNotreportedPresentUnknownEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class AnaplasiaExtentEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AnaplasiaExtentEnum",
    )

class StageSystemEnum(EnumDefinitionImpl):

    COG = PermissibleValue(text="COG",
                             description="An NCI-supported clinical cooperative group formed by the merger of the four national pediatric cancer research organizations: the Children's Cancer Group, the Intergroup Rhabdomyosarcoma Study Group, the National Wilms Tumor Study Group, and the Pediatric Oncology Group. The primary objective of the organization is to conduct clinical trials of new therapies for childhood and adolescent cancer. COG develops and coordinates clinical trials conducted at the 238 member institutions that include cancer centers of all major universities and teaching hospitals throughout the U.S. and Canada, as well as sites in Europe and Australia. COG members include over 5000 cancer researchers.",
                             meaning=NCIT.C39353)
    FIGO = PermissibleValue(text="FIGO",
                               description="An international organization with a mission to promote the wellbeing of women and to raise the standards of practice in obstetrics and gynecology. They are the creator of staging criteria to describe the extent and spread of gynecologic malignancies.",
                               meaning=NCIT.C89808)
    AJCC = PermissibleValue(text="AJCC",
                               description="A group formed for the purpose of developing a system of clinical staging for cancer that is acceptable to the American medical profession and is compatible with other accepted classifications.",
                               meaning=NCIT.C39315)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="StageSystemEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Ann Arbor",
                PermissibleValue(text="Ann Arbor",
                                 description="The Ann Arbor system classifies lymphoma into four stages based on anatomic lymph nodal group involvement. Disease confined to one nodal group or location defines stage I. Disease limited to one side of the diaphragm, (the muscle separating the chest from the abdomen), defines stage II. Stage III patients have disease on both sides of the diaphragm and stage IV patients once again have disseminated disease. Consideration of involvement of the liver, spleen, and bone marrow are also considered in this system. Finally, the stage is subdivided into categories of A and B depending on the presence of symptoms of itching, weight loss, fever, and night sweats. Those having symptoms receive the designation "B" and have a worse prognosis.",
                                 meaning=NCIT.C54179) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class StageEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="StageEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "INSS, Stage 1",
                PermissibleValue(text="INSS, Stage 1",
                                 description="Localized tumor with complete gross excision, with or without microscopic residual disease; representative ipsilateral lymph nodes negative for tumor microscopically (i.e., nodes attached to and removed with the primary tumor may be positive).") )
        setattr(cls, "INSS, Stage 2A",
                PermissibleValue(text="INSS, Stage 2A",
                                 description="Localized tumor with incomplete gross excision; representative ipsilateral nonadherent lymph nodes negative for tumor microscopically.") )
        setattr(cls, "INSS, Stage 2B",
                PermissibleValue(text="INSS, Stage 2B",
                                 description="Localized tumor with or without complete gross excision, with ipsilateral nonadherent lymph nodes positive for tumor. Enlarged contralateral lymph nodes must be negative microscopically.") )
        setattr(cls, "INSS, Stage 3",
                PermissibleValue(text="INSS, Stage 3",
                                 description="Unresectable unilateral tumor infiltrating across the midline, with or without regional lymph node involvement; or localized unilateral tumor with contralateral regional lymph node involvement; or midline tumor with bilateral extension by infiltration (unresectable) or by lymph node involvement. The midline is defined as the vertebral column. Tumors originating on one side and crossing the midline must infiltrate to or beyond the opposite side of the vertebral column.") )
        setattr(cls, "INSS, Stage 4",
                PermissibleValue(text="INSS, Stage 4",
                                 description="Any primary tumor with dissemination to distant lymph nodes, bone, bone marrow, liver, skin, and/or other organs, except as defined for stage 4S.") )
        setattr(cls, "INSS, Stage 4S",
                PermissibleValue(text="INSS, Stage 4S",
                                 description="Localized primary tumor, as defined for stage 1, 2A, or 2B, with dissemination limited to skin, liver, and/or bone marrow (by definition limited to infants younger than 12 months). Marrow involvement should be minimal (i.e., <10% of total nucleated cells identified as malignant by bone biopsy or by bone marrow aspirate). More extensive bone marrow involvement would be considered stage 4 disease. The results of the MIBG scan, if performed, should be negative for disease in the bone marrow.") )
        setattr(cls, "FIGO, Stage 1",
                PermissibleValue(text="FIGO, Stage 1",
                                 description="A FIGO stage term that applies to gynecologic cancers. For cervical cancer, it refers to invasive cancer that is confined to the cervix; for endometrial cancer, it refers to cancer confined to the corpus uteri with no or less than one-half myometrial invasion (IA) or invasion of one-half or more of the myometrium (IB).",
                                 meaning=NCIT.C96244) )
        setattr(cls, "FIGO, Stage 2",
                PermissibleValue(text="FIGO, Stage 2",
                                 description="A FIGO stage term that applies to gynecologic cancers. For cervical cancer, it refers to cancer that invades beyond the cervix, but not to the pelvic wall or lower third of the vagina; for endometrial cancer, it refers to cancer that invades the stromal connective tissue of the cervix, but it does not extend beyond the uterus.",
                                 meaning=NCIT.C96252) )
        setattr(cls, "FIGO, Stage 3",
                PermissibleValue(text="FIGO, Stage 3",
                                 description="A FIGO stage term that applies to gynecologic cancers. For cervical cancer, it refers to cancer that extends to the pelvic wall, and/or involves the lower third of vagina, and/or causes hydronephrosis or non-functioning kidney; for endometrial cancer, FIGO stage III is subdivided into stages IIIA and IIIB; in FIGO stage IIIA, there is involvement of the serosa and/or the adnexa; for FIGO stage IIIB, there is vaginal or parametrial involvement.",
                                 meaning=NCIT.C96255) )
        setattr(cls, "FIGO, Stage 4",
                PermissibleValue(text="FIGO, Stage 4",
                                 description="A FIGO stage term that applies to gynecologic cancers. For cervical cancer, it refers to cancer that invades the mucosa of bladder or rectum, and/or extends beyond the true pelvis (FIGO stage IVA), or to cancer with distant metastases (FIGO stage IVB); for endometrial cancer, it refers to cancer that invades the bladder mucosa and/or the bowel mucosa (FIGO stage IVA), or to cancer with distant metastases (FIGO stage IVB).",
                                 meaning=NCIT.C96261) )
        setattr(cls, "COG, Stage 1",
                PermissibleValue(text="COG, Stage 1",
                                 description="Invasive cancer confined to the original anatomic site of growth without lymph node involvement.",
                                 meaning=NCIT.C27966) )
        setattr(cls, "COG, Stage 2",
                PermissibleValue(text="COG, Stage 2",
                                 description="Invasive cancer more extensive than stage I, usually involving local lymph nodes without spread to distant anatomic sites.",
                                 meaning=NCIT.C28054) )
        setattr(cls, "COG, Stage 3",
                PermissibleValue(text="COG, Stage 3",
                                 description="Locally advanced cancer that has spread to nearby organs but not to distant anatomic sites.",
                                 meaning=NCIT.C27970) )
        setattr(cls, "COG, Stage 4",
                PermissibleValue(text="COG, Stage 4",
                                 description="Cancer that has spread to distant anatomic sites beyond its original site of growth.",
                                 meaning=NCIT.C27971) )
        setattr(cls, "AJCC, Stage 0",
                PermissibleValue(text="AJCC, Stage 0",
                                 description="Stage 0 includes: pTis, N0, M0, S0. pTis: Intratubular germ cell neoplasia (carcinoma in situ). N0: regional lymph node metastasis. M0: No distant metastasis. S0: Marker study levels within normal limits. (AJCC 6th and 7th eds.)",
                                 meaning=NCIT.C4523) )
        setattr(cls, "AJCC, Stage 1",
                PermissibleValue(text="AJCC, Stage 1",
                                 description="Stage I includes: pT1-4, N0, M0, SX. pT1: Tumor limited to the testis and epididymis without vascular/lymphatic invasion; tumor may invade into the tunica albuginea but not the tunica vaginalis. pT2: Tumor limited to the testis and epididymis with vascular/lymphatic invasion, or tumor extending through the tunica albuginea with involvement of the tunica vaginalis. pT3: Tumor invades the spermatic cord with or without vascular/lymphatic invasion. pT4: Tumor invades the scrotum with or without vascular/lymphatic invasion. N0: No regional lymph node metastasis. M0: No distant metastasis. SX: Marker studies not available or not performed. (AJCC 6th and 7th eds.)",
                                 meaning=NCIT.C7901) )
        setattr(cls, "AJCC, Stage 1A",
                PermissibleValue(text="AJCC, Stage 1A",
                                 description="Stage IA includes: pT1, N0, M0, S0. pT1: Tumor limited to the testis and epididymis without vascular/lymphatic invasion; tumor may invade into the tunica albuginea but not the tunica vaginalis. N0: No regional lymph node metastasis. M0: No distant metastasis. S0: Marker study levels within normal limits. (AJCC 6th and 7th eds.)",
                                 meaning=NCIT.C6361) )
        setattr(cls, "AJCC, Stage 1B",
                PermissibleValue(text="AJCC, Stage 1B",
                                 description="Stage IB includes: (pT2, N0, M0, S0); (pT3, N0, M0, S0); (pT4, N0, M0, S0). pT2: Tumor limited to the testis and epididymis with vascular/lymphatic invasion, or tumor extending through the tunica albuginea with involvement of the tunica vaginalis. pT3: Tumor invades the spermatic cord with or without vascular/lymphatic invasion. pT4: Tumor invades the scrotum with or without vascular/lymphatic invasion. N0: No regional lymph node metastasis. M0: No distant metastasis. S0: Marker study levels within normal limits. (AJCC 6th and 7th eds.)",
                                 meaning=NCIT.C6362) )
        setattr(cls, "AJCC, Stage 1s",
                PermissibleValue(text="AJCC, Stage 1s",
                                 description="Stage IS includes: Any pT/TX, N0, M0, S1-3. pTX: Primary tumor cannot be assessed. N0: No regional lymph node metastasis. M0: No distant metastasis. S1: LDH less than 1.5 x N (N indicates the upper limit of normal for the LDH assay) and hCG less than 5,000 and AFP less than 1,000. S2: LDH 1.5-10 x N or hCG 5,000-50,000 or AFP 1,000-10,000. S3: LDH more than 10 x N or hCG more than 50,000 or AFP more than 10,000. (AJCC 6th and 7th eds.)",
                                 meaning=NCIT.C6363) )
        setattr(cls, "AJCC, Stage 2",
                PermissibleValue(text="AJCC, Stage 2",
                                 description="Stage II includes: Any pT/TX, N1-3, M0, SX. pTX: Primary tumor cannot be assessed. N1: Metastasis with a lymph node mass 2 cm or less in greatest dimension; or multiple lymph nodes, none more than 2cm in greatest dimension. N2: Metastasis with a lymph node mass more than 2 cm but not more than 5 cm in greatest dimension; or multiple lymph nodes, any one mass greater than 2 cm but not more than 5 cm in greatest dimension. N3: Metastasis with a lymph node mass more than 5 cm in greatest dimension. M0: No distant metastasis. SX: Marker studies not available or not performed. (AJCC 6th and 7th eds.)",
                                 meaning=NCIT.C9073) )
        setattr(cls, "AJCC, Stage 2A",
                PermissibleValue(text="AJCC, Stage 2A",
                                 description="Stage IIA includes: (Any pT/TX, N1, M0, S0); (Any pT/TX, N1, M0, S1). TX: Testicular cancer in which the primary tumor cannot be assessed. N1: Testicular cancer with metastasis with a lymph node mass 2 cm or smaller in greatest dimension and less than or equal to five nodes positive, none larger than 2 cm in greatest dimension. M0: Testicular cancer without evidence of distant metastasis. S0: Marker study levels within normal limits. S1: LDH less than 1.5 x N and hCG (mlU/mL) less than 5,000 and AFP (ng/mL) less than 1,000. N indicates the upper limit of normal for the LDH assay. (AJCC 8th ed.)",
                                 meaning=NCIT.C6364) )
        setattr(cls, "AJCC, Stage 2B",
                PermissibleValue(text="AJCC, Stage 2B",
                                 description="Stage IIB includes: (Any pT/TX, N2, M0, S0); (Any pT/TX, N2, M0, S1). pTX: Primary tumor cannot be assessed. N2: Metastasis with a lymph node mass more than 2 cm but not more than 5 cm in greatest dimension; or multiple lymph nodes, any one mass greater than 2 cm but not more than 5 cm in greatest dimension. M0: No distant metastasis. S0: Marker study levels within normal limits. S1: LDH less than 1.5 x N (N indicates the upper limit of normal for the LDH assay) and hCG less than 5,000 and AFP less than 1,000. (AJCC 6th and 7th eds.)",
                                 meaning=NCIT.C6365) )
        setattr(cls, "AJCC, Stage 2C",
                PermissibleValue(text="AJCC, Stage 2C",
                                 description="Stage IIC includes: (Any pT/TX, N3, M0, S0); (Any pT/TX, N3, M0, S1). pTX: Primary tumor cannot be assessed. N3: Metastasis with a lymph node mass more than 5 cm in greatest dimension. M0: No distant metastasis. S0: Marker study levels within normal limits. S1: LDH less than 1.5 x N (N indicates the upper limit of normal for the LDH assay) and hCG less than 5,000 and AFP less than 1,000. (AJCC 6th and 7th eds.)",
                                 meaning=NCIT.C6366) )
        setattr(cls, "AJCC, Stage 3",
                PermissibleValue(text="AJCC, Stage 3",
                                 description="Stage III includes: Any pT/TX, Any N, M1, SX. M1: Distant metastasis. SX: Marker studies not available or not performed. (AJCC 6th and 7th eds.)",
                                 meaning=NCIT.C9074) )
        setattr(cls, "AJCC, Stage 3A",
                PermissibleValue(text="AJCC, Stage 3A",
                                 description="Stage IIIA includes: (Any pT/TX, Any N, M1a, S0); (Any pT/TX, Any N, M1a, S1). M1a: Non-regional nodal or pulmonary metastasis. S0: Marker study levels within normal limits. S1: LDH less than 1.5 x N (N indicates the upper limit of normal for the LDH assay) and hCG less than 5,000 and AFP less than 1,000. (AJCC 6th and 7th eds.)",
                                 meaning=NCIT.C6369) )
        setattr(cls, "AJCC, Stage 3B",
                PermissibleValue(text="AJCC, Stage 3B",
                                 description="Stage IIIB includes: (Any pT/TX, N1-3, M0, S2); (Any pT/TX, Any N, M1a, S2). N1: Metastasis with a lymph node mass 2 cm or less in greatest dimension; or multiple lymph nodes, none more than 2cm in greatest dimension. N2: Metastasis with a lymph node mass more than 2 cm but not more than 5 cm in greatest dimension; or multiple lymph nodes, any one mass greater than 2 cm but not more than 5 cm in greatest dimension. N3: Metastasis with a lymph node mass more than 5 cm in greatest dimension. M0: No distant metastasis. M1a: Non-regional nodal or pulmonary metastasis. S2: LDH 1.5-10 x N (N indicates the upper limit of normal for the LDH assay) or hCG 5,000-50,000 or AFP 1,000-10,000. (AJCC 6th and 7th eds.)",
                                 meaning=NCIT.C6368) )
        setattr(cls, "AJCC, Stage 3C",
                PermissibleValue(text="AJCC, Stage 3C",
                                 description="Stage IIIC includes: (Any pT/TX, N1-3, M0, S3); (Any pT/TX, Any N, M1a, S3); (Any pT/TX, Any N, M1b, Any S). N1: Metastasis with a lymph node mass 2 cm or less in greatest dimension; or multiple lymph nodes, none more than 2cm in greatest dimension. N2: Metastasis with a lymph node mass more than 2 cm but not more than 5 cm in greatest dimension; or multiple lymph nodes, any one mass greater than 2 cm but not more than 5 cm in greatest dimension. N3: Metastasis with a lymph node mass more than 5 cm in greatest dimension. M0: No distant metastasis. M1a: Non-regional nodal or pulmonary metastasis. M1b: Distant metastasis other than to non-regional lymph nodes and lung. S3: LDH more than 10 x N (N indicates the upper limit of normal for the LDH assay) or hCG more than 50,000 or AFP more than 10,000. (AJCC 6th and 7th eds.)",
                                 meaning=NCIT.C6367) )
        setattr(cls, "Evans, Stage 1",
                PermissibleValue(text="Evans, Stage 1",
                                 description="The tumor is completely resected.") )
        setattr(cls, "Evans, Stage 2",
                PermissibleValue(text="Evans, Stage 2",
                                 description="Microscopic residual tumor remains after resection.") )
        setattr(cls, "Evans, Stage 3",
                PermissibleValue(text="Evans, Stage 3",
                                 description="There are no distant metastases and at least one of the following is true: (1) the tumor is either unresectable or the tumor is resected with gross residual tumor; (2) there are positive extrahepatic lymph nodes.") )
        setattr(cls, "Evans, Stage 4",
                PermissibleValue(text="Evans, Stage 4",
                                 description="There is distant metastasis, regardless of the extent of liver involvement.") )
        setattr(cls, "INRGSS, Stage L1",
                PermissibleValue(text="INRGSS, Stage L1",
                                 description="Locoregional tumor without IDRFs") )
        setattr(cls, "INRGSS, Stage L2",
                PermissibleValue(text="INRGSS, Stage L2",
                                 description="Locoregional tumor with one or more IDRFs") )
        setattr(cls, "INRGSS, Stage M",
                PermissibleValue(text="INRGSS, Stage M",
                                 description="Distant metastatic disease (except Ms)") )
        setattr(cls, "INRGSS, Stage Ms",
                PermissibleValue(text="INRGSS, Stage Ms",
                                 description="INRG Stage L1 or L2 tumor with metastatic disease confined to skin and/or liver and/or bone marrow") )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class AnnArborModAbEnum(EnumDefinitionImpl):

    A = PermissibleValue(text="A",
                         description="An indication of whether a record includes A-symptom data based on the Ann Arbor lymphoma classification system guidelines.",
                         meaning=NCIT.C185483)
    B = PermissibleValue(text="B",
                         description="A indication of whether a record includes B-symptom data based on the Ann Arbor lymphoma classification system guidelines.",
                         meaning=NCIT.C177585)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="AnnArborModAbEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class TnmFindingEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="TnmFindingEnum",
    )

class IrsGroupEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="IrsGroupEnum",
    )

class HistAssessmentReviewEnum(EnumDefinitionImpl):

    Institutional = PermissibleValue(text="Institutional",
                                                 description="An established society, corporation, foundation or other organization founded and united for a specific purpose, e.g. for health-related research; also used to refer to a building or buildings occupied or used by such organization.",
                                                 meaning=NCIT.C41206)
    Central = PermissibleValue(text="Central",
                                     description="Clinical trial conducted according to a single protocol but at more than one site and, therefore, carried out by more than one investigator.",
                                     meaning=NCIT.C16104)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="HistAssessmentReviewEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class HistologyEnum(EnumDefinitionImpl):

    Choriocarcinoma = PermissibleValue(text="Choriocarcinoma",
                                                     description="An aggressive malignant tumor arising from trophoblastic cells. The vast majority of cases arise in the uterus and represent gestational choriocarcinomas that derive from placental trophoblastic cells. Approximately half of the cases develop from a complete hydatidiform mole. A minority of cases arise in the testis or the ovaries. There is often marked elevation of human chorionic gonadotropin (hCG) in the blood. Choriocarcinomas disseminate rapidly through the hematogenous route; the lungs are most frequently affected.",
                                                     meaning=NCIT.C2948)
    Gonadoblastoma = PermissibleValue(text="Gonadoblastoma",
                                                   description="A mixed germ cell/sex cord-stromal tumor characterized by the presence of large germ cells which resemble seminoma cells and small cells which resemble Sertoli or granulosa cells. It occurs in the testis and the ovary and is identified in children and adults. It is often associated with gonadal dysgenesis and abnormal karyotype.",
                                                   meaning=NCIT.C3754)
    Seminoma = PermissibleValue(text="Seminoma",
                                       description="A radiosensitive malignant germ cell tumor found in the testis (especially undescended), and extragonadal sites (anterior mediastinum and pineal gland). It is characterized by the presence of uniform cells with clear or dense cytoplasm which contains glycogen, and by a large nucleus which contains one or more nucleoli. The neoplastic germ cells form aggregates separated by fibrous septa. The fibrous septa contain chronic inflammatory cells, mainly lymphocytes.",
                                       meaning=NCIT.C9309)
    Dysgerminoma = PermissibleValue(text="Dysgerminoma",
                                               description="A malignant germ cell tumor characterized by the presence of a monotonous primitive germ cell population. The neoplastic cells form aggregates and have an abundant pale cytoplasm and uniform nuclei. The aggregates of the germ cells are separated by fibrous septa which contain inflammatory cells, mostly T-lymphocytes. It arises primarily in the ovaries, but can occur both primarily and secondarily at other sites, particularly the central nervous system. It responds to chemotherapy and radiotherapy. Its prognosis is related to the tumor stage.",
                                               meaning=NCIT.C2996)
    Germinoma = PermissibleValue(text="Germinoma",
                                         description="A malignant germ cell tumor arising in the central nervous system. It is characterized by the presence of primitive, large malignant germ cells and lymphocytes.",
                                         meaning=NCIT.C3753)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="HistologyEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Seminoma/Dysgerminoma/Germinoma",
                PermissibleValue(text="Seminoma/Dysgerminoma/Germinoma",
                                 description="A term that refers to germinoma, seminoma, or dysgerminoma.",
                                 meaning=NCIT.C121618) )
        setattr(cls, "Embryonal Carcinoma",
                PermissibleValue(text="Embryonal Carcinoma",
                                 description="A non-seminomatous malignant germ cell tumor characterized by the presence of large germ cells with abundant cytoplasm resembling epithelial cells, geographic necrosis, high mitotic activity, and pseudoglandular and pseudopapillary structures formation. It can arise from the testis, ovary, and extragonadal sites (central nervous system and mediastinum).",
                                 meaning=NCIT.C3752) )
        setattr(cls, "Yolk Sac Tumor",
                PermissibleValue(text="Yolk Sac Tumor",
                                 description="A non-seminomatous malignant germ cell tumor composed of primitive germ cells. It is the most common malignant germ cell tumor in the pediatric population. It occurs in the infant testis, ovary, sacrococcygeal region, vagina, uterus, prostate, abdomen, liver, retroperitoneum, thorax, and pineal/third ventricle. The tumor mimics the yolk sac of the embryo and produces alpha-fetoprotein (AFP). Treatment includes: surgical resection, radiation, and chemotherapy. This tumor is very responsive to chemotherapy regimens that include cisplatinum.",
                                 meaning=NCIT.C3011) )
        setattr(cls, "Mature Teratoma",
                PermissibleValue(text="Mature Teratoma",
                                 description="A teratoma which may be cystic; it is composed entirely of well differentiated, adult-type mature tissues, without evidence of fetal-type immature tissues (grade 0 teratoma).",
                                 meaning=NCIT.C9015) )
        setattr(cls, "Immature Teratoma",
                PermissibleValue(text="Immature Teratoma",
                                 description="A teratoma characterized by the presence of an extensive component of immature, fetal-type tissues.",
                                 meaning=NCIT.C4286) )
        setattr(cls, "Somatic Malignancy",
                PermissibleValue(text="Somatic Malignancy",
                                 description="A teratoma which is characterized by morphologic transformation to malignancy and an aggressive clinical course. The malignant component most often is sarcomatous or carcinomatous.",
                                 meaning=NCIT.C4289) )
        setattr(cls, "Necrotic Tumor",
                PermissibleValue(text="Necrotic Tumor",
                                 description="Necrotic Neoplasm",
                                 meaning=NCIT.C36029) )
        setattr(cls, "Teratoma, NOS",
                PermissibleValue(text="Teratoma, NOS",
                                 description="A non-seminomatous germ cell tumor characterized by the presence of various tissues which correspond to the different germinal layers (endoderm, mesoderm, and ectoderm). It occurs in the testis, ovary, and extragonadal sites including central nervous system, mediastinum, lung, and stomach. According to the level of differentiation of the tissues which comprise the tumor, teratomas are classified as benign (grade 0 or 1), immature (grade 2), and malignant (grade 3). Grade 0 teratomas contain only mature elements; grade 1 teratomas have a limited degree of immaturity; grade 2 teratomas have a more extensive degree of immaturity; grade 3 teratomas are composed exclusively of immature tissues. The prognosis depends on patient age, tumor size and grade, and stage.",
                                 meaning=NCIT.C3403) )
        setattr(cls, "Mixed Germ Cell Tumor",
                PermissibleValue(text="Mixed Germ Cell Tumor",
                                 description="A malignant germ cell tumor characterized by the presence of at least two different germ cell tumor components. The different germ cell tumor components include choriocarcinoma, embryonal carcinoma, yolk sac tumor, teratoma, and seminoma. It occurs in the ovary, testis, and extragonadal sites including central nervous system and mediastinum.",
                                 meaning=NCIT.C4290) )
        setattr(cls, "Malignant Teratoma",
                PermissibleValue(text="Malignant Teratoma",
                                 description="A teratoma composed exclusively of immature tissues.",
                                 meaning=NCIT.C4287) )
        setattr(cls, "Undifferentiated Ewing Tumor",
                PermissibleValue(text="Undifferentiated Ewing Tumor",
                                 description="An undifferentiated soft tissue sarcoma characterized by the presence of uniform round or ovoid malignant cells with a high nuclear to cytoplasmic ratio.",
                                 meaning=NCIT.C121799) )
        setattr(cls, "Neuro-differentiated Ewing Tumor",
                PermissibleValue(text="Neuro-differentiated Ewing Tumor",
                                 description="A small round cell tumor with neural differentiation arising from the soft tissues or bone.",
                                 meaning=NCIT.C9341) )
        setattr(cls, "Large Cell Ewing Tumor",
                PermissibleValue(text="Large Cell Ewing Tumor",
                                 description="Ewing sarcoma characterized by the presence of large malignant cells with prominent nucleoli and irregular contours.",
                                 meaning=NCIT.C174456) )
        setattr(cls, "Hodgkin Lymphoma, NOS",
                PermissibleValue(text="Hodgkin Lymphoma, NOS",
                                 description="A lymphoma, previously known as Hodgkin's disease, characterized by the presence of large tumor cells in an abundant admixture of nonneoplastic cells. There are two distinct subtypes: nodular lymphocyte predominant Hodgkin lymphoma and classical Hodgkin lymphoma. Hodgkin lymphoma involves primarily lymph nodes.",
                                 meaning=NCIT.C9357) )
        setattr(cls, "Hodgkin Lymphoma, Lymphocyte-Rich",
                PermissibleValue(text="Hodgkin Lymphoma, Lymphocyte-Rich",
                                 description="A subtype of classic Hodgkin lymphoma with scattered Hodgkin and Reed-Sternberg cells and a nodular or less often diffuse cellular background consisting of small lymphocytes and with an absence of neutrophils and eosinophils. (WHO, 2008)",
                                 meaning=NCIT.C6913) )
        setattr(cls, "Hodgkin lymphoma, Mixed Cellularity, NOS",
                PermissibleValue(text="Hodgkin lymphoma, Mixed Cellularity, NOS",
                                 description="A subtype of classic Hodgkin lymphoma with scattered Reed-Sternberg and Hodgkin cells in a diffuse or vaguely nodular mixed inflammatory background without nodular sclerosing fibrosis. (WHO, 2008)",
                                 meaning=NCIT.C3517) )
        setattr(cls, "Hodgkin Lymphoma, Lymphocyte Depletion, NOS",
                PermissibleValue(text="Hodgkin Lymphoma, Lymphocyte Depletion, NOS",
                                 description="A diffuse subtype of classic Hodgkin lymphoma which is rich in Hodgkin and Reed-Sternberg cells and/or depleted in non-neoplastic lymphocytes. (WHO, 2008)",
                                 meaning=NCIT.C9283) )
        setattr(cls, "Hodgkin Lymphoma, Nodular Lymphocyte Predominance",
                PermissibleValue(text="Hodgkin Lymphoma, Nodular Lymphocyte Predominance",
                                 description="A monoclonal B-cell neoplasm characterized by a nodular, or a nodular and diffuse proliferation of scattered large neoplastic cells known as popcorn or lymphocyte predominant cells (LP cells)- formerly called L&H cells for lymphocytic and/or histiocytic Reed-Sternberg cell variants. The LP cells lack CD15 and CD30 in nearly all instances. Patients are predominantly male, frequently in the 30-50 year age group. Most patients present with limited stage disease (localized peripheral lymphadenopathy, stage I or II). (WHO 2008)",
                                 meaning=NCIT.C7258) )
        setattr(cls, "Hodgkin Lymphoma, Nodular Sclerosis, NOS",
                PermissibleValue(text="Hodgkin Lymphoma, Nodular Sclerosis, NOS",
                                 description="A subtype of classic Hodgkin lymphoma characterized by collagen bands that surround at least one nodule, and Hodgkin and Reed-Sternberg cells with lacunar type morphology. (WHO, 2008)",
                                 meaning=NCIT.C3518) )
        setattr(cls, "Conventional Osteosarcoma",
                PermissibleValue(text="Conventional Osteosarcoma",
                                 description="A high grade malignant bone-forming mesenchymal neoplasm producing osteoid. The tumor arises from the medullary portion of the bone. It affects the long bones and most commonly, the distal femur, proximal tibia, and proximal humerus. Pain with or without a palpable mass is the most common clinical presentation. It usually has an aggressive growth and may metastasize through the hematogenous route. The lung is the most frequent site of metastasis.",
                                 meaning=NCIT.C35870) )
        setattr(cls, "Surface Osteosarcoma",
                PermissibleValue(text="Surface Osteosarcoma",
                                 description="A usually aggressive malignant bone-forming mesenchymal neoplasm arising from the surface of the bone.",
                                 meaning=NCIT.C7134) )
        setattr(cls, "Osteoblastic Osteosarcoma",
                PermissibleValue(text="Osteoblastic Osteosarcoma",
                                 description="A conventional osteosarcoma characterized by the predominance of osteoid matrix.",
                                 meaning=NCIT.C53953) )
        setattr(cls, "Chondroblastic Osteosarcoma",
                PermissibleValue(text="Chondroblastic Osteosarcoma",
                                 description="An osteosarcoma characterised by the presence of atypical cartilage of variable cellularity. It may or may not be associated with the presence of myxoid areas or focal bone formation.",
                                 meaning=NCIT.C4021) )
        setattr(cls, "Fibroblastic Osteosarcoma",
                PermissibleValue(text="Fibroblastic Osteosarcoma",
                                 description="A conventional osteosarcoma characterized by the presence of spindle shaped cells.",
                                 meaning=NCIT.C4020) )
        setattr(cls, "Periosteal Osteosarcoma",
                PermissibleValue(text="Periosteal Osteosarcoma",
                                 description="An intermediate grade malignant bone-forming mesenchymal neoplasm with chondroblastic differentiation. It arises from the surface of the bone and affects the diaphysis or diaphyseal- metaphyseal portion of the long bones. A painless mass or swelling is the most common clinical sign. It is associated with a better prognosis than conventional osteosarcoma.",
                                 meaning=NCIT.C8970) )
        setattr(cls, "Parosteal Osteosarcoma",
                PermissibleValue(text="Parosteal Osteosarcoma",
                                 description="A low grade malignant bone-forming mesenchymal neoplasm arising from the surface of the bone. It usually affects the distal posterior femur, the proximal tibia, and proximal humerus. Painless swelling is the usual clinical sign. Most patients are young adults and the prognosis is usually excellent.",
                                 meaning=NCIT.C8969) )
        setattr(cls, "Giant Cell Rich Osteosarcoma",
                PermissibleValue(text="Giant Cell Rich Osteosarcoma",
                                 description="An exceedingly rare, high-grade variant of conventional osteosarcoma characterized by the presence of numerous osteoclast-like giant cells and variable amount of tumor osteoid.",
                                 meaning=NCIT.C179410) )
        setattr(cls, "Telangiectatic Osteosarcoma",
                PermissibleValue(text="Telangiectatic Osteosarcoma",
                                 description="An osteosarcoma usually arising from the metaphysis of long bones. It is characterized by the presence of a cystic architecture with blood-filled spaces. The prognosis is similar to that of conventional osteosarcoma.",
                                 meaning=NCIT.C3902) )
        setattr(cls, "Small Cell Osteosarcoma",
                PermissibleValue(text="Small Cell Osteosarcoma",
                                 description="An osteosarcoma usually arising from the metaphysis of long bones. It is characterized by the presence of small cells and osteoid production. The prognosis is usually unfavorable.",
                                 meaning=NCIT.C4023) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class HistologyGradeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="HistologyGradeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "System NOS, GX",
                PermissibleValue(text="System NOS, GX",
                                 description="Tumor cannot be evaluated, system not specified") )
        setattr(cls, "System NOS, G1",
                PermissibleValue(text="System NOS, G1",
                                 description="Tumor is well differentiated (low grade), system not specified") )
        setattr(cls, "System NOS, G2",
                PermissibleValue(text="System NOS, G2",
                                 description="Tumor is moderately differentiated (intermediate grade), system not specified") )
        setattr(cls, "System NOS, G3",
                PermissibleValue(text="System NOS, G3",
                                 description="Tumor is poorly differentiated (high grade) , system not specified") )
        setattr(cls, "System NOS, G4",
                PermissibleValue(text="System NOS, G4",
                                 description="Tumor is undifferentiated (highest grade), system not specified") )
        setattr(cls, "FNCLCC, Grade GX",
                PermissibleValue(text="FNCLCC, Grade GX",
                                 description="Grade cannot be assessed.") )
        setattr(cls, "FNCLCC, Grade 1",
                PermissibleValue(text="FNCLCC, Grade 1",
                                 description="Total tumor differentiation, mitotic count, and necrosis score of 2 or 3.") )
        setattr(cls, "FNCLCC, Grade 2",
                PermissibleValue(text="FNCLCC, Grade 2",
                                 description="Total tumor differentiation, mitotic count, and necrosis score of 4 or 5.") )
        setattr(cls, "FNCLCC, Grade 3",
                PermissibleValue(text="FNCLCC, Grade 3",
                                 description="Total tumor differentiation, mitotic count, and necrosis score of 6, 7, or 8.") )
        setattr(cls, "Broders, Grade 1",
                PermissibleValue(text="Broders, Grade 1",
                                 description="well differentiated") )
        setattr(cls, "Broders, Grade 2",
                PermissibleValue(text="Broders, Grade 2",
                                 description="moderately differentiated") )
        setattr(cls, "Broders, Grade 3",
                PermissibleValue(text="Broders, Grade 3",
                                 description="poorly differentiated") )
        setattr(cls, "Broders, Grade 4",
                PermissibleValue(text="Broders, Grade 4",
                                 description="anaplastic") )
        setattr(cls, "Brynes. Grade 1",
                PermissibleValue(text="Brynes. Grade 1",
                                 description="well differentiated") )
        setattr(cls, "Brynes, Grade 2",
                PermissibleValue(text="Brynes, Grade 2",
                                 description="moderately differentiated") )
        setattr(cls, "Brynes, Grade 3",
                PermissibleValue(text="Brynes, Grade 3",
                                 description="poorly differentiated") )

class SomaticMalignancyTypeEnum(EnumDefinitionImpl):

    Rhabdomyosarcoma = PermissibleValue(text="Rhabdomyosarcoma",
                                                       description="A rare aggressive malignant mesenchymal neoplasm arising from skeletal muscle. It usually occurs in children and young adults. Only a small percentage of tumors arise in the skeletal muscle of the extremities. The majority arise in other anatomic sites.",
                                                       meaning=NCIT.C3359)
    Adenocarcinoma = PermissibleValue(text="Adenocarcinoma",
                                                   description="A common cancer characterized by the presence of malignant glandular cells. Morphologically, adenocarcinomas are classified according to the growth pattern (e.g., papillary, alveolar) or according to the secreting product (e.g., mucinous, serous). Representative examples of adenocarcinoma are ductal and lobular breast carcinoma, lung adenocarcinoma, renal cell carcinoma, hepatocellular carcinoma (hepatoma), colon adenocarcinoma, and prostate adenocarcinoma.",
                                                   meaning=NCIT.C2852)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="SomaticMalignancyTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Sarcoma, NOS",
                PermissibleValue(text="Sarcoma, NOS",
                                 description="A usually aggressive malignant neoplasm of the soft tissue or bone. It arises from muscle, fat, fibrous tissue, bone, cartilage, and blood vessels. Sarcomas occur in both children and adults. The prognosis depends largely on the degree of differentiation (grade) of the neoplasm. Representative subtypes are liposarcoma, leiomyosarcoma, osteosarcoma, and chondrosarcoma.",
                                 meaning=NCIT.C9118) )
        setattr(cls, "Primitive Neuroectodermal Tumor",
                PermissibleValue(text="Primitive Neuroectodermal Tumor",
                                 description="A malignant neoplasm that originates in the neuroectoderm. The neuroectoderm constitutes the portion of the ectoderm of the early embryo that gives rise to the central and peripheral nervous systems and includes some glial cell precursors.",
                                 meaning=NCIT.C3716) )
        setattr(cls, "Squamous Cell Carcinoma",
                PermissibleValue(text="Squamous Cell Carcinoma",
                                 description="A carcinoma arising from squamous epithelial cells. Morphologically, it is characterized by the proliferation of atypical, often pleomorphic squamous cells. Squamous cell carcinomas are graded by the degree of cellular differentiation as well, moderately, or poorly differentiated. Well differentiated carcinomas are usually associated with keratin production and the presence of intercellular bridges between adjacent cells. Representative examples are lung squamous cell carcinoma, skin squamous cell carcinoma, and cervical squamous cell carcinoma.",
                                 meaning=NCIT.C2929) )
        setattr(cls, "Malignant Histiocytosis",
                PermissibleValue(text="Malignant Histiocytosis",
                                 description="An antiquated term referring to cases of systemic non-Hodgkin lymphomas which are composed of large, atypical neoplastic lymphoid cells and cases of hemophagocytic syndromes. In the past, cases of anaplastic large cells lymphoma were called malignant histiocytosis.",
                                 meaning=NCIT.C7202) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class HistologyInpcEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="HistologyInpcEnum",
    )

class WhoAmlEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="WhoAmlEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "AML with t(8;21)(q22;q22.1); RUNX1-RUNX1T1",
                PermissibleValue(text="AML with t(8;21)(q22;q22.1); RUNX1-RUNX1T1",
                                 description="Acute Myeloid Leukemia with t(8;21); (q22; q22.1); RUNX1-RUNX1T1",
                                 meaning=NCIT.C9288) )
        setattr(cls, "AML with inv(16)(p13.1q22) or t(16;16)(p13.1;q22); CBFB-MYH11",
                PermissibleValue(text="AML with inv(16)(p13.1q22) or t(16;16)(p13.1;q22); CBFB-MYH11",
                                 description="Acute Myeloid Leukemia with inv(16)(p13.1q22) or t(16;16)(p13.1;q22); CBFB-MYH11",
                                 meaning=NCIT.C9287) )
        setattr(cls, "APL with PML-RARA",
                PermissibleValue(text="APL with PML-RARA",
                                 description="Childhood Acute Promyelocytic Leukemia with PML-RARA",
                                 meaning=NCIT.C7968) )
        setattr(cls, "AML with t(9;11)(p21.3;q23.3); KMT2A-MLLT3",
                PermissibleValue(text="AML with t(9;11)(p21.3;q23.3); KMT2A-MLLT3",
                                 description="Acute Myeloid Leukemia with t(9;11)(p21.3;q23.3); MLLT3-KMT2A",
                                 meaning=NCIT.C82403) )
        setattr(cls, "AML with t(6;9)(p23;q34.1);DEK-NUP214",
                PermissibleValue(text="AML with t(6;9)(p23;q34.1);DEK-NUP214",
                                 description="Acute Myeloid Leukemia with t(6;9) (p23;q34.1); DEK-NUP214",
                                 meaning=NCIT.C82423) )
        setattr(cls, "AML with inv(3)(q21.3q26.2) or t(3;3)(q21.3;q26.2); GATA2, MECOM",
                PermissibleValue(text="AML with inv(3)(q21.3q26.2) or t(3;3)(q21.3;q26.2); GATA2, MECOM",
                                 description="Acute Myeloid Leukemia with inv(3) (q21.3;q26.2) or t(3;3) (q21.3;q26.2); GATA2, MECOM",
                                 meaning=NCIT.C82426) )
        setattr(cls, "AML (megakaryoblastic) with t(1;22)(p13.3;q13.3); RBM15-MKL1",
                PermissibleValue(text="AML (megakaryoblastic) with t(1;22)(p13.3;q13.3); RBM15-MKL1",
                                 description="Acute Myeloid Leukemia (Megakaryoblastic) with t(1;22)(p13.3;q13.1); RBM15-MKL1",
                                 meaning=NCIT.C82427) )
        setattr(cls, "Provisional entity: AML with BCR-ABL1",
                PermissibleValue(text="Provisional entity: AML with BCR-ABL1",
                                 description="A rare, de novo acute myeloid leukemia in which the blasts harbor BCR-ABL1 translocation in the absence of a history and clinical and laboratory features of chronic myelogenous leukemia.",
                                 meaning=NCIT.C129785) )
        setattr(cls, "AML with mutated NPM1",
                PermissibleValue(text="AML with mutated NPM1",
                                 description="Acute Myeloid Leukemia with Mutated NPM1",
                                 meaning=NCIT.C82431) )
        setattr(cls, "AML with biallelic mutations of CEBPA",
                PermissibleValue(text="AML with biallelic mutations of CEBPA",
                                 description="An acute myeloid leukemia with double mutations of the CEBPA gene.",
                                 meaning=NCIT.C129782) )
        setattr(cls, "Provisional entity: AML with mutated RUNX1",
                PermissibleValue(text="Provisional entity: AML with mutated RUNX1",
                                 description="De novo acute myeloid leukemia with RUNX1 gene mutation, not associated with myelodysplastic syndrome-related cytogenetic abnormalities.",
                                 meaning=NCIT.C129786) )
        setattr(cls, "AML with myelodysplasia-related changes",
                PermissibleValue(text="AML with myelodysplasia-related changes",
                                 description="Acute Myeloid Leukemia with Myelodysplasia-Related Changes",
                                 meaning=NCIT.C7600) )
        setattr(cls, "Therapy-related myeloid neoplasms",
                PermissibleValue(text="Therapy-related myeloid neoplasms",
                                 description="Acute myeloid leukemias, myelodysplastic syndromes, and myelodysplastic/myeloproliferative neoplasms arising as a result of the mutagenic effect of chemotherapy agents and/or radiation that are used for the treatment of neoplastic or non-neoplastic disorders.",
                                 meaning=NCIT.C27912) )
        setattr(cls, "AML, NOS",
                PermissibleValue(text="AML, NOS",
                                 description="Acute Myeloid Leukemia NOS",
                                 meaning=NCIT.C27753) )
        setattr(cls, "AML with minimal differentiation",
                PermissibleValue(text="AML with minimal differentiation",
                                 description="Acute Myeloid Leukemia with Minimal Differentiation",
                                 meaning=NCIT.C8460) )
        setattr(cls, "AML without maturation",
                PermissibleValue(text="AML without maturation",
                                 description="Acute Myeloid Leukemia without Maturation",
                                 meaning=NCIT.C3249) )
        setattr(cls, "AML with maturation",
                PermissibleValue(text="AML with maturation",
                                 description="Acute Myeloid Leukemia with Maturation",
                                 meaning=NCIT.C3250) )
        setattr(cls, "Acute myelomonocytic leukemia",
                PermissibleValue(text="Acute myelomonocytic leukemia",
                                 description="Acute Myelomonocytic Leukemia",
                                 meaning=NCIT.C7463) )
        setattr(cls, "Acute monoblastic/monocytic leukemia",
                PermissibleValue(text="Acute monoblastic/monocytic leukemia",
                                 description="Acute Monoblastic and Monocytic Leukemia",
                                 meaning=NCIT.C7318) )
        setattr(cls, "Pure erythroid leukemia",
                PermissibleValue(text="Pure erythroid leukemia",
                                 description="Pure Erythroid Leukemia",
                                 meaning=NCIT.C7467) )
        setattr(cls, "Acute megakaryoblastic leukemia",
                PermissibleValue(text="Acute megakaryoblastic leukemia",
                                 description="Acute Megakaryoblastic Leukemia",
                                 meaning=NCIT.C3170) )
        setattr(cls, "Acute basophilic leukemia",
                PermissibleValue(text="Acute basophilic leukemia",
                                 description="Acute Basophilic Leukemia",
                                 meaning=NCIT.C3164) )
        setattr(cls, "Acute panmyelosis with myelofibrosis",
                PermissibleValue(text="Acute panmyelosis with myelofibrosis",
                                 description="Acute Panmyelosis with Myelofibrosis",
                                 meaning=NCIT.C4344) )
        setattr(cls, "Myeloid sarcoma",
                PermissibleValue(text="Myeloid sarcoma",
                                 description="Myeloid Sarcoma",
                                 meaning=NCIT.C3520) )
        setattr(cls, "Myeloid proliferations related to Down syndrome",
                PermissibleValue(text="Myeloid proliferations related to Down syndrome",
                                 description="Myeloid Proliferations Associated with Down Syndrome",
                                 meaning=NCIT.C82338) )
        setattr(cls, "Transient abnormal myelopoiesis (TAM)",
                PermissibleValue(text="Transient abnormal myelopoiesis (TAM)",
                                 description="Transient Abnormal Myelopoiesis Associated with Down Syndrome",
                                 meaning=NCIT.C82339) )
        setattr(cls, "Myeloid leukemia associated with Down syndrome",
                PermissibleValue(text="Myeloid leukemia associated with Down syndrome",
                                 description="Myeloid Leukemia Associated with Down Syndrome",
                                 meaning=NCIT.C43223) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class FabTypeEnum(EnumDefinitionImpl):

    M0 = PermissibleValue(text="M0",
                           description="Acute Myeloid Leukemia with Minimal Differentiation",
                           meaning=NCIT.C8460)
    M1 = PermissibleValue(text="M1",
                           description="Acute Myeloid Leukemia without Maturation",
                           meaning=NCIT.C3249)
    M2 = PermissibleValue(text="M2",
                           description="Acute Myeloid Leukemia with Maturation",
                           meaning=NCIT.C3250)
    M3 = PermissibleValue(text="M3",
                           description="Acute Promyelocytic Leukemia with PML-RARA",
                           meaning=NCIT.C3182)
    M4 = PermissibleValue(text="M4",
                           description="Acute Myelomonocytic Leukemia",
                           meaning=NCIT.C7463)
    M4eo = PermissibleValue(text="M4eo",
                               description="Acute Myelomonocytic Leukemia with Abnormal Eosinophils",
                               meaning=NCIT.C9020)
    M5 = PermissibleValue(text="M5",
                           description="Acute Monocytic Leukemia",
                           meaning=NCIT.C4861)
    M6 = PermissibleValue(text="M6",
                           description="Acute Erythroid Leukemia",
                           meaning=NCIT.C8923)
    M7 = PermissibleValue(text="M7",
                           description="Acute Megakaryoblastic Leukemia",
                           meaning=NCIT.C3170)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="FabTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "M3 Variant",
                PermissibleValue(text="M3 Variant",
                                 description="Acute promyelocytic leukemia in which the promyelocytes in the peripheral blood have paucity or absence of cytoplasmic granules and characteristic bilobed nuclei.",
                                 meaning=NCIT.C27757) )
        setattr(cls, "AML, NOS",
                PermissibleValue(text="AML, NOS",
                                 description="Acute Myeloid Leukemia NOS",
                                 meaning=NCIT.C27753) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class AllTypeEnum(EnumDefinitionImpl):

    MPAL = PermissibleValue(text="MPAL",
                               description="An acute leukemia of ambiguous lineage. It is characterized by the presence of either separate populations of blasts of more than one lineage, or one population of blasts co-expressing markers of more than one lineage.",
                               meaning=NCIT.C82179)

    _defn = EnumDefinition(
        name="AllTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "B-ALL",
                PermissibleValue(text="B-ALL",
                                 description="The most frequent type of acute lymphoblastic leukemia. Approximately 75% of cases occur in children under six years of age. This is a good prognosis leukemia. In the pediatric age group the complete remission rate is approximately 95% and the disease free survival rate is 70%. Approximately 80% of children appear to be cured. In the adult age group the complete remission rate is 60-85%. (WHO, 2001)",
                                 meaning=NCIT.C8644) )
        setattr(cls, "T-ALL",
                PermissibleValue(text="T-ALL",
                                 description="Acute lymphoblastic leukemia of T-cell origin. It comprises about 15% of childhood cases and 25% of adult cases. It is more common in males than females. (WHO, 2001)",
                                 meaning=NCIT.C3183) )
        setattr(cls, "Acute Leukemia, ambiguous lineage (mixed or biphenotypic)",
                PermissibleValue(text="Acute Leukemia, ambiguous lineage (mixed or biphenotypic)",
                                 description="An acute leukemia in which the blasts lack sufficient evidence to classify as myeloid or lymphoid or they have morphologic and/or immunophenotypic characteristics of both myeloid and lymphoid cells. (WHO, 2001)",
                                 meaning=NCIT.C7464) )

class RiskGroupSystemEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="RiskGroupSystemEnum",
    )

class RiskGroupEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="RiskGroupEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "IGCCCG, Good",
                PermissibleValue(text="IGCCCG, Good",
                                 description="The good prognosis category refers to testes/retroperitoneal primary and no nonpulmonary visceral metastases and the following markers: AFP less than 1,000 ng/mL, hCG less than 5,000 IU/L and LDH less than 1.5 × ULN.") )
        setattr(cls, "IGCCCG, Intermediate",
                PermissibleValue(text="IGCCCG, Intermediate",
                                 description="The intermediate risk group refers to testes/retroperitoneal primary and no nonpulmonary visceral metastases and the following markers: AFP greater than or equal to 1,000 ng/mL and less than or equal to 10,000 ng/mL, or hCG greater than or equal to 5,000 IU/L and less than or equal to 50,000 ng/mL or LDH greater than or equal to 1.5 × ULN and less than or equal to 10 × ULN.") )
        setattr(cls, "IGCCCG, Poor",
                PermissibleValue(text="IGCCCG, Poor",
                                 description="The poor prognosis category refers to mediastinal primary or nonpulmonary visceral metastases or markers with the following: AFP greater than 10,000 ng/mL or hCG greater than 50,000 IU/L or LDH greater than 10 × ULN.") )
        setattr(cls, "MaGIC, Low",
                PermissibleValue(text="MaGIC, Low",
                                 description="The low risk classification refers to age younger than 11 years and extragonadal stage III-IV disease.") )
        setattr(cls, "MaGIC, Standard",
                PermissibleValue(text="MaGIC, Standard",
                                 description="The standard risk classification refers to four-years-event-free survival of more than 80%.") )
        setattr(cls, "MaGIC, Poor",
                PermissibleValue(text="MaGIC, Poor",
                                 description="The poor risk classification refers to age equal or older than 11 years, ovarian stage IV disease, and extragonadal stage III-IV disease.") )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class MkiEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="MkiEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class DiseaseSiteEnum(EnumDefinitionImpl):

    Testes = PermissibleValue(text="Testes",
                                   description="Either of the paired male reproductive glands that produce the male germ cells and the male hormones.",
                                   meaning=NCIT.C12412)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="DiseaseSiteEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Bone Marrow",
                PermissibleValue(text="Bone Marrow",
                                 description="The tissue occupying the spaces of bone. It consiRMS of blood vessel sinuses and a network of hematopoietic cells which give rise to the red cells, white cells, and megakaryocytes.",
                                 meaning=NCIT[" C12431"]) )
        setattr(cls, "Central Nervous System",
                PermissibleValue(text="Central Nervous System",
                                 description="The part of the nervous system that consiRMS of the brain, spinal cord, and meninges.",
                                 meaning=NCIT.C12438) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class CnsDiseaseStatusEnum(EnumDefinitionImpl):

    CNS1 = PermissibleValue(text="CNS1",
                               description="The status of central nervous system leukemia at diagnosis, where there is an absence of blasts on a cerebral spinal fluid cytospin preparation, regardless of the number of white blood cells.",
                               meaning=NCIT.C116833)
    CNS2 = PermissibleValue(text="CNS2",
                               description="The status of central nervous system leukemia at diagnosis, where there are less than 5 white blood cells per microliter on a cerebral spinal fluid cytospin preparation that is positive for blasts; or greater than 5 white blood cells per microliter on a cerebral spinal fluid cytospin preparation that is considered negative by Steinherz/Bleyer algorithm.",
                               meaning=NCIT["C116834 "])
    CNS3 = PermissibleValue(text="CNS3",
                               description="The status of central nervous system leukemia at diagnosis, where there are more than 5 white blood cells per microliter on a cerebral spinal fluid cytospin preparation that is positive for blasts; with or without clinical signs of CNS leukemia.",
                               meaning=NCIT.C116835)
    CNS2a = PermissibleValue(text="CNS2a",
                                 description="The status of central nervous system leukemia at diagnosis, where there are less than 10 red blood cells and less than 5 white blood cells per microliter on a cerebral spinal fluid cytospin preparation that is positive for blasts.",
                                 meaning=NCIT.C116836)
    CNS2b = PermissibleValue(text="CNS2b",
                                 description="The status of central nervous system leukemia at diagnosis, where there are 10 or more red blood cells and less than 5 white blood cells per microliter on a cerebral spinal fluid cytospin preparation that is positive for blasts.",
                                 meaning=NCIT.C116837)
    CNS2c = PermissibleValue(text="CNS2c",
                                 description="The status of central nervous system leukemia at diagnosis, where there are 10 or more red blood cells and 5 or more white blood cells per microliter on a cerebral spinal fluid cytospin preparation that is positive for blasts and is considered negative by Steinherz/Bleyer algorithm.",
                                 meaning=NCIT.C116838)
    CNS3a = PermissibleValue(text="CNS3a",
                                 description="The status of central nervous system leukemia at diagnosis, where there are less than 10 red blood cells and 5 or more white blood cells per microliter on a cerebral spinal fluid cytospin preparation that is positive for blasts.",
                                 meaning=NCIT.C116840)
    CNS3b = PermissibleValue(text="CNS3b",
                                 description="The status of central nervous system leukemia at diagnosis, where there are 10 or more red blood cells and 5 or more white blood cells per microliter on a cerebral spinal fluid cytospin preparation that is considered positive by Steinherz/Bleyer algorithm.",
                                 meaning=NCIT.C116841)
    CNS3c = PermissibleValue(text="CNS3c",
                                 description="The status of central nervous system leukemia at diagnosis, where there are clinical signs of central system leukemia (such as facial nerve palsy, brain/eye involvement, or hypothalamic syndrome).",
                                 meaning=NCIT.C116843)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="CnsDiseaseStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class PerformanceScoreEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="PerformanceScoreEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class PerformanceScoreSystemEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="PerformanceScoreSystemEnum",
    )

class GpohScoreEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="GpohScoreEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class InitialTreatmentCategoryEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="InitialTreatmentCategoryEnum",
    )

class MyeloidSarcomaSiteEnum(EnumDefinitionImpl):

    Bone = PermissibleValue(text="Bone",
                               description="Connective tissue that forms the skeletal components of the body.",
                               meaning=NCIT.C12366)
    CNS = PermissibleValue(text="CNS",
                             description="The part of the nervous system that consiRMS of the brain, spinal cord, and meninges.",
                             meaning=NCIT.C12438)
    Orbit = PermissibleValue(text="Orbit",
                                 description="The bony cavity of the skull which contains the eye, anterior portion of the optic nerve, ocular muscles and ocular adnexa. Seven bones contribute to the structure of the orbit: the frontal, maxillary, zygomatic, sphenoid, lacrimal, ethmoid, and palatine bones.",
                                 meaning=NCIT.C12347)
    Skin = PermissibleValue(text="Skin",
                               description="An organ that constitutes the external surface of the body. It consiRMS of the epidermis, dermis, and skin appendages.",
                               meaning=NCIT.C12470)
    Testis = PermissibleValue(text="Testis",
                                   description="Either of the paired male reproductive glands that produce the male germ cells and the male hormones.",
                                   meaning=NCIT.C12412)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="MyeloidSarcomaSiteEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class GtsTreatmentEnum(EnumDefinitionImpl):

    Surgery = PermissibleValue(text="Surgery",
                                     description="The branch of medical science that treats disease or injury by operative procedures.",
                                     meaning=NCIT.C17173)
    Chemotherapy = PermissibleValue(text="Chemotherapy",
                                               description="The use of synthetic or naturally-occurring chemicals for the treatment of diseases.",
                                               meaning=NCIT.C15632)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT["17998"])

    _defn = EnumDefinition(
        name="GtsTreatmentEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT["43234"]) )

class AdministrationStatusEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="AdministrationStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Medication Administered",
                PermissibleValue(text="Medication Administered",
                                 description="An indication that medication was administered.",
                                 meaning=NCIT.C173298) )
        setattr(cls, "Medication Not Administered",
                PermissibleValue(text="Medication Not Administered",
                                 description="An indication that medication was not administered.",
                                 meaning=NCIT.C173299) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class MedicationEnum(EnumDefinitionImpl):

    Amifostine = PermissibleValue(text="Amifostine",
                                           description="The trihydrate form of a phosphorylated aminosulfhydryl compound. After dephosphorylation of amifostine by alkaline phosphatase to an active free sulfhydryl (thiol) metabolite, the thiol metabolite binds to and detoxifies cytotoxic platinum-containing metabolites of cisplatin and scavenges free radicals induced by cisplatin and ionizing radiation. The elevated activity of this agent in normal tissues results from both the relative abundance of alkaline phosphatase in normal tissues and the greater vascularity of normal tissues compared to tumor tissues.",
                                           meaning=NCIT.C488)
    Amsacrine = PermissibleValue(text="Amsacrine",
                                         description="An aminoacridine derivative with potential antineoplastic activity. Although its mechanism of action is incompletely defined, amsacrine may intercalate into DNA and inhibit topoisomerase II, resulting in DNA double-strand breaks, arrest of the S/G2 phase of the cell cycle, and cell death. This agent's cytotoxicity is maximal during the S phase of the cell cycle when topoisomerase levels are greatest. In addition, amsacrine may induce transcription of tumor promoter p53 protein and block p53 ubiquitination and proteasomal degradation, resulting in p53-dependent tumor cell apoptosis.",
                                         meaning=NCIT.C240)
    Bendamustine = PermissibleValue(text="Bendamustine",
                                               description="A bifunctional mechlorethamine derivative with alkylating and antimetabolite activities. Although the exact mechanism of action of bendamustine is unknown, this agent appears to alkylate and crosslink macromolecules, resulting in DNA, RNA and protein synthesis inhibition, and eventually the induction of apoptosis.",
                                               meaning=NCIT.C73261)
    Bleomycin = PermissibleValue(text="Bleomycin",
                                         description="A mixture of glycopeptide antineoplastic antibiotics isolated from the bacterium Streptomyces verticillus. Bleomycin forms complexes with iron that reduce molecular oxygen to superoxide and hydroxyl radicals which cause single- and double-stranded breaks in DNA; these reactive oxygen species also induce lipid peroxidation, carbohydrate oxidation, and alterations in prostaglandin synthesis and degradation.",
                                         meaning=NCIT.C313)
    Bortezomib = PermissibleValue(text="Bortezomib",
                                           description="A dipeptide boronic acid analogue with antineoplastic activity. Bortezomib reversibly inhibits the 26S proteasome, a large protease complex that degrades ubiquinated proteins. By blocking the targeted proteolysis normally performed by the proteasome, bortezomib disrupts various cell signaling pathways, leading to cell cycle arrest, apoptosis, and inhibition of angiogenesis. Specifically, the agent inhibits nuclear factor (NF)-kappaB, a protein that is constitutively activated in some cancers, thereby interfering with NF-kappaB-mediated cell survival, tumor growth, and angiogenesis. In vivo, bortezomib delays tumor growth and enhances the cytotoxic effects of radiation and chemotherapy.",
                                           meaning=NCIT.C1851)
    Busulfan = PermissibleValue(text="Busulfan",
                                       description="A synthetic derivative of dimethane-sulfonate with antineoplastic and cytotoxic properties. Although its mechanism of action is not fully understood, busulfan appears to act through the alkylation of DNA. Following systemic absorption of busulfan, carbonium ions are formed, resulting in DNA alkylation and DNA breaks and inhibition of DNA replication and RNA transcription. (NCI04)",
                                       meaning=NCIT.C321)
    Carboplatin = PermissibleValue(text="Carboplatin",
                                             description="A second-generation platinum compound with a broad spectrum of antineoplastic properties. Carboplatin contains a platinum atom complexed with two ammonia groups and a cyclobutane-dicarboxyl residue. This agent is activated intracellularly to form reactive platinum complexes that bind to nucleophilic groups such as GC-rich sites in DNA, thereby inducing intrastrand and interstrand DNA cross-links, as well as DNA-protein cross-links. These carboplatin-induced DNA and protein effects result in apoptosis and cell growth inhibition. This agent possesses tumoricidal activity similar to that of its parent compound, cisplatin, but is more stable and less toxic. (NCI04)",
                                             meaning=NCIT.C1282)
    Cabozantinib = PermissibleValue(text="Cabozantinib",
                                               description="An orally bioavailable, small molecule receptor tyrosine kinase (RTK) inhibitor with potential antineoplastic activity. Cabozantinib strongly binds to and inhibits several RTKs, which are often overexpressed in a variety of cancer cell types, including hepatocyte growth factor receptor (MET), RET (rearranged during transfection), vascular endothelial growth factor receptor types 1 (VEGFR-1), 2 (VEGFR-2), and 3 (VEGFR-3), mast/stem cell growth factor (KIT), FMS-like tyrosine kinase 3 (FLT-3), TIE-2 (TEK tyrosine kinase, endothelial), tropomyosin-related kinase B (TRKB) and AXL. This may result in an inhibition of both tumor growth and angiogenesis, and eventually lead to tumor regression.",
                                               meaning=NCIT.C52200)
    Carmustine = PermissibleValue(text="Carmustine",
                                           description="An antineoplastic nitrosourea. Carmustine alkylates and cross-links DNA during all phases of the cell cycle, resulting in disruption of DNA function, cell cycle arrest, and apoptosis. This agent also carbamoylates proteins, including DNA repair enzymes, resulting in an enhanced cytotoxic effect. Carmustine is highly lipophilic and crosses the blood-brain barrier readily. (NCI04)",
                                           meaning=NCIT.C349)
    Cisplatin = PermissibleValue(text="Cisplatin",
                                         description="An alkylating-like inorganic platinum agent (cis-diamminedichloroplatinum) with antineoplastic activity. Cisplatin forms highly reactive, charged, platinum complexes which bind to nucleophilic groups such as GC-rich sites in DNA inducing intrastrand and interstrand DNA cross-links, as well as DNA-protein cross-links. These cross-links result in apoptosis and cell growth inhibition.",
                                         meaning=NCIT.C376)
    Cladribine = PermissibleValue(text="Cladribine",
                                           description="A purine nucleoside antimetabolite analogue. Cladribine triphosphate, a phosphorylated metabolite of cladribine, incorporates into DNA, resulting in single-strand breaks in DNA, depletion of nicotinamide adenine dinucleotide (NAD) and adenosine triphosphate (ATP), and apoptosis.",
                                           meaning=NCIT.C1336)
    Clofarabine = PermissibleValue(text="Clofarabine",
                                             description="A second generation purine nucleoside analog with antineoplastic activity.",
                                             meaning=NCIT.C26638)
    Cyclophosphamide = PermissibleValue(text="Cyclophosphamide",
                                                       description="A synthetic alkylating agent chemically related to the nitrogen mustards with antineoplastic and immunosuppressive activities. In the liver, cyclophosphamide is converted to the active metabolites aldophosphamide and phosphoramide mustard, which bind to DNA, thereby inhibiting DNA replication and initiating cell death.",
                                                       meaning=NCIT.C405)
    Cytarabine = PermissibleValue(text="Cytarabine",
                                           description="An antimetabolite analogue of cytidine with a modified sugar moiety (arabinose instead of ribose).",
                                           meaning=NCIT.C408)
    Dacarbazine = PermissibleValue(text="Dacarbazine",
                                             description="A triazene derivative with antineoplastic activity. Dacarbazine alkylates and cross-links DNA during all phases of the cell cycle, resulting in disruption of DNA function, cell cycle arrest, and apoptosis. (NCI04)",
                                             meaning=NCIT.C411)
    Dactinomycin = PermissibleValue(text="Dactinomycin",
                                               description="A chromopeptide antineoplastic antibiotic isolated from the bacterium Streptomyces parvulus. Dactinomycin intercalates between adjacent guanine-cytosine base pairs, blocking the transcription of DNA by RNA polymerase; it also causes single-strand DNA breaks, possibly via a free-radical intermediate or an interaction with topoisomerase II. (NCI04)",
                                               meaning=NCIT.C412)
    Daunorubicin = PermissibleValue(text="Daunorubicin",
                                               description="An anthracycline antineoplastic antibiotic with therapeutic effects similar to those of doxorubicin. Daunorubicin exhibits cytotoxic activity through topoisomerase-mediated interaction with DNA, thereby inhibiting DNA replication and repair and RNA and protein synthesis.",
                                               meaning=NCIT.C62091)
    Denosumab = PermissibleValue(text="Denosumab",
                                         description="A fully human monoclonal antibody directed against the receptor activator of nuclear factor kappa beta ligand (RANKL) with antiosteoclast activity. Denosumab specifically binds to RANKL and blocks the interaction of RANKL with RANK, a receptor located on osteoclast cell surfaces, resulting in inhibition of osteoclast activity, a decrease in bone resorption, and a potential increase in bone mineral density. RANKL, a protein expressed by osteoblastic cells, plays an important role in osteoclastic differentiation and activation.",
                                         meaning=NCIT.C61313)
    Dexamethasone = PermissibleValue(text="Dexamethasone",
                                                 description="A synthetic adrenal corticosteroid with potent anti-inflammatory properties. In addition to binding to specific nuclear steroid receptors, dexamethasone also interferes with NF-kB activation and apoptotic pathways. This agent lacks the salt-retaining properties of other related adrenal hormones. (NCI04)",
                                                 meaning=NCIT.C422)
    Dexrazoxane = PermissibleValue(text="Dexrazoxane",
                                             description="Dexrazoxane",
                                             meaning=NCIT.C1333)
    Dinutuximab = PermissibleValue(text="Dinutuximab",
                                             description="A chimeric mouse/human monoclonal antibody with potential antineoplastic activity. Dinutuximab binds to the ganglioside GD2 and induces antibody-dependent cell-mediated cytotoxicity and complement-dependent cytotoxicity against GD2-expressing tumor cells. GD2 is overexpressed in malignant melanoma, neuroblastoma, osteosarcoma, and small cell carcinoma of the lung.",
                                             meaning=NCIT.C1570)
    Docetaxel = PermissibleValue(text="Docetaxel",
                                         description="A semi-synthetic, second-generation taxane derived from a compound found in the European yew tree, Taxus baccata. Docetaxel displays potent and broad antineoplastic properties; it binds to and stabilizes tubulin, thereby inhibiting microtubule disassembly which results in cell- cycle arrest at the G2/M phase and cell death. This agent also inhibits pro-angiogenic factors such as vascular endothelial growth factor (VEGF) and displays immunomodulatory and pro-inflammatory properties by inducing various mediators of the inflammatory response. Docetaxel has been studied for use as a radiation-sensitizing agent. (NCI04)",
                                         meaning=NCIT.C1526)
    Doxorubicin = PermissibleValue(text="Doxorubicin",
                                             description="An anthracycline antibiotic with antineoplastic activity. Doxorubicin, isolated from the bacterium Streptomyces peucetius var. caesius, is the hydroxylated congener of daunorubicin.",
                                             meaning=NCIT.C456)
    Etoposide = PermissibleValue(text="Etoposide",
                                         description="A semisynthetic derivative of podophyllotoxin, a substance extracted from the mandrake root Podophyllum peltatum. Possessing potent antineoplastic properties, etoposide binds to and inhibits topoisomerase II",
                                         meaning=NCIT.C491)
    Fludarabine = PermissibleValue(text="Fludarabine",
                                             description="A fluorinated nucleotide antimetabolite analog of the antiviral agent vidarabine (ara-A) with antineoplastic activity.",
                                             meaning=NCIT.C1094)
    Gemcitabine = PermissibleValue(text="Gemcitabine",
                                             description="A broad-spectrum antimetabolite and deoxycytidine analogue with antineoplastic activity. Upon administration, gemcitabine is converted into the active metabolites difluorodeoxycytidine diphosphate (dFdCDP) and difluorodeoxycytidine triphosphate (dFdCTP) by deoxycytidine kinase. dFdCTP competes with deoxycytidine triphosphate (dCTP) and is incorporated into DNA. This locks DNA polymerase thereby resulting in "masked termination" during DNA replication. On the other hand, dFdCDP inhibits ribonucleotide reductase, thereby decreasing the deoxynucleotide pool available for DNA synthesis. The reduction in the intracellular concentration of dCTP potentiates the incorporation of dFdCTP into DNA.",
                                             meaning=NCIT.C66876)
    Gilteritinib = PermissibleValue(text="Gilteritinib",
                                               description="An orally bioavailable inhibitor of the receptor tyrosine kinases (RTKs) FMS-related tyrosine kinase 3 (FLT3, STK1, or FLK2), AXL (UFO or JTK11) and anaplastic lymphoma kinase (ALK or CD246), with potential antineoplastic activity. Gilteritinib binds to and inhibits both the wild-type and mutated forms of FLT3, AXL and ALK. This may result in an inhibition of FLT3, AXL, and ALK-mediated signal transduction pathways and reduces tumor cell proliferation in cancer cell types that overexpress these RTKs. FLT3, AXL and ALK, overexpressed or mutated in a variety of cancer cell types, play a key role in tumor cell growth and survival.",
                                               meaning=NCIT.C116722)
    Glembatumumab = PermissibleValue(text="Glembatumumab",
                                                 description="A human monoclonal antibody against transmembrane glycoprotein non-metastatic melanoma protein B (GPNMB). Glembatumumab binds to GPNMB on cancer cells, but alone does not appear to inhibit cancer cell growth. However, this antibody could be utilized to deliver a conjugated cytotoxic agent to GPNMB-expressing tumor cells. GPNMB, overexpressed on the surface of various cancer cells, plays a key role in cancer cell proliferation.",
                                                 meaning=NCIT.C84520)
    Idarubicin = PermissibleValue(text="Idarubicin",
                                           description="A semisynthetic 4-demethoxy analogue of the antineoplastic anthracycline antibiotic daunorubicin.",
                                           meaning=NCIT.C562)
    Interferon = PermissibleValue(text="Interferon",
                                           description="Human interferons have been classified into 3 groups: alpha, beta, and gamma. Both alpha- and beta-IFNs, previously designated type I, are acid-stable, but they differ immunologically and in regard to some biologic and physiochemical properties. The IFNs produced by virus-stimulated leukocytes (leukocyte IFNs) are predominantly of the alpha type. Those produced by lymphoblastoid cells are about 90% alpha and 10% beta. Induced fibroblasts produce mainly or exclusively the beta type. The alpha- and beta-IFNs differ widely in amino acid sequence. The gamma or immune IFNs, which are produced by T lymphocytes in response to mitogens or to antigens to which they are sensitized, are acid-labile and serologically distinct from alpha- and beta-IFNs. (from OMIM 147570)",
                                           meaning=NCIT.C20493)
    Ifosfamide = PermissibleValue(text="Ifosfamide",
                                           description="A synthetic analogue of the nitrogen mustard cyclophosphamide with antineoplastic activity. Ifosfamide alkylates and forms DNA crosslinks, thereby preventing DNA strand separation and DNA replication. This agent is a prodrug that must be activated through hydroxylation by hepatic microsomal enzymes. (NCI04)",
                                           meaning=NCIT.C564)
    Melphalan = PermissibleValue(text="Melphalan",
                                         description="A phenylalanine derivative of nitrogen mustard with antineoplastic activity. Melphalan alkylates DNA at the N7 position of guanine and induces DNA inter-strand cross-linkages, resulting in the inhibition of DNA and RNA synthesis and cytotoxicity against both dividing and non-dividing tumor cells.",
                                         meaning=NCIT.C633)
    Methotrexate = PermissibleValue(text="Methotrexate",
                                               description="An antimetabolite and antifolate agent with antineoplastic and immunosuppressant activities. Methotrexate binds to and inhibits the enzyme dihydrofolate reductase, resulting in inhibition of purine nucleotide and thymidylate synthesis and, subsequently, inhibition of DNA and RNA syntheses. Methotrexate also exhibits potent immunosuppressant activity although the mechanism(s) of actions is unclear.",
                                               meaning=NCIT.C642)
    Midostaurin = PermissibleValue(text="Midostaurin",
                                             description="A synthetic indolocarbazole multikinase inhibitor with potential antiangiogenic and antineoplastic activities. Midostaurin inhibits protein kinase C alpha (PKCalpha), vascular endothelial growth factor receptor 2 (VEGFR2), c-kit, platelet-derived growth factor receptor (PDGFR) and FMS-like tyrosine kinase 3 (FLT3) tyrosine kinases, which may result in disruption of the cell cycle, inhibition of proliferation, apoptosis, and inhibition of angiogenesis in susceptible tumors.",
                                             meaning=NCIT.C1872)
    Mifamurtide = PermissibleValue(text="Mifamurtide",
                                             description="A liposomal formulation containing a muramyl dipeptide (MDP) analogue with potential immunomodulatory and antineoplastic activities. Muramyl tripeptide phosphatidylethanolamine (MTP-PE), a derivative of the mycobacterial cell wall component MDP, activates both monocytes and macrophages. Activated macrophages secrete cytokines and induce the recruitment and activation of other immune cells, which may result in indirect tumoricidal effects. Liposomal encapsulation of MTP-PE prolongs its half-life and enhances tissue targeting.",
                                             meaning=NCIT.C1394)
    Mitoxantrone = PermissibleValue(text="Mitoxantrone",
                                               description="An anthracenedione antibiotic with antineoplastic activity.",
                                               meaning=NCIT.C62050)
    Nivolumab = PermissibleValue(text="Nivolumab",
                                         description="A fully human immunoglobulin (Ig) G4 monoclonal antibody directed against the negative immunoregulatory human cell surface receptor programmed death-1 (PD-1, PCD-1) with immune checkpoint inhibitory and antineoplastic activities. Upon administration, nivolumab binds to and blocks the activation of PD-1, an immunoglobulin superfamily (IgSF) transmembrane protein, by its ligands programmed cell death ligand 1 (PD-L1), which is overexpressed on certain cancer cells, and programmed cell death ligand 2 (PD-L2), which is primarily expressed on antigen-presenting cells (APCs). This results in the activation of T-cells and cell-mediated immune responses against tumor cells. Activated PD-1 negatively regulates T-cell activation and plays a key role in tumor evasion from host immunity.",
                                         meaning=NCIT.C68814)
    Paclitaxel = PermissibleValue(text="Paclitaxel",
                                           description="A compound extracted from the Pacific yew tree Taxus brevifolia with antineoplastic activity. Paclitaxel binds to tubulin and inhibits the disassembly of microtubules, thereby resulting in the inhibition of cell division. This agent also induces apoptosis by binding to and blocking the function of the apoptosis inhibitor protein Bcl-2 (B-cell Leukemia 2). (NCI04)",
                                           meaning=NCIT.C1411)
    Pembrolizumab = PermissibleValue(text="Pembrolizumab",
                                                 description="A humanized monoclonal immunoglobulin (Ig) G4 antibody directed against human cell surface receptor PD-1 (programmed death-1 or programmed cell death-1) with potential immune checkpoint inhibitory and antineoplastic activities. Upon administration, pembrolizumab binds to PD-1, an inhibitory signaling receptor expressed on the surface of activated T cells, and blocks the binding to and activation of PD-1 by its ligands, which results in the activation of T-cell-mediated immune responses against tumor cells. The ligands for PD-1 include programmed cell death ligand 1 (PD-L1), overexpressed on certain cancer cells, and programmed cell death ligand 2 (PD-L2), which is primarily expressed on APCs. Activated PD-1 negatively regulates T-cell activation and plays a key role in in tumor evasion from host immunity.",
                                                 meaning=NCIT.C106432)
    Plerixafor = PermissibleValue(text="Plerixafor",
                                           description="A bicyclam with hematopoietic stem cell-mobilizing activity. Plerixafor blocks the binding of stromal cell-derived factor (SDF-1alpha) to the cellular receptor CXCR4, resulting in hematopoietic stem cell (HSC) release from bone marrow and HSC movement into the peripheral circulation.",
                                           meaning=NCIT.C1777)
    Prednisone = PermissibleValue(text="Prednisone",
                                           description="A synthetic glucocorticoid with anti-inflammatory and immunomodulating properties. After cell surface receptor attachment and cell entry, prednisone enters the nucleus where it binds to and activates specific nuclear receptors, resulting in an altered gene expression and inhibition of proinflammatory cytokine production. This agent also decreases the number of circulating lymphocytes, induces cell differentiation, and stimulates apoptosis in sensitive tumor cell populations.",
                                           meaning=NCIT.C770)
    Procarbazine = PermissibleValue(text="Procarbazine",
                                               description="A methylhydrazine derivative with antineoplastic and mutagenic activities. Although the exact mode of cytotoxicity has not been elucidated, procarbazine, after metabolic activation, appears to inhibit the trans-methylation of methionine into transfer RNA (t-RNA), thereby preventing protein synthesis and consequently DNA and RNA synthesis. This agent may also undergo auto-oxidation, resulting in the formation of cytotoxic free radicals which damage DNA through an alkylation reaction.",
                                               meaning=NCIT.C62072)
    Quizartinib = PermissibleValue(text="Quizartinib",
                                             description="An orally available small molecule with potential antineoplastic activity. Quizartinib selectively inhibits class III receptor tyrosine kinases, including FMS-related tyrosine kinase 3 (FLT3/STK1), colony-stimulating factor 1 receptor (CSF1R/FMS), stem cell factor receptor (SCFR/KIT), and platelet derived growth factor receptors (PDGFRs), resulting in inhibition of ligand-independent leukemic cell proliferation and apoptosis. Mutations in FLT3, resulting in constitutive activation, are the most frequent genetic alterations in acute myeloid leukemia (AML) and occur in approximately one-third of AML cases.",
                                             meaning=NCIT.C68936)
    Regorafenib = PermissibleValue(text="Regorafenib",
                                             description="The anhydrous form of regorafenib, an orally bioavailable small molecule with potential antiangiogenic and antineoplastic activities. Regorafenib binds to and inhibits vascular endothelial growth factor receptors (VEGFRs) 2 and 3, and Ret, Kit, PDGFR and Raf kinases, which may result in the inhibition of tumor angiogenesis and tumor cell proliferation. VEGFRs are receptor tyrosine kinases that play important roles in tumor angiogenesis; the receptor tyrosine kinases RET, KIT, and PDGFR, and the serine/threonine-specific Raf kinase are involved in tumor cell signaling.",
                                             meaning=NCIT.C78204)
    Sorafenib = PermissibleValue(text="Sorafenib",
                                         description="A synthetic compound targeting growth signaling and angiogenesis. Sorafenib blocks the enzyme RAF kinase, a critical component of the RAF/MEK/ERK signaling pathway that controls cell division and proliferation; in addition, sorafenib inhibits the VEGFR-2/PDGFR-beta signaling cascade, thereby blocking tumor angiogenesis.",
                                         meaning=NCIT.C61948)
    Thiotepa = PermissibleValue(text="Thiotepa",
                                       description="A polyfunctional, organophosphorus alkylating agent and a stable derivative of N,N',N''-triethylenephosphoramide (TEPA), with antineoplastic activity. Upon administration, thiotepa is converted into highly reactive ethylenimine groups, which covalently bind to nucleophilic groups in DNA and demonstrate a preference for the N7 position of guanine bases. This induces crosslinking of alkylated guanine bases in double-stranded DNA, interferes with both DNA replication and cell division, and results in both the induction of apoptosis and the inhibition of cell growth.",
                                       meaning=NCIT.C875)
    Tretinoin = PermissibleValue(text="Tretinoin",
                                         description="A naturally-occurring acid of retinol. Tretinoin binds to and activates retinoic acid receptors (RARs), thereby inducing changes in gene expression that lead to cell differentiation, decreased cell proliferation, and inhibition of tumorigenesis. This agent also inhibits telomerase, resulting in telomere shortening and eventual apoptosis of some tumor cell types. The oral form of tretinoin has teratogenic and embryotoxic properties.",
                                         meaning=NCIT.C900)
    Vinblastine = PermissibleValue(text="Vinblastine",
                                             description="A natural alkaloid isolated from the plant Vinca rosea Linn. Vinblastine binds to tubulin and inhibits microtubule formation, resulting in disruption of mitotic spindle assembly and arrest of tumor cells in the M phase of the cell cycle. This agent may also interfere with amino acid, cyclic AMP, and glutathione metabolism; calmodulin-dependent Ca++ -transport ATPase activity; cellular respiration; and nucleic acid and lipid biosynthesis. (NCI04)",
                                             meaning=NCIT.C930)
    Vincristine = PermissibleValue(text="Vincristine",
                                             description="A natural alkaloid isolated from the plant Vinca rosea Linn. Vincristine binds irreversibly to microtubules and spindle proteins in S phase of the cell cycle and interferes with the formation of the mitotic spindle, thereby arresting tumor cells in metaphase. This agent also depolymerizes microtubules and may also interfere with amino acid, cyclic AMP, and glutathione metabolism; calmodulin-dependent Ca++ -transport ATPase activity; cellular respiration; and nucleic acid and lipid biosynthesis. (NCI04)",
                                             meaning=NCIT.C933)
    Venoreline = PermissibleValue(text="Venoreline",
                                           description="A semisynthetic vinca alkaloid. Vinorelbine binds to tubulin and prevents formation of the mitotic spindle, resulting in the arrest of tumor cell growth in metaphase. This agent may also interfere with amino acid, cyclic AMP. and glutathione metabolism; calmodulin-dependent Ca++ -transport ATPase activity; cellular respiration; and nucleic acid and lipid biosynthesis.",
                                           meaning=NCIT.C1275)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="MedicationEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Arsenic Trioxide",
                PermissibleValue(text="Arsenic Trioxide",
                                 description="A small-molecule arsenic compound with antineoplastic activity. The mechanism of action of arsenic trioxide is not completely understood. This agent causes damage to or degradation of the promyelocytic leukemia protein/retinoic acid receptor-alpha (PML/RARa) fusion protein; induces apoptosis in acute promyelocytic leukemia (APL) cells and in many other tumor cell types; promotes cell differentiation and suppresses cell proliferation in many different tumor cell types; and is pro-angiogenic. (NCI04)",
                                 meaning=NCIT.C1005) )
        setattr(cls, "Brentuximab Vedotin",
                PermissibleValue(text="Brentuximab Vedotin",
                                 description="An antibody-drug conjugate (ADC) directed against the tumor necrosis factor (TNF) receptor CD30 with potential antineoplastic activity. Brentuximab vedotin is generated by conjugating the chimeric anti-CD30 monoclonal antibody SGN-30 to the cytotoxic agent monomethyl auristatin E (MMAE) via a valine-citrulline peptide linker. Upon administration and internalization by CD30-positive tumor cells, brentuximab vedotin undergoes enzymatic cleavage, releasing MMAE into the cytosol; MMAE binds to tubulin and inhibits tubulin polymerization, which may result in G2/M phase arrest and tumor cell apoptosis. Transiently activated during lymphocyte activation, CD30 (tumor necrosis factor receptor superfamily, member 8;TNFRSF8) may be constitutively expressed in hematologic malignancies including Hodgkin lymphoma and some T-cell non-Hodgkin lymphomas. The linkage system in brentuximab vedotin is highly stable in plasma, resulting in cytotoxic specificity for CD30-positive cells.",
                                 meaning=NCIT.C66944) )
        setattr(cls, "Daunorubicin (Liposomal)",
                PermissibleValue(text="Daunorubicin (Liposomal)",
                                 description="A liposome-encapsulated form of the citrate salt of the anthracycline antineoplastic antibiotic daunorubicin. Daunorubicin intercalates into DNA and interacts with topoisomerase II, thereby inhibiting DNA replication and repair and RNA and protein synthesis. Liposomal delivery of doxorubicin citrate improves drug penetration into tumors and decreases drug clearance, thereby increasing the duration of therapeutic drug effects.",
                                 meaning=NCIT.C2213) )
        setattr(cls, "Daunorubicin and Cytarabine (Liposomal)",
                PermissibleValue(text="Daunorubicin and Cytarabine (Liposomal)",
                                 description="A liposomal formulation containing a fixed combination of the antineoplastic agents cytarabine and daunorubicin in a 5:1 molar ratio. Liposome-encapsulated daunorubicin-cytarabine has been designed to provide optimal delivery of a specific ratio of cytarabine to daunorubicin, one that has been shown to be synergistic in vitro. The antimetabolite cytarabine competes with cytidine for incorporation into DNA, inhibiting DNA synthesis. This agent also inhibits DNA polymerase, resulting in a decrease in DNA replication and repair. Daunorubicin, an intercalator and a topoisomerase II inhibitor, prevents DNA replication and inhibits protein synthesis. This agent also generates oxygen free radicals, resulting in the cytotoxic lipid peroxidation of cell membrane lipids.",
                                 meaning=NCIT.C67504) )
        setattr(cls, "Etoposide Phosphate",
                PermissibleValue(text="Etoposide Phosphate",
                                 description="A phosphate salt of a semisynthetic derivative of podophyllotoxin. Etoposide binds to the enzyme topoisomerase II, inducing double-strand DNA breaks, inhibiting DNA repair, and resulting in decreased DNA synthesis and tumor cell proliferation. Cells in the S and G2 phases of the cell cycle are most sensitive to this agent. (NCI04)",
                                 meaning=NCIT.C1093) )
        setattr(cls, "Gemtuzumab Ozogamicin",
                PermissibleValue(text="Gemtuzumab Ozogamicin",
                                 description="A recombinant, humanized anti-CD33 monoclonal antibody attached to the cytotoxic antitumor antibiotic calicheamicin. In this conjugate, the antibody binds to and is internalized by tumor cells expressing CD33 antigen (a sialic acid-dependent glycoprotein commonly found on the surface of leukemic blasts), thereby delivering the attached calicheamicin to CD33-expressing tumor cells. Calicheamicin binds to the minor groove of DNA, causing double strand DNA breaks and resulting in inhibition of DNA synthesis. (NCI04)",
                                 meaning=NCIT.C1806) )
        setattr(cls, "Hydrocortisone Sodium Succinate",
                PermissibleValue(text="Hydrocortisone Sodium Succinate",
                                 description="The sodium salt of hydrocortisone succinate with glucocorticoid property. Hydrocortisone sodium succinate is chemically similar to the endogenous hormone that stimulates anti-inflammatory and immunosuppressive activities, in addition to exhibiting minor mineralocorticoid effects. This agent binds to intracellular glucocorticoid receptors and is translocated into the nucleus, where it initiates the transcription of glucocorticoid-responsive genes, such as various cytokines and lipocortins. Lipocortins inhibit phospholipase A2, thereby blocking the release of arachidonic acid from membrane phospholipids and preventing the synthesis of prostaglandins and leukotrienes, both potent mediators of inflammation.",
                                 meaning=NCIT.C1819) )
        setattr(cls, "Nitrogen Mustard",
                PermissibleValue(text="Nitrogen Mustard",
                                 description="A synthetic agent related to sulphur mustard with antineoplastic and immunosuppressive properties. Nitrogen mustard (a member of a family of chemotherapy agents including cyclophosphamide and chlorambucil) is an irritant and carcinogenic agent metabolized to a highly reactive ethylene immonium derivative; the ethylene immonium derivative alkylates DNA and inhibits DNA replication. This agent also exhibits lympholytic properties. (NCI04)",
                                 meaning=NCIT.C62056) )
        setattr(cls, "Systemic corticosteroid",
                PermissibleValue(text="Systemic corticosteroid",
                                 description="Treatment with corticosteroids via a delivery method that will affect the entire body (oral, intramuscular, intravenous).",
                                 meaning=NCIT.C122080) )
        setattr(cls, "Topical corticosteroid",
                PermissibleValue(text="Topical corticosteroid",
                                 description="Any synthetic steroid derivative exhibiting the same function as the naturally occurring corticosteroid hormone, formulated for topical application. Topical corticosteroids are applied to the skin where it exerts its effect, however, corticosteroids can be absorbed systemically after being applied locally. Topical corticosteroids are mainly used for the localized treatment of inflammation of the skin and help relieve symptoms such as itching, swelling and redness.",
                                 meaning=NCIT.C29505) )
        setattr(cls, "Zoledronic Acid",
                PermissibleValue(text="Zoledronic Acid",
                                 description="A synthetic imidazole bisphosphonate analog of pyrophosphate with anti-bone-resorption activity. A third-generation bisphosphonate, zoledronic acid binds to hydroxyapatite crystals in the bone matrix, slowing their dissolution and inhibiting the formation and aggregation of these crystals. This agent also inhibits farnesyl pyrophosphate synthase, an enzyme involved in terpenoid biosynthesis. Inhibition of this enzyme prevents the biosynthesis of isoprenoid lipids, donor substrates of farnesylation and geranylgeranylation during the post-translational modification of small GTPase signalling proteins, which are important in the process of osteoclast turnover. Decreased bone turnover and stabilization of the bone matrix contribute to the analgesic effect of zoledronic acid with respect to painful osteoblastic lesions. The agent also reduces serum calcium concentrations associated with hypercalcemia.",
                                 meaning=NCIT.C1699) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class NonProtocolTimingEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="NonProtocolTimingEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Prior to Study",
                PermissibleValue(text="Prior to Study",
                                 description="The time period before the study.",
                                 meaning=NCIT.C175039) )
        setattr(cls, "After Study Completion",
                PermissibleValue(text="After Study Completion",
                                 description="The time period after the completion of the study.",
                                 meaning=NCIT.C175040) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class NonProtocolReasonEnum(EnumDefinitionImpl):

    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)

    _defn = EnumDefinition(
        name="NonProtocolReasonEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Treatment for Adverse Event",
                PermissibleValue(text="Treatment for Adverse Event",
                                 meaning=NCIT.C88082) )

class RouteEnum(EnumDefinitionImpl):

    Systemic = PermissibleValue(text="Systemic",
                                       description="Immunotherapy that is disseminated throughout the body via the bloodstream.",
                                       meaning=NCIT.C173291)
    Intrathecal = PermissibleValue(text="Intrathecal",
                                             description="Immunotherapy that is administered into the cerebrospinal fluid.",
                                             meaning=NCIT.C173292)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="RouteEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class RouteDetailEnum(EnumDefinitionImpl):

    Parenteral = PermissibleValue(text="Parenteral",
                                           description="Administration of a substance by some means other than through the gastrointestinal tract: usually through injection, infusion, or implantation. Predominantly, the drug action is systemic, but in some cases, it is confined to local area.",
                                           meaning=NCIT.C38291)
    Oral = PermissibleValue(text="Oral",
                               description="The introduction of a substance to the mouth or into the gastrointestinal tract by the way of the mouth, usually for systemic action. It is the most common, convenient, and usually the safest and least expensive route of drug administration, but it uses the most complicated pathway to the tissues and bioavailability varies. The disadvantages of method are hepatic first pass metabolism and enzymatic degradation of the drug within the gastrointestinal tract. This prohibits oral administration of certain classes of drugs especially peptides and proteins.",
                               meaning=NCIT.C38288)

    _defn = EnumDefinition(
        name="RouteDetailEnum",
    )

class NormalizationBasisEnum(EnumDefinitionImpl):

    Weight = PermissibleValue(text="Weight",
                                   description="The weight of a subject.",
                                   meaning=NCIT.C81328)
    BSA = PermissibleValue(text="BSA",
                             description="A measure of the 2-dimensional extent of the body surface (i.e., the skin). Body surface area (BSA) can be calculated by mathematical formula or from a chart that relates height to weight. BSA is often an important factor in dosing.",
                             meaning=NCIT.C25157)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="NormalizationBasisEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class TotalDoseUnitsEnum(EnumDefinitionImpl):

    mg = PermissibleValue(text="mg",
                           description="A metric unit of mass equal to one thousandth of a gram or 1000 micrograms. One milligram equals approximately 0.015 432 grain or 35.274 x 10E-6 ounce.",
                           meaning=NCIT.C67402)
    IU = PermissibleValue(text="IU",
                           description="The unitage assigned by the WHO to International Biological Standards - substances, classed as biological according to the criteria provided by WHO Expert Committee on Biological Standardization (e.g. hormones, enzymes, and vaccines), to enable the results of biological and immunological assay procedures to be expressed in the same way throughout the world. The definition of an international unit is generally arbitrary and technical, and has to be officially approved by the International Conference for Unification of Formulae.",
                           meaning=NCIT.C48579)

    _defn = EnumDefinition(
        name="TotalDoseUnitsEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "mg/m2",
                PermissibleValue(text="mg/m2",
                                 description="A metric unit of areal density equal to approximately 2.94935E-5 ounce per square yard. Also used as a dose calculation unit.",
                                 meaning=NCIT.C67402) )
        setattr(cls, "mg/kilo",
                PermissibleValue(text="mg/kilo",
                                 description="A unit of a mass fraction expressed as a number of milligrams of substance per kilogram of mixture. The unit is also used as a dose calculation unit.",
                                 meaning=NCIT.C67401) )
        setattr(cls, "IU/m2",
                PermissibleValue(text="IU/m2",
                                 description="A dose calculation unit expressed as a number of arbitrary units of biological activity (International Units) of substance per square meter of body surface area.",
                                 meaning=NCIT.C67378) )

class ModTypeEnum(EnumDefinitionImpl):

    Substitution = PermissibleValue(text="Substitution",
                                               description="The act of putting one thing or person in the place of another.",
                                               meaning=NCIT.C54071)
    Discontinued = PermissibleValue(text="Discontinued",
                                               description="To stop or end, permanently or temporarily.",
                                               meaning=NCIT.C25484)
    Delayed = PermissibleValue(text="Delayed",
                                     description="Time during which some action is awaited; inactivity resulting in something being put off until a later time; the state of being slower or later.",
                                     meaning=NCIT.C25476)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)

    _defn = EnumDefinition(
        name="ModTypeEnum",
    )

class ModRationaleEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="ModRationaleEnum",
    )

class ModReasonEnum(EnumDefinitionImpl):

    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)

    _defn = EnumDefinition(
        name="ModReasonEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Hematologic Toxicity",
                PermissibleValue(text="Hematologic Toxicity",
                                 description="A treatment designed to reduce or prevent damage to the hematologic system due to adverse events from other drug therapies.",
                                 meaning=NCIT.C15474) )
        setattr(cls, "Surgical Complications",
                PermissibleValue(text="Surgical Complications",
                                 description="A disease or disorder that occurs during, soon after or as a result of a surgical procedure.",
                                 meaning=NCIT.C164157) )
        setattr(cls, "Subject Non-Compliance",
                PermissibleValue(text="Subject Non-Compliance",
                                 description="Failure of a patient to follow medical advice, take medication as directed, or adhere to a prescribed course of treatment.",
                                 meaning=NCIT.C91752) )

class ToxicityDetailEnum(EnumDefinitionImpl):

    Infection = PermissibleValue(text="Infection",
                                         description="The invasion of an organism's body tissues by disease-causing agents and their multiplication, as well as the reaction by the host to these organisms and/or toxins that the organisms produce.",
                                         meaning=NCIT.C128320)
    Mucositis = PermissibleValue(text="Mucositis",
                                         description="Inflammation of the mucous membranes.",
                                         meaning=NCIT.C115965)
    Neutropenia = PermissibleValue(text="Neutropenia",
                                             description="A decrease in the number of neutrophils in the peripheral blood.",
                                             meaning=NCIT.C80520)
    Thrombocytopenia = PermissibleValue(text="Thrombocytopenia",
                                                       description="A laboratory test result indicating that there is an abnormally small number of platelets in the circulating blood.",
                                                       meaning=NCIT.C3408)
    Neuropathy = PermissibleValue(text="Neuropathy",
                                           description="A disorder affecting the cranial nerves or the peripheral nervous system. It manifests with pain, tingling, numbness, and muscle weakness. It may be the result of physical injury, toxic substances, viral diseases, diabetes, renal failure, cancer, and drugs.",
                                           meaning=NCIT.C4731)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)

    _defn = EnumDefinition(
        name="ToxicityDetailEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Allergic Reaction",
                PermissibleValue(text="Allergic Reaction",
                                 description="An immune response that occurs following re-exposure to an innocuous antigen, and that requires the presence of existing antibodies against that antigen. This response involves the binding of IgE to mast cells, and may worsen with repeated exposures.",
                                 meaning=NCIT.C114476) )
        setattr(cls, "Renal Toxicity",
                PermissibleValue(text="Renal Toxicity",
                                 description="Toxicity that impairs or damages the kidney. This condition is often caused by the administration of a pharmaceutical agent that causes damage to the kidney.",
                                 meaning=NCIT.C115459) )
        setattr(cls, "Cardiac Toxicity",
                PermissibleValue(text="Cardiac Toxicity",
                                 description="Toxicity that impairs or damages the heart. This condition is often caused by the administration of a pharmaceutical agent that initiates a poisonous or toxic response in cardiac tissue.",
                                 meaning=NCIT.C27994) )
        setattr(cls, "Pulmonary Toxicity",
                PermissibleValue(text="Pulmonary Toxicity",
                                 description="Toxicity that impairs or damages the lung(s). This condition is often caused by the administration of a pharmaceutical agent that causes damage to the lungs.",
                                 meaning=NCIT.C177374) )
        setattr(cls, "Endocrine Toxicity",
                PermissibleValue(text="Endocrine Toxicity",
                                 description="Indicates that a toxicity adverse effect has been experienced during endocrine drug treatment.",
                                 meaning=NCIT.C138163) )

class BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum(EnumDefinitionImpl):

    Bendamustine = PermissibleValue(text="Bendamustine",
                                               description="A bifunctional mechlorethamine derivative with alkylating and antimetabolite activities. Although the exact mechanism of action of bendamustine is unknown, this agent appears to alkylate and crosslink macromolecules, resulting in DNA, RNA and protein synthesis inhibition, and eventually the induction of apoptosis.",
                                               meaning=NCIT.C73261)
    Bleomycin = PermissibleValue(text="Bleomycin",
                                         description="A mixture of glycopeptide antineoplastic antibiotics isolated from the bacterium Streptomyces verticillus. Bleomycin forms complexes with iron that reduce molecular oxygen to superoxide and hydroxyl radicals which cause single- and double-stranded breaks in DNA; these reactive oxygen species also induce lipid peroxidation, carbohydrate oxidation, and alterations in prostaglandin synthesis and degradation.",
                                         meaning=NCIT.C313)
    Busulfan = PermissibleValue(text="Busulfan",
                                       description="A synthetic derivative of dimethane-sulfonate with antineoplastic and cytotoxic properties. Although its mechanism of action is not fully understood, busulfan appears to act through the alkylation of DNA. Following systemic absorption of busulfan, carbonium ions are formed, resulting in DNA alkylation and DNA breaks and inhibition of DNA replication and RNA transcription. (NCI04)",
                                       meaning=NCIT.C321)
    Carboplatin = PermissibleValue(text="Carboplatin",
                                             description="A second-generation platinum compound with a broad spectrum of antineoplastic properties. Carboplatin contains a platinum atom complexed with two ammonia groups and a cyclobutane-dicarboxyl residue. This agent is activated intracellularly to form reactive platinum complexes that bind to nucleophilic groups such as GC-rich sites in DNA, thereby inducing intrastrand and interstrand DNA cross-links, as well as DNA-protein cross-links. These carboplatin-induced DNA and protein effects result in apoptosis and cell growth inhibition. This agent possesses tumoricidal activity similar to that of its parent compound, cisplatin, but is more stable and less toxic. (NCI04)",
                                             meaning=NCIT.C1282)
    Carmustine = PermissibleValue(text="Carmustine",
                                           description="An antineoplastic nitrosourea. Carmustine alkylates and cross-links DNA during all phases of the cell cycle, resulting in disruption of DNA function, cell cycle arrest, and apoptosis. This agent also carbamoylates proteins, including DNA repair enzymes, resulting in an enhanced cytotoxic effect. Carmustine is highly lipophilic and crosses the blood-brain barrier readily. (NCI04)",
                                           meaning=NCIT.C349)
    Cisplatin = PermissibleValue(text="Cisplatin",
                                         description="An alkylating-like inorganic platinum agent (cis-diamminedichloroplatinum) with antineoplastic activity. Cisplatin forms highly reactive, charged, platinum complexes which bind to nucleophilic groups such as GC-rich sites in DNA inducing intrastrand and interstrand DNA cross-links, as well as DNA-protein cross-links. These cross-links result in apoptosis and cell growth inhibition.",
                                         meaning=NCIT.C376)
    Cyclophosphamide = PermissibleValue(text="Cyclophosphamide",
                                                       description="A synthetic alkylating agent chemically related to the nitrogen mustards with antineoplastic and immunosuppressive activities. In the liver, cyclophosphamide is converted to the active metabolites aldophosphamide and phosphoramide mustard, which bind to DNA, thereby inhibiting DNA replication and initiating cell death.",
                                                       meaning=NCIT.C405)
    Cytarabine = PermissibleValue(text="Cytarabine",
                                           description="An antimetabolite analogue of cytidine with a modified sugar moiety (arabinose instead of ribose). Cytarabine is converted to the triphosphate form within the cell and then competes with cytidine for incorporation into DNA. Because the arabinose sugar sterically hinders the rotation of the molecule within DNA, DNA replication ceases, specifically during the S phase of the cell cycle. This agent also inhibits DNA polymerase, resulting in a decrease in DNA replication and repair. (NCI04)",
                                           meaning=NCIT.C408)
    Dacarbazine = PermissibleValue(text="Dacarbazine",
                                             description="A triazene derivative with antineoplastic activity. Dacarbazine alkylates and cross-links DNA during all phases of the cell cycle, resulting in disruption of DNA function, cell cycle arrest, and apoptosis. (NCI04)",
                                             meaning=NCIT.C411)
    Dexamethasone = PermissibleValue(text="Dexamethasone",
                                                 description="A synthetic adrenal corticosteroid with potent anti-inflammatory properties. In addition to binding to specific nuclear steroid receptors, dexamethasone also interferes with NF-kB activation and apoptotic pathways. This agent lacks the salt-retaining properties of other related adrenal hormones. (NCI04)",
                                                 meaning=NCIT.C422)
    Doxorubicin = PermissibleValue(text="Doxorubicin",
                                             description="An anthracycline antibiotic with antineoplastic activity. Doxorubicin, isolated from the bacterium Streptomyces peucetius var. caesius, is the hydroxylated congener of daunorubicin. Doxorubicin intercalates between base pairs in the DNA helix, thereby preventing DNA replication and ultimately inhibiting protein synthesis. Additionally, doxorubicin inhibits topoisomerase II which results in an increased and stabilized cleavable enzyme-DNA linked complex during DNA replication and subsequently prevents the ligation of the nucleotide strand after double-strand breakage. Doxorubicin also forms oxygen free radicals resulting in cytotoxicity secondary to lipid peroxidation of cell membrane lipids; the formation of oxygen free radicals also contributes to the toxicity of the anthracycline antibiotics, namely the cardiac and cutaneous vascular effects.",
                                             meaning=NCIT.C456)
    Etoposide = PermissibleValue(text="Etoposide",
                                         description="A semisynthetic derivative of podophyllotoxin, a substance extracted from the mandrake root Podophyllum peltatum. Possessing potent antineoplastic properties, etoposide binds to and inhibits topoisomerase II and its function in ligating cleaved DNA molecules, resulting in the accumulation of single- or double-strand DNA breaks, the inhibition of DNA replication and transcription, and apoptotic cell death. Etoposide acts primarily in the G2 and S phases of the cell cycle. (NCI04)",
                                         meaning=NCIT.C491)
    Fludarabine = PermissibleValue(text="Fludarabine",
                                             description="A fluorinated nucleotide antimetabolite analog of the antiviral agent vidarabine (ara-A) with antineoplastic activity. Administered parenterally as a phosphate salt, fludarabine phosphate is rapidly dephosphorylated to 2-fluoro-ara-A and then phosphorylated intracellularly by deoxycytidine kinase to the active triphosphate, 2-fluoro-ara-ATP. This metabolite may inhibit DNA polymerase alpha, ribonucleotide reductase and DNA primase, thereby interrupting DNA synthesis and inhibiting tumor cell growth. (NCI04)",
                                             meaning=NCIT.C1094)
    Gemcitabine = PermissibleValue(text="Gemcitabine",
                                             description="A broad-spectrum antimetabolite and deoxycytidine analogue with antineoplastic activity. Upon administration, gemcitabine is converted into the active metabolites difluorodeoxycytidine diphosphate (dFdCDP) and difluorodeoxycytidine triphosphate (dFdCTP) by deoxycytidine kinase. dFdCTP competes with deoxycytidine triphosphate (dCTP) and is incorporated into DNA. This locks DNA polymerase thereby resulting in "masked termination" during DNA replication. On the other hand, dFdCDP inhibits ribonucleotide reductase, thereby decreasing the deoxynucleotide pool available for DNA synthesis. The reduction in the intracellular concentration of dCTP potentiates the incorporation of dFdCTP into DNA.",
                                             meaning=NCIT.C66876)
    Ifosfamide = PermissibleValue(text="Ifosfamide",
                                           description="A synthetic analogue of the nitrogen mustard cyclophosphamide with antineoplastic activity. Ifosfamide alkylates and forms DNA crosslinks, thereby preventing DNA strand separation and DNA replication. This agent is a prodrug that must be activated through hydroxylation by hepatic microsomal enzymes. (NCI04)",
                                           meaning=NCIT.C564)
    Melphalan = PermissibleValue(text="Melphalan",
                                         description="A phenylalanine derivative of nitrogen mustard with antineoplastic activity. Melphalan alkylates DNA at the N7 position of guanine and induces DNA inter-strand cross-linkages, resulting in the inhibition of DNA and RNA synthesis and cytotoxicity against both dividing and non-dividing tumor cells.",
                                         meaning=NCIT.C633)
    Methotrexate = PermissibleValue(text="Methotrexate",
                                               description="An antimetabolite and antifolate agent with antineoplastic and immunosuppressant activities. Methotrexate binds to and inhibits the enzyme dihydrofolate reductase, resulting in inhibition of purine nucleotide and thymidylate synthesis and, subsequently, inhibition of DNA and RNA syntheses. Methotrexate also exhibits potent immunosuppressant activity although the mechanism(s) of actions is unclear.",
                                               meaning=NCIT.C642)
    Nivolumab = PermissibleValue(text="Nivolumab",
                                         description="A fully human immunoglobulin (Ig) G4 monoclonal antibody directed against the negative immunoregulatory human cell surface receptor programmed death-1 (PD-1, PCD-1) with immune checkpoint inhibitory and antineoplastic activities. Upon administration, nivolumab binds to and blocks the activation of PD-1, an immunoglobulin superfamily (IgSF) transmembrane protein, by its ligands programmed cell death ligand 1 (PD-L1), which is overexpressed on certain cancer cells, and programmed cell death ligand 2 (PD-L2), which is primarily expressed on antigen-presenting cells (APCs). This results in the activation of T-cells and cell-mediated immune responses against tumor cells. Activated PD-1 negatively regulates T-cell activation and plays a key role in tumor evasion from host immunity.",
                                         meaning=NCIT.C68814)
    Pembrolizumab = PermissibleValue(text="Pembrolizumab",
                                                 description="A humanized monoclonal immunoglobulin (Ig) G4 antibody directed against human cell surface receptor PD-1 (programmed death-1 or programmed cell death-1) with potential immune checkpoint inhibitory and antineoplastic activities. Upon administration, pembrolizumab binds to PD-1, an inhibitory signaling receptor expressed on the surface of activated T cells, and blocks the binding to and activation of PD-1 by its ligands, which results in the activation of T-cell-mediated immune responses against tumor cells. The ligands for PD-1 include programmed cell death ligand 1 (PD-L1), overexpressed on certain cancer cells, and programmed cell death ligand 2 (PD-L2), which is primarily expressed on APCs. Activated PD-1 negatively regulates T-cell activation and plays a key role in in tumor evasion from host immunity.",
                                                 meaning=NCIT.C106432)
    Prednisone = PermissibleValue(text="Prednisone",
                                           description="A synthetic glucocorticoid with anti-inflammatory and immunomodulating properties. After cell surface receptor attachment and cell entry, prednisone enters the nucleus where it binds to and activates specific nuclear receptors, resulting in an altered gene expression and inhibition of proinflammatory cytokine production. This agent also decreases the number of circulating lymphocytes, induces cell differentiation, and stimulates apoptosis in sensitive tumor cell populations.",
                                           meaning=NCIT.C770)
    Procarbazine = PermissibleValue(text="Procarbazine",
                                               description="A methylhydrazine derivative with antineoplastic and mutagenic activities. Although the exact mode of cytotoxicity has not been elucidated, procarbazine, after metabolic activation, appears to inhibit the trans-methylation of methionine into transfer RNA (t-RNA), thereby preventing protein synthesis and consequently DNA and RNA synthesis. This agent may also undergo auto-oxidation, resulting in the formation of cytotoxic free radicals which damage DNA through an alkylation reaction.",
                                               meaning=NCIT.C62072)
    Thiotepa = PermissibleValue(text="Thiotepa",
                                       description="A polyfunctional, organophosphorus alkylating agent and a stable derivative of N,N',N''-triethylenephosphoramide (TEPA), with antineoplastic activity. Upon administration, thiotepa is converted into highly reactive ethylenimine groups, which covalently bind to nucleophilic groups in DNA and demonstrate a preference for the N7 position of guanine bases. This induces crosslinking of alkylated guanine bases in double-stranded DNA, interferes with both DNA replication and cell division, and results in both the induction of apoptosis and the inhibition of cell growth.",
                                       meaning=NCIT.C875)
    Vinorelbine = PermissibleValue(text="Vinorelbine",
                                             description="A semisynthetic vinca alkaloid. Vinorelbine binds to tubulin and prevents formation of the mitotic spindle, resulting in the arrest of tumor cell growth in metaphase. This agent may also interfere with amino acid, cyclic AMP. and glutathione metabolism; calmodulin-dependent Ca++ -transport ATPase activity; cellular respiration; and nucleic acid and lipid biosynthesis.",
                                             meaning=NCIT.C1275)
    Vinblastine = PermissibleValue(text="Vinblastine",
                                             description="A natural alkaloid isolated from the plant Vinca rosea Linn. Vinblastine binds to tubulin and inhibits microtubule formation, resulting in disruption of mitotic spindle assembly and arrest of tumor cells in the M phase of the cell cycle. This agent may also interfere with amino acid, cyclic AMP, and glutathione metabolism; calmodulin-dependent Ca++ -transport ATPase activity; cellular respiration; and nucleic acid and lipid biosynthesis. (NCI04)",
                                             meaning=NCIT.C930)
    Vincristine = PermissibleValue(text="Vincristine",
                                             description="A natural alkaloid isolated from the plant Vinca rosea Linn. Vincristine binds irreversibly to microtubules and spindle proteins in S phase of the cell cycle and interferes with the formation of the mitotic spindle, thereby arresting tumor cells in metaphase. This agent also depolymerizes microtubules and may also interfere with amino acid, cyclic AMP, and glutathione metabolism; calmodulin-dependent Ca++ -transport ATPase activity; cellular respiration; and nucleic acid and lipid biosynthesis. (NCI04)",
                                             meaning=NCIT.C933)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)

    _defn = EnumDefinition(
        name="BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Brentuximab Vedotin",
                PermissibleValue(text="Brentuximab Vedotin",
                                 description="An antibody-drug conjugate (ADC) directed against the tumor necrosis factor (TNF) receptor CD30 with potential antineoplastic activity. Brentuximab vedotin is generated by conjugating the chimeric anti-CD30 monoclonal antibody SGN-30 to the cytotoxic agent monomethyl auristatin E (MMAE) via a valine-citrulline peptide linker. Upon administration and internalization by CD30-positive tumor cells, brentuximab vedotin undergoes enzymatic cleavage, releasing MMAE into the cytosol; MMAE binds to tubulin and inhibits tubulin polymerization, which may result in G2/M phase arrest and tumor cell apoptosis. Transiently activated during lymphocyte activation, CD30 (tumor necrosis factor receptor superfamily, member 8;TNFRSF8) may be constitutively expressed in hematologic malignancies including Hodgkin lymphoma and some T-cell non-Hodgkin lymphomas. The linkage system in brentuximab vedotin is highly stable in plasma, resulting in cytotoxic specificity for CD30-positive cells.",
                                 meaning=NCIT.C66944) )
        setattr(cls, "Etoposide Phosphate",
                PermissibleValue(text="Etoposide Phosphate",
                                 description="A phosphate salt of a semisynthetic derivative of podophyllotoxin. Etoposide binds to the enzyme topoisomerase II, inducing double-strand DNA breaks, inhibiting DNA repair, and resulting in decreased DNA synthesis and tumor cell proliferation. Cells in the S and G2 phases of the cell cycle are most sensitive to this agent. (NCI04)",
                                 meaning=NCIT.C1093) )
        setattr(cls, "Nitrogen Mustard",
                PermissibleValue(text="Nitrogen Mustard",
                                 description="A synthetic agent related to sulphur mustard with antineoplastic and immunosuppressive properties. Nitrogen mustard (a member of a family of chemotherapy agents including cyclophosphamide and chlorambucil) is an irritant and carcinogenic agent metabolized to a highly reactive ethylene immonium derivative; the ethylene immonium derivative alkylates DNA and inhibits DNA replication. This agent also exhibits lympholytic properties. (NCI04)",
                                 meaning=NCIT.C62056) )

class TumorClassificationEnum(EnumDefinitionImpl):

    Primary = PermissibleValue(text="Primary",
                                     description="A tumor at the original site of origin.",
                                     meaning=NCIT.C8509)
    Metastatic = PermissibleValue(text="Metastatic",
                                           description="A term referring to the clinical or pathologic observation of a tumor extension from its original site of growth to another anatomic site.",
                                           meaning=NCIT.C14174)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="TumorClassificationEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class BoneNotreportedSofttissueUnknownEnum(EnumDefinitionImpl):

    Bone = PermissibleValue(text="Bone",
                               description="Connective tissue that forms the skeletal components of the body.",
                               meaning=NCIT.C12366)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="BoneNotreportedSofttissueUnknownEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Soft Tissue",
                PermissibleValue(text="Soft Tissue",
                                 description="A general term comprising tissue that is not hardened or calcified; including muscle, fat, blood vessels, nerves, tendons, ligaments and fascia.",
                                 meaning=NCIT.C12471) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class RtSiteEnum(EnumDefinitionImpl):

    Abdomen = PermissibleValue(text="Abdomen",
                                     description="The portion of the body that lies between the thorax and the pelvis.",
                                     meaning=NCIT.C12664)
    Adrenal = PermissibleValue(text="Adrenal",
                                     description="A bone located between the femur and the tarsus, being part of the lower leg.",
                                     meaning=NCIT.C12800)
    Ankle = PermissibleValue(text="Ankle",
                                 description="The small, lateral calf bone extending from the knee to the ankle.",
                                 meaning=NCIT.C12718)
    Anus = PermissibleValue(text="Anus",
                               description="The lower opening of the digestive tract, lying in the cleft between the buttocks, through which fecal matter is extruded.",
                               meaning=NCIT.C43362)
    Appendix = PermissibleValue(text="Appendix",
                                       description="Small tissue projection existing as a cecal diverticulum with a questionable history of vestigial versus specialized organ.",
                                       meaning=NCIT.C12380)
    Axilla = PermissibleValue(text="Axilla",
                                   description="One of a pair of bones linking the scapula and the sternum. The clavicle is part of the pectoral girdle.",
                                   meaning=NCIT.C12695)
    Bladder = PermissibleValue(text="Bladder",
                                     description="The distensible sac-like organ that functions as a reservoir of urine, collecting from the kidneys and eliminating via the urethra.",
                                     meaning=NCIT.C12414)
    Brain = PermissibleValue(text="Brain",
                                 description="An organ composed of grey and white matter containing billions of neurons that is the center for intelligence and reasoning. It is protected by the bony cranium.",
                                 meaning=NCIT.C12439)
    Breast = PermissibleValue(text="Breast",
                                   description="One of two hemispheric projections of variable size situated in the subcutaneous layer over the pectoralis major muscle on either side of the chest.",
                                   meaning=NCIT.C12971)
    Bronchus = PermissibleValue(text="Bronchus",
                                       description="Tubular structure in continuation with the trachea, serving as air passage. It terminates in the lung (terminal bronchiole).",
                                       meaning=NCIT.C12683)
    Buttock = PermissibleValue(text="Buttock",
                                     description="Either of the fleshy mounds in the rear pelvic area of the human body formed by the gluteal muscles.",
                                     meaning=NCIT.C89806)
    Carpal = PermissibleValue(text="Carpal",
                                   description="A joint between the distal end of the radius and the proximal row of carpal bones.",
                                   meaning=NCIT.C33894)
    Chest = PermissibleValue(text="Chest",
                                 description="The anterior side of the thorax from the neck to the abdomen. The shape of the chest is often regarded as potential insight into a disease process, as in the case of barrel chest and respiratory dysfunction.",
                                 meaning=NCIT.C25389)
    Clavicle = PermissibleValue(text="Clavicle",
                                       description="One of a pair of bones linking the scapula and the sternum. The clavicle is part of the pectoral girdle.",
                                       meaning=NCIT.C12695)
    Coccyx = PermissibleValue(text="Coccyx",
                                   description="A small bone located at the bottom of the spine. The coccyx is a result of 3-5 fused rudimentary vertebrae.",
                                   meaning=NCIT.C12696)
    Colon = PermissibleValue(text="Colon",
                                 description="The part of the large intestine measured from the cecum to the rectum consisting of ascending, transverse, descending and sigmoid portions. The purpose of the colon is to remove water from digested food prior to excretion.",
                                 meaning=NCIT.C12382)
    Cutaneous = PermissibleValue(text="Cutaneous",
                                         description="Having to do with the skin.",
                                         meaning=NCIT.C13316)
    Duodenum = PermissibleValue(text="Duodenum",
                                       description="A jointed tube 25-30 cm long that connects the stomach to the jejunum.",
                                       meaning=NCIT.C12263)
    Elbow = PermissibleValue(text="Elbow",
                                 description="A type of hinge joint located between the forearm and upper arm.",
                                 meaning=NCIT.C32497)
    Epididymis = PermissibleValue(text="Epididymis",
                                           description="A crescent-like structure located in the upper and posterior surfaces of the testis. It consists of the efferent ductules and the duct of the epididymis. It facilitates the maturation of sperm that is produced in the testis.",
                                           meaning=NCIT.C12328)
    Esophagus = PermissibleValue(text="Esophagus",
                                         description="The portion of the digestive canal between the pharynx and stomach. It is about 25 cm long and consists of three parts: the cervical part, from the cricoid cartilage to the thoracic inlet; thoracic part, from thoracic inlet to the diaphragm; and abdominal part, below the diaphragm to the cardiac opening of the stomach.",
                                         meaning=NCIT.C12389)
    Ethmoid = PermissibleValue(text="Ethmoid",
                                     description="A light and spongy bone that is cubical in shape. This bone is positioned at the anterior part of the cranium, sitting between the two orbits, at the roof of the nose. It consists of four parts: a horizontal or cribriform plate; a perpendicular plate; and two lateral masses or labyrinths.",
                                     meaning=NCIT.C12711)
    Femur = PermissibleValue(text="Femur",
                                 description="The upper leg bone positioned between the pelvis and the knee.",
                                 meaning=NCIT.C12717)
    Fibula = PermissibleValue(text="Fibula",
                                   description="The small, lateral calf bone extending from the knee to the ankle.",
                                   meaning=NCIT.C12718)
    Finger = PermissibleValue(text="Finger",
                                   description="Any of the digits of the hand.",
                                   meaning=NCIT.C32608)
    Foot = PermissibleValue(text="Foot",
                               description="The structure found below the ankle joint required for locomotion.",
                               meaning=NCIT.C32622)
    Forearm = PermissibleValue(text="Forearm",
                                     description="The structure on the upper limb, between the elbow and the wrist.",
                                     meaning=NCIT.C32628)
    Gallbladder = PermissibleValue(text="Gallbladder",
                                             description="A pear-shaped organ located under the liver that stores and concentrates bile secreted by the liver. From the gallbladder the bile is delivered through the bile ducts into the intestine thereby aiding the digestion of fat-containing foods.",
                                             meaning=NCIT.C12377)
    Groin = PermissibleValue(text="Groin",
                                 description="The lower region of the anterior abdominal wall located laterally to the pubic region.",
                                 meaning=NCIT.C12726)
    Hand = PermissibleValue(text="Hand",
                               description="The distal portion of the upper extremity. It consists of the carpus, metacarpus, and digits.",
                               meaning=NCIT.C32712)
    Heart = PermissibleValue(text="Heart",
                                 description="A hollow organ located slightly to the left of the middle portion of the chest. It is composed of muscle and it is divided by a septum into two sides: the right side which receives de-oxygenated blood from the body and the left side which sends newly oxygenated blood to the body. Each side is composed of two chambers: the atrium (receiving blood) and ventricle (ejecting blood).",
                                 meaning=NCIT.C12727)
    Humerus = PermissibleValue(text="Humerus",
                                     description="The upper arm bone between the shoulder and elbow.",
                                     meaning=NCIT.C12731)
    Kidney = PermissibleValue(text="Kidney",
                                   description="One of the two bean-shaped organs located on each side of the spine in the retroperitoneum. The right kidney is located below the liver and the left kidney below the diaphragm. The kidneys filter and secrete metabolic products and minerals from the blood, thus maintaining homeostasis. On the superior pole of each kidney there is an adrenal gland. Each kidney and adrenal gland is surrounded by fat.",
                                   meaning=NCIT.C12415)
    Knee = PermissibleValue(text="Knee",
                               description="A joint connecting the lower part of the femur with the upper part of the tibia. The lower part of the femur and the upper part of the tibia are attached to each other by ligaments. Other structures of the knee joint include the upper part of the fibula, located below and parallel to the tibia, and the patella which moves as the knee bends.",
                               meaning=NCIT.C32898)
    Larynx = PermissibleValue(text="Larynx",
                                   description="The cartilaginous structure of the respiratory tract between the pharynx and the trachea. It contains elastic vocal cords required for sound production.",
                                   meaning=NCIT.C12420)
    Leg = PermissibleValue(text="Leg",
                             description="The portion of the lower extremity between the knee and the ankle. For clinical purposes this term is also used to refer to the whole inferior limb.",
                             meaning=NCIT.C32974)
    Lung = PermissibleValue(text="Lung",
                               description="One of a pair of viscera occupying the pulmonary cavities of the thorax, the organs of respiration in which aeration of the blood takes place. As a rule, the right lung is slightly larger than the left and is divided into three lobes (an upper, a middle, and a lower or basal), while the left has two lobes (an upper and a lower or basal). Each lung is irregularly conical in shape, presenting a blunt upper extremity (the apex), a concave base following the curve of the diaphragm, an outer convex surface (costal surface), an inner or mediastinal surface (mediastinal surface), a thin and sharp anterior border, and a thick and rounded posterior border.",
                               meaning=NCIT.C12468)
    Mandible = PermissibleValue(text="Mandible",
                                       description="The lower jaw bone holding the lower teeth.",
                                       meaning=NCIT.C12290)
    Maxilla = PermissibleValue(text="Maxilla",
                                     description="The upper jawbone in vertebrates; it is fused to the cranium.",
                                     meaning=NCIT.C26470)
    Meninges = PermissibleValue(text="Meninges",
                                       description="Any one of three membranes that surround the brain and spinal cord.",
                                       meaning=NCIT.C12348)
    Metacarpals = PermissibleValue(text="Metacarpals",
                                             description="Any of the five bones between the wrist and the fingers that form the skeleton of the palm.",
                                             meaning=NCIT.C12751)
    Metatarsals = PermissibleValue(text="Metatarsals",
                                             description="A bone belonging to the middle part of the foot located between toes and ankle. There are 5 metatarsal bones and they are numbered from the medial side.",
                                             meaning=NCIT.C12752)
    Neck = PermissibleValue(text="Neck",
                               description="The region that connects the head to the rest of the body.",
                               meaning=NCIT.C13063)
    Orbit = PermissibleValue(text="Orbit",
                                 description="The bony cavity of the skull which contains the eye, anterior portion of the optic nerve, ocular muscles and ocular adnexa. Seven bones contribute to the structure of the orbit: the frontal, maxillary, zygomatic, sphenoid, lacrimal, ethmoid, and palatine bones.",
                                 meaning=NCIT.C12347)
    Ovary = PermissibleValue(text="Ovary",
                                 description="One of the paired female reproductive glands containing the ova or germ cells; the ovary's stroma is a vascular connective tissue containing numbers of ovarian follicles enclosing the ova.",
                                 meaning=NCIT.C12404)
    Pancreas = PermissibleValue(text="Pancreas",
                                       description="An organ behind the lower part of the stomach that is the shape of a fish and about the size of a hand. It is a compound gland composed of both exocrine and endocrine tissues. The endocrine pancreas makes insulin so that the body can use glucose (sugar) for energy. The exocrine pancreas makes enzymes that help the body digest food. Spread all over the pancreas are areas called the Islets of Langerhans. The cells in these areas each have a special purpose. The alpha cells make glucagon, which raises the level of glucose in the blood; the beta cells make insulin; the delta cells make somatostatin. There are also PP cells and D1 cells, about which little is known.",
                                       meaning=NCIT.C12393)
    Paratesticular = PermissibleValue(text="Paratesticular",
                                                   description="A small anatomical compartment that contains the testicular collecting system, and mesothelial and mesenchymal components that represent extensions of the abdominal cavity and retroperitoneum.",
                                                   meaning=NCIT.C162491)
    Patella = PermissibleValue(text="Patella",
                                     description="A small flat triangular bone in front of the knee that articulates with the femur and protects the knee joint.",
                                     meaning=NCIT.C33282)
    Pelvis = PermissibleValue(text="Pelvis",
                                   description="The bony, basin-shaped structure formed by the hipbones and the base of the backbone supporting the lower limbs in humans.",
                                   meaning=NCIT.C12767)
    Penis = PermissibleValue(text="Penis",
                                 description="The male organ of urination and copulation.",
                                 meaning=NCIT.C12409)
    Peritoneum = PermissibleValue(text="Peritoneum",
                                           description="The tissue that lines the wall of the abdominal cavity, intestine, mesentery, and pelvic organs. It consists of the parietal peritoneum and the visceral peritoneum.",
                                           meaning=NCIT.C12770)
    Pleura = PermissibleValue(text="Pleura",
                                   description="The tissue that lines the wall of the thoracic cavity and the surface of the lungs.",
                                   meaning=NCIT.C12469)
    Prostate = PermissibleValue(text="Prostate",
                                       description="The walnut shaped accessory sex gland of the male reproductive system. It is located in the pelvis just below the bladder, surrounding the prostatic part of the urethra. The prostate gland secretes a fluid which is part of the semen.",
                                       meaning=NCIT.C12410)
    Radius = PermissibleValue(text="Radius",
                                   description="The long bone of the forearm that extends from the lateral aspect of the elbow to the thumb-side of the wrist.",
                                   meaning=NCIT.C12777)
    Rectum = PermissibleValue(text="Rectum",
                                   description="The terminal portion of the gastrointestinal tract, extending from the rectosigmoid junction to the anal canal.",
                                   meaning=NCIT.C12390)
    Rib = PermissibleValue(text="Rib",
                             description="Any one of the paired bones, 12 on either side, extending from the thoracic vertebrae toward the median line on the ventral aspect of the trunk. The long curved bones which form the rib cage. Generally, ribs 1 to 7 are connected to the sternum by their costal cartilages and are called true ribs, whereas ribs 8 to 12 are termed false ribs.",
                             meaning=NCIT.C12782)
    Sacrum = PermissibleValue(text="Sacrum",
                                   description="The triangular bone, made up of 5 fused bones of the spine, located in the lower area of the spine between the fifth lumbar vertebra and the coccyx.",
                                   meaning=NCIT.C33508)
    Scapula = PermissibleValue(text="Scapula",
                                     description="The flat triangle-shaped bone that connects the humerus with the clavicle in the back of the shoulder.",
                                     meaning=NCIT.C12783)
    Skull = PermissibleValue(text="Skull",
                                 description="The bones that form the head, made up of the bones of the braincase and face.",
                                 meaning=NCIT.C12789)
    Spleen = PermissibleValue(text="Spleen",
                                   description="An organ that is part of the hematopoietic and immune systems. It is composed of the white pulp and the red pulp and is surrounded by a capsule. It is located in the left hypochondriac region. Its functions include lymphocyte production, blood cell storage, and blood cell destruction.",
                                   meaning=NCIT.C12432)
    Sternum = PermissibleValue(text="Sternum",
                                     description="The long, flat bone connecting with the cartilages of the first seven ribs and the clavicle.",
                                     meaning=NCIT.C12793)
    Stomach = PermissibleValue(text="Stomach",
                                     description="An organ located under the diaphragm, between the liver and the spleen as well as between the esophagus and the small intestine. The stomach is the primary organ of food digestion.",
                                     meaning=NCIT.C12391)
    Tarsals = PermissibleValue(text="Tarsals",
                                     description="Any one of the seven bones forming the instep of the foot.",
                                     meaning=NCIT.C12796)
    Testes = PermissibleValue(text="Testes",
                                   description="Either of the paired male reproductive glands that produce the male germ cells and the male hormones.",
                                   meaning=NCIT.C12412)
    Thalamus = PermissibleValue(text="Thalamus",
                                       description="A part of the lower limb, located between hip and knee.",
                                       meaning=NCIT.C33763)
    Thyroid = PermissibleValue(text="Thyroid",
                                     description="A bone located between the femur and the tarsus, being part of the lower leg.",
                                     meaning=NCIT.C12800)
    Tibia = PermissibleValue(text="Tibia",
                                 description="One of the terminal digits of the foot.",
                                 meaning=NCIT.C33788)
    Tonsil = PermissibleValue(text="Tonsil",
                                   description="The two organs situated in the throat on either side of the narrow passage from the mouth to the pharynx. They are composed of lymphoid tissues.",
                                   meaning=NCIT.C12802)
    Ulna = PermissibleValue(text="Ulna",
                               description="One of the bones that comprise the forearm. The largest aspect articulates with the humerus at the elbow joint and the smallest portion of the ulna articulates with the carpal bones in the wrist.",
                               meaning=NCIT.C12809)
    Ureter = PermissibleValue(text="Ureter",
                                   description="The thick-walled tube that carries urine from each kidney to the bladder.",
                                   meaning=NCIT.C12416)
    Uterus = PermissibleValue(text="Uterus",
                                   description="A hollow, thick-walled, muscular organ located within the pelvic cavity of a woman. Within the uterus the fertilized egg implants and the fetus develops during pregnancy.",
                                   meaning=NCIT.C12405)
    Vagina = PermissibleValue(text="Vagina",
                                   description="The female genital canal, extending from the uterus to the vulva.",
                                   meaning=NCIT.C12407)
    Viscera = PermissibleValue(text="Viscera",
                                     description="Two or more internal organs.",
                                     meaning=NCIT.C28287)
    Vulva = PermissibleValue(text="Vulva",
                                 description="The external, visible part of the female genitalia surrounding the urethral and vaginal opening. The vulva includes the clitoris and inner as well as outer labia.",
                                 meaning=NCIT.C12408)
    Wrist = PermissibleValue(text="Wrist",
                                 description="A joint between the distal end of the radius and the proximal row of carpal bones.",
                                 meaning=NCIT.C33894)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="RtSiteEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Abdominal Wall",
                PermissibleValue(text="Abdominal Wall",
                                 description="The upper leg bone positioned between the pelvis and the knee.",
                                 meaning=NCIT.C12717) )
        setattr(cls, "Ankle Joint",
                PermissibleValue(text="Ankle Joint",
                                 description="A gliding joint between the distal ends of the tibia and fibula and the proximal end of the talus.",
                                 meaning=NCIT.C32078) )
        setattr(cls, "Bone Face",
                PermissibleValue(text="Bone Face",
                                 description="Any bone that contributes to the facial structures, except those bones that are part of the braincase.",
                                 meaning=NCIT.C63706) )
        setattr(cls, "Bone Foot",
                PermissibleValue(text="Bone Foot",
                                 description="One of the seven tarsal, five metatarsal, or 14 phalangeal bones in the foot.",
                                 meaning=NCIT.C13068) )
        setattr(cls, "Bone Shoulder Girdle",
                PermissibleValue(text="Bone Shoulder Girdle",
                                 description="The bony arch formed by the collarbones and shoulder blades.",
                                 meaning=NCIT.C33547) )
        setattr(cls, "Cervical Spine",
                PermissibleValue(text="Cervical Spine",
                                 description="The set of vertebrae immediately caudal to the skull.",
                                 meaning=NCIT.C69313) )
        setattr(cls, "Chest Wall",
                PermissibleValue(text="Chest Wall",
                                 description="The total system of structures outside the lungs that move as a part of breathing; it includes all structures from the skin to the parietal pleura.",
                                 meaning=NCIT.C62484) )
        setattr(cls, "Dorsal Spine",
                PermissibleValue(text="Dorsal Spine",
                                 description="A spinal curve that originates at the middle of the second thoracic vertebra and terminates at the middle of the last thoracic vertebra.",
                                 meaning=NCIT.C32472) )
        setattr(cls, "Elbow Joint",
                PermissibleValue(text="Elbow Joint",
                                 description="A type of hinge joint located between the forearm and upper arm.",
                                 meaning=NCIT.C32497) )
        setattr(cls, "Fallopian Tube",
                PermissibleValue(text="Fallopian Tube",
                                 description="One of a pair of tubes that extend from the uterus to each of the ovaries. Following ovulation the egg travels down the fallopian tube to the uterus where fertilization may or may not occur.",
                                 meaning=NCIT.C12403) )
        setattr(cls, "Foot Joint",
                PermissibleValue(text="Foot Joint",
                                 description="A bone of the foot.",
                                 meaning=NCIT.C52772) )
        setattr(cls, "Gastrointestinal Tract",
                PermissibleValue(text="Gastrointestinal Tract",
                                 description="The upper gastrointestinal (GI) tract is comprised of mouth, pharynx, esophagus and stomach while the lower GI tract consists of intestines and anus. The primary function of the GI tract is to ingest, digest, absorb and ultimately excrete food stuff.",
                                 meaning=NCIT.C34082) )
        setattr(cls, "Hand Bone",
                PermissibleValue(text="Hand Bone",
                                 description="A bone of the hand.",
                                 meaning=NCIT.C52771) )
        setattr(cls, "Hand Phalanges",
                PermissibleValue(text="Hand Phalanges",
                                 description="The hinge synovial joints between the phalanges of the fingers.",
                                 meaning=NCIT.C32868) )
        setattr(cls, "Head and Neck",
                PermissibleValue(text="Head and Neck",
                                 description="For oncology, an area of the body generally construed to comprise the base of skull and facial bones, sinuses, orbits, salivary glands, oral cavity, oropharynx, larynx, thyroid, facial and neck musculature and lymph nodes draining these areas.",
                                 meaning=NCIT.C12418) )
        setattr(cls, "Inferior Limb",
                PermissibleValue(text="Inferior Limb",
                                 description="A bone of the leg (lower extremity).",
                                 meaning=NCIT.C12982) )
        setattr(cls, "Knee Joint",
                PermissibleValue(text="Knee Joint",
                                 description="A joint connecting the lower part of the femur with the upper part of the tibia. The lower part of the femur and the upper part of the tibia are attached to each other by ligaments. Other structures of the knee joint include the upper part of the fibula, located below and parallel to the tibia, and the patella which moves as the knee bends.",
                                 meaning=NCIT.C32898) )
        setattr(cls, "Large Vessels",
                PermissibleValue(text="Large Vessels",
                                 description="Any of the major arteries or veins attached to the cardiac atria or ventricles. This includes the aorta, superior and inferior vena cava and the pulmonary arteries and veins.",
                                 meaning=NCIT.C102955) )
        setattr(cls, "Lower Limb",
                PermissibleValue(text="Lower Limb",
                                 description="The limb that is composed of the hip, thigh, leg and foot.",
                                 meaning=NCIT.C12742) )
        setattr(cls, "Lumbar Spine",
                PermissibleValue(text="Lumbar Spine",
                                 description="Those vertebrae between the ribs and the pelvis, L1-L5 in man.",
                                 meaning=NCIT.C69314) )
        setattr(cls, "Lymph Nodes",
                PermissibleValue(text="Lymph Nodes",
                                 description="A bean-shaped organ surrounded by a connective tissue capsule. It is part of the lymphatic system and is found throughout the body. It is composed predominantly of lymphocytes and its main function is immune protection.",
                                 meaning=NCIT.C12745) )
        setattr(cls, "Nasal Septum",
                PermissibleValue(text="Nasal Septum",
                                 description="The thin wall between the two nasal cavities.",
                                 meaning=NCIT.C33160) )
        setattr(cls, "Oral Cavity",
                PermissibleValue(text="Oral Cavity",
                                 description="The cavity located at the upper end of the alimentary canal, behind the teeth and gums that is bounded on the outside by the lips, above by the hard and soft palates and below by the tongue.",
                                 meaning=NCIT.C12421) )
        setattr(cls, "Salivary Gland",
                PermissibleValue(text="Salivary Gland",
                                 description="An exocrine gland that secretes saliva. Salivary glands are mostly located in and around the oral cavity.",
                                 meaning=NCIT.C12426) )
        setattr(cls, "Shoulder Girdle",
                PermissibleValue(text="Shoulder Girdle",
                                 description="The bony arch formed by the collarbones and shoulder blades.",
                                 meaning=NCIT.C33547) )
        setattr(cls, "Shoulder Joint",
                PermissibleValue(text="Shoulder Joint",
                                 description="A ball-and-socket joint at the upper end of the humerus, located at the junction of humerus and scapula.",
                                 meaning=NCIT.C33548) )
        setattr(cls, "Skull and Face Bone",
                PermissibleValue(text="Skull and Face Bone",
                                 description="The section of the intestines between the pylorus and cecum. The small intestine is approximately 20 feet long and consists of the duodenum, the jejunum, and the ileum. Its main function is to absorb nutrients from food as the food is transported to the large intestine.",
                                 meaning=NCIT.C12386) )
        setattr(cls, "Small Intestine",
                PermissibleValue(text="Small Intestine",
                                 description="The section of the intestines between the pylorus and cecum. The small intestine is approximately 20 feet long and consists of the duodenum, the jejunum, and the ileum. Its main function is to absorb nutrients from food as the food is transported to the large intestine.",
                                 meaning=NCIT.C12386) )
        setattr(cls, "Superior Maxilla",
                PermissibleValue(text="Superior Maxilla",
                                 meaning=NCIT.C33682) )
        setattr(cls, "Thorax Internal",
                PermissibleValue(text="Thorax Internal",
                                 description="An endocrine gland located at the base of the neck that produces and secretes thyroxine and other hormones. Thyroxine is important for metabolic control.",
                                 meaning=NCIT.C12400) )
        setattr(cls, "Upper Arm",
                PermissibleValue(text="Upper Arm",
                                 description="The portion of the upper extremity between the shoulder and the elbow. For clinical purposes this term is also used to refer to the whole superior limb.",
                                 meaning=NCIT.C32141) )
        setattr(cls, "Upper Extremity",
                PermissibleValue(text="Upper Extremity",
                                 description="The region of the body that includes the arm, the forearm, and hand.") )
        setattr(cls, "Upper Limb",
                PermissibleValue(text="Upper Limb",
                                 description="The thick-walled tube that carries urine from each kidney to the bladder.",
                                 meaning=NCIT.C12671) )
        setattr(cls, "Wrist Joint",
                PermissibleValue(text="Wrist Joint",
                                 description="A joint between the distal end of the radius and the proximal row of carpal bones.",
                                 meaning=NCIT.C33894) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class EnergyTypeEnum(EnumDefinitionImpl):

    Proton = PermissibleValue(text="Proton",
                                   description="A type of external beam radiation therapy using a beam of protons. It has the advantage of precisely localizing the radiation dose on the targeted tissue and avoiding damage to the healthy surrounding tissues.",
                                   meaning=NCIT.C66897)
    Photon = PermissibleValue(text="Photon",
                                   description="A single unit of electromagnetic radiation, generally considered to be a discrete particle having no mass or charge.",
                                   meaning=NCIT.C88112)
    Brachytherapy = PermissibleValue(text="Brachytherapy",
                                                 description="A type of radiation therapy in which radioactive material is placed inside the body, into a tumor or body cavity.",
                                                 meaning=NCIT.C15195)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="EnergyTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "3D Conformal",
                PermissibleValue(text="3D Conformal",
                                 description="A process by which a dose of radiation is automatically shaped to closely conform to the entire volume of the tumor, so that surrounding normal tissue is spared and treatment toxicity is decreased.",
                                 meaning=NCIT.C16035) )
        setattr(cls, "Intensity-Modulated Radiation Therapy",
                PermissibleValue(text="Intensity-Modulated Radiation Therapy",
                                 description="An advanced form of 3-Dimensional Conformal Radiation Therapy (3D CRT) that involves the use of varying intensities of small radiation beams to produce dosage distributions that are more precise than those possible with 3D CRT.",
                                 meaning=NCIT.C16135) )
        setattr(cls, "Proton Stereotactic Body Radiation Therapy",
                PermissibleValue(text="Proton Stereotactic Body Radiation Therapy",
                                 description="Stereotactic body radiation therapy (SBRT) that utilizes a proton beam.",
                                 meaning=NCIT.C175032) )
        setattr(cls, "Photon Stereotactic Body Radiation Therapy",
                PermissibleValue(text="Photon Stereotactic Body Radiation Therapy",
                                 description="Stereotactic body radiation therapy (SBRT) that utilizes a photon beam.",
                                 meaning=NCIT.C175033) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class RtUnitEnum(EnumDefinitionImpl):

    Gy = PermissibleValue(text="Gy",
                           description="A SI derived unit of absorbed radiation dose. One gray is equal to an absorbed dose of one joule per kilogram of matter, or to 100 rads.",
                           meaning=NCIT.C18063)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="RtUnitEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class TranspositionOrganEnum(EnumDefinitionImpl):

    Ovaries = PermissibleValue(text="Ovaries",
                                     description="One of the paired female reproductive glands containing the ova or germ cells; the ovary's stroma is a vascular connective tissue containing numbers of ovarian follicles enclosing the ova.",
                                     meaning=NCIT.C12404)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="TranspositionOrganEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class ProcedureSiteEnum(EnumDefinitionImpl):

    Adrenal = PermissibleValue(text="Adrenal",
                                     description="A bone located between the femur and the tarsus, being part of the lower leg.",
                                     meaning=NCIT.C12800)
    Ankle = PermissibleValue(text="Ankle",
                                 description="The small, lateral calf bone extending from the knee to the ankle.",
                                 meaning=NCIT.C12718)
    Anus = PermissibleValue(text="Anus",
                               description="The lower opening of the digestive tract, lying in the cleft between the buttocks, through which fecal matter is extruded.",
                               meaning=NCIT.C43362)
    Appendix = PermissibleValue(text="Appendix",
                                       description="Small tissue projection existing as a cecal diverticulum with a questionable history of vestigial versus specialized organ.",
                                       meaning=NCIT.C12380)
    Axilla = PermissibleValue(text="Axilla",
                                   description="One of a pair of bones linking the scapula and the sternum. The clavicle is part of the pectoral girdle.",
                                   meaning=NCIT.C12695)
    Bladder = PermissibleValue(text="Bladder",
                                     description="The distensible sac-like organ that functions as a reservoir of urine, collecting from the kidneys and eliminating via the urethra.",
                                     meaning=NCIT.C12414)
    Bone = PermissibleValue(text="Bone",
                               description="Connective tissue that forms the skeletal components of the body.",
                               meaning=NCIT.C12366)
    Brain = PermissibleValue(text="Brain",
                                 description="An organ composed of grey and white matter containing billions of neurons that is the center for intelligence and reasoning. It is protected by the bony cranium.",
                                 meaning=NCIT.C12439)
    Breast = PermissibleValue(text="Breast",
                                   description="One of two hemispheric projections of variable size situated in the subcutaneous layer over the pectoralis major muscle on either side of the chest.",
                                   meaning=NCIT.C12971)
    Bronchus = PermissibleValue(text="Bronchus",
                                       description="Tubular structure in continuation with the trachea, serving as air passage. It terminates in the lung (terminal bronchiole).",
                                       meaning=NCIT.C12683)
    Carpal = PermissibleValue(text="Carpal",
                                   description="A joint between the distal end of the radius and the proximal row of carpal bones.",
                                   meaning=NCIT.C33894)
    Colon = PermissibleValue(text="Colon",
                                 description="The part of the large intestine measured from the cecum to the rectum consisting of ascending, transverse, descending and sigmoid portions. The purpose of the colon is to remove water from digested food prior to excretion.",
                                 meaning=NCIT.C12382)
    Cutaneous = PermissibleValue(text="Cutaneous",
                                         description="Having to do with the skin.",
                                         meaning=NCIT.C13316)
    Duodenum = PermissibleValue(text="Duodenum",
                                       description="A jointed tube 25-30 cm long that connects the stomach to the jejunum.",
                                       meaning=NCIT.C12263)
    Epididymis = PermissibleValue(text="Epididymis",
                                           description="A crescent-like structure located in the upper and posterior surfaces of the testis. It consists of the efferent ductules and the duct of the epididymis. It facilitates the maturation of sperm that is produced in the testis.",
                                           meaning=NCIT.C12328)
    Esophagus = PermissibleValue(text="Esophagus",
                                         description="The portion of the digestive canal between the pharynx and stomach. It is about 25 cm long and consists of three parts: the cervical part, from the cricoid cartilage to the thoracic inlet; thoracic part, from thoracic inlet to the diaphragm; and abdominal part, below the diaphragm to the cardiac opening of the stomach.",
                                         meaning=NCIT.C12389)
    Femur = PermissibleValue(text="Femur",
                                 description="The upper leg bone positioned between the pelvis and the knee.",
                                 meaning=NCIT.C12717)
    Fibula = PermissibleValue(text="Fibula",
                                   description="The small, lateral calf bone extending from the knee to the ankle.",
                                   meaning=NCIT.C12718)
    Finger = PermissibleValue(text="Finger",
                                   description="Any of the digits of the hand.",
                                   meaning=NCIT.C32608)
    Foot = PermissibleValue(text="Foot",
                               description="The structure found below the ankle joint required for locomotion.",
                               meaning=NCIT.C32622)
    Forearm = PermissibleValue(text="Forearm",
                                     description="The structure on the upper limb, between the elbow and the wrist.",
                                     meaning=NCIT.C32628)
    Gallbladder = PermissibleValue(text="Gallbladder",
                                             description="A pear-shaped organ located under the liver that stores and concentrates bile secreted by the liver. From the gallbladder the bile is delivered through the bile ducts into the intestine thereby aiding the digestion of fat-containing foods.",
                                             meaning=NCIT.C12377)
    Groin = PermissibleValue(text="Groin",
                                 description="The lower region of the anterior abdominal wall located laterally to the pubic region.",
                                 meaning=NCIT.C12726)
    Hand = PermissibleValue(text="Hand",
                               description="The distal portion of the upper extremity. It consists of the carpus, metacarpus, and digits.",
                               meaning=NCIT.C32712)
    Heart = PermissibleValue(text="Heart",
                                 description="A hollow organ located slightly to the left of the middle portion of the chest. It is composed of muscle and it is divided by a septum into two sides: the right side which receives de-oxygenated blood from the body and the left side which sends newly oxygenated blood to the body. Each side is composed of two chambers: the atrium (receiving blood) and ventricle (ejecting blood).",
                                 meaning=NCIT.C12727)
    Humerus = PermissibleValue(text="Humerus",
                                     description="The upper arm bone between the shoulder and elbow.",
                                     meaning=NCIT.C12731)
    Kidney = PermissibleValue(text="Kidney",
                                   description="One of the two bean-shaped organs located on each side of the spine in the retroperitoneum. The right kidney is located below the liver and the left kidney below the diaphragm. The kidneys filter and secrete metabolic products and minerals from the blood, thus maintaining homeostasis. On the superior pole of each kidney there is an adrenal gland. Each kidney and adrenal gland is surrounded by fat.",
                                   meaning=NCIT.C12415)
    Knee = PermissibleValue(text="Knee",
                               description="A joint connecting the lower part of the femur with the upper part of the tibia. The lower part of the femur and the upper part of the tibia are attached to each other by ligaments. Other structures of the knee joint include the upper part of the fibula, located below and parallel to the tibia, and the patella which moves as the knee bends.",
                               meaning=NCIT.C32898)
    Larynx = PermissibleValue(text="Larynx",
                                   description="The cartilaginous structure of the respiratory tract between the pharynx and the trachea. It contains elastic vocal cords required for sound production.",
                                   meaning=NCIT.C12420)
    Leg = PermissibleValue(text="Leg",
                             description="The portion of the lower extremity between the knee and the ankle. For clinical purposes this term is also used to refer to the whole inferior limb.",
                             meaning=NCIT.C32974)
    Liver = PermissibleValue(text="Liver",
                                 description="A triangular-shaped organ located under the diaphragm in the right hypochondrium. It is the largest internal organ of the body, weighting up to 2 kg. Metabolism and bile secretion are its main functions. It is composed of cells which have the ability to regenerate.",
                                 meaning=NCIT.C12392)
    Lung = PermissibleValue(text="Lung",
                               description="One of a pair of viscera occupying the pulmonary cavities of the thorax, the organs of respiration in which aeration of the blood takes place. As a rule, the right lung is slightly larger than the left and is divided into three lobes (an upper, a middle, and a lower or basal), while the left has two lobes (an upper and a lower or basal). Each lung is irregularly conical in shape, presenting a blunt upper extremity (the apex), a concave base following the curve of the diaphragm, an outer convex surface (costal surface), an inner or mediastinal surface (mediastinal surface), a thin and sharp anterior border, and a thick and rounded posterior border.",
                               meaning=NCIT.C12468)
    Mandible = PermissibleValue(text="Mandible",
                                       description="The lower jaw bone holding the lower teeth.",
                                       meaning=NCIT.C12290)
    Maxilla = PermissibleValue(text="Maxilla",
                                     description="The upper jawbone in vertebrates; it is fused to the cranium.",
                                     meaning=NCIT.C26470)
    Mediastinum = PermissibleValue(text="Mediastinum",
                                             description="A Hodgkin lymphoma that arises from the mediastinum. It usually involves mediastinal lymph nodes and/or the thymus. Signs and symptoms include fever, weight loss, fatigue, and night sweats.",
                                             meaning=NCIT.C6634)
    Meninges = PermissibleValue(text="Meninges",
                                       description="Any one of three membranes that surround the brain and spinal cord.",
                                       meaning=NCIT.C12348)
    Metacarpus = PermissibleValue(text="Metacarpus",
                                           description="Any of the five bones between the wrist and the fingers that form the skeleton of the palm.",
                                           meaning=NCIT.C12751)
    Metatarsus = PermissibleValue(text="Metatarsus",
                                           description="A bone belonging to the middle part of the foot located between toes and ankle. There are 5 metatarsal bones and they are numbered from the medial side.",
                                           meaning=NCIT.C12752)
    Neck = PermissibleValue(text="Neck",
                               description="The region that connects the head to the rest of the body.",
                               meaning=NCIT.C13063)
    Orbit = PermissibleValue(text="Orbit",
                                 description="The bony cavity of the skull which contains the eye, anterior portion of the optic nerve, ocular muscles and ocular adnexa. Seven bones contribute to the structure of the orbit: the frontal, maxillary, zygomatic, sphenoid, lacrimal, ethmoid, and palatine bones.",
                                 meaning=NCIT.C12347)
    Ovary = PermissibleValue(text="Ovary",
                                 description="One of the paired female reproductive glands containing the ova or germ cells; the ovary's stroma is a vascular connective tissue containing numbers of ovarian follicles enclosing the ova.",
                                 meaning=NCIT.C12404)
    Pancreas = PermissibleValue(text="Pancreas",
                                       description="An organ behind the lower part of the stomach that is the shape of a fish and about the size of a hand. It is a compound gland composed of both exocrine and endocrine tissues. The endocrine pancreas makes insulin so that the body can use glucose (sugar) for energy. The exocrine pancreas makes enzymes that help the body digest food. Spread all over the pancreas are areas called the Islets of Langerhans. The cells in these areas each have a special purpose. The alpha cells make glucagon, which raises the level of glucose in the blood; the beta cells make insulin; the delta cells make somatostatin. There are also PP cells and D1 cells, about which little is known.",
                                       meaning=NCIT.C12393)
    Paratesticular = PermissibleValue(text="Paratesticular",
                                                   description="A small anatomical compartment that contains the testicular collecting system, and mesothelial and mesenchymal components that represent extensions of the abdominal cavity and retroperitoneum.",
                                                   meaning=NCIT.C162491)
    Patella = PermissibleValue(text="Patella",
                                     description="A small flat triangular bone in front of the knee that articulates with the femur and protects the knee joint.",
                                     meaning=NCIT.C33282)
    Pelvis = PermissibleValue(text="Pelvis",
                                   description="The bony, basin-shaped structure formed by the hipbones and the base of the backbone supporting the lower limbs in humans.",
                                   meaning=NCIT.C12767)
    Penis = PermissibleValue(text="Penis",
                                 description="The male organ of urination and copulation.",
                                 meaning=NCIT.C12409)
    Peritoneum = PermissibleValue(text="Peritoneum",
                                           description="The tissue that lines the wall of the abdominal cavity, intestine, mesentery, and pelvic organs. It consists of the parietal peritoneum and the visceral peritoneum.",
                                           meaning=NCIT.C12770)
    Pleural = PermissibleValue(text="Pleural",
                                     description="The tissue that lines the wall of the thoracic cavity and the surface of the lungs.",
                                     meaning=NCIT.C12469)
    Radius = PermissibleValue(text="Radius",
                                   description="The long bone of the forearm that extends from the lateral aspect of the elbow to the thumb-side of the wrist.",
                                   meaning=NCIT.C12777)
    Rectum = PermissibleValue(text="Rectum",
                                   description="The terminal portion of the gastrointestinal tract, extending from the rectosigmoid junction to the anal canal.",
                                   meaning=NCIT.C12390)
    Retroperitoneum = PermissibleValue(text="Retroperitoneum",
                                                     description="The back of the abdomen where the kidneys lie and the great blood vessels run.",
                                                     meaning=NCIT.C12298)
    Rib = PermissibleValue(text="Rib",
                             description="Any one of the paired bones, 12 on either side, extending from the thoracic vertebrae toward the median line on the ventral aspect of the trunk. The long curved bones which form the rib cage. Generally, ribs 1 to 7 are connected to the sternum by their costal cartilages and are called true ribs, whereas ribs 8 to 12 are termed false ribs.",
                             meaning=NCIT.C12782)
    Sacrum = PermissibleValue(text="Sacrum",
                                   description="The triangular bone, made up of 5 fused bones of the spine, located in the lower area of the spine between the fifth lumbar vertebra and the coccyx.",
                                   meaning=NCIT.C33508)
    Spine = PermissibleValue(text="Spine",
                                 description="A series of bones, muscles, tendons, and other tissues reaching from the base of the skull to the tailbone. The vertebral column forms the axis of the skeleton and encloses as well as protects the spinal cord and the fluid surrounding the spinal cord.",
                                 meaning=NCIT.C12998)
    Spleen = PermissibleValue(text="Spleen",
                                   description="An organ that is part of the hematopoietic and immune systems. It is composed of the white pulp and the red pulp and is surrounded by a capsule. It is located in the left hypochondriac region. Its functions include lymphocyte production, blood cell storage, and blood cell destruction.",
                                   meaning=NCIT.C12432)
    Sternum = PermissibleValue(text="Sternum",
                                     description="The long, flat bone connecting with the cartilages of the first seven ribs and the clavicle.",
                                     meaning=NCIT.C12793)
    Stomach = PermissibleValue(text="Stomach",
                                     description="An organ located under the diaphragm, between the liver and the spleen as well as between the esophagus and the small intestine. The stomach is the primary organ of food digestion.",
                                     meaning=NCIT.C12391)
    Tarsus = PermissibleValue(text="Tarsus",
                                   description="Any one of the seven bones forming the instep of the foot.",
                                   meaning=NCIT.C12412)
    Testes = PermissibleValue(text="Testes",
                                   description="Either of the paired male reproductive glands that produce the male germ cells and the male hormones.",
                                   meaning=NCIT.C12412)
    Thigh = PermissibleValue(text="Thigh",
                                 description="A part of the lower limb, located between hip and knee.",
                                 meaning=NCIT.C33763)
    Thyroid = PermissibleValue(text="Thyroid",
                                     description="An endocrine gland located at the base of the neck that produces and secretes thyroxine and other hormones. Thyroxine is important for metabolic control.",
                                     meaning=NCIT.C12400)
    Tibia = PermissibleValue(text="Tibia",
                                 description="One of the terminal digits of the foot.",
                                 meaning=NCIT.C33788)
    Tonsil = PermissibleValue(text="Tonsil",
                                   description="The two organs situated in the throat on either side of the narrow passage from the mouth to the pharynx. They are composed of lymphoid tissues.",
                                   meaning=NCIT.C12802)
    Ulna = PermissibleValue(text="Ulna",
                               description="One of the bones that comprise the forearm. The largest aspect articulates with the humerus at the elbow joint and the smallest portion of the ulna articulates with the carpal bones in the wrist.",
                               meaning=NCIT.C12809)
    Ureter = PermissibleValue(text="Ureter",
                                   description="The thick-walled tube that carries urine from each kidney to the bladder.",
                                   meaning=NCIT.C12416)
    Uterus = PermissibleValue(text="Uterus",
                                   description="A hollow, thick-walled, muscular organ located within the pelvic cavity of a woman. Within the uterus the fertilized egg implants and the fetus develops during pregnancy.",
                                   meaning=NCIT.C12405)
    Vagina = PermissibleValue(text="Vagina",
                                   description="The female genital canal, extending from the uterus to the vulva.",
                                   meaning=NCIT.C12407)
    Viscera = PermissibleValue(text="Viscera",
                                     description="Two or more internal organs.",
                                     meaning=NCIT.C28287)
    Vulva = PermissibleValue(text="Vulva",
                                 description="The external, visible part of the female genitalia surrounding the urethral and vaginal opening. The vulva includes the clitoris and inner as well as outer labia.",
                                 meaning=NCIT.C12408)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="ProcedureSiteEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Abdominal Wall",
                PermissibleValue(text="Abdominal Wall",
                                 description="The upper leg bone positioned between the pelvis and the knee.",
                                 meaning=NCIT.C12717) )
        setattr(cls, "Ankle Joint",
                PermissibleValue(text="Ankle Joint",
                                 description="A gliding joint between the distal ends of the tibia and fibula and the proximal end of the talus.",
                                 meaning=NCIT.C32078) )
        setattr(cls, "Axillary Nodes",
                PermissibleValue(text="Axillary Nodes",
                                 description="One of approximately 20-30 lymph nodes in chain formation that traverse the concavity of the underarm to the clavicle.",
                                 meaning=NCIT.C12904) )
        setattr(cls, "Bone Face",
                PermissibleValue(text="Bone Face",
                                 description="Any bone that contributes to the facial structures, except those bones that are part of the braincase.",
                                 meaning=NCIT.C63706) )
        setattr(cls, "Bone Foot",
                PermissibleValue(text="Bone Foot",
                                 description="One of the seven tarsal, five metatarsal, or 14 phalangeal bones in the foot.",
                                 meaning=NCIT.C13068) )
        setattr(cls, "Bone Marrow",
                PermissibleValue(text="Bone Marrow",
                                 description="The tissue occupying the spaces of bone. It consists of blood vessel sinuses and a network of hematopoietic cells which give rise to the red cells, white cells, and megakaryocytes.",
                                 meaning=NCIT.C12431) )
        setattr(cls, "Bone Shoulder Girdle",
                PermissibleValue(text="Bone Shoulder Girdle",
                                 description="The bony arch formed by the collarbones and shoulder blades.",
                                 meaning=NCIT.C33547) )
        setattr(cls, "Celiac Nodes",
                PermissibleValue(text="Celiac Nodes",
                                 description="A lymph node at the base of the celiac artery.",
                                 meaning=NCIT.C65166) )
        setattr(cls, "Cervical Nodes",
                PermissibleValue(text="Cervical Nodes",
                                 description="Any of the lymph nodes located in the neck.",
                                 meaning=NCIT.C32298) )
        setattr(cls, "Cervical Spine",
                PermissibleValue(text="Cervical Spine",
                                 description="The set of vertebrae immediately caudal to the skull.",
                                 meaning=NCIT.C69313) )
        setattr(cls, "Chest Wall",
                PermissibleValue(text="Chest Wall",
                                 description="The total system of structures outside the lungs that move as a part of breathing; it includes all structures from the skin to the parietal pleura.",
                                 meaning=NCIT.C62484) )
        setattr(cls, "Dorsal Spine",
                PermissibleValue(text="Dorsal Spine",
                                 description="A spinal curve that originates at the middle of the second thoracic vertebra and terminates at the middle of the last thoracic vertebra.",
                                 meaning=NCIT.C32472) )
        setattr(cls, "Elbow Joint",
                PermissibleValue(text="Elbow Joint",
                                 description="A type of hinge joint located between the forearm and upper arm.",
                                 meaning=NCIT.C32497) )
        setattr(cls, "Epitrochlear or Brachial Nodes",
                PermissibleValue(text="Epitrochlear or Brachial Nodes",
                                 description="A lymph node located above and adjacent to the elbow.",
                                 meaning=NCIT.C98182) )
        setattr(cls, "Ethmoid Bone",
                PermissibleValue(text="Ethmoid Bone",
                                 description="A light and spongy bone that is cubical in shape. This bone is positioned at the anterior part of the cranium, sitting between the two orbits, at the roof of the nose. It consists of four parts: a horizontal or cribriform plate; a perpendicular plate; and two lateral masses or labyrinths.",
                                 meaning=NCIT.C12711) )
        setattr(cls, "Fallopian Tube",
                PermissibleValue(text="Fallopian Tube",
                                 description="One of a pair of tubes that extend from the uterus to each of the ovaries. Following ovulation the egg travels down the fallopian tube to the uterus where fertilization may or may not occur.",
                                 meaning=NCIT.C12403) )
        setattr(cls, "Foot Joint",
                PermissibleValue(text="Foot Joint",
                                 description="A bone of the foot.",
                                 meaning=NCIT.C52772) )
        setattr(cls, "Gastrointestinal Tract",
                PermissibleValue(text="Gastrointestinal Tract",
                                 description="The upper gastrointestinal (GI) tract is comprised of mouth, pharynx, esophagus and stomach while the lower GI tract consists of intestines and anus. The primary function of the GI tract is to ingest, digest, absorb and ultimately excrete food stuff.",
                                 meaning=NCIT.C34082) )
        setattr(cls, "Hand Bone",
                PermissibleValue(text="Hand Bone",
                                 description="A bone of the hand.",
                                 meaning=NCIT.C52771) )
        setattr(cls, "Hand Phalanges",
                PermissibleValue(text="Hand Phalanges",
                                 description="The hinge synovial joints between the phalanges of the fingers.",
                                 meaning=NCIT.C32868) )
        setattr(cls, "Head and Neck",
                PermissibleValue(text="Head and Neck",
                                 description="For oncology, an area of the body generally construed to comprise the base of skull and facial bones, sinuses, orbits, salivary glands, oral cavity, oropharynx, larynx, thyroid, facial and neck musculature and lymph nodes draining these areas.",
                                 meaning=NCIT.C12418) )
        setattr(cls, "Hilar Nodes",
                PermissibleValue(text="Hilar Nodes",
                                 description="A pathologic finding about one or more characteristics of perihilar bile duct cancer, following the rules of the TNM AJCC v8 classification system as they pertain to staging of regional lymph nodes.",
                                 meaning=NCIT.C134731) )
        setattr(cls, "Iliac Crest",
                PermissibleValue(text="Iliac Crest",
                                 description="The broad, dorsal, upper, and widest of the three principal bones composing either half of the pelvis.",
                                 meaning=NCIT.C32765) )
        setattr(cls, "Inferior Limb",
                PermissibleValue(text="Inferior Limb",
                                 description="A bone of the leg (lower extremity).",
                                 meaning=NCIT.C12982) )
        setattr(cls, "Infraclavicular Nodes",
                PermissibleValue(text="Infraclavicular Nodes",
                                 description="A lymph node located in the area below the clavicle.",
                                 meaning=NCIT.C63705) )
        setattr(cls, "Inguinal or Femoral Nodes",
                PermissibleValue(text="Inguinal or Femoral Nodes",
                                 description="A superficial or deep lymph node located in the inguinal area.",
                                 meaning=NCIT.C32801) )
        setattr(cls, "Knee Joint",
                PermissibleValue(text="Knee Joint",
                                 description="A joint connecting the lower part of the femur with the upper part of the tibia. The lower part of the femur and the upper part of the tibia are attached to each other by ligaments. Other structures of the knee joint include the upper part of the fibula, located below and parallel to the tibia, and the patella which moves as the knee bends.",
                                 meaning=NCIT.C32898) )
        setattr(cls, "Large Vessels",
                PermissibleValue(text="Large Vessels",
                                 description="Any of the major arteries or veins attached to the cardiac atria or ventricles. This includes the aorta, superior and inferior vena cava and the pulmonary arteries and veins.",
                                 meaning=NCIT.C102955) )
        setattr(cls, "Lower Limb",
                PermissibleValue(text="Lower Limb",
                                 description="The limb that is composed of the hip, thigh, leg and foot.",
                                 meaning=NCIT.C12742) )
        setattr(cls, "Lumber Spine",
                PermissibleValue(text="Lumber Spine",
                                 description="Those vertebrae between the ribs and the pelvis, L1-L5 in man.",
                                 meaning=NCIT.C69314) )
        setattr(cls, "Mesenteric Nodes",
                PermissibleValue(text="Mesenteric Nodes",
                                 description="A lymph node located in the mesentery.",
                                 meaning=NCIT.C77641) )
        setattr(cls, "Nasal Septum",
                PermissibleValue(text="Nasal Septum",
                                 description="The thin wall between the two nasal cavities.",
                                 meaning=NCIT.C33160) )
        setattr(cls, "Oral Cavity",
                PermissibleValue(text="Oral Cavity",
                                 description="The cavity located at the upper end of the alimentary canal, behind the teeth and gums that is bounded on the outside by the lips, above by the hard and soft palates and below by the tongue.",
                                 meaning=NCIT.C12421) )
        setattr(cls, "Para-aortic Lymph Nodes",
                PermissibleValue(text="Para-aortic Lymph Nodes",
                                 description="A lymph node located adjacent to the lumbar region of the spine.",
                                 meaning=NCIT.C77643) )
        setattr(cls, "Pectoral Nodes",
                PermissibleValue(text="Pectoral Nodes",
                                 description="An axillary lymph node located along the lower edge of the pectoralis minor.",
                                 meaning=NCIT.C120322) )
        setattr(cls, "Popliteal Nodes",
                PermissibleValue(text="Popliteal Nodes",
                                 description="Lymph node located within the fat layer of the knee joint.",
                                 meaning=NCIT.C53146) )
        setattr(cls, "Pre-auricular Nodes",
                PermissibleValue(text="Pre-auricular Nodes",
                                 description="A lymph node located anterior to the auricle of the ear.",
                                 meaning=NCIT.C103429) )
        setattr(cls, "Salivary Gland",
                PermissibleValue(text="Salivary Gland",
                                 description="An exocrine gland that secretes saliva. Salivary glands are mostly located in and around the oral cavity.",
                                 meaning=NCIT.C12426) )
        setattr(cls, "Shoulder Girdle",
                PermissibleValue(text="Shoulder Girdle",
                                 description="The bony arch formed by the collarbones and shoulder blades.",
                                 meaning=NCIT.C33547) )
        setattr(cls, "Shoulder Joint",
                PermissibleValue(text="Shoulder Joint",
                                 description="A ball-and-socket joint at the upper end of the humerus, located at the junction of humerus and scapula.",
                                 meaning=NCIT.C33548) )
        setattr(cls, "Skull and Face Bone",
                PermissibleValue(text="Skull and Face Bone",
                                 description="The section of the intestines between the pylorus and cecum. The small intestine is approximately 20 feet long and consists of the duodenum, the jejunum, and the ileum. Its main function is to absorb nutrients from food as the food is transported to the large intestine.",
                                 meaning=NCIT.C12386) )
        setattr(cls, "Small Intestines",
                PermissibleValue(text="Small Intestines",
                                 description="The section of the intestines between the pylorus and cecum. The small intestine is approximately 20 feet long and consists of the duodenum, the jejunum, and the ileum. Its main function is to absorb nutrients from food as the food is transported to the large intestine.",
                                 meaning=NCIT.C12386) )
        setattr(cls, "Splenic Hilar Nodes",
                PermissibleValue(text="Splenic Hilar Nodes",
                                 description="A lymph node located in the hilar region of the spleen.",
                                 meaning=NCIT.C33600) )
        setattr(cls, "Superior Maxilla",
                PermissibleValue(text="Superior Maxilla",
                                 meaning=NCIT.C33682) )
        setattr(cls, "Supraclavicular Nodes",
                PermissibleValue(text="Supraclavicular Nodes",
                                 description="A lymph node which is located above the clavicle.",
                                 meaning=NCIT.C12903) )
        setattr(cls, "Upper Arm",
                PermissibleValue(text="Upper Arm",
                                 description="The portion of the upper extremity between the shoulder and the elbow. For clinical purposes this term is also used to refer to the whole superior limb.",
                                 meaning=NCIT.C32141) )
        setattr(cls, "Upper Limb",
                PermissibleValue(text="Upper Limb",
                                 description="The region of the body that includes the arm, the forearm, and hand.",
                                 meaning=NCIT.C12671) )
        setattr(cls, "Wrist Joint",
                PermissibleValue(text="Wrist Joint",
                                 description="A joint between the distal end of the radius and the proximal row of carpal bones.",
                                 meaning=NCIT.C33894) )
        setattr(cls, "Waldeyer's Ring",
                PermissibleValue(text="Waldeyer's Ring",
                                 description="The ring of lymphoid tissue located in the pharynx, consisting of the pharyngeal, tubal, palatine, and lingual tonsils.",
                                 meaning=NCIT.C73468) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class ProcedureLateralityEnum(EnumDefinitionImpl):

    Left = PermissibleValue(text="Left",
                               description="A finding indicating the tumor location is on the left side of the specimen.",
                               meaning=NCIT.C160200)
    Right = PermissibleValue(text="Right",
                                 description="A finding indicating the tumor location is on the right side of the specimen.",
                                 meaning=NCIT.C160199)
    Bilateral = PermissibleValue(text="Bilateral",
                                         description="A finding indicating the tumor location is on the both sides of the specimen.",
                                         meaning=NCIT.C160201)
    Midline = PermissibleValue(text="Midline",
                                     description="A finding indicating the tumor location is on the midline of the specimen.",
                                     meaning=NCIT.C162614)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="ProcedureLateralityEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class ProcedureTypeEnum(EnumDefinitionImpl):

    Surgery = PermissibleValue(text="Surgery",
                                     description="A diagnostic or treatment procedure performed by manual and/or instrumental means, often involving an incision and the removal or replacement of a diseased organ or tissue; of or relating to or involving or used in surgery or requiring or amenable to treatment by surgery.",
                                     meaning=NCIT.C15329)
    Biopsy = PermissibleValue(text="Biopsy",
                                   description="The removal of tissue specimens or fluid from the living body for microscopic examination, performed to establish a diagnosis.",
                                   meaning=NCIT.C15189)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="ProcedureTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Fine Needle Aspiration",
                PermissibleValue(text="Fine Needle Aspiration",
                                 description="The removal of tissue or fluid with a thin needle for examination under a microscope.",
                                 meaning=NCIT.C15361) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class SurgeryTypeLimbEnum(EnumDefinitionImpl):

    Amputation = PermissibleValue(text="Amputation",
                                           description="The surgical removal of all or part of a limb or other appendage.",
                                           meaning=NCIT.C15179)
    Excision = PermissibleValue(text="Excision",
                                       description="The surgical removal of a lesion, often as part of a biopsy and with healthy margins.",
                                       meaning=NCIT.C15232)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="SurgeryTypeLimbEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Limb-salvage",
                PermissibleValue(text="Limb-salvage",
                                 description="A procedure to avoid amputation of an arm or leg.",
                                 meaning=NCIT.C16042) )
        setattr(cls, "Wide Resection",
                PermissibleValue(text="Wide Resection",
                                 description="Surgery to cut out the cancer and some healthy tissue around it.",
                                 meaning=NCIT.C94441) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class AmputationTypeEnum(EnumDefinitionImpl):

    Disarticulation = PermissibleValue(text="Disarticulation",
                                                     description="The surgical separation of bones at a joint.",
                                                     meaning=NCIT.C175012)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="AmputationTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Amputation - Through Involved Bone",
                PermissibleValue(text="Amputation - Through Involved Bone",
                                 description="The surgical removal of all or part of a limb or other appendage.",
                                 meaning=NCIT.C15179) )
        setattr(cls, "Amputation - Proximal to Involved Bone",
                PermissibleValue(text="Amputation - Proximal to Involved Bone",
                                 description="A procedure to avoid amputation of an arm or leg.",
                                 meaning=NCIT.C16042) )
        setattr(cls, "Internal Hemipelvectomy",
                PermissibleValue(text="Internal Hemipelvectomy",
                                 description="Unilateral removal of the pelvic girdle by resecting the innominate bone while preserving the ipsilateral limb.",
                                 meaning=NCIT.C175013) )
        setattr(cls, "External Hemipelvectomy",
                PermissibleValue(text="External Hemipelvectomy",
                                 description="Unilateral removal of the pelvic girdle by resection of the innominate bone plus amputation of the ipsilateral limb.",
                                 meaning=NCIT.C175014) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class ResectionTypeEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="ResectionTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Intra-Articular Resection",
                PermissibleValue(text="Intra-Articular Resection",
                                 description="A resection performed within a joint.",
                                 meaning=NCIT.C175015) )
        setattr(cls, "Extra-Articular Resection",
                PermissibleValue(text="Extra-Articular Resection",
                                 description="A resection that is done outside the joint.",
                                 meaning=NCIT.C175016) )
        setattr(cls, "Intercalary Resection",
                PermissibleValue(text="Intercalary Resection",
                                 description="A resection of a diaphyseal segment with the goal of preserving adjacent joints. This may include portions of the metaphysis and/or epiphysis depending on the extent of disease.",
                                 meaning=NCIT.C175017) )
        setattr(cls, "Internal Hemipelvectomy",
                PermissibleValue(text="Internal Hemipelvectomy",
                                 description="Unilateral removal of the pelvic girdle by resecting the innominate bone while preserving the ipsilateral limb.",
                                 meaning=NCIT.C175013) )
        setattr(cls, "Not reported",
                PermissibleValue(text="Not reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class SurgeryTypeLimbSalvageEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="SurgeryTypeLimbSalvageEnum",
    )

class ReconstructionTypeEnum(EnumDefinitionImpl):

    Endoprosthetic = PermissibleValue(text="Endoprosthetic",
                                                   description="An artificial device inserted to replace a missing part.",
                                                   meaning=NCIT.C175018)
    Arthrodesis = PermissibleValue(text="Arthrodesis",
                                             description="Surgical fixation or immobilization of a joint, performed to allow bones to fuse or join together.",
                                             meaning=NCIT.C52007)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="ReconstructionTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Osteoarticular Allograft",
                PermissibleValue(text="Osteoarticular Allograft",
                                 description="Grafting bone and cartilage that has been obtained from an individual of the same species as the intended recipient.",
                                 meaning=NCIT.C175019) )
        setattr(cls, "Intercalary Allograft",
                PermissibleValue(text="Intercalary Allograft",
                                 description="Grafting a segment of long bone that is obtained from an individual of the same species as the intended recipient.",
                                 meaning=NCIT.C175020) )
        setattr(cls, "Allograft-Prosthetic",
                PermissibleValue(text="Allograft-Prosthetic",
                                 description="Grafting a composite of an allograft and a prosthetic device.",
                                 meaning=NCIT.C175021) )
        setattr(cls, "Non-Vascularized Autograft",
                PermissibleValue(text="Non-Vascularized Autograft",
                                 description="Harvesting a graft from the intended recipient that has no attached blood supply.",
                                 meaning=NCIT.C175022) )
        setattr(cls, "Vascularized Autograft",
                PermissibleValue(text="Vascularized Autograft",
                                 description="Harvesting a graft from the intended recipient that has attached blood supply.",
                                 meaning=NCIT.C175023) )
        setattr(cls, "Allograft + Vascularized Autograft",
                PermissibleValue(text="Allograft + Vascularized Autograft",
                                 description="The combination of a bone graft from a donor of the same species and a graft from the intended recipient that has attached arteries and veins.",
                                 meaning=NCIT.C175024) )
        setattr(cls, "Vascularized Autograft Endoprosthetic Composite",
                PermissibleValue(text="Vascularized Autograft Endoprosthetic Composite",
                                 description="The combination of a graft from the intended recipient that has attached arteries and veins and a prosthetic device intended for implant.",
                                 meaning=NCIT.C175025) )
        setattr(cls, "No Reconstruction",
                PermissibleValue(text="No Reconstruction",
                                 description="There was no surgical reconstruction performed.",
                                 meaning=NCIT.C175026) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class ProcedureExtentEnum(EnumDefinitionImpl):

    Equivocal = PermissibleValue(text="Equivocal",
                                         description="A laboratory test result that indicates that a specific disease, condition, or attribute being assessed is not clearly present or absent.",
                                         meaning=NCIT.C178921)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT["C17649 "])
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="ProcedureExtentEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Gross Total",
                PermissibleValue(text="Gross Total",
                                 description="Surgical removal of an entire visible lesion, with no obvious lesion detected on post-operative evaluation; microscopic residual disease may be present.",
                                 meaning=NCIT.C131672) )
        setattr(cls, "Complete Resection",
                PermissibleValue(text="Complete Resection",
                                 description="Complete clearance of the tumor with histologically proved negative margins.",
                                 meaning=NCIT.C175027) )
        setattr(cls, "Partial Resection",
                PermissibleValue(text="Partial Resection",
                                 description="Surgical removal of a part of a lesion; some portion of the lesion is detectable on post-operative evaluation.",
                                 meaning=NCIT.C131680) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class MarginsEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="MarginsEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "R0 - Complete Resection, Negative Margins",
                PermissibleValue(text="R0 - Complete Resection, Negative Margins",
                                 description="No detectable presence of residual tumor after treatment",
                                 meaning=NCIT.C139578) )
        setattr(cls, "R1 - Complete Resection, Positive Margins",
                PermissibleValue(text="R1 - Complete Resection, Positive Margins",
                                 description="Presence of microscopic residual tumor after treatment.",
                                 meaning=NCIT.C139579) )
        setattr(cls, "R2 - Gross Residual Disease",
                PermissibleValue(text="R2 - Gross Residual Disease",
                                 description="Presence of macroscopic residual tumor after treatment.",
                                 meaning=NCIT.C139580) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class BiopsyTypeEnum(EnumDefinitionImpl):

    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="BiopsyTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Core Needle Biopsy",
                PermissibleValue(text="Core Needle Biopsy",
                                 description="The removal of a tissue sample using a needle with a relatively large diameter, for microscopic examination.",
                                 meaning=NCIT.C15680) )
        setattr(cls, "Incisional Biopsy",
                PermissibleValue(text="Incisional Biopsy",
                                 description="A surgical procedure in which part of a lesion is removed for microscopic examination.",
                                 meaning=NCIT.C15386) )
        setattr(cls, "Excisional Biopsy",
                PermissibleValue(text="Excisional Biopsy",
                                 description="A surgical procedure in which an entire lesion is removed for microscopic examination.",
                                 meaning=NCIT.C15385) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class MetLungMgmtEnum(EnumDefinitionImpl):

    Thoracotomy = PermissibleValue(text="Thoracotomy",
                                             description="A surgical procedure in which an large incision is made into the chest wall, for the purpose of accessing organs inside the thoracic cavity.",
                                             meaning=NCIT.C15337)
    Sternotomy = PermissibleValue(text="Sternotomy",
                                           description="Incision into or through the sternum.",
                                           meaning=NCIT.C25220)
    Pneumonectomy = PermissibleValue(text="Pneumonectomy",
                                                 description="A lymph node located in the area below the clavicle.",
                                                 meaning=NCIT.C63705)
    Lobectomy = PermissibleValue(text="Lobectomy",
                                         description="Surgical removal of a lobe of an organ.",
                                         meaning=NCIT.C15272)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="MetLungMgmtEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Video-Assisted Thoroscopic Surgery",
                PermissibleValue(text="Video-Assisted Thoroscopic Surgery",
                                 description="Thoracic surgery that is aided by the use of a video camera.",
                                 meaning=NCIT.C63704) )
        setattr(cls, "Wedge Resection",
                PermissibleValue(text="Wedge Resection",
                                 description="Surgical removal of a triangular wedge shaped section of tissue.",
                                 meaning=NCIT.C51690) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class LocalizationTechniqueEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="LocalizationTechniqueEnum",
    )

class PelvicInvolvementEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="PelvicInvolvementEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class NumberNodesEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="NumberNodesEnum",
    )

class ProcedurePurposeEnum(EnumDefinitionImpl):

    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)

    _defn = EnumDefinition(
        name="ProcedurePurposeEnum",
    )

class TmpTypeEnum(EnumDefinitionImpl):

    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="TmpTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Exchange Transfusion",
                PermissibleValue(text="Exchange Transfusion",
                                 description="Withdrawn blood is exchanged for other blood or blood components and returned to the subject.",
                                 meaning=NCIT.C173284) )
        setattr(cls, "Therapeutic Apheresis",
                PermissibleValue(text="Therapeutic Apheresis",
                                 description="Withdrawal of blood from a subject and removal of any pathogenic components before returning the remainder to the subject.",
                                 meaning=NCIT.C173286) )
        setattr(cls, "Simple Transfusion",
                PermissibleValue(text="Simple Transfusion",
                                 description="Transfusion of blood into the body without removing any of the patient's blood volume.",
                                 meaning=NCIT.C173285) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class TmpProductEnum(EnumDefinitionImpl):

    RBC = PermissibleValue(text="RBC",
                             description="Red blood cells remaining after separating plasma from human blood, or collected by apheresis.",
                             meaning=NCIT.C133280)
    Platelets = PermissibleValue(text="Platelets",
                                         description="Platelets collected from a single donor and suspended in a specified volume of original plasma.",
                                         meaning=NCIT.C133278)
    WBC = PermissibleValue(text="WBC",
                             description="White blood cells intended as source material for further manufacturing use.",
                             meaning=NCIT.C133281)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="TmpProductEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class TmpProductTypeEnum(EnumDefinitionImpl):

    Random = PermissibleValue(text="Random",
                                   description="Governed by or depending on chance; lacking any definite plan or order or purpose.",
                                   meaning=NCIT.C60702)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)

    _defn = EnumDefinition(
        name="TmpProductTypeEnum",
    )

class CimtTypeEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="CimtTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Donor Lymphocyte Infusion",
                PermissibleValue(text="Donor Lymphocyte Infusion",
                                 description="The infusion of donor lymphocytes following hematopoietic stem cell transplantation for the purpose of augmenting the host immune response or preventing the rejection of the graft.",
                                 meaning=NCIT["C16145 "]) )
        setattr(cls, "Chimeric Antigen Receptor T-cell Therapy",
                PermissibleValue(text="Chimeric Antigen Receptor T-cell Therapy",
                                 description="Treatment that uses T-cells that have been engineered to contain a chimeric antigen receptor (CAR) that specifically targets a particular antigen.",
                                 meaning=NCIT.C126102) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class SctTypeEnum(EnumDefinitionImpl):

    Autologous = PermissibleValue(text="Autologous",
                                           description="Stem cell transfer or transplantation in which the patient is his own donor.",
                                           meaning=NCIT.C16039)
    Allogeneic = PermissibleValue(text="Allogeneic",
                                           description="A clinical treatment in which hematopoietic stem cells (HSCs) are transferred from one genetically dissimilar individual to another.",
                                           meaning=NCIT.C46089)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="SctTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class SctSourceEnum(EnumDefinitionImpl):

    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="SctSourceEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Bone Marrow",
                PermissibleValue(text="Bone Marrow",
                                 description="A procedure to replace diseased or pathologic bone marrow with transplanted healthy bone marrow cells.",
                                 meaning=NCIT.C15194) )
        setattr(cls, "Peripheral Blood",
                PermissibleValue(text="Peripheral Blood",
                                 description="A method of hematopoietic reconstitution utilizing stem cells harvested from the circulating blood of a patient or donor. Peripheral blood stem cell transplantation (PBSCT) is used for the treatment of certain blood disorders, following partial or complete bone marrow ablation, or following high dose chemotherapy or radiation treatment for cancer. Immature circulating blood cells, similar to stem cells in the bone marrow, are removed before treatment. The cells are then given to the patient after treatment to help the bone marrow recover and continue producing healthy blood cells. Transplantation may be autologous (the patient's own blood cells are used), allogeneic (blood cells are donated by someone else), or syngeneic (blood cells are donated by an identical twin).",
                                 meaning=NCIT.C15430) )
        setattr(cls, "Cord Blood",
                PermissibleValue(text="Cord Blood",
                                 description="A therapeutic procedure that involves the transplantation of hematopoietic stem cells collected from the umbilical cord or placenta.",
                                 meaning=NCIT.C15640) )
        setattr(cls, "Mixture of Stem Cells",
                PermissibleValue(text="Mixture of Stem Cells",
                                 description="A mixture of different sources of stem cells.",
                                 meaning=NCIT.C168886) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class SctDonorRelationshipEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="SctDonorRelationshipEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Biological Sibling",
                PermissibleValue(text="Biological Sibling",
                                 description="A person's brother or sister with whom they share a genetic makeup inherited from one or both of their shared biological parents.",
                                 meaning=NCIT.C100809) )
        setattr(cls, "Biological Parent",
                PermissibleValue(text="Biological Parent",
                                 description="The male who supplied the sperm or the female who supplied the egg which resulted in one's conception.",
                                 meaning=NCIT.C166114) )
        setattr(cls, "Biological Relative",
                PermissibleValue(text="Biological Relative",
                                 description="A person related by descent rather than by marriage or law.",
                                 meaning=NCIT.C71384) )
        setattr(cls, "Biologically Unrelated",
                PermissibleValue(text="Biologically Unrelated",
                                 description="A person who is biologically unrelated to another individual.",
                                 meaning=NCIT.C130053) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class HlaMatchEnum(EnumDefinitionImpl):

    Match = PermissibleValue(text="Match",
                                 description="The state when a recipient and their donor have the same alleles for tissue markers. A full match includes HLA-A, HLA-B, HLA-C, and HLA-DRB1. HLA match typing may also include alleles in the HLA-DQ serogroup.",
                                 meaning=NCIT.C129972)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="HlaMatchEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Non-Match",
                PermissibleValue(text="Non-Match",
                                 description="The state when a recipient of a hematopoietic stem cell transplant is not fully matched with their donor for HLA-A, HLA-B, HLA-C, and HLA-DRB1.",
                                 meaning=NCIT.C126298) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Both alleles matched",
                PermissibleValue(text="Both alleles matched",
                                 description="Both alleles match for one HLA locus",
                                 meaning=NCIT.C168821) )
        setattr(cls, "One allele mismatched",
                PermissibleValue(text="One allele mismatched",
                                 description="One allele matches for one HLA locus.",
                                 meaning=NCIT.C168819) )
        setattr(cls, "Two alleles mismatched",
                PermissibleValue(text="Two alleles mismatched",
                                 description="A mismatch exists at both alleles.",
                                 meaning=NCIT.C168820) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class SctConditioningTypeEnum(EnumDefinitionImpl):

    Myeloablative = PermissibleValue(text="Myeloablative",
                                                 description="A conditioning regimen with high doses of chemotherapy or radiation to eliminate host hematopoietic stem cells prior to restitution via transplantation.",
                                                 meaning=NCIT.C131679)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="SctConditioningTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Reduced Intensity Conditioning/Reduced Toxicity Conditioning",
                PermissibleValue(text="Reduced Intensity Conditioning/Reduced Toxicity Conditioning",
                                 description="A method of preparation for stem cell transplant that uses less than standard doses of chemotherapy and radiation prior to the transfer of stem cells, with the goal of providing protection against graft vs. host disease, while simultaneously minimizing the toxic effects of the conditioning treatment.",
                                 meaning=NCIT.C116471) )
        setattr(cls, "Non-Myeloablative",
                PermissibleValue(text="Non-Myeloablative",
                                 description="A modification of the standard method of allogeneic hematopoietic stem cell transplantation developed to allow for the therapy to be extended to a patient population that is unable to tolerate treatment with the conventional procedure due to its toxicity.",
                                 meaning=NCIT.C62714) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class ResponseCategoryEnum(EnumDefinitionImpl):

    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="ResponseCategoryEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Overall Response",
                PermissibleValue(text="Overall Response",
                                 description="An assessment of the overall response of the disease to the therapy.",
                                 meaning=NCIT.C96613) )
        setattr(cls, "Bone Marrow Response",
                PermissibleValue(text="Bone Marrow Response",
                                 description="The response of the bone marrow to the treatment.",
                                 meaning=NCIT.C173307) )
        setattr(cls, "CNS Response",
                PermissibleValue(text="CNS Response",
                                 description="The response of the central nervous system to treatment.",
                                 meaning=NCIT.C168952) )
        setattr(cls, "Myeloid Sarcoma Response",
                PermissibleValue(text="Myeloid Sarcoma Response",
                                 description="The response of the myeloid sarcoma to the treatment.",
                                 meaning=NCIT.C168965) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class TxPriorResponseEnum(EnumDefinitionImpl):

    Chemotherapy = PermissibleValue(text="Chemotherapy",
                                               description="The use of synthetic or naturally-occurring chemicals for the treatment of diseases.",
                                               meaning=NCIT.C15632)
    Chemoradiotherapy = PermissibleValue(text="Chemoradiotherapy",
                                                         description="Chemotherapy combined with immunotherapy. Chemotherapy uses different drugs to kill or slow the growth of cancer cells; immunotherapy uses treatments to stimulate or restore the ability of the immune system to fight cancer.",
                                                         meaning=NCIT.C94251)

    _defn = EnumDefinition(
        name="TxPriorResponseEnum",
    )

class InterimResponseEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="InterimResponseEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Progressive Disease",
                PermissibleValue(text="Progressive Disease",
                                 description="A clinical, pathologic, and/or molecular finding indicating that the course of a disease is worsening in terms of extent or severity.",
                                 meaning=NCIT.C35571) )

class ResponseEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="ResponseEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Complete Remission",
                PermissibleValue(text="Complete Remission",
                                 description="The disappearance of all signs of cancer in response to treatment.",
                                 meaning=NCIT.C4870) )
        setattr(cls, "Non-Response",
                PermissibleValue(text="Non-Response",
                                 description="A response defined as a non-response in the protocol.",
                                 meaning=NCIT.C173526) )
        setattr(cls, "Partial Response",
                PermissibleValue(text="Partial Response",
                                 description="A finding indicating that there is a decrease in the size and the extent of tissue involvement by a malignant tumor in a patient.",
                                 meaning=NCIT.C18058) )
        setattr(cls, "Stable Disease",
                PermissibleValue(text="Stable Disease",
                                 description="Cancer that is neither decreasing nor increasing in extent or severity.",
                                 meaning=NCIT.C18213) )
        setattr(cls, "Progressive Disease",
                PermissibleValue(text="Progressive Disease",
                                 description="A disease process that is increasing in scope or severity.",
                                 meaning=NCIT.C35571) )
        setattr(cls, "Complete Response",
                PermissibleValue(text="Complete Response",
                                 description="The disappearance of all signs of cancer in response to treatment.",
                                 meaning=NCIT.C4870) )
        setattr(cls, "Very Good Partial Response",
                PermissibleValue(text="Very Good Partial Response",
                                 description="Partial response with additional serum and urine M-protein reduction, but not meeting complete response.",
                                 meaning=NCIT.C123618) )
        setattr(cls, "Mixed Response",
                PermissibleValue(text="Mixed Response",
                                 description="An indication that some disease characteristics are improving while others are worsening over time.",
                                 meaning=NCIT.C165202) )
        setattr(cls, "Not Evaluable",
                PermissibleValue(text="Not Evaluable",
                                 description="Unable to be evaluated.",
                                 meaning=NCIT.C62222) )
        setattr(cls, "Not Applicable",
                PermissibleValue(text="Not Applicable",
                                 description="Determination of a value is not relevant in the current context.",
                                 meaning=NCIT.C48660) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class ResponseMethodEnum(EnumDefinitionImpl):

    Imaging = PermissibleValue(text="Imaging",
                                     description="Any technology or method that aids in the visualization of any biological process, cell, tissue or organ for use in screening, diagnosis, surgical procedures or therapy.",
                                     meaning=NCIT.C17369)
    Pathology = PermissibleValue(text="Pathology",
                                         description="The medical science, and specialty practice, concerned with all aspects of disease, but with special reference to the essential nature, causes, and development of abnormal conditions, as well as the structural and functional changes that result from the disease processes. Informally used to mean the result of such an examination.",
                                         meaning=NCIT.C18189)
    PET = PermissibleValue(text="PET",
                             description="A technique for measuring the gamma radiation produced by collisions of electrons and positrons (anti-electrons) within living tissue. In positron emission tomography (PET), a subject is given a dose of a positron-emitting radionuclide attached to a metabolically active substance (for example, 2-fluoro-2-deoxy-D-glucose (FDG), which is similar to a naturally occurring sugar, glucose, with the addition of a radioactive fluorine atom). When living tissue containing the positron emitter is bombarded by electrons, gamma radiation produced by collisions of electrons and positrons is detected by a scanner, revealing in fine detail the tissue location of the metabolically-active substance administered.",
                             meaning=NCIT.C17007)
    Gallium = PermissibleValue(text="Gallium",
                                     description="An element with atomic symbol Ga, atomic number 31, and atomic weight 69.7. A rare silvery (usually trivalent) metallic element; brittle at low temperatures but liquid above room temperature; occurs in trace amounts in bauxite and zinc ores.",
                                     meaning=NCIT.C66798)
    CT = PermissibleValue(text="CT",
                           description="A method of examining structures within the body by scanning them with X rays and using a computer to construct a series of cross-sectional scans along a single axis.",
                           meaning=NCIT.C17204)
    MRI = PermissibleValue(text="MRI",
                             description="Imaging that uses radiofrequency waves and a strong magnetic field rather than x-rays to provide detailed pictures of internal organs and tissues. The technique is valuable for the diagnosis of many pathologic conditions, including cancer, heart and vascular disease, stroke, and joint and musculoskeletal disorders.",
                             meaning=NCIT.C16809)
    Ultrasound = PermissibleValue(text="Ultrasound",
                                           description="High frequency sound, generally with a frequency greater than 20,000 Hz.",
                                           meaning=NCIT.C64384)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="ResponseMethodEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Tumor Marker",
                PermissibleValue(text="Tumor Marker",
                                 description="A substance present in or produced by a tumor or by the host, that can be used for differentiating neoplastic from normal tissue based on measurements in body fluids, secretions, cells, and/or tissues. Markers are used in diagnosis, staging and prognosis of cancer, provide an estimation of tumor burden, and serve for monitoring effects of therapy, detecting recurrence, localization of tumors, and screening in general populations.",
                                 meaning=NCIT.C17220) )
        setattr(cls, "PET-CT",
                PermissibleValue(text="PET-CT",
                                 description="An imaging technique that utilizes positron emission tomography and computed tomography in a single machine.",
                                 meaning=NCIT.C103512) )
        setattr(cls, "PET-MRI",
                PermissibleValue(text="PET-MRI",
                                 description="An imaging technique that utilizes positron emission tomography and magnetic resonance imaging in a single machine.",
                                 meaning=NCIT.C103514) )
        setattr(cls, "X-Ray",
                PermissibleValue(text="X-Ray",
                                 description="A radiographic procedure using the emission of x-rays to form an image of the structure penetrated by the radiation.",
                                 meaning=NCIT.C38101) )
        setattr(cls, "Bone Scan",
                PermissibleValue(text="Bone Scan",
                                 description="A nuclear imaging method used to evaluate pathological bone metabolism.",
                                 meaning=NCIT.C17646) )
        setattr(cls, "Bone Marrow Biopsy",
                PermissibleValue(text="Bone Marrow Biopsy",
                                 description="A biopsy involving the removal of a core tissue containing bone spicules and hematopoietic elements embedded in the marrow stroma. This procedure is done in the hip area mainly for the diagnosis and evaluation of neoplastic and non-neoplastic hematopoietic disorders (e.g. anemias, leukemias, lymphomas) and the evaluation of the spread of solid tumors (e.g. carcinomas, sarcomas) and lymphomas for therapeutic purposes.",
                                 meaning=NCIT.C15193) )
        setattr(cls, "Not Applicable",
                PermissibleValue(text="Not Applicable",
                                 description="Determination of a value is not relevant in the current context.",
                                 meaning=NCIT.C48660) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class ResponseSystemEnum(EnumDefinitionImpl):

    RECIST = PermissibleValue(text="RECIST",
                                   description="Standard parameters to be used when documenting response of solid tumors to treatment; a set of published rules that define when cancer patients improve ("respond"), stay the same ("stable"), or worsen ("progression") during treatments. (from www.recist.com)",
                                   meaning=NCIT.C49164)
    WHO = PermissibleValue(text="WHO",
                             description="A United Nations agency established to coordinate international health activities and to help governments improve health services.",
                             meaning=NCIT.C75419)
    Choi = PermissibleValue(text="Choi",
                               description="A composite set of criteria developed by Choi et al. using imaging techniques in the evaluation of gastrointestinal stromal tumors response to imatinib mesylate treatment. These criteria integrate changes in tumor size and tumor density.",
                               meaning=NCIT.C122394)
    mRECIST = PermissibleValue(text="mRECIST",
                                     description="Modified RECIST criteria for assessment of response in malignant pleural mesothelioma. (Byrne MJ, Nowak AK. Modified RECIST criteria for assessment of response in malignant pleural mesothelioma. Ann Oncol. 2004 Feb;15(2):257-60.)",
                                     meaning=NCIT.C126031)
    PERCIST = PermissibleValue(text="PERCIST",
                                     description="From RECIST to PERCIST: Evolving considerations for PET response criteria in solid tumors. (Wahl RL, Jacene H, Kasamon Y, Lodge MA. From RECIST to PERCIST: Evolving considerations for PET response criteria in solid tumors. J Nucl Med. 2009 May;50 Suppl 1:122S-50S.)",
                                     meaning=NCIT.C126039)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="ResponseSystemEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class BmAnalysisMethodAtResponseEnum(EnumDefinitionImpl):

    Morphology = PermissibleValue(text="Morphology",
                                           description="A light microscopic finding that describes the cellular characteristics and architectural patterns of cell populations in a tissue sample.",
                                           meaning=NCIT.C35867)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="BmAnalysisMethodAtResponseEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Flow Cytometry",
                PermissibleValue(text="Flow Cytometry",
                                 description="A technique for counting, examining and sorting microscopic particles suspended in a stream of fluid.",
                                 meaning=NCIT.C16585) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class MrdMethodEnum(EnumDefinitionImpl):

    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="MrdMethodEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Flow Cytometry",
                PermissibleValue(text="Flow Cytometry",
                                 description="A technique for counting, examining and sorting microscopic particles suspended in a stream of fluid.",
                                 meaning=NCIT.C16585) )
        setattr(cls, "Molecular Real-time Quantitative PCR",
                PermissibleValue(text="Molecular Real-time Quantitative PCR",
                                 description="An application of PCR that measures the products generated during each cycle of the polymerase chain reaction process in order to determine the starting amount of template in the reaction.",
                                 meaning=NCIT.C51962) )
        setattr(cls, "Next Generation Sequencing",
                PermissibleValue(text="Next Generation Sequencing",
                                 description="Technologies that facilitate the rapid determination of the nucleotide sequence of large numbers of strands or segments of DNA or RNA.",
                                 meaning=NCIT.C101293) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class FlowCytometryTypeEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="FlowCytometryTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Leukemia-Associated Immunophenotypes",
                PermissibleValue(text="Leukemia-Associated Immunophenotypes",
                                 description="A technique with leukemia-associated immunophenotypes for counting, examining or sorting microscopic particles suspended in a stream of fluid based on tagging the population of interest with antibody-based reagents.",
                                 meaning=NCIT.C168812) )
        setattr(cls, "Different-From-Normal",
                PermissibleValue(text="Different-From-Normal",
                                 description="The use of flow cytometry to detect whether material or cells in a sample or specimen is sorted differently than a normal control analyte.",
                                 meaning=NCIT.C168956) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class NotreportedUnknownEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="NotreportedUnknownEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "%",
                PermissibleValue(text="%",
                                 description="A unit for expressing a number as a fraction of hundred (on the basis of a rate or proportion per hundred).",
                                 meaning=NCIT.C48570) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class MrdSampleSourceEnum(EnumDefinitionImpl):

    Blood = PermissibleValue(text="Blood",
                                 description="Blood that has not been separated into its various components; blood that has not been modified except for the addition of an anticoagulant.",
                                 meaning=NCIT.C41067)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="MrdSampleSourceEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Bone Marrow",
                PermissibleValue(text="Bone Marrow",
                                 description="The tissue occupying the spaces of bone. It consiRMS of blood vessel sinuses and a network of hematopoietic cells which give rise to the red cells, white cells, and megakaryocytes.",
                                 meaning=NCIT["C12431 "]) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class MrdMolecularMarkersEnum(EnumDefinitionImpl):

    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="MrdMolecularMarkersEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "t(15;17)(q24;q21)",
                PermissibleValue(text="t(15;17)(q24;q21)",
                                 description="A cytogenetic abnormality that involves a translocation between chromosomes 15 and 17.",
                                 meaning=NCIT["C128656 "]) )
        setattr(cls, "t(10;11)(p12;q23) / MLL-MLLT10(AF10)",
                PermissibleValue(text="t(10;11)(p12;q23) / MLL-MLLT10(AF10)",
                                 description="A cytogenetic abnormality that refers to the translocation of chromosome 10p12 with chromosome 11q23. It is associated with acute myeloid leukemia in childhood.",
                                 meaning=NCIT.C132102) )
        setattr(cls, "t(10;11)(p11.2;q23)",
                PermissibleValue(text="t(10;11)(p11.2;q23)",
                                 description="A cytogenetic abnormality that refers to the translocation of the short arm (p11.2) of chromosome 10 and the long arm (q23) of chromosome 11. It is associated with KMT2A (MLL)/ABI1 fusions and acute myeloid leukemia.",
                                 meaning=NCIT.C168758) )
        setattr(cls, "t(1;11)(q21;q23) / MLL-MLLT11(AF1Q)",
                PermissibleValue(text="t(1;11)(q21;q23) / MLL-MLLT11(AF1Q)",
                                 description="A cytogenetic abnormality that refers to the translocation of the long arm (q21) of chromosome 1 and the long arm (q23) of chromosome 11. It is associated with KMT2A (MLL)/MLLT11 (AF1Q) fusions, acute myeloid leukemia and some cases of acute lymphoblastic leukemia.",
                                 meaning=NCIT.C168759) )
        setattr(cls, "t(4;11)(q21;q23) / MLL-MLLT2(AF4)",
                PermissibleValue(text="t(4;11)(q21;q23) / MLL-MLLT2(AF4)",
                                 description="A chromosomal abnormality consisting of the translocation of 4q21 with 11q23.",
                                 meaning=NCIT.C36365) )
        setattr(cls, "t(6;11)(q27;q23) / MLL-MLLT4(AF6)",
                PermissibleValue(text="t(6;11)(q27;q23) / MLL-MLLT4(AF6)",
                                 description="A cytogenetic abnormality that refers to the translocation of the long arm (q27) of chromosome 6 and the long arm (q23) of chromosome 11. It is associated with the development of de novo acute myeloid leukemia.",
                                 meaning=NCIT.C36610) )
        setattr(cls, "t(11;19)(q23;p13) (MLL-ENL)/(MLL-ELL)",
                PermissibleValue(text="t(11;19)(q23;p13) (MLL-ENL)/(MLL-ELL)",
                                 description="A cytogenetic abnormality that refers to the translocation of the long arm (q23) of chromosome 11 and the short arm (p13) of chromosome 19. It is associated with KMT2A (MLL) fusions, including those with MLLT1 (ENL) and ELL, and acute myeloid leukemia.",
                                 meaning=NCIT.C168764) )
        setattr(cls, "t(11;19)(q23;p13.1) (MLL-ELL)",
                PermissibleValue(text="t(11;19)(q23;p13.1) (MLL-ELL)",
                                 description="A cytogenetic abnormality that refers to the translocation of the long arm (q23) of chromosome 11 and the short arm (p13.1) of chromosome 19. It is associated with the development of acute myeloid leukemia with variant MLL translocations and topoisomerase II inhibitor-related acute myeloid leukemia.",
                                 meaning=NCIT.C36371) )
        setattr(cls, "t(11;19)(q23;p13.3) (MLL-ENL)",
                PermissibleValue(text="t(11;19)(q23;p13.3) (MLL-ENL)",
                                 description="t(11;19)(q23;p13.3)",
                                 meaning=NCIT["C36372 "]) )
        setattr(cls, "Monosomy 7",
                PermissibleValue(text="Monosomy 7",
                                 description="A chromosomal abnormality consisting of the absence of one of the copies of chromosome 7 in somatic cells.",
                                 meaning=NCIT["C36411 "]) )
        setattr(cls, "Monosomy 5",
                PermissibleValue(text="Monosomy 5",
                                 description="A cytogenetic aneuploidy abnormality that refers to the presence of one chromosome 5 only. It is associated with the development of refractory anemia with excess blasts, refractory anemia with multilineage dysplasia, and refractory anemia with multilineage dysplasia and ringed sideroblasts.",
                                 meaning=NCIT["C36523 "]) )
        setattr(cls, "Trisomy 8",
                PermissibleValue(text="Trisomy 8",
                                 description="A chromosomal abnormality consisting of the presence of a third copy of chromosome 8 in somatic cells.",
                                 meaning=NCIT["C36396 "]) )
        setattr(cls, "t(5;11)(q35;p15) NSD1/NUP98",
                PermissibleValue(text="t(5;11)(q35;p15) NSD1/NUP98",
                                 description="A cytogenetic abnormality that refers to the translocation of chromosome 11p15 with chromosome 5q35. It results in the formation of NUP98/NSD1 fusion gene. It is associated with the development of acute myeloid leukemia with t(5;11)(q35;p15); NUP98-NSD1.",
                                 meaning=NCIT.C131503) )
        setattr(cls, "t(7;12)(q36;p13) HLXB9(MNX1)/ETV6(TEL)",
                PermissibleValue(text="t(7;12)(q36;p13) HLXB9(MNX1)/ETV6(TEL)",
                                 description="A chromosomal translocation involving the ETV6 gene on chromosome 12p13 and HLXB9 gene on chromosome 7q36.",
                                 meaning=NCIT.C122689) )
        setattr(cls, "t(3;12)(q23;p12.3)(ETV6/EVI1)",
                PermissibleValue(text="t(3;12)(q23;p12.3)(ETV6/EVI1)",
                                 description="A cytogenetic abnormality that refers to the translocation of the long arm (q23) of chromosome 3 and the shot arm (p12.3) of chromosome 12. It is associated with ETV6/MECOM (EVI1) fusions, myeloproliferative disorders, myelodysplastic syndromes and acute myelogenous leukemia.",
                                 meaning=NCIT.C168766) )
        setattr(cls, "del(5q)(5q31-q32)",
                PermissibleValue(text="del(5q)(5q31-q32)",
                                 description="A cytogenetic abnormality that refers to deletion of chromosome bands 31-32 on the long arm of chromosome 5.",
                                 meaning=NCIT.C168769) )
        setattr(cls, "del(13q) (13q 14 - 21)",
                PermissibleValue(text="del(13q) (13q 14 - 21)",
                                 description="A cytogenetic abnormality that refers to deletion of chromosome bands 14-21 on the long arm of chromosome 13.",
                                 meaning=NCIT.C168770) )
        setattr(cls, "del(17p)",
                PermissibleValue(text="del(17p)",
                                 description="A cytogenetic abnormality that refers to the loss of all or part of the short arm of chromosome 17 (17p).",
                                 meaning=NCIT.C36499) )
        setattr(cls, "non-KMT2A MLLT10",
                PermissibleValue(text="non-KMT2A MLLT10",
                                 description="An indication that a cytogenetic rearrangement involving MLLT10 but not involving KMT2A was detected in a sample.",
                                 meaning=NCIT.C168771) )
        setattr(cls, "inv(16)(p13.3q24.3)/CBFA2T3-GLIS2",
                PermissibleValue(text="inv(16)(p13.3q24.3)/CBFA2T3-GLIS2",
                                 description="A pericentric chromosomal inversion that involves chromosome 16. It is associated with CBFA2T3/GLIS2 fusions and pediatric acute megakaryoblastic leukemia.",
                                 meaning=NCIT.C167195) )
        setattr(cls, "t(11;15)(p15;q35)/NUP98/JARID1A",
                PermissibleValue(text="t(11;15)(p15;q35)/NUP98/JARID1A",
                                 description="A cytogenetic abnormality that refers to the translocation of chromosome 11p15 with chromosome 15q35. It results in the formation of NUP98/JARID1A fusion gene. It is associated with the development of acute myeloid leukemia with t(11;15)(p15;q35); NUP98-JARID1A.",
                                 meaning=NCIT["C131505 "]) )
        setattr(cls, "t(16;21)(q24;q22)RUNX1-CBFA2T3",
                PermissibleValue(text="t(16;21)(q24;q22)RUNX1-CBFA2T3",
                                 description="A cytogenetic abnormality that refers to the translocation of the long arm (q24) of chromosome 16 and the long arm (q22) of chromosome 22. It is associated with RUNX1/CBFA2T3 fusions, myelodysplastic syndromes and acute myeloid leukemia.",
                                 meaning=NCIT.C168773) )
        setattr(cls, "t(3;5)(q25;q34)NPM1/MLF1",
                PermissibleValue(text="t(3;5)(q25;q34)NPM1/MLF1",
                                 description="A cytogenetic abnormality that refers to the translocation of the long arm (q25) of chromosome 3 and the long arm (q34) of chromosome 5. It is associated with the development of acute myeloid leukemia arising from myelodysplastic syndrome, acute myeloid leukemia with multilineage dysplasia, and acute myeloid leukemia with myelodysplasia-related changes.",
                                 meaning=NCIT.C36415) )
        setattr(cls, "t(16;21)(p11;q22)FUS/ERG",
                PermissibleValue(text="t(16;21)(p11;q22)FUS/ERG",
                                 description="A chromosomal translocation involving the FUS gene on chromosome 16p11 and the ERG gene on chromosome 21q22.",
                                 meaning=NCIT["C36616 "]) )
        setattr(cls, "NPM1 mutation",
                PermissibleValue(text="NPM1 mutation",
                                 description="Mutation of the nucleophosmin gene. It is seen in acute myeloid leukemias usually associated with a normal karyotype.",
                                 meaning=NCIT.C82429) )
        setattr(cls, "CEBPA mutation - monoallelic",
                PermissibleValue(text="CEBPA mutation - monoallelic",
                                 description="The presence of mutations in only one allele of the CEBPA gene.",
                                 meaning=NCIT.C168774) )
        setattr(cls, "CEBPA mutation - biallelic",
                PermissibleValue(text="CEBPA mutation - biallelic",
                                 description="The presence of mutations in both alleles of the CEBPA gene.",
                                 meaning=NCIT["C157569 "]) )
        setattr(cls, "CEBPA mutation - mutation unspecified",
                PermissibleValue(text="CEBPA mutation - mutation unspecified",
                                 description="Mutation of the CEBPA gene encoding CCAAT/enhancer binding protein alpha. It is seen in acute myeloid leukemias usually associated with a normal karyotype.",
                                 meaning=NCIT.C38372) )
        setattr(cls, "FLT3 internal tandem duplication",
                PermissibleValue(text="FLT3 internal tandem duplication",
                                 description="A genetic abnormality that arises from duplications of the juxtamembrane portion of the gene and results in constitutive activation of the FLT3 receptor tyrosine kinase protein in early hematopoietic progenitor cells. It is associated with acute myelogenous leukemia where it appears to correlate with a poor prognosis.",
                                 meaning=NCIT["C67494 "]) )
        setattr(cls, "FLT3-TKD",
                PermissibleValue(text="FLT3-TKD",
                                 description="Single nucleotide mutations in the tyrosine kinase domain encoded by the human FLT3 gene that are associated with acute myeloid leukemia and poor prognosis.",
                                 meaning=NCIT.C67495) )
        setattr(cls, "WT1 mutation",
                PermissibleValue(text="WT1 mutation",
                                 description="A change in the nucleotide sequence of the WT1 gene.",
                                 meaning=NCIT["C146726 "]) )
        setattr(cls, "CKIT mutation - ex17",
                PermissibleValue(text="CKIT mutation - ex17",
                                 description="A molecular genetic abnormality indicating the presence of a mutation in exon 17 of the KIT gene located within 4q11-q12.",
                                 meaning=NCIT.C116396) )
        setattr(cls, "CKIT mutation - ex8",
                PermissibleValue(text="CKIT mutation - ex8",
                                 description="A molecular genetic abnormality indicating the presence of a mutation in exon 8 of the KIT gene located within 4q11-q12.",
                                 meaning=NCIT.C128660) )
        setattr(cls, "CKIT mutation - unspecified",
                PermissibleValue(text="CKIT mutation - unspecified",
                                 description="A molecular genetic abnormality that refers to mutation of the c-kit (CD117) proto-oncogene. It is associated with the development of gastrointestinal stromal tumor and gastrointestinal autonomic nerve tumor. It has also been described in acute myeloid leukemias, dysgerminomas, and seminomas.",
                                 meaning=NCIT.C39712) )
        setattr(cls, "GATA1 mutation",
                PermissibleValue(text="GATA1 mutation",
                                 description="A change in the nucleotide sequence of the GATA1 gene.",
                                 meaning=NCIT["C82340 "]) )
        setattr(cls, "RUNX1 mutation",
                PermissibleValue(text="RUNX1 mutation",
                                 description="A change in the nucleotide sequence of the RUNX1 gene.",
                                 meaning=NCIT["C38362 "]) )
        setattr(cls, "PTPN11 mutation",
                PermissibleValue(text="PTPN11 mutation",
                                 description="Mutation of the protein tyrosine phosphatase, non-receptor type 11 gene. It is seen in cases of juvenile myelomonocytic leukemia.",
                                 meaning=NCIT["C82612 "]) )
        setattr(cls, "N-RAS mutation",
                PermissibleValue(text="N-RAS mutation",
                                 description="A change in the structure of the NRAS gene.",
                                 meaning=NCIT["C41381 "]) )
        setattr(cls, "K-RAS mutation",
                PermissibleValue(text="K-RAS mutation",
                                 description="A change in the nucleotide sequence of the KRAS gene.",
                                 meaning=NCIT["C41361 "]) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class AdverseEventEnum(EnumDefinitionImpl):

    Infection = PermissibleValue(text="Infection",
                                         description="The invasion of an organism's body tissues by disease-causing agents and their multiplication, as well as the reaction by the host to these organisms and/or toxins that the organisms produce.",
                                         meaning=NCIT.C128320)
    Typhlitis = PermissibleValue(text="Typhlitis",
                                         description="Inflammation of the cecum, usually accompanied by neutropenia.",
                                         meaning=NCIT.C38043)
    Hyperbilirubinemia = PermissibleValue(text="Hyperbilirubinemia",
                                                           description="Abnormally high level of bilirubin in the blood. Excess bilirubin is associated with jaundice.",
                                                           meaning=NCIT.C27088)
    Hemorrhage = PermissibleValue(text="Hemorrhage",
                                           description="The flow of blood from a ruptured blood vessel.",
                                           meaning=NCIT.C26791)
    Mucositis = PermissibleValue(text="Mucositis",
                                         description="Inflammation of the mucous membranes.",
                                         meaning=NCIT.C115965)
    Neutropenia = PermissibleValue(text="Neutropenia",
                                             description="A decrease in the number of neutrophils in the peripheral blood.",
                                             meaning=NCIT.C80520)
    Thrombocytopenia = PermissibleValue(text="Thrombocytopenia",
                                                       description="A laboratory test result indicating that there is an abnormally small number of platelets in the circulating blood.",
                                                       meaning=NCIT.C3408)
    Neuropathy = PermissibleValue(text="Neuropathy",
                                           description="A disorder affecting the cranial nerves or the peripheral nervous system. It manifests with pain, tingling, numbness, and muscle weakness. It may be the result of physical injury, toxic substances, viral diseases, diabetes, renal failure, cancer, and drugs.",
                                           meaning=NCIT.C4731)
    Fatigue = PermissibleValue(text="Fatigue",
                                     description="Overall tiredness and lack of energy.",
                                     meaning=NCIT.C3036)
    Ototoxicity = PermissibleValue(text="Ototoxicity",
                                             description="Damage to the inner ear as a result of exposure to drugs or chemicals.",
                                             meaning=NCIT.C66929)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="AdverseEventEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Left Ventricular Systolic Dysfunction",
                PermissibleValue(text="Left Ventricular Systolic Dysfunction",
                                 description="The degree of impairment of the left cardiac ventricle to contract efficiently. (ACC)",
                                 meaning=NCIT.C64251) )
        setattr(cls, "Sinusoidal Obstruction Syndrome",
                PermissibleValue(text="Sinusoidal Obstruction Syndrome",
                                 description="A disorder characterized by inflammation and damage of the hepatic sinusoidal endothelial cells of the hepatic venules that leads to venular occlusion and hepatocellular necrosis. It is most often a conditioning-related toxicity that results as a complication of hematopoietic stem cell transplantation (HSCT). It has also been described in populations of individuals who have ingested pyrrolizidine plant alkaloids. The clinical signs and symptoms include hyperbilirubinemia, hepatomegaly, and fluid retention.",
                                 meaning=NCIT.C26793) )
        setattr(cls, "Multi Organ Failure",
                PermissibleValue(text="Multi Organ Failure",
                                 description="Complete impairment of two or more organs or organ systems.",
                                 meaning=NCIT.C75568) )
        setattr(cls, "Neurotoxicity Syndrome",
                PermissibleValue(text="Neurotoxicity Syndrome",
                                 description="A group of neurologic disorders caused by damage to the nervous system following exposure to pharmacologic, biologic, and chemical agents. Examples of neurotoxins include chemotherapy agents, radiation treatment, heavy metals, pesticides, and food additives.",
                                 meaning=NCIT.C27961) )
        setattr(cls, "Graft Versus Host Disease",
                PermissibleValue(text="Graft Versus Host Disease",
                                 description="A reaction, which may be fatal, in an immunocompromised subject (host) who has received an antigenically incompatible tissue transplant (graft) from an immunocompetent donor. The reaction is secondary to the activation of the transplanted cells against those host tissues that express an antigen not expressed by the donor, and is seen most commonly following bone marrow transplantation; acute disease is seen after 5-40 days, and chronic disease occurs weeks to months after transplantation.",
                                 meaning=NCIT.C3063) )
        setattr(cls, "Allergic reaction",
                PermissibleValue(text="Allergic reaction",
                                 description="An immune response that occurs following re-exposure to an innocuous antigen, and that requires the presence of existing antibodies against that antigen. This response involves the binding of IgE to mast cells, and may worsen with repeated exposures.",
                                 meaning=NCIT.C114476) )
        setattr(cls, "Renal Toxicity",
                PermissibleValue(text="Renal Toxicity",
                                 description="Toxicity that impairs or damages the kidney. This condition is often caused by the administration of a pharmaceutical agent that causes damage to the kidney.",
                                 meaning=NCIT.C115459) )
        setattr(cls, "Cardiac Toxicity",
                PermissibleValue(text="Cardiac Toxicity",
                                 description="Toxicity that impairs or damages the heart. This condition is often caused by the administration of a pharmaceutical agent that initiates a poisonous or toxic response in cardiac tissue.",
                                 meaning=NCIT.C27994) )
        setattr(cls, "Pulmonary Toxicity",
                PermissibleValue(text="Pulmonary Toxicity",
                                 description="Toxicity that impairs or damages the lung(s). This condition is often caused by the administration of a pharmaceutical agent that causes damage to the lungs.",
                                 meaning=NCIT.C177374) )
        setattr(cls, "Endocrine toxicity",
                PermissibleValue(text="Endocrine toxicity",
                                 description="Indicates that a toxicity adverse effect has been experienced during endocrine drug treatment.",
                                 meaning=NCIT.C138163) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class AeGradeSystemEnum(EnumDefinitionImpl):

    CTCAE = PermissibleValue(text="CTCAE",
                                 description="A standard terminology developed to report adverse events occurring in cancer clinical trials. Common terminology criteria for adverse events (CTCAE) are used in study adverse event summaries and Investigational New Drug reports to the Food and Drug Administration. The CTCAE contain a grading scale for each adverse event term representing the severity of the event.",
                                 meaning=NCIT.C49704)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="AeGradeSystemEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "European Society for Blood and Marrow Transplantation (EBMT)",
                PermissibleValue(text="European Society for Blood and Marrow Transplantation (EBMT)",
                                 description="A non-profit organization established in 1974 to allow scientiRMS and physicians involved in clinical bone marrow transplantations to share experiences and develop co-operative studies.",
                                 meaning=NCIT.C168842) )
        setattr(cls, "Balis Neuropathy Scale",
                PermissibleValue(text="Balis Neuropathy Scale",
                                 description="An instrument used to grade neurotoxicity occurring in children on a 0-4 scale, where the higher number indicates worse neuropathy.",
                                 meaning=NCIT.C178081) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class AeGradeEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="AeGradeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Grade 1",
                PermissibleValue(text="Grade 1",
                                 description="An experience that is usually transient, and requires no special treatment or intervention. The event does not generally interfere with usual daily activities. Includes transient laboratory test alterations.",
                                 meaning=NCIT.C41338) )
        setattr(cls, "Grade 2",
                PermissibleValue(text="Grade 2",
                                 description="An experience that is alleviated with simple therapeutic treatments. The event impacts usual daily activities. Includes laboratory test alterations indicating injury, but without long-term risk.",
                                 meaning=NCIT.C41339) )
        setattr(cls, "Grade 3",
                PermissibleValue(text="Grade 3",
                                 description="An adverse event experience that requires intensive therapeutic intervention and interrupts usual daily activities.",
                                 meaning=NCIT.C41340) )
        setattr(cls, "Grade 4",
                PermissibleValue(text="Grade 4",
                                 description="Any adverse event that places the patient, in the view of the initial reporter, at immediate risk of death from the adverse event as it occurred, i.e., it does not include an adverse experience that, had it occurred in a more severe form, might have caused death.",
                                 meaning=NCIT.C41337) )
        setattr(cls, "Grade 5",
                PermissibleValue(text="Grade 5",
                                 description="The termination of life associated with an adverse event.",
                                 meaning=NCIT.C48275) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class AeAttributionEnum(EnumDefinitionImpl):

    Definite = PermissibleValue(text="Definite",
                                       description="Definite adverse event attribution to study product or procedure is established when there is a clear-cut temporal association between product or procedure administration and adverse event, and no other possible cause is present.",
                                       meaning=NCIT.C41356)
    Probable = PermissibleValue(text="Probable",
                                       description="Definite adverse event attribution to study product or procedure is established when there is a clear-cut temporal association between product or procedure administration and adverse event, and no other possible cause is present.",
                                       meaning=NCIT.C41356)
    Possible = PermissibleValue(text="Possible",
                                       description="Possible adverse event relationship to study product or procedure is defined when there is less clear temporal association between product or procedure administration and adverse event, and other etiologies of the event are also possible.",
                                       meaning=NCIT.C41359)
    Unlikely = PermissibleValue(text="Unlikely",
                                       description="A characteristic used to qualify the adverse event as unlikely related to the medical intervention. According to WHO causality assessment criteria of suspected adverse reactions it is applicable to a clinical event, including laboratory test abnormality, with a temporal relationship to the medical intervention which makes a causal relationship improbable, and in which other interventions or underlying disease provide plausible explanations.",
                                       meaning=NCIT.C53257)
    Unrelated = PermissibleValue(text="Unrelated",
                                         description="A characteristic used to qualify the adverse event as clearly not related to the medical intervention.",
                                         meaning=NCIT.C53256)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="AeAttributionEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class AeOutcomeEnum(EnumDefinitionImpl):

    Recovered = PermissibleValue(text="Recovered",
                                         description="One of the possible results of an adverse event outcome where the subject recuperated and is free of any pathological conditions resulting from the prior disease or injury.",
                                         meaning=NCIT.C85257)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="AeOutcomeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Death, Contributory",
                PermissibleValue(text="Death, Contributory",
                                 description="Any adverse event contributing to the cause of death.",
                                 meaning=NCIT.C168948) )
        setattr(cls, "Death, Noncontributory",
                PermissibleValue(text="Death, Noncontributory",
                                 description="The adverse event did not directly contribute to the death of the subject.",
                                 meaning=NCIT.C173315) )
        setattr(cls, "Not Yet Recovered",
                PermissibleValue(text="Not Yet Recovered",
                                 description="One of the possible results of an adverse event outcome that indicates that the event has not improved or recuperated.",
                                 meaning=NCIT.C49494) )
        setattr(cls, "Recovered with Sequelae",
                PermissibleValue(text="Recovered with Sequelae",
                                 description="One of the possible results of an adverse event outcome where the subject recuperated but retained pathological conditions resulting from the prior disease or injury.",
                                 meaning=NCIT.C49495) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class AvnJointEnum(EnumDefinitionImpl):

    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="AvnJointEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Ankle (distal tibia, intrinsic ankle bones)",
                PermissibleValue(text="Ankle (distal tibia, intrinsic ankle bones)",
                                 description="A gliding joint between the distal ends of the tibia and fibula and the proximal end of the talus.",
                                 meaning=NCIT.C32078) )
        setattr(cls, "Elbow (distal humerus, proximal radius, proximal ulna)",
                PermissibleValue(text="Elbow (distal humerus, proximal radius, proximal ulna)",
                                 description="A type of hinge joint located between the forearm and upper arm.",
                                 meaning=NCIT.C32497) )
        setattr(cls, "Heel (calcaneus)",
                PermissibleValue(text="Heel (calcaneus)",
                                 description="The rounded back part of the foot below the ankle and behind the arch.",
                                 meaning=NCIT.C161381) )
        setattr(cls, "Hip (proximal femur)",
                PermissibleValue(text="Hip (proximal femur)",
                                 description="A ball-and-socket joint between the head of the femur and the acetabulum.",
                                 meaning=NCIT.C32742) )
        setattr(cls, "Knee (distal femur, proximal tibia)",
                PermissibleValue(text="Knee (distal femur, proximal tibia)",
                                 description="A joint connecting the lower part of the femur with the upper part of the tibia. The lower part of the femur and the upper part of the tibia are attached to each other by ligaments. Other structures of the knee joint include the upper part of the fibula, located below and parallel to the tibia, and the patella which moves as the knee bends.",
                                 meaning=NCIT.C32898) )
        setattr(cls, "Shoulder (proximal humerus)",
                PermissibleValue(text="Shoulder (proximal humerus)",
                                 description="The region of the body between the neck and the upper arm.",
                                 meaning=NCIT.C25203) )
        setattr(cls, "Wrist (distal radius, distal ulna, intrinsic wrist bones)",
                PermissibleValue(text="Wrist (distal radius, distal ulna, intrinsic wrist bones)",
                                 description="A joint between the distal end of the radius and the proximal row of carpal bones.",
                                 meaning=NCIT.C33894) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class AvnJointLateralityEnum(EnumDefinitionImpl):

    Left = PermissibleValue(text="Left",
                               description="Being or located on or directed toward the side of the body to the west when facing north.",
                               meaning=NCIT.C25229)
    Right = PermissibleValue(text="Right",
                                 description="Being or located on or directed toward the side of the body to the east when facing north.",
                                 meaning=NCIT.C25228)
    Bilateral = PermissibleValue(text="Bilateral",
                                         description="Affecting both sides of the body or a matched pair of organs.",
                                         meaning=NCIT.C13332)
    Midline = PermissibleValue(text="Midline",
                                     description="A medial line, especially the medial line or medial plane of the body (or some part of the body).",
                                     meaning=NCIT.C81170)

    _defn = EnumDefinition(
        name="AvnJointLateralityEnum",
    )

class AvnMethodEnum(EnumDefinitionImpl):

    CT = PermissibleValue(text="CT",
                           description="A method of examining structures within the body by scanning them with X rays and using a computer to construct a series of cross-sectional scans along a single axis.",
                           meaning=NCIT.C17204)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)

    _defn = EnumDefinition(
        name="AvnMethodEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Bone Scan",
                PermissibleValue(text="Bone Scan",
                                 description="A nuclear imaging method used to evaluate pathological bone metabolism.",
                                 meaning=NCIT.C17646) )
        setattr(cls, "MRI (NMR)",
                PermissibleValue(text="MRI (NMR)",
                                 description="Imaging that uses radiofrequency waves and a strong magnetic field rather than x-rays to provide detailed pictures of internal organs and tissues. The technique is valuable for the diagnosis of many pathologic conditions, including cancer, heart and vascular disease, stroke, and joint and musculoskeletal disorders.",
                                 meaning=NCIT.C16809) )
        setattr(cls, "X-ray",
                PermissibleValue(text="X-ray",
                                 description="A radiographic procedure using the emission of x-rays to form an image of the structure penetrated by the radiation.",
                                 meaning=NCIT.C38101) )

class OrthopedicProcedureEnum(EnumDefinitionImpl):

    Chondroplasty = PermissibleValue(text="Chondroplasty",
                                                 description="An outpatient procedure to repair damaged cartilage in the knee.",
                                                 meaning=NCIT.C178090)
    Osteotomy = PermissibleValue(text="Osteotomy",
                                         description="Surgical cutting or removal of bone.",
                                         meaning=NCIT.C51903)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)

    _defn = EnumDefinition(
        name="OrthopedicProcedureEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Arthroplasty, Hemi/Resurfacing",
                PermissibleValue(text="Arthroplasty, Hemi/Resurfacing",
                                 description="The trimming and capping of the joint head with ceramic, metal or plastic components and the removal of damaged bone and cartilage within the socket and replacement with a metal shell.",
                                 meaning=NCIT.C178086) )
        setattr(cls, "Arthroplasty, Total",
                PermissibleValue(text="Arthroplasty, Total",
                                 description="The removal of the joint head and neck, and replacement with ceramic, metal or plastic components and the removal of damaged bone and cartilage within the socket and replacement with a metal shell.",
                                 meaning=NCIT.C178087) )
        setattr(cls, "Bone Graft, Free Vascularized",
                PermissibleValue(text="Bone Graft, Free Vascularized",
                                 description="Bone grafts that have their own blood supply.",
                                 meaning=NCIT.C178088) )
        setattr(cls, "Bone Graft, Nonvascularized",
                PermissibleValue(text="Bone Graft, Nonvascularized",
                                 description="Bone grafts without a blood supply.",
                                 meaning=NCIT.C178089) )
        setattr(cls, "Core Decompression",
                PermissibleValue(text="Core Decompression",
                                 description="A surgical procedure in which areas of dead bone are drilled to increase blood flow, slow or stop tissue destruction and decrease pressure.",
                                 meaning=NCIT.C157826) )

class AeExpectedEnum(EnumDefinitionImpl):

    Expected = PermissibleValue(text="Expected",
                                       description="Any adverse event associated with a medical product or procedure, whose nature and severity have been previously observed, identified in nature, severity, or frequency, and documented in the investigator brochure, investigational plan, protocol, current consent form, scientific publication, or in other relevant and reliable document. The old term Side Effect is retired and should not be used.",
                                       meaning=NCIT.C41333)
    Unexpected = PermissibleValue(text="Unexpected",
                                           description="Any adverse event associated with a medical product or procedure that has not been previously observed, whether or not the event was anticipated because of the pharmacologic properties of the study agent or the nature of the medical procedure. This includes events that are more serious than expected or occur more frequently than expected, particularly, any adverse experience, the nature, severity or frequency of which is not consistent with the product label, or with the current investigator brochure for investigational agent; or with the risk information described in the investigational plan or protocol or consent form.",
                                           meaning=NCIT.C41334)

    _defn = EnumDefinition(
        name="AeExpectedEnum",
    )

class AeInterventionDetailEnum(EnumDefinitionImpl):

    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="AeInterventionDetailEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "ACE-Inhibitor",
                PermissibleValue(text="ACE-Inhibitor",
                                 description="Any substance that inhibits angiotensin-converting enzyme (ACE), an enzyme that catalyzes the conversion of angiotensin I to angiotensin II. Inhibition of ACE results in a reduction in angiotensin II and angiotensin II-induced aldosterone secretion, causing vasodilation and natriuresis.",
                                 meaning=NCIT.C247) )
        setattr(cls, "Ionotropic Support",
                PermissibleValue(text="Ionotropic Support",
                                 description="An agent used to modify the strength of the contraction of the heart muscle.",
                                 meaning=NCIT.C168966) )
        setattr(cls, "Heart Transplant",
                PermissibleValue(text="Heart Transplant",
                                 description="A surgical procedure in which a damaged heart is removed and replaced by another heart from a suitable donor.",
                                 meaning=NCIT.C15246) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class AePathogenEnum(EnumDefinitionImpl):

    Bacteria = PermissibleValue(text="Bacteria",
                                       description="Unicellular, prokaryotic organisms that reproduce by cell division and usually have cell walls; can be shaped like spheres, rods or spirals and can be found in virtually any environment.",
                                       meaning=NCIT["C14187 "])
    Virus = PermissibleValue(text="Virus",
                                 description="An infectious agent which consists of two parts, genetic material and a protein coat. These organisms lack independent metabolism, and they must infect the cells of other types of organisms to reproduce. Most viruses are capable of passing through fine filters that retain bacteria, and are not visible through a light microscope.",
                                 meaning=NCIT["C14283 "])
    Fungus = PermissibleValue(text="Fungus",
                                   description="A kingdom of eukaryotic, heterotrophic organisms that live as saprobes or parasites, including mushrooms, yeasts, smuts, molds, etc. They reproduce either sexually or asexually, and have life cycles that range from simple to complex. Filamentous fungi refer to those that grow as multicellular colonies (mushrooms and molds).",
                                   meaning=NCIT["C14209 "])
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="AePathogenEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class AePathogenConfirmationEnum(EnumDefinitionImpl):

    Confirmed = PermissibleValue(text="Confirmed",
                                         description="Having been established or verified.",
                                         meaning=NCIT.C25458)
    Suspected = PermissibleValue(text="Suspected",
                                         description="Believed likely.",
                                         meaning=NCIT.C71458)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="AePathogenConfirmationEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class InfectionClassificationEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="InfectionClassificationEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Clinically Documented",
                PermissibleValue(text="Clinically Documented",
                                 description="Documentation supporting direct medical treatment or testing.",
                                 meaning=NCIT.C178092) )
        setattr(cls, "Microbiologically Documented Non-Sterile Site",
                PermissibleValue(text="Microbiologically Documented Non-Sterile Site",
                                 description="Documentation that supports the site was microbiologically non-sterile.",
                                 meaning=NCIT.C178093) )
        setattr(cls, "Microbiologically Documented Sterile Site",
                PermissibleValue(text="Microbiologically Documented Sterile Site",
                                 description="Documentation that supports the site was microbiologically sterile.",
                                 meaning=NCIT.C178094) )

class GvhdAcuityEnum(EnumDefinitionImpl):

    Acute = PermissibleValue(text="Acute",
                                 description="A syndrome of immunologically mediated tissue damage that may occur following an allogeneic transplant, usually affecting the skin, liver, and GI tract. The onset is usually within one hundred days of transplantation or immunologic manipulation.",
                                 meaning=NCIT.C4980)
    Chronic = PermissibleValue(text="Chronic",
                                     description="A syndrome of immunologically mediated tissue damage that may occur following an allogeneic transplant, and may affect multiple organs with manifestations similar to autoimmune diseases. The onset is usually within three years of transplantation or immunologic manipulation.",
                                     meaning=NCIT.C4981)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="GvhdAcuityEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class GvhdOrganEnum(EnumDefinitionImpl):

    Skin = PermissibleValue(text="Skin",
                               description="An organ that constitutes the external surface of the body. It consiRMS of the epidermis, dermis, and skin appendages.",
                               meaning=NCIT.C12470)
    Liver = PermissibleValue(text="Liver",
                                 description="A triangular-shaped organ located under the diaphragm in the right hypochondrium. It is the largest internal organ of the body, weighting up to 2 kg. Metabolism and bile secretion are its main functions. It is composed of cells which have the ability to regenerate.",
                                 meaning=NCIT.C12392)
    Lung = PermissibleValue(text="Lung",
                               description="One of a pair of viscera occupying the pulmonary cavities of the thorax, the organs of respiration in which aeration of the blood takes place. As a rule, the right lung is slightly larger than the left and is divided into three lobes (an upper, a middle, and a lower or basal), while the left has two lobes (an upper and a lower or basal). Each lung is irregularly conical in shape, presenting a blunt upper extremity (the apex), a concave base following the curve of the diaphragm, an outer convex surface (costal surface), an inner or mediastinal surface (mediastinal surface), a thin and sharp anterior border, and a thick and rounded posterior border.",
                               meaning=NCIT.C12468)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="GvhdOrganEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Gastrointestinal Tract",
                PermissibleValue(text="Gastrointestinal Tract",
                                 description="The upper gastrointestinal (GI) tract is comprised of mouth, pharynx, esophagus and stomach while the lower GI tract consiRMS of intestines and anus. The primary function of the GI tract is to ingest, digest, absorb and ultimately excrete food stuff.",
                                 meaning=NCIT.C34082) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class LeEnum(EnumDefinitionImpl):

    Fatigue = PermissibleValue(text="Fatigue",
                                     description="Overall tiredness and lack of energy.",
                                     meaning=NCIT.C3036)
    Xerostomia = PermissibleValue(text="Xerostomia",
                                           description="Dryness of the oral mucosa secondary to a decrease in saliva production, or a change in saliva composition.",
                                           meaning=NCIT.C26917)

    _defn = EnumDefinition(
        name="LeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Endocrine Disorder",
                PermissibleValue(text="Endocrine Disorder",
                                 description="A non-neoplastic or neoplastic disorder that affects the endocrine system. Representative examples of non-neoplastic disorders include diabetes mellitus, hyperthyroidism, and adrenal gland insufficiency. Representative examples of neoplastic disorders include carcinoid tumor, neuroendocrine carcinoma, and pheochromocytoma.",
                                 meaning=NCIT.C3009) )
        setattr(cls, "Cardiovascular Disorder",
                PermissibleValue(text="Cardiovascular Disorder",
                                 description="A non-neoplastic or neoplastic disorder affecting the heart or the vessels (arteries, veins and lymph vessels). Representative examples of non-neoplastic cardiovascular disorders are endocarditis and hypertension. Representative examples of neoplastic cardiovascular disorders are endocardial myxoma and angiosarcoma.",
                                 meaning=NCIT.C2931) )
        setattr(cls, "Muskuloskeletal Disorder",
                PermissibleValue(text="Muskuloskeletal Disorder",
                                 description="A non-neoplastic or neoplastic disorder that affects muscles and bones.",
                                 meaning=NCIT.C107377) )
        setattr(cls, "Neurological Disorder",
                PermissibleValue(text="Neurological Disorder",
                                 description="A non-neoplastic or neoplastic disorder that affects the brain, spinal cord, or peripheral nerves.",
                                 meaning=NCIT.C26835) )
        setattr(cls, "Pulmonary Disorder",
                PermissibleValue(text="Pulmonary Disorder",
                                 description="A non-neoplastic or neoplastic disorder affecting the lung. Representative examples of non-neoplastic disorders include chronic obstructive pulmonary disease and pneumonia. Representative examples of neoplastic disorders include benign processes (e.g., respiratory papilloma) and malignant processes (e.g., lung carcinoma and metastatic cancer to the lung).",
                                 meaning=NCIT.C3198) )
        setattr(cls, "Breast Hypoplasia",
                PermissibleValue(text="Breast Hypoplasia",
                                 description="Underdevelopment of the breast.",
                                 meaning=NCIT.C78222) )
        setattr(cls, "Dermatologic Disorder",
                PermissibleValue(text="Dermatologic Disorder",
                                 description="Any deviation from the normal structure or function of the skin or subcutaneous tissue that is manifested by a characteristic set of symptoms and signs.",
                                 meaning=NCIT.C3371) )
        setattr(cls, "Genitourinary Disorder",
                PermissibleValue(text="Genitourinary Disorder",
                                 description="A non-neoplastic or neoplastic disorder that affects the genitourinary system.",
                                 meaning=NCIT.C156660) )
        setattr(cls, "Immunologic Disorder",
                PermissibleValue(text="Immunologic Disorder",
                                 description="A disorder resulting from an abnormality in the immune system.",
                                 meaning=NCIT.C3507) )
        setattr(cls, "GI Disorder",
                PermissibleValue(text="GI Disorder",
                                 description="A non-neoplastic or neoplastic disorder that affects the gastrointestinal tract, anus, liver, biliary system, and pancreas.",
                                 meaning=NCIT.C2990) )
        setattr(cls, "Psychiatric Disorder",
                PermissibleValue(text="Psychiatric Disorder",
                                 description="A disorder characterized by behavioral and/or psychological abnormalities, often accompanied by physical symptoms. The symptoms may cause clinically significant distress or impairment in social and occupational areas of functioning. Representative examples include anxiety disorders, cognitive disorders, mood disorders and schizophrenia.",
                                 meaning=NCIT.C2893) )

class LeDetailEnum(EnumDefinitionImpl):

    Arrhythmia = PermissibleValue(text="Arrhythmia",
                                           description="Any variation from the normal rate or rhythm (which may include the origin of the impulse and/or its subsequent propagation) in the heart.",
                                           meaning=NCIT.C2881)
    Pericarditis = PermissibleValue(text="Pericarditis",
                                               description="An inflammatory process affecting the pericardium.",
                                               meaning=NCIT.C34915)
    Hypertension = PermissibleValue(text="Hypertension",
                                               description="Blood pressure that is abnormally high.",
                                               meaning=NCIT.C3117)
    Osteopenia = PermissibleValue(text="Osteopenia",
                                           description="Decreased calcification or density of bone tissue.",
                                           meaning=NCIT.C50910)
    Osteoporosis = PermissibleValue(text="Osteoporosis",
                                               description="A condition of reduced bone mass, with decreased cortical thickness and a decrease in the number and size of the trabeculae of cancellous bone (but normal chemical composition), resulting in increased fracture incidence. Osteoporosis is classified as primary (Type 1, postmenopausal osteoporosis; Type 2, age-associated osteoporosis; and idiopathic, which can affect juveniles, premenopausal women, and middle-aged men) and secondary osteoporosis (which results from an identifiable cause of bone mass loss).",
                                               meaning=NCIT.C3298)
    Scoliosis = PermissibleValue(text="Scoliosis",
                                         description="A congenital or acquired spinal deformity characterized by lateral curvature of the spine.",
                                         meaning=NCIT.C78603)
    Arthritis = PermissibleValue(text="Arthritis",
                                         description="An inflammatory process affecting a joint. Causes include infection, autoimmune processes, degenerative processes, and trauma. Signs and symptoms may include swelling around the affected joint and pain.",
                                         meaning=NCIT.C2883)
    Neuropathy = PermissibleValue(text="Neuropathy",
                                           description="A disorder affecting the cranial nerves or the peripheral nervous system. It manifests with pain, tingling, numbness, and muscle weakness. It may be the result of physical injury, toxic substances, viral diseases, diabetes, renal failure, cancer, and drugs.",
                                           meaning=NCIT.C4731)
    Neurocognitive = PermissibleValue(text="Neurocognitive",
                                                   description="Having to do with the ability to think and reason. This includes the ability to concentrate, remember things, process information, learn, speak, and understand.",
                                                   meaning=NCIT.C94321)
    Stroke = PermissibleValue(text="Stroke",
                                   description="A sudden loss of neurological function secondary to hemorrhage or ischemia in the brain parenchyma due to a vascular event.",
                                   meaning=NCIT.C3390)
    Dryness = PermissibleValue(text="Dryness",
                                     description="The lack of natural or normal moisture.",
                                     meaning=NCIT.C25489)
    Atrophy = PermissibleValue(text="Atrophy",
                                     description="Any weakening or degeneration, especially through lack of use.",
                                     meaning=NCIT.C79748)
    Contraction = PermissibleValue(text="Contraction",
                                             description="Permanent contraction of a muscle as a result of spasm or paralysis.",
                                             meaning=NCIT.C75585)
    Scarring = PermissibleValue(text="Scarring",
                                       description="A permanent mark left on the skin in the process of wound healing.",
                                       meaning=NCIT.C34483)
    Telengectasia = PermissibleValue(text="Telengectasia",
                                                 description="Local dilatation of small vessels resulting in red discoloration of the skin or mucous membranes.",
                                                 meaning=NCIT.C28194)
    Pancreatitis = PermissibleValue(text="Pancreatitis",
                                               description="Inflammation of the pancreas.",
                                               meaning=NCIT.C3306)
    Esophagitis = PermissibleValue(text="Esophagitis",
                                             description="An acute or chronic inflammatory process affecting the esophageal wall.",
                                             meaning=NCIT.C9224)
    Gastritis = PermissibleValue(text="Gastritis",
                                         description="Inflammation of the stomach.",
                                         meaning=NCIT.C26780)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)

    _defn = EnumDefinition(
        name="LeDetailEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Thyroid Disorder",
                PermissibleValue(text="Thyroid Disorder",
                                 description="A non-neoplastic or neoplastic disorder that affects the thyroid gland. Representative examples include hyperthyroidism, hypothyroidism, thyroiditis, follicular adenoma, and carcinoma.",
                                 meaning=NCIT.C26893) )
        setattr(cls, "Gonadal Dysfunction",
                PermissibleValue(text="Gonadal Dysfunction",
                                 description="A non-neoplastic or neoplastic disorder that affects the testis or the ovary.",
                                 meaning=NCIT.C26786) )
        setattr(cls, "Conduction abnormality",
                PermissibleValue(text="Conduction abnormality",
                                 description="A disorder affecting the conduction system that sends electrical signals in the myocardium.",
                                 meaning=NCIT.C78245) )
        setattr(cls, "Valvular Disease",
                PermissibleValue(text="Valvular Disease",
                                 description="Any heart disorder characterized by a defect in valve structure or function.",
                                 meaning=NCIT.C45525) )
        setattr(cls, "Ventricular Dysfunction",
                PermissibleValue(text="Ventricular Dysfunction",
                                 description="Impairment of the ventricle to either fill or eject adequately.",
                                 meaning=NCIT.C111655) )
        setattr(cls, "Vascular Disorder",
                PermissibleValue(text="Vascular Disorder",
                                 description="A non-neoplastic or neoplastic disorder affecting the arteries, veins, or lymphatic vessels. Examples include vasculitis, thrombophlebitis, arteriosclerosis, lymphedema, hemangioma, and angiosarcoma.",
                                 meaning=NCIT.C35117) )
        setattr(cls, "Avascular-Necrosis",
                PermissibleValue(text="Avascular-Necrosis",
                                 description="Tissue death resulting from an interruption to the blood supply.",
                                 meaning=NCIT.C118385) )
        setattr(cls, "Musculoskeletal Hypoplasia",
                PermissibleValue(text="Musculoskeletal Hypoplasia",
                                 description="Underdevelopment or incomplete development of the musculoskeletal system.",
                                 meaning=NCIT.C185696) )
        setattr(cls, "Restrictive Lung Disease",
                PermissibleValue(text="Restrictive Lung Disease",
                                 description="Decreased lung volume and inadequate ventilation due to parenchymal lung disorders (e.g., interstitial pulmonary fibrosis) or extrapulmonary disorders (e.g., scoliosis). Patients present with shortness of breath and cough.",
                                 meaning=NCIT.C91762) )
        setattr(cls, "Obstructive Lung Disease",
                PermissibleValue(text="Obstructive Lung Disease",
                                 description="A chronic and progressive lung disorder characterized by the loss of elasticity of the bronchial tree and the air sacs, destruction of the air sacs wall, thickening of the bronchial wall, and mucous accumulation in the bronchial tree. The pathologic changes result in the disruption of the air flow in the bronchial airways. Signs and symptoms include shortness of breath, wheezing, productive cough, and chest tightness. The two main types of chronic obstructive pulmonary disease are chronic obstructive bronchitis and emphysema.",
                                 meaning=NCIT.C3199) )
        setattr(cls, "Reactive Airway Disease",
                PermissibleValue(text="Reactive Airway Disease",
                                 description="Coughing, wheezing, or shortness of breath that is triggered by allergens, infection, or other irritants.",
                                 meaning=NCIT.C113673) )
        setattr(cls, "Pigment Changes",
                PermissibleValue(text="Pigment Changes",
                                 description="Abnormal skin pigmentation.",
                                 meaning=NCIT.C124224) )
        setattr(cls, "Renal Disorder",
                PermissibleValue(text="Renal Disorder",
                                 description="A neoplastic or non-neoplastic condition affecting the kidney. Representative examples of non-neoplastic conditions include glomerulonephritis and nephrotic syndrome. Representative examples of neoplastic conditions include benign processes (e.g., renal lipoma and renal fibroma) and malignant processes (e.g., renal cell carcinoma and renal lymphoma).",
                                 meaning=NCIT.C3149) )
        setattr(cls, "Bladder Disorder",
                PermissibleValue(text="Bladder Disorder",
                                 description="A non-neoplastic or neoplastic disorder affecting the urinary bladder. A representative example of non-neoplastic bladder disorder is bacterial bladder infection. A representative example of neoplastic bladder disorder is bladder carcinoma.",
                                 meaning=NCIT.C2900) )
        setattr(cls, "Autoimmune Reaction",
                PermissibleValue(text="Autoimmune Reaction",
                                 description="A specific humoral or cell-mediated immune response against autologous (self) antigens.",
                                 meaning=NCIT.C16313) )
        setattr(cls, "Acquired Immunodeficiency",
                PermissibleValue(text="Acquired Immunodeficiency",
                                 description="A syndrome resulting from the acquired deficiency of cellular immunity caused by the human immunodeficiency virus (HIV). It is characterized by the reduction of the Helper T-lymphocytes in the peripheral blood and the lymph nodes. Symptoms include generalized lymphadenopathy, fever, weight loss, and chronic diarrhea. Patients with AIDS are especially susceptible to opportunistic infections (usually pneumocystis carinii pneumonia, cytomegalovirus (CMV) infections, tuberculosis, candida infections, and cryptococcosis), and the development of malignant neoplasms (usually non-Hodgkin lymphoma and Kaposi sarcoma). The human immunodeficiency virus is transmitted through sexual contact, sharing of contaminated needles, or transfusion of contaminated blood.",
                                 meaning=NCIT.C2851) )
        setattr(cls, "GI Adhesions",
                PermissibleValue(text="GI Adhesions",
                                 description="A fibrous connection of tissue that joins together normally separate gastrointestinal regions.",
                                 meaning=NCIT.C185688) )
        setattr(cls, "Hepatic Dysfunction",
                PermissibleValue(text="Hepatic Dysfunction",
                                 description="A finding that indicates abnormal liver function.",
                                 meaning=NCIT.C50634) )

class LeSubDetailEnum(EnumDefinitionImpl):

    Hyperthyroid = PermissibleValue(text="Hyperthyroid",
                                               description="Overactivity of the thyroid gland resulting in overproduction of thyroid hormone and increased metabolic rate. Causes include diffuse hyperplasia of the thyroid gland (Graves' disease), single nodule in the thyroid gland, and thyroiditis. The symptoms are related to the increased metabolic rate and include weight loss, fatigue, heat intolerance, excessive sweating, diarrhea, tachycardia, insomnia, muscle weakness, and tremor.",
                                               meaning=NCIT.C3123)
    Hypothyroid = PermissibleValue(text="Hypothyroid",
                                             description="Abnormally low levels of thyroid hormone.",
                                             meaning=NCIT.C26800)
    Ammenorrhea = PermissibleValue(text="Ammenorrhea",
                                             description="The absence of menses in a woman who has achieved reproductive age.",
                                             meaning=NCIT.C61443)
    Asthma = PermissibleValue(text="Asthma",
                                   description="A chronic respiratory disease manifested as difficulty breathing due to the narrowing of bronchial passageways.",
                                   meaning=NCIT.C28397)
    AKI = PermissibleValue(text="AKI",
                             description="Sudden and sustained deterioration of the kidney function characterized by decreased glomerular filtration rate, increased serum creatinine or oliguria.",
                             meaning=NCIT.C26808)
    AIN = PermissibleValue(text="AIN",
                             description="A condition characterized by the autoantibody-induced destruction of neutrophils.",
                             meaning=NCIT.C176730)
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=NCIT.C17649)

    _defn = EnumDefinition(
        name="LeSubDetailEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Thyroid Nodule",
                PermissibleValue(text="Thyroid Nodule",
                                 description="A nodular lesion that develops in the thyroid gland. Causes include adenoma, thyroiditis, fluid-filled cyst, multinodular goiter, and carcinoma.",
                                 meaning=NCIT.C3415) )
        setattr(cls, "Menstrual Cycle Dysfunction",
                PermissibleValue(text="Menstrual Cycle Dysfunction",
                                 description="A category of conditions related to menses.",
                                 meaning=NCIT.C34815) )
        setattr(cls, "Germ Cell Failure, Suspected",
                PermissibleValue(text="Germ Cell Failure, Suspected",
                                 description="Clinical suspicion for germ cell failure not proven with testing.",
                                 meaning=NCIT.C185684) )
        setattr(cls, "Germ Cell Failure, Confirmed",
                PermissibleValue(text="Germ Cell Failure, Confirmed",
                                 description="A germ cell failure confirmed with testing.",
                                 meaning=NCIT.C185685) )
        setattr(cls, "Testosterone Deficiency",
                PermissibleValue(text="Testosterone Deficiency",
                                 description="A disorder characterized by low testosterone.",
                                 meaning=NCIT.C143195) )
        setattr(cls, "Fertility Disorder",
                PermissibleValue(text="Fertility Disorder",
                                 description="Inability to conceive for at least one year after trying and having unprotected sex. Causes of female infertility include endometriosis, fallopian tubes obstruction, and polycystic ovary syndrome. Causes of male infertility include abnormal sperm production or function, blockage of the epididymis, blockage of the ejaculatory ducts, hypospadias, exposure to pesticides, and health related issues.",
                                 meaning=NCIT.C3836) )
        setattr(cls, "Heart Block",
                PermissibleValue(text="Heart Block",
                                 description="A disorder characterized by an electrocardiographic finding of complete failure of atrial electrical impulse conduction to the ventricles. This is manifested on the ECG by disassociation of atrial and ventricular rhythms. The atrial rate must be faster than the ventricular rate. (CDISC)",
                                 meaning=NCIT.C50501) )
        setattr(cls, "Prolonged QT",
                PermissibleValue(text="Prolonged QT",
                                 description="An electrocardiographic finding in which the QT interval not corrected for heart rate is prolonged. Thresholds for different age, gender, and patient populations exist.",
                                 meaning=NCIT.C71034) )
        setattr(cls, "Supraventricular Tachycardia",
                PermissibleValue(text="Supraventricular Tachycardia",
                                 description="A disorder characterized by an electrocardiographic finding of a tachycardia which does not originate in the ventricles or His Purkinje system. There is an abnormally high heart rate and QRS complexes are typically narrow, but aberration or preexcitation may be present.",
                                 meaning=NCIT.C35061) )
        setattr(cls, "Cardiomyopathy, NOS",
                PermissibleValue(text="Cardiomyopathy, NOS",
                                 description="A disease of the heart muscle or myocardium proper. Cardiomyopathies may be classified as either primary or secondary, on the basis of etiology, or on the pathophysiology of the lesion: hypertrophic, dilated, or restrictive.",
                                 meaning=NCIT.C34830) )
        setattr(cls, "Restrictive Cardiomyopathy",
                PermissibleValue(text="Restrictive Cardiomyopathy",
                                 description="A type of heart disorder referring to the inability of the ventricles to fill with blood because the myocardium (heart muscle) stiffens and looses its flexibility. Causes include replacement of the myocardium with scar tissue, abnormal cellular infiltration of the myocardium, or deposition of a substance (e.g., amyloid) in the myocardium.",
                                 meaning=NCIT.C62798) )
        setattr(cls, "Dilated Cardiomyopathy",
                PermissibleValue(text="Dilated Cardiomyopathy",
                                 description="Cardiomyopathy which is characterized by dilation and contractile dysfunction of the left and right ventricles. It may be idiopathic, or it may result from a myocardial infarction, myocardial infection, or alcohol abuse. It is a cause of congestive heart failure.",
                                 meaning=NCIT.C84673) )
        setattr(cls, "Sensory Neuropathy",
                PermissibleValue(text="Sensory Neuropathy",
                                 description="Inflammation or degeneration of the sensory nerves.",
                                 meaning=NCIT.C3501) )
        setattr(cls, "Motor Neuropathy",
                PermissibleValue(text="Motor Neuropathy",
                                 description="Inflammation or degeneration of the peripheral motor nerves.",
                                 meaning=NCIT.C3500) )
        setattr(cls, "Pulmonary Fibrosis",
                PermissibleValue(text="Pulmonary Fibrosis",
                                 description="Chronic progressive interstitial lung disorder characterized by the replacement of the lung tissue by connective tissue, leading to progressive dyspnea, respiratory failure, or right heart failure. Causes include chronic inflammatory processes, exposure to environmental irritants, radiation therapy, autoimmune disorders, certain drugs, or it may be idiopathic (no identifiable cause).",
                                 meaning=NCIT.C26869) )
        setattr(cls, "Decreased Creatinine Clearance",
                PermissibleValue(text="Decreased Creatinine Clearance",
                                 description="A laboratory test finding that indicates decreased creatinine clearance.",
                                 meaning=NCIT.C185671) )
        setattr(cls, "Tubular Damage",
                PermissibleValue(text="Tubular Damage",
                                 description="Damage to the renal tubules.",
                                 meaning=NCIT.C185689) )
        setattr(cls, "Decreased GFR",
                PermissibleValue(text="Decreased GFR",
                                 description="A laboratory test result which indicates a decreased glomerular filtration rate.",
                                 meaning=NCIT.C78326) )

class LeSeverityGradeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="LeSeverityGradeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Mild Adverse Event",
                PermissibleValue(text="Mild Adverse Event",
                                 description="An experience that is usually transient, and requires no special treatment or intervention. The event does not generally interfere with usual daily activities. Includes transient laboratory test alterations.",
                                 meaning=NCIT.C41338) )
        setattr(cls, "Moderate Adverse Event",
                PermissibleValue(text="Moderate Adverse Event",
                                 description="An experience that is alleviated with simple therapeutic treatments. The event impacts usual daily activities. Includes laboratory test alterations indicating injury, but without long-term risk.",
                                 meaning=NCIT.C41339) )
        setattr(cls, "Severe Adverse Event",
                PermissibleValue(text="Severe Adverse Event",
                                 description="An adverse event experience that requires intensive therapeutic intervention and interrupts usual daily activities.",
                                 meaning=NCIT.C41340) )
        setattr(cls, "Life Threatening Adverse Event",
                PermissibleValue(text="Life Threatening Adverse Event",
                                 description="An adverse event that has life-threatening consequences; for which urgent intervention is indicated; that puts the patient at risk of death at the time of the event if immediate intervention is not undertaken.",
                                 meaning=NCIT.C84266) )
        setattr(cls, "Death Related to Adverse Event",
                PermissibleValue(text="Death Related to Adverse Event",
                                 description="The termination of life associated with an adverse event.",
                                 meaning=NCIT.C48275) )

class NoNotreportedUnknownYesEnum(EnumDefinitionImpl):

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
        name="NoNotreportedUnknownYesEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=NCIT.C43234) )

class SmnSiteEnum(EnumDefinitionImpl):

    Thorax = PermissibleValue(text="Thorax",
                                   description="The division of the body lying between the neck and the abdomen.",
                                   meaning=PCDC["/C12799"])
    Limbs = PermissibleValue(text="Limbs",
                                 description="A body region referring to an upper or lower extremity.",
                                 meaning=PCDC["/C12429"])
    Abdomen = PermissibleValue(text="Abdomen",
                                     description="The portion of the body that lies between the thorax and the pelvis.",
                                     meaning=PCDC["/C12664"])
    Pelvis = PermissibleValue(text="Pelvis",
                                   description="The bony, basin-shaped structure formed by the hipbones and the base of the backbone supporting the lower limbs in humans.",
                                   meaning=PCDC["/C12767"])
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=PCDC["/C17649"])
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=PCDC["/C17998"])

    _defn = EnumDefinition(
        name="SmnSiteEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Head and Neck",
                PermissibleValue(text="Head and Neck",
                                 description="For oncology, an area of the body generally construed to comprise the base of skull and facial bones, sinuses, orbits, salivary glands, oral cavity, oropharynx, larynx, thyroid, facial and neck musculature and lymph nodes draining these areas.",
                                 meaning=PCDC["/C12418"]) )
        setattr(cls, "Not Applicable",
                PermissibleValue(text="Not Applicable",
                                 description="Not provided or available.",
                                 meaning=PCDC["/C43234"]) )

class SmnTypeEnum(EnumDefinitionImpl):

    Leukemia = PermissibleValue(text="Leukemia",
                                       description="A malignant (clonal) hematologic disorder, involving hematopoietic stem cells and characterized by the presence of primitive or atypical myeloid or lymphoid cells in the bone marrow and the blood. Leukemias are classified as acute or chronic based on the degree of cellular differentiation and the predominant cell type present. Leukemia is usually associated with anemia, fever, hemorrhagic episodes, and splenomegaly. Common leukemias include acute myeloid leukemia, chronic myelogenous leukemia, acute lymphoblastic or precursor lymphoblastic leukemia, and chronic lymphocytic leukemia. Treatment is vital to patient survival; untreated, the natural course of acute leukemias is normally measured in weeks or months, while that of chronic leukemias is more often measured in months or years.",
                                       meaning=PCDC["/C3161"])
    Sarcoma = PermissibleValue(text="Sarcoma",
                                     description="A usually aggressive malignant neoplasm of the soft tissue or bone. It arises from muscle, fat, fibrous tissue, bone, cartilage, and blood vessels. Sarcomas occur in both children and adults. The prognosis depends largely on the degree of differentiation (grade) of the neoplasm. Representative subtypes are liposarcoma, leiomyosarcoma, osteosarcoma, and chondrosarcoma.",
                                     meaning=PCDC["/C9118"])
    Carcinoma = PermissibleValue(text="Carcinoma",
                                         description="A malignant tumor arising from epithelial cells. Carcinomas that arise from glandular epithelium are called adenocarcinomas, those that arise from squamous epithelium are called squamous cell carcinomas, and those that arise from transitional epithelium are called transitional cell carcinomas. Morphologically, the malignant epithelial cells may display abnormal mitotic figures, anaplasia, and necrosis. Carcinomas are graded by the degree of cellular differentiation as well, moderately, or poorly differentiated. Carcinomas invade the surrounding tissues and tend to metastasize to other anatomic sites. Lung carcinoma, skin carcinoma, breast carcinoma, colon carcinoma, and prostate carcinoma are the most frequently seen carcinomas.",
                                         meaning=PCDC["/C2916"])
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=PCDC["/C17649"])
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=PCDC["/C17998"])

    _defn = EnumDefinition(
        name="SmnTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Applicable",
                PermissibleValue(text="Not Applicable",
                                 description="Not provided or available.",
                                 meaning=PCDC["/C43234"]) )

class SmnFieldEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=PCDC["/C17998"])

    _defn = EnumDefinition(
        name="SmnFieldEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "In XRT Field",
                PermissibleValue(text="In XRT Field",
                                 description="Within the confines of the radiation field.",
                                 meaning=PCDC["/C175045"]) )
        setattr(cls, "Out of XRT Field",
                PermissibleValue(text="Out of XRT Field",
                                 description="Outside the confines of the radiation field.",
                                 meaning=PCDC["/C175046"]) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=PCDC["/C43234"]) )

class ProMeasuresEnum(EnumDefinitionImpl):

    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=PCDC["/C17649"])
    Unknown = PermissibleValue(text="Unknown",
                                     description="Reported as unknown by the data contributor.",
                                     meaning=PCDC["/C17998"])

    _defn = EnumDefinition(
        name="ProMeasuresEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "PROMIS Global",
                PermissibleValue(text="PROMIS Global",
                                 description="A 10 question instrument designed provide an efficient way of gathering general perceptions of health.",
                                 meaning=PCDC["/C103253"]) )
        setattr(cls, "PROMIS Fatigue Short Form",
                PermissibleValue(text="PROMIS Fatigue Short Form",
                                 description="A self-report tool that evaluates fatigue over a range of symptoms, from mild subjective feelings of tiredness to an overwhelming, debilitating, and sustained sense of exhaustion that likely decreases one's ability to execute daily activities and function normally in family or social roles. The fatigue short form is generic rather than disease specific and assesses fatigue over the past seven days.",
                                 meaning=PCDC["/C129493"]) )
        setattr(cls, "Fact NTX",
                PermissibleValue(text="Fact NTX",
                                 description="A questionnaire tool to assess the neurotoxic effects of cancer therapy.",
                                 meaning=PCDC["/C177378"]) )
        setattr(cls, "PRO-CTCAE",
                PermissibleValue(text="PRO-CTCAE",
                                 description="A library of items for patient self-reporting of symptoms and side effects associated with cancer treatment trials.",
                                 meaning=PCDC["/C103843"]) )
        setattr(cls, "PedsQL Multi-Dimensional Fatigue Scale",
                PermissibleValue(text="PedsQL Multi-Dimensional Fatigue Scale",
                                 description="An 18 item component of the Pediatric Quality of Life Inventory is a generic symptom-specific instrument to measure fatigue in pediatric patients ages 2-18 comprised of General Fatigue, Sleep/Rest Fatigue, and Cognitive Fatigue domains.",
                                 meaning=PCDC["/C131369"]) )
        setattr(cls, "PedsQL 4.0 Generic Core Scale",
                PermissibleValue(text="PedsQL 4.0 Generic Core Scale",
                                 description="Child self-report and parent proxy report scales developed to measure health-related quality of life issues in children and adolescents aged 2-18.",
                                 meaning=PCDC["/C177379"]) )
        setattr(cls, "AYA-HEARS",
                PermissibleValue(text="AYA-HEARS",
                                 description="A questionnaire designed to measure hearing loss or problems experienced by patients who have received treatment for cancer.",
                                 meaning=PCDC["/C131878"]) )
        setattr(cls, "EORTC QLQ-C30",
                PermissibleValue(text="EORTC QLQ-C30",
                                 description="A scale used both for the subjective scoring of a person's overall health, and for their quality of life, that ranges from 1: Very Poor to 7: Excellent.",
                                 meaning=PCDC["/C120497"]) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=PCDC["/C43234"]) )

class ProMeasurementTypeEnum(EnumDefinitionImpl):

    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=PCDC["/C17649"])
    Unknown = PermissibleValue(text="Unknown",
                                     description="Not known, observed, recorded; or reported as unknown by the data contributor.",
                                     meaning=PCDC["/C17998"])

    _defn = EnumDefinition(
        name="ProMeasurementTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Health Profile",
                PermissibleValue(text="Health Profile",
                                 description="Measures a person's perceptions of the social impact of oral disorders on their well-being; measures self-reported dysfunction, discomfort and disability attributed to oral conditions.",
                                 meaning=PCDC["/C62359"]) )
        setattr(cls, "Symptom Scale",
                PermissibleValue(text="Symptom Scale",
                                 description="A patient reported questionnaire composed of rating scales developed to measure the degree of distress experienced by the patient for specific symptoms.",
                                 meaning=PCDC["/C124147"]) )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=PCDC["/C432234"]) )

class RatersEnum(EnumDefinitionImpl):

    Subject = PermissibleValue(text="Subject",
                                     description="A matter or an individual that is observed, analyzed, examined, investigated, experimented upon, or/and treated in the course of a particular study.",
                                     meaning=PCDC["/C41189"])
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=PCDC["/C17649"])
    Unknown = PermissibleValue(text="Unknown",
                                     description="Not known, observed, recorded; or reported as unknown by the data contributor.",
                                     meaning=PCDC["/C17998"])

    _defn = EnumDefinition(
        name="RatersEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=PCDC["/C432234"]) )

class TimePointEnum(EnumDefinitionImpl):

    Baseline = PermissibleValue(text="Baseline",
                                       description="A starting point to which things may be compared.",
                                       meaning=PCDC["/C25213"])
    Other = PermissibleValue(text="Other",
                                 description="Different than the one(s) previously specified or mentioned.",
                                 meaning=PCDC["/C17649"])
    Unknown = PermissibleValue(text="Unknown",
                                     description="Not known, observed, recorded; or reported as unknown by the data contributor.",
                                     meaning=PCDC["/C17998"])

    _defn = EnumDefinition(
        name="TimePointEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "On Treatment",
                PermissibleValue(text="On Treatment",
                                 description="The time during which a patient is receiving treatment.",
                                 meaning=PCDC["/C142170"]) )
        setattr(cls, "End of Treatment",
                PermissibleValue(text="End of Treatment",
                                 description="The end of the planned treatment.") )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not provided or available.",
                                 meaning=PCDC["/C432234"]) )

# Slots
class slots:
    pass

slots.submitter_id = Slot(uri=DEFAULT_.submitter_id, name="submitter_id", curie=DEFAULT_.curie('submitter_id'),
                   model_uri=DEFAULT_.submitter_id, domain=None, range=str)

slots.type = Slot(uri=DEFAULT_.type, name="type", curie=DEFAULT_.curie('type'),
                   model_uri=DEFAULT_.type, domain=None, range=str)

slots.subjects = Slot(uri=DEFAULT_.subjects, name="subjects", curie=DEFAULT_.curie('subjects'),
                   model_uri=DEFAULT_.subjects, domain=None, range=Union[Union[dict, Subject], List[Union[dict, Subject]]])

slots.timings = Slot(uri=DEFAULT_.timings, name="timings", curie=DEFAULT_.curie('timings'),
                   model_uri=DEFAULT_.timings, domain=None, range=Optional[Union[dict, Timing]])

slots.sex = Slot(uri=DEFAULT_.sex, name="sex", curie=DEFAULT_.curie('sex'),
                   model_uri=DEFAULT_.sex, domain=None, range=Optional[Union[str, "SexEnum"]])

slots.race = Slot(uri=DEFAULT_.race, name="race", curie=DEFAULT_.curie('race'),
                   model_uri=DEFAULT_.race, domain=None, range=Optional[Union[str, "RaceEnum"]])

slots.race_other = Slot(uri=DEFAULT_.race_other, name="race_other", curie=DEFAULT_.curie('race_other'),
                   model_uri=DEFAULT_.race_other, domain=None, range=Optional[str])

slots.ethnicity = Slot(uri=DEFAULT_.ethnicity, name="ethnicity", curie=DEFAULT_.curie('ethnicity'),
                   model_uri=DEFAULT_.ethnicity, domain=None, range=Optional[Union[str, "EthnicityEnum"]])

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

slots.age_off = Slot(uri=DEFAULT_.age_off, name="age_off", curie=DEFAULT_.curie('age_off'),
                   model_uri=DEFAULT_.age_off, domain=None, range=Optional[int])

slots.off_type = Slot(uri=DEFAULT_.off_type, name="off_type", curie=DEFAULT_.curie('off_type'),
                   model_uri=DEFAULT_.off_type, domain=None, range=Optional[Union[str, "OffTypeEnum"]])

slots.reason_off = Slot(uri=DEFAULT_.reason_off, name="reason_off", curie=DEFAULT_.curie('reason_off'),
                   model_uri=DEFAULT_.reason_off, domain=None, range=Optional[Union[str, "ReasonOffEnum"]])

slots.reason_off_other = Slot(uri=DEFAULT_.reason_off_other, name="reason_off_other", curie=DEFAULT_.curie('reason_off_other'),
                   model_uri=DEFAULT_.reason_off_other, domain=None, range=Optional[str])

slots.another_study = Slot(uri=DEFAULT_.another_study, name="another_study", curie=DEFAULT_.curie('another_study'),
                   model_uri=DEFAULT_.another_study, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.prior_cancer = Slot(uri=DEFAULT_.prior_cancer, name="prior_cancer", curie=DEFAULT_.curie('prior_cancer'),
                   model_uri=DEFAULT_.prior_cancer, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.relation = Slot(uri=DEFAULT_.relation, name="relation", curie=DEFAULT_.curie('relation'),
                   model_uri=DEFAULT_.relation, domain=None, range=Optional[Union[str, "RelationEnum"]])

slots.prior_cancer_type = Slot(uri=DEFAULT_.prior_cancer_type, name="prior_cancer_type", curie=DEFAULT_.curie('prior_cancer_type'),
                   model_uri=DEFAULT_.prior_cancer_type, domain=None, range=Optional[str])

slots.condition = Slot(uri=DEFAULT_.condition, name="condition", curie=DEFAULT_.curie('condition'),
                   model_uri=DEFAULT_.condition, domain=None, range=Optional[Union[str, "ConditionEnum"]])

slots.condition_other = Slot(uri=DEFAULT_.condition_other, name="condition_other", curie=DEFAULT_.curie('condition_other'),
                   model_uri=DEFAULT_.condition_other, domain=None, range=Optional[str])

slots.condition_type = Slot(uri=DEFAULT_.condition_type, name="condition_type", curie=DEFAULT_.curie('condition_type'),
                   model_uri=DEFAULT_.condition_type, domain=None, range=Optional[Union[str, "ConditionTypeEnum"]])

slots.condition_status = Slot(uri=DEFAULT_.condition_status, name="condition_status", curie=DEFAULT_.curie('condition_status'),
                   model_uri=DEFAULT_.condition_status, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.assisted_conception = Slot(uri=DEFAULT_.assisted_conception, name="assisted_conception", curie=DEFAULT_.curie('assisted_conception'),
                   model_uri=DEFAULT_.assisted_conception, domain=None, range=Optional[Union[str, "AssistedConceptionEnum"]])

slots.age_at_lkss = Slot(uri=DEFAULT_.age_at_lkss, name="age_at_lkss", curie=DEFAULT_.curie('age_at_lkss'),
                   model_uri=DEFAULT_.age_at_lkss, domain=None, range=Optional[int])

slots.lkss = Slot(uri=DEFAULT_.lkss, name="lkss", curie=DEFAULT_.curie('lkss'),
                   model_uri=DEFAULT_.lkss, domain=None, range=Optional[Union[str, "LkssEnum"]])

slots.lkss_with_disease = Slot(uri=DEFAULT_.lkss_with_disease, name="lkss_with_disease", curie=DEFAULT_.curie('lkss_with_disease'),
                   model_uri=DEFAULT_.lkss_with_disease, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.age_lost_to_follow_up = Slot(uri=DEFAULT_.age_lost_to_follow_up, name="age_lost_to_follow_up", curie=DEFAULT_.curie('age_lost_to_follow_up'),
                   model_uri=DEFAULT_.age_lost_to_follow_up, domain=None, range=Optional[int])

slots.cause_of_death = Slot(uri=DEFAULT_.cause_of_death, name="cause_of_death", curie=DEFAULT_.curie('cause_of_death'),
                   model_uri=DEFAULT_.cause_of_death, domain=None, range=Optional[Union[str, "CauseOfDeathEnum"]])

slots.trm_type = Slot(uri=DEFAULT_.trm_type, name="trm_type", curie=DEFAULT_.curie('trm_type'),
                   model_uri=DEFAULT_.trm_type, domain=None, range=Optional[Union[str, "TrmTypeEnum"]])

slots.trm_type_other = Slot(uri=DEFAULT_.trm_type_other, name="trm_type_other", curie=DEFAULT_.curie('trm_type_other'),
                   model_uri=DEFAULT_.trm_type_other, domain=None, range=Optional[str])

slots.cause_of_death_detail = Slot(uri=DEFAULT_.cause_of_death_detail, name="cause_of_death_detail", curie=DEFAULT_.curie('cause_of_death_detail'),
                   model_uri=DEFAULT_.cause_of_death_detail, domain=None, range=Optional[Union[str, "CauseOfDeathDetailEnum"]])

slots.cause_of_death_detail_other = Slot(uri=DEFAULT_.cause_of_death_detail_other, name="cause_of_death_detail_other", curie=DEFAULT_.curie('cause_of_death_detail_other'),
                   model_uri=DEFAULT_.cause_of_death_detail_other, domain=None, range=Optional[str])

slots.cause_of_death_ranking = Slot(uri=DEFAULT_.cause_of_death_ranking, name="cause_of_death_ranking", curie=DEFAULT_.curie('cause_of_death_ranking'),
                   model_uri=DEFAULT_.cause_of_death_ranking, domain=None, range=Optional[Union[str, "CauseOfDeathRankingEnum"]])

slots.age_at_measurement = Slot(uri=DEFAULT_.age_at_measurement, name="age_at_measurement", curie=DEFAULT_.curie('age_at_measurement'),
                   model_uri=DEFAULT_.age_at_measurement, domain=None, range=Optional[int])

slots.measurement_type = Slot(uri=DEFAULT_.measurement_type, name="measurement_type", curie=DEFAULT_.curie('measurement_type'),
                   model_uri=DEFAULT_.measurement_type, domain=None, range=Optional[Union[str, "MeasurementTypeEnum"]])

slots.measurement = Slot(uri=DEFAULT_.measurement, name="measurement", curie=DEFAULT_.curie('measurement'),
                   model_uri=DEFAULT_.measurement, domain=None, range=Optional[str])

slots.measurement_numeric = Slot(uri=DEFAULT_.measurement_numeric, name="measurement_numeric", curie=DEFAULT_.curie('measurement_numeric'),
                   model_uri=DEFAULT_.measurement_numeric, domain=None, range=Optional[int])

slots.measurement_unit = Slot(uri=DEFAULT_.measurement_unit, name="measurement_unit", curie=DEFAULT_.curie('measurement_unit'),
                   model_uri=DEFAULT_.measurement_unit, domain=None, range=Optional[Union[str, "MeasurementUnitEnum"]])

slots.age_at_function_test = Slot(uri=DEFAULT_.age_at_function_test, name="age_at_function_test", curie=DEFAULT_.curie('age_at_function_test'),
                   model_uri=DEFAULT_.age_at_function_test, domain=None, range=Optional[int])

slots.function_category = Slot(uri=DEFAULT_.function_category, name="function_category", curie=DEFAULT_.curie('function_category'),
                   model_uri=DEFAULT_.function_category, domain=None, range=Optional[Union[str, "FunctionCategoryEnum"]])

slots.function_test = Slot(uri=DEFAULT_.function_test, name="function_test", curie=DEFAULT_.curie('function_test'),
                   model_uri=DEFAULT_.function_test, domain=None, range=Optional[Union[str, "FunctionTestEnum"]])

slots.function_result = Slot(uri=DEFAULT_.function_result, name="function_result", curie=DEFAULT_.curie('function_result'),
                   model_uri=DEFAULT_.function_result, domain=None, range=Optional[str])

slots.function_result_numeric = Slot(uri=DEFAULT_.function_result_numeric, name="function_result_numeric", curie=DEFAULT_.curie('function_result_numeric'),
                   model_uri=DEFAULT_.function_result_numeric, domain=None, range=Optional[int])

slots.function_result_unit = Slot(uri=DEFAULT_.function_result_unit, name="function_result_unit", curie=DEFAULT_.curie('function_result_unit'),
                   model_uri=DEFAULT_.function_result_unit, domain=None, range=Optional[Union[str, "FunctionResultUnitEnum"]])

slots.age_at_lab = Slot(uri=DEFAULT_.age_at_lab, name="age_at_lab", curie=DEFAULT_.curie('age_at_lab'),
                   model_uri=DEFAULT_.age_at_lab, domain=None, range=Optional[int])

slots.lab_category = Slot(uri=DEFAULT_.lab_category, name="lab_category", curie=DEFAULT_.curie('lab_category'),
                   model_uri=DEFAULT_.lab_category, domain=None, range=Optional[Union[str, "LabCategoryEnum"]])

slots.lab_test = Slot(uri=DEFAULT_.lab_test, name="lab_test", curie=DEFAULT_.curie('lab_test'),
                   model_uri=DEFAULT_.lab_test, domain=None, range=Optional[Union[str, "LabTestEnum"]])

slots.lab_test_other = Slot(uri=DEFAULT_.lab_test_other, name="lab_test_other", curie=DEFAULT_.curie('lab_test_other'),
                   model_uri=DEFAULT_.lab_test_other, domain=None, range=Optional[str])

slots.specimen = Slot(uri=DEFAULT_.specimen, name="specimen", curie=DEFAULT_.curie('specimen'),
                   model_uri=DEFAULT_.specimen, domain=None, range=Optional[Union[str, "SpecimenEnum"]])

slots.specimen_other = Slot(uri=DEFAULT_.specimen_other, name="specimen_other", curie=DEFAULT_.curie('specimen_other'),
                   model_uri=DEFAULT_.specimen_other, domain=None, range=Optional[str])

slots.lab_result = Slot(uri=DEFAULT_.lab_result, name="lab_result", curie=DEFAULT_.curie('lab_result'),
                   model_uri=DEFAULT_.lab_result, domain=None, range=Optional[str])

slots.lab_result_categorical = Slot(uri=DEFAULT_.lab_result_categorical, name="lab_result_categorical", curie=DEFAULT_.curie('lab_result_categorical'),
                   model_uri=DEFAULT_.lab_result_categorical, domain=None, range=Optional[Union[str, "LabResultCategoricalEnum"]])

slots.lab_result_numeric = Slot(uri=DEFAULT_.lab_result_numeric, name="lab_result_numeric", curie=DEFAULT_.curie('lab_result_numeric'),
                   model_uri=DEFAULT_.lab_result_numeric, domain=None, range=Optional[int])

slots.lab_result_unit = Slot(uri=DEFAULT_.lab_result_unit, name="lab_result_unit", curie=DEFAULT_.curie('lab_result_unit'),
                   model_uri=DEFAULT_.lab_result_unit, domain=None, range=Optional[Union[str, "LabResultUnitEnum"]])

slots.lab_method = Slot(uri=DEFAULT_.lab_method, name="lab_method", curie=DEFAULT_.curie('lab_method'),
                   model_uri=DEFAULT_.lab_method, domain=None, range=Optional[Union[str, "LabMethodEnum"]])

slots.lab_seq_method = Slot(uri=DEFAULT_.lab_seq_method, name="lab_seq_method", curie=DEFAULT_.curie('lab_seq_method'),
                   model_uri=DEFAULT_.lab_seq_method, domain=None, range=Optional[Union[str, "LabSeqMethodEnum"]])

slots.threshold_high = Slot(uri=DEFAULT_.threshold_high, name="threshold_high", curie=DEFAULT_.curie('threshold_high'),
                   model_uri=DEFAULT_.threshold_high, domain=None, range=Optional[int])

slots.threshold_low = Slot(uri=DEFAULT_.threshold_low, name="threshold_low", curie=DEFAULT_.curie('threshold_low'),
                   model_uri=DEFAULT_.threshold_low, domain=None, range=Optional[int])

slots.pmid_ref = Slot(uri=DEFAULT_.pmid_ref, name="pmid_ref", curie=DEFAULT_.curie('pmid_ref'),
                   model_uri=DEFAULT_.pmid_ref, domain=None, range=Optional[int])

slots.bm_morphology = Slot(uri=DEFAULT_.bm_morphology, name="bm_morphology", curie=DEFAULT_.curie('bm_morphology'),
                   model_uri=DEFAULT_.bm_morphology, domain=None, range=Optional[Union[str, "BmMorphologyEnum"]])

slots.traumatic_tap = Slot(uri=DEFAULT_.traumatic_tap, name="traumatic_tap", curie=DEFAULT_.curie('traumatic_tap'),
                   model_uri=DEFAULT_.traumatic_tap, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.age_at_imaging = Slot(uri=DEFAULT_.age_at_imaging, name="age_at_imaging", curie=DEFAULT_.curie('age_at_imaging'),
                   model_uri=DEFAULT_.age_at_imaging, domain=None, range=Optional[int])

slots.imaging_method = Slot(uri=DEFAULT_.imaging_method, name="imaging_method", curie=DEFAULT_.curie('imaging_method'),
                   model_uri=DEFAULT_.imaging_method, domain=None, range=Optional[Union[str, "ImagingMethodEnum"]])

slots.imaging_result = Slot(uri=DEFAULT_.imaging_result, name="imaging_result", curie=DEFAULT_.curie('imaging_result'),
                   model_uri=DEFAULT_.imaging_result, domain=None, range=Optional[Union[str, "ImagingResultEnum"]])

slots.deauville_score = Slot(uri=DEFAULT_.deauville_score, name="deauville_score", curie=DEFAULT_.curie('deauville_score'),
                   model_uri=DEFAULT_.deauville_score, domain=None, range=Optional[Union[str, "DeauvilleScoreEnum"]])

slots.qpet_score = Slot(uri=DEFAULT_.qpet_score, name="qpet_score", curie=DEFAULT_.curie('qpet_score'),
                   model_uri=DEFAULT_.qpet_score, domain=None, range=Optional[int])

slots.age_at_cytology = Slot(uri=DEFAULT_.age_at_cytology, name="age_at_cytology", curie=DEFAULT_.curie('age_at_cytology'),
                   model_uri=DEFAULT_.age_at_cytology, domain=None, range=Optional[int])

slots.malignant_cells = Slot(uri=DEFAULT_.malignant_cells, name="malignant_cells", curie=DEFAULT_.curie('malignant_cells'),
                   model_uri=DEFAULT_.malignant_cells, domain=None, range=Optional[Union[str, "AbsentNotreportedPresentUnknownEnum"]])

slots.cytology_spec_type = Slot(uri=DEFAULT_.cytology_spec_type, name="cytology_spec_type", curie=DEFAULT_.curie('cytology_spec_type'),
                   model_uri=DEFAULT_.cytology_spec_type, domain=None, range=Optional[Union[str, "CytologySpecTypeEnum"]])

slots.age_at_ihc = Slot(uri=DEFAULT_.age_at_ihc, name="age_at_ihc", curie=DEFAULT_.curie('age_at_ihc'),
                   model_uri=DEFAULT_.age_at_ihc, domain=None, range=Optional[int])

slots.ihc_test = Slot(uri=DEFAULT_.ihc_test, name="ihc_test", curie=DEFAULT_.curie('ihc_test'),
                   model_uri=DEFAULT_.ihc_test, domain=None, range=Optional[Union[str, "IhcTestEnum"]])

slots.ihc_spec_type = Slot(uri=DEFAULT_.ihc_spec_type, name="ihc_spec_type", curie=DEFAULT_.curie('ihc_spec_type'),
                   model_uri=DEFAULT_.ihc_spec_type, domain=None, range=Optional[Union[str, "IhcSpecTypeEnum"]])

slots.ihc_result = Slot(uri=DEFAULT_.ihc_result, name="ihc_result", curie=DEFAULT_.curie('ihc_result'),
                   model_uri=DEFAULT_.ihc_result, domain=None, range=Optional[str])

slots.ihc_result_numeric = Slot(uri=DEFAULT_.ihc_result_numeric, name="ihc_result_numeric", curie=DEFAULT_.curie('ihc_result_numeric'),
                   model_uri=DEFAULT_.ihc_result_numeric, domain=None, range=Optional[int])

slots.ihc_result_unit = Slot(uri=DEFAULT_.ihc_result_unit, name="ihc_result_unit", curie=DEFAULT_.curie('ihc_result_unit'),
                   model_uri=DEFAULT_.ihc_result_unit, domain=None, range=Optional[Union[str, "IhcResultUnitEnum"]])

slots.age_at_genetic_analysis = Slot(uri=DEFAULT_.age_at_genetic_analysis, name="age_at_genetic_analysis", curie=DEFAULT_.curie('age_at_genetic_analysis'),
                   model_uri=DEFAULT_.age_at_genetic_analysis, domain=None, range=Optional[int])

slots.lesion_classification = Slot(uri=DEFAULT_.lesion_classification, name="lesion_classification", curie=DEFAULT_.curie('lesion_classification'),
                   model_uri=DEFAULT_.lesion_classification, domain=None, range=Optional[Union[str, "LesionClassificationEnum"]])

slots.method = Slot(uri=DEFAULT_.method, name="method", curie=DEFAULT_.curie('method'),
                   model_uri=DEFAULT_.method, domain=None, range=Optional[Union[str, "MethodEnum"]])

slots.genomic_source_class = Slot(uri=DEFAULT_.genomic_source_class, name="genomic_source_class", curie=DEFAULT_.curie('genomic_source_class'),
                   model_uri=DEFAULT_.genomic_source_class, domain=None, range=Optional[Union[str, "GenomicSourceClassEnum"]])

slots.common_name = Slot(uri=DEFAULT_.common_name, name="common_name", curie=DEFAULT_.curie('common_name'),
                   model_uri=DEFAULT_.common_name, domain=None, range=Optional[Union[str, "CommonNameEnum"]])

slots.status = Slot(uri=DEFAULT_.status, name="status", curie=DEFAULT_.curie('status'),
                   model_uri=DEFAULT_.status, domain=None, range=Optional[Union[str, "StatusEnum"]])

slots.gene = Slot(uri=DEFAULT_.gene, name="gene", curie=DEFAULT_.curie('gene'),
                   model_uri=DEFAULT_.gene, domain=None, range=Optional[str])

slots.chromosome = Slot(uri=DEFAULT_.chromosome, name="chromosome", curie=DEFAULT_.curie('chromosome'),
                   model_uri=DEFAULT_.chromosome, domain=None, range=Optional[str])

slots.mutation_type = Slot(uri=DEFAULT_.mutation_type, name="mutation_type", curie=DEFAULT_.curie('mutation_type'),
                   model_uri=DEFAULT_.mutation_type, domain=None, range=Optional[Union[str, "MutationTypeEnum"]])

slots.mutation_type_other = Slot(uri=DEFAULT_.mutation_type_other, name="mutation_type_other", curie=DEFAULT_.curie('mutation_type_other'),
                   model_uri=DEFAULT_.mutation_type_other, domain=None, range=Optional[str])

slots.expression_consequence = Slot(uri=DEFAULT_.expression_consequence, name="expression_consequence", curie=DEFAULT_.curie('expression_consequence'),
                   model_uri=DEFAULT_.expression_consequence, domain=None, range=Optional[Union[str, "ExpressionConsequenceEnum"]])

slots.chromosomal_consequence = Slot(uri=DEFAULT_.chromosomal_consequence, name="chromosomal_consequence", curie=DEFAULT_.curie('chromosomal_consequence'),
                   model_uri=DEFAULT_.chromosomal_consequence, domain=None, range=Optional[Union[str, "ChromosomalConsequenceEnum"]])

slots.genomic_region = Slot(uri=DEFAULT_.genomic_region, name="genomic_region", curie=DEFAULT_.curie('genomic_region'),
                   model_uri=DEFAULT_.genomic_region, domain=None, range=Optional[Union[str, "GenomicRegionEnum"]])

slots.allelic_state = Slot(uri=DEFAULT_.allelic_state, name="allelic_state", curie=DEFAULT_.curie('allelic_state'),
                   model_uri=DEFAULT_.allelic_state, domain=None, range=Optional[Union[str, "AllelicStateEnum"]])

slots.inheritance_pattern = Slot(uri=DEFAULT_.inheritance_pattern, name="inheritance_pattern", curie=DEFAULT_.curie('inheritance_pattern'),
                   model_uri=DEFAULT_.inheritance_pattern, domain=None, range=Optional[Union[str, "InheritancePatternEnum"]])

slots.parental_status = Slot(uri=DEFAULT_.parental_status, name="parental_status", curie=DEFAULT_.curie('parental_status'),
                   model_uri=DEFAULT_.parental_status, domain=None, range=Optional[Union[str, "ParentalStatusEnum"]])

slots.hgvs_coding = Slot(uri=DEFAULT_.hgvs_coding, name="hgvs_coding", curie=DEFAULT_.curie('hgvs_coding'),
                   model_uri=DEFAULT_.hgvs_coding, domain=None, range=Optional[str])

slots.hgvs_protein = Slot(uri=DEFAULT_.hgvs_protein, name="hgvs_protein", curie=DEFAULT_.curie('hgvs_protein'),
                   model_uri=DEFAULT_.hgvs_protein, domain=None, range=Optional[str])

slots.iscn = Slot(uri=DEFAULT_.iscn, name="iscn", curie=DEFAULT_.curie('iscn'),
                   model_uri=DEFAULT_.iscn, domain=None, range=Optional[str])

slots.clingen_id = Slot(uri=DEFAULT_.clingen_id, name="clingen_id", curie=DEFAULT_.curie('clingen_id'),
                   model_uri=DEFAULT_.clingen_id, domain=None, range=Optional[str])

slots.copy_number_variation = Slot(uri=DEFAULT_.copy_number_variation, name="copy_number_variation", curie=DEFAULT_.curie('copy_number_variation'),
                   model_uri=DEFAULT_.copy_number_variation, domain=None, range=Optional[Union[str, "CopyNumberVariationEnum"]])

slots.copy_number = Slot(uri=DEFAULT_.copy_number, name="copy_number", curie=DEFAULT_.curie('copy_number'),
                   model_uri=DEFAULT_.copy_number, domain=None, range=Optional[int])

slots.amplification = Slot(uri=DEFAULT_.amplification, name="amplification", curie=DEFAULT_.curie('amplification'),
                   model_uri=DEFAULT_.amplification, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.allelic_frequency = Slot(uri=DEFAULT_.allelic_frequency, name="allelic_frequency", curie=DEFAULT_.curie('allelic_frequency'),
                   model_uri=DEFAULT_.allelic_frequency, domain=None, range=Optional[int])

slots.gene2 = Slot(uri=DEFAULT_.gene2, name="gene2", curie=DEFAULT_.curie('gene2'),
                   model_uri=DEFAULT_.gene2, domain=None, range=Optional[str])

slots.mosaicism = Slot(uri=DEFAULT_.mosaicism, name="mosaicism", curie=DEFAULT_.curie('mosaicism'),
                   model_uri=DEFAULT_.mosaicism, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.mosaicism_percent = Slot(uri=DEFAULT_.mosaicism_percent, name="mosaicism_percent", curie=DEFAULT_.curie('mosaicism_percent'),
                   model_uri=DEFAULT_.mosaicism_percent, domain=None, range=Optional[int])

slots.alt_status = Slot(uri=DEFAULT_.alt_status, name="alt_status", curie=DEFAULT_.curie('alt_status'),
                   model_uri=DEFAULT_.alt_status, domain=None, range=Optional[Union[str, "AltStatusEnum"]])

slots.total_chromosomes = Slot(uri=DEFAULT_.total_chromosomes, name="total_chromosomes", curie=DEFAULT_.curie('total_chromosomes'),
                   model_uri=DEFAULT_.total_chromosomes, domain=None, range=Optional[int])

slots.independent_aberations = Slot(uri=DEFAULT_.independent_aberations, name="independent_aberations", curie=DEFAULT_.curie('independent_aberations'),
                   model_uri=DEFAULT_.independent_aberations, domain=None, range=Optional[int])

slots.cells_in_metaphase = Slot(uri=DEFAULT_.cells_in_metaphase, name="cells_in_metaphase", curie=DEFAULT_.curie('cells_in_metaphase'),
                   model_uri=DEFAULT_.cells_in_metaphase, domain=None, range=Optional[int])

slots.karyotype_status = Slot(uri=DEFAULT_.karyotype_status, name="karyotype_status", curie=DEFAULT_.curie('karyotype_status'),
                   model_uri=DEFAULT_.karyotype_status, domain=None, range=Optional[Union[str, "KaryotypeStatusEnum"]])

slots.dna_index = Slot(uri=DEFAULT_.dna_index, name="dna_index", curie=DEFAULT_.curie('dna_index'),
                   model_uri=DEFAULT_.dna_index, domain=None, range=Optional[Union[str, "DnaIndexEnum"]])

slots.dna_index_numeric = Slot(uri=DEFAULT_.dna_index_numeric, name="dna_index_numeric", curie=DEFAULT_.curie('dna_index_numeric'),
                   model_uri=DEFAULT_.dna_index_numeric, domain=None, range=Optional[int])

slots.cytodifferentiation = Slot(uri=DEFAULT_.cytodifferentiation, name="cytodifferentiation", curie=DEFAULT_.curie('cytodifferentiation'),
                   model_uri=DEFAULT_.cytodifferentiation, domain=None, range=Optional[Union[str, "CytodifferentiationEnum"]])

slots.mitotic_rate = Slot(uri=DEFAULT_.mitotic_rate, name="mitotic_rate", curie=DEFAULT_.curie('mitotic_rate'),
                   model_uri=DEFAULT_.mitotic_rate, domain=None, range=Optional[Union[str, "MitoticRateEnum"]])

slots.age_at_lesion_assessment = Slot(uri=DEFAULT_.age_at_lesion_assessment, name="age_at_lesion_assessment", curie=DEFAULT_.curie('age_at_lesion_assessment'),
                   model_uri=DEFAULT_.age_at_lesion_assessment, domain=None, range=Optional[int])

slots.lesion_assessment_review = Slot(uri=DEFAULT_.lesion_assessment_review, name="lesion_assessment_review", curie=DEFAULT_.curie('lesion_assessment_review'),
                   model_uri=DEFAULT_.lesion_assessment_review, domain=None, range=Optional[Union[str, "LesionAssessmentReviewEnum"]])

slots.lesion_state = Slot(uri=DEFAULT_.lesion_state, name="lesion_state", curie=DEFAULT_.curie('lesion_state'),
                   model_uri=DEFAULT_.lesion_state, domain=None, range=Optional[Union[str, "LesionStateEnum"]])

slots.detection_method = Slot(uri=DEFAULT_.detection_method, name="detection_method", curie=DEFAULT_.curie('detection_method'),
                   model_uri=DEFAULT_.detection_method, domain=None, range=Optional[Union[str, "DetectionMethodEnum"]])

slots.tissue_type = Slot(uri=DEFAULT_.tissue_type, name="tissue_type", curie=DEFAULT_.curie('tissue_type'),
                   model_uri=DEFAULT_.tissue_type, domain=None, range=Optional[Union[str, "BoneNotreportedSofttissueUnknownEnum"]])

slots.lesion_presentation = Slot(uri=DEFAULT_.lesion_presentation, name="lesion_presentation", curie=DEFAULT_.curie('lesion_presentation'),
                   model_uri=DEFAULT_.lesion_presentation, domain=None, range=Optional[Union[str, "LesionPresentationEnum"]])

slots.lesion_site = Slot(uri=DEFAULT_.lesion_site, name="lesion_site", curie=DEFAULT_.curie('lesion_site'),
                   model_uri=DEFAULT_.lesion_site, domain=None, range=Optional[Union[str, "LesionSiteEnum"]])

slots.lesion_site_other = Slot(uri=DEFAULT_.lesion_site_other, name="lesion_site_other", curie=DEFAULT_.curie('lesion_site_other'),
                   model_uri=DEFAULT_.lesion_site_other, domain=None, range=Optional[str])

slots.morph_sno = Slot(uri=DEFAULT_.morph_sno, name="morph_sno", curie=DEFAULT_.curie('morph_sno'),
                   model_uri=DEFAULT_.morph_sno, domain=None, range=Optional[str])

slots.icd_o_morph = Slot(uri=DEFAULT_.icd_o_morph, name="icd_o_morph", curie=DEFAULT_.curie('icd_o_morph'),
                   model_uri=DEFAULT_.icd_o_morph, domain=None, range=Optional[str])

slots.morph_txt = Slot(uri=DEFAULT_.morph_txt, name="morph_txt", curie=DEFAULT_.curie('morph_txt'),
                   model_uri=DEFAULT_.morph_txt, domain=None, range=Optional[str])

slots.top_sno = Slot(uri=DEFAULT_.top_sno, name="top_sno", curie=DEFAULT_.curie('top_sno'),
                   model_uri=DEFAULT_.top_sno, domain=None, range=Optional[str])

slots.icd_o_top = Slot(uri=DEFAULT_.icd_o_top, name="icd_o_top", curie=DEFAULT_.curie('icd_o_top'),
                   model_uri=DEFAULT_.icd_o_top, domain=None, range=Optional[str])

slots.top_txt = Slot(uri=DEFAULT_.top_txt, name="top_txt", curie=DEFAULT_.curie('top_txt'),
                   model_uri=DEFAULT_.top_txt, domain=None, range=Optional[str])

slots.lesion_size = Slot(uri=DEFAULT_.lesion_size, name="lesion_size", curie=DEFAULT_.curie('lesion_size'),
                   model_uri=DEFAULT_.lesion_size, domain=None, range=Optional[Union[str, "LesionSizeEnum"]])

slots.longest_diam_dim1 = Slot(uri=DEFAULT_.longest_diam_dim1, name="longest_diam_dim1", curie=DEFAULT_.curie('longest_diam_dim1'),
                   model_uri=DEFAULT_.longest_diam_dim1, domain=None, range=Optional[int])

slots.longest_diam_dim2 = Slot(uri=DEFAULT_.longest_diam_dim2, name="longest_diam_dim2", curie=DEFAULT_.curie('longest_diam_dim2'),
                   model_uri=DEFAULT_.longest_diam_dim2, domain=None, range=Optional[int])

slots.longest_diam_dim3 = Slot(uri=DEFAULT_.longest_diam_dim3, name="longest_diam_dim3", curie=DEFAULT_.curie('longest_diam_dim3'),
                   model_uri=DEFAULT_.longest_diam_dim3, domain=None, range=Optional[int])

slots.diam_type = Slot(uri=DEFAULT_.diam_type, name="diam_type", curie=DEFAULT_.curie('diam_type'),
                   model_uri=DEFAULT_.diam_type, domain=None, range=Optional[Union[str, "DiamTypeEnum"]])

slots.lesion_volume = Slot(uri=DEFAULT_.lesion_volume, name="lesion_volume", curie=DEFAULT_.curie('lesion_volume'),
                   model_uri=DEFAULT_.lesion_volume, domain=None, range=Optional[Union[str, "LesionVolumeEnum"]])

slots.estimated_volume_numeric = Slot(uri=DEFAULT_.estimated_volume_numeric, name="estimated_volume_numeric", curie=DEFAULT_.curie('estimated_volume_numeric'),
                   model_uri=DEFAULT_.estimated_volume_numeric, domain=None, range=Optional[int])

slots.computed_volume_numeric = Slot(uri=DEFAULT_.computed_volume_numeric, name="computed_volume_numeric", curie=DEFAULT_.curie('computed_volume_numeric'),
                   model_uri=DEFAULT_.computed_volume_numeric, domain=None, range=Optional[int])

slots.depth = Slot(uri=DEFAULT_.depth, name="depth", curie=DEFAULT_.curie('depth'),
                   model_uri=DEFAULT_.depth, domain=None, range=Optional[Union[str, "DepthEnum"]])

slots.lesion_bulky = Slot(uri=DEFAULT_.lesion_bulky, name="lesion_bulky", curie=DEFAULT_.curie('lesion_bulky'),
                   model_uri=DEFAULT_.lesion_bulky, domain=None, range=Optional[Union[str, "LesionBulkyEnum"]])

slots.laterality = Slot(uri=DEFAULT_.laterality, name="laterality", curie=DEFAULT_.curie('laterality'),
                   model_uri=DEFAULT_.laterality, domain=None, range=Optional[Union[str, "LateralityEnum"]])

slots.invasiveness = Slot(uri=DEFAULT_.invasiveness, name="invasiveness", curie=DEFAULT_.curie('invasiveness'),
                   model_uri=DEFAULT_.invasiveness, domain=None, range=Optional[Union[str, "InvasivenessEnum"]])

slots.extension_site = Slot(uri=DEFAULT_.extension_site, name="extension_site", curie=DEFAULT_.curie('extension_site'),
                   model_uri=DEFAULT_.extension_site, domain=None, range=Optional[Union[str, "ExtensionSiteEnum"]])

slots.lesion_response = Slot(uri=DEFAULT_.lesion_response, name="lesion_response", curie=DEFAULT_.curie('lesion_response'),
                   model_uri=DEFAULT_.lesion_response, domain=None, range=Optional[Union[str, "LesionResponseEnum"]])

slots.lesion_pct_change = Slot(uri=DEFAULT_.lesion_pct_change, name="lesion_pct_change", curie=DEFAULT_.curie('lesion_pct_change'),
                   model_uri=DEFAULT_.lesion_pct_change, domain=None, range=Optional[int])

slots.nodal_involvement = Slot(uri=DEFAULT_.nodal_involvement, name="nodal_involvement", curie=DEFAULT_.curie('nodal_involvement'),
                   model_uri=DEFAULT_.nodal_involvement, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.nodal_site = Slot(uri=DEFAULT_.nodal_site, name="nodal_site", curie=DEFAULT_.curie('nodal_site'),
                   model_uri=DEFAULT_.nodal_site, domain=None, range=Optional[Union[str, "NodalSiteEnum"]])

slots.nodal_determination = Slot(uri=DEFAULT_.nodal_determination, name="nodal_determination", curie=DEFAULT_.curie('nodal_determination'),
                   model_uri=DEFAULT_.nodal_determination, domain=None, range=Optional[Union[str, "NodalDeterminationEnum"]])

slots.nodal_determination_source = Slot(uri=DEFAULT_.nodal_determination_source, name="nodal_determination_source", curie=DEFAULT_.curie('nodal_determination_source'),
                   model_uri=DEFAULT_.nodal_determination_source, domain=None, range=Optional[Union[str, "NodalDeterminationSourceEnum"]])

slots.mibg_avidity = Slot(uri=DEFAULT_.mibg_avidity, name="mibg_avidity", curie=DEFAULT_.curie('mibg_avidity'),
                   model_uri=DEFAULT_.mibg_avidity, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.necrosis = Slot(uri=DEFAULT_.necrosis, name="necrosis", curie=DEFAULT_.curie('necrosis'),
                   model_uri=DEFAULT_.necrosis, domain=None, range=Optional[Union[str, "NecrosisEnum"]])

slots.necrosis_pct = Slot(uri=DEFAULT_.necrosis_pct, name="necrosis_pct", curie=DEFAULT_.curie('necrosis_pct'),
                   model_uri=DEFAULT_.necrosis_pct, domain=None, range=Optional[int])

slots.parameningeal_extension = Slot(uri=DEFAULT_.parameningeal_extension, name="parameningeal_extension", curie=DEFAULT_.curie('parameningeal_extension'),
                   model_uri=DEFAULT_.parameningeal_extension, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.skip_lesion = Slot(uri=DEFAULT_.skip_lesion, name="skip_lesion", curie=DEFAULT_.curie('skip_lesion'),
                   model_uri=DEFAULT_.skip_lesion, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.ipsilateral_nodules = Slot(uri=DEFAULT_.ipsilateral_nodules, name="ipsilateral_nodules", curie=DEFAULT_.curie('ipsilateral_nodules'),
                   model_uri=DEFAULT_.ipsilateral_nodules, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.joint_involvement = Slot(uri=DEFAULT_.joint_involvement, name="joint_involvement", curie=DEFAULT_.curie('joint_involvement'),
                   model_uri=DEFAULT_.joint_involvement, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.site_within_bone = Slot(uri=DEFAULT_.site_within_bone, name="site_within_bone", curie=DEFAULT_.curie('site_within_bone'),
                   model_uri=DEFAULT_.site_within_bone, domain=None, range=Optional[Union[str, "SiteWithinBoneEnum"]])

slots.cartilage_percent = Slot(uri=DEFAULT_.cartilage_percent, name="cartilage_percent", curie=DEFAULT_.curie('cartilage_percent'),
                   model_uri=DEFAULT_.cartilage_percent, domain=None, range=Optional[int])

slots.peritoneal_cytology = Slot(uri=DEFAULT_.peritoneal_cytology, name="peritoneal_cytology", curie=DEFAULT_.curie('peritoneal_cytology'),
                   model_uri=DEFAULT_.peritoneal_cytology, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.pleural_cytology = Slot(uri=DEFAULT_.pleural_cytology, name="pleural_cytology", curie=DEFAULT_.curie('pleural_cytology'),
                   model_uri=DEFAULT_.pleural_cytology, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.peritoneal_effusion = Slot(uri=DEFAULT_.peritoneal_effusion, name="peritoneal_effusion", curie=DEFAULT_.curie('peritoneal_effusion'),
                   model_uri=DEFAULT_.peritoneal_effusion, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.pleural_effusion = Slot(uri=DEFAULT_.pleural_effusion, name="pleural_effusion", curie=DEFAULT_.curie('pleural_effusion'),
                   model_uri=DEFAULT_.pleural_effusion, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.pericardial_effusion = Slot(uri=DEFAULT_.pericardial_effusion, name="pericardial_effusion", curie=DEFAULT_.curie('pericardial_effusion'),
                   model_uri=DEFAULT_.pericardial_effusion, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.e_extension_site = Slot(uri=DEFAULT_.e_extension_site, name="e_extension_site", curie=DEFAULT_.curie('e_extension_site'),
                   model_uri=DEFAULT_.e_extension_site, domain=None, range=Optional[Union[str, "EExtensionSiteEnum"]])

slots.anaplasia = Slot(uri=DEFAULT_.anaplasia, name="anaplasia", curie=DEFAULT_.curie('anaplasia'),
                   model_uri=DEFAULT_.anaplasia, domain=None, range=Optional[Union[str, "AbsentNotreportedPresentUnknownEnum"]])

slots.anaplasia_extent = Slot(uri=DEFAULT_.anaplasia_extent, name="anaplasia_extent", curie=DEFAULT_.curie('anaplasia_extent'),
                   model_uri=DEFAULT_.anaplasia_extent, domain=None, range=Optional[Union[str, "AnaplasiaExtentEnum"]])

slots.age_at_staging = Slot(uri=DEFAULT_.age_at_staging, name="age_at_staging", curie=DEFAULT_.curie('age_at_staging'),
                   model_uri=DEFAULT_.age_at_staging, domain=None, range=Optional[int])

slots.stage_system = Slot(uri=DEFAULT_.stage_system, name="stage_system", curie=DEFAULT_.curie('stage_system'),
                   model_uri=DEFAULT_.stage_system, domain=None, range=Optional[Union[str, "StageSystemEnum"]])

slots.stage = Slot(uri=DEFAULT_.stage, name="stage", curie=DEFAULT_.curie('stage'),
                   model_uri=DEFAULT_.stage, domain=None, range=Optional[Union[str, "StageEnum"]])

slots.ann_arbor_mod_ab = Slot(uri=DEFAULT_.ann_arbor_mod_ab, name="ann_arbor_mod_ab", curie=DEFAULT_.curie('ann_arbor_mod_ab'),
                   model_uri=DEFAULT_.ann_arbor_mod_ab, domain=None, range=Optional[Union[str, "AnnArborModAbEnum"]])

slots.ann_arbor_mod_e = Slot(uri=DEFAULT_.ann_arbor_mod_e, name="ann_arbor_mod_e", curie=DEFAULT_.curie('ann_arbor_mod_e'),
                   model_uri=DEFAULT_.ann_arbor_mod_e, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.ann_arbor_mod_s = Slot(uri=DEFAULT_.ann_arbor_mod_s, name="ann_arbor_mod_s", curie=DEFAULT_.curie('ann_arbor_mod_s'),
                   model_uri=DEFAULT_.ann_arbor_mod_s, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.tnm_finding = Slot(uri=DEFAULT_.tnm_finding, name="tnm_finding", curie=DEFAULT_.curie('tnm_finding'),
                   model_uri=DEFAULT_.tnm_finding, domain=None, range=Optional[Union[str, "TnmFindingEnum"]])

slots.irs_group = Slot(uri=DEFAULT_.irs_group, name="irs_group", curie=DEFAULT_.curie('irs_group'),
                   model_uri=DEFAULT_.irs_group, domain=None, range=Optional[Union[str, "IrsGroupEnum"]])

slots.age_at_hist_assessment = Slot(uri=DEFAULT_.age_at_hist_assessment, name="age_at_hist_assessment", curie=DEFAULT_.curie('age_at_hist_assessment'),
                   model_uri=DEFAULT_.age_at_hist_assessment, domain=None, range=Optional[int])

slots.hist_assessment_review = Slot(uri=DEFAULT_.hist_assessment_review, name="hist_assessment_review", curie=DEFAULT_.curie('hist_assessment_review'),
                   model_uri=DEFAULT_.hist_assessment_review, domain=None, range=Optional[Union[str, "HistAssessmentReviewEnum"]])

slots.histology = Slot(uri=DEFAULT_.histology, name="histology", curie=DEFAULT_.curie('histology'),
                   model_uri=DEFAULT_.histology, domain=None, range=Optional[Union[str, "HistologyEnum"]])

slots.histology_result = Slot(uri=DEFAULT_.histology_result, name="histology_result", curie=DEFAULT_.curie('histology_result'),
                   model_uri=DEFAULT_.histology_result, domain=None, range=Optional[str])

slots.histology_result_numeric = Slot(uri=DEFAULT_.histology_result_numeric, name="histology_result_numeric", curie=DEFAULT_.curie('histology_result_numeric'),
                   model_uri=DEFAULT_.histology_result_numeric, domain=None, range=Optional[int])

slots.histology_result_unit = Slot(uri=DEFAULT_.histology_result_unit, name="histology_result_unit", curie=DEFAULT_.curie('histology_result_unit'),
                   model_uri=DEFAULT_.histology_result_unit, domain=None, range=Optional[Union[str, "NotreportedUnknownEnum"]])

slots.histology_grade = Slot(uri=DEFAULT_.histology_grade, name="histology_grade", curie=DEFAULT_.curie('histology_grade'),
                   model_uri=DEFAULT_.histology_grade, domain=None, range=Optional[Union[str, "HistologyGradeEnum"]])

slots.hist_icd_o_morph_code = Slot(uri=DEFAULT_.hist_icd_o_morph_code, name="hist_icd_o_morph_code", curie=DEFAULT_.curie('hist_icd_o_morph_code'),
                   model_uri=DEFAULT_.hist_icd_o_morph_code, domain=None, range=Optional[str])

slots.mature_glial_implants = Slot(uri=DEFAULT_.mature_glial_implants, name="mature_glial_implants", curie=DEFAULT_.curie('mature_glial_implants'),
                   model_uri=DEFAULT_.mature_glial_implants, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.somatic_malignancy_type = Slot(uri=DEFAULT_.somatic_malignancy_type, name="somatic_malignancy_type", curie=DEFAULT_.curie('somatic_malignancy_type'),
                   model_uri=DEFAULT_.somatic_malignancy_type, domain=None, range=Optional[Union[str, "SomaticMalignancyTypeEnum"]])

slots.histology_inpc = Slot(uri=DEFAULT_.histology_inpc, name="histology_inpc", curie=DEFAULT_.curie('histology_inpc'),
                   model_uri=DEFAULT_.histology_inpc, domain=None, range=Optional[Union[str, "HistologyInpcEnum"]])

slots.who_aml = Slot(uri=DEFAULT_.who_aml, name="who_aml", curie=DEFAULT_.curie('who_aml'),
                   model_uri=DEFAULT_.who_aml, domain=None, range=Optional[Union[str, "WhoAmlEnum"]])

slots.fab_type = Slot(uri=DEFAULT_.fab_type, name="fab_type", curie=DEFAULT_.curie('fab_type'),
                   model_uri=DEFAULT_.fab_type, domain=None, range=Optional[Union[str, "FabTypeEnum"]])

slots.all_type = Slot(uri=DEFAULT_.all_type, name="all_type", curie=DEFAULT_.curie('all_type'),
                   model_uri=DEFAULT_.all_type, domain=None, range=Optional[Union[str, "AllTypeEnum"]])

slots.mpal = Slot(uri=DEFAULT_.mpal, name="mpal", curie=DEFAULT_.curie('mpal'),
                   model_uri=DEFAULT_.mpal, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.mlds = Slot(uri=DEFAULT_.mlds, name="mlds", curie=DEFAULT_.curie('mlds'),
                   model_uri=DEFAULT_.mlds, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.tamds = Slot(uri=DEFAULT_.tamds, name="tamds", curie=DEFAULT_.curie('tamds'),
                   model_uri=DEFAULT_.tamds, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.secondary_aml = Slot(uri=DEFAULT_.secondary_aml, name="secondary_aml", curie=DEFAULT_.curie('secondary_aml'),
                   model_uri=DEFAULT_.secondary_aml, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.risk_group_system = Slot(uri=DEFAULT_.risk_group_system, name="risk_group_system", curie=DEFAULT_.curie('risk_group_system'),
                   model_uri=DEFAULT_.risk_group_system, domain=None, range=Optional[Union[str, "RiskGroupSystemEnum"]])

slots.risk_group = Slot(uri=DEFAULT_.risk_group, name="risk_group", curie=DEFAULT_.curie('risk_group'),
                   model_uri=DEFAULT_.risk_group, domain=None, range=Optional[Union[str, "RiskGroupEnum"]])

slots.mki = Slot(uri=DEFAULT_.mki, name="mki", curie=DEFAULT_.curie('mki'),
                   model_uri=DEFAULT_.mki, domain=None, range=Optional[Union[str, "MkiEnum"]])

slots.disease_site = Slot(uri=DEFAULT_.disease_site, name="disease_site", curie=DEFAULT_.curie('disease_site'),
                   model_uri=DEFAULT_.disease_site, domain=None, range=Optional[Union[str, "DiseaseSiteEnum"]])

slots.cns_disease_status = Slot(uri=DEFAULT_.cns_disease_status, name="cns_disease_status", curie=DEFAULT_.curie('cns_disease_status'),
                   model_uri=DEFAULT_.cns_disease_status, domain=None, range=Optional[Union[str, "CnsDiseaseStatusEnum"]])

slots.performance_score = Slot(uri=DEFAULT_.performance_score, name="performance_score", curie=DEFAULT_.curie('performance_score'),
                   model_uri=DEFAULT_.performance_score, domain=None, range=Optional[Union[str, "PerformanceScoreEnum"]])

slots.performance_score_system = Slot(uri=DEFAULT_.performance_score_system, name="performance_score_system", curie=DEFAULT_.curie('performance_score_system'),
                   model_uri=DEFAULT_.performance_score_system, domain=None, range=Optional[Union[str, "PerformanceScoreSystemEnum"]])

slots.gpoh_score = Slot(uri=DEFAULT_.gpoh_score, name="gpoh_score", curie=DEFAULT_.curie('gpoh_score'),
                   model_uri=DEFAULT_.gpoh_score, domain=None, range=Optional[Union[str, "GpohScoreEnum"]])

slots.prior_steroids_week = Slot(uri=DEFAULT_.prior_steroids_week, name="prior_steroids_week", curie=DEFAULT_.curie('prior_steroids_week'),
                   model_uri=DEFAULT_.prior_steroids_week, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.prior_steroids_month = Slot(uri=DEFAULT_.prior_steroids_month, name="prior_steroids_month", curie=DEFAULT_.curie('prior_steroids_month'),
                   model_uri=DEFAULT_.prior_steroids_month, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.bulk_disease = Slot(uri=DEFAULT_.bulk_disease, name="bulk_disease", curie=DEFAULT_.curie('bulk_disease'),
                   model_uri=DEFAULT_.bulk_disease, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.bulk_nodal_aggregate = Slot(uri=DEFAULT_.bulk_nodal_aggregate, name="bulk_nodal_aggregate", curie=DEFAULT_.curie('bulk_nodal_aggregate'),
                   model_uri=DEFAULT_.bulk_nodal_aggregate, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.bulk_med_mass = Slot(uri=DEFAULT_.bulk_med_mass, name="bulk_med_mass", curie=DEFAULT_.curie('bulk_med_mass'),
                   model_uri=DEFAULT_.bulk_med_mass, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.med_ratio = Slot(uri=DEFAULT_.med_ratio, name="med_ratio", curie=DEFAULT_.curie('med_ratio'),
                   model_uri=DEFAULT_.med_ratio, domain=None, range=Optional[int])

slots.fever = Slot(uri=DEFAULT_.fever, name="fever", curie=DEFAULT_.curie('fever'),
                   model_uri=DEFAULT_.fever, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.night_sweats = Slot(uri=DEFAULT_.night_sweats, name="night_sweats", curie=DEFAULT_.curie('night_sweats'),
                   model_uri=DEFAULT_.night_sweats, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.weight_loss = Slot(uri=DEFAULT_.weight_loss, name="weight_loss", curie=DEFAULT_.curie('weight_loss'),
                   model_uri=DEFAULT_.weight_loss, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.nodular_splenic = Slot(uri=DEFAULT_.nodular_splenic, name="nodular_splenic", curie=DEFAULT_.curie('nodular_splenic'),
                   model_uri=DEFAULT_.nodular_splenic, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.initial_treatment_category = Slot(uri=DEFAULT_.initial_treatment_category, name="initial_treatment_category", curie=DEFAULT_.curie('initial_treatment_category'),
                   model_uri=DEFAULT_.initial_treatment_category, domain=None, range=Optional[Union[str, "InitialTreatmentCategoryEnum"]])

slots.myeloid_sarcoma = Slot(uri=DEFAULT_.myeloid_sarcoma, name="myeloid_sarcoma", curie=DEFAULT_.curie('myeloid_sarcoma'),
                   model_uri=DEFAULT_.myeloid_sarcoma, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.myeloid_sarcoma_site = Slot(uri=DEFAULT_.myeloid_sarcoma_site, name="myeloid_sarcoma_site", curie=DEFAULT_.curie('myeloid_sarcoma_site'),
                   model_uri=DEFAULT_.myeloid_sarcoma_site, domain=None, range=Optional[Union[str, "MyeloidSarcomaSiteEnum"]])

slots.gts = Slot(uri=DEFAULT_.gts, name="gts", curie=DEFAULT_.curie('gts'),
                   model_uri=DEFAULT_.gts, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.gts_treatment = Slot(uri=DEFAULT_.gts_treatment, name="gts_treatment", curie=DEFAULT_.curie('gts_treatment'),
                   model_uri=DEFAULT_.gts_treatment, domain=None, range=Optional[Union[str, "GtsTreatmentEnum"]])

slots.age_at_medication_start = Slot(uri=DEFAULT_.age_at_medication_start, name="age_at_medication_start", curie=DEFAULT_.curie('age_at_medication_start'),
                   model_uri=DEFAULT_.age_at_medication_start, domain=None, range=Optional[int])

slots.age_at_medication_end = Slot(uri=DEFAULT_.age_at_medication_end, name="age_at_medication_end", curie=DEFAULT_.curie('age_at_medication_end'),
                   model_uri=DEFAULT_.age_at_medication_end, domain=None, range=Optional[int])

slots.administration_status = Slot(uri=DEFAULT_.administration_status, name="administration_status", curie=DEFAULT_.curie('administration_status'),
                   model_uri=DEFAULT_.administration_status, domain=None, range=Optional[Union[str, "AdministrationStatusEnum"]])

slots.medication = Slot(uri=DEFAULT_.medication, name="medication", curie=DEFAULT_.curie('medication'),
                   model_uri=DEFAULT_.medication, domain=None, range=Optional[Union[str, "MedicationEnum"]])

slots.protocol_medication = Slot(uri=DEFAULT_.protocol_medication, name="protocol_medication", curie=DEFAULT_.curie('protocol_medication'),
                   model_uri=DEFAULT_.protocol_medication, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.non_protocol_timing = Slot(uri=DEFAULT_.non_protocol_timing, name="non_protocol_timing", curie=DEFAULT_.curie('non_protocol_timing'),
                   model_uri=DEFAULT_.non_protocol_timing, domain=None, range=Optional[Union[str, "NonProtocolTimingEnum"]])

slots.non_protocol_reason = Slot(uri=DEFAULT_.non_protocol_reason, name="non_protocol_reason", curie=DEFAULT_.curie('non_protocol_reason'),
                   model_uri=DEFAULT_.non_protocol_reason, domain=None, range=Optional[Union[str, "NonProtocolReasonEnum"]])

slots.route = Slot(uri=DEFAULT_.route, name="route", curie=DEFAULT_.curie('route'),
                   model_uri=DEFAULT_.route, domain=None, range=Optional[Union[str, "RouteEnum"]])

slots.route_detail = Slot(uri=DEFAULT_.route_detail, name="route_detail", curie=DEFAULT_.curie('route_detail'),
                   model_uri=DEFAULT_.route_detail, domain=None, range=Optional[Union[str, "RouteDetailEnum"]])

slots.normalization_basis = Slot(uri=DEFAULT_.normalization_basis, name="normalization_basis", curie=DEFAULT_.curie('normalization_basis'),
                   model_uri=DEFAULT_.normalization_basis, domain=None, range=Optional[Union[str, "NormalizationBasisEnum"]])

slots.number_doses = Slot(uri=DEFAULT_.number_doses, name="number_doses", curie=DEFAULT_.curie('number_doses'),
                   model_uri=DEFAULT_.number_doses, domain=None, range=Optional[int])

slots.total_dose_administered = Slot(uri=DEFAULT_.total_dose_administered, name="total_dose_administered", curie=DEFAULT_.curie('total_dose_administered'),
                   model_uri=DEFAULT_.total_dose_administered, domain=None, range=Optional[int])

slots.total_dose_intended = Slot(uri=DEFAULT_.total_dose_intended, name="total_dose_intended", curie=DEFAULT_.curie('total_dose_intended'),
                   model_uri=DEFAULT_.total_dose_intended, domain=None, range=Optional[int])

slots.total_dose_units = Slot(uri=DEFAULT_.total_dose_units, name="total_dose_units", curie=DEFAULT_.curie('total_dose_units'),
                   model_uri=DEFAULT_.total_dose_units, domain=None, range=Optional[Union[str, "TotalDoseUnitsEnum"]])

slots.age_at_mod = Slot(uri=DEFAULT_.age_at_mod, name="age_at_mod", curie=DEFAULT_.curie('age_at_mod'),
                   model_uri=DEFAULT_.age_at_mod, domain=None, range=Optional[int])

slots.mod_type = Slot(uri=DEFAULT_.mod_type, name="mod_type", curie=DEFAULT_.curie('mod_type'),
                   model_uri=DEFAULT_.mod_type, domain=None, range=Optional[Union[str, "ModTypeEnum"]])

slots.mod_rationale = Slot(uri=DEFAULT_.mod_rationale, name="mod_rationale", curie=DEFAULT_.curie('mod_rationale'),
                   model_uri=DEFAULT_.mod_rationale, domain=None, range=Optional[Union[str, "ModRationaleEnum"]])

slots.mod_reason = Slot(uri=DEFAULT_.mod_reason, name="mod_reason", curie=DEFAULT_.curie('mod_reason'),
                   model_uri=DEFAULT_.mod_reason, domain=None, range=Optional[Union[str, "ModReasonEnum"]])

slots.toxicity_detail = Slot(uri=DEFAULT_.toxicity_detail, name="toxicity_detail", curie=DEFAULT_.curie('toxicity_detail'),
                   model_uri=DEFAULT_.toxicity_detail, domain=None, range=Optional[Union[str, "ToxicityDetailEnum"]])

slots.toxicity_immune = Slot(uri=DEFAULT_.toxicity_immune, name="toxicity_immune", curie=DEFAULT_.curie('toxicity_immune'),
                   model_uri=DEFAULT_.toxicity_immune, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.toxicity_infusion = Slot(uri=DEFAULT_.toxicity_infusion, name="toxicity_infusion", curie=DEFAULT_.curie('toxicity_infusion'),
                   model_uri=DEFAULT_.toxicity_infusion, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.original_agent = Slot(uri=DEFAULT_.original_agent, name="original_agent", curie=DEFAULT_.curie('original_agent'),
                   model_uri=DEFAULT_.original_agent, domain=None, range=Optional[Union[str, "BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum"]])

slots.sub_agent = Slot(uri=DEFAULT_.sub_agent, name="sub_agent", curie=DEFAULT_.curie('sub_agent'),
                   model_uri=DEFAULT_.sub_agent, domain=None, range=Optional[Union[str, "BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum"]])

slots.age_at_rt_start = Slot(uri=DEFAULT_.age_at_rt_start, name="age_at_rt_start", curie=DEFAULT_.curie('age_at_rt_start'),
                   model_uri=DEFAULT_.age_at_rt_start, domain=None, range=Optional[int])

slots.age_at_rt_end = Slot(uri=DEFAULT_.age_at_rt_end, name="age_at_rt_end", curie=DEFAULT_.curie('age_at_rt_end'),
                   model_uri=DEFAULT_.age_at_rt_end, domain=None, range=Optional[int])

slots.protocol_radiation_therapy = Slot(uri=DEFAULT_.protocol_radiation_therapy, name="protocol_radiation_therapy", curie=DEFAULT_.curie('protocol_radiation_therapy'),
                   model_uri=DEFAULT_.protocol_radiation_therapy, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.tumor_classification = Slot(uri=DEFAULT_.tumor_classification, name="tumor_classification", curie=DEFAULT_.curie('tumor_classification'),
                   model_uri=DEFAULT_.tumor_classification, domain=None, range=Optional[Union[str, "TumorClassificationEnum"]])

slots.tumor_tissue_type = Slot(uri=DEFAULT_.tumor_tissue_type, name="tumor_tissue_type", curie=DEFAULT_.curie('tumor_tissue_type'),
                   model_uri=DEFAULT_.tumor_tissue_type, domain=None, range=Optional[Union[str, "BoneNotreportedSofttissueUnknownEnum"]])

slots.rt_site = Slot(uri=DEFAULT_.rt_site, name="rt_site", curie=DEFAULT_.curie('rt_site'),
                   model_uri=DEFAULT_.rt_site, domain=None, range=Optional[Union[str, "RtSiteEnum"]])

slots.energy_type = Slot(uri=DEFAULT_.energy_type, name="energy_type", curie=DEFAULT_.curie('energy_type'),
                   model_uri=DEFAULT_.energy_type, domain=None, range=Optional[Union[str, "EnergyTypeEnum"]])

slots.rt_dose = Slot(uri=DEFAULT_.rt_dose, name="rt_dose", curie=DEFAULT_.curie('rt_dose'),
                   model_uri=DEFAULT_.rt_dose, domain=None, range=Optional[int])

slots.rt_unit = Slot(uri=DEFAULT_.rt_unit, name="rt_unit", curie=DEFAULT_.curie('rt_unit'),
                   model_uri=DEFAULT_.rt_unit, domain=None, range=Optional[Union[str, "RtUnitEnum"]])

slots.boost = Slot(uri=DEFAULT_.boost, name="boost", curie=DEFAULT_.curie('boost'),
                   model_uri=DEFAULT_.boost, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.boost_dose = Slot(uri=DEFAULT_.boost_dose, name="boost_dose", curie=DEFAULT_.curie('boost_dose'),
                   model_uri=DEFAULT_.boost_dose, domain=None, range=Optional[int])

slots.num_fraction = Slot(uri=DEFAULT_.num_fraction, name="num_fraction", curie=DEFAULT_.curie('num_fraction'),
                   model_uri=DEFAULT_.num_fraction, domain=None, range=Optional[int])

slots.transposition_organ = Slot(uri=DEFAULT_.transposition_organ, name="transposition_organ", curie=DEFAULT_.curie('transposition_organ'),
                   model_uri=DEFAULT_.transposition_organ, domain=None, range=Optional[Union[str, "TranspositionOrganEnum"]])

slots.age_at_procedure = Slot(uri=DEFAULT_.age_at_procedure, name="age_at_procedure", curie=DEFAULT_.curie('age_at_procedure'),
                   model_uri=DEFAULT_.age_at_procedure, domain=None, range=Optional[int])

slots.protocol_procedure = Slot(uri=DEFAULT_.protocol_procedure, name="protocol_procedure", curie=DEFAULT_.curie('protocol_procedure'),
                   model_uri=DEFAULT_.protocol_procedure, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.procedure_site = Slot(uri=DEFAULT_.procedure_site, name="procedure_site", curie=DEFAULT_.curie('procedure_site'),
                   model_uri=DEFAULT_.procedure_site, domain=None, range=Optional[Union[str, "ProcedureSiteEnum"]])

slots.procedure_laterality = Slot(uri=DEFAULT_.procedure_laterality, name="procedure_laterality", curie=DEFAULT_.curie('procedure_laterality'),
                   model_uri=DEFAULT_.procedure_laterality, domain=None, range=Optional[Union[str, "ProcedureLateralityEnum"]])

slots.procedure_type = Slot(uri=DEFAULT_.procedure_type, name="procedure_type", curie=DEFAULT_.curie('procedure_type'),
                   model_uri=DEFAULT_.procedure_type, domain=None, range=Optional[Union[str, "ProcedureTypeEnum"]])

slots.surgery_type_limb = Slot(uri=DEFAULT_.surgery_type_limb, name="surgery_type_limb", curie=DEFAULT_.curie('surgery_type_limb'),
                   model_uri=DEFAULT_.surgery_type_limb, domain=None, range=Optional[Union[str, "SurgeryTypeLimbEnum"]])

slots.amputation_type = Slot(uri=DEFAULT_.amputation_type, name="amputation_type", curie=DEFAULT_.curie('amputation_type'),
                   model_uri=DEFAULT_.amputation_type, domain=None, range=Optional[Union[str, "AmputationTypeEnum"]])

slots.resection_type = Slot(uri=DEFAULT_.resection_type, name="resection_type", curie=DEFAULT_.curie('resection_type'),
                   model_uri=DEFAULT_.resection_type, domain=None, range=Optional[Union[str, "ResectionTypeEnum"]])

slots.surgery_type_limb_salvage = Slot(uri=DEFAULT_.surgery_type_limb_salvage, name="surgery_type_limb_salvage", curie=DEFAULT_.curie('surgery_type_limb_salvage'),
                   model_uri=DEFAULT_.surgery_type_limb_salvage, domain=None, range=Optional[Union[str, "SurgeryTypeLimbSalvageEnum"]])

slots.reconstruction_type = Slot(uri=DEFAULT_.reconstruction_type, name="reconstruction_type", curie=DEFAULT_.curie('reconstruction_type'),
                   model_uri=DEFAULT_.reconstruction_type, domain=None, range=Optional[Union[str, "ReconstructionTypeEnum"]])

slots.procedure_extent = Slot(uri=DEFAULT_.procedure_extent, name="procedure_extent", curie=DEFAULT_.curie('procedure_extent'),
                   model_uri=DEFAULT_.procedure_extent, domain=None, range=Optional[Union[str, "ProcedureExtentEnum"]])

slots.margins = Slot(uri=DEFAULT_.margins, name="margins", curie=DEFAULT_.curie('margins'),
                   model_uri=DEFAULT_.margins, domain=None, range=Optional[Union[str, "MarginsEnum"]])

slots.biopsy_type = Slot(uri=DEFAULT_.biopsy_type, name="biopsy_type", curie=DEFAULT_.curie('biopsy_type'),
                   model_uri=DEFAULT_.biopsy_type, domain=None, range=Optional[Union[str, "BiopsyTypeEnum"]])

slots.met_non_lung_mgmt = Slot(uri=DEFAULT_.met_non_lung_mgmt, name="met_non_lung_mgmt", curie=DEFAULT_.curie('met_non_lung_mgmt'),
                   model_uri=DEFAULT_.met_non_lung_mgmt, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.met_lung_mgmt = Slot(uri=DEFAULT_.met_lung_mgmt, name="met_lung_mgmt", curie=DEFAULT_.curie('met_lung_mgmt'),
                   model_uri=DEFAULT_.met_lung_mgmt, domain=None, range=Optional[Union[str, "MetLungMgmtEnum"]])

slots.localization_technique = Slot(uri=DEFAULT_.localization_technique, name="localization_technique", curie=DEFAULT_.curie('localization_technique'),
                   model_uri=DEFAULT_.localization_technique, domain=None, range=Optional[Union[str, "LocalizationTechniqueEnum"]])

slots.distance_margin_tumor = Slot(uri=DEFAULT_.distance_margin_tumor, name="distance_margin_tumor", curie=DEFAULT_.curie('distance_margin_tumor'),
                   model_uri=DEFAULT_.distance_margin_tumor, domain=None, range=Optional[int])

slots.pelvic_involvement = Slot(uri=DEFAULT_.pelvic_involvement, name="pelvic_involvement", curie=DEFAULT_.curie('pelvic_involvement'),
                   model_uri=DEFAULT_.pelvic_involvement, domain=None, range=Optional[Union[str, "PelvicInvolvementEnum"]])

slots.surgery = Slot(uri=DEFAULT_.surgery, name="surgery", curie=DEFAULT_.curie('surgery'),
                   model_uri=DEFAULT_.surgery, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.number_nodes = Slot(uri=DEFAULT_.number_nodes, name="number_nodes", curie=DEFAULT_.curie('number_nodes'),
                   model_uri=DEFAULT_.number_nodes, domain=None, range=Optional[Union[str, "NumberNodesEnum"]])

slots.number_nodes_numeric = Slot(uri=DEFAULT_.number_nodes_numeric, name="number_nodes_numeric", curie=DEFAULT_.curie('number_nodes_numeric'),
                   model_uri=DEFAULT_.number_nodes_numeric, domain=None, range=Optional[int])

slots.procedure_purpose = Slot(uri=DEFAULT_.procedure_purpose, name="procedure_purpose", curie=DEFAULT_.curie('procedure_purpose'),
                   model_uri=DEFAULT_.procedure_purpose, domain=None, range=Optional[Union[str, "ProcedurePurposeEnum"]])

slots.age_at_tmp_start = Slot(uri=DEFAULT_.age_at_tmp_start, name="age_at_tmp_start", curie=DEFAULT_.curie('age_at_tmp_start'),
                   model_uri=DEFAULT_.age_at_tmp_start, domain=None, range=Optional[int])

slots.protocol_transfusion = Slot(uri=DEFAULT_.protocol_transfusion, name="protocol_transfusion", curie=DEFAULT_.curie('protocol_transfusion'),
                   model_uri=DEFAULT_.protocol_transfusion, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.tmp_type = Slot(uri=DEFAULT_.tmp_type, name="tmp_type", curie=DEFAULT_.curie('tmp_type'),
                   model_uri=DEFAULT_.tmp_type, domain=None, range=Optional[Union[str, "TmpTypeEnum"]])

slots.tmp_product = Slot(uri=DEFAULT_.tmp_product, name="tmp_product", curie=DEFAULT_.curie('tmp_product'),
                   model_uri=DEFAULT_.tmp_product, domain=None, range=Optional[Union[str, "TmpProductEnum"]])

slots.tmp_product_type = Slot(uri=DEFAULT_.tmp_product_type, name="tmp_product_type", curie=DEFAULT_.curie('tmp_product_type'),
                   model_uri=DEFAULT_.tmp_product_type, domain=None, range=Optional[Union[str, "TmpProductTypeEnum"]])

slots.tmp_number_units = Slot(uri=DEFAULT_.tmp_number_units, name="tmp_number_units", curie=DEFAULT_.curie('tmp_number_units'),
                   model_uri=DEFAULT_.tmp_number_units, domain=None, range=Optional[int])

slots.age_at_cimt_start = Slot(uri=DEFAULT_.age_at_cimt_start, name="age_at_cimt_start", curie=DEFAULT_.curie('age_at_cimt_start'),
                   model_uri=DEFAULT_.age_at_cimt_start, domain=None, range=Optional[int])

slots.protocol_cimt = Slot(uri=DEFAULT_.protocol_cimt, name="protocol_cimt", curie=DEFAULT_.curie('protocol_cimt'),
                   model_uri=DEFAULT_.protocol_cimt, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.cimt_type = Slot(uri=DEFAULT_.cimt_type, name="cimt_type", curie=DEFAULT_.curie('cimt_type'),
                   model_uri=DEFAULT_.cimt_type, domain=None, range=Optional[Union[str, "CimtTypeEnum"]])

slots.age_at_sct = Slot(uri=DEFAULT_.age_at_sct, name="age_at_sct", curie=DEFAULT_.curie('age_at_sct'),
                   model_uri=DEFAULT_.age_at_sct, domain=None, range=Optional[int])

slots.protocol_sct = Slot(uri=DEFAULT_.protocol_sct, name="protocol_sct", curie=DEFAULT_.curie('protocol_sct'),
                   model_uri=DEFAULT_.protocol_sct, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.sct_type = Slot(uri=DEFAULT_.sct_type, name="sct_type", curie=DEFAULT_.curie('sct_type'),
                   model_uri=DEFAULT_.sct_type, domain=None, range=Optional[Union[str, "SctTypeEnum"]])

slots.sct_source = Slot(uri=DEFAULT_.sct_source, name="sct_source", curie=DEFAULT_.curie('sct_source'),
                   model_uri=DEFAULT_.sct_source, domain=None, range=Optional[Union[str, "SctSourceEnum"]])

slots.sct_donor_relationship = Slot(uri=DEFAULT_.sct_donor_relationship, name="sct_donor_relationship", curie=DEFAULT_.curie('sct_donor_relationship'),
                   model_uri=DEFAULT_.sct_donor_relationship, domain=None, range=Optional[Union[str, "SctDonorRelationshipEnum"]])

slots.hla_match = Slot(uri=DEFAULT_.hla_match, name="hla_match", curie=DEFAULT_.curie('hla_match'),
                   model_uri=DEFAULT_.hla_match, domain=None, range=Optional[Union[str, "HlaMatchEnum"]])

slots.number_hla = Slot(uri=DEFAULT_.number_hla, name="number_hla", curie=DEFAULT_.curie('number_hla'),
                   model_uri=DEFAULT_.number_hla, domain=None, range=Optional[int])

slots.number_matches = Slot(uri=DEFAULT_.number_matches, name="number_matches", curie=DEFAULT_.curie('number_matches'),
                   model_uri=DEFAULT_.number_matches, domain=None, range=Optional[int])

slots.hla_a_result = Slot(uri=DEFAULT_.hla_a_result, name="hla_a_result", curie=DEFAULT_.curie('hla_a_result'),
                   model_uri=DEFAULT_.hla_a_result, domain=None, range=Optional[Union[str, "BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum"]])

slots.hla_b_result = Slot(uri=DEFAULT_.hla_b_result, name="hla_b_result", curie=DEFAULT_.curie('hla_b_result'),
                   model_uri=DEFAULT_.hla_b_result, domain=None, range=Optional[Union[str, "BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum"]])

slots.hla_c_result = Slot(uri=DEFAULT_.hla_c_result, name="hla_c_result", curie=DEFAULT_.curie('hla_c_result'),
                   model_uri=DEFAULT_.hla_c_result, domain=None, range=Optional[Union[str, "BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum"]])

slots.hla_drb1_result = Slot(uri=DEFAULT_.hla_drb1_result, name="hla_drb1_result", curie=DEFAULT_.curie('hla_drb1_result'),
                   model_uri=DEFAULT_.hla_drb1_result, domain=None, range=Optional[Union[str, "BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum"]])

slots.hla_dq_result = Slot(uri=DEFAULT_.hla_dq_result, name="hla_dq_result", curie=DEFAULT_.curie('hla_dq_result'),
                   model_uri=DEFAULT_.hla_dq_result, domain=None, range=Optional[Union[str, "BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum"]])

slots.sct_conditioning_type = Slot(uri=DEFAULT_.sct_conditioning_type, name="sct_conditioning_type", curie=DEFAULT_.curie('sct_conditioning_type'),
                   model_uri=DEFAULT_.sct_conditioning_type, domain=None, range=Optional[Union[str, "SctConditioningTypeEnum"]])

slots.sct_tbi = Slot(uri=DEFAULT_.sct_tbi, name="sct_tbi", curie=DEFAULT_.curie('sct_tbi'),
                   model_uri=DEFAULT_.sct_tbi, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.sct_cycles = Slot(uri=DEFAULT_.sct_cycles, name="sct_cycles", curie=DEFAULT_.curie('sct_cycles'),
                   model_uri=DEFAULT_.sct_cycles, domain=None, range=Optional[Decimal])

slots.sct_cd34_coll = Slot(uri=DEFAULT_.sct_cd34_coll, name="sct_cd34_coll", curie=DEFAULT_.curie('sct_cd34_coll'),
                   model_uri=DEFAULT_.sct_cd34_coll, domain=None, range=Optional[Decimal])

slots.sct_cd34_transplant = Slot(uri=DEFAULT_.sct_cd34_transplant, name="sct_cd34_transplant", curie=DEFAULT_.curie('sct_cd34_transplant'),
                   model_uri=DEFAULT_.sct_cd34_transplant, domain=None, range=Optional[Decimal])

slots.age_at_response = Slot(uri=DEFAULT_.age_at_response, name="age_at_response", curie=DEFAULT_.curie('age_at_response'),
                   model_uri=DEFAULT_.age_at_response, domain=None, range=Optional[int])

slots.response_category = Slot(uri=DEFAULT_.response_category, name="response_category", curie=DEFAULT_.curie('response_category'),
                   model_uri=DEFAULT_.response_category, domain=None, range=Optional[Union[str, "ResponseCategoryEnum"]])

slots.tx_prior_response = Slot(uri=DEFAULT_.tx_prior_response, name="tx_prior_response", curie=DEFAULT_.curie('tx_prior_response'),
                   model_uri=DEFAULT_.tx_prior_response, domain=None, range=Optional[Union[str, "TxPriorResponseEnum"]])

slots.interim_response = Slot(uri=DEFAULT_.interim_response, name="interim_response", curie=DEFAULT_.curie('interim_response'),
                   model_uri=DEFAULT_.interim_response, domain=None, range=Optional[Union[str, "InterimResponseEnum"]])

slots.response = Slot(uri=DEFAULT_.response, name="response", curie=DEFAULT_.curie('response'),
                   model_uri=DEFAULT_.response, domain=None, range=Optional[Union[str, "ResponseEnum"]])

slots.response_method = Slot(uri=DEFAULT_.response_method, name="response_method", curie=DEFAULT_.curie('response_method'),
                   model_uri=DEFAULT_.response_method, domain=None, range=Optional[Union[str, "ResponseMethodEnum"]])

slots.response_system = Slot(uri=DEFAULT_.response_system, name="response_system", curie=DEFAULT_.curie('response_system'),
                   model_uri=DEFAULT_.response_system, domain=None, range=Optional[Union[str, "ResponseSystemEnum"]])

slots.response_system_version = Slot(uri=DEFAULT_.response_system_version, name="response_system_version", curie=DEFAULT_.curie('response_system_version'),
                   model_uri=DEFAULT_.response_system_version, domain=None, range=Optional[str])

slots.bm_pct_blasts_at_response = Slot(uri=DEFAULT_.bm_pct_blasts_at_response, name="bm_pct_blasts_at_response", curie=DEFAULT_.curie('bm_pct_blasts_at_response'),
                   model_uri=DEFAULT_.bm_pct_blasts_at_response, domain=None, range=Optional[int])

slots.bm_analysis_method_at_response = Slot(uri=DEFAULT_.bm_analysis_method_at_response, name="bm_analysis_method_at_response", curie=DEFAULT_.curie('bm_analysis_method_at_response'),
                   model_uri=DEFAULT_.bm_analysis_method_at_response, domain=None, range=Optional[Union[str, "BmAnalysisMethodAtResponseEnum"]])

slots.anc_at_response = Slot(uri=DEFAULT_.anc_at_response, name="anc_at_response", curie=DEFAULT_.curie('anc_at_response'),
                   model_uri=DEFAULT_.anc_at_response, domain=None, range=Optional[int])

slots.anc_threshold_at_response = Slot(uri=DEFAULT_.anc_threshold_at_response, name="anc_threshold_at_response", curie=DEFAULT_.curie('anc_threshold_at_response'),
                   model_uri=DEFAULT_.anc_threshold_at_response, domain=None, range=Optional[int])

slots.platelet_count_at_response = Slot(uri=DEFAULT_.platelet_count_at_response, name="platelet_count_at_response", curie=DEFAULT_.curie('platelet_count_at_response'),
                   model_uri=DEFAULT_.platelet_count_at_response, domain=None, range=Optional[int])

slots.platelet_threshold_at_response = Slot(uri=DEFAULT_.platelet_threshold_at_response, name="platelet_threshold_at_response", curie=DEFAULT_.curie('platelet_threshold_at_response'),
                   model_uri=DEFAULT_.platelet_threshold_at_response, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.symptoms = Slot(uri=DEFAULT_.symptoms, name="symptoms", curie=DEFAULT_.curie('symptoms'),
                   model_uri=DEFAULT_.symptoms, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.palpable_nodes = Slot(uri=DEFAULT_.palpable_nodes, name="palpable_nodes", curie=DEFAULT_.curie('palpable_nodes'),
                   model_uri=DEFAULT_.palpable_nodes, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.age_at_mrd_assessment = Slot(uri=DEFAULT_.age_at_mrd_assessment, name="age_at_mrd_assessment", curie=DEFAULT_.curie('age_at_mrd_assessment'),
                   model_uri=DEFAULT_.age_at_mrd_assessment, domain=None, range=Optional[int])

slots.mrd_method = Slot(uri=DEFAULT_.mrd_method, name="mrd_method", curie=DEFAULT_.curie('mrd_method'),
                   model_uri=DEFAULT_.mrd_method, domain=None, range=Optional[Union[str, "MrdMethodEnum"]])

slots.flow_cytometry_type = Slot(uri=DEFAULT_.flow_cytometry_type, name="flow_cytometry_type", curie=DEFAULT_.curie('flow_cytometry_type'),
                   model_uri=DEFAULT_.flow_cytometry_type, domain=None, range=Optional[Union[str, "FlowCytometryTypeEnum"]])

slots.mrd_result = Slot(uri=DEFAULT_.mrd_result, name="mrd_result", curie=DEFAULT_.curie('mrd_result'),
                   model_uri=DEFAULT_.mrd_result, domain=None, range=Optional[str])

slots.mrd_result_numeric = Slot(uri=DEFAULT_.mrd_result_numeric, name="mrd_result_numeric", curie=DEFAULT_.curie('mrd_result_numeric'),
                   model_uri=DEFAULT_.mrd_result_numeric, domain=None, range=Optional[int])

slots.mrd_result_unit = Slot(uri=DEFAULT_.mrd_result_unit, name="mrd_result_unit", curie=DEFAULT_.curie('mrd_result_unit'),
                   model_uri=DEFAULT_.mrd_result_unit, domain=None, range=Optional[Union[str, "NotreportedUnknownEnum"]])

slots.mrd_sensitivty = Slot(uri=DEFAULT_.mrd_sensitivty, name="mrd_sensitivty", curie=DEFAULT_.curie('mrd_sensitivty'),
                   model_uri=DEFAULT_.mrd_sensitivty, domain=None, range=Optional[int])

slots.mrd_sample_source = Slot(uri=DEFAULT_.mrd_sample_source, name="mrd_sample_source", curie=DEFAULT_.curie('mrd_sample_source'),
                   model_uri=DEFAULT_.mrd_sample_source, domain=None, range=Optional[Union[str, "MrdSampleSourceEnum"]])

slots.mrd_molecular_markers = Slot(uri=DEFAULT_.mrd_molecular_markers, name="mrd_molecular_markers", curie=DEFAULT_.curie('mrd_molecular_markers'),
                   model_uri=DEFAULT_.mrd_molecular_markers, domain=None, range=Optional[Union[str, "MrdMolecularMarkersEnum"]])

slots.age_at_ae = Slot(uri=DEFAULT_.age_at_ae, name="age_at_ae", curie=DEFAULT_.curie('age_at_ae'),
                   model_uri=DEFAULT_.age_at_ae, domain=None, range=Optional[int])

slots.age_at_ae_resolved = Slot(uri=DEFAULT_.age_at_ae_resolved, name="age_at_ae_resolved", curie=DEFAULT_.curie('age_at_ae_resolved'),
                   model_uri=DEFAULT_.age_at_ae_resolved, domain=None, range=Optional[int])

slots.adverse_event = Slot(uri=DEFAULT_.adverse_event, name="adverse_event", curie=DEFAULT_.curie('adverse_event'),
                   model_uri=DEFAULT_.adverse_event, domain=None, range=Optional[Union[str, "AdverseEventEnum"]])

slots.ae_immune = Slot(uri=DEFAULT_.ae_immune, name="ae_immune", curie=DEFAULT_.curie('ae_immune'),
                   model_uri=DEFAULT_.ae_immune, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.ae_infusion = Slot(uri=DEFAULT_.ae_infusion, name="ae_infusion", curie=DEFAULT_.curie('ae_infusion'),
                   model_uri=DEFAULT_.ae_infusion, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.ae_code = Slot(uri=DEFAULT_.ae_code, name="ae_code", curie=DEFAULT_.curie('ae_code'),
                   model_uri=DEFAULT_.ae_code, domain=None, range=Optional[str])

slots.ae_grade_system = Slot(uri=DEFAULT_.ae_grade_system, name="ae_grade_system", curie=DEFAULT_.curie('ae_grade_system'),
                   model_uri=DEFAULT_.ae_grade_system, domain=None, range=Optional[Union[str, "AeGradeSystemEnum"]])

slots.ae_system_version = Slot(uri=DEFAULT_.ae_system_version, name="ae_system_version", curie=DEFAULT_.curie('ae_system_version'),
                   model_uri=DEFAULT_.ae_system_version, domain=None, range=Optional[str])

slots.ae_grade = Slot(uri=DEFAULT_.ae_grade, name="ae_grade", curie=DEFAULT_.curie('ae_grade'),
                   model_uri=DEFAULT_.ae_grade, domain=None, range=Optional[Union[str, "AeGradeEnum"]])

slots.ae_reported = Slot(uri=DEFAULT_.ae_reported, name="ae_reported", curie=DEFAULT_.curie('ae_reported'),
                   model_uri=DEFAULT_.ae_reported, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.ae_attribution = Slot(uri=DEFAULT_.ae_attribution, name="ae_attribution", curie=DEFAULT_.curie('ae_attribution'),
                   model_uri=DEFAULT_.ae_attribution, domain=None, range=Optional[Union[str, "AeAttributionEnum"]])

slots.ae_outcome = Slot(uri=DEFAULT_.ae_outcome, name="ae_outcome", curie=DEFAULT_.curie('ae_outcome'),
                   model_uri=DEFAULT_.ae_outcome, domain=None, range=Optional[Union[str, "AeOutcomeEnum"]])

slots.avn_joint = Slot(uri=DEFAULT_.avn_joint, name="avn_joint", curie=DEFAULT_.curie('avn_joint'),
                   model_uri=DEFAULT_.avn_joint, domain=None, range=Optional[Union[str, "AvnJointEnum"]])

slots.avn_joint_laterality = Slot(uri=DEFAULT_.avn_joint_laterality, name="avn_joint_laterality", curie=DEFAULT_.curie('avn_joint_laterality'),
                   model_uri=DEFAULT_.avn_joint_laterality, domain=None, range=Optional[Union[str, "AvnJointLateralityEnum"]])

slots.avn_method = Slot(uri=DEFAULT_.avn_method, name="avn_method", curie=DEFAULT_.curie('avn_method'),
                   model_uri=DEFAULT_.avn_method, domain=None, range=Optional[Union[str, "AvnMethodEnum"]])

slots.orthopedic_procedure = Slot(uri=DEFAULT_.orthopedic_procedure, name="orthopedic_procedure", curie=DEFAULT_.curie('orthopedic_procedure'),
                   model_uri=DEFAULT_.orthopedic_procedure, domain=None, range=Optional[Union[str, "OrthopedicProcedureEnum"]])

slots.ae_expected = Slot(uri=DEFAULT_.ae_expected, name="ae_expected", curie=DEFAULT_.curie('ae_expected'),
                   model_uri=DEFAULT_.ae_expected, domain=None, range=Optional[Union[str, "AeExpectedEnum"]])

slots.ae_tx_mod = Slot(uri=DEFAULT_.ae_tx_mod, name="ae_tx_mod", curie=DEFAULT_.curie('ae_tx_mod'),
                   model_uri=DEFAULT_.ae_tx_mod, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.ae_hospitalization = Slot(uri=DEFAULT_.ae_hospitalization, name="ae_hospitalization", curie=DEFAULT_.curie('ae_hospitalization'),
                   model_uri=DEFAULT_.ae_hospitalization, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.ae_icu = Slot(uri=DEFAULT_.ae_icu, name="ae_icu", curie=DEFAULT_.curie('ae_icu'),
                   model_uri=DEFAULT_.ae_icu, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.ae_medication = Slot(uri=DEFAULT_.ae_medication, name="ae_medication", curie=DEFAULT_.curie('ae_medication'),
                   model_uri=DEFAULT_.ae_medication, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.ae_intervention = Slot(uri=DEFAULT_.ae_intervention, name="ae_intervention", curie=DEFAULT_.curie('ae_intervention'),
                   model_uri=DEFAULT_.ae_intervention, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.ae_intervention_detail = Slot(uri=DEFAULT_.ae_intervention_detail, name="ae_intervention_detail", curie=DEFAULT_.curie('ae_intervention_detail'),
                   model_uri=DEFAULT_.ae_intervention_detail, domain=None, range=Optional[Union[str, "AeInterventionDetailEnum"]])

slots.ae_pathogen = Slot(uri=DEFAULT_.ae_pathogen, name="ae_pathogen", curie=DEFAULT_.curie('ae_pathogen'),
                   model_uri=DEFAULT_.ae_pathogen, domain=None, range=Optional[Union[str, "AePathogenEnum"]])

slots.ae_pathogen_confirmation = Slot(uri=DEFAULT_.ae_pathogen_confirmation, name="ae_pathogen_confirmation", curie=DEFAULT_.curie('ae_pathogen_confirmation'),
                   model_uri=DEFAULT_.ae_pathogen_confirmation, domain=None, range=Optional[Union[str, "AePathogenConfirmationEnum"]])

slots.infection_classification = Slot(uri=DEFAULT_.infection_classification, name="infection_classification", curie=DEFAULT_.curie('infection_classification'),
                   model_uri=DEFAULT_.infection_classification, domain=None, range=Optional[Union[str, "InfectionClassificationEnum"]])

slots.gvhd_acuity = Slot(uri=DEFAULT_.gvhd_acuity, name="gvhd_acuity", curie=DEFAULT_.curie('gvhd_acuity'),
                   model_uri=DEFAULT_.gvhd_acuity, domain=None, range=Optional[Union[str, "GvhdAcuityEnum"]])

slots.gvhd_organ = Slot(uri=DEFAULT_.gvhd_organ, name="gvhd_organ", curie=DEFAULT_.curie('gvhd_organ'),
                   model_uri=DEFAULT_.gvhd_organ, domain=None, range=Optional[Union[str, "GvhdOrganEnum"]])

slots.age_at_le_eval = Slot(uri=DEFAULT_.age_at_le_eval, name="age_at_le_eval", curie=DEFAULT_.curie('age_at_le_eval'),
                   model_uri=DEFAULT_.age_at_le_eval, domain=None, range=Optional[int])

slots.le = Slot(uri=DEFAULT_.le, name="le", curie=DEFAULT_.curie('le'),
                   model_uri=DEFAULT_.le, domain=None, range=Optional[Union[str, "LeEnum"]])

slots.le_detail = Slot(uri=DEFAULT_.le_detail, name="le_detail", curie=DEFAULT_.curie('le_detail'),
                   model_uri=DEFAULT_.le_detail, domain=None, range=Optional[Union[str, "LeDetailEnum"]])

slots.le_sub_detail = Slot(uri=DEFAULT_.le_sub_detail, name="le_sub_detail", curie=DEFAULT_.curie('le_sub_detail'),
                   model_uri=DEFAULT_.le_sub_detail, domain=None, range=Optional[Union[str, "LeSubDetailEnum"]])

slots.le_severity_grade = Slot(uri=DEFAULT_.le_severity_grade, name="le_severity_grade", curie=DEFAULT_.curie('le_severity_grade'),
                   model_uri=DEFAULT_.le_severity_grade, domain=None, range=Optional[Union[str, "LeSeverityGradeEnum"]])

slots.le_ctcae_version = Slot(uri=DEFAULT_.le_ctcae_version, name="le_ctcae_version", curie=DEFAULT_.curie('le_ctcae_version'),
                   model_uri=DEFAULT_.le_ctcae_version, domain=None, range=Optional[str])

slots.age_at_smn = Slot(uri=DEFAULT_.age_at_smn, name="age_at_smn", curie=DEFAULT_.curie('age_at_smn'),
                   model_uri=DEFAULT_.age_at_smn, domain=None, range=Optional[int])

slots.smn_status = Slot(uri=DEFAULT_.smn_status, name="smn_status", curie=DEFAULT_.curie('smn_status'),
                   model_uri=DEFAULT_.smn_status, domain=None, range=Optional[Union[str, "NoNotreportedUnknownYesEnum"]])

slots.smn_morph_sno = Slot(uri=DEFAULT_.smn_morph_sno, name="smn_morph_sno", curie=DEFAULT_.curie('smn_morph_sno'),
                   model_uri=DEFAULT_.smn_morph_sno, domain=None, range=Optional[str])

slots.smn_icd_o_morph = Slot(uri=DEFAULT_.smn_icd_o_morph, name="smn_icd_o_morph", curie=DEFAULT_.curie('smn_icd_o_morph'),
                   model_uri=DEFAULT_.smn_icd_o_morph, domain=None, range=Optional[str])

slots.snm_morph_txt = Slot(uri=DEFAULT_.snm_morph_txt, name="snm_morph_txt", curie=DEFAULT_.curie('snm_morph_txt'),
                   model_uri=DEFAULT_.snm_morph_txt, domain=None, range=Optional[str])

slots.smn_top_sno = Slot(uri=DEFAULT_.smn_top_sno, name="smn_top_sno", curie=DEFAULT_.curie('smn_top_sno'),
                   model_uri=DEFAULT_.smn_top_sno, domain=None, range=Optional[str])

slots.smn_icd_o_top = Slot(uri=DEFAULT_.smn_icd_o_top, name="smn_icd_o_top", curie=DEFAULT_.curie('smn_icd_o_top'),
                   model_uri=DEFAULT_.smn_icd_o_top, domain=None, range=Optional[str])

slots.smn_top_txt = Slot(uri=DEFAULT_.smn_top_txt, name="smn_top_txt", curie=DEFAULT_.curie('smn_top_txt'),
                   model_uri=DEFAULT_.smn_top_txt, domain=None, range=Optional[str])

slots.smn_site = Slot(uri=DEFAULT_.smn_site, name="smn_site", curie=DEFAULT_.curie('smn_site'),
                   model_uri=DEFAULT_.smn_site, domain=None, range=Optional[Union[str, "SmnSiteEnum"]])

slots.smn_type = Slot(uri=DEFAULT_.smn_type, name="smn_type", curie=DEFAULT_.curie('smn_type'),
                   model_uri=DEFAULT_.smn_type, domain=None, range=Optional[Union[str, "SmnTypeEnum"]])

slots.smn_field = Slot(uri=DEFAULT_.smn_field, name="smn_field", curie=DEFAULT_.curie('smn_field'),
                   model_uri=DEFAULT_.smn_field, domain=None, range=Optional[Union[str, "SmnFieldEnum"]])

slots.pro_measures = Slot(uri=DEFAULT_.pro_measures, name="pro_measures", curie=DEFAULT_.curie('pro_measures'),
                   model_uri=DEFAULT_.pro_measures, domain=None, range=Optional[Union[str, "ProMeasuresEnum"]])

slots.pro_measurement_type = Slot(uri=DEFAULT_.pro_measurement_type, name="pro_measurement_type", curie=DEFAULT_.curie('pro_measurement_type'),
                   model_uri=DEFAULT_.pro_measurement_type, domain=None, range=Optional[Union[str, "ProMeasurementTypeEnum"]])

slots.raters = Slot(uri=DEFAULT_.raters, name="raters", curie=DEFAULT_.curie('raters'),
                   model_uri=DEFAULT_.raters, domain=None, range=Optional[Union[str, "RatersEnum"]])

slots.eligible_age_lower = Slot(uri=DEFAULT_.eligible_age_lower, name="eligible_age_lower", curie=DEFAULT_.curie('eligible_age_lower'),
                   model_uri=DEFAULT_.eligible_age_lower, domain=None, range=Optional[int])

slots.eligible_age_upper = Slot(uri=DEFAULT_.eligible_age_upper, name="eligible_age_upper", curie=DEFAULT_.curie('eligible_age_upper'),
                   model_uri=DEFAULT_.eligible_age_upper, domain=None, range=Optional[int])

slots.time_point = Slot(uri=DEFAULT_.time_point, name="time_point", curie=DEFAULT_.curie('time_point'),
                   model_uri=DEFAULT_.time_point, domain=None, range=Optional[Union[str, "TimePointEnum"]])

slots.subject__persons = Slot(uri=DEFAULT_.persons, name="subject__persons", curie=DEFAULT_.curie('persons'),
                   model_uri=DEFAULT_.subject__persons, domain=None, range=Union[dict, Person])
