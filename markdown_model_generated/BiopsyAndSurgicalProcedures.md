
# Class: Biopsy And Surgical Procedures




URI: [https://w3id.org/pcdc/model/BiopsyAndSurgicalProcedures](https://w3id.org/pcdc/model/BiopsyAndSurgicalProcedures)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..*-++[BiopsyAndSurgicalProcedures&#124;age_at_procedure:integer%20%3F;protocol_procedure:NoNotreportedUnknownYesEnum%20%3F;non_protocol_timing:NonProtocolTimingEnum%20%3F;procedure:ProcedureEnum%20%3F;site:SiteEnum%20%3F;site_other:string%20%3F;extent:ExtentEnum%20%3F;outcome:OutcomeEnum%20%3F;hydrocephalus:HydrocephalusEnum%20%3F;posterior_fossa_syndrome:NoNotreportedUnknownYesEnum%20%3F;csf_diversion:CsfDiversionEnum%20%3F;nephron_sparing_partial_nephrectomy:NoNotreportedUnknownYesEnum%20%3F;surgery_type_limb:SurgeryTypeLimbEnum%20%3F;margins:MarginsEnum%20%3F;tumor_rupture:NoNotreportedUnknownYesEnum%20%3F;surgical_complications:SurgicalComplicationsEnum%20%3F;surgical_complications_other:string%20%3F;classification:ClassificationEnum%20%3F;tissue_type:TissueTypeEnum%20%3F;laterality:BilateralLeftMidlineNotreportedRightUnknownEnum%20%3F;biopsy_type:BiopsyTypeEnum%20%3F;surgery_type_amputation:SurgeryTypeAmputationEnum%20%3F;surgery_type_limb_salvage:SurgeryTypeLimbSalvageEnum%20%3F;reconstruction_type:ReconstructionTypeEnum%20%3F;procedure_extent:ProcedureExtentEnum%20%3F;met_non_lung_mgmt:NoNotreportedUnknownYesEnum%20%3F;met_lung_mgmt:MetLungMgmtEnum%20%3F;localization_technique:LocalizationTechniqueEnum%20%3F;distance_margin_tumor:decimal%20%3F;procedure_other:string%20%3F;biopsy_type_other:string%20%3F;number_nodes:NumberNodesEnum%20%3F;number_nodes_numeric:decimal%20%3F;procedure_purpose:ProcedurePurposeEnum%20%3F;procedure_purpose_other:string%20%3F;amputation_type:AmputationTypeEnum%20%3F;resection_type:ResectionTypeEnum%20%3F;distance_margin:decimal%20%3F;hemipelvectomy_type:HemipelvectomyTypeEnum%20%3F;hemipelvectomy_site:HemipelvectomySiteEnum%20%3F;intraop_adjuvant:IntraopAdjuvantEnum%20%3F;intraop_adjuvant_other:string%20%3F;laser_type:LaserTypeEnum%20%3F;laser_type_other:string%20%3F;laser_power:LaserPowerEnum%20%3F;laser_duration:LaserDurationEnum%20%3F;laser_duration_numeric:decimal%20%3F;cryotherapy_freezes:integer%20%3F;freeze_thaw_cycle_number:integer%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[BiopsyAndSurgicalProcedures],[Thing]^-[BiopsyAndSurgicalProcedures])](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..*-++[BiopsyAndSurgicalProcedures&#124;age_at_procedure:integer%20%3F;protocol_procedure:NoNotreportedUnknownYesEnum%20%3F;non_protocol_timing:NonProtocolTimingEnum%20%3F;procedure:ProcedureEnum%20%3F;site:SiteEnum%20%3F;site_other:string%20%3F;extent:ExtentEnum%20%3F;outcome:OutcomeEnum%20%3F;hydrocephalus:HydrocephalusEnum%20%3F;posterior_fossa_syndrome:NoNotreportedUnknownYesEnum%20%3F;csf_diversion:CsfDiversionEnum%20%3F;nephron_sparing_partial_nephrectomy:NoNotreportedUnknownYesEnum%20%3F;surgery_type_limb:SurgeryTypeLimbEnum%20%3F;margins:MarginsEnum%20%3F;tumor_rupture:NoNotreportedUnknownYesEnum%20%3F;surgical_complications:SurgicalComplicationsEnum%20%3F;surgical_complications_other:string%20%3F;classification:ClassificationEnum%20%3F;tissue_type:TissueTypeEnum%20%3F;laterality:BilateralLeftMidlineNotreportedRightUnknownEnum%20%3F;biopsy_type:BiopsyTypeEnum%20%3F;surgery_type_amputation:SurgeryTypeAmputationEnum%20%3F;surgery_type_limb_salvage:SurgeryTypeLimbSalvageEnum%20%3F;reconstruction_type:ReconstructionTypeEnum%20%3F;procedure_extent:ProcedureExtentEnum%20%3F;met_non_lung_mgmt:NoNotreportedUnknownYesEnum%20%3F;met_lung_mgmt:MetLungMgmtEnum%20%3F;localization_technique:LocalizationTechniqueEnum%20%3F;distance_margin_tumor:decimal%20%3F;procedure_other:string%20%3F;biopsy_type_other:string%20%3F;number_nodes:NumberNodesEnum%20%3F;number_nodes_numeric:decimal%20%3F;procedure_purpose:ProcedurePurposeEnum%20%3F;procedure_purpose_other:string%20%3F;amputation_type:AmputationTypeEnum%20%3F;resection_type:ResectionTypeEnum%20%3F;distance_margin:decimal%20%3F;hemipelvectomy_type:HemipelvectomyTypeEnum%20%3F;hemipelvectomy_site:HemipelvectomySiteEnum%20%3F;intraop_adjuvant:IntraopAdjuvantEnum%20%3F;intraop_adjuvant_other:string%20%3F;laser_type:LaserTypeEnum%20%3F;laser_type_other:string%20%3F;laser_power:LaserPowerEnum%20%3F;laser_duration:LaserDurationEnum%20%3F;laser_duration_numeric:decimal%20%3F;cryotherapy_freezes:integer%20%3F;freeze_thaw_cycle_number:integer%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[BiopsyAndSurgicalProcedures],[Thing]^-[BiopsyAndSurgicalProcedures])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_procedure](age_at_procedure.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the time of this procedure.
     * Range: [Integer](types/Integer.md)
 * [time_periods](time_periods.md)  <sub>0..1</sub>
     * Range: [TimePeriod](TimePeriod.md)
 * [protocol_procedure](protocol_procedure.md)  <sub>0..1</sub>
     * Description: Was this procedure part of the treatment protocol?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [non_protocol_timing](non_protocol_timing.md)  <sub>0..1</sub>
     * Description: If a non-protocol radiation therapy, when was this radiation therapy administered?
     * Range: [NonProtocolTimingEnum](NonProtocolTimingEnum.md)
 * [procedure](procedure.md)  <sub>0..1</sub>
     * Description: A categorization of surgical procedures by type or purpose.
     * Range: [ProcedureEnum](ProcedureEnum.md)
 * [site](site.md)  <sub>0..1</sub>
     * Description: Specifies the anatomic site of a localized pathological or traumatic structural change, damage, deformity, or discontinuity of tissue, organ, or body part.
     * Range: [SiteEnum](SiteEnum.md)
 * [site_other](site_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" TUMOR_SITE
     * Range: [String](types/String.md)
 * [extent](extent.md)  <sub>0..1</sub>
     * Description: The degree to which the lesion has been cut out, or resected.
     * Range: [ExtentEnum](ExtentEnum.md)
 * [outcome](outcome.md)  <sub>0..1</sub>
     * Range: [OutcomeEnum](OutcomeEnum.md)
 * [hydrocephalus](hydrocephalus.md)  <sub>0..1</sub>
     * Description: A disorder characterized by an abnormal increase of cerebrospinal fluid in the ventricles of the brain.
     * Range: [HydrocephalusEnum](HydrocephalusEnum.md)
 * [posterior_fossa_syndrome](posterior_fossa_syndrome.md)  <sub>0..1</sub>
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [csf_diversion](csf_diversion.md)  <sub>0..1</sub>
     * Range: [CsfDiversionEnum](CsfDiversionEnum.md)
 * [nephron_sparing_partial_nephrectomy](nephron_sparing_partial_nephrectomy.md)  <sub>0..1</sub>
     * Description: If this is a renal tumor, was nephron-sparing surgery/partial nephrectomy performed?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [surgery_type_limb](surgery_type_limb.md)  <sub>0..1</sub>
     * Description: The type of surgical procedures performed on the limb of the subject.
     * Range: [SurgeryTypeLimbEnum](SurgeryTypeLimbEnum.md)
 * [margins](margins.md)  <sub>0..1</sub>
     * Description: The edge or border of the tissue removed in cancer surgery. The margin is described as negative or clean when the pathologist finds no cancer cells at the edge of the tissue, suggesting that all of the cancer has been removed. The margin is described as positive or involved when the pathologist finds cancer cells at the edge of the tissue, suggesting that all of the cancer has not been removed. (Source: NCI Dictionary of Cancer Terms)
     * Range: [MarginsEnum](MarginsEnum.md)
 * [tumor_rupture](tumor_rupture.md)  <sub>0..1</sub>
     * Description: If this is a solid tumor, was there pre-surgical tumor rupture?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [surgical_complications](surgical_complications.md)  <sub>0..1</sub>
     * Range: [SurgicalComplicationsEnum](SurgicalComplicationsEnum.md)
 * [surgical_complications_other](surgical_complications_other.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [classification](classification.md)  <sub>0..1</sub>
     * Description: The classification of a tumor based primarily on histopathological characteristics.
     * Range: [ClassificationEnum](ClassificationEnum.md)
 * [tissue_type](tissue_type.md)  <sub>0..1</sub>
     * Description: A piece of tissue removed from an organism for examination, analysis, or propagation.
     * Range: [TissueTypeEnum](TissueTypeEnum.md)
 * [laterality](laterality.md)  <sub>0..1</sub>
     * Description: A qualifier for the side of the body the tumor findings assessment is performed.
     * Range: [BilateralLeftMidlineNotreportedRightUnknownEnum](BilateralLeftMidlineNotreportedRightUnknownEnum.md)
 * [biopsy_type](biopsy_type.md)  <sub>0..1</sub>
     * Description: The removal of cells or tissues for examination by a pathologist. The pathologist may study the tissue under a microscope or perform other tests on the cells or tissue. There are many different types of biopsy procedures. The most common types include: (1) incisional biopsy, in which only a sample of tissue is removed; (2) excisional biopsy, in which an entire lump or suspicious area is removed; and (3) needle biopsy, in which a sample of tissue or fluid is removed with a needle. When a wide needle is used, the procedure is called a core biopsy. When a thin needle is used, the procedure is called a fine-needle aspiration biopsy. (Source: NCI Dictionary of Cancer Terms)
     * Range: [BiopsyTypeEnum](BiopsyTypeEnum.md)
 * [surgery_type_amputation](surgery_type_amputation.md)  <sub>0..1</sub>
     * Description: The removal by surgery of a limb (arm or leg) or other body part because of injury or disease, such as diabetes or cancer. (Source: NCI Dictionary of Cancer Terms)
     * Range: [SurgeryTypeAmputationEnum](SurgeryTypeAmputationEnum.md)
 * [surgery_type_limb_salvage](surgery_type_limb_salvage.md)  <sub>0..1</sub>
     * Description: A procedure to avoid amputation of an arm or leg.
     * Range: [SurgeryTypeLimbSalvageEnum](SurgeryTypeLimbSalvageEnum.md)
 * [reconstruction_type](reconstruction_type.md)  <sub>0..1</sub>
     * Description: The type of reconstruction performed on the subject.
     * Range: [ReconstructionTypeEnum](ReconstructionTypeEnum.md)
 * [procedure_extent](procedure_extent.md)  <sub>0..1</sub>
     * Description: The degree to which the lesion has been cut out, or resected.
     * Range: [ProcedureExtentEnum](ProcedureExtentEnum.md)
 * [met_non_lung_mgmt](met_non_lung_mgmt.md)  <sub>0..1</sub>
     * Description: Surgical treatment of metastatic disease not involving the lungs.
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [met_lung_mgmt](met_lung_mgmt.md)  <sub>0..1</sub>
     * Description: Surgical treatment of disease metastatic to the lungs.
     * Range: [MetLungMgmtEnum](MetLungMgmtEnum.md)
 * [localization_technique](localization_technique.md)  <sub>0..1</sub>
     * Description: The process of determining or marking the location or site of a tumor or disease. May also refer to the process of keeping a tumor or disease in a specific location or site. (Source: NCI Dictionary of Cancer Terms)
     * Range: [LocalizationTechniqueEnum](LocalizationTechniqueEnum.md)
 * [distance_margin_tumor](distance_margin_tumor.md)  <sub>0..1</sub>
     * Description: The distance of the closest surgical margin from tumor after surgical resection of the tumor. The closest distance between a tumor and its resection margin has prognostic significance.	
     * Range: [Decimal](types/Decimal.md)
 * [procedure_other](procedure_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" PROCEDURE_TYPE
     * Range: [String](types/String.md)
 * [biopsy_type_other](biopsy_type_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" BIOPSY_TYPE
     * Range: [String](types/String.md)
 * [number_nodes](number_nodes.md)  <sub>0..1</sub>
     * Description: A question whether an individual has a single or multiple lymph nodes involved.
     * Range: [NumberNodesEnum](NumberNodesEnum.md)
 * [number_nodes_numeric](number_nodes_numeric.md)  <sub>0..1</sub>
     * Description: The number of lymph nodes that were examined.
     * Range: [Decimal](types/Decimal.md)
 * [procedure_purpose](procedure_purpose.md)  <sub>0..1</sub>
     * Description: The reason a procedure is performed.
     * Range: [ProcedurePurposeEnum](ProcedurePurposeEnum.md)
 * [procedure_purpose_other](procedure_purpose_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" PROCEDURE_PURPOSE
     * Range: [String](types/String.md)
 * [amputation_type](amputation_type.md)  <sub>0..1</sub>
     * Description: The removal by surgery of a limb (arm or leg) or other body part because of injury or disease, such as diabetes or cancer. (Source: NCI Dictionary of Cancer Terms)
     * Range: [AmputationTypeEnum](AmputationTypeEnum.md)
 * [resection_type](resection_type.md)  <sub>0..1</sub>
     * Description: Surgery to remove tissue or part or all of an organ. (Source: NCI Dictionary of Cancer Terms)
     * Range: [ResectionTypeEnum](ResectionTypeEnum.md)
 * [distance_margin](distance_margin.md)  <sub>0..1</sub>
     * Description: The distance of the closest surgical margin from tumor after surgical resection of the tumor. The closest distance between a tumor and its resection margin has prognostic significance.
     * Range: [Decimal](types/Decimal.md)
 * [hemipelvectomy_type](hemipelvectomy_type.md)  <sub>0..1</sub>
     * Description: If the pelvis was involved, was the involved procedure internal or external?
     * Range: [HemipelvectomyTypeEnum](HemipelvectomyTypeEnum.md)
 * [hemipelvectomy_site](hemipelvectomy_site.md)  <sub>0..1</sub>
     * Description: The area involved in the hemipelvectomy.
     * Range: [HemipelvectomySiteEnum](HemipelvectomySiteEnum.md)
 * [intraop_adjuvant](intraop_adjuvant.md)  <sub>0..1</sub>
     * Description: An additional therapy administered during surgery.
     * Range: [IntraopAdjuvantEnum](IntraopAdjuvantEnum.md)
 * [intraop_adjuvant_other](intraop_adjuvant_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" INTRAOP_ADJUVANT
     * Range: [String](types/String.md)
 * [laser_type](laser_type.md)  <sub>0..1</sub>
     * Range: [LaserTypeEnum](LaserTypeEnum.md)
 * [laser_type_other](laser_type_other.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [laser_power](laser_power.md)  <sub>0..1</sub>
     * Range: [LaserPowerEnum](LaserPowerEnum.md)
 * [laser_duration](laser_duration.md)  <sub>0..1</sub>
     * Range: [LaserDurationEnum](LaserDurationEnum.md)
 * [laser_duration_numeric](laser_duration_numeric.md)  <sub>0..1</sub>
     * Range: [Decimal](types/Decimal.md)
 * [cryotherapy_freezes](cryotherapy_freezes.md)  <sub>0..1</sub>
     * Description: Number of cryotherapy freezes
     * Range: [Integer](types/Integer.md)
 * [freeze_thaw_cycle_number](freeze_thaw_cycle_number.md)  <sub>0..1</sub>
     * Description: Number of freeze-thaw cycle
     * Range: [Integer](types/Integer.md)
 * [subjects](subjects.md)  <sub>1..\*</sub>
     * Range: [Subject](Subject.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
