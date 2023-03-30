
# Class: Immunohistochemistry




URI: [https://w3id.org/pcdc/model/Immunohistochemistry](https://w3id.org/pcdc/model/Immunohistochemistry)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[Immunohistochemistry&#124;age_at_ihc:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;ihc_test:IhcTestEnum%20%3F;ihc_spec_type:IhcSpecTypeEnum%20%3F;ihc_result:string%20%3F;ihc_result_numeric:integer%20%3F;ihc_result_unit:IhcResultUnitEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[Immunohistochemistry])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[Immunohistochemistry&#124;age_at_ihc:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;ihc_test:IhcTestEnum%20%3F;ihc_spec_type:IhcSpecTypeEnum%20%3F;ihc_result:string%20%3F;ihc_result_numeric:integer%20%3F;ihc_result_unit:IhcResultUnitEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[Immunohistochemistry])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_ihc](age_at_ihc.md)  <sub>0..1</sub>
     * Description: Age in Days at Immunohistochemistry Test
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
 * [ihc_test](ihc_test.md)  <sub>0..1</sub>
     * Description: A laboratory method that uses antibodies to check for certain antigens (markers) in a sample of tissue. The antibodies are usually linked to an enzyme or a fluorescent dye. After the antibodies bind to the antigen in the tissue sample, the enzyme or dye is activated, and the antigen can then be seen under a microscope. Immunohistochemistry is used to help diagnose diseases, such as cancer. It may also be used to help tell the difference between different types of cancer (Source: NCI Dictionary of Cancer Terms)
     * Range: [IhcTestEnum](IhcTestEnum.md)
 * [ihc_spec_type](ihc_spec_type.md)  <sub>0..1</sub>
     * Description: The type of a material sample taken from a biological entity for immunohistochemistry testing.
     * Range: [IhcSpecTypeEnum](IhcSpecTypeEnum.md)
 * [ihc_result](ihc_result.md)  <sub>0..1</sub>
     * Description: The result from the immunohistochemical test.
     * Range: [String](types/String.md)
 * [ihc_result_numeric](ihc_result_numeric.md)  <sub>0..1</sub>
     * Description: The numerical identifier of an immunohistochemistry specimen assessment result.
     * Range: [Integer](types/Integer.md)
 * [ihc_result_unit](ihc_result_unit.md)  <sub>0..1</sub>
     * Description: The unit of an immunohistochemistry test result.
     * Range: [IhcResultUnitEnum](IhcResultUnitEnum.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
