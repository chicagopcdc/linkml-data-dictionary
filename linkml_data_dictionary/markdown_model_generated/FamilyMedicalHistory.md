
# Class: Family Medical History




URI: [https://w3id.org/pcdc/model/FamilyMedicalHistory](https://w3id.org/pcdc/model/FamilyMedicalHistory)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Subject],[Subject]<subjects%201..*-++[FamilyMedicalHistory&#124;relation:RelationEnum%20%3F;relation_other:string%20%3F;shared_predisposition:NoNotreportedUnknownYesEnum%20%3F;relative_honest_broker_id:string%20%3F;prior_cancer:NoNotreportedUnknownYesEnum%20%3F;prior_cancer_type:string%20%3F;prior_cancer_laterality:PriorCancerLateralityEnum%20%3F;lkss_of_relative:AliveDeadNotreportedUnknownEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[FamilyMedicalHistory])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Subject],[Subject]<subjects%201..*-++[FamilyMedicalHistory&#124;relation:RelationEnum%20%3F;relation_other:string%20%3F;shared_predisposition:NoNotreportedUnknownYesEnum%20%3F;relative_honest_broker_id:string%20%3F;prior_cancer:NoNotreportedUnknownYesEnum%20%3F;prior_cancer_type:string%20%3F;prior_cancer_laterality:PriorCancerLateralityEnum%20%3F;lkss_of_relative:AliveDeadNotreportedUnknownEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[FamilyMedicalHistory])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [relation](relation.md)  <sub>0..1</sub>
     * Description: What kind of relation is this relative who has had a relevant medical condition?
     * Range: [RelationEnum](RelationEnum.md)
 * [relation_other](relation_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" RELATION
     * Range: [String](types/String.md)
 * [shared_predisposition](shared_predisposition.md)  <sub>0..1</sub>
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [relative_honest_broker_id](relative_honest_broker_id.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [prior_cancer](prior_cancer.md)  <sub>0..1</sub>
     * Description: Does the subject have a relative who has a medical history that includes cancer?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [prior_cancer_type](prior_cancer_type.md)  <sub>0..1</sub>
     * Description: The type of prior cancer from the medical history of the relative of the subject.
     * Range: [String](types/String.md)
 * [prior_cancer_laterality](prior_cancer_laterality.md)  <sub>0..1</sub>
     * Description: The laterality of the prior cancer of the relative of the subject.
     * Range: [PriorCancerLateralityEnum](PriorCancerLateralityEnum.md)
 * [lkss_of_relative](lkss_of_relative.md)  <sub>0..1</sub>
     * Description: The last known survival status of the relative of the subject with the prior cancer.
     * Range: [AliveDeadNotreportedUnknownEnum](AliveDeadNotreportedUnknownEnum.md)
 * [subjects](subjects.md)  <sub>1..\*</sub>
     * Range: [Subject](Subject.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
