
# Class: Imaging




URI: [https://w3id.org/pcdc/model/Imaging](https://w3id.org/pcdc/model/Imaging)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[Imaging&#124;age_at_imaging:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;imaging_method:ImagingMethodEnum%20%3F;imaging_result:ImagingResultEnum%20%3F;deauville_score:DeauvilleScoreEnum%20%3F;qpet_score:integer%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[Imaging])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[Imaging&#124;age_at_imaging:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;imaging_method:ImagingMethodEnum%20%3F;imaging_result:ImagingResultEnum%20%3F;deauville_score:DeauvilleScoreEnum%20%3F;qpet_score:integer%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[Imaging])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_imaging](age_at_imaging.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the time of imaging.
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
 * [imaging_method](imaging_method.md)  <sub>0..1</sub>
     * Description: The testing method/technique used to generate the observed results.
     * Range: [ImagingMethodEnum](ImagingMethodEnum.md)
 * [imaging_result](imaging_result.md)  <sub>0..1</sub>
     * Description: The result of an evaluation technique using a visual display of structural or functional patterns of organs or tissues that is performed to determine the presence, absence, or degree of a condition.
     * Range: [ImagingResultEnum](ImagingResultEnum.md)
 * [deauville_score](deauville_score.md)  <sub>0..1</sub>
     * Description: A 5 point scale devised to assess the response to treatment of Hodgkin and Aggressive Non-Hodgkin Lymphoma.
     * Range: [DeauvilleScoreEnum](DeauvilleScoreEnum.md)
 * [qpet_score](qpet_score.md)  <sub>0..1</sub>
     * Description: A methodology that provides semi-automatic quantification for interim FDG-PET response in lymphoma. It extends the ordinal Deauville score to a continuous scale.
     * Range: [Integer](types/Integer.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
