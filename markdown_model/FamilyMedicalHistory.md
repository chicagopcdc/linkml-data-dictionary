
# Class: FamilyMedicalHistory


prior cancer information of a first-degree relative

URI: [https://w3id.org/pcdc/model/FamilyMedicalHistory](https://w3id.org/pcdc/model/FamilyMedicalHistory)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Subject],[NamedThing],[Subject]<subjects%201..1-%20[FamilyMedicalHistory&#124;prior_cancer:YesNoUnknownNotReportedEnum;relation:RelationEnum%20%3F;prior_cancer_type:string%20%3F;submitter_id(i):string;type(i):string%20%3F],[NamedThing]^-[FamilyMedicalHistory])](https://yuml.me/diagram/nofunky;dir:TB/class/[Subject],[NamedThing],[Subject]<subjects%201..1-%20[FamilyMedicalHistory&#124;prior_cancer:YesNoUnknownNotReportedEnum;relation:RelationEnum%20%3F;prior_cancer_type:string%20%3F;submitter_id(i):string;type(i):string%20%3F],[NamedThing]^-[FamilyMedicalHistory])

## Parents

 *  is_a: [NamedThing](NamedThing.md)

## Referenced by Class


## Attributes


### Own

 * [prior_cancer](prior_cancer.md)  <sub>1..1</sub>
     * Description: Does the subject have a relative who has a medical history that includes cancer?
     * Range: [YesNoUnknownNotReportedEnum](YesNoUnknownNotReportedEnum.md)
 * [relation](relation.md)  <sub>0..1</sub>
     * Description: What kind of relation is this relative who has had a relevant medical condition?
     * Range: [RelationEnum](RelationEnum.md)
 * [prior_cancer_type](prior_cancer_type.md)  <sub>0..1</sub>
     * Description: The type of prior cancer from the medical history of the relative of the subject.
     * Range: [String](types/String.md)
 * [FamilyMedicalHistory➞subjects](FamilyMedicalHistory_subjects.md)  <sub>1..1</sub>
     * Range: [Subject](Subject.md)

### Inherited from NamedThing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>0..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | pcdc:FamilyMedicalHistory |

