
# Class: Subject




URI: [https://w3id.org/pcdc/model/Subject](https://w3id.org/pcdc/model/Subject)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Person]<persons%201..1-++[Subject&#124;honest_broker_subject_id:string%20%3F;consortium:ConsortiumEnum%20%3F;data_contributor_id:DataContributorIdEnum%20%3F;study_id:StudyIdEnum%20%3F;age_at_enrollment:integer%20%3F;year_at_enrollment:integer%20%3F;treatment_arm:TreatmentArmEnum%20%3F;enrolled_status:EnrolledStatusEnum%20%3F;efs_censor_status:EfsCensorStatusEnum%20%3F;age_at_censor_status:integer%20%3F;data_source:DataSourceEnum%20%3F;randomized_status:RandomizedStatusEnum%20%3F;study_phase:StudyPhaseEnum%20%3F;study_type:StudyTypeEnum%20%3F;submitter_id(i):string;type(i):string],[FamilyMedicalHistory]++-%20subjects%201..*>[Subject],[Timing]++-%20subjects%201..*>[Subject],[Thing]^-[Subject],[Timing],[Person],[FamilyMedicalHistory])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Person]<persons%201..1-++[Subject&#124;honest_broker_subject_id:string%20%3F;consortium:ConsortiumEnum%20%3F;data_contributor_id:DataContributorIdEnum%20%3F;study_id:StudyIdEnum%20%3F;age_at_enrollment:integer%20%3F;year_at_enrollment:integer%20%3F;treatment_arm:TreatmentArmEnum%20%3F;enrolled_status:EnrolledStatusEnum%20%3F;efs_censor_status:EfsCensorStatusEnum%20%3F;age_at_censor_status:integer%20%3F;data_source:DataSourceEnum%20%3F;randomized_status:RandomizedStatusEnum%20%3F;study_phase:StudyPhaseEnum%20%3F;study_type:StudyTypeEnum%20%3F;submitter_id(i):string;type(i):string],[FamilyMedicalHistory]++-%20subjects%201..*>[Subject],[Timing]++-%20subjects%201..*>[Subject],[Thing]^-[Subject],[Timing],[Person],[FamilyMedicalHistory])

## Parents

 *  is_a: [Thing](Thing.md)

## Referenced by Class

 *  **None** *[subjects](subjects.md)*  <sub>1..\*</sub>  **[Subject](Subject.md)**

## Attributes


### Own

 * [honest_broker_subject_id](honest_broker_subject_id.md)  <sub>0..1</sub>
     * Description: The identifier assigned to the subject by the honest broker--an individual, organization or system acting for, or on behalf of, a covered entity to collect and provide health information to research investigators in such a manner whereby it would not be reasonably possible for the investigators or others to identify the corresponding patients-subjects directly or indirectly. The honest broker cannot be one of the investigators. The information provided to the investigators by the honest broker may incorporate linkage codes to permit information collation and/or subsequent inquiries (i.e., a "re-identification code"), however the information linking this re-identification code to the patient's identity must be retained by the honest broker and subsequent inquiries are conducted through the honest broker. (Source: NCI Thersaurus)
     * Range: [String](types/String.md)
 * [consortium](consortium.md)  <sub>0..1</sub>
     * Description: The disease consortium to which the data contributor belongs.
     * Range: [ConsortiumEnum](ConsortiumEnum.md)
 * [data_contributor_id](data_contributor_id.md)  <sub>0..1</sub>
     * Description: An identifier assigned to a data contributor.
     * Range: [DataContributorIdEnum](DataContributorIdEnum.md)
 * [study_id](study_id.md)  <sub>0..1</sub>
     * Description: A sequence of characters used to identify, name, or characterize the study.
     * Range: [StudyIdEnum](StudyIdEnum.md)
 * [age_at_enrollment](age_at_enrollment.md)  <sub>0..1</sub>
     * Description: Age of subject (in days) when the subject enrolled in the study.
     * Range: [Integer](types/Integer.md)
 * [year_at_enrollment](year_at_enrollment.md)  <sub>0..1</sub>
     * Description: The year at which a subject enrolled in a study.
     * Range: [Integer](types/Integer.md)
 * [treatment_arm](treatment_arm.md)  <sub>0..1</sub>
     * Description: A specific treatment plan within a clinical trial that describes the activities a subject will be involved in as he or she progresses through the study.
     * Range: [TreatmentArmEnum](TreatmentArmEnum.md)
 * [enrolled_status](enrolled_status.md)  <sub>0..1</sub>
     * Description: This variable indicates if the subject was enrolled in the study, or if the subject was not enrolled in the study but received treatment per the study's protocol.
     * Range: [EnrolledStatusEnum](EnrolledStatusEnum.md)
 * [efs_censor_status](efs_censor_status.md)  <sub>0..1</sub>
     * Description: The event free survival censor status
     * Range: [EfsCensorStatusEnum](EfsCensorStatusEnum.md)
 * [age_at_censor_status](age_at_censor_status.md)  <sub>0..1</sub>
     * Description: Age (in days) of the subject at the time of the CENSOR_STATUS
     * Range: [Integer](types/Integer.md)
 * [data_source](data_source.md)  <sub>0..1</sub>
     * Description: Is this data coming from a cancer registry or via a clinical study?
     * Range: [DataSourceEnum](DataSourceEnum.md)
 * [randomized_status](randomized_status.md)  <sub>0..1</sub>
     * Description: The allocation of individuals to groups by chance, especially in order to control the variables in an experiment.
     * Range: [RandomizedStatusEnum](RandomizedStatusEnum.md)
 * [study_phase](study_phase.md)  <sub>0..1</sub>
     * Description: The phase of the clinical trial that the subject was enrolled in for the collection of this data.
     * Range: [StudyPhaseEnum](StudyPhaseEnum.md)
 * [study_type](study_type.md)  <sub>0..1</sub>
     * Description: The nature of the investigation or the investigational use for which clinical study is being done.
     * Range: [StudyTypeEnum](StudyTypeEnum.md)
 * [➞persons](subject__persons.md)  <sub>1..1</sub>
     * Range: [Person](Person.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
