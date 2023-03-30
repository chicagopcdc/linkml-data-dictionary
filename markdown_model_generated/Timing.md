
# Class: Timing




URI: [https://w3id.org/pcdc/model/Timing](https://w3id.org/pcdc/model/Timing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing]<timings%200..1-++[Timing&#124;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;age_at_disease_phase:integer%20%3F;year_at_disease_phase:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;age_at_course_start:integer%20%3F;age_at_course_end:integer%20%3F;age_at_txassign:integer%20%3F;age_at_course_anc_500:integer%20%3F;cycle_number:integer%20%3F;age_at_cycle_start:integer%20%3F;age_at_cycle_end:integer%20%3F;submitter_id(i):string;type(i):string],[Subject]<subjects%201..*-++[Timing],[Thing]^-[Timing],[Thing],[Subject])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing]<timings%200..1-++[Timing&#124;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;age_at_disease_phase:integer%20%3F;year_at_disease_phase:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;age_at_course_start:integer%20%3F;age_at_course_end:integer%20%3F;age_at_txassign:integer%20%3F;age_at_course_anc_500:integer%20%3F;cycle_number:integer%20%3F;age_at_cycle_start:integer%20%3F;age_at_cycle_end:integer%20%3F;submitter_id(i):string;type(i):string],[Subject]<subjects%201..*-++[Timing],[Thing]^-[Timing],[Thing],[Subject])

## Parents

 *  is_a: [Thing](Thing.md)

## Referenced by Class

 *  **None** *[timings](timings.md)*  <sub>0..1</sub>  **[Timing](Timing.md)**

## Attributes


### Own

 * [disease_phase](disease_phase.md)  <sub>0..1</sub>
     * Description: The phase of the cancer treatment process during which relevant observations were recorded. This variable is used across domains to frame the timing of these longitudinal observations and reduce the number of redundant variables needed to report similar concepts (see "Disease Phase Timing and Course Table" in the documentation for additional guidance).
     * Range: [DiseasePhaseEnum](DiseasePhaseEnum.md)
 * [disease_phase_number](disease_phase_number.md)  <sub>0..1</sub>
     * Description: This variable indicates the ordinal numbering of the Disease Phase variable within its various subgroups (e.g., Relapse 1, Relapse 2, Relapse 3, etc.). The observations across domains can therefore be organized longitudinally without the need for specific dates.
     * Range: [Integer](types/Integer.md)
 * [age_at_disease_phase](age_at_disease_phase.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the time that this ordinally numbered disease phase was recorded.
     * Range: [Integer](types/Integer.md)
 * [year_at_disease_phase](year_at_disease_phase.md)  <sub>0..1</sub>
     * Description: The year in which this ordinally numbered disease phase was recorded.
     * Range: [Integer](types/Integer.md)
 * [course](course.md)  <sub>0..1</sub>
     * Description: The protocol treatment "course" during which relevant observations were recorded. This variable is used across domains to frame the timing of these longitudinal observations and reduce the number of redundant variables needed to report similar concepts (see "Disease Phase Timing and Course Table" in the documentation for additional guidance).
     * Range: [CourseEnum](CourseEnum.md)
 * [course_number](course_number.md)  <sub>0..1</sub>
     * Description: This variable indicates the ordinal numbering of the Course variable within its various subgroups (e.g., Induction 1, Induction 2, Induction 3, etc.). The observations across domains can therefore be organized longitudinally without the need for specific dates.
     * Range: [Integer](types/Integer.md)
 * [age_at_course_start](age_at_course_start.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the time that this ordinally numbered course was started.
     * Range: [Integer](types/Integer.md)
 * [age_at_course_end](age_at_course_end.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the time that this ordinally numbered course was completed.
     * Range: [Integer](types/Integer.md)
 * [age_at_txassign](age_at_txassign.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the time that this treartment was assigned.
     * Range: [Integer](types/Integer.md)
 * [age_at_course_anc_500](age_at_course_anc_500.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject when the subject's neutrophil count exceeded 500 (ANC/mm3)
     * Range: [Integer](types/Integer.md)
 * [cycle_number](cycle_number.md)  <sub>0..1</sub>
     * Description: This variable indicates the ordinal numbering of cycles of treatment therapy administered to the subject.
     * Range: [Integer](types/Integer.md)
 * [age_at_cycle_start](age_at_cycle_start.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the beginning of the treatment cycle.
     * Range: [Integer](types/Integer.md)
 * [age_at_cycle_end](age_at_cycle_end.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the end of the treatment cycle.
     * Range: [Integer](types/Integer.md)
 * [subjects](subjects.md)  <sub>1..\*</sub>
     * Range: [Subject](Subject.md)
 * [timings](timings.md)  <sub>0..1</sub>
     * Range: [Timing](Timing.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
