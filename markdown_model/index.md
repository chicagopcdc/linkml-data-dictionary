
# data-dictionary


**metamodel version:** 1.7.0

**version:** 0.0.1





### Classes

 * [NamedThing](NamedThing.md)
     * [FamilyMedicalHistory](FamilyMedicalHistory.md) - prior cancer information of a first-degree relative
     * [Person](Person.md) - demographic information about an individual
     * [Subject](Subject.md)
     * [Timing](Timing.md)

### Mixins


### Slots

 * [age_at_censor_status](age_at_censor_status.md) - Age (in days) of the subject at the time of the CENSOR_STATUS
 * [age_at_course_anc_500](age_at_course_anc_500.md) - Age in Days When Neutrophil Count Exceeded 500 (ANC/mm3)
 * [age_at_course_end](age_at_course_end.md) - Age of subject (in days) at the end of the course.
 * [age_at_course_start](age_at_course_start.md) - Age of subject (in days) at the start of the course.
 * [age_at_cycle_start](age_at_cycle_start.md) - Age in Days at Cycle Start
 * [age_at_cyle_end](age_at_cyle_end.md) - Age in Days at Cycle End
 * [age_at_disease_phase](age_at_disease_phase.md) - Age of subject (in days) at the disease phase.
 * [age_at_enrollment](age_at_enrollment.md) - Age of subject (in days) when the subject enrolled in the study.
 * [age_at_txassign](age_at_txassign.md) - Age in Days at Treatment Assignment.
 * [consortium](consortium.md) - The consortium under which this data is being contributed to the Pediatric Cancer Data Commons.
 * [course](course.md) - The type of protocol treatment course administered.
 * [course_number](course_number.md) - The number assigned to a course of therapeutic agent administration, indicating where a particular course of treatment falls within a sequence of treatments.
 * [cycle_number](cycle_number.md) - Cycle Number
 * [data_contributor_id](data_contributor_id.md) - An identifier assigned to a data contributor.
 * [data_source](data_source.md) - The nature of the investigation or the investigational use for which clinical study is being done.
 * [disease_phase](disease_phase.md) - The phase of the cancer treatment process during which relevant observations were recorded. This variable is used across domains to frame the timing of these longitudinal observations and reduce the number of redundant variables needed to report similar concepts (see "Disease Phase Timing and Course Table" in the documentation for additional guidance).
 * [disease_phase_number](disease_phase_number.md) - The number of the disease phase.
 * [efs_censor_status](efs_censor_status.md) - The event free survival censor status
 * [enrolled_status](enrolled_status.md) - This variable indicates if the subject was enrolled in the study, or if the subject was not enrolled in the study but received treatment per the study's protocol.
 * [ethnicity](ethnicity.md) - The social and cultural characteristics, backgrounds, or experiences shared by a group of people. These include language, religion, beliefs, values, and behaviors that are often handed down from one generation to the next. Some conditions or diseases, such as cancer, may be more common in certain ethnic groups than in others. (Source NCI Dictionary of Cancer Terms)
 * [honest_broker_subject_id](honest_broker_subject_id.md) - The identifier assigned to the subject by the honest broker--an individual, organization or system acting for, or on behalf of, a covered entity to collect and provide health information to research investigators in such a manner whereby it would not be reasonably possible for the investigators or others to identify the corresponding patients-subjects directly or indirectly. The honest broker cannot be one of the investigators. The information provided to the investigators by the honest broker may incorporate linkage codes to permit information collation and/or subsequent inquiries (i.e., a "re-identification code"), however the information linking this re-identification code to the patient's identity must be retained by the honest broker and subsequent inquiries are conducted through the honest broker. (Source NCI Thersaurus)
 * [prior_cancer](prior_cancer.md) - Does the subject have a relative who has a medical history that includes cancer?
 * [prior_cancer_type](prior_cancer_type.md) - The type of prior cancer from the medical history of the relative of the subject.
 * [race](race.md) - A group of people who share physical characteristics, such as skin color and facial features. They may also share similar social or cultural identities and ancestral backgrounds. There are many racial groups, and a person may belong to or identify with more than one group. Some diseases, such as cancer, may be more common in certain races than in others. (Source NCI Dictionary of Cancer Terms)
 * [race_other](race_other.md) - Specify the "Other" RACE
 * [randomized_status](randomized_status.md) - The allocation of individuals to groups by chance, especially in order to control the variables in an experiment.
 * [relation](relation.md) - What kind of relation is this relative who has had a relevant medical condition?
 * [sex](sex.md) - The biological sex of the subject.
 * [study_id](study_id.md) - A sequence of characters used to identify, name, or characterize the study.
 * [study_phase](study_phase.md) - The phase of the clinical trial that the subject was enrolled in for the collection of this data.
 * [study_type](study_type.md) - The nature of the investigation or the investigational use for which clinical study is being done.
 * [➞persons](subject__persons.md)
 * [subjects](subjects.md)
     * [FamilyMedicalHistory➞subjects](FamilyMedicalHistory_subjects.md)
     * [Timing➞subjects](Timing_subjects.md)
 * [submitter_id](submitter_id.md) - PCDC internal event ID
 * [timing_type](timing_type.md) - The time frame or phase the patient got a treatment or data have been collected
 * [timings](timings.md)
 * [treatment_arm](treatment_arm.md) - A specific treatment plan within a clinical trial that describes the activities a subject will be involved in as he or she progresses through the study.
 * [type](type.md) - Default system-assigned property for each node
 * [year_at_disease_phase](year_at_disease_phase.md) - Year of disease phase
 * [year_at_enrollment](year_at_enrollment.md) - The year at which a subject enrolled in a study.

### Enums

 * [CensorStatusEnum](CensorStatusEnum.md)
 * [ConsortiumEnum](ConsortiumEnum.md)
 * [CourseEnum](CourseEnum.md)
 * [DataContributorIdEnum](DataContributorIdEnum.md)
 * [DataSourceEnum](DataSourceEnum.md)
 * [DiseasePhaseEnum](DiseasePhaseEnum.md)
 * [EnrolledStatusEnum](EnrolledStatusEnum.md)
 * [EthnicityEnum](EthnicityEnum.md)
 * [RaceEnum](RaceEnum.md)
 * [RandomizedStatusEnum](RandomizedStatusEnum.md)
 * [RelationEnum](RelationEnum.md)
 * [SexEnum](SexEnum.md)
 * [StudyIdEnum](StudyIdEnum.md)
 * [StudyPhaseEnum](StudyPhaseEnum.md)
 * [StudyTypeEnum](StudyTypeEnum.md)
 * [TreatmentArmEnum](TreatmentArmEnum.md)
 * [YesNoUnknownNotReportedEnum](YesNoUnknownNotReportedEnum.md)

### Subsets

 * [ALL](ALL.md)
 * [CNS](CNS.md)
 * [CP](CP.md)
 * [EWS](EWS.md)
 * [HL](HL.md)
 * [NBL](NBL.md)
 * [NPC](NPC.md)
 * [OS](OS.md)
 * [RB](RB.md)
 * [RMS](RMS.md)

### Types


#### Built in

 * **Bool**
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
