
# Class: BiopsyAndSurgicalProcedures




URI: [https://w3id.org/pcdc/model/BiopsyAndSurgicalProcedures](https://w3id.org/pcdc/model/BiopsyAndSurgicalProcedures)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[BiopsyAndSurgicalProcedures&#124;age_at_procedure:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;protocol_procedure:NoNotreportedUnknownYesEnum%20%3F;non_protocol_timing:NonProtocolTimingEnum%20%3F;tumor_classification:TumorClassificationEnum%20%3F;tumor_tissue_type:BoneNotreportedSofttissueUnknownEnum%20%3F;procedure_site:ProcedureSiteEnum%20%3F;procedure_laterality:ProcedureLateralityEnum%20%3F;procedure_type:ProcedureTypeEnum%20%3F;surgery_type_limb:SurgeryTypeLimbEnum%20%3F;amputation_type:AmputationTypeEnum%20%3F;resection_type:ResectionTypeEnum%20%3F;surgery_type_limb_salvage:SurgeryTypeLimbSalvageEnum%20%3F;reconstruction_type:ReconstructionTypeEnum%20%3F;procedure_extent:ProcedureExtentEnum%20%3F;margins:MarginsEnum%20%3F;biopsy_type:BiopsyTypeEnum%20%3F;met_non_lung_mgmt:NoNotreportedUnknownYesEnum%20%3F;met_lung_mgmt:MetLungMgmtEnum%20%3F;localization_technique:LocalizationTechniqueEnum%20%3F;distance_margin_tumor:integer%20%3F;pelvic_involvement:PelvicInvolvementEnum%20%3F;surgery:NoNotreportedUnknownYesEnum%20%3F;number_nodes:NumberNodesEnum%20%3F;number_nodes_numeric:integer%20%3F;procedure_purpose:ProcedurePurposeEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[BiopsyAndSurgicalProcedures])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[BiopsyAndSurgicalProcedures&#124;age_at_procedure:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;protocol_procedure:NoNotreportedUnknownYesEnum%20%3F;non_protocol_timing:NonProtocolTimingEnum%20%3F;tumor_classification:TumorClassificationEnum%20%3F;tumor_tissue_type:BoneNotreportedSofttissueUnknownEnum%20%3F;procedure_site:ProcedureSiteEnum%20%3F;procedure_laterality:ProcedureLateralityEnum%20%3F;procedure_type:ProcedureTypeEnum%20%3F;surgery_type_limb:SurgeryTypeLimbEnum%20%3F;amputation_type:AmputationTypeEnum%20%3F;resection_type:ResectionTypeEnum%20%3F;surgery_type_limb_salvage:SurgeryTypeLimbSalvageEnum%20%3F;reconstruction_type:ReconstructionTypeEnum%20%3F;procedure_extent:ProcedureExtentEnum%20%3F;margins:MarginsEnum%20%3F;biopsy_type:BiopsyTypeEnum%20%3F;met_non_lung_mgmt:NoNotreportedUnknownYesEnum%20%3F;met_lung_mgmt:MetLungMgmtEnum%20%3F;localization_technique:LocalizationTechniqueEnum%20%3F;distance_margin_tumor:integer%20%3F;pelvic_involvement:PelvicInvolvementEnum%20%3F;surgery:NoNotreportedUnknownYesEnum%20%3F;number_nodes:NumberNodesEnum%20%3F;number_nodes_numeric:integer%20%3F;procedure_purpose:ProcedurePurposeEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[BiopsyAndSurgicalProcedures])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_procedure](age_at_procedure.md)  <sub>0..1</sub>
     * Description: Age in Days at Procedure
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
 * [protocol_procedure](protocol_procedure.md)  <sub>0..1</sub>
     * Description: Was this procedure part of the treatment protocol?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [non_protocol_timing](non_protocol_timing.md)  <sub>0..1</sub>
     * Description: If a non-protocol medication, when was this medication administered?
     * Range: [NonProtocolTimingEnum](NonProtocolTimingEnum.md)
 * [tumor_classification](tumor_classification.md)  <sub>0..1</sub>
     * Description: Tumor Classification
     * Range: [TumorClassificationEnum](TumorClassificationEnum.md)
 * [tumor_tissue_type](tumor_tissue_type.md)  <sub>0..1</sub>
     * Description: Radiation Therapy Tissue Type
     * Range: [BoneNotreportedSofttissueUnknownEnum](BoneNotreportedSofttissueUnknownEnum.md)
 * [procedure_site](procedure_site.md)  <sub>0..1</sub>
     * Description: Procedure Site
     * Range: [ProcedureSiteEnum](ProcedureSiteEnum.md)
 * [procedure_laterality](procedure_laterality.md)  <sub>0..1</sub>
     * Description: Procedure Laterality
     * Range: [ProcedureLateralityEnum](ProcedureLateralityEnum.md)
 * [procedure_type](procedure_type.md)  <sub>0..1</sub>
     * Description: Procedure Type
     * Range: [ProcedureTypeEnum](ProcedureTypeEnum.md)
 * [surgery_type_limb](surgery_type_limb.md)  <sub>0..1</sub>
     * Description: Limb Surgery Type
     * Range: [SurgeryTypeLimbEnum](SurgeryTypeLimbEnum.md)
 * [amputation_type](amputation_type.md)  <sub>0..1</sub>
     * Description: The removal by surgery of a limb (arm or leg) or other body part because of injury or disease, such as diabetes or cancer. (Source: NCI Dictionary of Cancer Terms)
     * Range: [AmputationTypeEnum](AmputationTypeEnum.md)
 * [resection_type](resection_type.md)  <sub>0..1</sub>
     * Description: Surgery to remove tissue or part or all of an organ. (Source: NCI Dictionary of Cancer Terms)
     * Range: [ResectionTypeEnum](ResectionTypeEnum.md)
 * [surgery_type_limb_salvage](surgery_type_limb_salvage.md)  <sub>0..1</sub>
     * Description: Limb Salvage Surgery Type
     * Range: [SurgeryTypeLimbSalvageEnum](SurgeryTypeLimbSalvageEnum.md)
 * [reconstruction_type](reconstruction_type.md)  <sub>0..1</sub>
     * Description: Surgical Reconstruction Type
     * Range: [ReconstructionTypeEnum](ReconstructionTypeEnum.md)
 * [procedure_extent](procedure_extent.md)  <sub>0..1</sub>
     * Description: Procedure Extent
     * Range: [ProcedureExtentEnum](ProcedureExtentEnum.md)
 * [margins](margins.md)  <sub>0..1</sub>
     * Description: The edge or border of the tissue removed in cancer surgery. The margin is described as negative or clean when the pathologist finds no cancer cells at the edge of the tissue, suggesting that all of the cancer has been removed. The margin is described as positive or involved when the pathologist finds cancer cells at the edge of the tissue, suggesting that all of the cancer has not been removed. (Source: NCI Dictionary of Cancer Terms)
     * Range: [MarginsEnum](MarginsEnum.md)
 * [biopsy_type](biopsy_type.md)  <sub>0..1</sub>
     * Description: The removal of cells or tissues for examination by a pathologist. The pathologist may study the tissue under a microscope or perform other tests on the cells or tissue. There are many different types of biopsy procedures. The most common types include: (1) incisional biopsy, in which only a sample of tissue is removed; (2) excisional biopsy, in which an entire lump or suspicious area is removed; and (3) needle biopsy, in which a sample of tissue or fluid is removed with a needle. When a wide needle is used, the procedure is called a core biopsy. When a thin needle is used, the procedure is called a fine-needle aspiration biopsy. (Source: NCI Dictionary of Cancer Terms)
     * Range: [BiopsyTypeEnum](BiopsyTypeEnum.md)
 * [met_non_lung_mgmt](met_non_lung_mgmt.md)  <sub>0..1</sub>
     * Description: Non-lung Metastatic Site Surgical Management
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [met_lung_mgmt](met_lung_mgmt.md)  <sub>0..1</sub>
     * Description: Metastatic Lung Disease Surgical Management
     * Range: [MetLungMgmtEnum](MetLungMgmtEnum.md)
 * [localization_technique](localization_technique.md)  <sub>0..1</sub>
     * Description: The process of determining or marking the location or site of a lesion or disease. May also refer to the process of keeping a lesion or disease in a specific location or site. (Source: NCI Dictionary of Cancer Terms)
     * Range: [LocalizationTechniqueEnum](LocalizationTechniqueEnum.md)
 * [distance_margin_tumor](distance_margin_tumor.md)  <sub>0..1</sub>
     * Description: Closest Distance from Margin to Resected Tumor
     * Range: [Integer](types/Integer.md)
 * [pelvic_involvement](pelvic_involvement.md)  <sub>0..1</sub>
     * Description: Pelvic Involvement
     * Range: [PelvicInvolvementEnum](PelvicInvolvementEnum.md)
 * [surgery](surgery.md)  <sub>0..1</sub>
     * Description: A procedure to remove or repair a part of the body or to find out whether disease is present. Also called operation. (Source: NCI Dictionary of Cancer Terms)
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [number_nodes](number_nodes.md)  <sub>0..1</sub>
     * Description: Involved Lymph Nodes Single or Multiple
     * Range: [NumberNodesEnum](NumberNodesEnum.md)
 * [number_nodes_numeric](number_nodes_numeric.md)  <sub>0..1</sub>
     * Description: Number of Involved Lymph Nodes
     * Range: [Integer](types/Integer.md)
 * [procedure_purpose](procedure_purpose.md)  <sub>0..1</sub>
     * Description: Procedure Purpose
     * Range: [ProcedurePurposeEnum](ProcedurePurposeEnum.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
