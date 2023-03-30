
# Class: MinimalResidualDisease




URI: [https://w3id.org/pcdc/model/MinimalResidualDisease](https://w3id.org/pcdc/model/MinimalResidualDisease)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[MinimalResidualDisease&#124;age_at_mrd_assessment:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;mrd_method:MrdMethodEnum%20%3F;flow_cytometry_type:FlowCytometryTypeEnum%20%3F;mrd_result:string%20%3F;mrd_result_numeric:integer%20%3F;mrd_result_unit:NotreportedUnknownEnum%20%3F;mrd_sensitivty:integer%20%3F;mrd_sample_source:MrdSampleSourceEnum%20%3F;mrd_molecular_markers:MrdMolecularMarkersEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[MinimalResidualDisease])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[MinimalResidualDisease&#124;age_at_mrd_assessment:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;mrd_method:MrdMethodEnum%20%3F;flow_cytometry_type:FlowCytometryTypeEnum%20%3F;mrd_result:string%20%3F;mrd_result_numeric:integer%20%3F;mrd_result_unit:NotreportedUnknownEnum%20%3F;mrd_sensitivty:integer%20%3F;mrd_sample_source:MrdSampleSourceEnum%20%3F;mrd_molecular_markers:MrdMolecularMarkersEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[MinimalResidualDisease])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_mrd_assessment](age_at_mrd_assessment.md)  <sub>0..1</sub>
     * Description: Age in Days at Minimal Residual Disease Assessment
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
 * [mrd_method](mrd_method.md)  <sub>0..1</sub>
     * Description: A term used to describe a very small number of cancer cells that remain in the body during or after treatment. Minimal residual disease can be found only by highly sensitive laboratory methods that are able to find one cancer cell among one million normal cells. Checking to see if there is minimal residual disease may help plan treatment, find out how well treatment is working or if cancer has come back, or make a prognosis. Minimal residual disease testing is used mostly for blood cancers such as lymphoma and leukemia. Also called MRD. (Source: NCI Dictionary of Cancer Terms)
     * Range: [MrdMethodEnum](MrdMethodEnum.md)
 * [flow_cytometry_type](flow_cytometry_type.md)  <sub>0..1</sub>
     * Range: [FlowCytometryTypeEnum](FlowCytometryTypeEnum.md)
 * [mrd_result](mrd_result.md)  <sub>0..1</sub>
     * Description: Minimal Residual Disease Result
     * Range: [String](types/String.md)
 * [mrd_result_numeric](mrd_result_numeric.md)  <sub>0..1</sub>
     * Description: Numeric Minimal Residual Disease Result
     * Range: [Integer](types/Integer.md)
 * [mrd_result_unit](mrd_result_unit.md)  <sub>0..1</sub>
     * Description: Numeric Minimal Residual Disease Result Unit
     * Range: [NotreportedUnknownEnum](NotreportedUnknownEnum.md)
 * [mrd_sensitivty](mrd_sensitivty.md)  <sub>0..1</sub>
     * Description: Minimal Residual Disease Method Sensitivity
     * Range: [Integer](types/Integer.md)
 * [mrd_sample_source](mrd_sample_source.md)  <sub>0..1</sub>
     * Description: Minimal Residual Disease Sample Source
     * Range: [MrdSampleSourceEnum](MrdSampleSourceEnum.md)
 * [mrd_molecular_markers](mrd_molecular_markers.md)  <sub>0..1</sub>
     * Description: Minimal residual disease molecular markers
     * Range: [MrdMolecularMarkersEnum](MrdMolecularMarkersEnum.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
