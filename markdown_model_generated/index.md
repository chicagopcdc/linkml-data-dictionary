
# data-dictionary


**metamodel version:** 1.7.0

**version:** 0.0.1





### Classes

 * [Thing](Thing.md)
     * [AdverseEvents](AdverseEvents.md)
     * [BiopsyAndSurgicalProcedures](BiopsyAndSurgicalProcedures.md)
     * [CellularImmunotherapy](CellularImmunotherapy.md)
     * [Cytology](Cytology.md)
     * [DiseaseCharacteristics](DiseaseCharacteristics.md)
     * [FamilyMedicalHistory](FamilyMedicalHistory.md)
     * [FunctionTest](FunctionTest.md)
     * [GeneticAnalysis](GeneticAnalysis.md)
     * [Histology](Histology.md)
     * [Imaging](Imaging.md)
     * [Immunohistochemistry](Immunohistochemistry.md)
     * [LaboratoryTest](LaboratoryTest.md)
     * [LateEffects](LateEffects.md)
     * [LesionCharacteristics](LesionCharacteristics.md)
     * [MedicalHistory](MedicalHistory.md)
     * [Medication](Medication.md)
     * [MinimalResidualDisease](MinimalResidualDisease.md)
     * [OffProtocolTherapyOrStudy](OffProtocolTherapyOrStudy.md)
     * [PatientReportedOutcomesMetadata](PatientReportedOutcomesMetadata.md)
     * [Person](Person.md)
     * [ProtocolTreatmentModifications](ProtocolTreatmentModifications.md)
     * [RadiationTherapy](RadiationTherapy.md)
     * [SecondaryMalignantNeoplasm](SecondaryMalignantNeoplasm.md)
     * [Staging](Staging.md)
     * [StemCellTransplant](StemCellTransplant.md)
     * [Subject](Subject.md)
     * [SubjectCharacteristics](SubjectCharacteristics.md)
     * [SubjectResponse](SubjectResponse.md)
     * [SurvivalCharacteristics](SurvivalCharacteristics.md)
     * [Timing](Timing.md)
     * [TransfusionMedicineProcedure](TransfusionMedicineProcedure.md)
     * [VitalsAndAnthropometrics](VitalsAndAnthropometrics.md)

### Mixins


### Slots

 * [administration_status](administration_status.md) - Medication Administration Status
 * [adverse_event](adverse_event.md) - An unexpected medical problem that happens during treatment with a drug or other therapy. Adverse events may be mild, moderate, or severe, and may be caused by something other than the drug or therapy being given. Also called adverse effect. (Source: NCI Dictionary of Cancer Terms)
 * [ae_attribution](ae_attribution.md) - Adverse Event Attribution to Product or Procedure
 * [ae_code](ae_code.md) - Adverse Event Coded
 * [ae_expected](ae_expected.md) - Adverse Event Expected
 * [ae_grade](ae_grade.md) - Adverse Event Severity Grade
 * [ae_grade_system](ae_grade_system.md) - Adverse Event Grading System
 * [ae_hospitalization](ae_hospitalization.md) - Adverse Event Associated with Hospitalization
 * [ae_icu](ae_icu.md) - Admitted to ICU
 * [ae_immune](ae_immune.md) - Immune Related Adverse Event
 * [ae_infusion](ae_infusion.md) - Infusion Related Adverse Event
 * [ae_intervention](ae_intervention.md) - Adverse Event Intervention
 * [ae_intervention_detail](ae_intervention_detail.md) - Intervention or Medication Detail
 * [ae_medication](ae_medication.md) - Adverse Event Supportive Care Medication
 * [ae_outcome](ae_outcome.md) - Adverse Event Outcome
 * [ae_pathogen](ae_pathogen.md) - Pathogen Causing Infection
 * [ae_pathogen_confirmation](ae_pathogen_confirmation.md) - Pathogen Confirmation Indicator
 * [ae_reported](ae_reported.md) - SAE Reported to Sponsor
 * [ae_system_version](ae_system_version.md) - Adverse Event Grading System Version
 * [ae_tx_mod](ae_tx_mod.md) - Protocol Treatment Modifications
 * [age_at_ae](age_at_ae.md) - Age in Days at Onset Adverse Event
 * [age_at_ae_resolved](age_at_ae_resolved.md) - Age in Days at Resolved Adverse Event
 * [age_at_censor_status](age_at_censor_status.md) - Age (in days) of the subject at the time of the CENSOR_STATUS
 * [age_at_cimt_start](age_at_cimt_start.md) - Age in Days at Start of Cellular Immunotherapy
 * [age_at_course_anc_500](age_at_course_anc_500.md) - The age (in days) of the subject when the subject's neutrophil count exceeded 500 (ANC/mm3)
 * [age_at_course_end](age_at_course_end.md) - The age (in days) of the subject at the time that this ordinally numbered course was completed.
 * [age_at_course_start](age_at_course_start.md) - The age (in days) of the subject at the time that this ordinally numbered course was started.
 * [age_at_cycle_end](age_at_cycle_end.md) - The age (in days) of the subject at the end of the treatment cycle.
 * [age_at_cycle_start](age_at_cycle_start.md) - The age (in days) of the subject at the beginning of the treatment cycle.
 * [age_at_cytology](age_at_cytology.md) - Age in Days at Cytology Test
 * [age_at_disease_phase](age_at_disease_phase.md) - The age (in days) of the subject at the time that this ordinally numbered disease phase was recorded.
 * [age_at_enrollment](age_at_enrollment.md) - Age of subject (in days) when the subject enrolled in the study.
 * [age_at_function_test](age_at_function_test.md) - The age (in days) of the subject at the time of the function test.
 * [age_at_genetic_analysis](age_at_genetic_analysis.md) - The age, in days, of the subject at the time of this analysis.
 * [age_at_hist_assessment](age_at_hist_assessment.md) - Age in Days of Histology Assessment
 * [age_at_ihc](age_at_ihc.md) - Age in Days at Immunohistochemistry Test
 * [age_at_imaging](age_at_imaging.md) - The age (in days) of the subject at the time of imaging.
 * [age_at_lab](age_at_lab.md) - The age (in days) of the subject at the time of the laboratory test.
 * [age_at_le_eval](age_at_le_eval.md) - Age of subject (in days) when the late effect evaluation was performed.
 * [age_at_lesion_assessment](age_at_lesion_assessment.md) - Age in Days at Lesion Assessment
 * [age_at_lkss](age_at_lkss.md) - The age (in days) when the last known survival status of the subject was captured.
 * [age_at_measurement](age_at_measurement.md) - The age (in days) of the subject when the vitals measurement was taken.
 * [age_at_medication_end](age_at_medication_end.md) - Age in Days at End of Total Dose Calculation
 * [age_at_medication_start](age_at_medication_start.md) - Age in Days at Start of Total Dose Calculation
 * [age_at_mod](age_at_mod.md) - Age in Days of Protocol Treatment Modification
 * [age_at_mrd_assessment](age_at_mrd_assessment.md) - Age in Days at Minimal Residual Disease Assessment
 * [age_at_procedure](age_at_procedure.md) - Age in Days at Procedure
 * [age_at_response](age_at_response.md) - Age in Days of Response Assessment
 * [age_at_rt_end](age_at_rt_end.md) - Age in Days at End of Radiation Therapy
 * [age_at_rt_start](age_at_rt_start.md) - Age in Days at Start of Radiation Therapy
 * [age_at_sct](age_at_sct.md) - Age in Days at Stem Cell Transplant
 * [age_at_smn](age_at_smn.md) - Age in Days at Secondary Malignant Neoplasm
 * [age_at_staging](age_at_staging.md) - Age in Days of Staging Assessment
 * [age_at_tmp_start](age_at_tmp_start.md) - Age in Days at Start of Transfusion Medicine Procedure
 * [age_at_txassign](age_at_txassign.md) - The age (in days) of the subject at the time that this treartment was assigned.
 * [age_lost_to_follow_up](age_lost_to_follow_up.md) - The age (in days) when the subject was lost to follow-up
 * [age_off](age_off.md) - The age (in days) when the subject went off of the protocol therapy or study.
 * [all_type](all_type.md)
 * [allelic_frequency](allelic_frequency.md) - The incidence of this mutation in a population (%).
 * [allelic_state](allelic_state.md) - The genetic condition of a zygote, especially with respect to its being a homozygote or a heterozygote.
 * [alt_status](alt_status.md) - Activitation of the Alternative Lengthening of Telomeres (ALT) pathway.
 * [amplification](amplification.md) - Was the copy number gain high enough to be reported as a gene amplification?
 * [amputation_type](amputation_type.md) - The removal by surgery of a limb (arm or leg) or other body part because of injury or disease, such as diabetes or cancer. (Source: NCI Dictionary of Cancer Terms)
 * [anaplasia](anaplasia.md) - Anaplasia
 * [anaplasia_extent](anaplasia_extent.md) - Anaplasia Extent
 * [anc_at_response](anc_at_response.md) - ANC at Response (ANC/mm3)
 * [anc_threshold_at_response](anc_threshold_at_response.md) - ANC Threshold at Response
 * [ann_arbor_mod_ab](ann_arbor_mod_ab.md) - HL Ann Arbor A vs B Staging Designation
 * [ann_arbor_mod_e](ann_arbor_mod_e.md) - HL Ann Arbor E Staging Designation
 * [ann_arbor_mod_s](ann_arbor_mod_s.md) - HL Ann Arbor S Staging Designation
 * [another_study](another_study.md) - Did the subject enroll in another study after they went off of the study indicated by OFF_TYPE?
 * [assisted_conception](assisted_conception.md) - If the subject was conceived through assisted conception, what was the type of assisted conception?
 * [avn_joint](avn_joint.md) - Avascular Necrosis Joint Involvement
 * [avn_joint_laterality](avn_joint_laterality.md) - Avascular Necrosis Joint Laterality
 * [avn_method](avn_method.md) - Avascular Necrosis Method of Evaluation
 * [biopsy_type](biopsy_type.md) - The removal of cells or tissues for examination by a pathologist. The pathologist may study the tissue under a microscope or perform other tests on the cells or tissue. There are many different types of biopsy procedures. The most common types include: (1) incisional biopsy, in which only a sample of tissue is removed; (2) excisional biopsy, in which an entire lump or suspicious area is removed; and (3) needle biopsy, in which a sample of tissue or fluid is removed with a needle. When a wide needle is used, the procedure is called a core biopsy. When a thin needle is used, the procedure is called a fine-needle aspiration biopsy. (Source: NCI Dictionary of Cancer Terms)
 * [bm_analysis_method_at_response](bm_analysis_method_at_response.md) - BM Analysis Modality at Response
 * [bm_morphology](bm_morphology.md) - The morphology of bone marrow blasts 
 * [bm_pct_blasts_at_response](bm_pct_blasts_at_response.md) - BM Percent Blasts At Response
 * [boost](boost.md) - Boost Given
 * [boost_dose](boost_dose.md) - Boost Dose
 * [bulk_disease](bulk_disease.md)
 * [bulk_med_mass](bulk_med_mass.md) - Bulky Mediastinal Mass
 * [bulk_nodal_aggregate](bulk_nodal_aggregate.md)
 * [cartilage_percent](cartilage_percent.md) - The percentage of cartilage.
 * [cause_of_death](cause_of_death.md) - The circumstance or condition that results in the death of a living being.
 * [cause_of_death_detail](cause_of_death_detail.md) - More granular causes for the death of the subject than what is permissible in CAUSE_OF_DEATH.
 * [cause_of_death_detail_other](cause_of_death_detail_other.md) - Specify the "Other" CAUSE_OF_DEATH_DETAIL
 * [cause_of_death_ranking](cause_of_death_ranking.md) - Assigning a weighted relevance to the cause of death.
 * [cells_in_metaphase](cells_in_metaphase.md) - The number of cells in the sample that were arrested in the metaphase stage of the cell cycle and used for the karyotype through which this abnormality was detected.
 * [chromosomal_consequence](chromosomal_consequence.md)
 * [chromosome](chromosome.md) - One of the bodies in the cell nucleus that is the bearer of genes, has the form of a delicate chromatin filament during interphase, contracts to form a compact cylinder segmented into two arms by the centromere during metaphase and anaphase stages of cell division, and is capable of reproducing its physical and chemical structure through successive cell divisions.
 * [cimt_type](cimt_type.md) - Cellular Immunotherapy Type
 * [clingen_id](clingen_id.md) - This ID will allow users to find the most current clinical significance classification for this instance of variation
 * [cns_disease_status](cns_disease_status.md) - CNS Involvement Status
 * [common_name](common_name.md) - The non-standardized name of the mutation represented by this observation.
 * [computed_volume_numeric](computed_volume_numeric.md) - Computed Volume (mL)
 * [condition](condition.md) - Relevant condition that may or may not (see CONDITION_STATUS) be in part of the subject's medical history. 
 * [condition_other](condition_other.md) - Specify the "Other" CONDITION
 * [condition_status](condition_status.md) - Was this condition observed in the subject?
 * [condition_type](condition_type.md) - The type of relevant condition from the subject's medical history.
 * [consortium](consortium.md) - The disease consortium to which the data contributor belongs.
 * [copy_number](copy_number.md) - The number of gene copies resulting from this mutation.
 * [copy_number_variation](copy_number_variation.md) - If there was a change in the number of gene copies, this variable specifies the type of change.
 * [course](course.md) - The protocol treatment "course" during which relevant observations were recorded. This variable is used across domains to frame the timing of these longitudinal observations and reduce the number of redundant variables needed to report similar concepts (see "Disease Phase Timing and Course Table" in the documentation for additional guidance).
 * [course_number](course_number.md) - This variable indicates the ordinal numbering of the Course variable within its various subgroups (e.g., Induction 1, Induction 2, Induction 3, etc.). The observations across domains can therefore be organized longitudinally without the need for specific dates.
 * [cycle_number](cycle_number.md) - This variable indicates the ordinal numbering of cycles of treatment therapy administered to the subject.
 * [cytodifferentiation](cytodifferentiation.md) - Cytodifferentiation Score
 * [cytology_spec_type](cytology_spec_type.md) - The study of cells using a microscope (Source: NCI Dictionary of Cancer Terms)
 * [data_contributor_id](data_contributor_id.md) - An identifier assigned to a data contributor.
 * [data_source](data_source.md) - Is this data coming from a cancer registry or via a clinical study?
 * [deauville_score](deauville_score.md) - A 5 point scale devised to assess the response to treatment of Hodgkin and Aggressive Non-Hodgkin Lymphoma.
 * [depth](depth.md) - The extent downward or inward; the perpendicular measurement from the surface downward to determine deepness.
 * [detection_method](detection_method.md) - The method used to detect the extent of the disease involvement.
 * [diam_type](diam_type.md) - Dimension 2 Direction
 * [disease_phase](disease_phase.md) - The phase of the cancer treatment process during which relevant observations were recorded. This variable is used across domains to frame the timing of these longitudinal observations and reduce the number of redundant variables needed to report similar concepts (see "Disease Phase Timing and Course Table" in the documentation for additional guidance).
 * [disease_phase_number](disease_phase_number.md) - This variable indicates the ordinal numbering of the Disease Phase variable within its various subgroups (e.g., Relapse 1, Relapse 2, Relapse 3, etc.). The observations across domains can therefore be organized longitudinally without the need for specific dates.
 * [disease_site](disease_site.md) - Disease Involvement Site
 * [distance_margin_tumor](distance_margin_tumor.md) - Closest Distance from Margin to Resected Tumor
 * [dna_index](dna_index.md)
 * [dna_index_numeric](dna_index_numeric.md) - The ratio of the DNA content or chromosome number in a tumor sample compared to that in a normal sample.
 * [e_extension_site](e_extension_site.md) - The anatomic location outside of the lymph nodes into which a disease lesion has directly spread.
 * [efs_censor_status](efs_censor_status.md) - The event free survival censor status
 * [eligible_age_lower](eligible_age_lower.md) - Lower Age Range of Child Rater
 * [eligible_age_upper](eligible_age_upper.md) - Upper Age Range of Child Rater
 * [energy_type](energy_type.md) - Energy Type
 * [enrolled_status](enrolled_status.md) - This variable indicates if the subject was enrolled in the study, or if the subject was not enrolled in the study but received treatment per the study's protocol.
 * [estimated_volume_numeric](estimated_volume_numeric.md) - Estimated Volume (mL)
 * [ethnicity](ethnicity.md) - The social and cultural characteristics, backgrounds, or experiences shared by a group of people. These include language, religion, beliefs, values, and behaviors that are often handed down from one generation to the next. Some conditions or diseases, such as cancer, may be more common in certain ethnic groups than in others. (Source: NCI Dictionary of Cancer Terms)
 * [expression_consequence](expression_consequence.md)
 * [extension_site](extension_site.md)
 * [fab_type](fab_type.md) - French-American-British Classification
 * [fever](fever.md) - An increase in body temperature above normal (98.6 degrees F), usually caused by disease. (Source: NCI Dictionary of Cancer Terms)
 * [flow_cytometry_type](flow_cytometry_type.md)
 * [function_category](function_category.md) - The category of the function test.
 * [function_result](function_result.md) - The string/text result of the function test.
 * [function_result_numeric](function_result_numeric.md) - The numeric value of the result of the function test.
 * [function_result_unit](function_result_unit.md) - The unit used for the numeric result of the function test used on the subject.
 * [function_test](function_test.md) - The function test used on the subject.
 * [gene](gene.md) - A gene targeted for mutation analysis, identified in HUGO Gene Nomenclature Committee (HGNC) notation.
 * [gene2](gene2.md) - This should be used for mutations that span two gene locations (fusion, translocation, inversion, etc.). The gene name should be identified in HUGO Gene Nomenclature Committee (HGNC) notation.
 * [genomic_region](genomic_region.md)
 * [genomic_source_class](genomic_source_class.md) - The genomic class of the specimen being analyzed, for example, germline for inherited genome and somatic for cancer genome.
 * [gpoh_score](gpoh_score.md)
 * [gts](gts.md)
 * [gts_treatment](gts_treatment.md) - Growing Teratoma Syndrome Treatment
 * [gvhd_acuity](gvhd_acuity.md) - Graft Versus Host Disease Acuity
 * [gvhd_organ](gvhd_organ.md) - Graft Versus Host Disease Organ
 * [hgvs_coding](hgvs_coding.md) - If this mutation is described at the sequence/chromosome level, this is its representation in HGVS nomenclature (cHGVS).
 * [hgvs_protein](hgvs_protein.md) - If this mutation is described at the translational product level, this is its representation in HGVS nomenclature (pHGVS)
 * [hist_assessment_review](hist_assessment_review.md) - Institutional or Central Histological Assessment
 * [hist_icd_o_morph_code](hist_icd_o_morph_code.md) - Histology ICD-O Morphology Code
 * [histology](histology.md) - The study of tissues and cells under a microscope (Source: NCI Dictionary of Cancer Terms)
 * [histology_grade](histology_grade.md)
 * [histology_inpc](histology_inpc.md) - Revised INPC Prognostic Group (2003)
 * [histology_result](histology_result.md)
 * [histology_result_numeric](histology_result_numeric.md)
 * [histology_result_unit](histology_result_unit.md) - Numeric Histology Result Unit
 * [hla_a_result](hla_a_result.md) - HLA-A Match Finding
 * [hla_b_result](hla_b_result.md) - HLA-B Match Finding
 * [hla_c_result](hla_c_result.md) - HLA-C Match Finding
 * [hla_dq_result](hla_dq_result.md) - HLA-DQ Match Finding
 * [hla_drb1_result](hla_drb1_result.md) - HLA-DRB1 Match Finding
 * [hla_match](hla_match.md) - HLA Match Status
 * [honest_broker_subject_id](honest_broker_subject_id.md) - The identifier assigned to the subject by the honest broker--an individual, organization or system acting for, or on behalf of, a covered entity to collect and provide health information to research investigators in such a manner whereby it would not be reasonably possible for the investigators or others to identify the corresponding patients-subjects directly or indirectly. The honest broker cannot be one of the investigators. The information provided to the investigators by the honest broker may incorporate linkage codes to permit information collation and/or subsequent inquiries (i.e., a "re-identification code"), however the information linking this re-identification code to the patient's identity must be retained by the honest broker and subsequent inquiries are conducted through the honest broker. (Source: NCI Thersaurus)
 * [icd_o_morph](icd_o_morph.md) - Morphology ICD-O Code
 * [icd_o_top](icd_o_top.md) - Topography ICD-O Code
 * [ihc_result](ihc_result.md) - The result from the immunohistochemical test.
 * [ihc_result_numeric](ihc_result_numeric.md) - The numerical identifier of an immunohistochemistry specimen assessment result.
 * [ihc_result_unit](ihc_result_unit.md) - The unit of an immunohistochemistry test result.
 * [ihc_spec_type](ihc_spec_type.md) - The type of a material sample taken from a biological entity for immunohistochemistry testing.
 * [ihc_test](ihc_test.md) - A laboratory method that uses antibodies to check for certain antigens (markers) in a sample of tissue. The antibodies are usually linked to an enzyme or a fluorescent dye. After the antibodies bind to the antigen in the tissue sample, the enzyme or dye is activated, and the antigen can then be seen under a microscope. Immunohistochemistry is used to help diagnose diseases, such as cancer. It may also be used to help tell the difference between different types of cancer (Source: NCI Dictionary of Cancer Terms)
 * [imaging_method](imaging_method.md) - The testing method/technique used to generate the observed results.
 * [imaging_result](imaging_result.md) - The result of an evaluation technique using a visual display of structural or functional patterns of organs or tissues that is performed to determine the presence, absence, or degree of a condition.
 * [independent_aberations](independent_aberations.md) - The total number of aberrations / mutations / abnormalities detected on the karyotype through which this abnormality was detected.
 * [infection_classification](infection_classification.md) - Infection Site Classification
 * [inheritance_pattern](inheritance_pattern.md)
 * [initial_treatment_category](initial_treatment_category.md) - The category of initial treatment that the patient receive for their disease.
 * [interim_response](interim_response.md) - Interim Response
 * [invasiveness](invasiveness.md) - Tumor Invasiveness
 * [ipsilateral_nodules](ipsilateral_nodules.md) - A metastatic tumor nodule located in the same side of the organ in which the primary tumor occurred.
 * [irs_group](irs_group.md) - IRS Surgical-Pathologic Grouping System
 * [iscn](iscn.md) - If this mutation is described by the structure of the resulting chromosomes, this is its representation in ISCN nomenclature.
 * [joint_involvement](joint_involvement.md) - A finding indicating the spread of cancer to a joint.
 * [karyotype_status](karyotype_status.md) - Karyotype Status
 * [lab_category](lab_category.md) - The category of laboratory test performed on the subject.
 * [lab_method](lab_method.md) - A systematic course of action that is performed in order to complete a laboratory test.
 * [lab_result](lab_result.md) - The string/text result of the laboratory test.
 * [lab_result_categorical](lab_result_categorical.md)
 * [lab_result_numeric](lab_result_numeric.md) - The numeric result of the laboratory test.
 * [lab_result_unit](lab_result_unit.md) - The units used for the numeric result of the laboratory test,
 * [lab_seq_method](lab_seq_method.md) - The number of molecules of a particular type on or in a cell or part of a cell. Usually applied to specific genes or to plasmids within a bacterium.
 * [lab_test](lab_test.md) - A medical procedure that involves testing a sample of blood, urine, or other substance from the body. Laboratory tests can help determine a diagnosis, plan treatment, check to see if treatment is working, or monitor the disease over time Source: NCI Dictionary of Cancer Terms)
 * [lab_test_other](lab_test_other.md) - Specify the "Other" LAB_TEST
 * [laterality](laterality.md)
 * [le](le.md) - Any symptom or condition which is a result of a medical intervention but arises months or years after it.
 * [le_ctcae_version](le_ctcae_version.md) - The version of the Common Terminology Criteria for Adverse Events (CTCAE) Terminology.
 * [le_detail](le_detail.md) - An in-depth explanation of a health problem that occurs months or years after a disease is diagnosed or after treatment has ended.
 * [le_severity_grade](le_severity_grade.md) - A severity grade assigned to the late effects.
 * [le_sub_detail](le_sub_detail.md) - An added in-depth or explanation of a health problem that occurs months or years after a disease is diagnosed or after treatment has ended.
 * [lesion_assessment_review](lesion_assessment_review.md) - Institutional or Central Lesion Review
 * [lesion_bulky](lesion_bulky.md) - Bulky Lesion
 * [lesion_classification](lesion_classification.md) - The classification of a lesion of interest.
 * [lesion_pct_change](lesion_pct_change.md) - 2-Dimensional Percent Change of Lesion
 * [lesion_presentation](lesion_presentation.md)
 * [lesion_response](lesion_response.md)
 * [lesion_site](lesion_site.md) - Specifies the anatomic site of a localized pathological or traumatic structural change, damage, deformity, or discontinuity of tissue, organ, or body part.
 * [lesion_site_other](lesion_site_other.md)
 * [lesion_size](lesion_size.md)
 * [lesion_state](lesion_state.md) - A condition or state of a tumor at a particular time and a particular tumor site.
 * [lesion_volume](lesion_volume.md)
 * [lkss](lkss.md) - The last known survival status of the subject.
 * [lkss_with_disease](lkss_with_disease.md) - Did the subject still have measurable/evaluable disease at the LKSS?
 * [localization_technique](localization_technique.md) - The process of determining or marking the location or site of a lesion or disease. May also refer to the process of keeping a lesion or disease in a specific location or site. (Source: NCI Dictionary of Cancer Terms)
 * [longest_diam_dim1](longest_diam_dim1.md) - Longest Diameter of Tumor Dimension 1 (cm)
 * [longest_diam_dim2](longest_diam_dim2.md) - Longest Diameter of Tumor Dimension 2 (cm)
 * [longest_diam_dim3](longest_diam_dim3.md) - Longest Diameter of Tumor Dimension 3 (cm)
 * [malignant_cells](malignant_cells.md) - A term used to describe cancer. Malignant cells grow in an uncontrolled way and can invade nearby tissues and spread to other parts of the body through the blood and lymph system (Source: NCI Dictionary of Cancer Terms)
 * [margins](margins.md) - The edge or border of the tissue removed in cancer surgery. The margin is described as negative or clean when the pathologist finds no cancer cells at the edge of the tissue, suggesting that all of the cancer has been removed. The margin is described as positive or involved when the pathologist finds cancer cells at the edge of the tissue, suggesting that all of the cancer has not been removed. (Source: NCI Dictionary of Cancer Terms)
 * [mature_glial_implants](mature_glial_implants.md) - Mature Glial Implants Present
 * [measurement](measurement.md) - The vital sign or anthropomorphic measurement being recorded (non-numeric)
 * [measurement_numeric](measurement_numeric.md) - The vital sign or anthropomorphic measurement being recorded (numeric)
 * [measurement_type](measurement_type.md) - The type of vital sign or anthropomorphic measurement being recorded
 * [measurement_unit](measurement_unit.md) - The units used for the vital sign or anthropomorphic measurement being recorded (numeric)
 * [med_ratio](med_ratio.md) - Mediastinal Ratio
 * [medication](medication.md) - A dosage form that contains one or more active and/or inactive ingredients. Medications come in many dosage forms, including tablets, capsules, liquids, creams, and patches. They can also be given in different ways, such as by mouth, by infusion into a vein, or by drops that are put into the ear or eye. The form with the active ingredient is used to prevent, diagnose, treat, or relieve symptoms of a disease or abnormal condition. A medication that does not contain an active ingredient and is used in research studies is called a placebo. Also called drug product. (Source: NCI Dictionary of Cancer Terms)
 * [met_lung_mgmt](met_lung_mgmt.md) - Metastatic Lung Disease Surgical Management
 * [met_non_lung_mgmt](met_non_lung_mgmt.md) - Non-lung Metastatic Site Surgical Management
 * [method](method.md) - The testing method/technique used to generate the observed results.
 * [mibg_avidity](mibg_avidity.md)
 * [mitotic_rate](mitotic_rate.md) - Mitoses Count
 * [mki](mki.md) - Mitosis Karyorrhexis Index as revised by the International Neuroblastoma Pathology Classification (INPC)
 * [mlds](mlds.md) - Myeloid Leukemia Associated with Down Syndrome
 * [mod_rationale](mod_rationale.md) - Treatment Modification Rationale
 * [mod_reason](mod_reason.md) - Treatment Modification Reason
 * [mod_type](mod_type.md) - Modification Type
 * [morph_sno](morph_sno.md) - Morphology SNOMED Code
 * [morph_txt](morph_txt.md) - Morphology Text
 * [mosaicism](mosaicism.md) - Does this subject have two or more genetically different sets of cells in their body?
 * [mosaicism_percent](mosaicism_percent.md) - The numeric level of mosaicism in this subject.
 * [mpal](mpal.md) - Mixed Phenotype Acute Leukemia
 * [mrd_method](mrd_method.md) - A term used to describe a very small number of cancer cells that remain in the body during or after treatment. Minimal residual disease can be found only by highly sensitive laboratory methods that are able to find one cancer cell among one million normal cells. Checking to see if there is minimal residual disease may help plan treatment, find out how well treatment is working or if cancer has come back, or make a prognosis. Minimal residual disease testing is used mostly for blood cancers such as lymphoma and leukemia. Also called MRD. (Source: NCI Dictionary of Cancer Terms)
 * [mrd_molecular_markers](mrd_molecular_markers.md) - Minimal residual disease molecular markers
 * [mrd_result](mrd_result.md) - Minimal Residual Disease Result
 * [mrd_result_numeric](mrd_result_numeric.md) - Numeric Minimal Residual Disease Result
 * [mrd_result_unit](mrd_result_unit.md) - Numeric Minimal Residual Disease Result Unit
 * [mrd_sample_source](mrd_sample_source.md) - Minimal Residual Disease Sample Source
 * [mrd_sensitivty](mrd_sensitivty.md) - Minimal Residual Disease Method Sensitivity
 * [mutation_type](mutation_type.md) - The type of mutation detected by this genetic analysis.
 * [mutation_type_other](mutation_type_other.md) - Specify the "Other" MUTATION_TYPE
 * [myeloid_sarcoma](myeloid_sarcoma.md) - A rare type of cancer that is made up of myeloblasts (a type of immature white blood cell) and forms outside the bone marrow and blood. The tumor cells may look green when viewed under a microscope. Myeloid sarcomas can occur anywhere in the body. They most commonly occur in people with acute myeloid leukemia or a myeloproliferative disorder. Also called chloroma, extramedullary myeloid tumor, and granulocytic sarcoma. (Source: NCI Dictionary of Cancer Terms)
 * [myeloid_sarcoma_site](myeloid_sarcoma_site.md)
 * [necrosis](necrosis.md) - Refers to the death of living tissues.
 * [necrosis_pct](necrosis_pct.md) - Tumor Necrosis (%)
 * [night_sweats](night_sweats.md) - Episodes of excessive sweating that occur during sleep. Night sweats can be severe and soak a person’s bedclothes and bed sheets, which may cause the person to wake up. Night sweats are a common symptom of menopause. They may also be caused by illness or medical conditions, such as infection, cancer, low blood sugar, hormone disorders, and neurologic conditions. They may also be a side effect of certain medicines, cancer treatment, too much caffeine or alcohol, or tobacco or drug use. (Source: NCI Dictionary of Cancer Terms)
 * [nodal_determination](nodal_determination.md) - Determination of Regional Lymph Node Involvement
 * [nodal_determination_source](nodal_determination_source.md)
 * [nodal_involvement](nodal_involvement.md) - Regional Lymph Node Involvement
 * [nodal_site](nodal_site.md)
 * [nodular_splenic](nodular_splenic.md) - Nodular Splenic Involvement
 * [non_protocol_reason](non_protocol_reason.md) - If a non-protocol medication, why was this medication administered?
 * [non_protocol_timing](non_protocol_timing.md) - If a non-protocol medication, when was this medication administered?
 * [normalization_basis](normalization_basis.md) - Normalization Basis
 * [num_fraction](num_fraction.md) - Number of Fractions
 * [number_doses](number_doses.md) - Number of times a dose of the medication was administered between the AGE_AT_MEDICATION_START and AGE_AT_MEDICATION_END values.
 * [number_hla](number_hla.md) - Number of Evaluated HLAs
 * [number_matches](number_matches.md) - Number of Matched HLAs
 * [number_nodes](number_nodes.md) - Involved Lymph Nodes Single or Multiple
 * [number_nodes_numeric](number_nodes_numeric.md) - Number of Involved Lymph Nodes
 * [off_type](off_type.md) - Did the subject go off of a study or off of a certain protocol therapy?
 * [original_agent](original_agent.md) - Original Agent
 * [orthopedic_procedure](orthopedic_procedure.md) - Avascular Necrosis Orthopedic Procedures
 * [palpable_nodes](palpable_nodes.md) - Palpable Lymph Nodes
 * [parameningeal_extension](parameningeal_extension.md)
 * [parental_status](parental_status.md)
 * [pelvic_involvement](pelvic_involvement.md) - Pelvic Involvement
 * [performance_score](performance_score.md) - A standard way of measuring the ability of cancer patients to perform ordinary tasks. Scores range from 0 to 100. A higher score means the patient is better able to carry out daily activities. May be used to determine a patient's prognosis, to measure changes in a patient’s ability to function, or to decide if a patient could be included in a clinical trial. (Source: NCI Dictionary of Cancer Terms)
 * [performance_score_system](performance_score_system.md)
 * [pericardial_effusion](pericardial_effusion.md) - Fluid collection within the pericardial sac, usually due to inflammation.
 * [peritoneal_cytology](peritoneal_cytology.md) - An examination of cells obtained from a sample of peritoneal fluid.
 * [peritoneal_effusion](peritoneal_effusion.md) - The abnormal collection of fluid in the peritoneal cavity resulting in ascites.
 * [platelet_count_at_response](platelet_count_at_response.md) - Platelet Count At Responset (platelets/mm3)
 * [platelet_threshold_at_response](platelet_threshold_at_response.md) - Exceeded Platelet Threshold >=50,000 (platelets/mm3) At Response
 * [pleural_cytology](pleural_cytology.md) - An examination of cells obtained from a sample of pleural fluid.
 * [pleural_effusion](pleural_effusion.md) - Increased amounts of fluid within the pleural cavity. Symptoms include shortness of breath, cough, and chest pain. It is usually caused by lung infections, congestive heart failure, pleural and lung tumors, connective tissue disorders, and trauma.
 * [pmid_ref](pmid_ref.md) - A globally unique identifier for a biomedical article, as assigned by PubMed.
 * [prior_cancer](prior_cancer.md) - Does the subject have a relative who has a medical history that includes cancer?
 * [prior_cancer_type](prior_cancer_type.md) - The type of prior cancer from the medical history of the relative of the subject.
 * [prior_steroids_month](prior_steroids_month.md) - Received Steroids within One Month Prior to Diagnosis
 * [prior_steroids_week](prior_steroids_week.md) - Received Steroids within One Week Prior to Diagnosis
 * [pro_measurement_type](pro_measurement_type.md) - PRO Measurement Type
 * [pro_measures](pro_measures.md) - PRO Measures
 * [procedure_extent](procedure_extent.md) - Procedure Extent
 * [procedure_laterality](procedure_laterality.md) - Procedure Laterality
 * [procedure_purpose](procedure_purpose.md) - Procedure Purpose
 * [procedure_site](procedure_site.md) - Procedure Site
 * [procedure_type](procedure_type.md) - Procedure Type
 * [protocol_cimt](protocol_cimt.md) - Was this cellular immunotherapy part of the treatment protocol?
 * [protocol_medication](protocol_medication.md) - Was this medication part of the treatment protocol?
 * [protocol_procedure](protocol_procedure.md) - Was this procedure part of the treatment protocol?
 * [protocol_radiation_therapy](protocol_radiation_therapy.md) - Was this radiation therapy administration part of the treatment protocol?
 * [protocol_sct](protocol_sct.md) - Was this stem cell transplant part of the treatment protocol?
 * [protocol_transfusion](protocol_transfusion.md) - Was this transfusion part of the treatment protocol?
 * [qpet_score](qpet_score.md) - A methodology that provides semi-automatic quantification for interim FDG-PET response in lymphoma. It extends the ordinal Deauville score to a continuous scale.
 * [race](race.md) - A group of people who share physical characteristics, such as skin color and facial features. They may also share similar social or cultural identities and ancestral backgrounds. There are many racial groups, and a person may belong to or identify with more than one group. Some diseases, such as cancer, may be more common in certain races than in others. (Source: NCI Dictionary of Cancer Terms)
 * [race_other](race_other.md) - Specify the "Other" RACE
 * [randomized_status](randomized_status.md) - The allocation of individuals to groups by chance, especially in order to control the variables in an experiment.
 * [raters](raters.md) - Raters Allowed to Report
 * [reason_off](reason_off.md) - What was the reason that the subject went off of a study or off of a certain protocol therapy?
 * [reason_off_other](reason_off_other.md) - Specify the "Other" REASON_OFF
 * [reconstruction_type](reconstruction_type.md) - Surgical Reconstruction Type
 * [relation](relation.md) - What kind of relation is this relative who has had a relevant medical condition?
 * [resection_type](resection_type.md) - Surgery to remove tissue or part or all of an organ. (Source: NCI Dictionary of Cancer Terms)
 * [response](response.md) - A standard way to measure how well a cancer patient responds to treatment. It is based on whether tumors shrink, stay the same, or get bigger. To use Response Evaluation Criteria In Solid Tumors, there must be at least one tumor that can be measured on x-rays, CT scans, or MRI scans. The types of response a patient can have are a complete response (CR), a partial response (PR), progressive disease (PD), and stable disease (SD). Also called RECIST. (Source: NCI Dictionary of Cancer Terms)
 * [response_category](response_category.md) - Response Assessment Category
 * [response_method](response_method.md) - Response Assessment Method
 * [response_system](response_system.md) - Response Criteria
 * [response_system_version](response_system_version.md) - Response Criteria Version
 * [risk_group](risk_group.md)
 * [risk_group_system](risk_group_system.md) - MaGIC Risk Group
 * [route](route.md) - Route of Administration
 * [route_detail](route_detail.md) - Route of Administration Detail
 * [rt_dose](rt_dose.md) - Total Radiation Dose
 * [rt_site](rt_site.md) - Radiation Therapy Site
 * [rt_unit](rt_unit.md) - Radiation Dose Unit
 * [sct_cd34_coll](sct_cd34_coll.md) - Number of Stem Cells Collected in SCT Apheresis (10^6 CD34+/kg)
 * [sct_cd34_transplant](sct_cd34_transplant.md) - Number of Stem Cells Given in SCT Apheresis (10^6 CD34+/kg)
 * [sct_conditioning_type](sct_conditioning_type.md) - Type of Stem Cell Transplant Conditioning Prior to Transplant
 * [sct_cycles](sct_cycles.md) - Number of Stem Cell Transplant Cycles
 * [sct_donor_relationship](sct_donor_relationship.md) - Stem Cell Transplant Donor Relationship
 * [sct_source](sct_source.md) - Stem Cell Transplant Source
 * [sct_tbi](sct_tbi.md) - Total Body Irradiation Prior to Stem Cell Transplant
 * [sct_type](sct_type.md) - A procedure in which a patient receives healthy stem cells (blood-forming cells) to replace their own stem cells that have been destroyed by treatment with radiation or high doses of chemotherapy. The healthy stem cells may come from the blood or bone marrow of the patient or from a related or unrelated donor. A stem cell transplant may be autologous (using a patient’s own stem cells that were collected and saved before treatment), allogeneic (using stem cells from a related or unrelated donor), syngeneic (using stem cells donated by an identical twin), or cord blood (using umbilical cord blood donated after a baby is born). (Source: NCI Dictionary of Cancer Terms)
 * [secondary_aml](secondary_aml.md) - Secondary Acute Myeloid Leukemia
 * [sex](sex.md) - The biological sex of the subject.
 * [site_within_bone](site_within_bone.md) - The anatomic site within the bone.
 * [skip_lesion](skip_lesion.md) - A benign or malignant pathologic process which is patchy and skips areas which are normal (uninvolved by the pathologic process).
 * [smn_field](smn_field.md) - Relation of SMN to Prior Radiation Therapy Field
 * [smn_icd_o_morph](smn_icd_o_morph.md) - SMN Morphology ICD-O Code
 * [smn_icd_o_top](smn_icd_o_top.md) - SMN Topography ICD-O Code
 * [smn_morph_sno](smn_morph_sno.md) - SMN Morphology SNOMED Code
 * [smn_site](smn_site.md) - SMN Site
 * [smn_status](smn_status.md) - Secondary Malignancy Present
 * [smn_top_sno](smn_top_sno.md) - SMN Topography SNOMED Code
 * [smn_top_txt](smn_top_txt.md) - SMN Topography Text
 * [smn_type](smn_type.md) - SMN Type
 * [snm_morph_txt](snm_morph_txt.md) - SMN Morphology Text
 * [somatic_malignancy_type](somatic_malignancy_type.md)
 * [specimen](specimen.md) - The biological specimen of the subject used for the laboratory test. 
 * [specimen_other](specimen_other.md) - Specify the "Other" SPECIMEN
 * [stage](stage.md) - The extent of a cancer in the body. Staging is usually based on the size of the tumor, whether lymph nodes contain cancer, and whether the cancer has spread from the original site to other parts of the body (Source: NCI Dictionary of Cancer Terms)
 * [stage_system](stage_system.md) - A systematic method for clinicopathologic evaluation of tumors.
 * [status](status.md) - Is this mutation/abnormality present in this subject?
 * [study_id](study_id.md) - A sequence of characters used to identify, name, or characterize the study.
 * [study_phase](study_phase.md) - The phase of the clinical trial that the subject was enrolled in for the collection of this data.
 * [study_type](study_type.md) - The nature of the investigation or the investigational use for which clinical study is being done.
 * [sub_agent](sub_agent.md) - Substitution Agent
 * [➞persons](subject__persons.md)
 * [subjects](subjects.md)
 * [submitter_id](submitter_id.md) - PCDC internal event ID
 * [surgery](surgery.md) - A procedure to remove or repair a part of the body or to find out whether disease is present. Also called operation. (Source: NCI Dictionary of Cancer Terms)
 * [surgery_type_limb](surgery_type_limb.md) - Limb Surgery Type
 * [surgery_type_limb_salvage](surgery_type_limb_salvage.md) - Limb Salvage Surgery Type
 * [symptoms](symptoms.md) - A physical or mental problem that a person experiences that may indicate a disease or condition. Symptoms cannot be seen and do not show up on medical tests. Some examples of symptoms are headache, fatigue, nausea, and pain. (Source: NCI Dictionary of Cancer Terms)
 * [tamds](tamds.md) - AML Diagnosed Within Four Years of Transient Abnormal Myelopoiesis Associated with Down Syndrome Diagnosis
 * [threshold_high](threshold_high.md) - The maximum level that must be exceeded for a certain reaction to occur or be manifested.
 * [threshold_low](threshold_low.md) - The minimum level that must be attained for a certain reaction to occur or be manifested.
 * [time_point](time_point.md) - PRO Measures Assessment Time Point
 * [timings](timings.md)
 * [tissue_type](tissue_type.md) - A piece of tissue removed from an organism for examination, analysis, or propagation.
 * [tmp_number_units](tmp_number_units.md) - Number of Units of Product Transfused
 * [tmp_product](tmp_product.md) - Transfusion Medicine Procedure Product
 * [tmp_product_type](tmp_product_type.md) - Transfusion Medicine Procedure Product Type
 * [tmp_type](tmp_type.md) - Transfusion Medicine Procedure Type
 * [tnm_finding](tnm_finding.md)
 * [top_sno](top_sno.md) - Topography SNOMED Code
 * [top_txt](top_txt.md) - Topography Text
 * [total_chromosomes](total_chromosomes.md) - The number of chromosomes detected on the karyotype through which this abnormality was detected.
 * [total_dose_administered](total_dose_administered.md) - Total amount of medication administered between the AGE_AT_MEDICATION_START and AGE_AT_MEDICATION values. Assuming all doses administered are the same amount of medication, this value should be equal to the amount of medication given at each dose multiplied by the number of doses.
 * [total_dose_intended](total_dose_intended.md) - This is the total amount of medication that was intended to be administered either by trial protocol, by prescription, or other indicator at the time point of AGE_AT_MEDICATION_START. Often, this will be equal to TOTAL_DOSE_ADMINISTERED. If TOTAL_DOSE_ADMINISTERED and TOTAL_DOSE_INTENDED are different, this indicates a deviation from the protocol or plan and may be due to a variety of factors including patient intolerance, patient non-adherence, etc.
 * [total_dose_units](total_dose_units.md) - Total Dose Units
 * [toxicity_detail](toxicity_detail.md) - Toxicity Detail
 * [toxicity_immune](toxicity_immune.md) - Immune Related Toxicity
 * [toxicity_infusion](toxicity_infusion.md) - Infusion Related Toxicity
 * [transposition_organ](transposition_organ.md) - Surgical Transposition of Organs
 * [traumatic_tap](traumatic_tap.md) - Was the lumbar puncture artifically contaminated by peripheral blood?
 * [treatment_arm](treatment_arm.md) - A specific treatment plan within a clinical trial that describes the activities a subject will be involved in as he or she progresses through the study.
 * [trm_type](trm_type.md) - If the mortality is treatment related, what type of treatment was involved?
 * [trm_type_other](trm_type_other.md) - Specify the "Other" TRM_TYPE
 * [tumor_classification](tumor_classification.md) - Tumor Classification
 * [tumor_tissue_type](tumor_tissue_type.md) - Radiation Therapy Tissue Type
 * [tx_prior_response](tx_prior_response.md) - Treatment Type Prior to Response Assessment
 * [type](type.md) - Default system-assigned property for each node
 * [weight_loss](weight_loss.md) - Surgery done to help people who are obese lose weight. There are different types of weight loss surgery, and each type changes the way the digestive system works. Some types make the stomach smaller, which decreases the amount of food that it can hold so the person feels full sooner and eats less. Other types make changes to the stomach and the small intestine, which decreases the nutrients and calories that are absorbed from food. Weight loss surgery can improve many obesity-related health problems, such as diabetes, high blood pressure, unhealthy cholesterol levels, sleep apnea, and knee, hip, or other body pain. Having weight loss surgery may also decrease the risk of some cancers, including endometrial cancer. Also called bariatric surgery. (Source: NCI Dictionary of Cancer Terms)
 * [who_aml](who_aml.md) - WHO AML Classification of Tumors
 * [year_at_disease_phase](year_at_disease_phase.md) - The year in which this ordinally numbered disease phase was recorded.
 * [year_at_enrollment](year_at_enrollment.md) - The year at which a subject enrolled in a study.

### Enums

 * [AbsentNotreportedPresentUnknownEnum](AbsentNotreportedPresentUnknownEnum.md)
 * [AdministrationStatusEnum](AdministrationStatusEnum.md)
 * [AdverseEventEnum](AdverseEventEnum.md)
 * [AeAttributionEnum](AeAttributionEnum.md)
 * [AeExpectedEnum](AeExpectedEnum.md)
 * [AeGradeEnum](AeGradeEnum.md)
 * [AeGradeSystemEnum](AeGradeSystemEnum.md)
 * [AeInterventionDetailEnum](AeInterventionDetailEnum.md)
 * [AeOutcomeEnum](AeOutcomeEnum.md)
 * [AePathogenConfirmationEnum](AePathogenConfirmationEnum.md)
 * [AePathogenEnum](AePathogenEnum.md)
 * [AllTypeEnum](AllTypeEnum.md)
 * [AllelicStateEnum](AllelicStateEnum.md)
 * [AltStatusEnum](AltStatusEnum.md)
 * [AmputationTypeEnum](AmputationTypeEnum.md)
 * [AnaplasiaExtentEnum](AnaplasiaExtentEnum.md)
 * [AnnArborModAbEnum](AnnArborModAbEnum.md)
 * [AssistedConceptionEnum](AssistedConceptionEnum.md)
 * [AvnJointEnum](AvnJointEnum.md)
 * [AvnJointLateralityEnum](AvnJointLateralityEnum.md)
 * [AvnMethodEnum](AvnMethodEnum.md)
 * [BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum](BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum.md)
 * [BiopsyTypeEnum](BiopsyTypeEnum.md)
 * [BmAnalysisMethodAtResponseEnum](BmAnalysisMethodAtResponseEnum.md)
 * [BmMorphologyEnum](BmMorphologyEnum.md)
 * [BoneNotreportedSofttissueUnknownEnum](BoneNotreportedSofttissueUnknownEnum.md)
 * [BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum](BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum.md)
 * [CauseOfDeathDetailEnum](CauseOfDeathDetailEnum.md)
 * [CauseOfDeathEnum](CauseOfDeathEnum.md)
 * [CauseOfDeathRankingEnum](CauseOfDeathRankingEnum.md)
 * [ChromosomalConsequenceEnum](ChromosomalConsequenceEnum.md)
 * [CimtTypeEnum](CimtTypeEnum.md)
 * [CnsDiseaseStatusEnum](CnsDiseaseStatusEnum.md)
 * [CommonNameEnum](CommonNameEnum.md)
 * [ConditionEnum](ConditionEnum.md)
 * [ConditionTypeEnum](ConditionTypeEnum.md)
 * [ConsortiumEnum](ConsortiumEnum.md)
 * [CopyNumberVariationEnum](CopyNumberVariationEnum.md)
 * [CourseEnum](CourseEnum.md)
 * [CytodifferentiationEnum](CytodifferentiationEnum.md)
 * [CytologySpecTypeEnum](CytologySpecTypeEnum.md)
 * [DataContributorIdEnum](DataContributorIdEnum.md)
 * [DataSourceEnum](DataSourceEnum.md)
 * [DeauvilleScoreEnum](DeauvilleScoreEnum.md)
 * [DepthEnum](DepthEnum.md)
 * [DetectionMethodEnum](DetectionMethodEnum.md)
 * [DiamTypeEnum](DiamTypeEnum.md)
 * [DiseasePhaseEnum](DiseasePhaseEnum.md)
 * [DiseaseSiteEnum](DiseaseSiteEnum.md)
 * [DnaIndexEnum](DnaIndexEnum.md)
 * [EExtensionSiteEnum](EExtensionSiteEnum.md)
 * [EfsCensorStatusEnum](EfsCensorStatusEnum.md)
 * [EnergyTypeEnum](EnergyTypeEnum.md)
 * [EnrolledStatusEnum](EnrolledStatusEnum.md)
 * [EthnicityEnum](EthnicityEnum.md)
 * [ExpressionConsequenceEnum](ExpressionConsequenceEnum.md)
 * [ExtensionSiteEnum](ExtensionSiteEnum.md)
 * [FabTypeEnum](FabTypeEnum.md)
 * [FlowCytometryTypeEnum](FlowCytometryTypeEnum.md)
 * [FunctionCategoryEnum](FunctionCategoryEnum.md)
 * [FunctionResultUnitEnum](FunctionResultUnitEnum.md)
 * [FunctionTestEnum](FunctionTestEnum.md)
 * [GenomicRegionEnum](GenomicRegionEnum.md)
 * [GenomicSourceClassEnum](GenomicSourceClassEnum.md)
 * [GpohScoreEnum](GpohScoreEnum.md)
 * [GtsTreatmentEnum](GtsTreatmentEnum.md)
 * [GvhdAcuityEnum](GvhdAcuityEnum.md)
 * [GvhdOrganEnum](GvhdOrganEnum.md)
 * [HistAssessmentReviewEnum](HistAssessmentReviewEnum.md)
 * [HistologyEnum](HistologyEnum.md)
 * [HistologyGradeEnum](HistologyGradeEnum.md)
 * [HistologyInpcEnum](HistologyInpcEnum.md)
 * [HlaMatchEnum](HlaMatchEnum.md)
 * [IhcResultUnitEnum](IhcResultUnitEnum.md)
 * [IhcSpecTypeEnum](IhcSpecTypeEnum.md)
 * [IhcTestEnum](IhcTestEnum.md)
 * [ImagingMethodEnum](ImagingMethodEnum.md)
 * [ImagingResultEnum](ImagingResultEnum.md)
 * [InfectionClassificationEnum](InfectionClassificationEnum.md)
 * [InheritancePatternEnum](InheritancePatternEnum.md)
 * [InitialTreatmentCategoryEnum](InitialTreatmentCategoryEnum.md)
 * [InterimResponseEnum](InterimResponseEnum.md)
 * [InvasivenessEnum](InvasivenessEnum.md)
 * [IrsGroupEnum](IrsGroupEnum.md)
 * [KaryotypeStatusEnum](KaryotypeStatusEnum.md)
 * [LabCategoryEnum](LabCategoryEnum.md)
 * [LabMethodEnum](LabMethodEnum.md)
 * [LabResultCategoricalEnum](LabResultCategoricalEnum.md)
 * [LabResultUnitEnum](LabResultUnitEnum.md)
 * [LabSeqMethodEnum](LabSeqMethodEnum.md)
 * [LabTestEnum](LabTestEnum.md)
 * [LateralityEnum](LateralityEnum.md)
 * [LeDetailEnum](LeDetailEnum.md)
 * [LeEnum](LeEnum.md)
 * [LeSeverityGradeEnum](LeSeverityGradeEnum.md)
 * [LeSubDetailEnum](LeSubDetailEnum.md)
 * [LesionAssessmentReviewEnum](LesionAssessmentReviewEnum.md)
 * [LesionBulkyEnum](LesionBulkyEnum.md)
 * [LesionClassificationEnum](LesionClassificationEnum.md)
 * [LesionPresentationEnum](LesionPresentationEnum.md)
 * [LesionResponseEnum](LesionResponseEnum.md)
 * [LesionSiteEnum](LesionSiteEnum.md)
 * [LesionSizeEnum](LesionSizeEnum.md)
 * [LesionStateEnum](LesionStateEnum.md)
 * [LesionVolumeEnum](LesionVolumeEnum.md)
 * [LkssEnum](LkssEnum.md)
 * [LocalizationTechniqueEnum](LocalizationTechniqueEnum.md)
 * [MarginsEnum](MarginsEnum.md)
 * [MeasurementTypeEnum](MeasurementTypeEnum.md)
 * [MeasurementUnitEnum](MeasurementUnitEnum.md)
 * [MedicationEnum](MedicationEnum.md)
 * [MetLungMgmtEnum](MetLungMgmtEnum.md)
 * [MethodEnum](MethodEnum.md)
 * [MitoticRateEnum](MitoticRateEnum.md)
 * [MkiEnum](MkiEnum.md)
 * [ModRationaleEnum](ModRationaleEnum.md)
 * [ModReasonEnum](ModReasonEnum.md)
 * [ModTypeEnum](ModTypeEnum.md)
 * [MrdMethodEnum](MrdMethodEnum.md)
 * [MrdMolecularMarkersEnum](MrdMolecularMarkersEnum.md)
 * [MrdSampleSourceEnum](MrdSampleSourceEnum.md)
 * [MutationTypeEnum](MutationTypeEnum.md)
 * [MyeloidSarcomaSiteEnum](MyeloidSarcomaSiteEnum.md)
 * [NecrosisEnum](NecrosisEnum.md)
 * [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [NodalDeterminationEnum](NodalDeterminationEnum.md)
 * [NodalDeterminationSourceEnum](NodalDeterminationSourceEnum.md)
 * [NodalSiteEnum](NodalSiteEnum.md)
 * [NonProtocolReasonEnum](NonProtocolReasonEnum.md)
 * [NonProtocolTimingEnum](NonProtocolTimingEnum.md)
 * [NormalizationBasisEnum](NormalizationBasisEnum.md)
 * [NotreportedUnknownEnum](NotreportedUnknownEnum.md)
 * [NumberNodesEnum](NumberNodesEnum.md)
 * [OffTypeEnum](OffTypeEnum.md)
 * [OrthopedicProcedureEnum](OrthopedicProcedureEnum.md)
 * [ParentalStatusEnum](ParentalStatusEnum.md)
 * [PelvicInvolvementEnum](PelvicInvolvementEnum.md)
 * [PerformanceScoreEnum](PerformanceScoreEnum.md)
 * [PerformanceScoreSystemEnum](PerformanceScoreSystemEnum.md)
 * [ProMeasurementTypeEnum](ProMeasurementTypeEnum.md)
 * [ProMeasuresEnum](ProMeasuresEnum.md)
 * [ProcedureExtentEnum](ProcedureExtentEnum.md)
 * [ProcedureLateralityEnum](ProcedureLateralityEnum.md)
 * [ProcedurePurposeEnum](ProcedurePurposeEnum.md)
 * [ProcedureSiteEnum](ProcedureSiteEnum.md)
 * [ProcedureTypeEnum](ProcedureTypeEnum.md)
 * [RaceEnum](RaceEnum.md)
 * [RandomizedStatusEnum](RandomizedStatusEnum.md)
 * [RatersEnum](RatersEnum.md)
 * [ReasonOffEnum](ReasonOffEnum.md)
 * [ReconstructionTypeEnum](ReconstructionTypeEnum.md)
 * [RelationEnum](RelationEnum.md)
 * [ResectionTypeEnum](ResectionTypeEnum.md)
 * [ResponseCategoryEnum](ResponseCategoryEnum.md)
 * [ResponseEnum](ResponseEnum.md)
 * [ResponseMethodEnum](ResponseMethodEnum.md)
 * [ResponseSystemEnum](ResponseSystemEnum.md)
 * [RiskGroupEnum](RiskGroupEnum.md)
 * [RiskGroupSystemEnum](RiskGroupSystemEnum.md)
 * [RouteDetailEnum](RouteDetailEnum.md)
 * [RouteEnum](RouteEnum.md)
 * [RtSiteEnum](RtSiteEnum.md)
 * [RtUnitEnum](RtUnitEnum.md)
 * [SctConditioningTypeEnum](SctConditioningTypeEnum.md)
 * [SctDonorRelationshipEnum](SctDonorRelationshipEnum.md)
 * [SctSourceEnum](SctSourceEnum.md)
 * [SctTypeEnum](SctTypeEnum.md)
 * [SexEnum](SexEnum.md)
 * [SiteWithinBoneEnum](SiteWithinBoneEnum.md)
 * [SmnFieldEnum](SmnFieldEnum.md)
 * [SmnSiteEnum](SmnSiteEnum.md)
 * [SmnTypeEnum](SmnTypeEnum.md)
 * [SomaticMalignancyTypeEnum](SomaticMalignancyTypeEnum.md)
 * [SpecimenEnum](SpecimenEnum.md)
 * [StageEnum](StageEnum.md)
 * [StageSystemEnum](StageSystemEnum.md)
 * [StatusEnum](StatusEnum.md)
 * [StudyIdEnum](StudyIdEnum.md)
 * [StudyPhaseEnum](StudyPhaseEnum.md)
 * [StudyTypeEnum](StudyTypeEnum.md)
 * [SurgeryTypeLimbEnum](SurgeryTypeLimbEnum.md)
 * [SurgeryTypeLimbSalvageEnum](SurgeryTypeLimbSalvageEnum.md)
 * [TimePointEnum](TimePointEnum.md)
 * [TmpProductEnum](TmpProductEnum.md)
 * [TmpProductTypeEnum](TmpProductTypeEnum.md)
 * [TmpTypeEnum](TmpTypeEnum.md)
 * [TnmFindingEnum](TnmFindingEnum.md)
 * [TotalDoseUnitsEnum](TotalDoseUnitsEnum.md)
 * [ToxicityDetailEnum](ToxicityDetailEnum.md)
 * [TranspositionOrganEnum](TranspositionOrganEnum.md)
 * [TreatmentArmEnum](TreatmentArmEnum.md)
 * [TrmTypeEnum](TrmTypeEnum.md)
 * [TumorClassificationEnum](TumorClassificationEnum.md)
 * [TxPriorResponseEnum](TxPriorResponseEnum.md)
 * [WhoAmlEnum](WhoAmlEnum.md)

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
