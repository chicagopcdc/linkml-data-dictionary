
# Class: VitalsAndAnthropometrics




URI: [https://w3id.org/pcdc/model/VitalsAndAnthropometrics](https://w3id.org/pcdc/model/VitalsAndAnthropometrics)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing]<timings%200..1-++[VitalsAndAnthropometrics&#124;age_at_measurement:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;measurement_type:MeasurementTypeEnum%20%3F;measurement:string%20%3F;measurement_numeric:integer%20%3F;measurement_unit:MeasurementUnitEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[VitalsAndAnthropometrics],[Timing],[Thing])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing]<timings%200..1-++[VitalsAndAnthropometrics&#124;age_at_measurement:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;measurement_type:MeasurementTypeEnum%20%3F;measurement:string%20%3F;measurement_numeric:integer%20%3F;measurement_unit:MeasurementUnitEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[VitalsAndAnthropometrics],[Timing],[Thing])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_measurement](age_at_measurement.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject when the vitals measurement was taken.
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
 * [measurement_type](measurement_type.md)  <sub>0..1</sub>
     * Description: The type of vital sign or anthropomorphic measurement being recorded
     * Range: [MeasurementTypeEnum](MeasurementTypeEnum.md)
 * [measurement](measurement.md)  <sub>0..1</sub>
     * Description: The vital sign or anthropomorphic measurement being recorded (non-numeric)
     * Range: [String](types/String.md)
 * [measurement_numeric](measurement_numeric.md)  <sub>0..1</sub>
     * Description: The vital sign or anthropomorphic measurement being recorded (numeric)
     * Range: [Integer](types/Integer.md)
 * [measurement_unit](measurement_unit.md)  <sub>0..1</sub>
     * Description: The units used for the vital sign or anthropomorphic measurement being recorded (numeric)
     * Range: [MeasurementUnitEnum](MeasurementUnitEnum.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
