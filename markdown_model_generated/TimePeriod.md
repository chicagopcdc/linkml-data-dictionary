
# Class: Time Period




URI: [https://w3id.org/pcdc/model/TimePeriod](https://w3id.org/pcdc/model/TimePeriod)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Subject]<subjects%201..*-++[TimePeriod&#124;time_period_type:TimePeriodTypeEnum%20%3F;disease_phase:DiseasePhaseEnum%20%3F;course:CourseEnum%20%3F;time_period_number:integer%20%3F;year_at_start:integer%20%3F;age_at_start:integer%20%3F;age_at_end:integer%20%3F;course_other:string%20%3F;age_at_course_anc_500:integer%20%3F;age_at_txassign:integer%20%3F;age_precision:AgePrecisionEnum%20%3F;exam_type:ExamTypeEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[TimePeriod],[Thing]^-[TimePeriod],[Thing],[Subject])](https://yuml.me/diagram/nofunky;dir:TB/class/[Subject]<subjects%201..*-++[TimePeriod&#124;time_period_type:TimePeriodTypeEnum%20%3F;disease_phase:DiseasePhaseEnum%20%3F;course:CourseEnum%20%3F;time_period_number:integer%20%3F;year_at_start:integer%20%3F;age_at_start:integer%20%3F;age_at_end:integer%20%3F;course_other:string%20%3F;age_at_course_anc_500:integer%20%3F;age_at_txassign:integer%20%3F;age_precision:AgePrecisionEnum%20%3F;exam_type:ExamTypeEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[TimePeriod],[Thing]^-[TimePeriod],[Thing],[Subject])

## Parents

 *  is_a: [Thing](Thing.md)

## Referenced by Class

 *  **None** *[time_periods](time_periods.md)*  <sub>0..1</sub>  **[TimePeriod](TimePeriod.md)**

## Attributes


### Own

 * [time_period_type](time_period_type.md)  <sub>0..1</sub>
     * Description: The type of time period being reported.
     * Range: [TimePeriodTypeEnum](TimePeriodTypeEnum.md)
 * [disease_phase](disease_phase.md)  <sub>0..1</sub>
     * Description: The phase of the cancer treatment process during which relevant observations were recorded. This variable is used across domains to frame the timing of these longitudinal observations and reduce the number of redundant variables needed to report similar concepts (see "Disease Phase Timing and Course Table" in the documentation for additional guidance).
     * Range: [DiseasePhaseEnum](DiseasePhaseEnum.md)
 * [course](course.md)  <sub>0..1</sub>
     * Description: The protocol treatment "course" during which relevant observations were recorded. This variable is used across domains to frame the timing of these longitudinal observations and reduce the number of redundant variables needed to report similar concepts (see "Disease Phase Timing and Course Table" in the documentation for additional guidance).
     * Range: [CourseEnum](CourseEnum.md)
 * [time_period_number](time_period_number.md)  <sub>0..1</sub>
     * Description: This variable indicates the ordinal numbering of time periods of the same TIME_PERIOD_TYPE within its various subgroups (e.g., Relapse 1, Relapse 2, Relapse 3, etc.). The observations across domains can therefore be organized longitudinally without the need for specific dates.
     * Range: [Integer](types/Integer.md)
 * [year_at_start](year_at_start.md)  <sub>0..1</sub>
     * Description: The year at the start of the indicated time period
     * Range: [Integer](types/Integer.md)
 * [age_at_start](age_at_start.md)  <sub>0..1</sub>
     * Description: The age (in days) of the patient at the start of the reported time period. 
     * Range: [Integer](types/Integer.md)
 * [age_at_end](age_at_end.md)  <sub>0..1</sub>
     * Description: The age (in days) of the patient at the end of the reported time period. 
     * Range: [Integer](types/Integer.md)
 * [course_other](course_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" COURSE
     * Range: [String](types/String.md)
 * [age_at_course_anc_500](age_at_course_anc_500.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject when the subject's neutrophil count exceeded 500 (ANC/mm3)
     * Range: [Integer](types/Integer.md)
 * [age_at_txassign](age_at_txassign.md)  <sub>0..1</sub>
     * Description: Age in Days at Treatment Assignment
     * Range: [Integer](types/Integer.md)
 * [age_precision](age_precision.md)  <sub>0..1</sub>
     * Description: The precision of the age provided in AGE_AT_DISEASE_PHASE
     * Range: [AgePrecisionEnum](AgePrecisionEnum.md)
 * [exam_type](exam_type.md)  <sub>0..1</sub>
     * Description: The type of exam during which data for the patient was collected.
     * Range: [ExamTypeEnum](ExamTypeEnum.md)
 * [time_periods](time_periods.md)  <sub>0..1</sub>
     * Range: [TimePeriod](TimePeriod.md)
 * [subjects](subjects.md)  <sub>1..\*</sub>
     * Range: [Subject](Subject.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
