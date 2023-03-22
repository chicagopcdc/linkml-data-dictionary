
# Class: LateEffects




URI: [https://w3id.org/pcdc/model/LateEffects](https://w3id.org/pcdc/model/LateEffects)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[LateEffects&#124;age_at_le_eval:integer%20%3F;le:LeEnum%20%3F;le_detail:LeDetailEnum%20%3F;le_sub_detail:LeSubDetailEnum%20%3F;le_severity_grade:LeSeverityGradeEnum%20%3F;le_ctcae_version:string%20%3F;submitter_id(i):string;type(i):string])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[LateEffects&#124;age_at_le_eval:integer%20%3F;le:LeEnum%20%3F;le_detail:LeDetailEnum%20%3F;le_sub_detail:LeSubDetailEnum%20%3F;le_severity_grade:LeSeverityGradeEnum%20%3F;le_ctcae_version:string%20%3F;submitter_id(i):string;type(i):string])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_le_eval](age_at_le_eval.md)  <sub>0..1</sub>
     * Description: Age of subject (in days) when the late effect evaluation was performed.
     * Range: [Integer](types/Integer.md)
 * [le](le.md)  <sub>0..1</sub>
     * Description: Any symptom or condition which is a result of a medical intervention but arises months or years after it.
     * Range: [LeEnum](LeEnum.md)
 * [le_detail](le_detail.md)  <sub>0..1</sub>
     * Description: An in-depth explanation of a health problem that occurs months or years after a disease is diagnosed or after treatment has ended.
     * Range: [LeDetailEnum](LeDetailEnum.md)
 * [le_sub_detail](le_sub_detail.md)  <sub>0..1</sub>
     * Description: An added in-depth or explanation of a health problem that occurs months or years after a disease is diagnosed or after treatment has ended.
     * Range: [LeSubDetailEnum](LeSubDetailEnum.md)
 * [le_severity_grade](le_severity_grade.md)  <sub>0..1</sub>
     * Description: A severity grade assigned to the late effects.
     * Range: [LeSeverityGradeEnum](LeSeverityGradeEnum.md)
 * [le_ctcae_version](le_ctcae_version.md)  <sub>0..1</sub>
     * Description: The version of the Common Terminology Criteria for Adverse Events (CTCAE) Terminology.
     * Range: [String](types/String.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
