
# Class: Vitals And Anthropometrics




URI: [https://w3id.org/pcdc/model/VitalsAndAnthropometrics](https://w3id.org/pcdc/model/VitalsAndAnthropometrics)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Subject]<subjects%201..*-++[VitalsAndAnthropometrics&#124;age_at_measurement:integer%20%3F;measurement_type:MeasurementTypeEnum%20%3F;measurement_text:string%20%3F;measurement_numeric:decimal%20%3F;measurement_unit:MeasurementUnitEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[VitalsAndAnthropometrics],[Thing]^-[VitalsAndAnthropometrics],[TimePeriod],[Thing],[Subject])](https://yuml.me/diagram/nofunky;dir:TB/class/[Subject]<subjects%201..*-++[VitalsAndAnthropometrics&#124;age_at_measurement:integer%20%3F;measurement_type:MeasurementTypeEnum%20%3F;measurement_text:string%20%3F;measurement_numeric:decimal%20%3F;measurement_unit:MeasurementUnitEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[VitalsAndAnthropometrics],[Thing]^-[VitalsAndAnthropometrics],[TimePeriod],[Thing],[Subject])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_measurement](age_at_measurement.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject when the vitals measurement was taken.
     * Range: [Integer](types/Integer.md)
 * [time_periods](time_periods.md)  <sub>0..1</sub>
     * Range: [TimePeriod](TimePeriod.md)
 * [measurement_type](measurement_type.md)  <sub>0..1</sub>
     * Description: The type of vital sign or anthropomorphic measurement being recorded
     * Range: [MeasurementTypeEnum](MeasurementTypeEnum.md)
 * [measurement_text](measurement_text.md)  <sub>0..1</sub>
     * Description: The vital sign or anthropomorphic measurement being recorded (non-numeric)
     * Range: [String](types/String.md)
 * [measurement_numeric](measurement_numeric.md)  <sub>0..1</sub>
     * Description: The vital sign or anthropomorphic measurement being recorded (numeric)
     * Range: [Decimal](types/Decimal.md)
 * [measurement_unit](measurement_unit.md)  <sub>0..1</sub>
     * Description: The units used for the vital sign or anthropomorphic measurement being recorded (numeric)
     * Range: [MeasurementUnitEnum](MeasurementUnitEnum.md)
 * [subjects](subjects.md)  <sub>1..\*</sub>
     * Range: [Subject](Subject.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
