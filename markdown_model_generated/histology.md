
# Class: Histology




URI: [https://w3id.org/pcdc/model/Histology](https://w3id.org/pcdc/model/Histology)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[Histology&#124;age_at_hist_assessment:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;hist_assessment_review:HistAssessmentReviewEnum%20%3F;histology:HistologyEnum%20%3F;histology_result:string%20%3F;histology_result_numeric:integer%20%3F;histology_result_unit:NotreportedUnknownEnum%20%3F;histology_grade:HistologyGradeEnum%20%3F;hist_icd_o_morph_code:string%20%3F;mature_glial_implants:NoNotreportedUnknownYesEnum%20%3F;somatic_malignancy_type:SomaticMalignancyTypeEnum%20%3F;histology_inpc:HistologyInpcEnum%20%3F;who_aml:WhoAmlEnum%20%3F;fab_type:FabTypeEnum%20%3F;all_type:AllTypeEnum%20%3F;mpal:NoNotreportedUnknownYesEnum%20%3F;mlds:NoNotreportedUnknownYesEnum%20%3F;tamds:NoNotreportedUnknownYesEnum%20%3F;secondary_aml:NoNotreportedUnknownYesEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[Histology])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[Histology&#124;age_at_hist_assessment:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;hist_assessment_review:HistAssessmentReviewEnum%20%3F;histology:HistologyEnum%20%3F;histology_result:string%20%3F;histology_result_numeric:integer%20%3F;histology_result_unit:NotreportedUnknownEnum%20%3F;histology_grade:HistologyGradeEnum%20%3F;hist_icd_o_morph_code:string%20%3F;mature_glial_implants:NoNotreportedUnknownYesEnum%20%3F;somatic_malignancy_type:SomaticMalignancyTypeEnum%20%3F;histology_inpc:HistologyInpcEnum%20%3F;who_aml:WhoAmlEnum%20%3F;fab_type:FabTypeEnum%20%3F;all_type:AllTypeEnum%20%3F;mpal:NoNotreportedUnknownYesEnum%20%3F;mlds:NoNotreportedUnknownYesEnum%20%3F;tamds:NoNotreportedUnknownYesEnum%20%3F;secondary_aml:NoNotreportedUnknownYesEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[Histology])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_hist_assessment](age_at_hist_assessment.md)  <sub>0..1</sub>
     * Description: Age in Days of Histology Assessment
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
 * [hist_assessment_review](hist_assessment_review.md)  <sub>0..1</sub>
     * Description: Institutional or Central Histological Assessment
     * Range: [HistAssessmentReviewEnum](HistAssessmentReviewEnum.md)
 * [histology](histology.md)  <sub>0..1</sub>
     * Description: The study of tissues and cells under a microscope (Source: NCI Dictionary of Cancer Terms)
     * Range: [HistologyEnum](HistologyEnum.md)
 * [histology_result](histology_result.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [histology_result_numeric](histology_result_numeric.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
 * [histology_result_unit](histology_result_unit.md)  <sub>0..1</sub>
     * Description: Numeric Histology Result Unit
     * Range: [NotreportedUnknownEnum](NotreportedUnknownEnum.md)
 * [histology_grade](histology_grade.md)  <sub>0..1</sub>
     * Range: [HistologyGradeEnum](HistologyGradeEnum.md)
 * [hist_icd_o_morph_code](hist_icd_o_morph_code.md)  <sub>0..1</sub>
     * Description: Histology ICD-O Morphology Code
     * Range: [String](types/String.md)
 * [mature_glial_implants](mature_glial_implants.md)  <sub>0..1</sub>
     * Description: Mature Glial Implants Present
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [somatic_malignancy_type](somatic_malignancy_type.md)  <sub>0..1</sub>
     * Range: [SomaticMalignancyTypeEnum](SomaticMalignancyTypeEnum.md)
 * [histology_inpc](histology_inpc.md)  <sub>0..1</sub>
     * Description: Revised INPC Prognostic Group (2003)
     * Range: [HistologyInpcEnum](HistologyInpcEnum.md)
 * [who_aml](who_aml.md)  <sub>0..1</sub>
     * Description: WHO AML Classification of Tumors
     * Range: [WhoAmlEnum](WhoAmlEnum.md)
 * [fab_type](fab_type.md)  <sub>0..1</sub>
     * Description: French-American-British Classification
     * Range: [FabTypeEnum](FabTypeEnum.md)
 * [all_type](all_type.md)  <sub>0..1</sub>
     * Range: [AllTypeEnum](AllTypeEnum.md)
 * [mpal](mpal.md)  <sub>0..1</sub>
     * Description: Mixed Phenotype Acute Leukemia
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [mlds](mlds.md)  <sub>0..1</sub>
     * Description: Myeloid Leukemia Associated with Down Syndrome
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [tamds](tamds.md)  <sub>0..1</sub>
     * Description: AML Diagnosed Within Four Years of Transient Abnormal Myelopoiesis Associated with Down Syndrome Diagnosis
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [secondary_aml](secondary_aml.md)  <sub>0..1</sub>
     * Description: Secondary Acute Myeloid Leukemia
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
