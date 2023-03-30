
# Class: MedicalHistory




URI: [https://w3id.org/pcdc/model/MedicalHistory](https://w3id.org/pcdc/model/MedicalHistory)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[MedicalHistory&#124;condition:ConditionEnum%20%3F;condition_other:string%20%3F;condition_type:ConditionTypeEnum%20%3F;condition_status:NoNotreportedUnknownYesEnum%20%3F;assisted_conception:AssistedConceptionEnum%20%3F;submitter_id(i):string;type(i):string])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[MedicalHistory&#124;condition:ConditionEnum%20%3F;condition_other:string%20%3F;condition_type:ConditionTypeEnum%20%3F;condition_status:NoNotreportedUnknownYesEnum%20%3F;assisted_conception:AssistedConceptionEnum%20%3F;submitter_id(i):string;type(i):string])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [condition](condition.md)  <sub>0..1</sub>
     * Description: Relevant condition that may or may not (see CONDITION_STATUS) be in part of the subject's medical history. 
     * Range: [ConditionEnum](ConditionEnum.md)
 * [condition_other](condition_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" CONDITION
     * Range: [String](types/String.md)
 * [condition_type](condition_type.md)  <sub>0..1</sub>
     * Description: The type of relevant condition from the subject's medical history.
     * Range: [ConditionTypeEnum](ConditionTypeEnum.md)
 * [condition_status](condition_status.md)  <sub>0..1</sub>
     * Description: Was this condition observed in the subject?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [assisted_conception](assisted_conception.md)  <sub>0..1</sub>
     * Description: If the subject was conceived through assisted conception, what was the type of assisted conception?
     * Range: [AssistedConceptionEnum](AssistedConceptionEnum.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
