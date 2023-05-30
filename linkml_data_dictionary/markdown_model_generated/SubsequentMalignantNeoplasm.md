
# Class: Subsequent Malignant Neoplasm




URI: [https://w3id.org/pcdc/model/SubsequentMalignantNeoplasm](https://w3id.org/pcdc/model/SubsequentMalignantNeoplasm)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject]<subjects%201..1-++[SubsequentMalignantNeoplasm&#124;age_at_smn:integer%20%3F;treatment_related:NoNotreportedUnknownYesEnum%20%3F;morph_code:string%20%3F;morph_code_system:MorphCodeSystemEnum%20%3F;morph_code_system_version:string%20%3F;top_code:string%20%3F;top_code_system:TopCodeSystemEnum%20%3F;top_code_system_version:string%20%3F;smn_status:AbsentNotreportedPresentUnknownEnum%20%3F;morph_code_txt:string%20%3F;top_code_txt:string%20%3F;smn_field:SmnFieldEnum%20%3F;site:SiteEnum%20%3F;site_other:string%20%3F;smn:SmnEnum%20%3F;smn_other:string%20%3F;smn_type_other:string%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[SubsequentMalignantNeoplasm],[Thing]^-[SubsequentMalignantNeoplasm],[Subject])](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject]<subjects%201..1-++[SubsequentMalignantNeoplasm&#124;age_at_smn:integer%20%3F;treatment_related:NoNotreportedUnknownYesEnum%20%3F;morph_code:string%20%3F;morph_code_system:MorphCodeSystemEnum%20%3F;morph_code_system_version:string%20%3F;top_code:string%20%3F;top_code_system:TopCodeSystemEnum%20%3F;top_code_system_version:string%20%3F;smn_status:AbsentNotreportedPresentUnknownEnum%20%3F;morph_code_txt:string%20%3F;top_code_txt:string%20%3F;smn_field:SmnFieldEnum%20%3F;site:SiteEnum%20%3F;site_other:string%20%3F;smn:SmnEnum%20%3F;smn_other:string%20%3F;smn_type_other:string%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[SubsequentMalignantNeoplasm],[Thing]^-[SubsequentMalignantNeoplasm],[Subject])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_smn](age_at_smn.md)  <sub>0..1</sub>
     * Description: The age (in days) of subject at the diagnosis of the subsequent malignant neoplasm.
     * Range: [Integer](types/Integer.md)
 * [treatment_related](treatment_related.md)  <sub>0..1</sub>
     * Description: Is this subsequent malignancy related to prior treatment recieved?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [morph_code](morph_code.md)  <sub>0..1</sub>
     * Description: The code for the morphology of the subsequent tumor
     * Range: [String](types/String.md)
 * [morph_code_system](morph_code_system.md)  <sub>0..1</sub>
     * Description: The coding system for MORPH_CODE
     * Range: [MorphCodeSystemEnum](MorphCodeSystemEnum.md)
 * [morph_code_system_version](morph_code_system_version.md)  <sub>0..1</sub>
     * Description: The version of the coding system indicated in MORPH_CODE_SYSTEM
     * Range: [String](types/String.md)
 * [top_code](top_code.md)  <sub>0..1</sub>
     * Description: The topography code describes the site of origin of the neoplasm.
     * Range: [String](types/String.md)
 * [top_code_system](top_code_system.md)  <sub>0..1</sub>
     * Description: The coding system for the code used in TOP_CODE
     * Range: [TopCodeSystemEnum](TopCodeSystemEnum.md)
 * [top_code_system_version](top_code_system_version.md)  <sub>0..1</sub>
     * Description: The version of the coding system indicated in TOP_CODE_SYSTEM
     * Range: [String](types/String.md)
 * [time_periods](time_periods.md)  <sub>0..1</sub>
     * Range: [TimePeriod](TimePeriod.md)
 * [smn_status](smn_status.md)  <sub>0..1</sub>
     * Description: Was the indicated subsequent malignant neoplasm found in the patient?
     * Range: [AbsentNotreportedPresentUnknownEnum](AbsentNotreportedPresentUnknownEnum.md)
 * [morph_code_txt](morph_code_txt.md)  <sub>0..1</sub>
     * Description: The display text for MORPH_CODE 
     * Range: [String](types/String.md)
 * [top_code_txt](top_code_txt.md)  <sub>0..1</sub>
     * Description: The display text for TOP_CODE 
     * Range: [String](types/String.md)
 * [smn_field](smn_field.md)  <sub>0..1</sub>
     * Description: The location of the subsequent malignant neoplasm related to the prior radiation field.
     * Range: [SmnFieldEnum](SmnFieldEnum.md)
 * [site](site.md)  <sub>0..1</sub>
     * Description: Specifies the anatomic site of a localized pathological or traumatic structural change, damage, deformity, or discontinuity of tissue, organ, or body part.
     * Range: [SiteEnum](SiteEnum.md)
 * [site_other](site_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" TUMOR_SITE
     * Range: [String](types/String.md)
 * [smn](smn.md)  <sub>0..1</sub>
     * Description: SMN Type
     * Range: [SmnEnum](SmnEnum.md)
 * [smn_other](smn_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" SMN
     * Range: [String](types/String.md)
 * [smn_type_other](smn_type_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" SMN_TYPE
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
