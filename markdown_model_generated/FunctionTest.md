
# Class: FunctionTest




URI: [https://w3id.org/pcdc/model/FunctionTest](https://w3id.org/pcdc/model/FunctionTest)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[FunctionTest&#124;age_at_function_test:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;function_category:FunctionCategoryEnum%20%3F;function_test:FunctionTestEnum%20%3F;function_result:string%20%3F;function_result_numeric:integer%20%3F;function_result_unit:FunctionResultUnitEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[FunctionTest])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[FunctionTest&#124;age_at_function_test:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;function_category:FunctionCategoryEnum%20%3F;function_test:FunctionTestEnum%20%3F;function_result:string%20%3F;function_result_numeric:integer%20%3F;function_result_unit:FunctionResultUnitEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[FunctionTest])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_function_test](age_at_function_test.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the time of the function test.
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
 * [function_category](function_category.md)  <sub>0..1</sub>
     * Description: The category of the function test.
     * Range: [FunctionCategoryEnum](FunctionCategoryEnum.md)
 * [function_test](function_test.md)  <sub>0..1</sub>
     * Description: The function test used on the subject.
     * Range: [FunctionTestEnum](FunctionTestEnum.md)
 * [function_result](function_result.md)  <sub>0..1</sub>
     * Description: The string/text result of the function test.
     * Range: [String](types/String.md)
 * [function_result_numeric](function_result_numeric.md)  <sub>0..1</sub>
     * Description: The numeric value of the result of the function test.
     * Range: [Integer](types/Integer.md)
 * [function_result_unit](function_result_unit.md)  <sub>0..1</sub>
     * Description: The unit used for the numeric result of the function test used on the subject.
     * Range: [FunctionResultUnitEnum](FunctionResultUnitEnum.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
