
# Class: Function Test




URI: [https://w3id.org/pcdc/model/FunctionTest](https://w3id.org/pcdc/model/FunctionTest)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..1-++[FunctionTest&#124;age_at_function_test:integer%20%3F;test:TestEnum%20%3F;measurement_type:MeasurementTypeEnum%20%3F;measurement_text:string%20%3F;measurement_numeric:decimal%20%3F;measurement_unit:MeasurementUnitEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[FunctionTest],[Thing]^-[FunctionTest])](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..1-++[FunctionTest&#124;age_at_function_test:integer%20%3F;test:TestEnum%20%3F;measurement_type:MeasurementTypeEnum%20%3F;measurement_text:string%20%3F;measurement_numeric:decimal%20%3F;measurement_unit:MeasurementUnitEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[FunctionTest],[Thing]^-[FunctionTest])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_function_test](age_at_function_test.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the time of the function test.
     * Range: [Integer](types/Integer.md)
 * [time_periods](time_periods.md)  <sub>0..1</sub>
     * Range: [TimePeriod](TimePeriod.md)
 * [test](test.md)  <sub>0..1</sub>
     * Description: A medical procedure that involves testing a sample of blood, urine, or other substance from the body. Laboratory tests can help determine a diagnosis, plan treatment, check to see if treatment is working, or monitor the disease over time Source: NCI Dictionary of Cancer Terms)
     * Range: [TestEnum](TestEnum.md)
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
 * [subjects](subjects.md)  <sub>1..1</sub>
     * Range: [Subject](Subject.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
