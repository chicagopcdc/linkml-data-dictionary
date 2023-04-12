
# Class: Tumor Assessment




URI: [https://w3id.org/pcdc/model/TumorAssessment](https://w3id.org/pcdc/model/TumorAssessment)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Subject]<subjects%201..*-++[TumorAssessment&#124;age_at_assessment:integer%20%3F;detection_method:DetectionMethodEnum%20%3F;review_source:ReviewSourceEnum%20%3F;mri_sequence:MriSequenceEnum%20%3F;tumor_presentation:TumorPresentationEnum%20%3F;classification:ClassificationEnum%20%3F;site:SiteEnum%20%3F;site_other:string%20%3F;age_at_tumor_assessment:integer%20%3F;status:StatusEnum%20%3F;assessment_reason:AssessmentReasonEnum%20%3F;morph_code:string%20%3F;morph_code_txt:string%20%3F;morph_code_system:MorphCodeSystemEnum%20%3F;morph_code_system_version:string%20%3F;top_code:string%20%3F;top_code_txt:string%20%3F;top_code_system:TopCodeSystemEnum%20%3F;top_code_system_version:string%20%3F;longest_diam_dim1:decimal%20%3F;longest_diam_dim2:decimal%20%3F;longest_diam_dim3:decimal%20%3F;tumor_submitter_id:string%20%3F;primary_tumor_submitter_id:string%20%3F;tissue_type:TissueTypeEnum%20%3F;classification_status:ClassificationStatusEnum%20%3F;multiplicity:MultiplicityEnum%20%3F;tumor_size:TumorSizeEnum%20%3F;tumor_volume:TumorVolumeEnum%20%3F;estimated_volume:decimal%20%3F;laterality:BilateralLeftMidlineNotreportedRightUnknownEnum%20%3F;fracture:NoNotreportedUnknownYesEnum%20%3F;skip_tumor:NoNotreportedUnknownYesEnum%20%3F;ipsilateral_nodules:NoNotreportedUnknownYesEnum%20%3F;joint_involvement:NoNotreportedUnknownYesEnum%20%3F;site_within_bone:SiteWithinBoneEnum%20%3F;nodal_involvement:NoNotreportedUnknownYesEnum%20%3F;nodal_site:NodalSiteEnum%20%3F;extension_tumor_type:ExtensionTumorTypeEnum%20%3F;detection_method_other:string%20%3F;e_extension_site:EExtensionSiteEnum%20%3F;e_extension_site_other:string%20%3F;diam_type:DiamTypeEnum%20%3F;bulky_disease:NoNotreportedUnknownYesEnum%20%3F;effusion:NoNotreportedUnknownYesEnum%20%3F;effusion_type:EffusionTypeEnum%20%3F;response:ResponseEnum%20%3F;pct_change:decimal%20%3F;course_timepoint:CourseTimepointEnum%20%3F;tumor_type:TumorTypeEnum%20%3F;mibg_avidity:NoNotreportedUnknownYesEnum%20%3F;invasiveness_status:NoNotreportedUnknownYesEnum%20%3F;depth:DepthEnum%20%3F;skip_met_involvement:SkipMetInvolvementEnum%20%3F;fracture_site:NoNotreportedUnknownYesEnum%20%3F;massive_choroidal_extension:MassiveChoroidalExtensionEnum%20%3F;visual_discrete_tumors:NoNotreportedUnknownYesEnum%20%3F;tumor_number:decimal%20%3F;tumor_from_fovea:TumorFromFoveaEnum%20%3F;tumor_from_optic_nerve:TumorFromOpticNerveEnum%20%3F;fluid_from_tumor:FluidFromTumorEnum%20%3F;seeds_present:NoNotreportedUnknownYesEnum%20%3F;seeds_pattern:SeedsPatternEnum%20%3F;seeds_status:SeedsStatusEnum%20%3F;seeds_classification:SeedsClassificationEnum%20%3F;invasiveness:InvasivenessEnum%20%3F;nodal_determination:NodalDeterminationEnum%20%3F;nodal_determination_source:NodalDeterminationSourceEnum%20%3F;parameningeal_extension:NoNotreportedUnknownYesEnum%20%3F;necrosis_status:AbsentNotreportedPresentUnknownEnum%20%3F;necrosis_pct_numeric:decimal%20%3F;anaplasia_status:AbsentNotreportedPresentUnknownEnum%20%3F;anaplasia_type:AnaplasiaTypeEnum%20%3F;anaplasia_pct_numeric:decimal%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[TumorAssessment],[Thing]^-[TumorAssessment],[TimePeriod],[Thing],[Subject])](https://yuml.me/diagram/nofunky;dir:TB/class/[Subject]<subjects%201..*-++[TumorAssessment&#124;age_at_assessment:integer%20%3F;detection_method:DetectionMethodEnum%20%3F;review_source:ReviewSourceEnum%20%3F;mri_sequence:MriSequenceEnum%20%3F;tumor_presentation:TumorPresentationEnum%20%3F;classification:ClassificationEnum%20%3F;site:SiteEnum%20%3F;site_other:string%20%3F;age_at_tumor_assessment:integer%20%3F;status:StatusEnum%20%3F;assessment_reason:AssessmentReasonEnum%20%3F;morph_code:string%20%3F;morph_code_txt:string%20%3F;morph_code_system:MorphCodeSystemEnum%20%3F;morph_code_system_version:string%20%3F;top_code:string%20%3F;top_code_txt:string%20%3F;top_code_system:TopCodeSystemEnum%20%3F;top_code_system_version:string%20%3F;longest_diam_dim1:decimal%20%3F;longest_diam_dim2:decimal%20%3F;longest_diam_dim3:decimal%20%3F;tumor_submitter_id:string%20%3F;primary_tumor_submitter_id:string%20%3F;tissue_type:TissueTypeEnum%20%3F;classification_status:ClassificationStatusEnum%20%3F;multiplicity:MultiplicityEnum%20%3F;tumor_size:TumorSizeEnum%20%3F;tumor_volume:TumorVolumeEnum%20%3F;estimated_volume:decimal%20%3F;laterality:BilateralLeftMidlineNotreportedRightUnknownEnum%20%3F;fracture:NoNotreportedUnknownYesEnum%20%3F;skip_tumor:NoNotreportedUnknownYesEnum%20%3F;ipsilateral_nodules:NoNotreportedUnknownYesEnum%20%3F;joint_involvement:NoNotreportedUnknownYesEnum%20%3F;site_within_bone:SiteWithinBoneEnum%20%3F;nodal_involvement:NoNotreportedUnknownYesEnum%20%3F;nodal_site:NodalSiteEnum%20%3F;extension_tumor_type:ExtensionTumorTypeEnum%20%3F;detection_method_other:string%20%3F;e_extension_site:EExtensionSiteEnum%20%3F;e_extension_site_other:string%20%3F;diam_type:DiamTypeEnum%20%3F;bulky_disease:NoNotreportedUnknownYesEnum%20%3F;effusion:NoNotreportedUnknownYesEnum%20%3F;effusion_type:EffusionTypeEnum%20%3F;response:ResponseEnum%20%3F;pct_change:decimal%20%3F;course_timepoint:CourseTimepointEnum%20%3F;tumor_type:TumorTypeEnum%20%3F;mibg_avidity:NoNotreportedUnknownYesEnum%20%3F;invasiveness_status:NoNotreportedUnknownYesEnum%20%3F;depth:DepthEnum%20%3F;skip_met_involvement:SkipMetInvolvementEnum%20%3F;fracture_site:NoNotreportedUnknownYesEnum%20%3F;massive_choroidal_extension:MassiveChoroidalExtensionEnum%20%3F;visual_discrete_tumors:NoNotreportedUnknownYesEnum%20%3F;tumor_number:decimal%20%3F;tumor_from_fovea:TumorFromFoveaEnum%20%3F;tumor_from_optic_nerve:TumorFromOpticNerveEnum%20%3F;fluid_from_tumor:FluidFromTumorEnum%20%3F;seeds_present:NoNotreportedUnknownYesEnum%20%3F;seeds_pattern:SeedsPatternEnum%20%3F;seeds_status:SeedsStatusEnum%20%3F;seeds_classification:SeedsClassificationEnum%20%3F;invasiveness:InvasivenessEnum%20%3F;nodal_determination:NodalDeterminationEnum%20%3F;nodal_determination_source:NodalDeterminationSourceEnum%20%3F;parameningeal_extension:NoNotreportedUnknownYesEnum%20%3F;necrosis_status:AbsentNotreportedPresentUnknownEnum%20%3F;necrosis_pct_numeric:decimal%20%3F;anaplasia_status:AbsentNotreportedPresentUnknownEnum%20%3F;anaplasia_type:AnaplasiaTypeEnum%20%3F;anaplasia_pct_numeric:decimal%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[TumorAssessment],[Thing]^-[TumorAssessment],[TimePeriod],[Thing],[Subject])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_assessment](age_at_assessment.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the time of this tumor assessment.
     * Range: [Integer](types/Integer.md)
 * [time_periods](time_periods.md)  <sub>0..1</sub>
     * Range: [TimePeriod](TimePeriod.md)
 * [detection_method](detection_method.md)  <sub>0..1</sub>
     * Description: Disease Involvement Detection Method
     * Range: [DetectionMethodEnum](DetectionMethodEnum.md)
 * [review_source](review_source.md)  <sub>0..1</sub>
     * Description: The type of assessment that was used to review.
     * Range: [ReviewSourceEnum](ReviewSourceEnum.md)
 * [mri_sequence](mri_sequence.md)  <sub>0..1</sub>
     * Range: [MriSequenceEnum](MriSequenceEnum.md)
 * [tumor_presentation](tumor_presentation.md)  <sub>0..1</sub>
     * Range: [TumorPresentationEnum](TumorPresentationEnum.md)
 * [classification](classification.md)  <sub>0..1</sub>
     * Description: The classification of a tumor based primarily on histopathological characteristics.
     * Range: [ClassificationEnum](ClassificationEnum.md)
 * [site](site.md)  <sub>0..1</sub>
     * Description: Specifies the anatomic site of a localized pathological or traumatic structural change, damage, deformity, or discontinuity of tissue, organ, or body part.
     * Range: [SiteEnum](SiteEnum.md)
 * [site_other](site_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" TUMOR_SITE
     * Range: [String](types/String.md)
 * [age_at_tumor_assessment](age_at_tumor_assessment.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the time of this tumor assessment.
     * Range: [Integer](types/Integer.md)
 * [status](status.md)  <sub>0..1</sub>
     * Description: Is this mutation/abnormality present in this subject?
     * Range: [StatusEnum](StatusEnum.md)
 * [assessment_reason](assessment_reason.md)  <sub>0..1</sub>
     * Range: [AssessmentReasonEnum](AssessmentReasonEnum.md)
 * [morph_code](morph_code.md)  <sub>0..1</sub>
     * Description: The code for the morphology of the subsequent tumor
     * Range: [String](types/String.md)
 * [morph_code_txt](morph_code_txt.md)  <sub>0..1</sub>
     * Description: The display text for MORPH_CODE 
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
 * [top_code_txt](top_code_txt.md)  <sub>0..1</sub>
     * Description: The display text for TOP_CODE 
     * Range: [String](types/String.md)
 * [top_code_system](top_code_system.md)  <sub>0..1</sub>
     * Description: The coding system for the code used in TOP_CODE
     * Range: [TopCodeSystemEnum](TopCodeSystemEnum.md)
 * [top_code_system_version](top_code_system_version.md)  <sub>0..1</sub>
     * Description: The version of the coding system indicated in TOP_CODE_SYSTEM
     * Range: [String](types/String.md)
 * [longest_diam_dim1](longest_diam_dim1.md)  <sub>0..1</sub>
     * Description: Longest Diameter of Tumor Dimension 1 (cm)
     * Range: [Decimal](types/Decimal.md)
 * [longest_diam_dim2](longest_diam_dim2.md)  <sub>0..1</sub>
     * Description: Longest Diameter of Tumor Dimension 2 (cm)
     * Range: [Decimal](types/Decimal.md)
 * [longest_diam_dim3](longest_diam_dim3.md)  <sub>0..1</sub>
     * Description: Longest Diameter of Tumor Dimension 3 (cm)
     * Range: [Decimal](types/Decimal.md)
 * [tumor_submitter_id](tumor_submitter_id.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [primary_tumor_submitter_id](primary_tumor_submitter_id.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [tissue_type](tissue_type.md)  <sub>0..1</sub>
     * Description: A piece of tissue removed from an organism for examination, analysis, or propagation.
     * Range: [TissueTypeEnum](TissueTypeEnum.md)
 * [classification_status](classification_status.md)  <sub>0..1</sub>
     * Description: The status of the tumor classification whether it was completed or not.
     * Range: [ClassificationStatusEnum](ClassificationStatusEnum.md)
 * [multiplicity](multiplicity.md)  <sub>0..1</sub>
     * Description: This variable indicates if the recorded observation is detailing a single tumor or multiple tumors at a given site.
     * Range: [MultiplicityEnum](MultiplicityEnum.md)
 * [tumor_size](tumor_size.md)  <sub>0..1</sub>
     * Description: The tumor size of the largest tumor.
     * Range: [TumorSizeEnum](TumorSizeEnum.md)
 * [tumor_volume](tumor_volume.md)  <sub>0..1</sub>
     * Description: The size of a cancer measured by the amount of space taken up by the tumor. For example, the tumor volume of prostate cancer is the percentage of the prostate taken up by the tumor.
     * Range: [TumorVolumeEnum](TumorVolumeEnum.md)
 * [estimated_volume](estimated_volume.md)  <sub>0..1</sub>
     * Description: Estimated Volume (mL)
     * Range: [Decimal](types/Decimal.md)
 * [laterality](laterality.md)  <sub>0..1</sub>
     * Description: A qualifier for the side of the body the tumor findings assessment is performed.
     * Range: [BilateralLeftMidlineNotreportedRightUnknownEnum](BilateralLeftMidlineNotreportedRightUnknownEnum.md)
 * [fracture](fracture.md)  <sub>0..1</sub>
     * Description: Fracture at Primary Site
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [skip_tumor](skip_tumor.md)  <sub>0..1</sub>
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
 * [nodal_involvement](nodal_involvement.md)  <sub>0..1</sub>
     * Description: Regional Lymph Node Involvement
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [nodal_site](nodal_site.md)  <sub>0..1</sub>
     * Description: The anatomic site of a tumor node.
     * Range: [NodalSiteEnum](NodalSiteEnum.md)
 * [extension_tumor_type](extension_tumor_type.md)  <sub>0..1</sub>
     * Range: [ExtensionTumorTypeEnum](ExtensionTumorTypeEnum.md)
 * [detection_method_other](detection_method_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" DETECTION_METHOD
     * Range: [String](types/String.md)
 * [e_extension_site](e_extension_site.md)  <sub>0..1</sub>
     * Description: The anatomic location outside of the lymph nodes into which a disease lesion has directly spread.
     * Range: [EExtensionSiteEnum](EExtensionSiteEnum.md)
 * [e_extension_site_other](e_extension_site_other.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [diam_type](diam_type.md)  <sub>0..1</sub>
     * Description: The orientation of the diameters provided
     * Range: [DiamTypeEnum](DiamTypeEnum.md)
 * [bulky_disease](bulky_disease.md)  <sub>0..1</sub>
     * Description: Is this nodal mass big enough to be classified as bulky disease?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [effusion](effusion.md)  <sub>0..1</sub>
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [effusion_type](effusion_type.md)  <sub>0..1</sub>
     * Range: [EffusionTypeEnum](EffusionTypeEnum.md)
 * [response](response.md)  <sub>0..1</sub>
     * Description: A qualitative or quantitative measurement of the response of a target lesion(s) to the therapy.
     * Range: [ResponseEnum](ResponseEnum.md)
 * [pct_change](pct_change.md)  <sub>0..1</sub>
     * Description: The percentage of change in a particular lesion.
     * Range: [Decimal](types/Decimal.md)
 * [course_timepoint](course_timepoint.md)  <sub>0..1</sub>
     * Description: This variable gives more precise granularity to when an observation occured during the period of the indicated "Course" TIME_PERIOD
     * Range: [CourseTimepointEnum](CourseTimepointEnum.md)
 * [tumor_type](tumor_type.md)  <sub>0..1</sub>
     * Range: [TumorTypeEnum](TumorTypeEnum.md)
 * [mibg_avidity](mibg_avidity.md)  <sub>0..1</sub>
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [invasiveness_status](invasiveness_status.md)  <sub>0..1</sub>
     * Description: Tumor Invasiveness
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [depth](depth.md)  <sub>0..1</sub>
     * Description: The depth of the tumor.
     * Range: [DepthEnum](DepthEnum.md)
 * [skip_met_involvement](skip_met_involvement.md)  <sub>0..1</sub>
     * Description: A question about the areas involved in the skip metastasis.
     * Range: [SkipMetInvolvementEnum](SkipMetInvolvementEnum.md)
 * [fracture_site](fracture_site.md)  <sub>0..1</sub>
     * Description: If the anatomical site of the tumor is within a bone, is that bone fractured?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [massive_choroidal_extension](massive_choroidal_extension.md)  <sub>0..1</sub>
     * Range: [MassiveChoroidalExtensionEnum](MassiveChoroidalExtensionEnum.md)
 * [visual_discrete_tumors](visual_discrete_tumors.md)  <sub>0..1</sub>
     * Description: Visual Disrete Tumors
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [tumor_number](tumor_number.md)  <sub>0..1</sub>
     * Description: The number of tumors found.
     * Range: [Decimal](types/Decimal.md)
 * [tumor_from_fovea](tumor_from_fovea.md)  <sub>0..1</sub>
     * Description: Tumor Distance from Fovea of the Closest Tumor
     * Range: [TumorFromFoveaEnum](TumorFromFoveaEnum.md)
 * [tumor_from_optic_nerve](tumor_from_optic_nerve.md)  <sub>0..1</sub>
     * Description: Tumor Distance from Optic Nerve of the Closest Tumor
     * Range: [TumorFromOpticNerveEnum](TumorFromOpticNerveEnum.md)
 * [fluid_from_tumor](fluid_from_tumor.md)  <sub>0..1</sub>
     * Description: Fluid from Tumor Base
     * Range: [FluidFromTumorEnum](FluidFromTumorEnum.md)
 * [seeds_present](seeds_present.md)  <sub>0..1</sub>
     * Description: Retinoblastoma Seeds Present
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [seeds_pattern](seeds_pattern.md)  <sub>0..1</sub>
     * Description: Retinoblastoma Seeds Pattern
     * Range: [SeedsPatternEnum](SeedsPatternEnum.md)
 * [seeds_status](seeds_status.md)  <sub>0..1</sub>
     * Description: Retinoblastoma Seeds Status
     * Range: [SeedsStatusEnum](SeedsStatusEnum.md)
 * [seeds_classification](seeds_classification.md)  <sub>0..1</sub>
     * Description: Retinoblastoma Seeds Classification
     * Range: [SeedsClassificationEnum](SeedsClassificationEnum.md)
 * [invasiveness](invasiveness.md)  <sub>0..1</sub>
     * Description: Tumor Invasiveness
     * Range: [InvasivenessEnum](InvasivenessEnum.md)
 * [nodal_determination](nodal_determination.md)  <sub>0..1</sub>
     * Description: Determination of Regional Lymph Node Involvement
     * Range: [NodalDeterminationEnum](NodalDeterminationEnum.md)
 * [nodal_determination_source](nodal_determination_source.md)  <sub>0..1</sub>
     * Description: The source of the determination of regional lymph node involvement. 
     * Range: [NodalDeterminationSourceEnum](NodalDeterminationSourceEnum.md)
 * [parameningeal_extension](parameningeal_extension.md)  <sub>0..1</sub>
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [necrosis_status](necrosis_status.md)  <sub>0..1</sub>
     * Description: Indicates the presence or absence of necrosis in the tumor.
     * Range: [AbsentNotreportedPresentUnknownEnum](AbsentNotreportedPresentUnknownEnum.md)
 * [necrosis_pct_numeric](necrosis_pct_numeric.md)  <sub>0..1</sub>
     * Description: The numeric percentage of necrosis found in the tumor.
     * Range: [Decimal](types/Decimal.md)
 * [anaplasia_status](anaplasia_status.md)  <sub>0..1</sub>
     * Description: Indicates the presence or absence of anaplasia in the tumor.
     * Range: [AbsentNotreportedPresentUnknownEnum](AbsentNotreportedPresentUnknownEnum.md)
 * [anaplasia_type](anaplasia_type.md)  <sub>0..1</sub>
     * Description: describes the type or extent of anaplasia found during a histopathologic exam.
     * Range: [AnaplasiaTypeEnum](AnaplasiaTypeEnum.md)
 * [anaplasia_pct_numeric](anaplasia_pct_numeric.md)  <sub>0..1</sub>
     * Description: The numeric percentage of anaplasia found in the tumor.
     * Range: [Decimal](types/Decimal.md)
 * [subjects](subjects.md)  <sub>1..\*</sub>
     * Range: [Subject](Subject.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
