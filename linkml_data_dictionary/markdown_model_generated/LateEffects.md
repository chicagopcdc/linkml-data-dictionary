
# Class: Late Effects




URI: [https://w3id.org/pcdc/model/LateEffects](https://w3id.org/pcdc/model/LateEffects)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Subject],[Subject]<subjects%201..1-++[LateEffects&#124;age_at_le_eval:integer%20%3F;late_effect:LateEffectEnum%20%3F;code:string%20%3F;code_system:CodeSystemEnum%20%3F;code_system_version:string%20%3F;grade:GradeEnum%20%3F;grade_system:GradeSystemEnum%20%3F;grade_system_version:string%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[LateEffects])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Subject],[Subject]<subjects%201..1-++[LateEffects&#124;age_at_le_eval:integer%20%3F;late_effect:LateEffectEnum%20%3F;code:string%20%3F;code_system:CodeSystemEnum%20%3F;code_system_version:string%20%3F;grade:GradeEnum%20%3F;grade_system:GradeSystemEnum%20%3F;grade_system_version:string%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[LateEffects])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_le_eval](age_at_le_eval.md)  <sub>0..1</sub>
     * Description: The age (in days) of subject when the late effect evaluation was performed.
     * Range: [Integer](types/Integer.md)
 * [late_effect](late_effect.md)  <sub>0..1</sub>
     * Description: A health problem that occurs months or years after a disease is diagnosed or after treatment has ended. Late effects may be caused by cancer or cancer treatment. They may include physical, mental, and social problems and second cancers. (Source: NCI Dictionary of Cancer Terms)
     * Range: [LateEffectEnum](LateEffectEnum.md)
 * [code](code.md)  <sub>0..1</sub>
     * Description: The code of the adverse event.
     * Range: [String](types/String.md)
 * [code_system](code_system.md)  <sub>0..1</sub>
     * Description: The coding system used for the AE_CODE
     * Range: [CodeSystemEnum](CodeSystemEnum.md)
 * [code_system_version](code_system_version.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [grade](grade.md)  <sub>0..1</sub>
     * Description: A numeric value corresponding to the degree of severity of an adverse event.
     * Range: [GradeEnum](GradeEnum.md)
 * [grade_system](grade_system.md)  <sub>0..1</sub>
     * Description: The grading system used to refer to the severity of the adverse event.
     * Range: [GradeSystemEnum](GradeSystemEnum.md)
 * [grade_system_version](grade_system_version.md)  <sub>0..1</sub>
     * Description: The version of the adverse event grading system.
     * Range: [String](types/String.md)
 * [subjects](subjects.md)  <sub>1..1</sub>
     * Range: [Subject](Subject.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
