
# Class: Transfusion Medicine Procedures




URI: [https://w3id.org/pcdc/model/TransfusionMedicineProcedures](https://w3id.org/pcdc/model/TransfusionMedicineProcedures)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Subject]<subjects%201..*-++[TransfusionMedicineProcedures&#124;age_at_tmp_start:integer%20%3F;product:ProductEnum%20%3F;age_at_tmp:integer%20%3F;product_processing:ProductProcessingEnum%20%3F;product_processing_other:string%20%3F;number_units:decimal%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[TransfusionMedicineProcedures],[Thing]^-[TransfusionMedicineProcedures],[TimePeriod],[Thing],[Subject])](https://yuml.me/diagram/nofunky;dir:TB/class/[Subject]<subjects%201..*-++[TransfusionMedicineProcedures&#124;age_at_tmp_start:integer%20%3F;product:ProductEnum%20%3F;age_at_tmp:integer%20%3F;product_processing:ProductProcessingEnum%20%3F;product_processing_other:string%20%3F;number_units:decimal%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[TransfusionMedicineProcedures],[Thing]^-[TransfusionMedicineProcedures],[TimePeriod],[Thing],[Subject])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_tmp_start](age_at_tmp_start.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the start of the transfuction medicine procedure
     * Range: [Integer](types/Integer.md)
 * [time_periods](time_periods.md)  <sub>0..1</sub>
     * Range: [TimePeriod](TimePeriod.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
 * [product](product.md)  <sub>0..1</sub>
     * Description: The type of product intended for transfusion.
     * Range: [ProductEnum](ProductEnum.md)
 * [age_at_tmp](age_at_tmp.md)  <sub>0..1</sub>
     * Description: The age (in days) of subject at the start of the transfusion medicine procedure
     * Range: [Integer](types/Integer.md)
 * [product_processing](product_processing.md)  <sub>0..1</sub>
     * Description: The type of processing that is used on the transfusion product.
     * Range: [ProductProcessingEnum](ProductProcessingEnum.md)
 * [product_processing_other](product_processing_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" PRODUCT_PROCESSING
     * Range: [String](types/String.md)
 * [number_units](number_units.md)  <sub>0..1</sub>
     * Description: The number of units transfused into an individual.
     * Range: [Decimal](types/Decimal.md)
 * [subjects](subjects.md)  <sub>1..\*</sub>
     * Range: [Subject](Subject.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
