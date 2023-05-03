-- # Class: "Thing" Description: ""
--     * Slot: id Description: 
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
-- # Class: "Person" Description: ""
--     * Slot: id Description: 
--     * Slot: sex Description: The biological sex of the subject.
--     * Slot: race Description: A group of people who share physical characteristics, such as skin color and facial features. They may also share similar social or cultural identities and ancestral backgrounds. There are many racial groups, and a person may belong to or identify with more than one group. Some diseases, such as cancer, may be more common in certain races than in others. (Source: NCI Dictionary of Cancer Terms)
--     * Slot: race_other Description: Specify the "Other" RACE
--     * Slot: ethnicity Description: The social and cultural characteristics, backgrounds, or experiences shared by a group of people. These include language, religion, beliefs, values, and behaviors that are often handed down from one generation to the next. Some conditions or diseases, such as cancer, may be more common in certain ethnic groups than in others. (Source: NCI Dictionary of Cancer Terms)
--     * Slot: country Description: The country where the subject was enrolled in their study.
--     * Slot: race_identification_source Description: Who supplied the value in RACE?
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
-- # Class: "Subject" Description: ""
--     * Slot: id Description: 
--     * Slot: honest_broker_subject_id Description: The identifier assigned to the subject by the honest broker--an individual, organization or system acting for, or on behalf of, a covered entity to collect and provide health information to research investigators in such a manner whereby it would not be reasonably possible for the investigators or others to identify the corresponding patients-subjects directly or indirectly. The honest broker cannot be one of the investigators. The information provided to the investigators by the honest broker may incorporate linkage codes to permit information collation and/or subsequent inquiries (i.e., a "re-identification code"), however the information linking this re-identification code to the patient's identity must be retained by the honest broker and subsequent inquiries are conducted through the honest broker. (Source: NCI Thersaurus)
--     * Slot: consortium Description: The consortium under which this data is being contributed to the Pediatric Cancer Data Commons.
--     * Slot: data_contributor_id Description: An identifier assigned to a data contributor.
--     * Slot: study_id Description: A sequence of characters used to identify, name, or characterize the study.
--     * Slot: age_at_enrollment Description: The age (in days) when the subject enrolled in the study. 
--     * Slot: treatment_arm Description: A specific treatment plan within a clinical trial that describes the activities a subject will be involved in as he or she progresses through the study.
--     * Slot: enrolled_status Description: This variable indicates if the subject was enrolled in the study, or if the subject was not enrolled in the study but received treatment per the study's protocol.
--     * Slot: data_source Description: The nature of the investigation or the investigational use for which clinical study is being done.
--     * Slot: year_at_enrollment Description: The year at which a subject enrolled in a study.
--     * Slot: study_phase Description: The phase of the clinical trial that the subject was enrolled in for the collection of this data.
--     * Slot: study_type Description: The nature of the investigation or the investigational use for which clinical study is being done.
--     * Slot: efs_censor_status Description: The event free survival censor status
--     * Slot: age_at_censor_status Description: Age (in days) of the subject at the time of the CENSOR_STATUS
--     * Slot: randomized_status Description: The allocation of individuals to groups by chance, especially in order to control the variables in an experiment.
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: persons_id Description: 
-- # Class: "Time Period" Description: ""
--     * Slot: id Description: 
--     * Slot: time_period_type Description: The type of time period being reported.
--     * Slot: disease_phase Description: The phase of the cancer treatment process during which relevant observations were recorded. This variable is used across domains to frame the timing of these longitudinal observations and reduce the number of redundant variables needed to report similar concepts (see "Disease Phase Timing and Course Table" in the documentation for additional guidance).
--     * Slot: course Description: The protocol treatment "course" during which relevant observations were recorded. This variable is used across domains to frame the timing of these longitudinal observations and reduce the number of redundant variables needed to report similar concepts (see "Disease Phase Timing and Course Table" in the documentation for additional guidance).
--     * Slot: time_period_number Description: This variable indicates the ordinal numbering of time periods of the same TIME_PERIOD_TYPE within its various subgroups (e.g., Relapse 1, Relapse 2, Relapse 3, etc.). The observations across domains can therefore be organized longitudinally without the need for specific dates.
--     * Slot: year_at_start Description: The year at the start of the indicated time period
--     * Slot: age_at_start Description: The age (in days) of the patient at the start of the reported time period. 
--     * Slot: age_at_end Description: The age (in days) of the patient at the end of the reported time period. 
--     * Slot: course_other Description: Specify the "Other" COURSE
--     * Slot: age_at_course_anc_500 Description: The age (in days) of the subject when the subject's neutrophil count exceeded 500 (ANC/mm3)
--     * Slot: age_at_txassign Description: Age in Days at Treatment Assignment
--     * Slot: age_precision Description: The precision of the age provided in AGE_AT_DISEASE_PHASE
--     * Slot: exam_type Description: The type of exam during which data for the patient was collected.
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: time_periods_id Description: 
--     * Slot: subjects_id Description: 
-- # Class: "Off Protocol Therapy Or Study" Description: ""
--     * Slot: id Description: 
--     * Slot: age_off Description: The age (in days) when the subject went off of the protocol therapy or study.
--     * Slot: off_type Description: The code used to designate that the subject went off therapy or off the study.
--     * Slot: reason_off Description: The reason a subject went off the therapy or study.
--     * Slot: reason_off_other Description: Specify the "Other" REASON_OFF
--     * Slot: another_study Description: Did the subject enroll in another study after they went off of the study indicated by OFF_TYPE?
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: time_periods_id Description: 
--     * Slot: subjects_id Description: 
-- # Class: "Medical History" Description: ""
--     * Slot: id Description: 
--     * Slot: condition Description: Relevant condition from the subject's medical history.
--     * Slot: condition_other Description: Specify the "Other" CONDITION
--     * Slot: age_at_condition Description: 
--     * Slot: condition_type Description: The type of relevant condition from the subject's medical history.
--     * Slot: diagnosis_basis Description: The basis for diagnosis of the CPS. 
--     * Slot: condition_status Description: Was this condition observed in the subject?
--     * Slot: assisted_conception Description: If the subject was conceived through assisted conception, what was the type of assisted conception?
--     * Slot: developmental_delay Description: Did the subject experience developmental delay?
--     * Slot: developmental_delay_type Description: What was the type of developmental delay?
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: subjects_id Description: 
-- # Class: "Survival Characteristics" Description: ""
--     * Slot: id Description: 
--     * Slot: age_at_lkss Description: The age (in days) when the last known survival status of the subject was captured.
--     * Slot: lkss Description: The last known survival status of the subject.
--     * Slot: lkss_with_disease Description: Did the subject still have measurable/evaluable disease at the LKSS?
--     * Slot: age_lost_to_follow_up Description: The age (in days) when the subject was lost to follow-up.
--     * Slot: cause_of_death Description: The circumstance or condition that results in the death of a living being.
--     * Slot: cause_of_death_other Description: Specify the "Other" CAUSE_OF_DEATH
--     * Slot: trm_type Description: If the mortality is treatment related, what type of treatment was involved?
--     * Slot: trm_type_other Description: Specify the "Other" TRM_TYPE
--     * Slot: cause_of_death_detail Description: The more granular reason for the CAUSE_OF_DEATH of the subject.
--     * Slot: cause_of_death_detail_other Description: Specify the "Other" CAUSE_OF_DEATH_DETAIL
--     * Slot: cause_of_death_ranking Description: Assigning a weighted relevance to the cause of death.
--     * Slot: course_timepoint Description: This variable gives more precise granularity to when an observation occured during the period of the indicated "Course" TIME_PERIOD
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: time_periods_id Description: 
--     * Slot: subjects_id Description: 
-- # Class: "Family Medical History" Description: ""
--     * Slot: id Description: 
--     * Slot: relation Description: What kind of relation is this relative who has had a relevant medical condition?
--     * Slot: relation_other Description: Specify the "Other" RELATION
--     * Slot: shared_predisposition Description: 
--     * Slot: relative_honest_broker_id Description: 
--     * Slot: prior_cancer Description: Does the subject have a relative who has a medical history that includes cancer?
--     * Slot: prior_cancer_type Description: The type of prior cancer from the medical history of the relative of the subject.
--     * Slot: prior_cancer_laterality Description: The laterality of the prior cancer of the relative of the subject.
--     * Slot: lkss_of_relative Description: The last known survival status of the relative of the subject with the prior cancer.
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: subjects_id Description: 
-- # Class: "Vitals And Anthropometrics" Description: ""
--     * Slot: id Description: 
--     * Slot: age_at_measurement Description: The age (in days) of the subject when the vitals measurement was taken.
--     * Slot: measurement_type Description: The type of vital sign or anthropomorphic measurement being recorded
--     * Slot: measurement_text Description: The vital sign or anthropomorphic measurement being recorded (non-numeric)
--     * Slot: measurement_numeric Description: The vital sign or anthropomorphic measurement being recorded (numeric)
--     * Slot: measurement_unit Description: The units used for the vital sign or anthropomorphic measurement being recorded (numeric)
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: time_periods_id Description: 
--     * Slot: subjects_id Description: 
-- # Class: "Laboratory Test" Description: ""
--     * Slot: id Description: 
--     * Slot: age_at_lab Description: The age (in days) of the subject at the time of the laboratory test.
--     * Slot: category Description: The category of laboratory test performed on the subject.
--     * Slot: test Description: A medical procedure that involves testing a sample of blood, urine, or other substance from the body. Laboratory tests can help determine a diagnosis, plan treatment, check to see if treatment is working, or monitor the disease over time Source: NCI Dictionary of Cancer Terms)
--     * Slot: specimen Description: The type of specimen analyzed.
--     * Slot: specimen_other Description: Specify the "Other" SPECIMEN
--     * Slot: method Description: A systematic course of action that is performed in order to complete a laboratory test.
--     * Slot: method_other Description: Specify the "Other" LAB_METHOD
--     * Slot: result_text Description: The string/text result of the laboratory test.
--     * Slot: result_numeric Description: The numeric result of the laboratory test.
--     * Slot: result_unit Description: The units used for the numeric result of the laboratory test.
--     * Slot: traumatic_tap Description: Contamination of a cerebrospinal fluid sample by red blood cells greater than 10/mm3.
--     * Slot: bm_morphology Description: The morphology of bone marrow blasts.
--     * Slot: result Description: The text result of the laboratory test.
--     * Slot: threshold_level Description: The point at which a psychological or physiological effect begins to be produced.
--     * Slot: threshold_high Description: The maximum level that must be exceeded for a certain reaction to occur or be manifested.
--     * Slot: thredhold_low Description: The minimum level that must be attained for a certain reaction to occur or be manifested.
--     * Slot: seq_method Description: Quantitative Sequencing Method
--     * Slot: threshold_low Description: The minimum level that must be attained for a certain reaction to occur or be manifested.
--     * Slot: pmid_ref Description: A globally unique identifier for a biomedical article, as assigned by PubMed.
--     * Slot: malignant_cells Description: A term used to describe cancer. Malignant cells grow in an uncontrolled way and can invade nearby tissues and spread to other parts of the body through the blood and lymph system (Source: NCI Dictionary of Cancer Terms)
--     * Slot: course_timepoint Description: This variable gives more precise granularity to when an observation occured during the period of the indicated "Course" TIME_PERIOD
--     * Slot: test_other Description: Specify the "Other" LAB_TEST
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: time_periods_id Description: 
--     * Slot: subjects_id Description: 
-- # Class: "Genetic Analysis" Description: ""
--     * Slot: id Description: 
--     * Slot: age_at_genetic_analysis Description: The age (in days) of the subject at the time of this analysis.
--     * Slot: method Description: A systematic course of action that is performed in order to complete a laboratory test.
--     * Slot: specimen Description: The type of specimen analyzed.
--     * Slot: common_name Description: The non-standardized name of the mutation represented by this observation.
--     * Slot: karyotype_status Description: The status of the subject's karyotype.
--     * Slot: status Description: Is this mutation/abnormality present in this subject?
--     * Slot: iscn Description: If this mutation is described by the structure of the resulting chromosomes, this is its representation in ISCN nomenclature.
--     * Slot: total_chromosomes Description: The number of chromosomes detected on the karyotype through which this abnormality was detected.
--     * Slot: chromosome Description: A structure found in cells that is comprised of a strand of linearized double-stranded DNA plus proteins that package the DNA in a condensed coil form and regulate chromosomal function.
--     * Slot: gene Description: A gene targeted for mutation analysis, identified in HUGO Gene Nomenclature Committee (HGNC) notation.
--     * Slot: gene2 Description: This should be used for mutations that span two gene locations (fusion, translocation, inversion, etc.). The gene name should be identified in HUGO Gene Nomenclature Committee (HGNC) notation.
--     * Slot: variation_type Description: The type of variation detected by this genetic analysis.
--     * Slot: variation_type_other Description: Specify the "Other" MUTATION_TYPE
--     * Slot: copy_number_variation Description: If there was a change in the number of gene copies, this variable specifies the type of change.
--     * Slot: copy_number Description: The number of gene copies resulting from this mutation.
--     * Slot: hgvs_coding Description: If this mutation is described at the sequence/chromosome level, this is its representation in HGVS nomenclature (cHGVS).
--     * Slot: hgvs_protein Description: If this mutation is described at the translational product level, this is its representation in HGVS nomenclature (pHGVS)
--     * Slot: dna_index_numeric Description: The ratio of the DNA content or chromosome number in a tumor sample compared to that in a normal sample.
--     * Slot: method_other Description: Specify the "Other" LAB_METHOD
--     * Slot: independent_aberations Description: The total number of aberrations / mutations / abnormalities detected on the karyotype through which this abnormality was detected.
--     * Slot: cells_in_metaphase Description: The number of cells in the sample that were arrested in the metaphase stage of the cell cycle and used for the karyotype through which this abnormality was detected.
--     * Slot: common_name_other Description: Specify the "Other" COMMON_NAME
--     * Slot: mutant_allele_fraction Description: A measure of the percentage of mutant alleles within the totality of alleles in any given sample
--     * Slot: genomic_source_class Description: The genomic class of the specimen being analyzed, for example, germline for inherited genome and somatic for cancer genome.
--     * Slot: expression_consequence Description: 
--     * Slot: chromosomal_consequence Description: Chromosomal abnormalities can have many different effects, depending on the specific abnormality. For example, an extra copy of chromosome 21 causes Down syndrome (trisomy 21). Chromosomal abnormalities can also cause miscarriage, disease, or problems in growth or development.
--     * Slot: allelic_state Description: The level of occurrence of a single DNA Marker within a set of chromosomes. Heterozygous indicates the DNA Marker is only present in one of the two genes contained in homologous chromosomes. Homozygous indicates the DNA Marker is present in both genes contained in homologous chromosomes. Hemizygous indicates the DNA Marker exists in the only single copy of a gene in a non-homologous chromosome (The male X and Y chromosome are non-homologous). Hemiplasmic indicates that the DNA Marker is present in some but not all of the copies of mitochondrial DNA. Homoplasmic indicates that the DNA Maker is present in all of the copies of mitochondrial DNA. (Source: LOINC)
--     * Slot: allelic_frequency Description: The incidence of this mutation in the tumor (%).
--     * Slot: external_ref_id Description: An ID to an external knowledge base that holds additional information about this genetic variant.
--     * Slot: external_ref_id_system Description: The name of the external knowledge base from which the EXTERNAL_REF_ID is drawn.
--     * Slot: mosaicism_percent Description: The numeric level of mosaicism in this subject.
--     * Slot: variation_effect Description: 
--     * Slot: inheritance_pattern Description: 
--     * Slot: parental_status Description: 
--     * Slot: hgvs_coding_transcript Description: This is the transcript used in the HGVS expression for this mutation.
--     * Slot: hgvs_protein_transcript Description: 
--     * Slot: reported_significance Description: The reported ACMG clinical significance of this genetic variation
--     * Slot: associated_condition Description: A condition associated with the reported genetic mutation 
--     * Slot: associated_condition_other Description: Specify the "Other" ASSOCIATED_CONDITION
--     * Slot: review_source Description: The type of assessment that was used to review.
--     * Slot: tumor_classification Description: The classification of a tumor based primarily on histopathological characteristics.
--     * Slot: course_timepoint Description: This variable gives more precise granularity to when an observation occured during the period of the indicated "Course" TIME_PERIOD
--     * Slot: specimen_other Description: Specify the "Other" SPECIMEN
--     * Slot: biological_analyte Description: A biological substance of interest that needs detection.
--     * Slot: biological_analyte_other Description: Specify the "Other" BIOLOGICAL_ANALYTE
--     * Slot: source_pct Description: Percent of tumor cells in the sample (categorical)
--     * Slot: source_pct_numeric Description: Percent of tumor cells in the sample (numeric)
--     * Slot: tkd_involvement Description: 
--     * Slot: maf Description: 
--     * Slot: maf_numeric Description: A measure of the percentage of mutant alleles within the totality of alleles in any given sample
--     * Slot: clonal_status Description: 
--     * Slot: dna_index Description: The categorical result of the DNA index for this subject
--     * Slot: cytodifferentiation Description: Cytodifferentiation Score
--     * Slot: mitotic_rate Description: Mitoses Count
--     * Slot: mutated_allele_frequency Description: The incidence of this mutation in the tumor (%).
--     * Slot: cascade_testing Description: 
--     * Slot: alt_status Description: Activitation of the Alternative Lengthening of Telomeres (ALT) pathway.
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: time_periods_id Description: 
--     * Slot: subjects_id Description: 
-- # Class: "Function Test" Description: ""
--     * Slot: id Description: 
--     * Slot: age_at_function_test Description: The age (in days) of the subject at the time of the function test.
--     * Slot: test Description: A medical procedure that involves testing a sample of blood, urine, or other substance from the body. Laboratory tests can help determine a diagnosis, plan treatment, check to see if treatment is working, or monitor the disease over time Source: NCI Dictionary of Cancer Terms)
--     * Slot: measurement_type Description: The type of vital sign or anthropomorphic measurement being recorded
--     * Slot: measurement_text Description: The vital sign or anthropomorphic measurement being recorded (non-numeric)
--     * Slot: measurement_numeric Description: The vital sign or anthropomorphic measurement being recorded (numeric)
--     * Slot: measurement_unit Description: The units used for the vital sign or anthropomorphic measurement being recorded (numeric)
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: time_periods_id Description: 
--     * Slot: subjects_id Description: 
-- # Class: "Immunohistochemistry" Description: ""
--     * Slot: id Description: 
--     * Slot: age_at_ihc Description: The age (in days) of the subject at the immunohistochemical test.
--     * Slot: review_source Description: The type of assessment that was used to review.
--     * Slot: test Description: A medical procedure that involves testing a sample of blood, urine, or other substance from the body. Laboratory tests can help determine a diagnosis, plan treatment, check to see if treatment is working, or monitor the disease over time Source: NCI Dictionary of Cancer Terms)
--     * Slot: result Description: The text result of the laboratory test.
--     * Slot: result_text Description: The string/text result of the laboratory test.
--     * Slot: result_numeric Description: The numeric result of the laboratory test.
--     * Slot: specimen Description: The type of specimen analyzed.
--     * Slot: result_unit Description: The units used for the numeric result of the laboratory test.
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: time_periods_id Description: 
--     * Slot: subjects_id Description: 
-- # Class: "Imaging" Description: ""
--     * Slot: id Description: 
--     * Slot: age_at_imaging Description: The age (in days) of the subject at the time of imaging.
--     * Slot: method Description: A systematic course of action that is performed in order to complete a laboratory test.
--     * Slot: result Description: The text result of the laboratory test.
--     * Slot: deauville_score Description: A 5 point scale devised to assess the response to treatment of Hodgkin and Aggressive Non-Hodgkin Lymphoma.
--     * Slot: qpet_score Description: A methodology that provides semi-automatic quantification for interim FDG-PET response in lymphoma. It extends the ordinal Deauville score to a continuous scale.
--     * Slot: finding Description: The result of an evaluation technique using a visual display of structural or functional patterns of organs or tissues that is performed to determine the presence, absence, or degree of a condition.
--     * Slot: finding_other Description: Specify the "Other" IMAGING_FINDING
--     * Slot: finding_site Description: The site in which the results of the imaging finding was located. 
--     * Slot: finding_site_other Description: Specify the "Other" IMAGING_FINDING_SITE
--     * Slot: bone_marrow Description: An indication of whether malignant cells are present in a bone marrow sample.
--     * Slot: csf_result Description: The results of cerebrospinal fluid laboratory tests.
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: time_periods_id Description: 
--     * Slot: subjects_id Description: 
-- # Class: "Histology" Description: ""
--     * Slot: id Description: 
--     * Slot: age_at_hist_assessment Description: The age (in days) of the subject at the time of this histological assessment.
--     * Slot: morph_code Description: The code for the morphology of the subsequent tumor
--     * Slot: morph_code_system Description: The coding system for MORPH_CODE
--     * Slot: morph_code_system_version Description: The version of the coding system indicated in MORPH_CODE_SYSTEM
--     * Slot: top_code Description: The topography code describes the site of origin of the neoplasm.
--     * Slot: top_code_system Description: The coding system for the code used in TOP_CODE
--     * Slot: top_code_system_version Description: The version of the coding system indicated in TOP_CODE_SYSTEM
--     * Slot: all_type Description: Leukemia with an acute onset, characterized by the presence of lymphoblasts in the bone marrow and the peripheral blood. It includes the acute B lymphoblastic leukemia and acute T lymphoblastic leukemia.
--     * Slot: fab_type Description: A classification system for acute myeloid leukemias, acute lymphoblastic leukemias, and myelodysplastic syndromes. It is based on the morphologic and cytochemical evaluation of bone marrow and peripheral blood smears.
--     * Slot: who_aml Description: A classification of acute myeloid leukemia tumors by the World Health Organization (WHO).
--     * Slot: mpal Description: An acute leukemia of ambiguous lineage. It is characterized by the presence of either separate populations of blasts of more than one lineage, or one population of blasts co-expressing markers of more than one lineage.
--     * Slot: mlds Description: Acute myeloid leukemia or myelodysplastic syndrome occurring in children with Down syndrome. The acute myeloid leukemia is usually an acute megakaryoblastic leukemia, and is associated with GATA1 gene mutation.
--     * Slot: tam Description: A myeloid proliferation occurring in newborns with Down syndrome. It is clinically and morphologically indistinguishable from acute myeloid leukemia and is associated with GATA1 mutations. The blasts display morphologic and immunophenotypic features of megakaryocytic lineage. In the majority of patients the myeloid proliferation undergoes spontaneous remission.
--     * Slot: secondary_aml Description: Secondary Acute Myeloid Leukemia
--     * Slot: histology Description: The study of tissues and cells under a microscope (Source: NCI Dictionary of Cancer Terms)
--     * Slot: molecular_classification Description: 
--     * Slot: molecular_classification_other Description: Specify the "Other" MOLECULAR_CLASSIFICATION
--     * Slot: determination_source Description: 
--     * Slot: method Description: A systematic course of action that is performed in order to complete a laboratory test.
--     * Slot: morph_code_txt Description: The display text for MORPH_CODE 
--     * Slot: review_source Description: The type of assessment that was used to review.
--     * Slot: histology_result_text Description: 
--     * Slot: histology_result_numeric Description: The numeric value for the histology result.
--     * Slot: histology_result_unit Description: The unit being used as the measurement for the histology test.
--     * Slot: histology_grade Description: A description of a tumor based on how abnormal the cancer cells and tissue look under a microscope and how quickly the cancer cells are likely to grow and spread
--     * Slot: mature_glial_implants Description: A nodule of mature glial tissue that develops in the peritoneum. It is usually accompanied by mature or immature ovarian teratoma.
--     * Slot: somatic_malignancy_type Description: A malignant non-germ cell component that typically develops secondarily within a germ cell tumor. The malignant cellular component is usually sarcomatous or carcinomatous.
--     * Slot: somatic_malignancy_type_other Description: Specify the "Other" SOMATIC_MALIGNANCY_TYPE
--     * Slot: course_timepoint Description: This variable gives more precise granularity to when an observation occured during the period of the indicated "Course" TIME_PERIOD
--     * Slot: revised_inpc Description: Revised INPC Prognostic Group (2003)
--     * Slot: mki Description: MKI (Revised INPC)
--     * Slot: histology_other Description: Specify the "Other" HISTOLOGY
--     * Slot: tumor_site Description: 
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: time_periods_id Description: 
--     * Slot: subjects_id Description: 
-- # Class: "Disease Characteristics" Description: ""
--     * Slot: id Description: 
--     * Slot: disease_site Description: Disease Involvement Site
--     * Slot: detection_method_other Description: Specify the "Other" DETECTION_METHOD
--     * Slot: cns_disease_status Description: CNS Involvement Status
--     * Slot: prior_steroids_week Description: Received Steroids within One Week Prior to Diagnosis
--     * Slot: prior_steroids_month Description: Received Steroids within One Month Prior to Diagnosis
--     * Slot: bulk_med_mass Description: When the maximum width of a mass is equal or greater than one-third of the internal transverse diameter of the thorax at the level of T5/6 on a PA CXR. Bulk at an alternate site is defined as any mass measuring 10 cm or more by any imaging study.
--     * Slot: disease_site_other Description: Specify the "Other" DISEASE_SITE
--     * Slot: detection_method Description: Disease Involvement Detection Method
--     * Slot: myeloid_sarcoma Description: A rare type of cancer that is made up of myeloblasts (a type of immature white blood cell) and forms outside the bone marrow and blood. The tumor cells may look green when viewed under a microscope. Myeloid sarcomas can occur anywhere in the body. They most commonly occur in people with acute myeloid leukemia or a myeloproliferative disorder. Also called chloroma, extramedullary myeloid tumor, and granulocytic sarcoma. (Source: NCI Dictionary of Cancer Terms)
--     * Slot: myeloid_sarcoma_site Description: The site of the extramedullary myeloid sarcoma.
--     * Slot: myeloid_sarcoma_site_other Description: Specify the "Other" MYELOID_SARCOMA_SITE
--     * Slot: age_at_disease_characteristic Description: 
--     * Slot: performance_score Description: A standard way of measuring the ability of cancer patients to perform ordinary tasks. Scores range from 0 to 100. A higher score means the patient is better able to carry out daily activities. May be used to determine a patient's prognosis, to measure changes in a patient’s ability to function, or to decide if a patient could be included in a clinical trial. (Source: NCI Dictionary of Cancer Terms)
--     * Slot: performance_score_system Description: The performance scale used.
--     * Slot: gpoh_score Description: A measure of an individual's overall performance status or ability to perform their activities of daily living.
--     * Slot: risk_group_system Description: MaGIC Risk Group
--     * Slot: risk_group Description: 
--     * Slot: gts_treatment Description: Growing Teratoma Syndrome treatment type
--     * Slot: bulk_disease Description: 
--     * Slot: bulk_nodal_aggregate Description: 
--     * Slot: med_ratio Description: Mediastinal Ratio
--     * Slot: fever Description: An increase in body temperature above normal (98.6 degrees F), usually caused by disease. (Source: NCI Dictionary of Cancer Terms)
--     * Slot: night_sweats Description: Episodes of excessive sweating that occur during sleep. Night sweats can be severe and soak a person’s bedclothes and bed sheets, which may cause the person to wake up. Night sweats are a common symptom of menopause. They may also be caused by illness or medical conditions, such as infection, cancer, low blood sugar, hormone disorders, and neurologic conditions. They may also be a side effect of certain medicines, cancer treatment, too much caffeine or alcohol, or tobacco or drug use. (Source: NCI Dictionary of Cancer Terms)
--     * Slot: weight_loss Description: Surgery done to help people who are obese lose weight. There are different types of weight loss surgery, and each type changes the way the digestive system works. Some types make the stomach smaller, which decreases the amount of food that it can hold so the person feels full sooner and eats less. Other types make changes to the stomach and the small intestine, which decreases the nutrients and calories that are absorbed from food. Weight loss surgery can improve many obesity-related health problems, such as diabetes, high blood pressure, unhealthy cholesterol levels, sleep apnea, and knee, hip, or other body pain. Having weight loss surgery may also decrease the risk of some cancers, including endometrial cancer. Also called bariatric surgery. (Source: NCI Dictionary of Cancer Terms)
--     * Slot: nodular_splenic Description: Nodular Splenic Involvement
--     * Slot: course_timepoint Description: This variable gives more precise granularity to when an observation occured during the period of the indicated "Course" TIME_PERIOD
--     * Slot: initial_treatment_category Description: The category of initial treatment that the patient receive for their disease.
--     * Slot: tumor_site Description: 
--     * Slot: evaluator Description: 
--     * Slot: evaluator_other Description: Specify the "Other" PRESENTATION_EVALUATOR
--     * Slot: presentation_symptoms Description: 
--     * Slot: presentation_symptoms_other Description: Specify the "Other" PRESENTATION_SYMPTOMS
--     * Slot: clinical_signs Description: Clinical Related Symptoms
--     * Slot: clinical_signs_other Description: 
--     * Slot: suspected_referring_diagnosis Description: Suspected Referring Diagnosis
--     * Slot: suspected_diagnosis_other Description: Specify the "Other" SUSPECTED_DIAGNOSIS
--     * Slot: visual_acuity_technique Description: Visual Acuity Technique
--     * Slot: visual_acuity_result Description: Visual Acuity Result
--     * Slot: visual_acuity_result_numeric Description: Visual Acuity Result Numeric
--     * Slot: visual_acuity_notation Description: Visual Acuity Notation
--     * Slot: anterior_segment_exam Description: Anterior Segment Exam
--     * Slot: anterior_segment_details Description: Anterior Segment Details
--     * Slot: anterior_segment_details_other Description: Specify the "Other" ANTERIOR_SEGMENT_DETAILS
--     * Slot: intraocular_pressure Description: Intraocular Pressure
--     * Slot: intraocular_pressure_unit Description: Intraocular Pressure Unit
--     * Slot: retinal_detachment Description: Retinal Detachment Present and Number of Quadrants
--     * Slot: advanced_disease_signs Description: Other Clinical Signs of Advanced Disease
--     * Slot: advanced_disease_signs_other Description: Specify the "Other" ADVANCED_DISEASE_SIGNS
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: time_periods_id Description: 
--     * Slot: subjects_id Description: 
-- # Class: "Tumor Assessment" Description: ""
--     * Slot: id Description: 
--     * Slot: age_at_assessment Description: The age (in days) of the subject at the time of this tumor assessment.
--     * Slot: detection_method Description: Disease Involvement Detection Method
--     * Slot: review_source Description: The type of assessment that was used to review.
--     * Slot: mri_sequence Description: 
--     * Slot: tumor_presentation Description: 
--     * Slot: classification Description: The classification of a tumor based primarily on histopathological characteristics.
--     * Slot: site Description: Specifies the anatomic site of a localized pathological or traumatic structural change, damage, deformity, or discontinuity of tissue, organ, or body part.
--     * Slot: site_other Description: Specify the "Other" TUMOR_SITE
--     * Slot: age_at_tumor_assessment Description: The age (in days) of the subject at the time of this tumor assessment.
--     * Slot: status Description: Is this mutation/abnormality present in this subject?
--     * Slot: assessment_reason Description: 
--     * Slot: morph_code Description: The code for the morphology of the subsequent tumor
--     * Slot: morph_code_txt Description: The display text for MORPH_CODE 
--     * Slot: morph_code_system Description: The coding system for MORPH_CODE
--     * Slot: morph_code_system_version Description: The version of the coding system indicated in MORPH_CODE_SYSTEM
--     * Slot: top_code Description: The topography code describes the site of origin of the neoplasm.
--     * Slot: top_code_txt Description: The display text for TOP_CODE 
--     * Slot: top_code_system Description: The coding system for the code used in TOP_CODE
--     * Slot: top_code_system_version Description: The version of the coding system indicated in TOP_CODE_SYSTEM
--     * Slot: longest_diam_dim1 Description: Longest Diameter of Tumor Dimension 1 (cm)
--     * Slot: longest_diam_dim2 Description: Longest Diameter of Tumor Dimension 2 (cm)
--     * Slot: longest_diam_dim3 Description: Longest Diameter of Tumor Dimension 3 (cm)
--     * Slot: tumor_submitter_id Description: 
--     * Slot: primary_tumor_submitter_id Description: 
--     * Slot: tissue_type Description: A piece of tissue removed from an organism for examination, analysis, or propagation.
--     * Slot: classification_status Description: The status of the tumor classification whether it was completed or not.
--     * Slot: multiplicity Description: This variable indicates if the recorded observation is detailing a single tumor or multiple tumors at a given site.
--     * Slot: tumor_size Description: The tumor size of the largest tumor.
--     * Slot: tumor_volume Description: The size of a cancer measured by the amount of space taken up by the tumor. For example, the tumor volume of prostate cancer is the percentage of the prostate taken up by the tumor.
--     * Slot: estimated_volume Description: Estimated Volume (mL)
--     * Slot: laterality Description: A qualifier for the side of the body the tumor findings assessment is performed.
--     * Slot: fracture Description: Fracture at Primary Site
--     * Slot: skip_tumor Description: A benign or malignant pathologic process which is patchy and skips areas which are normal (uninvolved by the pathologic process).
--     * Slot: ipsilateral_nodules Description: A metastatic tumor nodule located in the same side of the organ in which the primary tumor occurred.
--     * Slot: joint_involvement Description: A finding indicating the spread of cancer to a joint.
--     * Slot: site_within_bone Description: The anatomic site within the bone.
--     * Slot: nodal_involvement Description: Regional Lymph Node Involvement
--     * Slot: nodal_site Description: The anatomic site of a tumor node.
--     * Slot: extension_tumor_type Description: 
--     * Slot: detection_method_other Description: Specify the "Other" DETECTION_METHOD
--     * Slot: e_extension_site Description: The anatomic location outside of the lymph nodes into which a disease lesion has directly spread.
--     * Slot: e_extension_site_other Description: 
--     * Slot: diam_type Description: The orientation of the diameters provided
--     * Slot: bulky_disease Description: Is this nodal mass big enough to be classified as bulky disease?
--     * Slot: effusion Description: 
--     * Slot: effusion_type Description: 
--     * Slot: response Description: A qualitative or quantitative measurement of the response of a target lesion(s) to the therapy.
--     * Slot: pct_change Description: The percentage of change in a particular lesion.
--     * Slot: course_timepoint Description: This variable gives more precise granularity to when an observation occured during the period of the indicated "Course" TIME_PERIOD
--     * Slot: tumor_type Description: 
--     * Slot: mibg_avidity Description: 
--     * Slot: invasiveness_status Description: Tumor Invasiveness
--     * Slot: depth Description: The depth of the tumor.
--     * Slot: skip_met_involvement Description: A question about the areas involved in the skip metastasis.
--     * Slot: fracture_site Description: If the anatomical site of the tumor is within a bone, is that bone fractured?
--     * Slot: massive_choroidal_extension Description: 
--     * Slot: visual_discrete_tumors Description: Visual Disrete Tumors
--     * Slot: tumor_number Description: The number of tumors found.
--     * Slot: tumor_from_fovea Description: Tumor Distance from Fovea of the Closest Tumor
--     * Slot: tumor_from_optic_nerve Description: Tumor Distance from Optic Nerve of the Closest Tumor
--     * Slot: fluid_from_tumor Description: Fluid from Tumor Base
--     * Slot: seeds_present Description: Retinoblastoma Seeds Present
--     * Slot: seeds_pattern Description: Retinoblastoma Seeds Pattern
--     * Slot: seeds_status Description: Retinoblastoma Seeds Status
--     * Slot: seeds_classification Description: Retinoblastoma Seeds Classification
--     * Slot: invasiveness Description: Tumor Invasiveness
--     * Slot: nodal_determination Description: Determination of Regional Lymph Node Involvement
--     * Slot: nodal_determination_source Description: The source of the determination of regional lymph node involvement. 
--     * Slot: parameningeal_extension Description: 
--     * Slot: necrosis_status Description: Indicates the presence or absence of necrosis in the tumor.
--     * Slot: necrosis_pct_numeric Description: The numeric percentage of necrosis found in the tumor.
--     * Slot: anaplasia_status Description: Indicates the presence or absence of anaplasia in the tumor.
--     * Slot: anaplasia_type Description: describes the type or extent of anaplasia found during a histopathologic exam.
--     * Slot: anaplasia_pct_numeric Description: The numeric percentage of anaplasia found in the tumor.
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: time_periods_id Description: 
--     * Slot: subjects_id Description: 
-- # Class: "Staging" Description: ""
--     * Slot: id Description: 
--     * Slot: age_at_staging Description: The age (in days) of the subject at the time of this staging assessment.
--     * Slot: stage_system Description: A systematic method for clinicopathologic evaluation of tumors.
--     * Slot: stage Description: The extent of a cancer in the body. Staging is usually based on the size of the tumor, whether lymph nodes contain cancer, and whether the cancer has spread from the original site to other parts of the body (Source: NCI Dictionary of Cancer Terms)
--     * Slot: stage_other Description: Specify the "Other" STAGE
--     * Slot: ann_arbor_mod_ab Description: HL Ann Arbor A vs B Staging Designation
--     * Slot: ann_arbor_mod_e Description: HL Ann Arbor E Staging Designation
--     * Slot: ann_arbor_mod_s Description: HL Ann Arbor S Staging Designation
--     * Slot: course_timepoint Description: This variable gives more precise granularity to when an observation occured during the period of the indicated "Course" TIME_PERIOD
--     * Slot: site Description: Specifies the anatomic site of a localized pathological or traumatic structural change, damage, deformity, or discontinuity of tissue, organ, or body part.
--     * Slot: stage_system_category Description: 
--     * Slot: stage_type Description: 
--     * Slot: h_stage Description: 
--     * Slot: group_system Description: 
--     * Slot: group Description: 
--     * Slot: tnm_finding Description: 
--     * Slot: irs_group Description: IRS Surgical-Pathologic Grouping System
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: time_periods_id Description: 
--     * Slot: subjects_id Description: 
-- # Class: "Radiation Therapy" Description: ""
--     * Slot: id Description: 
--     * Slot: age_at_rt_start Description: The age (in days) of the subject at the start of this radiation treatment.
--     * Slot: age_at_rt_end Description: The age (in days) of the subject at the end of this radiation treatment.
--     * Slot: protocol_radiation_therapy Description: Was this radiation therapy administration part of the treatment protocol?
--     * Slot: non_protocol_timing Description: If a non-protocol radiation therapy, when was this radiation therapy administered?
--     * Slot: site Description: Specifies the anatomic site of a localized pathological or traumatic structural change, damage, deformity, or discontinuity of tissue, organ, or body part.
--     * Slot: site_other Description: Specify the "Other" TUMOR_SITE
--     * Slot: total_dose Description: The total radiation dose administered.
--     * Slot: total_dose_unit Description: A unit of measurement of the dose of radiation received or absorbed.
--     * Slot: technique Description: Treatment of a disease by means of exposure of the target or the whole body to radiation. Radiation therapy is often used as part of curative therapy and occasionally as a component of palliative treatment for cancer. Other uses include total body irradiation prior to transplantation.
--     * Slot: energy_type Description: Treatment of a disease by means of exposure of the target or the whole body to radiation. Radiation therapy is often used as part of curative therapy and occasionally as a component of palliative treatment for cancer. Other uses include total body irradiation prior to transplantation.
--     * Slot: margin Description: 
--     * Slot: rt_data_source Description: Whether radiation data was obtained from a protocol-defined dose, or 
--     * Slot: fraction_dose Description: 
--     * Slot: fraction_dose_unit Description: A unit of measurement of the dose of radiation received or absorbed.
--     * Slot: num_fraction Description: The number of divided radiation doses received per day.
--     * Slot: target_volume Description: The intended target volume for this radiation therapy.
--     * Slot: boost Description: One or more extra radiation treatments targeted at the tumor bed, given after the regular sessions of radiation are complete.
--     * Slot: boost_dose Description: The dose amount of the radiation boost.
--     * Slot: boost_unit Description: 
--     * Slot: boost_target_volume Description: 
--     * Slot: classification Description: The classification of a tumor based primarily on histopathological characteristics.
--     * Slot: tissue_type Description: A piece of tissue removed from an organism for examination, analysis, or propagation.
--     * Slot: laterality Description: A qualifier for the side of the body the tumor findings assessment is performed.
--     * Slot: technique_other Description: Specify the "Other" TECHNIQUE
--     * Slot: transposition_organ Description: A procedure to move organs out of the range of the damaging effects of radiation.
--     * Slot: boost_dose_unit Description: A unit of measurement of the dose of radiation received or absorbed.
--     * Slot: energy_type_other Description: Specify the "Other" ENERGY_TYPE
--     * Slot: indication Description: 
--     * Slot: indication_other Description: 
--     * Slot: proton_delivery_mode Description: 
--     * Slot: plaque_size Description: Size of the plaque holding the radiation source
--     * Slot: apex_dose Description: 
--     * Slot: rt_completed Description: Radiation Therapy Completed as Planned
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: time_periods_id Description: 
--     * Slot: subjects_id Description: 
-- # Class: "Stem Cell Transplant" Description: ""
--     * Slot: id Description: 
--     * Slot: age_at_sct Description: The age (in days) of subject at the time of stem cell transplantation.
--     * Slot: protocol_sct Description: Was this stem cell transplant part of the treatment protocol?
--     * Slot: non_protocol_timing Description: If a non-protocol radiation therapy, when was this radiation therapy administered?
--     * Slot: sct_type Description: A procedure in which a patient receives healthy stem cells (blood-forming cells) to replace their own stem cells that have been destroyed by treatment with radiation or high doses of chemotherapy. The healthy stem cells may come from the blood or bone marrow of the patient or from a related or unrelated donor. A stem cell transplant may be autologous (using a patient’s own stem cells that were collected and saved before treatment), allogeneic (using stem cells from a related or unrelated donor), syngeneic (using stem cells donated by an identical twin), or cord blood (using umbilical cord blood donated after a baby is born). (Source: NCI Dictionary of Cancer Terms)
--     * Slot: stem_cell_source Description: The source of the stem cells for the stem cell transplant.
--     * Slot: donor_relationship Description: The biological relationship between the stem cell donor and the recipients.
--     * Slot: hla_match Description: HLA Match Status
--     * Slot: number_hla Description: Number of Evaluated HLAs
--     * Slot: number_matches Description: Number of Matched HLAs
--     * Slot: conditioning_type Description: The type of conditioning the subject received prior to stem-cell transplantation.
--     * Slot: prior_tbi Description: Total Body Irradiation Prior to Stem Cell Transplant
--     * Slot: hla_a_result Description: HLA-A Match Finding
--     * Slot: hla_b_result Description: HLA-B Match Finding
--     * Slot: hla_c_result Description: HLA-C Match Finding
--     * Slot: hla_drb1_result Description: HLA-DRB1 Match Finding
--     * Slot: hla_dq_result Description: HLA-DQ Match Finding
--     * Slot: age_at_sct_harvest Description: The age (in days) of subject at the time of stem cell harvest
--     * Slot: age_at_recovery Description: The age (in days) of subject at the time of stem cell transplant per recovery type.
--     * Slot: recovery_type Description: The type of recovery after the transplant procedure.
--     * Slot: recovery_status Description: The recovery status per recovery type.
--     * Slot: cd34_collected Description: The determination of the amount of CD34 expressing stem cells present in a sample (10^6 CD34+/kg).
--     * Slot: cd34_transplant Description: The determination of the amount of transplanted CD34 expressing stem cells (10^6 CD34+/kg).
--     * Slot: sct_cycles Description: Number of Stem Cell Transplant Cycles
--     * Slot: stem_cell_source_other Description: Specify the "Other" STEM_CELL_SOURCE
--     * Slot: sct_success Description: Was the stem cell transplant successful?
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: time_periods_id Description: 
--     * Slot: subjects_id Description: 
-- # Class: "Medication" Description: ""
--     * Slot: id Description: 
--     * Slot: age_at_medication_start Description: The age (in days) of the subject at the start of this medication treatment.
--     * Slot: age_at_medication_end Description: The age (in days) of the subject at the end of this medication treatment.
--     * Slot: route Description: Route of Administration
--     * Slot: medication Description: A dosage form that contains one or more active and/or inactive ingredients. Medications come in many dosage forms, including tablets, capsules, liquids, creams, and patches. They can also be given in different ways, such as by mouth, by infusion into a vein, or by drops that are put into the ear or eye. The form with the active ingredient is used to prevent, diagnose, treat, or relieve symptoms of a disease or abnormal condition. A medication that does not contain an active ingredient and is used in research studies is called a placebo. Also called drug product.
--     * Slot: administration_status Description: The status of the medication administration.
--     * Slot: number_doses Description: Number of times a dose of the medication was administered between the AGE_AT_MEDICATION_START and AGE_AT_MEDICATION_END values.
--     * Slot: total_dose_administered Description: Total amount of medication administered between the AGE_AT_MEDICATION_START and AGE_AT_MEDICATION values. Assuming all doses administered are the same amount of medication, this value should be equal to the amount of medication given at each dose multiplied by the number of doses.
--     * Slot: total_dose_intended Description: This is the total amount of medication that was intended to be administered either by trial protocol, by prescription, or other indicator at the time point of AGE_AT_MEDICATION_START. Often, this will be equal to TOTAL_DOSE_ADMINISTERED. If TOTAL_DOSE_ADMINISTERED and TOTAL_DOSE_INTENDED are different, this indicates a deviation from the protocol or plan and may be due to a variety of factors including patient intolerance, patient non-adherence, etc.
--     * Slot: total_dose_unit Description: A unit of measurement of the dose of radiation received or absorbed.
--     * Slot: protocol_medication Description: Was this medication part of the treatment protocol?
--     * Slot: non_protocol_timing Description: If a non-protocol radiation therapy, when was this radiation therapy administered?
--     * Slot: non_protocol_reason Description: If a non-protocol medication, why was this medication administered?
--     * Slot: medication_other Description: Specify the "Other" MEDICATION
--     * Slot: category Description: The category of laboratory test performed on the subject.
--     * Slot: concomitant_reason Description: If a non-protocol medication, why was this medication administered?
--     * Slot: concomitant_reason_other Description: Specify the "Other" CONCOMITANT_REASON
--     * Slot: route_detail Description: Designation of the part of the body through which or into which, or the way in which, the medicinal product is intended to be introduced. In some cases a medicinal product can be intended for more than one route and/or method of administration.
--     * Slot: normalization_basis Description: An indication of what method was used to normalize the data.
--     * Slot: cycle_number Description: The number of the individual chemotherapeutic cycle.
--     * Slot: cycles_planned Description: 
--     * Slot: session_number Description: 
--     * Slot: tumor_site Description: 
--     * Slot: administration_site Description: 
--     * Slot: total_dose_given Description: Was the full dose of this cycle or session administered?
--     * Slot: delivery_status Description: Was this cycle or session delivered successfully?
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: time_periods_id Description: 
--     * Slot: subjects_id Description: 
-- # Class: "Transfusion Medicine Procedures" Description: ""
--     * Slot: id Description: 
--     * Slot: age_at_tmp_start Description: The age (in days) of the subject at the start of the transfuction medicine procedure
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: product Description: The type of product intended for transfusion.
--     * Slot: age_at_tmp Description: The age (in days) of subject at the start of the transfusion medicine procedure
--     * Slot: product_processing Description: The type of processing that is used on the transfusion product.
--     * Slot: product_processing_other Description: Specify the "Other" PRODUCT_PROCESSING
--     * Slot: number_units Description: The number of units transfused into an individual.
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: time_periods_id Description: 
--     * Slot: subjects_id Description: 
-- # Class: "Cellular Immunotherapy" Description: ""
--     * Slot: id Description: 
--     * Slot: age_at_cimt_start Description: The age (in days) of subject at the time of cellular immunotherapy.
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: type_other Description: Specify the "Other" CIMT_TYPE
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: time_periods_id Description: 
--     * Slot: subjects_id Description: 
-- # Class: "Biopsy And Surgical Procedures" Description: ""
--     * Slot: id Description: 
--     * Slot: age_at_procedure Description: The age (in days) of the subject at the time of this procedure.
--     * Slot: protocol_procedure Description: Was this procedure part of the treatment protocol?
--     * Slot: non_protocol_timing Description: If a non-protocol radiation therapy, when was this radiation therapy administered?
--     * Slot: procedure Description: A categorization of surgical procedures by type or purpose.
--     * Slot: site Description: Specifies the anatomic site of a localized pathological or traumatic structural change, damage, deformity, or discontinuity of tissue, organ, or body part.
--     * Slot: site_other Description: Specify the "Other" TUMOR_SITE
--     * Slot: extent Description: The degree to which the lesion has been cut out, or resected.
--     * Slot: outcome Description: 
--     * Slot: hydrocephalus Description: A disorder characterized by an abnormal increase of cerebrospinal fluid in the ventricles of the brain.
--     * Slot: posterior_fossa_syndrome Description: 
--     * Slot: csf_diversion Description: 
--     * Slot: nephron_sparing_partial_nephrectomy Description: If this is a renal tumor, was nephron-sparing surgery/partial nephrectomy performed?
--     * Slot: surgery_type_limb Description: The type of surgical procedures performed on the limb of the subject.
--     * Slot: margins Description: The edge or border of the tissue removed in cancer surgery. The margin is described as negative or clean when the pathologist finds no cancer cells at the edge of the tissue, suggesting that all of the cancer has been removed. The margin is described as positive or involved when the pathologist finds cancer cells at the edge of the tissue, suggesting that all of the cancer has not been removed. (Source: NCI Dictionary of Cancer Terms)
--     * Slot: tumor_rupture Description: If this is a solid tumor, was there pre-surgical tumor rupture?
--     * Slot: surgical_complications Description: 
--     * Slot: surgical_complications_other Description: 
--     * Slot: classification Description: The classification of a tumor based primarily on histopathological characteristics.
--     * Slot: tissue_type Description: A piece of tissue removed from an organism for examination, analysis, or propagation.
--     * Slot: laterality Description: A qualifier for the side of the body the tumor findings assessment is performed.
--     * Slot: biopsy_type Description: The removal of cells or tissues for examination by a pathologist. The pathologist may study the tissue under a microscope or perform other tests on the cells or tissue. There are many different types of biopsy procedures. The most common types include: (1) incisional biopsy, in which only a sample of tissue is removed; (2) excisional biopsy, in which an entire lump or suspicious area is removed; and (3) needle biopsy, in which a sample of tissue or fluid is removed with a needle. When a wide needle is used, the procedure is called a core biopsy. When a thin needle is used, the procedure is called a fine-needle aspiration biopsy. (Source: NCI Dictionary of Cancer Terms)
--     * Slot: surgery_type_amputation Description: The removal by surgery of a limb (arm or leg) or other body part because of injury or disease, such as diabetes or cancer. (Source: NCI Dictionary of Cancer Terms)
--     * Slot: surgery_type_limb_salvage Description: A procedure to avoid amputation of an arm or leg.
--     * Slot: reconstruction_type Description: The type of reconstruction performed on the subject.
--     * Slot: procedure_extent Description: The degree to which the lesion has been cut out, or resected.
--     * Slot: met_non_lung_mgmt Description: Surgical treatment of metastatic disease not involving the lungs.
--     * Slot: met_lung_mgmt Description: Surgical treatment of disease metastatic to the lungs.
--     * Slot: localization_technique Description: The process of determining or marking the location or site of a tumor or disease. May also refer to the process of keeping a tumor or disease in a specific location or site. (Source: NCI Dictionary of Cancer Terms)
--     * Slot: distance_margin_tumor Description: The distance of the closest surgical margin from tumor after surgical resection of the tumor. The closest distance between a tumor and its resection margin has prognostic significance.	
--     * Slot: procedure_other Description: Specify the "Other" PROCEDURE_TYPE
--     * Slot: biopsy_type_other Description: Specify the "Other" BIOPSY_TYPE
--     * Slot: number_nodes Description: A question whether an individual has a single or multiple lymph nodes involved.
--     * Slot: number_nodes_numeric Description: The number of lymph nodes that were examined.
--     * Slot: procedure_purpose Description: The reason a procedure is performed.
--     * Slot: procedure_purpose_other Description: Specify the "Other" PROCEDURE_PURPOSE
--     * Slot: amputation_type Description: The removal by surgery of a limb (arm or leg) or other body part because of injury or disease, such as diabetes or cancer. (Source: NCI Dictionary of Cancer Terms)
--     * Slot: resection_type Description: Surgery to remove tissue or part or all of an organ. (Source: NCI Dictionary of Cancer Terms)
--     * Slot: distance_margin Description: The distance of the closest surgical margin from tumor after surgical resection of the tumor. The closest distance between a tumor and its resection margin has prognostic significance.
--     * Slot: hemipelvectomy_type Description: If the pelvis was involved, was the involved procedure internal or external?
--     * Slot: hemipelvectomy_site Description: The area involved in the hemipelvectomy.
--     * Slot: intraop_adjuvant Description: An additional therapy administered during surgery.
--     * Slot: intraop_adjuvant_other Description: Specify the "Other" INTRAOP_ADJUVANT
--     * Slot: laser_type Description: 
--     * Slot: laser_type_other Description: 
--     * Slot: laser_power Description: 
--     * Slot: laser_duration Description: 
--     * Slot: laser_duration_numeric Description: 
--     * Slot: cryotherapy_freezes Description: Number of cryotherapy freezes
--     * Slot: freeze_thaw_cycle_number Description: Number of freeze-thaw cycle
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: time_periods_id Description: 
--     * Slot: subjects_id Description: 
-- # Class: "Protocol Treatment Modifications" Description: ""
--     * Slot: id Description: 
--     * Slot: age_at_modification Description: The age (in days) of subject since the protocol treatment modification.
--     * Slot: modification Description: The type of modification used.
--     * Slot: modification_other Description: Specify the "Other" MODIFICATION
--     * Slot: modification_basis Description: The rationale for why an entity or event is changed.	
--     * Slot: reason Description: The reasoning behind a treatment modification.	
--     * Slot: reason_other Description: Specify the "Other" REASON
--     * Slot: toxicity_detail Description: Information about the conditions surrounding the toxicity.	
--     * Slot: toxicity_detail_other Description: 
--     * Slot: toxicity_immune Description: Toxicity that impairs or damages the immune system.	
--     * Slot: toxicity_infusion Description: Toxicity related to an infusion.	
--     * Slot: original_agent Description: The first agent planned for a therapy.	
--     * Slot: original_agent_other Description: Specify the "Other" ORIGINAL_AGENT
--     * Slot: sub_agent Description: A medication was substituted with another.	
--     * Slot: sub_agent_other Description: Specify the "Other" SUB_AGENT
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: time_periods_id Description: 
--     * Slot: subjects_id Description: 
-- # Class: "Minimal Residual Disease" Description: ""
--     * Slot: id Description: 
--     * Slot: age_at_mrd_assessment Description: Age in Days at Minimal Residual Disease Assessment
--     * Slot: method Description: A systematic course of action that is performed in order to complete a laboratory test.
--     * Slot: result_text Description: The string/text result of the laboratory test.
--     * Slot: result_numeric Description: The numeric result of the laboratory test.
--     * Slot: result_unit Description: The units used for the numeric result of the laboratory test.
--     * Slot: sensitivity Description: Sensitivity of modality used to determine minimal residual disease.
--     * Slot: sample_source Description: Minimal Residual Disease Sample Source
--     * Slot: method_other Description: Specify the "Other" LAB_METHOD
--     * Slot: molecular_markers Description: Minimal residual disease molecular markers
--     * Slot: molecular_markers_other Description: Specify the "Other" MRD_MOLECULAR_MARKERS
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: time_periods_id Description: 
--     * Slot: subjects_id Description: 
-- # Class: "Subject Response" Description: ""
--     * Slot: id Description: 
--     * Slot: age_at_response Description: The age (in days) of subject when the response assessment was made.
--     * Slot: response_category Description: The category used to assess the response to therapy.
--     * Slot: response Description: A qualitative or quantitative measurement of the response of a target lesion(s) to the therapy.
--     * Slot: bm_pct_blasts_at_response Description: BM Percent Blasts At Response
--     * Slot: bm_analysis_method_at_response Description: BM Analysis Modality at Response
--     * Slot: anc_at_response Description: ANC at Response (ANC/mm3)
--     * Slot: anc_threshold_at_response Description: ANC Threshold at Response
--     * Slot: platelet_count_at_response Description: Platelet Count At Responset (platelets/mm3)
--     * Slot: platelet_threshold_at_response Description: Exceeded Platelet Threshold >=50,000 (platelets/mm3) At Response
--     * Slot: response_method Description: The method used to assess the response to therapy.
--     * Slot: response_system Description: A standard from which a judgment concerning tumor response to therapy can be established.
--     * Slot: mri_sequence Description: 
--     * Slot: neurological_status Description: 
--     * Slot: response_system_version Description: The version of the response system.
--     * Slot: necrosis Description: The quantitative value for the percent of necrosis.
--     * Slot: necrosis_pct Description: A numeric measurement of the percent of cells undergoing necrosis compared to the number of total cells present in a sample.
--     * Slot: interim_response Description: An evaluation prior to the completion of therapy that the individual is responding to therapy.
--     * Slot: response_method_other Description: "Specify the "Other" RESPONSE_METHOD
--     * Slot: symptoms Description: A physical or mental problem that a person experiences that may indicate a disease or condition. Symptoms cannot be seen and do not show up on medical tests. Some examples of symptoms are headache, fatigue, nausea, and pain. (Source: NCI Dictionary of Cancer Terms)
--     * Slot: palpable_nodes Description: The lymph nodes are felt on palpation.
--     * Slot: nodular_splenic Description: Nodular Splenic Involvement
--     * Slot: course_timepoint Description: This variable gives more precise granularity to when an observation occured during the period of the indicated "Course" TIME_PERIOD
--     * Slot: measurement_type Description: The type of vital sign or anthropomorphic measurement being recorded
--     * Slot: measurement_numeric Description: The vital sign or anthropomorphic measurement being recorded (numeric)
--     * Slot: tx_prior_response Description: Treatment Type Prior to Response Assessment
--     * Slot: tumor_site Description: 
--     * Slot: microscopic_change_type Description: 
--     * Slot: microscopic_change_status Description: 
--     * Slot: microscopic_change_pct Description: 
--     * Slot: microscopic_change_pct_numeric Description: 
--     * Slot: macroscopic_change_type Description: 
--     * Slot: macroscopic_change_status Description: 
--     * Slot: macroscopic_change_pct_numeric Description: 
--     * Slot: anaplasia_status Description: Indicates the presence or absence of anaplasia in the tumor.
--     * Slot: anaplasia_type Description: describes the type or extent of anaplasia found during a histopathologic exam.
--     * Slot: anaplasia_pct_numeric Description: The numeric percentage of anaplasia found in the tumor.
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: time_periods_id Description: 
--     * Slot: subjects_id Description: 
-- # Class: "Adverse Events" Description: ""
--     * Slot: id Description: 
--     * Slot: age_at_ae Description: The age (in days) of the subject at the onset of this adverse event
--     * Slot: ae_code Description: The code of the adverse event.
--     * Slot: ae_code_system Description: The coding system used for the AE_CODE
--     * Slot: ae_code_system_version Description: The version of the adverse event grading system.
--     * Slot: grade Description: A numeric value corresponding to the degree of severity of an adverse event.
--     * Slot: grade_system Description: The grading system used to refer to the severity of the adverse event.
--     * Slot: grade_system_version Description: The version of the adverse event grading system.
--     * Slot: attribution Description: A specific identifiable level (defined qualitatively or quantitatively) of probability of adverse event being caused or associated with the product or procedure administration to a patient.
--     * Slot: avn_joint Description: Death of bone tissue in a joint due to temporary or permanent interruption of blood flow.
--     * Slot: avn_joint_other Description: Specify the "Other" AVN_JOINT
--     * Slot: avn_joint_laterality Description: A finding descriptive of the laterality of the avascular necrosis in the joints.
--     * Slot: avn_method Description: The method used to determine the diagnosis of the avascular necrosis.
--     * Slot: orthopedic_procedure Description: Orthopedic procedures to repair avascular necrosis.
--     * Slot: orthopedic_procedure_other Description: Specify the "Other" ORTHOPEDIC_PROCEDURE
--     * Slot: ae_pathogen Description: The pathogen identified as the agent causing the adverse event.
--     * Slot: ae_pathogen_other Description: Specify the "Other" AE_PATHOGEN
--     * Slot: infection_classification Description: The type of evidence regarding the infection type.
--     * Slot: age_at_ae_resolved Description: The age (in days) of the subject when this adverse event was resolved
--     * Slot: adverse_event Description: An unexpected medical problem that happens during treatment with a drug or other therapy. Adverse events may be mild, moderate, or severe, and may be caused by something other than the drug or therapy being given. Also called adverse effect. (Source: NCI Dictionary of Cancer Terms)
--     * Slot: adverse_event_other Description: Specify the "Other" ADVERSE_EVENT
--     * Slot: icu Description: Admitted to ICU
--     * Slot: supportive_medication Description: Adverse Event Supportive Care Medication
--     * Slot: intervention_status Description: Adverse Event Intervention
--     * Slot: intervention Description: Intervention or Medication Detail
--     * Slot: intervention_other Description: Specify the "Other" INTERVENTION_DETAIL
--     * Slot: ae_pathogen_confirmation Description: Pathogen Confirmation Indicator
--     * Slot: gvhd_acuity Description: Graft Versus Host Disease Acuity
--     * Slot: gvhd_organ Description: Graft Versus Host Disease Organ
--     * Slot: gvhd_organ_other Description: Specify the "Other" GVHD_ORGAN
--     * Slot: ae_outcome Description: A condition or event that is attributed to the adverse event and is the result or conclusion of the adverse event.
--     * Slot: modification_required Description: An indication that a change in treatment or a change to a device will be required following an adverse event.
--     * Slot: tox_delay Description: Were there treatment delays due to toxicity?
--     * Slot: tox_high_grade_events Description: The number of grade III-IV (CTCAE) toxicity events
--     * Slot: tox_dose_reductions Description: The number of chemotherapy dose reductions due to toxicity
--     * Slot: ae_immune Description: An adverse event affecting the immune system.
--     * Slot: ae_infusion Description: An adverse event that can be related to an infusion.
--     * Slot: reported Description: SAE Reported to Sponsor
--     * Slot: as_expected Description: Specifies whether the nature, frequency, or severity of an adverse event is consistent with the applicable study documentation (e.g., investigator's brochure, protocol document, or consent document) or product labeling (package insert).
--     * Slot: hospitalization Description: An indication or description that an adverse event is associated with or prolongs hospitalization.
--     * Slot: ae_pathogen_status Description: An indication that the reported pathogen was confirmed or suspected as the cause of an infection.
--     * Slot: tumor_site Description: 
--     * Slot: ae_hospitalization_reason_other Description: Specify the "Other" AE_HOSPITALIZATION_REASON
--     * Slot: ae_hospitalization Description: An indication or description that an adverse event is associated with or prolongs hospitalization.
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: time_periods_id Description: 
--     * Slot: subjects_id Description: 
-- # Class: "Subsequent Malignant Neoplasm" Description: ""
--     * Slot: id Description: 
--     * Slot: age_at_smn Description: The age (in days) of subject at the diagnosis of the subsequent malignant neoplasm.
--     * Slot: treatment_related Description: Is this subsequent malignancy related to prior treatment recieved?
--     * Slot: morph_code Description: The code for the morphology of the subsequent tumor
--     * Slot: morph_code_system Description: The coding system for MORPH_CODE
--     * Slot: morph_code_system_version Description: The version of the coding system indicated in MORPH_CODE_SYSTEM
--     * Slot: top_code Description: The topography code describes the site of origin of the neoplasm.
--     * Slot: top_code_system Description: The coding system for the code used in TOP_CODE
--     * Slot: top_code_system_version Description: The version of the coding system indicated in TOP_CODE_SYSTEM
--     * Slot: smn_status Description: Was the indicated subsequent malignant neoplasm found in the patient?
--     * Slot: morph_code_txt Description: The display text for MORPH_CODE 
--     * Slot: top_code_txt Description: The display text for TOP_CODE 
--     * Slot: smn_field Description: The location of the subsequent malignant neoplasm related to the prior radiation field.
--     * Slot: site Description: Specifies the anatomic site of a localized pathological or traumatic structural change, damage, deformity, or discontinuity of tissue, organ, or body part.
--     * Slot: site_other Description: Specify the "Other" TUMOR_SITE
--     * Slot: smn Description: SMN Type
--     * Slot: smn_other Description: Specify the "Other" SMN
--     * Slot: smn_type_other Description: Specify the "Other" SMN_TYPE
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: time_periods_id Description: 
--     * Slot: subjects_id Description: 
-- # Class: "Patient Reported Outcomes Metadata" Description: ""
--     * Slot: id Description: 
--     * Slot: study_id Description: A sequence of characters used to identify, name, or characterize the study.
--     * Slot: pro_measures Description: Survey measures that are completed by the patient which help assess patient status with regards to pain, mobility, quality of life, ability to perform daily tasks or notable events in a clinical study.
--     * Slot: pro_measures_other Description: Specify the "Other"
--     * Slot: pro_measurement_type Description: The type of patient reported outcome measurement.
--     * Slot: pro_measurement_type_other Description: Specify the "Other" PRO_MEASUREMENT_TYPE
--     * Slot: raters Description: Raters are allowed to report the patient reported outcomes.
--     * Slot: raters_other Description: Specify the "Other" RATERS
--     * Slot: eligible_age_lower Description: The low age range of the child for an evaluation tool.
--     * Slot: eligible_age_upper Description: The upper age range of the child for an evaluation tool.
--     * Slot: time_point Description: The point in time that acts as a fixed reference point to an event.
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: subjects_id Description: 
-- # Class: "Late Effects" Description: ""
--     * Slot: id Description: 
--     * Slot: age_at_le_eval Description: The age (in days) of subject when the late effect evaluation was performed.
--     * Slot: late_effect Description: A health problem that occurs months or years after a disease is diagnosed or after treatment has ended. Late effects may be caused by cancer or cancer treatment. They may include physical, mental, and social problems and second cancers. (Source: NCI Dictionary of Cancer Terms)
--     * Slot: code Description: The code of the adverse event.
--     * Slot: code_system Description: The coding system used for the AE_CODE
--     * Slot: code_system_version Description: 
--     * Slot: grade Description: A numeric value corresponding to the degree of severity of an adverse event.
--     * Slot: grade_system Description: The grading system used to refer to the severity of the adverse event.
--     * Slot: grade_system_version Description: The version of the adverse event grading system.
--     * Slot: submitter_id Description: PCDC internal event ID
--     * Slot: type Description: Default system-assigned property for each node
--     * Slot: subjects_id Description: 

CREATE TABLE "Thing" (
	id INTEGER, 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Person" (
	id INTEGER, 
	sex VARCHAR(16), 
	race VARCHAR(41), 
	race_other TEXT, 
	ethnicity VARCHAR(22), 
	country TEXT, 
	race_identification_source VARCHAR(22), 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Subject" (
	id INTEGER, 
	honest_broker_subject_id TEXT, 
	consortium VARCHAR(12), 
	data_contributor_id VARCHAR(12), 
	study_id VARCHAR(19), 
	age_at_enrollment INTEGER, 
	treatment_arm VARCHAR(71), 
	enrolled_status VARCHAR(12), 
	data_source VARCHAR(17), 
	year_at_enrollment INTEGER, 
	study_phase VARCHAR(12), 
	study_type VARCHAR(12), 
	efs_censor_status VARCHAR(12), 
	age_at_censor_status INTEGER, 
	randomized_status VARCHAR(14), 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	persons_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(persons_id) REFERENCES "Person" (id)
);
CREATE TABLE "Time Period" (
	id INTEGER, 
	time_period_type VARCHAR(13), 
	disease_phase VARCHAR(19), 
	course VARCHAR(33), 
	time_period_number INTEGER, 
	year_at_start INTEGER, 
	age_at_start INTEGER, 
	age_at_end INTEGER, 
	course_other TEXT, 
	age_at_course_anc_500 INTEGER, 
	age_at_txassign INTEGER, 
	age_precision VARCHAR(12), 
	exam_type VARCHAR(40), 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	time_periods_id TEXT, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_periods_id) REFERENCES "Time Period" (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Medical History" (
	id INTEGER, 
	condition VARCHAR(60), 
	condition_other TEXT, 
	age_at_condition INTEGER, 
	condition_type VARCHAR(18), 
	diagnosis_basis VARCHAR(12), 
	condition_status VARCHAR(12), 
	assisted_conception VARCHAR(32), 
	developmental_delay VARCHAR(12), 
	developmental_delay_type TEXT, 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Family Medical History" (
	id INTEGER, 
	relation VARCHAR(8), 
	relation_other TEXT, 
	shared_predisposition VARCHAR(12), 
	relative_honest_broker_id TEXT, 
	prior_cancer VARCHAR(12), 
	prior_cancer_type TEXT, 
	prior_cancer_laterality VARCHAR(12), 
	lkss_of_relative VARCHAR(12), 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Patient Reported Outcomes Metadata" (
	id INTEGER, 
	study_id VARCHAR(19), 
	pro_measures VARCHAR(38), 
	pro_measures_other TEXT, 
	pro_measurement_type VARCHAR(14), 
	pro_measurement_type_other TEXT, 
	raters VARCHAR(27), 
	raters_other TEXT, 
	eligible_age_lower INTEGER, 
	eligible_age_upper INTEGER, 
	time_point VARCHAR(20), 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Late Effects" (
	id INTEGER, 
	age_at_le_eval INTEGER, 
	late_effect VARCHAR(30), 
	code TEXT, 
	code_system VARCHAR, 
	code_system_version TEXT, 
	grade VARCHAR(14), 
	grade_system VARCHAR(60), 
	grade_system_version TEXT, 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Off Protocol Therapy Or Study" (
	id INTEGER, 
	age_off INTEGER, 
	off_type VARCHAR(16), 
	reason_off VARCHAR(42), 
	reason_off_other TEXT, 
	another_study VARCHAR(12), 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	time_periods_id TEXT, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_periods_id) REFERENCES "Time Period" (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Survival Characteristics" (
	id INTEGER, 
	age_at_lkss INTEGER, 
	lkss VARCHAR(12), 
	lkss_with_disease VARCHAR(12), 
	age_lost_to_follow_up INTEGER, 
	cause_of_death VARCHAR(36), 
	cause_of_death_other TEXT, 
	trm_type VARCHAR(20), 
	trm_type_other TEXT, 
	cause_of_death_detail VARCHAR(35), 
	cause_of_death_detail_other TEXT, 
	cause_of_death_ranking VARCHAR(12), 
	course_timepoint VARCHAR(12), 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	time_periods_id TEXT, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_periods_id) REFERENCES "Time Period" (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Vitals And Anthropometrics" (
	id INTEGER, 
	age_at_measurement INTEGER, 
	measurement_type VARCHAR(24), 
	measurement_text TEXT, 
	measurement_numeric INTEGER, 
	measurement_unit VARCHAR(12), 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	time_periods_id TEXT, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_periods_id) REFERENCES "Time Period" (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Laboratory Test" (
	id INTEGER, 
	age_at_lab INTEGER, 
	category VARCHAR(28), 
	test VARCHAR(25), 
	specimen VARCHAR(19), 
	specimen_other TEXT, 
	method VARCHAR(19), 
	method_other TEXT, 
	result_text TEXT, 
	result_numeric INTEGER, 
	result_unit VARCHAR(12), 
	traumatic_tap VARCHAR(12), 
	bm_morphology VARCHAR(29), 
	result VARCHAR(12), 
	threshold_level VARCHAR(4), 
	threshold_high INTEGER, 
	thredhold_low INTEGER, 
	seq_method VARCHAR(12), 
	threshold_low INTEGER, 
	pmid_ref INTEGER, 
	malignant_cells VARCHAR(12), 
	course_timepoint VARCHAR(12), 
	test_other TEXT, 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	time_periods_id TEXT, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_periods_id) REFERENCES "Time Period" (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Genetic Analysis" (
	id INTEGER, 
	age_at_genetic_analysis INTEGER, 
	method VARCHAR(19), 
	specimen VARCHAR(19), 
	common_name VARCHAR(47), 
	karyotype_status VARCHAR(18), 
	status VARCHAR(12), 
	iscn TEXT, 
	total_chromosomes INTEGER, 
	chromosome TEXT, 
	gene TEXT, 
	gene2 TEXT, 
	variation_type VARCHAR(42), 
	variation_type_other TEXT, 
	copy_number_variation VARCHAR(23), 
	copy_number INTEGER, 
	hgvs_coding TEXT, 
	hgvs_protein TEXT, 
	dna_index_numeric INTEGER, 
	method_other TEXT, 
	independent_aberations INTEGER, 
	cells_in_metaphase INTEGER, 
	common_name_other TEXT, 
	mutant_allele_fraction INTEGER, 
	genomic_source_class VARCHAR(22), 
	expression_consequence VARCHAR(19), 
	chromosomal_consequence VARCHAR(12), 
	allelic_state VARCHAR(12), 
	allelic_frequency INTEGER, 
	external_ref_id TEXT, 
	external_ref_id_system VARCHAR, 
	mosaicism_percent INTEGER, 
	variation_effect VARCHAR(12), 
	inheritance_pattern VARCHAR(12), 
	parental_status VARCHAR(12), 
	hgvs_coding_transcript TEXT, 
	hgvs_protein_transcript TEXT, 
	reported_significance VARCHAR(22), 
	associated_condition VARCHAR(12), 
	associated_condition_other TEXT, 
	review_source VARCHAR(13), 
	tumor_classification VARCHAR(12), 
	course_timepoint VARCHAR(12), 
	specimen_other TEXT, 
	biological_analyte VARCHAR(12), 
	biological_analyte_other TEXT, 
	source_pct VARCHAR(12), 
	source_pct_numeric INTEGER, 
	tkd_involvement VARCHAR(12), 
	maf VARCHAR(12), 
	maf_numeric INTEGER, 
	clonal_status VARCHAR(12), 
	dna_index VARCHAR(12), 
	cytodifferentiation VARCHAR, 
	mitotic_rate VARCHAR, 
	mutated_allele_frequency INTEGER, 
	cascade_testing VARCHAR(12), 
	alt_status VARCHAR(12), 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	time_periods_id TEXT, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_periods_id) REFERENCES "Time Period" (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Function Test" (
	id INTEGER, 
	age_at_function_test INTEGER, 
	test VARCHAR(25), 
	measurement_type VARCHAR(24), 
	measurement_text TEXT, 
	measurement_numeric INTEGER, 
	measurement_unit VARCHAR(12), 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	time_periods_id TEXT, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_periods_id) REFERENCES "Time Period" (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Immunohistochemistry" (
	id INTEGER, 
	age_at_ihc INTEGER, 
	review_source VARCHAR(13), 
	test VARCHAR(25), 
	result VARCHAR(12), 
	result_text TEXT, 
	result_numeric INTEGER, 
	specimen VARCHAR(19), 
	result_unit VARCHAR(12), 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	time_periods_id TEXT, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_periods_id) REFERENCES "Time Period" (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Imaging" (
	id INTEGER, 
	age_at_imaging INTEGER, 
	method VARCHAR(19), 
	result VARCHAR(12), 
	deauville_score VARCHAR(7), 
	qpet_score INTEGER, 
	finding VARCHAR(37), 
	finding_other TEXT, 
	finding_site VARCHAR(26), 
	finding_site_other TEXT, 
	bone_marrow VARCHAR(12), 
	csf_result VARCHAR(12), 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	time_periods_id TEXT, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_periods_id) REFERENCES "Time Period" (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Histology" (
	id INTEGER, 
	age_at_hist_assessment INTEGER, 
	morph_code TEXT, 
	morph_code_system VARCHAR, 
	morph_code_system_version TEXT, 
	top_code TEXT, 
	top_code_system VARCHAR, 
	top_code_system_version TEXT, 
	all_type VARCHAR(57), 
	fab_type VARCHAR(12), 
	who_aml VARCHAR(64), 
	mpal VARCHAR(12), 
	mlds VARCHAR(12), 
	tam VARCHAR(12), 
	secondary_aml VARCHAR(12), 
	histology VARCHAR(84), 
	molecular_classification VARCHAR(47), 
	molecular_classification_other TEXT, 
	determination_source VARCHAR, 
	method VARCHAR(19), 
	morph_code_txt TEXT, 
	review_source VARCHAR(13), 
	histology_result_text TEXT, 
	histology_result_numeric INTEGER, 
	histology_result_unit VARCHAR(12), 
	histology_grade VARCHAR(19), 
	mature_glial_implants VARCHAR(12), 
	somatic_malignancy_type VARCHAR(31), 
	somatic_malignancy_type_other TEXT, 
	course_timepoint VARCHAR(12), 
	revised_inpc VARCHAR, 
	mki VARCHAR, 
	histology_other TEXT, 
	tumor_site VARCHAR(12), 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	time_periods_id TEXT, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_periods_id) REFERENCES "Time Period" (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Disease Characteristics" (
	id INTEGER, 
	disease_site VARCHAR(22), 
	detection_method_other TEXT, 
	cns_disease_status VARCHAR(12), 
	prior_steroids_week VARCHAR(12), 
	prior_steroids_month VARCHAR(12), 
	bulk_med_mass VARCHAR(12), 
	disease_site_other TEXT, 
	detection_method VARCHAR(27), 
	myeloid_sarcoma VARCHAR(12), 
	myeloid_sarcoma_site VARCHAR(12), 
	myeloid_sarcoma_site_other TEXT, 
	age_at_disease_characteristic INTEGER, 
	performance_score VARCHAR(12), 
	performance_score_system VARCHAR(12), 
	gpoh_score VARCHAR(12), 
	risk_group_system VARCHAR, 
	risk_group VARCHAR(19), 
	gts_treatment VARCHAR(12), 
	bulk_disease VARCHAR(12), 
	bulk_nodal_aggregate VARCHAR(12), 
	med_ratio INTEGER, 
	fever VARCHAR(12), 
	night_sweats VARCHAR(12), 
	weight_loss VARCHAR(12), 
	nodular_splenic VARCHAR(12), 
	course_timepoint VARCHAR(12), 
	initial_treatment_category VARCHAR, 
	tumor_site VARCHAR(12), 
	evaluator VARCHAR(12), 
	evaluator_other TEXT, 
	presentation_symptoms VARCHAR(12), 
	presentation_symptoms_other TEXT, 
	clinical_signs VARCHAR(12), 
	clinical_signs_other TEXT, 
	suspected_referring_diagnosis VARCHAR, 
	suspected_diagnosis_other TEXT, 
	visual_acuity_technique VARCHAR(12), 
	visual_acuity_result VARCHAR(12), 
	visual_acuity_result_numeric INTEGER, 
	visual_acuity_notation VARCHAR(12), 
	anterior_segment_exam VARCHAR, 
	anterior_segment_details VARCHAR, 
	anterior_segment_details_other TEXT, 
	intraocular_pressure INTEGER, 
	intraocular_pressure_unit VARCHAR, 
	retinal_detachment VARCHAR, 
	advanced_disease_signs VARCHAR, 
	advanced_disease_signs_other TEXT, 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	time_periods_id TEXT, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_periods_id) REFERENCES "Time Period" (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Tumor Assessment" (
	id INTEGER, 
	age_at_assessment INTEGER, 
	detection_method VARCHAR(27), 
	review_source VARCHAR(13), 
	mri_sequence VARCHAR(26), 
	tumor_presentation VARCHAR(12), 
	classification VARCHAR(12), 
	site VARCHAR(34), 
	site_other TEXT, 
	age_at_tumor_assessment INTEGER, 
	status VARCHAR(12), 
	assessment_reason VARCHAR(12), 
	morph_code TEXT, 
	morph_code_txt TEXT, 
	morph_code_system VARCHAR, 
	morph_code_system_version TEXT, 
	top_code TEXT, 
	top_code_txt TEXT, 
	top_code_system VARCHAR, 
	top_code_system_version TEXT, 
	longest_diam_dim1 INTEGER, 
	longest_diam_dim2 INTEGER, 
	longest_diam_dim3 INTEGER, 
	tumor_submitter_id TEXT, 
	primary_tumor_submitter_id TEXT, 
	tissue_type VARCHAR(12), 
	classification_status VARCHAR(13), 
	multiplicity VARCHAR(12), 
	tumor_size VARCHAR(12), 
	tumor_volume VARCHAR(12), 
	estimated_volume INTEGER, 
	laterality VARCHAR(12), 
	fracture VARCHAR(12), 
	skip_tumor VARCHAR(12), 
	ipsilateral_nodules VARCHAR(12), 
	joint_involvement VARCHAR(12), 
	site_within_bone VARCHAR(12), 
	nodal_involvement VARCHAR(12), 
	nodal_site VARCHAR(15), 
	extension_tumor_type VARCHAR(12), 
	detection_method_other TEXT, 
	e_extension_site VARCHAR(12), 
	e_extension_site_other TEXT, 
	diam_type VARCHAR(14), 
	bulky_disease VARCHAR(12), 
	effusion VARCHAR(12), 
	effusion_type VARCHAR, 
	response VARCHAR(29), 
	pct_change INTEGER, 
	course_timepoint VARCHAR(12), 
	tumor_type VARCHAR(12), 
	mibg_avidity VARCHAR(12), 
	invasiveness_status VARCHAR(12), 
	depth VARCHAR(15), 
	skip_met_involvement VARCHAR(12), 
	fracture_site VARCHAR(12), 
	massive_choroidal_extension VARCHAR, 
	visual_discrete_tumors VARCHAR(12), 
	tumor_number INTEGER, 
	tumor_from_fovea VARCHAR(12), 
	tumor_from_optic_nerve VARCHAR(12), 
	fluid_from_tumor VARCHAR(12), 
	seeds_present VARCHAR(12), 
	seeds_pattern VARCHAR(12), 
	seeds_status VARCHAR(12), 
	seeds_classification VARCHAR(12), 
	invasiveness VARCHAR(12), 
	nodal_determination VARCHAR(12), 
	nodal_determination_source VARCHAR(12), 
	parameningeal_extension VARCHAR(12), 
	necrosis_status VARCHAR(12), 
	necrosis_pct_numeric INTEGER, 
	anaplasia_status VARCHAR(12), 
	anaplasia_type VARCHAR(12), 
	anaplasia_pct_numeric INTEGER, 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	time_periods_id TEXT, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_periods_id) REFERENCES "Time Period" (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Staging" (
	id INTEGER, 
	age_at_staging INTEGER, 
	stage_system VARCHAR(76), 
	stage VARCHAR(31), 
	stage_other TEXT, 
	ann_arbor_mod_ab VARCHAR(12), 
	ann_arbor_mod_e VARCHAR(12), 
	ann_arbor_mod_s VARCHAR(12), 
	course_timepoint VARCHAR(12), 
	site VARCHAR(34), 
	stage_system_category VARCHAR(12), 
	stage_type VARCHAR(12), 
	h_stage VARCHAR(12), 
	group_system VARCHAR(12), 
	"group" VARCHAR(12), 
	tnm_finding VARCHAR(12), 
	irs_group VARCHAR(12), 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	time_periods_id TEXT, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_periods_id) REFERENCES "Time Period" (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Radiation Therapy" (
	id INTEGER, 
	age_at_rt_start INTEGER, 
	age_at_rt_end INTEGER, 
	protocol_radiation_therapy VARCHAR(12), 
	non_protocol_timing VARCHAR(22), 
	site VARCHAR(34), 
	site_other TEXT, 
	total_dose INTEGER, 
	total_dose_unit VARCHAR(12), 
	technique VARCHAR(31), 
	energy_type VARCHAR(12), 
	margin VARCHAR(12), 
	rt_data_source VARCHAR(12), 
	fraction_dose INTEGER, 
	fraction_dose_unit VARCHAR(12), 
	num_fraction INTEGER, 
	target_volume VARCHAR(12), 
	boost VARCHAR(12), 
	boost_dose INTEGER, 
	boost_unit VARCHAR(12), 
	boost_target_volume VARCHAR(12), 
	classification VARCHAR(12), 
	tissue_type VARCHAR(12), 
	laterality VARCHAR(12), 
	technique_other TEXT, 
	transposition_organ VARCHAR(12), 
	boost_dose_unit VARCHAR(12), 
	energy_type_other TEXT, 
	indication VARCHAR(12), 
	indication_other TEXT, 
	proton_delivery_mode VARCHAR(12), 
	plaque_size VARCHAR(12), 
	apex_dose INTEGER, 
	rt_completed VARCHAR(12), 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	time_periods_id TEXT, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_periods_id) REFERENCES "Time Period" (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Stem Cell Transplant" (
	id INTEGER, 
	age_at_sct INTEGER, 
	protocol_sct VARCHAR(12), 
	non_protocol_timing VARCHAR(22), 
	sct_type VARCHAR(12), 
	stem_cell_source VARCHAR(21), 
	donor_relationship VARCHAR(22), 
	hla_match VARCHAR(12), 
	number_hla INTEGER, 
	number_matches INTEGER, 
	conditioning_type VARCHAR(60), 
	prior_tbi VARCHAR(12), 
	hla_a_result VARCHAR(22), 
	hla_b_result VARCHAR(22), 
	hla_c_result VARCHAR(22), 
	hla_drb1_result VARCHAR(22), 
	hla_dq_result VARCHAR(22), 
	age_at_sct_harvest INTEGER, 
	age_at_recovery INTEGER, 
	recovery_type VARCHAR(10), 
	recovery_status VARCHAR, 
	cd34_collected INTEGER, 
	cd34_transplant INTEGER, 
	sct_cycles INTEGER, 
	stem_cell_source_other TEXT, 
	sct_success VARCHAR(12), 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	time_periods_id TEXT, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_periods_id) REFERENCES "Time Period" (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Medication" (
	id INTEGER, 
	age_at_medication_start INTEGER, 
	age_at_medication_end INTEGER, 
	route VARCHAR(12), 
	medication VARCHAR(42), 
	administration_status VARCHAR(27), 
	number_doses INTEGER, 
	total_dose_administered INTEGER, 
	total_dose_intended INTEGER, 
	total_dose_unit VARCHAR(12), 
	protocol_medication VARCHAR(12), 
	non_protocol_timing VARCHAR(22), 
	non_protocol_reason VARCHAR(27), 
	medication_other TEXT, 
	category VARCHAR(28), 
	concomitant_reason VARCHAR(27), 
	concomitant_reason_other TEXT, 
	route_detail VARCHAR(12), 
	normalization_basis VARCHAR(12), 
	cycle_number INTEGER, 
	cycles_planned INTEGER, 
	session_number INTEGER, 
	tumor_site VARCHAR(12), 
	administration_site VARCHAR(12), 
	total_dose_given VARCHAR(12), 
	delivery_status VARCHAR(12), 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	time_periods_id TEXT, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_periods_id) REFERENCES "Time Period" (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Transfusion Medicine Procedures" (
	id INTEGER, 
	age_at_tmp_start INTEGER, 
	type TEXT NOT NULL, 
	product VARCHAR(12), 
	age_at_tmp INTEGER, 
	product_processing VARCHAR(12), 
	product_processing_other TEXT, 
	number_units INTEGER, 
	submitter_id TEXT NOT NULL, 
	time_periods_id TEXT, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_periods_id) REFERENCES "Time Period" (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Cellular Immunotherapy" (
	id INTEGER, 
	age_at_cimt_start INTEGER, 
	type TEXT NOT NULL, 
	type_other TEXT, 
	submitter_id TEXT NOT NULL, 
	time_periods_id TEXT, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_periods_id) REFERENCES "Time Period" (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Biopsy And Surgical Procedures" (
	id INTEGER, 
	age_at_procedure INTEGER, 
	protocol_procedure VARCHAR(12), 
	non_protocol_timing VARCHAR(22), 
	procedure VARCHAR(22), 
	site VARCHAR(34), 
	site_other TEXT, 
	extent VARCHAR(18), 
	outcome VARCHAR(12), 
	hydrocephalus VARCHAR(12), 
	posterior_fossa_syndrome VARCHAR(12), 
	csf_diversion VARCHAR(26), 
	nephron_sparing_partial_nephrectomy VARCHAR(12), 
	surgery_type_limb VARCHAR(14), 
	margins VARCHAR(41), 
	tumor_rupture VARCHAR(12), 
	surgical_complications VARCHAR, 
	surgical_complications_other TEXT, 
	classification VARCHAR(12), 
	tissue_type VARCHAR(12), 
	laterality VARCHAR(12), 
	biopsy_type VARCHAR(18), 
	surgery_type_amputation VARCHAR(38), 
	surgery_type_limb_salvage VARCHAR(25), 
	reconstruction_type VARCHAR(47), 
	procedure_extent VARCHAR(18), 
	met_non_lung_mgmt VARCHAR(12), 
	met_lung_mgmt VARCHAR(34), 
	localization_technique VARCHAR(48), 
	distance_margin_tumor INTEGER, 
	procedure_other TEXT, 
	biopsy_type_other TEXT, 
	number_nodes VARCHAR(20), 
	number_nodes_numeric INTEGER, 
	procedure_purpose VARCHAR(46), 
	procedure_purpose_other TEXT, 
	amputation_type VARCHAR(38), 
	resection_type VARCHAR(32), 
	distance_margin INTEGER, 
	hemipelvectomy_type VARCHAR(12), 
	hemipelvectomy_site VARCHAR(15), 
	intraop_adjuvant VARCHAR(48), 
	intraop_adjuvant_other TEXT, 
	laser_type VARCHAR(12), 
	laser_type_other TEXT, 
	laser_power VARCHAR, 
	laser_duration VARCHAR, 
	laser_duration_numeric INTEGER, 
	cryotherapy_freezes INTEGER, 
	freeze_thaw_cycle_number INTEGER, 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	time_periods_id TEXT, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_periods_id) REFERENCES "Time Period" (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Protocol Treatment Modifications" (
	id INTEGER, 
	age_at_modification INTEGER, 
	modification VARCHAR(18), 
	modification_other TEXT, 
	modification_basis VARCHAR(19), 
	reason VARCHAR(30), 
	reason_other TEXT, 
	toxicity_detail VARCHAR(24), 
	toxicity_detail_other TEXT, 
	toxicity_immune VARCHAR(12), 
	toxicity_infusion VARCHAR(12), 
	original_agent VARCHAR(19), 
	original_agent_other TEXT, 
	sub_agent VARCHAR(19), 
	sub_agent_other TEXT, 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	time_periods_id TEXT, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_periods_id) REFERENCES "Time Period" (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Minimal Residual Disease" (
	id INTEGER, 
	age_at_mrd_assessment INTEGER, 
	method VARCHAR(19), 
	result_text TEXT, 
	result_numeric INTEGER, 
	result_unit VARCHAR(12), 
	sensitivity INTEGER, 
	sample_source VARCHAR(12), 
	method_other TEXT, 
	molecular_markers VARCHAR(38), 
	molecular_markers_other TEXT, 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	time_periods_id TEXT, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_periods_id) REFERENCES "Time Period" (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Subject Response" (
	id INTEGER, 
	age_at_response INTEGER, 
	response_category VARCHAR(24), 
	response VARCHAR(29), 
	bm_pct_blasts_at_response INTEGER, 
	bm_analysis_method_at_response VARCHAR(14), 
	anc_at_response INTEGER, 
	anc_threshold_at_response VARCHAR(12), 
	platelet_count_at_response INTEGER, 
	platelet_threshold_at_response VARCHAR(12), 
	response_method VARCHAR(20), 
	response_system VARCHAR(12), 
	mri_sequence VARCHAR(26), 
	neurological_status VARCHAR(13), 
	response_system_version TEXT, 
	necrosis VARCHAR(15), 
	necrosis_pct INTEGER, 
	interim_response VARCHAR(32), 
	response_method_other TEXT, 
	symptoms VARCHAR(12), 
	palpable_nodes VARCHAR(12), 
	nodular_splenic VARCHAR(12), 
	course_timepoint VARCHAR(12), 
	measurement_type VARCHAR(24), 
	measurement_numeric INTEGER, 
	tx_prior_response VARCHAR(17), 
	tumor_site VARCHAR(12), 
	microscopic_change_type VARCHAR(20), 
	microscopic_change_status VARCHAR(12), 
	microscopic_change_pct VARCHAR(12), 
	microscopic_change_pct_numeric INTEGER, 
	macroscopic_change_type VARCHAR(12), 
	macroscopic_change_status VARCHAR(12), 
	macroscopic_change_pct_numeric INTEGER, 
	anaplasia_status VARCHAR(12), 
	anaplasia_type VARCHAR(12), 
	anaplasia_pct_numeric INTEGER, 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	time_periods_id TEXT, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_periods_id) REFERENCES "Time Period" (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Adverse Events" (
	id INTEGER, 
	age_at_ae INTEGER, 
	ae_code TEXT, 
	ae_code_system VARCHAR(12), 
	ae_code_system_version TEXT, 
	grade VARCHAR(14), 
	grade_system VARCHAR(60), 
	grade_system_version TEXT, 
	attribution VARCHAR(12), 
	avn_joint VARCHAR(57), 
	avn_joint_other TEXT, 
	avn_joint_laterality VARCHAR(12), 
	avn_method VARCHAR(12), 
	orthopedic_procedure VARCHAR(30), 
	orthopedic_procedure_other TEXT, 
	ae_pathogen VARCHAR(12), 
	ae_pathogen_other TEXT, 
	infection_classification VARCHAR(45), 
	age_at_ae_resolved INTEGER, 
	adverse_event VARCHAR(37), 
	adverse_event_other TEXT, 
	icu VARCHAR(12), 
	supportive_medication VARCHAR(12), 
	intervention_status VARCHAR(12), 
	intervention VARCHAR(18), 
	intervention_other TEXT, 
	ae_pathogen_confirmation VARCHAR(12), 
	gvhd_acuity VARCHAR(12), 
	gvhd_organ VARCHAR(22), 
	gvhd_organ_other TEXT, 
	ae_outcome VARCHAR(23), 
	modification_required VARCHAR(12), 
	tox_delay VARCHAR(12), 
	tox_high_grade_events INTEGER, 
	tox_dose_reductions INTEGER, 
	ae_immune VARCHAR(12), 
	ae_infusion VARCHAR(12), 
	reported VARCHAR(12), 
	as_expected VARCHAR(12), 
	hospitalization VARCHAR(12), 
	ae_pathogen_status VARCHAR(12), 
	tumor_site VARCHAR(12), 
	ae_hospitalization_reason_other TEXT, 
	ae_hospitalization VARCHAR(12), 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	time_periods_id TEXT, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_periods_id) REFERENCES "Time Period" (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Subsequent Malignant Neoplasm" (
	id INTEGER, 
	age_at_smn INTEGER, 
	treatment_related VARCHAR(12), 
	morph_code TEXT, 
	morph_code_system VARCHAR, 
	morph_code_system_version TEXT, 
	top_code TEXT, 
	top_code_system VARCHAR, 
	top_code_system_version TEXT, 
	smn_status VARCHAR(12), 
	morph_code_txt TEXT, 
	top_code_txt TEXT, 
	smn_field VARCHAR(19), 
	site VARCHAR(34), 
	site_other TEXT, 
	smn VARCHAR(19), 
	smn_other TEXT, 
	smn_type_other TEXT, 
	submitter_id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	time_periods_id TEXT, 
	subjects_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_periods_id) REFERENCES "Time Period" (id), 
	FOREIGN KEY(subjects_id) REFERENCES "Subject" (id)
);
