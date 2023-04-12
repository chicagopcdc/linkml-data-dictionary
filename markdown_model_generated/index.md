
# data-dictionary


**metamodel version:** 1.7.0

**version:** 0.0.1





### Classes

 * [Thing](Thing.md)
     * [AdverseEvents](AdverseEvents.md)
     * [BiopsyAndSurgicalProcedures](BiopsyAndSurgicalProcedures.md)
     * [CellularImmunotherapy](CellularImmunotherapy.md)
     * [DiseaseCharacteristics](DiseaseCharacteristics.md)
     * [FamilyMedicalHistory](FamilyMedicalHistory.md)
     * [FunctionTest](FunctionTest.md)
     * [GeneticAnalysis](GeneticAnalysis.md)
     * [Histology](Histology.md)
     * [Imaging](Imaging.md)
     * [Immunohistochemistry](Immunohistochemistry.md)
     * [LaboratoryTest](LaboratoryTest.md)
     * [LateEffects](LateEffects.md)
     * [MedicalHistory](MedicalHistory.md)
     * [Medication](Medication.md)
     * [MinimalResidualDisease](MinimalResidualDisease.md)
     * [OffProtocolTherapyOrStudy](OffProtocolTherapyOrStudy.md)
     * [PatientReportedOutcomesMetadata](PatientReportedOutcomesMetadata.md)
     * [Person](Person.md)
     * [ProtocolTreatmentModifications](ProtocolTreatmentModifications.md)
     * [RadiationTherapy](RadiationTherapy.md)
     * [Staging](Staging.md)
     * [StemCellTransplant](StemCellTransplant.md)
     * [Subject](Subject.md)
     * [SubjectResponse](SubjectResponse.md)
     * [SubsequentMalignantNeoplasm](SubsequentMalignantNeoplasm.md)
     * [SurvivalCharacteristics](SurvivalCharacteristics.md)
     * [TimePeriod](TimePeriod.md)
     * [TransfusionMedicineProcedures](TransfusionMedicineProcedures.md)
     * [TumorAssessment](TumorAssessment.md)
     * [VitalsAndAnthropometrics](VitalsAndAnthropometrics.md)

### Mixins


### Slots

 * [administration_site](administration_site.md)
 * [administration_status](administration_status.md) - The status of the medication administration.
 * [advanced_disease_signs](advanced_disease_signs.md) - Other Clinical Signs of Advanced Disease
 * [advanced_disease_signs_other](advanced_disease_signs_other.md) - Specify the "Other" ADVANCED_DISEASE_SIGNS
 * [adverse_event](adverse_event.md) - An unexpected medical problem that happens during treatment with a drug or other therapy. Adverse events may be mild, moderate, or severe, and may be caused by something other than the drug or therapy being given. Also called adverse effect. (Source: NCI Dictionary of Cancer Terms)
 * [adverse_event_other](adverse_event_other.md) - Specify the "Other" ADVERSE_EVENT
 * [ae_code](ae_code.md) - The code of the adverse event.
 * [ae_code_system](ae_code_system.md) - The coding system used for the AE_CODE
 * [ae_code_system_version](ae_code_system_version.md) - The version of the adverse event grading system.
 * [ae_hospitalization](ae_hospitalization.md) - An indication or description that an adverse event is associated with or prolongs hospitalization.
 * [ae_hospitalization_reason_other](ae_hospitalization_reason_other.md) - Specify the "Other" AE_HOSPITALIZATION_REASON
 * [ae_immune](ae_immune.md) - An adverse event affecting the immune system.
 * [ae_infusion](ae_infusion.md) - An adverse event that can be related to an infusion.
 * [ae_outcome](ae_outcome.md) - A condition or event that is attributed to the adverse event and is the result or conclusion of the adverse event.
 * [ae_pathogen](ae_pathogen.md) - The pathogen identified as the agent causing the adverse event.
 * [ae_pathogen_confirmation](ae_pathogen_confirmation.md) - Pathogen Confirmation Indicator
 * [ae_pathogen_other](ae_pathogen_other.md) - Specify the "Other" AE_PATHOGEN
 * [ae_pathogen_status](ae_pathogen_status.md) - An indication that the reported pathogen was confirmed or suspected as the cause of an infection.
 * [age_at_ae](age_at_ae.md) - The age (in days) of the subject at the onset of this adverse event
 * [age_at_ae_resolved](age_at_ae_resolved.md) - The age (in days) of the subject when this adverse event was resolved
 * [age_at_assessment](age_at_assessment.md) - The age (in days) of the subject at the time of this tumor assessment.
 * [age_at_censor_status](age_at_censor_status.md) - Age (in days) of the subject at the time of the CENSOR_STATUS
 * [age_at_cimt_start](age_at_cimt_start.md) - The age (in days) of subject at the time of cellular immunotherapy.
 * [age_at_condition](age_at_condition.md)
 * [age_at_course_anc_500](age_at_course_anc_500.md) - The age (in days) of the subject when the subject's neutrophil count exceeded 500 (ANC/mm3)
 * [age_at_disease_characteristic](age_at_disease_characteristic.md)
 * [age_at_end](age_at_end.md) - The age (in days) of the patient at the end of the reported time period. 
 * [age_at_enrollment](age_at_enrollment.md) - The age (in days) when the subject enrolled in the study. 
 * [age_at_function_test](age_at_function_test.md) - The age (in days) of the subject at the time of the function test.
 * [age_at_genetic_analysis](age_at_genetic_analysis.md) - The age (in days) of the subject at the time of this analysis.
 * [age_at_hist_assessment](age_at_hist_assessment.md) - The age (in days) of the subject at the time of this histological assessment.
 * [age_at_ihc](age_at_ihc.md) - The age (in days) of the subject at the immunohistochemical test.
 * [age_at_imaging](age_at_imaging.md) - The age (in days) of the subject at the time of imaging.
 * [age_at_lab](age_at_lab.md) - The age (in days) of the subject at the time of the laboratory test.
 * [age_at_le_eval](age_at_le_eval.md) - The age (in days) of subject when the late effect evaluation was performed.
 * [age_at_lkss](age_at_lkss.md) - The age (in days) when the last known survival status of the subject was captured.
 * [age_at_measurement](age_at_measurement.md) - The age (in days) of the subject when the vitals measurement was taken.
 * [age_at_medication_end](age_at_medication_end.md) - The age (in days) of the subject at the end of this medication treatment.
 * [age_at_medication_start](age_at_medication_start.md) - The age (in days) of the subject at the start of this medication treatment.
 * [age_at_modification](age_at_modification.md) - The age (in days) of subject since the protocol treatment modification.
 * [age_at_mrd_assessment](age_at_mrd_assessment.md) - Age in Days at Minimal Residual Disease Assessment
 * [age_at_procedure](age_at_procedure.md) - The age (in days) of the subject at the time of this procedure.
 * [age_at_recovery](age_at_recovery.md) - The age (in days) of subject at the time of stem cell transplant per recovery type.
 * [age_at_response](age_at_response.md) - The age (in days) of subject when the response assessment was made.
 * [age_at_rt_end](age_at_rt_end.md) - The age (in days) of the subject at the end of this radiation treatment.
 * [age_at_rt_start](age_at_rt_start.md) - The age (in days) of the subject at the start of this radiation treatment.
 * [age_at_sct](age_at_sct.md) - The age (in days) of subject at the time of stem cell transplantation.
 * [age_at_sct_harvest](age_at_sct_harvest.md) - The age (in days) of subject at the time of stem cell harvest
 * [age_at_smn](age_at_smn.md) - The age (in days) of subject at the diagnosis of the subsequent malignant neoplasm.
 * [age_at_staging](age_at_staging.md) - The age (in days) of the subject at the time of this staging assessment.
 * [age_at_start](age_at_start.md) - The age (in days) of the patient at the start of the reported time period. 
 * [age_at_tmp](age_at_tmp.md) - The age (in days) of subject at the start of the transfusion medicine procedure
 * [age_at_tmp_start](age_at_tmp_start.md) - The age (in days) of the subject at the start of the transfuction medicine procedure
 * [age_at_tumor_assessment](age_at_tumor_assessment.md) - The age (in days) of the subject at the time of this tumor assessment.
 * [age_at_txassign](age_at_txassign.md) - Age in Days at Treatment Assignment
 * [age_lost_to_follow_up](age_lost_to_follow_up.md) - The age (in days) when the subject was lost to follow-up.
 * [age_off](age_off.md) - The age (in days) when the subject went off of the protocol therapy or study.
 * [age_precision](age_precision.md) - The precision of the age provided in AGE_AT_DISEASE_PHASE
 * [all_type](all_type.md) - Leukemia with an acute onset, characterized by the presence of lymphoblasts in the bone marrow and the peripheral blood. It includes the acute B lymphoblastic leukemia and acute T lymphoblastic leukemia.
 * [allelic_frequency](allelic_frequency.md) - The incidence of this mutation in the tumor (%).
 * [allelic_state](allelic_state.md) - The level of occurrence of a single DNA Marker within a set of chromosomes. Heterozygous indicates the DNA Marker is only present in one of the two genes contained in homologous chromosomes. Homozygous indicates the DNA Marker is present in both genes contained in homologous chromosomes. Hemizygous indicates the DNA Marker exists in the only single copy of a gene in a non-homologous chromosome (The male X and Y chromosome are non-homologous). Hemiplasmic indicates that the DNA Marker is present in some but not all of the copies of mitochondrial DNA. Homoplasmic indicates that the DNA Maker is present in all of the copies of mitochondrial DNA. (Source: LOINC)
 * [alt_status](alt_status.md) - Activitation of the Alternative Lengthening of Telomeres (ALT) pathway.
 * [amputation_type](amputation_type.md) - The removal by surgery of a limb (arm or leg) or other body part because of injury or disease, such as diabetes or cancer. (Source: NCI Dictionary of Cancer Terms)
 * [anaplasia_pct_numeric](anaplasia_pct_numeric.md) - The numeric percentage of anaplasia found in the tumor.
 * [anaplasia_status](anaplasia_status.md) - Indicates the presence or absence of anaplasia in the tumor.
 * [anaplasia_type](anaplasia_type.md) - describes the type or extent of anaplasia found during a histopathologic exam.
 * [anc_at_response](anc_at_response.md) - ANC at Response (ANC/mm3)
 * [anc_threshold_at_response](anc_threshold_at_response.md) - ANC Threshold at Response
 * [ann_arbor_mod_ab](ann_arbor_mod_ab.md) - HL Ann Arbor A vs B Staging Designation
 * [ann_arbor_mod_e](ann_arbor_mod_e.md) - HL Ann Arbor E Staging Designation
 * [ann_arbor_mod_s](ann_arbor_mod_s.md) - HL Ann Arbor S Staging Designation
 * [another_study](another_study.md) - Did the subject enroll in another study after they went off of the study indicated by OFF_TYPE?
 * [anterior_segment_details](anterior_segment_details.md) - Anterior Segment Details
 * [anterior_segment_details_other](anterior_segment_details_other.md) - Specify the "Other" ANTERIOR_SEGMENT_DETAILS
 * [anterior_segment_exam](anterior_segment_exam.md) - Anterior Segment Exam
 * [apex_dose](apex_dose.md)
 * [as_expected](as_expected.md) - Specifies whether the nature, frequency, or severity of an adverse event is consistent with the applicable study documentation (e.g., investigator's brochure, protocol document, or consent document) or product labeling (package insert).
 * [assessment_reason](assessment_reason.md)
 * [assisted_conception](assisted_conception.md) - If the subject was conceived through assisted conception, what was the type of assisted conception?
 * [associated_condition](associated_condition.md) - A condition associated with the reported genetic mutation 
 * [associated_condition_other](associated_condition_other.md) - Specify the "Other" ASSOCIATED_CONDITION
 * [attribution](attribution.md) - A specific identifiable level (defined qualitatively or quantitatively) of probability of adverse event being caused or associated with the product or procedure administration to a patient.
 * [avn_joint](avn_joint.md) - Death of bone tissue in a joint due to temporary or permanent interruption of blood flow.
 * [avn_joint_laterality](avn_joint_laterality.md) - A finding descriptive of the laterality of the avascular necrosis in the joints.
 * [avn_joint_other](avn_joint_other.md) - Specify the "Other" AVN_JOINT
 * [avn_method](avn_method.md) - The method used to determine the diagnosis of the avascular necrosis.
 * [biological_analyte](biological_analyte.md) - A biological substance of interest that needs detection.
 * [biological_analyte_other](biological_analyte_other.md) - Specify the "Other" BIOLOGICAL_ANALYTE
 * [biopsy_type](biopsy_type.md) - The removal of cells or tissues for examination by a pathologist. The pathologist may study the tissue under a microscope or perform other tests on the cells or tissue. There are many different types of biopsy procedures. The most common types include: (1) incisional biopsy, in which only a sample of tissue is removed; (2) excisional biopsy, in which an entire lump or suspicious area is removed; and (3) needle biopsy, in which a sample of tissue or fluid is removed with a needle. When a wide needle is used, the procedure is called a core biopsy. When a thin needle is used, the procedure is called a fine-needle aspiration biopsy. (Source: NCI Dictionary of Cancer Terms)
 * [biopsy_type_other](biopsy_type_other.md) - Specify the "Other" BIOPSY_TYPE
 * [bm_analysis_method_at_response](bm_analysis_method_at_response.md) - BM Analysis Modality at Response
 * [bm_morphology](bm_morphology.md) - The morphology of bone marrow blasts.
 * [bm_pct_blasts_at_response](bm_pct_blasts_at_response.md) - BM Percent Blasts At Response
 * [bone_marrow](bone_marrow.md) - An indication of whether malignant cells are present in a bone marrow sample.
 * [boost](boost.md) - One or more extra radiation treatments targeted at the tumor bed, given after the regular sessions of radiation are complete.
 * [boost_dose](boost_dose.md) - The dose amount of the radiation boost.
 * [boost_dose_unit](boost_dose_unit.md) - A unit of measurement of the dose of radiation received or absorbed.
 * [boost_target_volume](boost_target_volume.md)
 * [boost_unit](boost_unit.md)
 * [bulk_disease](bulk_disease.md)
 * [bulk_med_mass](bulk_med_mass.md) - When the maximum width of a mass is equal or greater than one-third of the internal transverse diameter of the thorax at the level of T5/6 on a PA CXR. Bulk at an alternate site is defined as any mass measuring 10 cm or more by any imaging study.
 * [bulk_nodal_aggregate](bulk_nodal_aggregate.md)
 * [bulky_disease](bulky_disease.md) - Is this nodal mass big enough to be classified as bulky disease?
 * [cascade_testing](cascade_testing.md)
 * [category](category.md) - The category of laboratory test performed on the subject.
 * [cause_of_death](cause_of_death.md) - The circumstance or condition that results in the death of a living being.
 * [cause_of_death_detail](cause_of_death_detail.md) - The more granular reason for the CAUSE_OF_DEATH of the subject.
 * [cause_of_death_detail_other](cause_of_death_detail_other.md) - Specify the "Other" CAUSE_OF_DEATH_DETAIL
 * [cause_of_death_other](cause_of_death_other.md) - Specify the "Other" CAUSE_OF_DEATH
 * [cause_of_death_ranking](cause_of_death_ranking.md) - Assigning a weighted relevance to the cause of death.
 * [cd34_collected](cd34_collected.md) - The determination of the amount of CD34 expressing stem cells present in a sample (10^6 CD34+/kg).
 * [cd34_transplant](cd34_transplant.md) - The determination of the amount of transplanted CD34 expressing stem cells (10^6 CD34+/kg).
 * [cells_in_metaphase](cells_in_metaphase.md) - The number of cells in the sample that were arrested in the metaphase stage of the cell cycle and used for the karyotype through which this abnormality was detected.
 * [chromosomal_consequence](chromosomal_consequence.md) - Chromosomal abnormalities can have many different effects, depending on the specific abnormality. For example, an extra copy of chromosome 21 causes Down syndrome (trisomy 21). Chromosomal abnormalities can also cause miscarriage, disease, or problems in growth or development.
 * [chromosome](chromosome.md) - A structure found in cells that is comprised of a strand of linearized double-stranded DNA plus proteins that package the DNA in a condensed coil form and regulate chromosomal function.
 * [classification](classification.md) - The classification of a tumor based primarily on histopathological characteristics.
 * [classification_status](classification_status.md) - The status of the tumor classification whether it was completed or not.
 * [clinical_signs](clinical_signs.md) - Clinical Related Symptoms
 * [clinical_signs_other](clinical_signs_other.md)
 * [clonal_status](clonal_status.md)
 * [cns_disease_status](cns_disease_status.md) - CNS Involvement Status
 * [code](code.md) - The code of the adverse event.
 * [code_system](code_system.md) - The coding system used for the AE_CODE
 * [code_system_version](code_system_version.md)
 * [common_name](common_name.md) - The non-standardized name of the mutation represented by this observation.
 * [common_name_other](common_name_other.md) - Specify the "Other" COMMON_NAME
 * [concomitant_reason](concomitant_reason.md) - If a non-protocol medication, why was this medication administered?
 * [concomitant_reason_other](concomitant_reason_other.md) - Specify the "Other" CONCOMITANT_REASON
 * [condition](condition.md) - Relevant condition from the subject's medical history.
 * [condition_other](condition_other.md) - Specify the "Other" CONDITION
 * [condition_status](condition_status.md) - Was this condition observed in the subject?
 * [condition_type](condition_type.md) - The type of relevant condition from the subject's medical history.
 * [conditioning_type](conditioning_type.md) - The type of conditioning the subject received prior to stem-cell transplantation.
 * [consortium](consortium.md) - The consortium under which this data is being contributed to the Pediatric Cancer Data Commons.
 * [copy_number](copy_number.md) - The number of gene copies resulting from this mutation.
 * [copy_number_variation](copy_number_variation.md) - If there was a change in the number of gene copies, this variable specifies the type of change.
 * [country](country.md) - The country where the subject was enrolled in their study.
 * [course](course.md) - The protocol treatment "course" during which relevant observations were recorded. This variable is used across domains to frame the timing of these longitudinal observations and reduce the number of redundant variables needed to report similar concepts (see "Disease Phase Timing and Course Table" in the documentation for additional guidance).
 * [course_other](course_other.md) - Specify the "Other" COURSE
 * [course_timepoint](course_timepoint.md) - This variable gives more precise granularity to when an observation occured during the period of the indicated "Course" TIME_PERIOD
 * [cryotherapy_freezes](cryotherapy_freezes.md) - Number of cryotherapy freezes
 * [csf_diversion](csf_diversion.md)
 * [csf_result](csf_result.md) - The results of cerebrospinal fluid laboratory tests.
 * [cycle_number](cycle_number.md) - The number of the individual chemotherapeutic cycle.
 * [cycles_planned](cycles_planned.md)
 * [cytodifferentiation](cytodifferentiation.md) - Cytodifferentiation Score
 * [data_contributor_id](data_contributor_id.md) - An identifier assigned to a data contributor.
 * [data_source](data_source.md) - The nature of the investigation or the investigational use for which clinical study is being done.
 * [deauville_score](deauville_score.md) - A 5 point scale devised to assess the response to treatment of Hodgkin and Aggressive Non-Hodgkin Lymphoma.
 * [delivery_status](delivery_status.md) - Was this cycle or session delivered successfully?
 * [depth](depth.md) - The depth of the tumor.
 * [detection_method](detection_method.md) - Disease Involvement Detection Method
 * [detection_method_other](detection_method_other.md) - Specify the "Other" DETECTION_METHOD
 * [determination_source](determination_source.md)
 * [developmental_delay](developmental_delay.md) - Did the subject experience developmental delay?
 * [developmental_delay_type](developmental_delay_type.md) - What was the type of developmental delay?
 * [diagnosis_basis](diagnosis_basis.md) - The basis for diagnosis of the CPS. 
 * [diam_type](diam_type.md) - The orientation of the diameters provided
 * [disease_phase](disease_phase.md) - The phase of the cancer treatment process during which relevant observations were recorded. This variable is used across domains to frame the timing of these longitudinal observations and reduce the number of redundant variables needed to report similar concepts (see "Disease Phase Timing and Course Table" in the documentation for additional guidance).
 * [disease_site](disease_site.md) - Disease Involvement Site
 * [disease_site_other](disease_site_other.md) - Specify the "Other" DISEASE_SITE
 * [distance_margin](distance_margin.md) - The distance of the closest surgical margin from tumor after surgical resection of the tumor. The closest distance between a tumor and its resection margin has prognostic significance.
 * [distance_margin_tumor](distance_margin_tumor.md) - The distance of the closest surgical margin from tumor after surgical resection of the tumor. The closest distance between a tumor and its resection margin has prognostic significance.	
 * [dna_index](dna_index.md) - The categorical result of the DNA index for this subject
 * [dna_index_numeric](dna_index_numeric.md) - The ratio of the DNA content or chromosome number in a tumor sample compared to that in a normal sample.
 * [donor_relationship](donor_relationship.md) - The biological relationship between the stem cell donor and the recipients.
 * [e_extension_site](e_extension_site.md) - The anatomic location outside of the lymph nodes into which a disease lesion has directly spread.
 * [e_extension_site_other](e_extension_site_other.md)
 * [effusion](effusion.md)
 * [effusion_type](effusion_type.md)
 * [efs_censor_status](efs_censor_status.md) - The event free survival censor status
 * [eligible_age_lower](eligible_age_lower.md) - The low age range of the child for an evaluation tool.
 * [eligible_age_upper](eligible_age_upper.md) - The upper age range of the child for an evaluation tool.
 * [energy_type](energy_type.md) - Treatment of a disease by means of exposure of the target or the whole body to radiation. Radiation therapy is often used as part of curative therapy and occasionally as a component of palliative treatment for cancer. Other uses include total body irradiation prior to transplantation.
 * [energy_type_other](energy_type_other.md) - Specify the "Other" ENERGY_TYPE
 * [enrolled_status](enrolled_status.md) - This variable indicates if the subject was enrolled in the study, or if the subject was not enrolled in the study but received treatment per the study's protocol.
 * [estimated_volume](estimated_volume.md) - Estimated Volume (mL)
 * [ethnicity](ethnicity.md) - The social and cultural characteristics, backgrounds, or experiences shared by a group of people. These include language, religion, beliefs, values, and behaviors that are often handed down from one generation to the next. Some conditions or diseases, such as cancer, may be more common in certain ethnic groups than in others. (Source: NCI Dictionary of Cancer Terms)
 * [evaluator](evaluator.md)
 * [evaluator_other](evaluator_other.md) - Specify the "Other" PRESENTATION_EVALUATOR
 * [exam_type](exam_type.md) - The type of exam during which data for the patient was collected.
 * [expression_consequence](expression_consequence.md)
 * [extension_tumor_type](extension_tumor_type.md)
 * [extent](extent.md) - The degree to which the lesion has been cut out, or resected.
 * [external_ref_id](external_ref_id.md) - An ID to an external knowledge base that holds additional information about this genetic variant.
 * [external_ref_id_system](external_ref_id_system.md) - The name of the external knowledge base from which the EXTERNAL_REF_ID is drawn.
 * [fab_type](fab_type.md) - A classification system for acute myeloid leukemias, acute lymphoblastic leukemias, and myelodysplastic syndromes. It is based on the morphologic and cytochemical evaluation of bone marrow and peripheral blood smears.
 * [fever](fever.md) - An increase in body temperature above normal (98.6 degrees F), usually caused by disease. (Source: NCI Dictionary of Cancer Terms)
 * [finding](finding.md) - The result of an evaluation technique using a visual display of structural or functional patterns of organs or tissues that is performed to determine the presence, absence, or degree of a condition.
 * [finding_other](finding_other.md) - Specify the "Other" IMAGING_FINDING
 * [finding_site](finding_site.md) - The site in which the results of the imaging finding was located. 
 * [finding_site_other](finding_site_other.md) - Specify the "Other" IMAGING_FINDING_SITE
 * [fluid_from_tumor](fluid_from_tumor.md) - Fluid from Tumor Base
 * [fraction_dose](fraction_dose.md)
 * [fraction_dose_unit](fraction_dose_unit.md) - A unit of measurement of the dose of radiation received or absorbed.
 * [fracture](fracture.md) - Fracture at Primary Site
 * [fracture_site](fracture_site.md) - If the anatomical site of the tumor is within a bone, is that bone fractured?
 * [freeze_thaw_cycle_number](freeze_thaw_cycle_number.md) - Number of freeze-thaw cycle
 * [gene](gene.md) - A gene targeted for mutation analysis, identified in HUGO Gene Nomenclature Committee (HGNC) notation.
 * [gene2](gene2.md) - This should be used for mutations that span two gene locations (fusion, translocation, inversion, etc.). The gene name should be identified in HUGO Gene Nomenclature Committee (HGNC) notation.
 * [genomic_source_class](genomic_source_class.md) - The genomic class of the specimen being analyzed, for example, germline for inherited genome and somatic for cancer genome.
 * [gpoh_score](gpoh_score.md) - A measure of an individual's overall performance status or ability to perform their activities of daily living.
 * [grade](grade.md) - A numeric value corresponding to the degree of severity of an adverse event.
 * [grade_system](grade_system.md) - The grading system used to refer to the severity of the adverse event.
 * [grade_system_version](grade_system_version.md) - The version of the adverse event grading system.
 * [group](group.md)
 * [group_system](group_system.md)
 * [gts_treatment](gts_treatment.md) - Growing Teratoma Syndrome treatment type
 * [gvhd_acuity](gvhd_acuity.md) - Graft Versus Host Disease Acuity
 * [gvhd_organ](gvhd_organ.md) - Graft Versus Host Disease Organ
 * [gvhd_organ_other](gvhd_organ_other.md) - Specify the "Other" GVHD_ORGAN
 * [h_stage](h_stage.md)
 * [hemipelvectomy_site](hemipelvectomy_site.md) - The area involved in the hemipelvectomy.
 * [hemipelvectomy_type](hemipelvectomy_type.md) - If the pelvis was involved, was the involved procedure internal or external?
 * [hgvs_coding](hgvs_coding.md) - If this mutation is described at the sequence/chromosome level, this is its representation in HGVS nomenclature (cHGVS).
 * [hgvs_coding_transcript](hgvs_coding_transcript.md) - This is the transcript used in the HGVS expression for this mutation.
 * [hgvs_protein](hgvs_protein.md) - If this mutation is described at the translational product level, this is its representation in HGVS nomenclature (pHGVS)
 * [hgvs_protein_transcript](hgvs_protein_transcript.md)
 * [histology](histology.md) - The study of tissues and cells under a microscope (Source: NCI Dictionary of Cancer Terms)
 * [histology_grade](histology_grade.md) - A description of a tumor based on how abnormal the cancer cells and tissue look under a microscope and how quickly the cancer cells are likely to grow and spread
 * [histology_other](histology_other.md) - Specify the "Other" HISTOLOGY
 * [histology_result_numeric](histology_result_numeric.md) - The numeric value for the histology result.
 * [histology_result_text](histology_result_text.md)
 * [histology_result_unit](histology_result_unit.md) - The unit being used as the measurement for the histology test.
 * [hla_a_result](hla_a_result.md) - HLA-A Match Finding
 * [hla_b_result](hla_b_result.md) - HLA-B Match Finding
 * [hla_c_result](hla_c_result.md) - HLA-C Match Finding
 * [hla_dq_result](hla_dq_result.md) - HLA-DQ Match Finding
 * [hla_drb1_result](hla_drb1_result.md) - HLA-DRB1 Match Finding
 * [hla_match](hla_match.md) - HLA Match Status
 * [honest_broker_subject_id](honest_broker_subject_id.md) - The identifier assigned to the subject by the honest broker--an individual, organization or system acting for, or on behalf of, a covered entity to collect and provide health information to research investigators in such a manner whereby it would not be reasonably possible for the investigators or others to identify the corresponding patients-subjects directly or indirectly. The honest broker cannot be one of the investigators. The information provided to the investigators by the honest broker may incorporate linkage codes to permit information collation and/or subsequent inquiries (i.e., a "re-identification code"), however the information linking this re-identification code to the patient's identity must be retained by the honest broker and subsequent inquiries are conducted through the honest broker. (Source: NCI Thersaurus)
 * [hospitalization](hospitalization.md) - An indication or description that an adverse event is associated with or prolongs hospitalization.
 * [hydrocephalus](hydrocephalus.md) - A disorder characterized by an abnormal increase of cerebrospinal fluid in the ventricles of the brain.
 * [icu](icu.md) - Admitted to ICU
 * [independent_aberations](independent_aberations.md) - The total number of aberrations / mutations / abnormalities detected on the karyotype through which this abnormality was detected.
 * [indication](indication.md)
 * [indication_other](indication_other.md)
 * [infection_classification](infection_classification.md) - The type of evidence regarding the infection type.
 * [inheritance_pattern](inheritance_pattern.md)
 * [initial_treatment_category](initial_treatment_category.md) - The category of initial treatment that the patient receive for their disease.
 * [interim_response](interim_response.md) - An evaluation prior to the completion of therapy that the individual is responding to therapy.
 * [intervention](intervention.md) - Intervention or Medication Detail
 * [intervention_other](intervention_other.md) - Specify the "Other" INTERVENTION_DETAIL
 * [intervention_status](intervention_status.md) - Adverse Event Intervention
 * [intraocular_pressure](intraocular_pressure.md) - Intraocular Pressure
 * [intraocular_pressure_unit](intraocular_pressure_unit.md) - Intraocular Pressure Unit
 * [intraop_adjuvant](intraop_adjuvant.md) - An additional therapy administered during surgery.
 * [intraop_adjuvant_other](intraop_adjuvant_other.md) - Specify the "Other" INTRAOP_ADJUVANT
 * [invasiveness](invasiveness.md) - Tumor Invasiveness
 * [invasiveness_status](invasiveness_status.md) - Tumor Invasiveness
 * [ipsilateral_nodules](ipsilateral_nodules.md) - A metastatic tumor nodule located in the same side of the organ in which the primary tumor occurred.
 * [irs_group](irs_group.md) - IRS Surgical-Pathologic Grouping System
 * [iscn](iscn.md) - If this mutation is described by the structure of the resulting chromosomes, this is its representation in ISCN nomenclature.
 * [joint_involvement](joint_involvement.md) - A finding indicating the spread of cancer to a joint.
 * [karyotype_status](karyotype_status.md) - The status of the subject's karyotype.
 * [laser_duration](laser_duration.md)
 * [laser_duration_numeric](laser_duration_numeric.md)
 * [laser_power](laser_power.md)
 * [laser_type](laser_type.md)
 * [laser_type_other](laser_type_other.md)
 * [late_effect](late_effect.md) - A health problem that occurs months or years after a disease is diagnosed or after treatment has ended. Late effects may be caused by cancer or cancer treatment. They may include physical, mental, and social problems and second cancers. (Source: NCI Dictionary of Cancer Terms)
 * [laterality](laterality.md) - A qualifier for the side of the body the tumor findings assessment is performed.
 * [lkss](lkss.md) - The last known survival status of the subject.
 * [lkss_of_relative](lkss_of_relative.md) - The last known survival status of the relative of the subject with the prior cancer.
 * [lkss_with_disease](lkss_with_disease.md) - Did the subject still have measurable/evaluable disease at the LKSS?
 * [localization_technique](localization_technique.md) - The process of determining or marking the location or site of a tumor or disease. May also refer to the process of keeping a tumor or disease in a specific location or site. (Source: NCI Dictionary of Cancer Terms)
 * [longest_diam_dim1](longest_diam_dim1.md) - Longest Diameter of Tumor Dimension 1 (cm)
 * [longest_diam_dim2](longest_diam_dim2.md) - Longest Diameter of Tumor Dimension 2 (cm)
 * [longest_diam_dim3](longest_diam_dim3.md) - Longest Diameter of Tumor Dimension 3 (cm)
 * [macroscopic_change_pct_numeric](macroscopic_change_pct_numeric.md)
 * [macroscopic_change_status](macroscopic_change_status.md)
 * [macroscopic_change_type](macroscopic_change_type.md)
 * [maf](maf.md)
 * [maf_numeric](maf_numeric.md) - A measure of the percentage of mutant alleles within the totality of alleles in any given sample
 * [malignant_cells](malignant_cells.md) - A term used to describe cancer. Malignant cells grow in an uncontrolled way and can invade nearby tissues and spread to other parts of the body through the blood and lymph system (Source: NCI Dictionary of Cancer Terms)
 * [margin](margin.md)
 * [margins](margins.md) - The edge or border of the tissue removed in cancer surgery. The margin is described as negative or clean when the pathologist finds no cancer cells at the edge of the tissue, suggesting that all of the cancer has been removed. The margin is described as positive or involved when the pathologist finds cancer cells at the edge of the tissue, suggesting that all of the cancer has not been removed. (Source: NCI Dictionary of Cancer Terms)
 * [massive_choroidal_extension](massive_choroidal_extension.md)
 * [mature_glial_implants](mature_glial_implants.md) - A nodule of mature glial tissue that develops in the peritoneum. It is usually accompanied by mature or immature ovarian teratoma.
 * [measurement_numeric](measurement_numeric.md) - The vital sign or anthropomorphic measurement being recorded (numeric)
 * [measurement_text](measurement_text.md) - The vital sign or anthropomorphic measurement being recorded (non-numeric)
 * [measurement_type](measurement_type.md) - The type of vital sign or anthropomorphic measurement being recorded
 * [measurement_unit](measurement_unit.md) - The units used for the vital sign or anthropomorphic measurement being recorded (numeric)
 * [med_ratio](med_ratio.md) - Mediastinal Ratio
 * [medication](medication.md) - A dosage form that contains one or more active and/or inactive ingredients. Medications come in many dosage forms, including tablets, capsules, liquids, creams, and patches. They can also be given in different ways, such as by mouth, by infusion into a vein, or by drops that are put into the ear or eye. The form with the active ingredient is used to prevent, diagnose, treat, or relieve symptoms of a disease or abnormal condition. A medication that does not contain an active ingredient and is used in research studies is called a placebo. Also called drug product.
 * [medication_other](medication_other.md) - Specify the "Other" MEDICATION
 * [met_lung_mgmt](met_lung_mgmt.md) - Surgical treatment of disease metastatic to the lungs.
 * [met_non_lung_mgmt](met_non_lung_mgmt.md) - Surgical treatment of metastatic disease not involving the lungs.
 * [method](method.md) - A systematic course of action that is performed in order to complete a laboratory test.
 * [method_other](method_other.md) - Specify the "Other" LAB_METHOD
 * [mibg_avidity](mibg_avidity.md)
 * [microscopic_change_pct](microscopic_change_pct.md)
 * [microscopic_change_pct_numeric](microscopic_change_pct_numeric.md)
 * [microscopic_change_status](microscopic_change_status.md)
 * [microscopic_change_type](microscopic_change_type.md)
 * [mitotic_rate](mitotic_rate.md) - Mitoses Count
 * [mki](mki.md) - MKI (Revised INPC)
 * [mlds](mlds.md) - Acute myeloid leukemia or myelodysplastic syndrome occurring in children with Down syndrome. The acute myeloid leukemia is usually an acute megakaryoblastic leukemia, and is associated with GATA1 gene mutation.
 * [modification](modification.md) - The type of modification used.
 * [modification_basis](modification_basis.md) - The rationale for why an entity or event is changed.	
 * [modification_other](modification_other.md) - Specify the "Other" MODIFICATION
 * [modification_required](modification_required.md) - An indication that a change in treatment or a change to a device will be required following an adverse event.
 * [molecular_classification](molecular_classification.md)
 * [molecular_classification_other](molecular_classification_other.md) - Specify the "Other" MOLECULAR_CLASSIFICATION
 * [molecular_markers](molecular_markers.md) - Minimal residual disease molecular markers
 * [molecular_markers_other](molecular_markers_other.md) - Specify the "Other" MRD_MOLECULAR_MARKERS
 * [morph_code](morph_code.md) - The code for the morphology of the subsequent tumor
 * [morph_code_system](morph_code_system.md) - The coding system for MORPH_CODE
 * [morph_code_system_version](morph_code_system_version.md) - The version of the coding system indicated in MORPH_CODE_SYSTEM
 * [morph_code_txt](morph_code_txt.md) - The display text for MORPH_CODE 
 * [mosaicism_percent](mosaicism_percent.md) - The numeric level of mosaicism in this subject.
 * [mpal](mpal.md) - An acute leukemia of ambiguous lineage. It is characterized by the presence of either separate populations of blasts of more than one lineage, or one population of blasts co-expressing markers of more than one lineage.
 * [mri_sequence](mri_sequence.md)
 * [multiplicity](multiplicity.md) - This variable indicates if the recorded observation is detailing a single tumor or multiple tumors at a given site.
 * [mutant_allele_fraction](mutant_allele_fraction.md) - A measure of the percentage of mutant alleles within the totality of alleles in any given sample
 * [mutated_allele_frequency](mutated_allele_frequency.md) - The incidence of this mutation in the tumor (%).
 * [myeloid_sarcoma](myeloid_sarcoma.md) - A rare type of cancer that is made up of myeloblasts (a type of immature white blood cell) and forms outside the bone marrow and blood. The tumor cells may look green when viewed under a microscope. Myeloid sarcomas can occur anywhere in the body. They most commonly occur in people with acute myeloid leukemia or a myeloproliferative disorder. Also called chloroma, extramedullary myeloid tumor, and granulocytic sarcoma. (Source: NCI Dictionary of Cancer Terms)
 * [myeloid_sarcoma_site](myeloid_sarcoma_site.md) - The site of the extramedullary myeloid sarcoma.
 * [myeloid_sarcoma_site_other](myeloid_sarcoma_site_other.md) - Specify the "Other" MYELOID_SARCOMA_SITE
 * [necrosis](necrosis.md) - The quantitative value for the percent of necrosis.
 * [necrosis_pct](necrosis_pct.md) - A numeric measurement of the percent of cells undergoing necrosis compared to the number of total cells present in a sample.
 * [necrosis_pct_numeric](necrosis_pct_numeric.md) - The numeric percentage of necrosis found in the tumor.
 * [necrosis_status](necrosis_status.md) - Indicates the presence or absence of necrosis in the tumor.
 * [nephron_sparing_partial_nephrectomy](nephron_sparing_partial_nephrectomy.md) - If this is a renal tumor, was nephron-sparing surgery/partial nephrectomy performed?
 * [neurological_status](neurological_status.md)
 * [night_sweats](night_sweats.md) - Episodes of excessive sweating that occur during sleep. Night sweats can be severe and soak a person’s bedclothes and bed sheets, which may cause the person to wake up. Night sweats are a common symptom of menopause. They may also be caused by illness or medical conditions, such as infection, cancer, low blood sugar, hormone disorders, and neurologic conditions. They may also be a side effect of certain medicines, cancer treatment, too much caffeine or alcohol, or tobacco or drug use. (Source: NCI Dictionary of Cancer Terms)
 * [nodal_determination](nodal_determination.md) - Determination of Regional Lymph Node Involvement
 * [nodal_determination_source](nodal_determination_source.md) - The source of the determination of regional lymph node involvement. 
 * [nodal_involvement](nodal_involvement.md) - Regional Lymph Node Involvement
 * [nodal_site](nodal_site.md) - The anatomic site of a tumor node.
 * [nodular_splenic](nodular_splenic.md) - Nodular Splenic Involvement
 * [non_protocol_reason](non_protocol_reason.md) - If a non-protocol medication, why was this medication administered?
 * [non_protocol_timing](non_protocol_timing.md) - If a non-protocol radiation therapy, when was this radiation therapy administered?
 * [normalization_basis](normalization_basis.md) - An indication of what method was used to normalize the data.
 * [num_fraction](num_fraction.md) - The number of divided radiation doses received per day.
 * [number_doses](number_doses.md) - Number of times a dose of the medication was administered between the AGE_AT_MEDICATION_START and AGE_AT_MEDICATION_END values.
 * [number_hla](number_hla.md) - Number of Evaluated HLAs
 * [number_matches](number_matches.md) - Number of Matched HLAs
 * [number_nodes](number_nodes.md) - A question whether an individual has a single or multiple lymph nodes involved.
 * [number_nodes_numeric](number_nodes_numeric.md) - The number of lymph nodes that were examined.
 * [number_units](number_units.md) - The number of units transfused into an individual.
 * [off_type](off_type.md) - The code used to designate that the subject went off therapy or off the study.
 * [original_agent](original_agent.md) - The first agent planned for a therapy.	
 * [original_agent_other](original_agent_other.md) - Specify the "Other" ORIGINAL_AGENT
 * [orthopedic_procedure](orthopedic_procedure.md) - Orthopedic procedures to repair avascular necrosis.
 * [orthopedic_procedure_other](orthopedic_procedure_other.md) - Specify the "Other" ORTHOPEDIC_PROCEDURE
 * [outcome](outcome.md)
 * [palpable_nodes](palpable_nodes.md) - The lymph nodes are felt on palpation.
 * [parameningeal_extension](parameningeal_extension.md)
 * [parental_status](parental_status.md)
 * [pct_change](pct_change.md) - The percentage of change in a particular lesion.
 * [performance_score](performance_score.md) - A standard way of measuring the ability of cancer patients to perform ordinary tasks. Scores range from 0 to 100. A higher score means the patient is better able to carry out daily activities. May be used to determine a patient's prognosis, to measure changes in a patient’s ability to function, or to decide if a patient could be included in a clinical trial. (Source: NCI Dictionary of Cancer Terms)
 * [performance_score_system](performance_score_system.md) - The performance scale used.
 * [plaque_size](plaque_size.md) - Size of the plaque holding the radiation source
 * [platelet_count_at_response](platelet_count_at_response.md) - Platelet Count At Responset (platelets/mm3)
 * [platelet_threshold_at_response](platelet_threshold_at_response.md) - Exceeded Platelet Threshold >=50,000 (platelets/mm3) At Response
 * [pmid_ref](pmid_ref.md) - A globally unique identifier for a biomedical article, as assigned by PubMed.
 * [posterior_fossa_syndrome](posterior_fossa_syndrome.md)
 * [presentation_symptoms](presentation_symptoms.md)
 * [presentation_symptoms_other](presentation_symptoms_other.md) - Specify the "Other" PRESENTATION_SYMPTOMS
 * [primary_tumor_submitter_id](primary_tumor_submitter_id.md)
 * [prior_cancer](prior_cancer.md) - Does the subject have a relative who has a medical history that includes cancer?
 * [prior_cancer_laterality](prior_cancer_laterality.md) - The laterality of the prior cancer of the relative of the subject.
 * [prior_cancer_type](prior_cancer_type.md) - The type of prior cancer from the medical history of the relative of the subject.
 * [prior_steroids_month](prior_steroids_month.md) - Received Steroids within One Month Prior to Diagnosis
 * [prior_steroids_week](prior_steroids_week.md) - Received Steroids within One Week Prior to Diagnosis
 * [prior_tbi](prior_tbi.md) - Total Body Irradiation Prior to Stem Cell Transplant
 * [pro_measurement_type](pro_measurement_type.md) - The type of patient reported outcome measurement.
 * [pro_measurement_type_other](pro_measurement_type_other.md) - Specify the "Other" PRO_MEASUREMENT_TYPE
 * [pro_measures](pro_measures.md) - Survey measures that are completed by the patient which help assess patient status with regards to pain, mobility, quality of life, ability to perform daily tasks or notable events in a clinical study.
 * [pro_measures_other](pro_measures_other.md) - Specify the "Other"
 * [procedure](procedure.md) - A categorization of surgical procedures by type or purpose.
 * [procedure_extent](procedure_extent.md) - The degree to which the lesion has been cut out, or resected.
 * [procedure_other](procedure_other.md) - Specify the "Other" PROCEDURE_TYPE
 * [procedure_purpose](procedure_purpose.md) - The reason a procedure is performed.
 * [procedure_purpose_other](procedure_purpose_other.md) - Specify the "Other" PROCEDURE_PURPOSE
 * [product](product.md) - The type of product intended for transfusion.
 * [product_processing](product_processing.md) - The type of processing that is used on the transfusion product.
 * [product_processing_other](product_processing_other.md) - Specify the "Other" PRODUCT_PROCESSING
 * [protocol_medication](protocol_medication.md) - Was this medication part of the treatment protocol?
 * [protocol_procedure](protocol_procedure.md) - Was this procedure part of the treatment protocol?
 * [protocol_radiation_therapy](protocol_radiation_therapy.md) - Was this radiation therapy administration part of the treatment protocol?
 * [protocol_sct](protocol_sct.md) - Was this stem cell transplant part of the treatment protocol?
 * [proton_delivery_mode](proton_delivery_mode.md)
 * [qpet_score](qpet_score.md) - A methodology that provides semi-automatic quantification for interim FDG-PET response in lymphoma. It extends the ordinal Deauville score to a continuous scale.
 * [race](race.md) - A group of people who share physical characteristics, such as skin color and facial features. They may also share similar social or cultural identities and ancestral backgrounds. There are many racial groups, and a person may belong to or identify with more than one group. Some diseases, such as cancer, may be more common in certain races than in others. (Source: NCI Dictionary of Cancer Terms)
 * [race_identification_source](race_identification_source.md) - Who supplied the value in RACE?
 * [race_other](race_other.md) - Specify the "Other" RACE
 * [randomized_status](randomized_status.md) - The allocation of individuals to groups by chance, especially in order to control the variables in an experiment.
 * [raters](raters.md) - Raters are allowed to report the patient reported outcomes.
 * [raters_other](raters_other.md) - Specify the "Other" RATERS
 * [reason](reason.md) - The reasoning behind a treatment modification.	
 * [reason_off](reason_off.md) - The reason a subject went off the therapy or study.
 * [reason_off_other](reason_off_other.md) - Specify the "Other" REASON_OFF
 * [reason_other](reason_other.md) - Specify the "Other" REASON
 * [reconstruction_type](reconstruction_type.md) - The type of reconstruction performed on the subject.
 * [recovery_status](recovery_status.md) - The recovery status per recovery type.
 * [recovery_type](recovery_type.md) - The type of recovery after the transplant procedure.
 * [relation](relation.md) - What kind of relation is this relative who has had a relevant medical condition?
 * [relation_other](relation_other.md) - Specify the "Other" RELATION
 * [relative_honest_broker_id](relative_honest_broker_id.md)
 * [reported](reported.md) - SAE Reported to Sponsor
 * [reported_significance](reported_significance.md) - The reported ACMG clinical significance of this genetic variation
 * [resection_type](resection_type.md) - Surgery to remove tissue or part or all of an organ. (Source: NCI Dictionary of Cancer Terms)
 * [response](response.md) - A qualitative or quantitative measurement of the response of a target lesion(s) to the therapy.
 * [response_category](response_category.md) - The category used to assess the response to therapy.
 * [response_method](response_method.md) - The method used to assess the response to therapy.
 * [response_method_other](response_method_other.md) - "Specify the "Other" RESPONSE_METHOD
 * [response_system](response_system.md) - A standard from which a judgment concerning tumor response to therapy can be established.
 * [response_system_version](response_system_version.md) - The version of the response system.
 * [result](result.md) - The text result of the laboratory test.
 * [result_numeric](result_numeric.md) - The numeric result of the laboratory test.
 * [result_text](result_text.md) - The string/text result of the laboratory test.
 * [result_unit](result_unit.md) - The units used for the numeric result of the laboratory test.
 * [retinal_detachment](retinal_detachment.md) - Retinal Detachment Present and Number of Quadrants
 * [review_source](review_source.md) - The type of assessment that was used to review.
 * [revised_inpc](revised_inpc.md) - Revised INPC Prognostic Group (2003)
 * [risk_group](risk_group.md)
 * [risk_group_system](risk_group_system.md) - MaGIC Risk Group
 * [route](route.md) - Route of Administration
 * [route_detail](route_detail.md) - Designation of the part of the body through which or into which, or the way in which, the medicinal product is intended to be introduced. In some cases a medicinal product can be intended for more than one route and/or method of administration.
 * [rt_completed](rt_completed.md) - Radiation Therapy Completed as Planned
 * [rt_data_source](rt_data_source.md) - Whether radiation data was obtained from a protocol-defined dose, or 
 * [sample_source](sample_source.md) - Minimal Residual Disease Sample Source
 * [sct_cycles](sct_cycles.md) - Number of Stem Cell Transplant Cycles
 * [sct_success](sct_success.md) - Was the stem cell transplant successful?
 * [sct_type](sct_type.md) - A procedure in which a patient receives healthy stem cells (blood-forming cells) to replace their own stem cells that have been destroyed by treatment with radiation or high doses of chemotherapy. The healthy stem cells may come from the blood or bone marrow of the patient or from a related or unrelated donor. A stem cell transplant may be autologous (using a patient’s own stem cells that were collected and saved before treatment), allogeneic (using stem cells from a related or unrelated donor), syngeneic (using stem cells donated by an identical twin), or cord blood (using umbilical cord blood donated after a baby is born). (Source: NCI Dictionary of Cancer Terms)
 * [secondary_aml](secondary_aml.md) - Secondary Acute Myeloid Leukemia
 * [seeds_classification](seeds_classification.md) - Retinoblastoma Seeds Classification
 * [seeds_pattern](seeds_pattern.md) - Retinoblastoma Seeds Pattern
 * [seeds_present](seeds_present.md) - Retinoblastoma Seeds Present
 * [seeds_status](seeds_status.md) - Retinoblastoma Seeds Status
 * [sensitivity](sensitivity.md) - Sensitivity of modality used to determine minimal residual disease.
 * [seq_method](seq_method.md) - Quantitative Sequencing Method
 * [session_number](session_number.md)
 * [sex](sex.md) - The biological sex of the subject.
 * [shared_predisposition](shared_predisposition.md)
 * [site](site.md) - Specifies the anatomic site of a localized pathological or traumatic structural change, damage, deformity, or discontinuity of tissue, organ, or body part.
 * [site_other](site_other.md) - Specify the "Other" TUMOR_SITE
 * [site_within_bone](site_within_bone.md) - The anatomic site within the bone.
 * [skip_met_involvement](skip_met_involvement.md) - A question about the areas involved in the skip metastasis.
 * [skip_tumor](skip_tumor.md) - A benign or malignant pathologic process which is patchy and skips areas which are normal (uninvolved by the pathologic process).
 * [smn](smn.md) - SMN Type
 * [smn_field](smn_field.md) - The location of the subsequent malignant neoplasm related to the prior radiation field.
 * [smn_other](smn_other.md) - Specify the "Other" SMN
 * [smn_status](smn_status.md) - Was the indicated subsequent malignant neoplasm found in the patient?
 * [smn_type_other](smn_type_other.md) - Specify the "Other" SMN_TYPE
 * [somatic_malignancy_type](somatic_malignancy_type.md) - A malignant non-germ cell component that typically develops secondarily within a germ cell tumor. The malignant cellular component is usually sarcomatous or carcinomatous.
 * [somatic_malignancy_type_other](somatic_malignancy_type_other.md) - Specify the "Other" SOMATIC_MALIGNANCY_TYPE
 * [source_pct](source_pct.md) - Percent of tumor cells in the sample (categorical)
 * [source_pct_numeric](source_pct_numeric.md) - Percent of tumor cells in the sample (numeric)
 * [specimen](specimen.md) - The type of specimen analyzed.
 * [specimen_other](specimen_other.md) - Specify the "Other" SPECIMEN
 * [stage](stage.md) - The extent of a cancer in the body. Staging is usually based on the size of the tumor, whether lymph nodes contain cancer, and whether the cancer has spread from the original site to other parts of the body (Source: NCI Dictionary of Cancer Terms)
 * [stage_other](stage_other.md) - Specify the "Other" STAGE
 * [stage_system](stage_system.md) - A systematic method for clinicopathologic evaluation of tumors.
 * [stage_system_category](stage_system_category.md)
 * [stage_type](stage_type.md)
 * [status](status.md) - Is this mutation/abnormality present in this subject?
 * [stem_cell_source](stem_cell_source.md) - The source of the stem cells for the stem cell transplant.
 * [stem_cell_source_other](stem_cell_source_other.md) - Specify the "Other" STEM_CELL_SOURCE
 * [study_id](study_id.md) - A sequence of characters used to identify, name, or characterize the study.
 * [study_phase](study_phase.md) - The phase of the clinical trial that the subject was enrolled in for the collection of this data.
 * [study_type](study_type.md) - The nature of the investigation or the investigational use for which clinical study is being done.
 * [sub_agent](sub_agent.md) - A medication was substituted with another.	
 * [sub_agent_other](sub_agent_other.md) - Specify the "Other" SUB_AGENT
 * [➞persons](subject__persons.md)
 * [subjects](subjects.md)
 * [submitter_id](submitter_id.md) - PCDC internal event ID
 * [supportive_medication](supportive_medication.md) - Adverse Event Supportive Care Medication
 * [surgery_type_amputation](surgery_type_amputation.md) - The removal by surgery of a limb (arm or leg) or other body part because of injury or disease, such as diabetes or cancer. (Source: NCI Dictionary of Cancer Terms)
 * [surgery_type_limb](surgery_type_limb.md) - The type of surgical procedures performed on the limb of the subject.
 * [surgery_type_limb_salvage](surgery_type_limb_salvage.md) - A procedure to avoid amputation of an arm or leg.
 * [surgical_complications](surgical_complications.md)
 * [surgical_complications_other](surgical_complications_other.md)
 * [suspected_diagnosis_other](suspected_diagnosis_other.md) - Specify the "Other" SUSPECTED_DIAGNOSIS
 * [suspected_referring_diagnosis](suspected_referring_diagnosis.md) - Suspected Referring Diagnosis
 * [symptoms](symptoms.md) - A physical or mental problem that a person experiences that may indicate a disease or condition. Symptoms cannot be seen and do not show up on medical tests. Some examples of symptoms are headache, fatigue, nausea, and pain. (Source: NCI Dictionary of Cancer Terms)
 * [tam](tam.md) - A myeloid proliferation occurring in newborns with Down syndrome. It is clinically and morphologically indistinguishable from acute myeloid leukemia and is associated with GATA1 mutations. The blasts display morphologic and immunophenotypic features of megakaryocytic lineage. In the majority of patients the myeloid proliferation undergoes spontaneous remission.
 * [target_volume](target_volume.md) - The intended target volume for this radiation therapy.
 * [technique](technique.md) - Treatment of a disease by means of exposure of the target or the whole body to radiation. Radiation therapy is often used as part of curative therapy and occasionally as a component of palliative treatment for cancer. Other uses include total body irradiation prior to transplantation.
 * [technique_other](technique_other.md) - Specify the "Other" TECHNIQUE
 * [test](test.md) - A medical procedure that involves testing a sample of blood, urine, or other substance from the body. Laboratory tests can help determine a diagnosis, plan treatment, check to see if treatment is working, or monitor the disease over time Source: NCI Dictionary of Cancer Terms)
 * [test_other](test_other.md) - Specify the "Other" LAB_TEST
 * [thredhold_low](thredhold_low.md) - The minimum level that must be attained for a certain reaction to occur or be manifested.
 * [threshold_high](threshold_high.md) - The maximum level that must be exceeded for a certain reaction to occur or be manifested.
 * [threshold_level](threshold_level.md) - The point at which a psychological or physiological effect begins to be produced.
 * [threshold_low](threshold_low.md) - The minimum level that must be attained for a certain reaction to occur or be manifested.
 * [time_period_number](time_period_number.md) - This variable indicates the ordinal numbering of time periods of the same TIME_PERIOD_TYPE within its various subgroups (e.g., Relapse 1, Relapse 2, Relapse 3, etc.). The observations across domains can therefore be organized longitudinally without the need for specific dates.
 * [time_period_type](time_period_type.md) - The type of time period being reported.
 * [time_periods](time_periods.md)
 * [time_point](time_point.md) - The point in time that acts as a fixed reference point to an event.
 * [tissue_type](tissue_type.md) - A piece of tissue removed from an organism for examination, analysis, or propagation.
 * [tkd_involvement](tkd_involvement.md)
 * [tnm_finding](tnm_finding.md)
 * [top_code](top_code.md) - The topography code describes the site of origin of the neoplasm.
 * [top_code_system](top_code_system.md) - The coding system for the code used in TOP_CODE
 * [top_code_system_version](top_code_system_version.md) - The version of the coding system indicated in TOP_CODE_SYSTEM
 * [top_code_txt](top_code_txt.md) - The display text for TOP_CODE 
 * [total_chromosomes](total_chromosomes.md) - The number of chromosomes detected on the karyotype through which this abnormality was detected.
 * [total_dose](total_dose.md) - The total radiation dose administered.
 * [total_dose_administered](total_dose_administered.md) - Total amount of medication administered between the AGE_AT_MEDICATION_START and AGE_AT_MEDICATION values. Assuming all doses administered are the same amount of medication, this value should be equal to the amount of medication given at each dose multiplied by the number of doses.
 * [total_dose_given](total_dose_given.md) - Was the full dose of this cycle or session administered?
 * [total_dose_intended](total_dose_intended.md) - This is the total amount of medication that was intended to be administered either by trial protocol, by prescription, or other indicator at the time point of AGE_AT_MEDICATION_START. Often, this will be equal to TOTAL_DOSE_ADMINISTERED. If TOTAL_DOSE_ADMINISTERED and TOTAL_DOSE_INTENDED are different, this indicates a deviation from the protocol or plan and may be due to a variety of factors including patient intolerance, patient non-adherence, etc.
 * [total_dose_unit](total_dose_unit.md) - A unit of measurement of the dose of radiation received or absorbed.
 * [tox_delay](tox_delay.md) - Were there treatment delays due to toxicity?
 * [tox_dose_reductions](tox_dose_reductions.md) - The number of chemotherapy dose reductions due to toxicity
 * [tox_high_grade_events](tox_high_grade_events.md) - The number of grade III-IV (CTCAE) toxicity events
 * [toxicity_detail](toxicity_detail.md) - Information about the conditions surrounding the toxicity.	
 * [toxicity_detail_other](toxicity_detail_other.md)
 * [toxicity_immune](toxicity_immune.md) - Toxicity that impairs or damages the immune system.	
 * [toxicity_infusion](toxicity_infusion.md) - Toxicity related to an infusion.	
 * [transposition_organ](transposition_organ.md) - A procedure to move organs out of the range of the damaging effects of radiation.
 * [traumatic_tap](traumatic_tap.md) - Contamination of a cerebrospinal fluid sample by red blood cells greater than 10/mm3.
 * [treatment_arm](treatment_arm.md) - A specific treatment plan within a clinical trial that describes the activities a subject will be involved in as he or she progresses through the study.
 * [treatment_related](treatment_related.md) - Is this subsequent malignancy related to prior treatment recieved?
 * [trm_type](trm_type.md) - If the mortality is treatment related, what type of treatment was involved?
 * [trm_type_other](trm_type_other.md) - Specify the "Other" TRM_TYPE
 * [tumor_classification](tumor_classification.md) - The classification of a tumor based primarily on histopathological characteristics.
 * [tumor_from_fovea](tumor_from_fovea.md) - Tumor Distance from Fovea of the Closest Tumor
 * [tumor_from_optic_nerve](tumor_from_optic_nerve.md) - Tumor Distance from Optic Nerve of the Closest Tumor
 * [tumor_number](tumor_number.md) - The number of tumors found.
 * [tumor_presentation](tumor_presentation.md)
 * [tumor_rupture](tumor_rupture.md) - If this is a solid tumor, was there pre-surgical tumor rupture?
 * [tumor_site](tumor_site.md)
 * [tumor_size](tumor_size.md) - The tumor size of the largest tumor.
 * [tumor_submitter_id](tumor_submitter_id.md)
 * [tumor_type](tumor_type.md)
 * [tumor_volume](tumor_volume.md) - The size of a cancer measured by the amount of space taken up by the tumor. For example, the tumor volume of prostate cancer is the percentage of the prostate taken up by the tumor.
 * [tx_prior_response](tx_prior_response.md) - Treatment Type Prior to Response Assessment
 * [type](type.md) - Default system-assigned property for each node
 * [type_other](type_other.md) - Specify the "Other" CIMT_TYPE
 * [variation_effect](variation_effect.md)
 * [variation_type](variation_type.md) - The type of variation detected by this genetic analysis.
 * [variation_type_other](variation_type_other.md) - Specify the "Other" MUTATION_TYPE
 * [visual_acuity_notation](visual_acuity_notation.md) - Visual Acuity Notation
 * [visual_acuity_result](visual_acuity_result.md) - Visual Acuity Result
 * [visual_acuity_result_numeric](visual_acuity_result_numeric.md) - Visual Acuity Result Numeric
 * [visual_acuity_technique](visual_acuity_technique.md) - Visual Acuity Technique
 * [visual_discrete_tumors](visual_discrete_tumors.md) - Visual Disrete Tumors
 * [weight_loss](weight_loss.md) - Surgery done to help people who are obese lose weight. There are different types of weight loss surgery, and each type changes the way the digestive system works. Some types make the stomach smaller, which decreases the amount of food that it can hold so the person feels full sooner and eats less. Other types make changes to the stomach and the small intestine, which decreases the nutrients and calories that are absorbed from food. Weight loss surgery can improve many obesity-related health problems, such as diabetes, high blood pressure, unhealthy cholesterol levels, sleep apnea, and knee, hip, or other body pain. Having weight loss surgery may also decrease the risk of some cancers, including endometrial cancer. Also called bariatric surgery. (Source: NCI Dictionary of Cancer Terms)
 * [who_aml](who_aml.md) - A classification of acute myeloid leukemia tumors by the World Health Organization (WHO).
 * [year_at_enrollment](year_at_enrollment.md) - The year at which a subject enrolled in a study.
 * [year_at_start](year_at_start.md) - The year at the start of the indicated time period

### Enums

 * [AbsentNotreportedPresentUnknownEnum](AbsentNotreportedPresentUnknownEnum.md)
 * [AdministrationSiteEnum](AdministrationSiteEnum.md)
 * [AdministrationStatusEnum](AdministrationStatusEnum.md)
 * [AdvancedDiseaseSignsEnum](AdvancedDiseaseSignsEnum.md)
 * [AdverseEventEnum](AdverseEventEnum.md)
 * [AeCodeSystemEnum](AeCodeSystemEnum.md)
 * [AeOutcomeEnum](AeOutcomeEnum.md)
 * [AePathogenEnum](AePathogenEnum.md)
 * [AgePrecisionEnum](AgePrecisionEnum.md)
 * [AliveDeadNotreportedUnknownEnum](AliveDeadNotreportedUnknownEnum.md)
 * [AllTypeEnum](AllTypeEnum.md)
 * [AllelicStateEnum](AllelicStateEnum.md)
 * [AltStatusEnum](AltStatusEnum.md)
 * [AmputationTypeEnum](AmputationTypeEnum.md)
 * [AnaplasiaTypeEnum](AnaplasiaTypeEnum.md)
 * [AnnArborModAbEnum](AnnArborModAbEnum.md)
 * [AnteriorSegmentDetailsEnum](AnteriorSegmentDetailsEnum.md)
 * [AnteriorSegmentExamEnum](AnteriorSegmentExamEnum.md)
 * [AssessmentReasonEnum](AssessmentReasonEnum.md)
 * [AssistedConceptionEnum](AssistedConceptionEnum.md)
 * [AssociatedConditionEnum](AssociatedConditionEnum.md)
 * [AttributionEnum](AttributionEnum.md)
 * [AvnJointEnum](AvnJointEnum.md)
 * [AvnMethodEnum](AvnMethodEnum.md)
 * [BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum](BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum.md)
 * [BilateralLeftMidlineNotreportedRightUnknownEnum](BilateralLeftMidlineNotreportedRightUnknownEnum.md)
 * [BiologicalAnalyteEnum](BiologicalAnalyteEnum.md)
 * [BiopsyTypeEnum](BiopsyTypeEnum.md)
 * [BmAnalysisMethodAtResponseEnum](BmAnalysisMethodAtResponseEnum.md)
 * [BmMorphologyEnum](BmMorphologyEnum.md)
 * [BoostDoseUnitEnum](BoostDoseUnitEnum.md)
 * [BoostTargetVolumeEnum](BoostTargetVolumeEnum.md)
 * [BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum](BothallelesmatchedNotreportedOneallelemismatchedTwoallelesmismatchedUnknownEnum.md)
 * [CategoryEnum](CategoryEnum.md)
 * [CauseOfDeathDetailEnum](CauseOfDeathDetailEnum.md)
 * [CauseOfDeathEnum](CauseOfDeathEnum.md)
 * [CauseOfDeathRankingEnum](CauseOfDeathRankingEnum.md)
 * [CgeNotreportedUnknownCgyEnum](CgeNotreportedUnknownCgyEnum.md)
 * [ChromosomalConsequenceEnum](ChromosomalConsequenceEnum.md)
 * [ClassificationEnum](ClassificationEnum.md)
 * [ClassificationStatusEnum](ClassificationStatusEnum.md)
 * [ClinicalSignsEnum](ClinicalSignsEnum.md)
 * [ClonalStatusEnum](ClonalStatusEnum.md)
 * [CnsDiseaseStatusEnum](CnsDiseaseStatusEnum.md)
 * [CodeSystemEnum](CodeSystemEnum.md)
 * [CommonNameEnum](CommonNameEnum.md)
 * [ConcomitantReasonEnum](ConcomitantReasonEnum.md)
 * [ConditionEnum](ConditionEnum.md)
 * [ConditionTypeEnum](ConditionTypeEnum.md)
 * [ConditioningTypeEnum](ConditioningTypeEnum.md)
 * [ConfirmedNotreportedSuspectedUnknownEnum](ConfirmedNotreportedSuspectedUnknownEnum.md)
 * [ConsortiumEnum](ConsortiumEnum.md)
 * [CopyNumberVariationEnum](CopyNumberVariationEnum.md)
 * [CourseEnum](CourseEnum.md)
 * [CourseTimepointEnum](CourseTimepointEnum.md)
 * [CsfDiversionEnum](CsfDiversionEnum.md)
 * [CytodifferentiationEnum](CytodifferentiationEnum.md)
 * [DataContributorIdEnum](DataContributorIdEnum.md)
 * [DataSourceEnum](DataSourceEnum.md)
 * [DeauvilleScoreEnum](DeauvilleScoreEnum.md)
 * [DepthEnum](DepthEnum.md)
 * [DetectionMethodEnum](DetectionMethodEnum.md)
 * [DeterminationSourceEnum](DeterminationSourceEnum.md)
 * [DiagnosisBasisEnum](DiagnosisBasisEnum.md)
 * [DiamTypeEnum](DiamTypeEnum.md)
 * [DiseasePhaseEnum](DiseasePhaseEnum.md)
 * [DiseaseSiteEnum](DiseaseSiteEnum.md)
 * [DnaIndexEnum](DnaIndexEnum.md)
 * [DonorRelationshipEnum](DonorRelationshipEnum.md)
 * [EExtensionSiteEnum](EExtensionSiteEnum.md)
 * [EffusionTypeEnum](EffusionTypeEnum.md)
 * [EfsCensorStatusEnum](EfsCensorStatusEnum.md)
 * [EnergyTypeEnum](EnergyTypeEnum.md)
 * [EnrolledStatusEnum](EnrolledStatusEnum.md)
 * [EthnicityEnum](EthnicityEnum.md)
 * [EvaluatorEnum](EvaluatorEnum.md)
 * [ExamTypeEnum](ExamTypeEnum.md)
 * [ExpressionConsequenceEnum](ExpressionConsequenceEnum.md)
 * [ExtensionTumorTypeEnum](ExtensionTumorTypeEnum.md)
 * [ExtentEnum](ExtentEnum.md)
 * [ExternalRefIdSystemEnum](ExternalRefIdSystemEnum.md)
 * [FabTypeEnum](FabTypeEnum.md)
 * [FindingEnum](FindingEnum.md)
 * [FindingSiteEnum](FindingSiteEnum.md)
 * [FluidFromTumorEnum](FluidFromTumorEnum.md)
 * [GenomicSourceClassEnum](GenomicSourceClassEnum.md)
 * [GpohScoreEnum](GpohScoreEnum.md)
 * [GradeEnum](GradeEnum.md)
 * [GradeSystemEnum](GradeSystemEnum.md)
 * [GroupEnum](GroupEnum.md)
 * [GroupSystemEnum](GroupSystemEnum.md)
 * [GtsTreatmentEnum](GtsTreatmentEnum.md)
 * [GvhdAcuityEnum](GvhdAcuityEnum.md)
 * [GvhdOrganEnum](GvhdOrganEnum.md)
 * [HStageEnum](HStageEnum.md)
 * [HemipelvectomySiteEnum](HemipelvectomySiteEnum.md)
 * [HemipelvectomyTypeEnum](HemipelvectomyTypeEnum.md)
 * [HistologyEnum](HistologyEnum.md)
 * [HistologyGradeEnum](HistologyGradeEnum.md)
 * [HistologyResultUnitEnum](HistologyResultUnitEnum.md)
 * [HydrocephalusEnum](HydrocephalusEnum.md)
 * [IndicationEnum](IndicationEnum.md)
 * [InfectionClassificationEnum](InfectionClassificationEnum.md)
 * [InheritancePatternEnum](InheritancePatternEnum.md)
 * [InitialTreatmentCategoryEnum](InitialTreatmentCategoryEnum.md)
 * [InterimResponseEnum](InterimResponseEnum.md)
 * [InterventionEnum](InterventionEnum.md)
 * [IntraocularPressureUnitEnum](IntraocularPressureUnitEnum.md)
 * [IntraopAdjuvantEnum](IntraopAdjuvantEnum.md)
 * [InvasivenessEnum](InvasivenessEnum.md)
 * [IrsGroupEnum](IrsGroupEnum.md)
 * [KaryotypeStatusEnum](KaryotypeStatusEnum.md)
 * [LaserDurationEnum](LaserDurationEnum.md)
 * [LaserPowerEnum](LaserPowerEnum.md)
 * [LaserTypeEnum](LaserTypeEnum.md)
 * [LateEffectEnum](LateEffectEnum.md)
 * [LocalizationTechniqueEnum](LocalizationTechniqueEnum.md)
 * [MacroscopicChangeTypeEnum](MacroscopicChangeTypeEnum.md)
 * [MafEnum](MafEnum.md)
 * [MarginEnum](MarginEnum.md)
 * [MarginsEnum](MarginsEnum.md)
 * [MassiveChoroidalExtensionEnum](MassiveChoroidalExtensionEnum.md)
 * [MeasurementTypeEnum](MeasurementTypeEnum.md)
 * [MeasurementUnitEnum](MeasurementUnitEnum.md)
 * [MedicationEnum](MedicationEnum.md)
 * [MetLungMgmtEnum](MetLungMgmtEnum.md)
 * [MethodEnum](MethodEnum.md)
 * [MicroscopicChangePctEnum](MicroscopicChangePctEnum.md)
 * [MicroscopicChangeTypeEnum](MicroscopicChangeTypeEnum.md)
 * [MitoticRateEnum](MitoticRateEnum.md)
 * [MkiEnum](MkiEnum.md)
 * [ModificationBasisEnum](ModificationBasisEnum.md)
 * [ModificationEnum](ModificationEnum.md)
 * [MolecularClassificationEnum](MolecularClassificationEnum.md)
 * [MolecularMarkersEnum](MolecularMarkersEnum.md)
 * [MorphCodeSystemEnum](MorphCodeSystemEnum.md)
 * [MriSequenceEnum](MriSequenceEnum.md)
 * [MultiplicityEnum](MultiplicityEnum.md)
 * [MyeloidSarcomaSiteEnum](MyeloidSarcomaSiteEnum.md)
 * [NecrosisEnum](NecrosisEnum.md)
 * [NegativeNotreportedPositiveUnknownEnum](NegativeNotreportedPositiveUnknownEnum.md)
 * [NeurologicalStatusEnum](NeurologicalStatusEnum.md)
 * [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [NodalDeterminationEnum](NodalDeterminationEnum.md)
 * [NodalDeterminationSourceEnum](NodalDeterminationSourceEnum.md)
 * [NodalSiteEnum](NodalSiteEnum.md)
 * [NonProtocolReasonEnum](NonProtocolReasonEnum.md)
 * [NonProtocolTimingEnum](NonProtocolTimingEnum.md)
 * [NormalizationBasisEnum](NormalizationBasisEnum.md)
 * [NumberNodesEnum](NumberNodesEnum.md)
 * [OffTypeEnum](OffTypeEnum.md)
 * [OrthopedicProcedureEnum](OrthopedicProcedureEnum.md)
 * [OutcomeEnum](OutcomeEnum.md)
 * [ParentalStatusEnum](ParentalStatusEnum.md)
 * [PerformanceScoreEnum](PerformanceScoreEnum.md)
 * [PerformanceScoreSystemEnum](PerformanceScoreSystemEnum.md)
 * [PlaqueSizeEnum](PlaqueSizeEnum.md)
 * [PresentationSymptomsEnum](PresentationSymptomsEnum.md)
 * [PriorCancerLateralityEnum](PriorCancerLateralityEnum.md)
 * [ProMeasurementTypeEnum](ProMeasurementTypeEnum.md)
 * [ProMeasuresEnum](ProMeasuresEnum.md)
 * [ProcedureEnum](ProcedureEnum.md)
 * [ProcedureExtentEnum](ProcedureExtentEnum.md)
 * [ProcedurePurposeEnum](ProcedurePurposeEnum.md)
 * [ProductEnum](ProductEnum.md)
 * [ProductProcessingEnum](ProductProcessingEnum.md)
 * [ProtonDeliveryModeEnum](ProtonDeliveryModeEnum.md)
 * [RaceEnum](RaceEnum.md)
 * [RaceIdentificationSourceEnum](RaceIdentificationSourceEnum.md)
 * [RandomizedStatusEnum](RandomizedStatusEnum.md)
 * [RatersEnum](RatersEnum.md)
 * [ReasonEnum](ReasonEnum.md)
 * [ReasonOffEnum](ReasonOffEnum.md)
 * [ReconstructionTypeEnum](ReconstructionTypeEnum.md)
 * [RecoveryStatusEnum](RecoveryStatusEnum.md)
 * [RecoveryTypeEnum](RecoveryTypeEnum.md)
 * [RelationEnum](RelationEnum.md)
 * [ReportedSignificanceEnum](ReportedSignificanceEnum.md)
 * [ResectionTypeEnum](ResectionTypeEnum.md)
 * [ResponseCategoryEnum](ResponseCategoryEnum.md)
 * [ResponseEnum](ResponseEnum.md)
 * [ResponseMethodEnum](ResponseMethodEnum.md)
 * [ResponseSystemEnum](ResponseSystemEnum.md)
 * [ResultUnitEnum](ResultUnitEnum.md)
 * [RetinalDetachmentEnum](RetinalDetachmentEnum.md)
 * [ReviewSourceEnum](ReviewSourceEnum.md)
 * [RevisedInpcEnum](RevisedInpcEnum.md)
 * [RiskGroupEnum](RiskGroupEnum.md)
 * [RiskGroupSystemEnum](RiskGroupSystemEnum.md)
 * [RouteDetailEnum](RouteDetailEnum.md)
 * [RouteEnum](RouteEnum.md)
 * [RtDataSourceEnum](RtDataSourceEnum.md)
 * [SampleSourceEnum](SampleSourceEnum.md)
 * [SctTypeEnum](SctTypeEnum.md)
 * [SeedsClassificationEnum](SeedsClassificationEnum.md)
 * [SeedsPatternEnum](SeedsPatternEnum.md)
 * [SeedsStatusEnum](SeedsStatusEnum.md)
 * [SeqMethodEnum](SeqMethodEnum.md)
 * [SexEnum](SexEnum.md)
 * [SiteEnum](SiteEnum.md)
 * [SiteWithinBoneEnum](SiteWithinBoneEnum.md)
 * [SkipMetInvolvementEnum](SkipMetInvolvementEnum.md)
 * [SmnEnum](SmnEnum.md)
 * [SmnFieldEnum](SmnFieldEnum.md)
 * [SomaticMalignancyTypeEnum](SomaticMalignancyTypeEnum.md)
 * [SourcePctEnum](SourcePctEnum.md)
 * [SpecimenEnum](SpecimenEnum.md)
 * [StageEnum](StageEnum.md)
 * [StageSystemCategoryEnum](StageSystemCategoryEnum.md)
 * [StageSystemEnum](StageSystemEnum.md)
 * [StageTypeEnum](StageTypeEnum.md)
 * [StatusEnum](StatusEnum.md)
 * [StemCellSourceEnum](StemCellSourceEnum.md)
 * [StudyIdEnum](StudyIdEnum.md)
 * [StudyPhaseEnum](StudyPhaseEnum.md)
 * [StudyTypeEnum](StudyTypeEnum.md)
 * [SurgeryTypeAmputationEnum](SurgeryTypeAmputationEnum.md)
 * [SurgeryTypeLimbEnum](SurgeryTypeLimbEnum.md)
 * [SurgeryTypeLimbSalvageEnum](SurgeryTypeLimbSalvageEnum.md)
 * [SurgicalComplicationsEnum](SurgicalComplicationsEnum.md)
 * [SuspectedReferringDiagnosisEnum](SuspectedReferringDiagnosisEnum.md)
 * [TargetVolumeEnum](TargetVolumeEnum.md)
 * [TechniqueEnum](TechniqueEnum.md)
 * [TestEnum](TestEnum.md)
 * [ThresholdLevelEnum](ThresholdLevelEnum.md)
 * [TimePeriodTypeEnum](TimePeriodTypeEnum.md)
 * [TimePointEnum](TimePointEnum.md)
 * [TissueTypeEnum](TissueTypeEnum.md)
 * [TnmFindingEnum](TnmFindingEnum.md)
 * [TopCodeSystemEnum](TopCodeSystemEnum.md)
 * [TotalDoseUnitEnum](TotalDoseUnitEnum.md)
 * [ToxicityDetailEnum](ToxicityDetailEnum.md)
 * [TranspositionOrganEnum](TranspositionOrganEnum.md)
 * [TreatmentArmEnum](TreatmentArmEnum.md)
 * [TrmTypeEnum](TrmTypeEnum.md)
 * [TumorClassificationEnum](TumorClassificationEnum.md)
 * [TumorFromFoveaEnum](TumorFromFoveaEnum.md)
 * [TumorFromOpticNerveEnum](TumorFromOpticNerveEnum.md)
 * [TumorPresentationEnum](TumorPresentationEnum.md)
 * [TumorSiteEnum](TumorSiteEnum.md)
 * [TumorSizeEnum](TumorSizeEnum.md)
 * [TumorTypeEnum](TumorTypeEnum.md)
 * [TumorVolumeEnum](TumorVolumeEnum.md)
 * [TxPriorResponseEnum](TxPriorResponseEnum.md)
 * [VariationEffectEnum](VariationEffectEnum.md)
 * [VariationTypeEnum](VariationTypeEnum.md)
 * [VisualAcuityNotationEnum](VisualAcuityNotationEnum.md)
 * [VisualAcuityResultEnum](VisualAcuityResultEnum.md)
 * [VisualAcuityTechniqueEnum](VisualAcuityTechniqueEnum.md)
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
