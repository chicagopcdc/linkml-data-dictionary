
# Class: StemCellTransplant




URI: [https://w3id.org/pcdc/model/StemCellTransplant](https://w3id.org/pcdc/model/StemCellTransplant)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[StemCellTransplant&#124;age_at_sct:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;protocol_sct:NoNotreportedUnknownYesEnum%20%3F;non_protocol_timing:NonProtocolTimingEnum%20%3F;sct_type:SctTypeEnum%20%3F;sct_source:SctSourceEnum%20%3F;sct_donor_relationship:SctDonorRelationshipEnum%20%3F;hla_match:HlaMatchEnum%20%3F;number_hla:integer%20%3F;number_matches:integer%20%3F;hla_a_result:BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum%20%3F;hla_b_result:BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum%20%3F;hla_c_result:BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum%20%3F;hla_drb1_result:BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum%20%3F;hla_dq_result:BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum%20%3F;sct_conditioning_type:SctConditioningTypeEnum%20%3F;sct_tbi:NoNotreportedUnknownYesEnum%20%3F;sct_cycles:decimal%20%3F;sct_cd34_coll:decimal%20%3F;sct_cd34_transplant:decimal%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[StemCellTransplant])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[StemCellTransplant&#124;age_at_sct:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;protocol_sct:NoNotreportedUnknownYesEnum%20%3F;non_protocol_timing:NonProtocolTimingEnum%20%3F;sct_type:SctTypeEnum%20%3F;sct_source:SctSourceEnum%20%3F;sct_donor_relationship:SctDonorRelationshipEnum%20%3F;hla_match:HlaMatchEnum%20%3F;number_hla:integer%20%3F;number_matches:integer%20%3F;hla_a_result:BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum%20%3F;hla_b_result:BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum%20%3F;hla_c_result:BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum%20%3F;hla_drb1_result:BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum%20%3F;hla_dq_result:BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum%20%3F;sct_conditioning_type:SctConditioningTypeEnum%20%3F;sct_tbi:NoNotreportedUnknownYesEnum%20%3F;sct_cycles:decimal%20%3F;sct_cd34_coll:decimal%20%3F;sct_cd34_transplant:decimal%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[StemCellTransplant])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_sct](age_at_sct.md)  <sub>0..1</sub>
     * Description: Age in Days at Stem Cell Transplant
     * Range: [Integer](types/Integer.md)
 * [timings](timings.md)  <sub>0..1</sub>
     * Range: [Timing](Timing.md)
 * [disease_phase](disease_phase.md)  <sub>0..1</sub>
     * Description: The phase of the cancer treatment process during which relevant observations were recorded. This variable is used across domains to frame the timing of these longitudinal observations and reduce the number of redundant variables needed to report similar concepts (see "Disease Phase Timing and Course Table" in the documentation for additional guidance).
     * Range: [DiseasePhaseEnum](DiseasePhaseEnum.md)
 * [disease_phase_number](disease_phase_number.md)  <sub>0..1</sub>
     * Description: This variable indicates the ordinal numbering of the Disease Phase variable within its various subgroups (e.g., Relapse 1, Relapse 2, Relapse 3, etc.). The observations across domains can therefore be organized longitudinally without the need for specific dates.
     * Range: [Integer](types/Integer.md)
 * [course](course.md)  <sub>0..1</sub>
     * Description: The protocol treatment "course" during which relevant observations were recorded. This variable is used across domains to frame the timing of these longitudinal observations and reduce the number of redundant variables needed to report similar concepts (see "Disease Phase Timing and Course Table" in the documentation for additional guidance).
     * Range: [CourseEnum](CourseEnum.md)
 * [course_number](course_number.md)  <sub>0..1</sub>
     * Description: This variable indicates the ordinal numbering of the Course variable within its various subgroups (e.g., Induction 1, Induction 2, Induction 3, etc.). The observations across domains can therefore be organized longitudinally without the need for specific dates.
     * Range: [Integer](types/Integer.md)
 * [protocol_sct](protocol_sct.md)  <sub>0..1</sub>
     * Description: Was this stem cell transplant part of the treatment protocol?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [non_protocol_timing](non_protocol_timing.md)  <sub>0..1</sub>
     * Description: If a non-protocol medication, when was this medication administered?
     * Range: [NonProtocolTimingEnum](NonProtocolTimingEnum.md)
 * [sct_type](sct_type.md)  <sub>0..1</sub>
     * Description: A procedure in which a patient receives healthy stem cells (blood-forming cells) to replace their own stem cells that have been destroyed by treatment with radiation or high doses of chemotherapy. The healthy stem cells may come from the blood or bone marrow of the patient or from a related or unrelated donor. A stem cell transplant may be autologous (using a patient’s own stem cells that were collected and saved before treatment), allogeneic (using stem cells from a related or unrelated donor), syngeneic (using stem cells donated by an identical twin), or cord blood (using umbilical cord blood donated after a baby is born). (Source: NCI Dictionary of Cancer Terms)
     * Range: [SctTypeEnum](SctTypeEnum.md)
 * [sct_source](sct_source.md)  <sub>0..1</sub>
     * Description: Stem Cell Transplant Source
     * Range: [SctSourceEnum](SctSourceEnum.md)
 * [sct_donor_relationship](sct_donor_relationship.md)  <sub>0..1</sub>
     * Description: Stem Cell Transplant Donor Relationship
     * Range: [SctDonorRelationshipEnum](SctDonorRelationshipEnum.md)
 * [hla_match](hla_match.md)  <sub>0..1</sub>
     * Description: HLA Match Status
     * Range: [HlaMatchEnum](HlaMatchEnum.md)
 * [number_hla](number_hla.md)  <sub>0..1</sub>
     * Description: Number of Evaluated HLAs
     * Range: [Integer](types/Integer.md)
 * [number_matches](number_matches.md)  <sub>0..1</sub>
     * Description: Number of Matched HLAs
     * Range: [Integer](types/Integer.md)
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
 * [sct_conditioning_type](sct_conditioning_type.md)  <sub>0..1</sub>
     * Description: Type of Stem Cell Transplant Conditioning Prior to Transplant
     * Range: [SctConditioningTypeEnum](SctConditioningTypeEnum.md)
 * [sct_tbi](sct_tbi.md)  <sub>0..1</sub>
     * Description: Total Body Irradiation Prior to Stem Cell Transplant
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [sct_cycles](sct_cycles.md)  <sub>0..1</sub>
     * Description: Number of Stem Cell Transplant Cycles
     * Range: [Decimal](types/Decimal.md)
 * [sct_cd34_coll](sct_cd34_coll.md)  <sub>0..1</sub>
     * Description: Number of Stem Cells Collected in SCT Apheresis (10^6 CD34+/kg)
     * Range: [Decimal](types/Decimal.md)
 * [sct_cd34_transplant](sct_cd34_transplant.md)  <sub>0..1</sub>
     * Description: Number of Stem Cells Given in SCT Apheresis (10^6 CD34+/kg)
     * Range: [Decimal](types/Decimal.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
