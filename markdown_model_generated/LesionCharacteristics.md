
# Class: LesionCharacteristics




URI: [https://w3id.org/pcdc/model/LesionCharacteristics](https://w3id.org/pcdc/model/LesionCharacteristics)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[LesionCharacteristics&#124;age_at_lesion_assessment:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;lesion_assessment_review:LesionAssessmentReviewEnum%20%3F;lesion_state:LesionStateEnum%20%3F;detection_method:DetectionMethodEnum%20%3F;tissue_type:BoneNotreportedSofttissueUnknownEnum%20%3F;lesion_classification:LesionClassificationEnum%20%3F;lesion_presentation:LesionPresentationEnum%20%3F;lesion_site:LesionSiteEnum%20%3F;lesion_site_other:string%20%3F;morph_sno:string%20%3F;icd_o_morph:string%20%3F;morph_txt:string%20%3F;top_sno:string%20%3F;icd_o_top:string%20%3F;top_txt:string%20%3F;lesion_size:LesionSizeEnum%20%3F;longest_diam_dim1:integer%20%3F;longest_diam_dim2:integer%20%3F;longest_diam_dim3:integer%20%3F;diam_type:DiamTypeEnum%20%3F;lesion_volume:LesionVolumeEnum%20%3F;estimated_volume_numeric:integer%20%3F;computed_volume_numeric:integer%20%3F;depth:DepthEnum%20%3F;lesion_bulky:LesionBulkyEnum%20%3F;laterality:LateralityEnum%20%3F;invasiveness:InvasivenessEnum%20%3F;extension_site:ExtensionSiteEnum%20%3F;lesion_response:LesionResponseEnum%20%3F;lesion_pct_change:integer%20%3F;nodal_involvement:NoNotreportedUnknownYesEnum%20%3F;nodal_site:NodalSiteEnum%20%3F;nodal_determination:NodalDeterminationEnum%20%3F;nodal_determination_source:NodalDeterminationSourceEnum%20%3F;mibg_avidity:NoNotreportedUnknownYesEnum%20%3F;necrosis:NecrosisEnum%20%3F;necrosis_pct:integer%20%3F;parameningeal_extension:NoNotreportedUnknownYesEnum%20%3F;skip_lesion:NoNotreportedUnknownYesEnum%20%3F;ipsilateral_nodules:NoNotreportedUnknownYesEnum%20%3F;joint_involvement:NoNotreportedUnknownYesEnum%20%3F;site_within_bone:SiteWithinBoneEnum%20%3F;cartilage_percent:integer%20%3F;peritoneal_cytology:NoNotreportedUnknownYesEnum%20%3F;pleural_cytology:NoNotreportedUnknownYesEnum%20%3F;peritoneal_effusion:NoNotreportedUnknownYesEnum%20%3F;pleural_effusion:NoNotreportedUnknownYesEnum%20%3F;pericardial_effusion:NoNotreportedUnknownYesEnum%20%3F;e_extension_site:EExtensionSiteEnum%20%3F;anaplasia:AbsentNotreportedPresentUnknownEnum%20%3F;anaplasia_extent:AnaplasiaExtentEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[LesionCharacteristics])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[LesionCharacteristics&#124;age_at_lesion_assessment:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;lesion_assessment_review:LesionAssessmentReviewEnum%20%3F;lesion_state:LesionStateEnum%20%3F;detection_method:DetectionMethodEnum%20%3F;tissue_type:BoneNotreportedSofttissueUnknownEnum%20%3F;lesion_classification:LesionClassificationEnum%20%3F;lesion_presentation:LesionPresentationEnum%20%3F;lesion_site:LesionSiteEnum%20%3F;lesion_site_other:string%20%3F;morph_sno:string%20%3F;icd_o_morph:string%20%3F;morph_txt:string%20%3F;top_sno:string%20%3F;icd_o_top:string%20%3F;top_txt:string%20%3F;lesion_size:LesionSizeEnum%20%3F;longest_diam_dim1:integer%20%3F;longest_diam_dim2:integer%20%3F;longest_diam_dim3:integer%20%3F;diam_type:DiamTypeEnum%20%3F;lesion_volume:LesionVolumeEnum%20%3F;estimated_volume_numeric:integer%20%3F;computed_volume_numeric:integer%20%3F;depth:DepthEnum%20%3F;lesion_bulky:LesionBulkyEnum%20%3F;laterality:LateralityEnum%20%3F;invasiveness:InvasivenessEnum%20%3F;extension_site:ExtensionSiteEnum%20%3F;lesion_response:LesionResponseEnum%20%3F;lesion_pct_change:integer%20%3F;nodal_involvement:NoNotreportedUnknownYesEnum%20%3F;nodal_site:NodalSiteEnum%20%3F;nodal_determination:NodalDeterminationEnum%20%3F;nodal_determination_source:NodalDeterminationSourceEnum%20%3F;mibg_avidity:NoNotreportedUnknownYesEnum%20%3F;necrosis:NecrosisEnum%20%3F;necrosis_pct:integer%20%3F;parameningeal_extension:NoNotreportedUnknownYesEnum%20%3F;skip_lesion:NoNotreportedUnknownYesEnum%20%3F;ipsilateral_nodules:NoNotreportedUnknownYesEnum%20%3F;joint_involvement:NoNotreportedUnknownYesEnum%20%3F;site_within_bone:SiteWithinBoneEnum%20%3F;cartilage_percent:integer%20%3F;peritoneal_cytology:NoNotreportedUnknownYesEnum%20%3F;pleural_cytology:NoNotreportedUnknownYesEnum%20%3F;peritoneal_effusion:NoNotreportedUnknownYesEnum%20%3F;pleural_effusion:NoNotreportedUnknownYesEnum%20%3F;pericardial_effusion:NoNotreportedUnknownYesEnum%20%3F;e_extension_site:EExtensionSiteEnum%20%3F;anaplasia:AbsentNotreportedPresentUnknownEnum%20%3F;anaplasia_extent:AnaplasiaExtentEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[LesionCharacteristics])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_lesion_assessment](age_at_lesion_assessment.md)  <sub>0..1</sub>
     * Description: Age in Days at Lesion Assessment
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
 * [lesion_assessment_review](lesion_assessment_review.md)  <sub>0..1</sub>
     * Description: Institutional or Central Lesion Review
     * Range: [LesionAssessmentReviewEnum](LesionAssessmentReviewEnum.md)
 * [lesion_state](lesion_state.md)  <sub>0..1</sub>
     * Description: A condition or state of a tumor at a particular time and a particular tumor site.
     * Range: [LesionStateEnum](LesionStateEnum.md)
 * [detection_method](detection_method.md)  <sub>0..1</sub>
     * Description: The method used to detect the extent of the disease involvement.
     * Range: [DetectionMethodEnum](DetectionMethodEnum.md)
 * [tissue_type](tissue_type.md)  <sub>0..1</sub>
     * Description: A piece of tissue removed from an organism for examination, analysis, or propagation.
     * Range: [BoneNotreportedSofttissueUnknownEnum](BoneNotreportedSofttissueUnknownEnum.md)
 * [lesion_classification](lesion_classification.md)  <sub>0..1</sub>
     * Description: The classification of a lesion of interest.
     * Range: [LesionClassificationEnum](LesionClassificationEnum.md)
 * [lesion_presentation](lesion_presentation.md)  <sub>0..1</sub>
     * Range: [LesionPresentationEnum](LesionPresentationEnum.md)
 * [lesion_site](lesion_site.md)  <sub>0..1</sub>
     * Description: Specifies the anatomic site of a localized pathological or traumatic structural change, damage, deformity, or discontinuity of tissue, organ, or body part.
     * Range: [LesionSiteEnum](LesionSiteEnum.md)
 * [lesion_site_other](lesion_site_other.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [morph_sno](morph_sno.md)  <sub>0..1</sub>
     * Description: Morphology SNOMED Code
     * Range: [String](types/String.md)
 * [icd_o_morph](icd_o_morph.md)  <sub>0..1</sub>
     * Description: Morphology ICD-O Code
     * Range: [String](types/String.md)
 * [morph_txt](morph_txt.md)  <sub>0..1</sub>
     * Description: Morphology Text
     * Range: [String](types/String.md)
 * [top_sno](top_sno.md)  <sub>0..1</sub>
     * Description: Topography SNOMED Code
     * Range: [String](types/String.md)
 * [icd_o_top](icd_o_top.md)  <sub>0..1</sub>
     * Description: Topography ICD-O Code
     * Range: [String](types/String.md)
 * [top_txt](top_txt.md)  <sub>0..1</sub>
     * Description: Topography Text
     * Range: [String](types/String.md)
 * [lesion_size](lesion_size.md)  <sub>0..1</sub>
     * Range: [LesionSizeEnum](LesionSizeEnum.md)
 * [longest_diam_dim1](longest_diam_dim1.md)  <sub>0..1</sub>
     * Description: Longest Diameter of Tumor Dimension 1 (cm)
     * Range: [Integer](types/Integer.md)
 * [longest_diam_dim2](longest_diam_dim2.md)  <sub>0..1</sub>
     * Description: Longest Diameter of Tumor Dimension 2 (cm)
     * Range: [Integer](types/Integer.md)
 * [longest_diam_dim3](longest_diam_dim3.md)  <sub>0..1</sub>
     * Description: Longest Diameter of Tumor Dimension 3 (cm)
     * Range: [Integer](types/Integer.md)
 * [diam_type](diam_type.md)  <sub>0..1</sub>
     * Description: Dimension 2 Direction
     * Range: [DiamTypeEnum](DiamTypeEnum.md)
 * [lesion_volume](lesion_volume.md)  <sub>0..1</sub>
     * Range: [LesionVolumeEnum](LesionVolumeEnum.md)
 * [estimated_volume_numeric](estimated_volume_numeric.md)  <sub>0..1</sub>
     * Description: Estimated Volume (mL)
     * Range: [Integer](types/Integer.md)
 * [computed_volume_numeric](computed_volume_numeric.md)  <sub>0..1</sub>
     * Description: Computed Volume (mL)
     * Range: [Integer](types/Integer.md)
 * [depth](depth.md)  <sub>0..1</sub>
     * Description: The extent downward or inward; the perpendicular measurement from the surface downward to determine deepness.
     * Range: [DepthEnum](DepthEnum.md)
 * [lesion_bulky](lesion_bulky.md)  <sub>0..1</sub>
     * Description: Bulky Lesion
     * Range: [LesionBulkyEnum](LesionBulkyEnum.md)
 * [laterality](laterality.md)  <sub>0..1</sub>
     * Range: [LateralityEnum](LateralityEnum.md)
 * [invasiveness](invasiveness.md)  <sub>0..1</sub>
     * Description: Tumor Invasiveness
     * Range: [InvasivenessEnum](InvasivenessEnum.md)
 * [extension_site](extension_site.md)  <sub>0..1</sub>
     * Range: [ExtensionSiteEnum](ExtensionSiteEnum.md)
 * [lesion_response](lesion_response.md)  <sub>0..1</sub>
     * Range: [LesionResponseEnum](LesionResponseEnum.md)
 * [lesion_pct_change](lesion_pct_change.md)  <sub>0..1</sub>
     * Description: 2-Dimensional Percent Change of Lesion
     * Range: [Integer](types/Integer.md)
 * [nodal_involvement](nodal_involvement.md)  <sub>0..1</sub>
     * Description: Regional Lymph Node Involvement
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [nodal_site](nodal_site.md)  <sub>0..1</sub>
     * Range: [NodalSiteEnum](NodalSiteEnum.md)
 * [nodal_determination](nodal_determination.md)  <sub>0..1</sub>
     * Description: Determination of Regional Lymph Node Involvement
     * Range: [NodalDeterminationEnum](NodalDeterminationEnum.md)
 * [nodal_determination_source](nodal_determination_source.md)  <sub>0..1</sub>
     * Range: [NodalDeterminationSourceEnum](NodalDeterminationSourceEnum.md)
 * [mibg_avidity](mibg_avidity.md)  <sub>0..1</sub>
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [necrosis](necrosis.md)  <sub>0..1</sub>
     * Description: Refers to the death of living tissues.
     * Range: [NecrosisEnum](NecrosisEnum.md)
 * [necrosis_pct](necrosis_pct.md)  <sub>0..1</sub>
     * Description: Tumor Necrosis (%)
     * Range: [Integer](types/Integer.md)
 * [parameningeal_extension](parameningeal_extension.md)  <sub>0..1</sub>
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [skip_lesion](skip_lesion.md)  <sub>0..1</sub>
     * Description: A benign or malignant pathologic process which is patchy and skips areas which are normal (uninvolved by the pathologic process).
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [ipsilateral_nodules](ipsilateral_nodules.md)  <sub>0..1</sub>
     * Description: A metastatic tumor nodule located in the same side of the organ in which the primary tumor occurred.
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [joint_involvement](joint_involvement.md)  <sub>0..1</sub>
     * Description: A finding indicating the spread of cancer to a joint.
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [site_within_bone](site_within_bone.md)  <sub>0..1</sub>
     * Description: The anatomic site within the bone.
     * Range: [SiteWithinBoneEnum](SiteWithinBoneEnum.md)
 * [cartilage_percent](cartilage_percent.md)  <sub>0..1</sub>
     * Description: The percentage of cartilage.
     * Range: [Integer](types/Integer.md)
 * [peritoneal_cytology](peritoneal_cytology.md)  <sub>0..1</sub>
     * Description: An examination of cells obtained from a sample of peritoneal fluid.
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [pleural_cytology](pleural_cytology.md)  <sub>0..1</sub>
     * Description: An examination of cells obtained from a sample of pleural fluid.
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [peritoneal_effusion](peritoneal_effusion.md)  <sub>0..1</sub>
     * Description: The abnormal collection of fluid in the peritoneal cavity resulting in ascites.
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [pleural_effusion](pleural_effusion.md)  <sub>0..1</sub>
     * Description: Increased amounts of fluid within the pleural cavity. Symptoms include shortness of breath, cough, and chest pain. It is usually caused by lung infections, congestive heart failure, pleural and lung tumors, connective tissue disorders, and trauma.
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [pericardial_effusion](pericardial_effusion.md)  <sub>0..1</sub>
     * Description: Fluid collection within the pericardial sac, usually due to inflammation.
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [e_extension_site](e_extension_site.md)  <sub>0..1</sub>
     * Description: The anatomic location outside of the lymph nodes into which a disease lesion has directly spread.
     * Range: [EExtensionSiteEnum](EExtensionSiteEnum.md)
 * [anaplasia](anaplasia.md)  <sub>0..1</sub>
     * Description: Anaplasia
     * Range: [AbsentNotreportedPresentUnknownEnum](AbsentNotreportedPresentUnknownEnum.md)
 * [anaplasia_extent](anaplasia_extent.md)  <sub>0..1</sub>
     * Description: Anaplasia Extent
     * Range: [AnaplasiaExtentEnum](AnaplasiaExtentEnum.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
