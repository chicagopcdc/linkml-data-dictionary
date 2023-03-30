
# Class: SubjectResponse




URI: [https://w3id.org/pcdc/model/SubjectResponse](https://w3id.org/pcdc/model/SubjectResponse)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[SubjectResponse&#124;age_at_response:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;response_category:ResponseCategoryEnum%20%3F;tx_prior_response:TxPriorResponseEnum%20%3F;interim_response:InterimResponseEnum%20%3F;response:ResponseEnum%20%3F;response_method:ResponseMethodEnum%20%3F;response_system:ResponseSystemEnum%20%3F;response_system_version:string%20%3F;necrosis:NecrosisEnum%20%3F;necrosis_pct:integer%20%3F;bm_pct_blasts_at_response:integer%20%3F;bm_analysis_method_at_response:BmAnalysisMethodAtResponseEnum%20%3F;anc_at_response:integer%20%3F;anc_threshold_at_response:integer%20%3F;platelet_count_at_response:integer%20%3F;platelet_threshold_at_response:NoNotreportedUnknownYesEnum%20%3F;symptoms:NoNotreportedUnknownYesEnum%20%3F;palpable_nodes:NoNotreportedUnknownYesEnum%20%3F;nodular_splenic:NoNotreportedUnknownYesEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[SubjectResponse])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[SubjectResponse&#124;age_at_response:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;response_category:ResponseCategoryEnum%20%3F;tx_prior_response:TxPriorResponseEnum%20%3F;interim_response:InterimResponseEnum%20%3F;response:ResponseEnum%20%3F;response_method:ResponseMethodEnum%20%3F;response_system:ResponseSystemEnum%20%3F;response_system_version:string%20%3F;necrosis:NecrosisEnum%20%3F;necrosis_pct:integer%20%3F;bm_pct_blasts_at_response:integer%20%3F;bm_analysis_method_at_response:BmAnalysisMethodAtResponseEnum%20%3F;anc_at_response:integer%20%3F;anc_threshold_at_response:integer%20%3F;platelet_count_at_response:integer%20%3F;platelet_threshold_at_response:NoNotreportedUnknownYesEnum%20%3F;symptoms:NoNotreportedUnknownYesEnum%20%3F;palpable_nodes:NoNotreportedUnknownYesEnum%20%3F;nodular_splenic:NoNotreportedUnknownYesEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[SubjectResponse])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_response](age_at_response.md)  <sub>0..1</sub>
     * Description: Age in Days of Response Assessment
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
 * [response_category](response_category.md)  <sub>0..1</sub>
     * Description: Response Assessment Category
     * Range: [ResponseCategoryEnum](ResponseCategoryEnum.md)
 * [tx_prior_response](tx_prior_response.md)  <sub>0..1</sub>
     * Description: Treatment Type Prior to Response Assessment
     * Range: [TxPriorResponseEnum](TxPriorResponseEnum.md)
 * [interim_response](interim_response.md)  <sub>0..1</sub>
     * Description: Interim Response
     * Range: [InterimResponseEnum](InterimResponseEnum.md)
 * [response](response.md)  <sub>0..1</sub>
     * Description: A standard way to measure how well a cancer patient responds to treatment. It is based on whether tumors shrink, stay the same, or get bigger. To use Response Evaluation Criteria In Solid Tumors, there must be at least one tumor that can be measured on x-rays, CT scans, or MRI scans. The types of response a patient can have are a complete response (CR), a partial response (PR), progressive disease (PD), and stable disease (SD). Also called RECIST. (Source: NCI Dictionary of Cancer Terms)
     * Range: [ResponseEnum](ResponseEnum.md)
 * [response_method](response_method.md)  <sub>0..1</sub>
     * Description: Response Assessment Method
     * Range: [ResponseMethodEnum](ResponseMethodEnum.md)
 * [response_system](response_system.md)  <sub>0..1</sub>
     * Description: Response Criteria
     * Range: [ResponseSystemEnum](ResponseSystemEnum.md)
 * [response_system_version](response_system_version.md)  <sub>0..1</sub>
     * Description: Response Criteria Version
     * Range: [String](types/String.md)
 * [necrosis](necrosis.md)  <sub>0..1</sub>
     * Description: Refers to the death of living tissues.
     * Range: [NecrosisEnum](NecrosisEnum.md)
 * [necrosis_pct](necrosis_pct.md)  <sub>0..1</sub>
     * Description: Tumor Necrosis (%)
     * Range: [Integer](types/Integer.md)
 * [bm_pct_blasts_at_response](bm_pct_blasts_at_response.md)  <sub>0..1</sub>
     * Description: BM Percent Blasts At Response
     * Range: [Integer](types/Integer.md)
 * [bm_analysis_method_at_response](bm_analysis_method_at_response.md)  <sub>0..1</sub>
     * Description: BM Analysis Modality at Response
     * Range: [BmAnalysisMethodAtResponseEnum](BmAnalysisMethodAtResponseEnum.md)
 * [anc_at_response](anc_at_response.md)  <sub>0..1</sub>
     * Description: ANC at Response (ANC/mm3)
     * Range: [Integer](types/Integer.md)
 * [anc_threshold_at_response](anc_threshold_at_response.md)  <sub>0..1</sub>
     * Description: ANC Threshold at Response
     * Range: [Integer](types/Integer.md)
 * [platelet_count_at_response](platelet_count_at_response.md)  <sub>0..1</sub>
     * Description: Platelet Count At Responset (platelets/mm3)
     * Range: [Integer](types/Integer.md)
 * [platelet_threshold_at_response](platelet_threshold_at_response.md)  <sub>0..1</sub>
     * Description: Exceeded Platelet Threshold >=50,000 (platelets/mm3) At Response
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [symptoms](symptoms.md)  <sub>0..1</sub>
     * Description: A physical or mental problem that a person experiences that may indicate a disease or condition. Symptoms cannot be seen and do not show up on medical tests. Some examples of symptoms are headache, fatigue, nausea, and pain. (Source: NCI Dictionary of Cancer Terms)
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [palpable_nodes](palpable_nodes.md)  <sub>0..1</sub>
     * Description: Palpable Lymph Nodes
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [nodular_splenic](nodular_splenic.md)  <sub>0..1</sub>
     * Description: Nodular Splenic Involvement
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
