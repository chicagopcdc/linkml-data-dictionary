
# Class: Cellular Immunotherapy




URI: [https://w3id.org/pcdc/model/CellularImmunotherapy](https://w3id.org/pcdc/model/CellularImmunotherapy)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..1-++[CellularImmunotherapy&#124;age_at_cimt_start:integer%20%3F;type_other:string%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[CellularImmunotherapy],[Thing]^-[CellularImmunotherapy])](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..1-++[CellularImmunotherapy&#124;age_at_cimt_start:integer%20%3F;type_other:string%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[CellularImmunotherapy],[Thing]^-[CellularImmunotherapy])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_cimt_start](age_at_cimt_start.md)  <sub>0..1</sub>
     * Description: The age (in days) of subject at the time of cellular immunotherapy.
     * Range: [Integer](types/Integer.md)
 * [time_periods](time_periods.md)  <sub>0..1</sub>
     * Range: [TimePeriod](TimePeriod.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
 * [type_other](type_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" CIMT_TYPE
     * Range: [String](types/String.md)
 * [subjects](subjects.md)  <sub>1..1</sub>
     * Range: [Subject](Subject.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
