
# Class: Imaging




URI: [https://w3id.org/pcdc/model/Imaging](https://w3id.org/pcdc/model/Imaging)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..*-++[Imaging&#124;age_at_imaging:integer%20%3F;method:MethodEnum%20%3F;result:NegativeNotreportedPositiveUnknownEnum%20%3F;deauville_score:DeauvilleScoreEnum%20%3F;qpet_score:decimal%20%3F;finding:FindingEnum%20%3F;finding_other:string%20%3F;finding_site:FindingSiteEnum%20%3F;finding_site_other:string%20%3F;bone_marrow:NoNotreportedUnknownYesEnum%20%3F;csf_result:NegativeNotreportedPositiveUnknownEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[Imaging],[Thing]^-[Imaging])](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..*-++[Imaging&#124;age_at_imaging:integer%20%3F;method:MethodEnum%20%3F;result:NegativeNotreportedPositiveUnknownEnum%20%3F;deauville_score:DeauvilleScoreEnum%20%3F;qpet_score:decimal%20%3F;finding:FindingEnum%20%3F;finding_other:string%20%3F;finding_site:FindingSiteEnum%20%3F;finding_site_other:string%20%3F;bone_marrow:NoNotreportedUnknownYesEnum%20%3F;csf_result:NegativeNotreportedPositiveUnknownEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[Imaging],[Thing]^-[Imaging])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_imaging](age_at_imaging.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the time of imaging.
     * Range: [Integer](types/Integer.md)
 * [time_periods](time_periods.md)  <sub>0..1</sub>
     * Range: [TimePeriod](TimePeriod.md)
 * [method](method.md)  <sub>0..1</sub>
     * Description: A systematic course of action that is performed in order to complete a laboratory test.
     * Range: [MethodEnum](MethodEnum.md)
 * [result](result.md)  <sub>0..1</sub>
     * Description: The text result of the laboratory test.
     * Range: [NegativeNotreportedPositiveUnknownEnum](NegativeNotreportedPositiveUnknownEnum.md)
 * [deauville_score](deauville_score.md)  <sub>0..1</sub>
     * Description: A 5 point scale devised to assess the response to treatment of Hodgkin and Aggressive Non-Hodgkin Lymphoma.
     * Range: [DeauvilleScoreEnum](DeauvilleScoreEnum.md)
 * [qpet_score](qpet_score.md)  <sub>0..1</sub>
     * Description: A methodology that provides semi-automatic quantification for interim FDG-PET response in lymphoma. It extends the ordinal Deauville score to a continuous scale.
     * Range: [Decimal](types/Decimal.md)
 * [finding](finding.md)  <sub>0..1</sub>
     * Description: The result of an evaluation technique using a visual display of structural or functional patterns of organs or tissues that is performed to determine the presence, absence, or degree of a condition.
     * Range: [FindingEnum](FindingEnum.md)
 * [finding_other](finding_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" IMAGING_FINDING
     * Range: [String](types/String.md)
 * [finding_site](finding_site.md)  <sub>0..1</sub>
     * Description: The site in which the results of the imaging finding was located. 
     * Range: [FindingSiteEnum](FindingSiteEnum.md)
 * [finding_site_other](finding_site_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" IMAGING_FINDING_SITE
     * Range: [String](types/String.md)
 * [bone_marrow](bone_marrow.md)  <sub>0..1</sub>
     * Description: An indication of whether malignant cells are present in a bone marrow sample.
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [csf_result](csf_result.md)  <sub>0..1</sub>
     * Description: The results of cerebrospinal fluid laboratory tests.
     * Range: [NegativeNotreportedPositiveUnknownEnum](NegativeNotreportedPositiveUnknownEnum.md)
 * [subjects](subjects.md)  <sub>1..\*</sub>
     * Range: [Subject](Subject.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
