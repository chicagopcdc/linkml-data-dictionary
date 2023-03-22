
# Class: Cytology




URI: [https://w3id.org/pcdc/model/Cytology](https://w3id.org/pcdc/model/Cytology)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[Cytology&#124;age_at_cytology:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;malignant_cells:AbsentNotreportedPresentUnknownEnum%20%3F;cytology_spec_type:CytologySpecTypeEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[Cytology])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[Cytology&#124;age_at_cytology:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;malignant_cells:AbsentNotreportedPresentUnknownEnum%20%3F;cytology_spec_type:CytologySpecTypeEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[Cytology])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_cytology](age_at_cytology.md)  <sub>0..1</sub>
     * Description: Age in Days at Cytology Test
     * Range: [Integer](types/Integer.md)
 * [timings](timings.md)  <sub>0..1</sub>
     * Range: [Timing](Timing.md)
 * [disease_phase](disease_phase.md)  <sub>0..1</sub>
     * Description: The phase of the cancer treatment process during which relevant observations were recorded. This variable is used across domains to frame the timing of these longitudinal observations and reduce the number of redundant variables needed to report similar concepts (see "Disease Phase Timing and Course Table" in the documentation for additional guidance).
     * Range: [DiseasePhaseEnum](DiseasePhaseEnum.md)
 * [disease_phase_number](disease_phase_number.md)  <sub>0..1</sub>
     * Description: This variable indicates the ordinal numbering of the Disease Phase variable within its various subgroups (e.g., Relapse 1, Relapse 2, Relapse 3, etc.). The observations across domains can therefore be organized longitudinally without the need for specific dates.
     * Range: [Integer](types/Integer.md)
 * [course](course.md)  <sub>0..1</sub>
     * Description: The protocol treatment "course" during which relevant observations were recorded. This variable is used across domains to frame the timing of these longitudinal observations and reduce the number of redundant variables needed to report similar concepts (see "Disease Phase Timing and Course Table" in the documentation for additional guidance).
     * Range: [CourseEnum](CourseEnum.md)
 * [course_number](course_number.md)  <sub>0..1</sub>
     * Description: This variable indicates the ordinal numbering of the Course variable within its various subgroups (e.g., Induction 1, Induction 2, Induction 3, etc.). The observations across domains can therefore be organized longitudinally without the need for specific dates.
     * Range: [Integer](types/Integer.md)
 * [malignant_cells](malignant_cells.md)  <sub>0..1</sub>
     * Description: A term used to describe cancer. Malignant cells grow in an uncontrolled way and can invade nearby tissues and spread to other parts of the body through the blood and lymph system (Source: NCI Dictionary of Cancer Terms)
     * Range: [AbsentNotreportedPresentUnknownEnum](AbsentNotreportedPresentUnknownEnum.md)
 * [cytology_spec_type](cytology_spec_type.md)  <sub>0..1</sub>
     * Description: The study of cells using a microscope (Source: NCI Dictionary of Cancer Terms)
     * Range: [CytologySpecTypeEnum](CytologySpecTypeEnum.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
