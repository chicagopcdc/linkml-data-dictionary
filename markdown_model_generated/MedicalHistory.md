
# Class: Medical History




URI: [https://w3id.org/pcdc/model/MedicalHistory](https://w3id.org/pcdc/model/MedicalHistory)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Subject],[Subject]<subjects%201..*-++[MedicalHistory&#124;condition:ConditionEnum%20%3F;condition_other:string%20%3F;age_at_condition:integer%20%3F;condition_type:ConditionTypeEnum%20%3F;diagnosis_basis:DiagnosisBasisEnum%20%3F;condition_status:NoNotreportedUnknownYesEnum%20%3F;assisted_conception:AssistedConceptionEnum%20%3F;developmental_delay:NoNotreportedUnknownYesEnum%20%3F;developmental_delay_type:string%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[MedicalHistory])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Subject],[Subject]<subjects%201..*-++[MedicalHistory&#124;condition:ConditionEnum%20%3F;condition_other:string%20%3F;age_at_condition:integer%20%3F;condition_type:ConditionTypeEnum%20%3F;diagnosis_basis:DiagnosisBasisEnum%20%3F;condition_status:NoNotreportedUnknownYesEnum%20%3F;assisted_conception:AssistedConceptionEnum%20%3F;developmental_delay:NoNotreportedUnknownYesEnum%20%3F;developmental_delay_type:string%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[MedicalHistory])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [condition](condition.md)  <sub>0..1</sub>
     * Description: Relevant condition from the subject's medical history.
     * Range: [ConditionEnum](ConditionEnum.md)
 * [condition_other](condition_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" CONDITION
     * Range: [String](types/String.md)
 * [age_at_condition](age_at_condition.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
 * [condition_type](condition_type.md)  <sub>0..1</sub>
     * Description: The type of relevant condition from the subject's medical history.
     * Range: [ConditionTypeEnum](ConditionTypeEnum.md)
 * [diagnosis_basis](diagnosis_basis.md)  <sub>0..1</sub>
     * Description: The basis for diagnosis of the CPS. 
     * Range: [DiagnosisBasisEnum](DiagnosisBasisEnum.md)
 * [condition_status](condition_status.md)  <sub>0..1</sub>
     * Description: Was this condition observed in the subject?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [assisted_conception](assisted_conception.md)  <sub>0..1</sub>
     * Description: If the subject was conceived through assisted conception, what was the type of assisted conception?
     * Range: [AssistedConceptionEnum](AssistedConceptionEnum.md)
 * [developmental_delay](developmental_delay.md)  <sub>0..1</sub>
     * Description: Did the subject experience developmental delay?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [developmental_delay_type](developmental_delay_type.md)  <sub>0..1</sub>
     * Description: What was the type of developmental delay?
     * Range: [String](types/String.md)
 * [subjects](subjects.md)  <sub>1..\*</sub>
     * Range: [Subject](Subject.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
