
# Class: Subject Response




URI: [https://w3id.org/pcdc/model/SubjectResponse](https://w3id.org/pcdc/model/SubjectResponse)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject]<subjects%201..*-++[SubjectResponse&#124;age_at_response:integer%20%3F;response_category:ResponseCategoryEnum%20%3F;response:ResponseEnum%20%3F;bm_pct_blasts_at_response:decimal%20%3F;bm_analysis_method_at_response:BmAnalysisMethodAtResponseEnum%20%3F;anc_at_response:decimal%20%3F;anc_threshold_at_response:NoNotreportedUnknownYesEnum%20%3F;platelet_count_at_response:decimal%20%3F;platelet_threshold_at_response:NoNotreportedUnknownYesEnum%20%3F;response_method:ResponseMethodEnum%20%3F;response_system:ResponseSystemEnum%20%3F;mri_sequence:MriSequenceEnum%20%3F;neurological_status:NeurologicalStatusEnum%20%3F;response_system_version:string%20%3F;necrosis:NecrosisEnum%20%3F;necrosis_pct:decimal%20%3F;interim_response:InterimResponseEnum%20%3F;response_method_other:string%20%3F;symptoms:NoNotreportedUnknownYesEnum%20%3F;palpable_nodes:NoNotreportedUnknownYesEnum%20%3F;nodular_splenic:NoNotreportedUnknownYesEnum%20%3F;course_timepoint:CourseTimepointEnum%20%3F;measurement_type:MeasurementTypeEnum%20%3F;measurement_numeric:decimal%20%3F;tx_prior_response:TxPriorResponseEnum%20%3F;tumor_site:TumorSiteEnum%20%3F;microscopic_change_type:MicroscopicChangeTypeEnum%20%3F;microscopic_change_status:AbsentNotreportedPresentUnknownEnum%20%3F;microscopic_change_pct:MicroscopicChangePctEnum%20%3F;microscopic_change_pct_numeric:decimal%20%3F;macroscopic_change_type:MacroscopicChangeTypeEnum%20%3F;macroscopic_change_status:AbsentNotreportedPresentUnknownEnum%20%3F;macroscopic_change_pct_numeric:decimal%20%3F;anaplasia_status:AbsentNotreportedPresentUnknownEnum%20%3F;anaplasia_type:AnaplasiaTypeEnum%20%3F;anaplasia_pct_numeric:decimal%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[SubjectResponse],[Thing]^-[SubjectResponse],[Subject])](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject]<subjects%201..*-++[SubjectResponse&#124;age_at_response:integer%20%3F;response_category:ResponseCategoryEnum%20%3F;response:ResponseEnum%20%3F;bm_pct_blasts_at_response:decimal%20%3F;bm_analysis_method_at_response:BmAnalysisMethodAtResponseEnum%20%3F;anc_at_response:decimal%20%3F;anc_threshold_at_response:NoNotreportedUnknownYesEnum%20%3F;platelet_count_at_response:decimal%20%3F;platelet_threshold_at_response:NoNotreportedUnknownYesEnum%20%3F;response_method:ResponseMethodEnum%20%3F;response_system:ResponseSystemEnum%20%3F;mri_sequence:MriSequenceEnum%20%3F;neurological_status:NeurologicalStatusEnum%20%3F;response_system_version:string%20%3F;necrosis:NecrosisEnum%20%3F;necrosis_pct:decimal%20%3F;interim_response:InterimResponseEnum%20%3F;response_method_other:string%20%3F;symptoms:NoNotreportedUnknownYesEnum%20%3F;palpable_nodes:NoNotreportedUnknownYesEnum%20%3F;nodular_splenic:NoNotreportedUnknownYesEnum%20%3F;course_timepoint:CourseTimepointEnum%20%3F;measurement_type:MeasurementTypeEnum%20%3F;measurement_numeric:decimal%20%3F;tx_prior_response:TxPriorResponseEnum%20%3F;tumor_site:TumorSiteEnum%20%3F;microscopic_change_type:MicroscopicChangeTypeEnum%20%3F;microscopic_change_status:AbsentNotreportedPresentUnknownEnum%20%3F;microscopic_change_pct:MicroscopicChangePctEnum%20%3F;microscopic_change_pct_numeric:decimal%20%3F;macroscopic_change_type:MacroscopicChangeTypeEnum%20%3F;macroscopic_change_status:AbsentNotreportedPresentUnknownEnum%20%3F;macroscopic_change_pct_numeric:decimal%20%3F;anaplasia_status:AbsentNotreportedPresentUnknownEnum%20%3F;anaplasia_type:AnaplasiaTypeEnum%20%3F;anaplasia_pct_numeric:decimal%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[SubjectResponse],[Thing]^-[SubjectResponse],[Subject])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_response](age_at_response.md)  <sub>0..1</sub>
     * Description: The age (in days) of subject when the response assessment was made.
     * Range: [Integer](types/Integer.md)
 * [time_periods](time_periods.md)  <sub>0..1</sub>
     * Range: [TimePeriod](TimePeriod.md)
 * [response_category](response_category.md)  <sub>0..1</sub>
     * Description: The category used to assess the response to therapy.
     * Range: [ResponseCategoryEnum](ResponseCategoryEnum.md)
 * [response](response.md)  <sub>0..1</sub>
     * Description: A qualitative or quantitative measurement of the response of a target lesion(s) to the therapy.
     * Range: [ResponseEnum](ResponseEnum.md)
 * [bm_pct_blasts_at_response](bm_pct_blasts_at_response.md)  <sub>0..1</sub>
     * Description: BM Percent Blasts At Response
     * Range: [Decimal](types/Decimal.md)
 * [bm_analysis_method_at_response](bm_analysis_method_at_response.md)  <sub>0..1</sub>
     * Description: BM Analysis Modality at Response
     * Range: [BmAnalysisMethodAtResponseEnum](BmAnalysisMethodAtResponseEnum.md)
 * [anc_at_response](anc_at_response.md)  <sub>0..1</sub>
     * Description: ANC at Response (ANC/mm3)
     * Range: [Decimal](types/Decimal.md)
 * [anc_threshold_at_response](anc_threshold_at_response.md)  <sub>0..1</sub>
     * Description: ANC Threshold at Response
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [platelet_count_at_response](platelet_count_at_response.md)  <sub>0..1</sub>
     * Description: Platelet Count At Responset (platelets/mm3)
     * Range: [Decimal](types/Decimal.md)
 * [platelet_threshold_at_response](platelet_threshold_at_response.md)  <sub>0..1</sub>
     * Description: Exceeded Platelet Threshold >=50,000 (platelets/mm3) At Response
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [response_method](response_method.md)  <sub>0..1</sub>
     * Description: The method used to assess the response to therapy.
     * Range: [ResponseMethodEnum](ResponseMethodEnum.md)
 * [response_system](response_system.md)  <sub>0..1</sub>
     * Description: A standard from which a judgment concerning tumor response to therapy can be established.
     * Range: [ResponseSystemEnum](ResponseSystemEnum.md)
 * [mri_sequence](mri_sequence.md)  <sub>0..1</sub>
     * Range: [MriSequenceEnum](MriSequenceEnum.md)
 * [neurological_status](neurological_status.md)  <sub>0..1</sub>
     * Range: [NeurologicalStatusEnum](NeurologicalStatusEnum.md)
 * [response_system_version](response_system_version.md)  <sub>0..1</sub>
     * Description: The version of the response system.
     * Range: [String](types/String.md)
 * [necrosis](necrosis.md)  <sub>0..1</sub>
     * Description: The quantitative value for the percent of necrosis.
     * Range: [NecrosisEnum](NecrosisEnum.md)
 * [necrosis_pct](necrosis_pct.md)  <sub>0..1</sub>
     * Description: A numeric measurement of the percent of cells undergoing necrosis compared to the number of total cells present in a sample.
     * Range: [Decimal](types/Decimal.md)
 * [interim_response](interim_response.md)  <sub>0..1</sub>
     * Description: An evaluation prior to the completion of therapy that the individual is responding to therapy.
     * Range: [InterimResponseEnum](InterimResponseEnum.md)
 * [response_method_other](response_method_other.md)  <sub>0..1</sub>
     * Description: "Specify the "Other" RESPONSE_METHOD
     * Range: [String](types/String.md)
 * [symptoms](symptoms.md)  <sub>0..1</sub>
     * Description: A physical or mental problem that a person experiences that may indicate a disease or condition. Symptoms cannot be seen and do not show up on medical tests. Some examples of symptoms are headache, fatigue, nausea, and pain. (Source: NCI Dictionary of Cancer Terms)
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [palpable_nodes](palpable_nodes.md)  <sub>0..1</sub>
     * Description: The lymph nodes are felt on palpation.
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [nodular_splenic](nodular_splenic.md)  <sub>0..1</sub>
     * Description: Nodular Splenic Involvement
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [course_timepoint](course_timepoint.md)  <sub>0..1</sub>
     * Description: This variable gives more precise granularity to when an observation occured during the period of the indicated "Course" TIME_PERIOD
     * Range: [CourseTimepointEnum](CourseTimepointEnum.md)
 * [measurement_type](measurement_type.md)  <sub>0..1</sub>
     * Description: The type of vital sign or anthropomorphic measurement being recorded
     * Range: [MeasurementTypeEnum](MeasurementTypeEnum.md)
 * [measurement_numeric](measurement_numeric.md)  <sub>0..1</sub>
     * Description: The vital sign or anthropomorphic measurement being recorded (numeric)
     * Range: [Decimal](types/Decimal.md)
 * [tx_prior_response](tx_prior_response.md)  <sub>0..1</sub>
     * Description: Treatment Type Prior to Response Assessment
     * Range: [TxPriorResponseEnum](TxPriorResponseEnum.md)
 * [tumor_site](tumor_site.md)  <sub>0..1</sub>
     * Range: [TumorSiteEnum](TumorSiteEnum.md)
 * [microscopic_change_type](microscopic_change_type.md)  <sub>0..1</sub>
     * Range: [MicroscopicChangeTypeEnum](MicroscopicChangeTypeEnum.md)
 * [microscopic_change_status](microscopic_change_status.md)  <sub>0..1</sub>
     * Range: [AbsentNotreportedPresentUnknownEnum](AbsentNotreportedPresentUnknownEnum.md)
 * [microscopic_change_pct](microscopic_change_pct.md)  <sub>0..1</sub>
     * Range: [MicroscopicChangePctEnum](MicroscopicChangePctEnum.md)
 * [microscopic_change_pct_numeric](microscopic_change_pct_numeric.md)  <sub>0..1</sub>
     * Range: [Decimal](types/Decimal.md)
 * [macroscopic_change_type](macroscopic_change_type.md)  <sub>0..1</sub>
     * Range: [MacroscopicChangeTypeEnum](MacroscopicChangeTypeEnum.md)
 * [macroscopic_change_status](macroscopic_change_status.md)  <sub>0..1</sub>
     * Range: [AbsentNotreportedPresentUnknownEnum](AbsentNotreportedPresentUnknownEnum.md)
 * [macroscopic_change_pct_numeric](macroscopic_change_pct_numeric.md)  <sub>0..1</sub>
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
