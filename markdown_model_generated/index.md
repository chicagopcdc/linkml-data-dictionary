
# data-dictionary


**metamodel version:** 1.7.0

**version:** 0.0.1





### Classes

 * [Thing](Thing.md)
     * [FamilyMedicalHistory](FamilyMedicalHistory.md)
     * [Person](Person.md)
     * [Subject](Subject.md)
     * [Timing](Timing.md)

### Mixins


### Slots

 * [age_at_censor_status](age_at_censor_status.md) - Age (in days) of the subject at the time of the CENSOR_STATUS
 * [age_at_course_anc_500](age_at_course_anc_500.md) - The age (in days) of the subject when the subject's neutrophil count exceeded 500 (ANC/mm3)
 * [age_at_course_end](age_at_course_end.md) - The age (in days) of the subject at the time that this ordinally numbered course was completed.
 * [age_at_course_start](age_at_course_start.md) - The age (in days) of the subject at the time that this ordinally numbered course was started.
 * [age_at_cycle_end](age_at_cycle_end.md) - The age (in days) of the subject at the end of the treatment cycle.
 * [age_at_cycle_start](age_at_cycle_start.md) - The age (in days) of the subject at the beginning of the treatment cycle.
 * [age_at_disease_phase](age_at_disease_phase.md) - The age (in days) of the subject at the time that this ordinally numbered disease phase was recorded.
 * [age_at_enrollment](age_at_enrollment.md) - Age of subject (in days) when the subject enrolled in the study.
 * [age_at_txassign](age_at_txassign.md) - The age (in days) of the subject at the time that this treartment was assigned.
 * [consortium](consortium.md) - The disease consortium to which the data contributor belongs.
 * [course](course.md) - The protocol treatment "course" during which relevant observations were recorded. This variable is used across domains to frame the timing of these longitudinal observations and reduce the number of redundant variables needed to report similar concepts (see "Disease Phase Timing and Course Table" in the documentation for additional guidance).
 * [course_number](course_number.md) - This variable indicates the ordinal numbering of the Course variable within its various subgroups (e.g., Induction 1, Induction 2, Induction 3, etc.). The observations across domains can therefore be organized longitudinally without the need for specific dates.
 * [cycle_number](cycle_number.md) - This variable indicates the ordinal numbering of cycles of treatment therapy administered to the subject.
 * [data_contributor_id](data_contributor_id.md) - An identifier assigned to a data contributor.
 * [data_source](data_source.md) - Is this data coming from a cancer registry or via a clinical study?
 * [disease_phase](disease_phase.md) - The phase of the cancer treatment process during which relevant observations were recorded. This variable is used across domains to frame the timing of these longitudinal observations and reduce the number of redundant variables needed to report similar concepts (see "Disease Phase Timing and Course Table" in the documentation for additional guidance).
 * [disease_phase_number](disease_phase_number.md) - This variable indicates the ordinal numbering of the Disease Phase variable within its various subgroups (e.g., Relapse 1, Relapse 2, Relapse 3, etc.). The observations across domains can therefore be organized longitudinally without the need for specific dates.
 * [efs_censor_status](efs_censor_status.md) - The event free survival censor status
 * [enrolled_status](enrolled_status.md) - This variable indicates if the subject was enrolled in the study, or if the subject was not enrolled in the study but received treatment per the study's protocol.
 * [ethnicity](ethnicity.md) - The social and cultural characteristics, backgrounds, or experiences shared by a group of people. These include language, religion, beliefs, values, and behaviors that are often handed down from one generation to the next. Some conditions or diseases, such as cancer, may be more common in certain ethnic groups than in others. (Source: NCI Dictionary of Cancer Terms)
 * [honest_broker_subject_id](honest_broker_subject_id.md) - The identifier assigned to the subject by the honest broker--an individual, organization or system acting for, or on behalf of, a covered entity to collect and provide health information to research investigators in such a manner whereby it would not be reasonably possible for the investigators or others to identify the corresponding patients-subjects directly or indirectly. The honest broker cannot be one of the investigators. The information provided to the investigators by the honest broker may incorporate linkage codes to permit information collation and/or subsequent inquiries (i.e., a "re-identification code"), however the information linking this re-identification code to the patient's identity must be retained by the honest broker and subsequent inquiries are conducted through the honest broker. (Source: NCI Thersaurus)
 * [prior_cancer](prior_cancer.md) - Does the subject have a relative who has a medical history that includes cancer?
 * [prior_cancer_type](prior_cancer_type.md) - The type of prior cancer from the medical history of the relative of the subject.
 * [race](race.md) - A group of people who share physical characteristics, such as skin color and facial features. They may also share similar social or cultural identities and ancestral backgrounds. There are many racial groups, and a person may belong to or identify with more than one group. Some diseases, such as cancer, may be more common in certain races than in others. (Source: NCI Dictionary of Cancer Terms)
 * [race_other](race_other.md) - Specify the "Other" RACE
 * [randomized_status](randomized_status.md) - The allocation of individuals to groups by chance, especially in order to control the variables in an experiment.
 * [relation](relation.md) - What kind of relation is this relative who has had a relevant medical condition?
 * [sex](sex.md) - The biological sex of the subject.
 * [study_id](study_id.md) - A sequence of characters used to identify, name, or characterize the study.
 * [study_phase](study_phase.md) - The phase of the clinical trial that the subject was enrolled in for the collection of this data.
 * [study_type](study_type.md) - The nature of the investigation or the investigational use for which clinical study is being done.
 * [➞persons](subject__persons.md)
 * [subjects](subjects.md)
 * [submitter_id](submitter_id.md) - PCDC internal event ID
 * [treatment_arm](treatment_arm.md) - A specific treatment plan within a clinical trial that describes the activities a subject will be involved in as he or she progresses through the study.
 * [type](type.md) - Default system-assigned property for each node
 * [year_at_disease_phase](year_at_disease_phase.md) - The year in which this ordinally numbered disease phase was recorded.
 * [year_at_enrollment](year_at_enrollment.md) - The year at which a subject enrolled in a study.

### Enums

 * [ConsortiumEnum](ConsortiumEnum.md)
 * [CourseEnum](CourseEnum.md)
 * [DataContributorIdEnum](DataContributorIdEnum.md)
 * [DataSourceEnum](DataSourceEnum.md)
 * [DiseasePhaseEnum](DiseasePhaseEnum.md)
 * [EfsCensorStatusEnum](EfsCensorStatusEnum.md)
 * [EnrolledStatusEnum](EnrolledStatusEnum.md)
 * [EthnicityEnum](EthnicityEnum.md)
 * [PriorCancerEnum](PriorCancerEnum.md)
 * [RaceEnum](RaceEnum.md)
 * [RandomizedStatusEnum](RandomizedStatusEnum.md)
 * [RelationEnum](RelationEnum.md)
 * [SexEnum](SexEnum.md)
 * [StudyIdEnum](StudyIdEnum.md)
 * [StudyPhaseEnum](StudyPhaseEnum.md)
 * [StudyTypeEnum](StudyTypeEnum.md)
 * [TreatmentArmEnum](TreatmentArmEnum.md)

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
