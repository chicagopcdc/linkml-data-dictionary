
# Class: Stem Cell Transplant




URI: [https://w3id.org/pcdc/model/StemCellTransplant](https://w3id.org/pcdc/model/StemCellTransplant)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..1-++[StemCellTransplant&#124;age_at_sct:integer%20%3F;protocol_sct:NoNotreportedUnknownYesEnum%20%3F;non_protocol_timing:NonProtocolTimingEnum%20%3F;sct_type:SctTypeEnum%20%3F;stem_cell_source:StemCellSourceEnum%20%3F;donor_relationship:DonorRelationshipEnum%20%3F;hla_match:NoNotreportedUnknownYesEnum%20%3F;number_hla:decimal%20%3F;number_matches:decimal%20%3F;conditioning_type:ConditioningTypeEnum%20%3F;prior_tbi:NoNotreportedUnknownYesEnum%20%3F;hla_a_result:BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum%20%3F;hla_b_result:BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum%20%3F;hla_c_result:BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum%20%3F;hla_drb1_result:BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum%20%3F;hla_dq_result:BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum%20%3F;age_at_sct_harvest:integer%20%3F;age_at_recovery:integer%20%3F;recovery_type:RecoveryTypeEnum%20%3F;recovery_status:RecoveryStatusEnum%20%3F;cd34_collected:decimal%20%3F;cd34_transplant:decimal%20%3F;sct_cycles:decimal%20%3F;stem_cell_source_other:string%20%3F;sct_success:NoNotreportedUnknownYesEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[StemCellTransplant],[Thing]^-[StemCellTransplant])](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..1-++[StemCellTransplant&#124;age_at_sct:integer%20%3F;protocol_sct:NoNotreportedUnknownYesEnum%20%3F;non_protocol_timing:NonProtocolTimingEnum%20%3F;sct_type:SctTypeEnum%20%3F;stem_cell_source:StemCellSourceEnum%20%3F;donor_relationship:DonorRelationshipEnum%20%3F;hla_match:NoNotreportedUnknownYesEnum%20%3F;number_hla:decimal%20%3F;number_matches:decimal%20%3F;conditioning_type:ConditioningTypeEnum%20%3F;prior_tbi:NoNotreportedUnknownYesEnum%20%3F;hla_a_result:BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum%20%3F;hla_b_result:BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum%20%3F;hla_c_result:BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum%20%3F;hla_drb1_result:BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum%20%3F;hla_dq_result:BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum%20%3F;age_at_sct_harvest:integer%20%3F;age_at_recovery:integer%20%3F;recovery_type:RecoveryTypeEnum%20%3F;recovery_status:RecoveryStatusEnum%20%3F;cd34_collected:decimal%20%3F;cd34_transplant:decimal%20%3F;sct_cycles:decimal%20%3F;stem_cell_source_other:string%20%3F;sct_success:NoNotreportedUnknownYesEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[StemCellTransplant],[Thing]^-[StemCellTransplant])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_sct](age_at_sct.md)  <sub>0..1</sub>
     * Description: The age (in days) of subject at the time of stem cell transplantation.
     * Range: [Integer](types/Integer.md)
 * [time_periods](time_periods.md)  <sub>0..1</sub>
     * Range: [TimePeriod](TimePeriod.md)
 * [protocol_sct](protocol_sct.md)  <sub>0..1</sub>
     * Description: Was this stem cell transplant part of the treatment protocol?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [non_protocol_timing](non_protocol_timing.md)  <sub>0..1</sub>
     * Description: If a non-protocol radiation therapy, when was this radiation therapy administered?
     * Range: [NonProtocolTimingEnum](NonProtocolTimingEnum.md)
 * [sct_type](sct_type.md)  <sub>0..1</sub>
     * Description: A procedure in which a patient receives healthy stem cells (blood-forming cells) to replace their own stem cells that have been destroyed by treatment with radiation or high doses of chemotherapy. The healthy stem cells may come from the blood or bone marrow of the patient or from a related or unrelated donor. A stem cell transplant may be autologous (using a patient’s own stem cells that were collected and saved before treatment), allogeneic (using stem cells from a related or unrelated donor), syngeneic (using stem cells donated by an identical twin), or cord blood (using umbilical cord blood donated after a baby is born). (Source: NCI Dictionary of Cancer Terms)
     * Range: [SctTypeEnum](SctTypeEnum.md)
 * [stem_cell_source](stem_cell_source.md)  <sub>0..1</sub>
     * Description: The source of the stem cells for the stem cell transplant.
     * Range: [StemCellSourceEnum](StemCellSourceEnum.md)
 * [donor_relationship](donor_relationship.md)  <sub>0..1</sub>
     * Description: The biological relationship between the stem cell donor and the recipients.
     * Range: [DonorRelationshipEnum](DonorRelationshipEnum.md)
 * [hla_match](hla_match.md)  <sub>0..1</sub>
     * Description: HLA Match Status
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [number_hla](number_hla.md)  <sub>0..1</sub>
     * Description: Number of Evaluated HLAs
     * Range: [Decimal](types/Decimal.md)
 * [number_matches](number_matches.md)  <sub>0..1</sub>
     * Description: Number of Matched HLAs
     * Range: [Decimal](types/Decimal.md)
 * [conditioning_type](conditioning_type.md)  <sub>0..1</sub>
     * Description: The type of conditioning the subject received prior to stem-cell transplantation.
     * Range: [ConditioningTypeEnum](ConditioningTypeEnum.md)
 * [prior_tbi](prior_tbi.md)  <sub>0..1</sub>
     * Description: Total Body Irradiation Prior to Stem Cell Transplant
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [hla_a_result](hla_a_result.md)  <sub>0..1</sub>
     * Description: HLA-A Match Finding
     * Range: [BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum](BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum.md)
 * [hla_b_result](hla_b_result.md)  <sub>0..1</sub>
     * Description: HLA-B Match Finding
     * Range: [BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum](BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum.md)
 * [hla_c_result](hla_c_result.md)  <sub>0..1</sub>
     * Description: HLA-C Match Finding
     * Range: [BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum](BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum.md)
 * [hla_drb1_result](hla_drb1_result.md)  <sub>0..1</sub>
     * Description: HLA-DRB1 Match Finding
     * Range: [BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum](BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum.md)
 * [hla_dq_result](hla_dq_result.md)  <sub>0..1</sub>
     * Description: HLA-DQ Match Finding
     * Range: [BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum](BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum.md)
 * [age_at_sct_harvest](age_at_sct_harvest.md)  <sub>0..1</sub>
     * Description: The age (in days) of subject at the time of stem cell harvest
     * Range: [Integer](types/Integer.md)
 * [age_at_recovery](age_at_recovery.md)  <sub>0..1</sub>
     * Description: The age (in days) of subject at the time of stem cell transplant per recovery type.
     * Range: [Integer](types/Integer.md)
 * [recovery_type](recovery_type.md)  <sub>0..1</sub>
     * Description: The type of recovery after the transplant procedure.
     * Range: [RecoveryTypeEnum](RecoveryTypeEnum.md)
 * [recovery_status](recovery_status.md)  <sub>0..1</sub>
     * Description: The recovery status per recovery type.
     * Range: [RecoveryStatusEnum](RecoveryStatusEnum.md)
 * [cd34_collected](cd34_collected.md)  <sub>0..1</sub>
     * Description: The determination of the amount of CD34 expressing stem cells present in a sample (10^6 CD34+/kg).
     * Range: [Decimal](types/Decimal.md)
 * [cd34_transplant](cd34_transplant.md)  <sub>0..1</sub>
     * Description: The determination of the amount of transplanted CD34 expressing stem cells (10^6 CD34+/kg).
     * Range: [Decimal](types/Decimal.md)
 * [sct_cycles](sct_cycles.md)  <sub>0..1</sub>
     * Description: Number of Stem Cell Transplant Cycles
     * Range: [Decimal](types/Decimal.md)
 * [stem_cell_source_other](stem_cell_source_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" STEM_CELL_SOURCE
     * Range: [String](types/String.md)
 * [sct_success](sct_success.md)  <sub>0..1</sub>
     * Description: Was the stem cell transplant successful?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [subjects](subjects.md)  <sub>1..1</sub>
     * Range: [Subject](Subject.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
