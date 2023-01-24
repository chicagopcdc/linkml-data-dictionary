
# Class: Timing




URI: [https://w3id.org/pcdc/model/Timing](https://w3id.org/pcdc/model/Timing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Subject]<subjects%201..1-%20[Timing&#124;age_at_course_anc_500:integer%20%3F;age_at_course_start:integer%20%3F;age_at_course_end:integer%20%3F;age_at_cycle_start:integer%20%3F;age_at_cyle_end:integer%20%3F;age_at_disease_phase:integer%20%3F;age_at_txassign:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;cycle_number:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;timing_type:string%20%3F;year_at_disease_phase:integer%20%3F;submitter_id(i):string;type(i):string%20%3F],[Timing]<timings%200..1-++[Timing],[NamedThing]^-[Timing],[Subject],[NamedThing])](https://yuml.me/diagram/nofunky;dir:TB/class/[Subject]<subjects%201..1-%20[Timing&#124;age_at_course_anc_500:integer%20%3F;age_at_course_start:integer%20%3F;age_at_course_end:integer%20%3F;age_at_cycle_start:integer%20%3F;age_at_cyle_end:integer%20%3F;age_at_disease_phase:integer%20%3F;age_at_txassign:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;cycle_number:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;timing_type:string%20%3F;year_at_disease_phase:integer%20%3F;submitter_id(i):string;type(i):string%20%3F],[Timing]<timings%200..1-++[Timing],[NamedThing]^-[Timing],[Subject],[NamedThing])

## Parents

 *  is_a: [NamedThing](NamedThing.md)

## Referenced by Class

 *  **None** *[timings](timings.md)*  <sub>0..1</sub>  **[Timing](Timing.md)**

## Attributes


### Own

 * [age_at_course_anc_500](age_at_course_anc_500.md)  <sub>0..1</sub>
     * Description: Age in Days When Neutrophil Count Exceeded 500 (ANC/mm3)
     * Range: [Integer](types/Integer.md)
 * [age_at_course_start](age_at_course_start.md)  <sub>0..1</sub>
     * Description: Age of subject (in days) at the start of the course.
     * Range: [Integer](types/Integer.md)
 * [age_at_course_end](age_at_course_end.md)  <sub>0..1</sub>
     * Description: Age of subject (in days) at the end of the course.
     * Range: [Integer](types/Integer.md)
 * [age_at_cycle_start](age_at_cycle_start.md)  <sub>0..1</sub>
     * Description: Age in Days at Cycle Start
     * Range: [Integer](types/Integer.md)
 * [age_at_cyle_end](age_at_cyle_end.md)  <sub>0..1</sub>
     * Description: Age in Days at Cycle End
     * Range: [Integer](types/Integer.md)
 * [age_at_disease_phase](age_at_disease_phase.md)  <sub>0..1</sub>
     * Description: Age of subject (in days) at the disease phase.
     * Range: [Integer](types/Integer.md)
 * [age_at_txassign](age_at_txassign.md)  <sub>0..1</sub>
     * Description: Age in Days at Treatment Assignment.
     * Range: [Integer](types/Integer.md)
 * [course](course.md)  <sub>0..1</sub>
     * Description: The type of protocol treatment course administered.
     * Range: [CourseEnum](CourseEnum.md)
 * [course_number](course_number.md)  <sub>0..1</sub>
     * Description: The number assigned to a course of therapeutic agent administration, indicating where a particular course of treatment falls within a sequence of treatments.
     * Range: [Integer](types/Integer.md)
 * [cycle_number](cycle_number.md)  <sub>0..1</sub>
     * Description: Cycle Number
     * Range: [Integer](types/Integer.md)
 * [disease_phase](disease_phase.md)  <sub>0..1</sub>
     * Description: The phase of the cancer treatment process during which relevant observations were recorded. This variable is used across domains to frame the timing of these longitudinal observations and reduce the number of redundant variables needed to report similar concepts (see "Disease Phase Timing and Course Table" in the documentation for additional guidance).
     * Range: [DiseasePhaseEnum](DiseasePhaseEnum.md)
 * [disease_phase_number](disease_phase_number.md)  <sub>0..1</sub>
     * Description: The number of the disease phase.
     * Range: [Integer](types/Integer.md)
 * [timing_type](timing_type.md)  <sub>0..1</sub>
     * Description: The time frame or phase the patient got a treatment or data have been collected
     * Range: [String](types/String.md)
 * [timings](timings.md)  <sub>0..1</sub>
     * Range: [Timing](Timing.md)
 * [year_at_disease_phase](year_at_disease_phase.md)  <sub>0..1</sub>
     * Description: Year of disease phase
     * Range: [Integer](types/Integer.md)
 * [Timing➞subjects](Timing_subjects.md)  <sub>1..1</sub>
     * Range: [Subject](Subject.md)

### Inherited from NamedThing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>0..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | pcdc:Timing |

