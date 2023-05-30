
# Class: Histology




URI: [https://w3id.org/pcdc/model/Histology](https://w3id.org/pcdc/model/Histology)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..1-++[Histology&#124;age_at_hist_assessment:integer%20%3F;morph_code:string%20%3F;morph_code_system:MorphCodeSystemEnum%20%3F;morph_code_system_version:string%20%3F;top_code:string%20%3F;top_code_system:TopCodeSystemEnum%20%3F;top_code_system_version:string%20%3F;all_type:AllTypeEnum%20%3F;fab_type:FabTypeEnum%20%3F;who_aml:WhoAmlEnum%20%3F;mpal:NoNotreportedUnknownYesEnum%20%3F;mlds:NoNotreportedUnknownYesEnum%20%3F;tam:NoNotreportedUnknownYesEnum%20%3F;secondary_aml:NoNotreportedUnknownYesEnum%20%3F;histology:HistologyEnum%20%3F;molecular_classification:MolecularClassificationEnum%20%3F;molecular_classification_other:string%20%3F;determination_source:DeterminationSourceEnum%20%3F;method:MethodEnum%20%3F;morph_code_txt:string%20%3F;review_source:ReviewSourceEnum%20%3F;histology_result_text:string%20%3F;histology_result_numeric:decimal%20%3F;histology_result_unit:HistologyResultUnitEnum%20%3F;histology_grade:HistologyGradeEnum%20%3F;mature_glial_implants:NoNotreportedUnknownYesEnum%20%3F;somatic_malignancy_type:SomaticMalignancyTypeEnum%20%3F;somatic_malignancy_type_other:string%20%3F;course_timepoint:CourseTimepointEnum%20%3F;revised_inpc:RevisedInpcEnum%20%3F;mki:MkiEnum%20%3F;histology_other:string%20%3F;tumor_site:TumorSiteEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[Histology],[Thing]^-[Histology])](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..1-++[Histology&#124;age_at_hist_assessment:integer%20%3F;morph_code:string%20%3F;morph_code_system:MorphCodeSystemEnum%20%3F;morph_code_system_version:string%20%3F;top_code:string%20%3F;top_code_system:TopCodeSystemEnum%20%3F;top_code_system_version:string%20%3F;all_type:AllTypeEnum%20%3F;fab_type:FabTypeEnum%20%3F;who_aml:WhoAmlEnum%20%3F;mpal:NoNotreportedUnknownYesEnum%20%3F;mlds:NoNotreportedUnknownYesEnum%20%3F;tam:NoNotreportedUnknownYesEnum%20%3F;secondary_aml:NoNotreportedUnknownYesEnum%20%3F;histology:HistologyEnum%20%3F;molecular_classification:MolecularClassificationEnum%20%3F;molecular_classification_other:string%20%3F;determination_source:DeterminationSourceEnum%20%3F;method:MethodEnum%20%3F;morph_code_txt:string%20%3F;review_source:ReviewSourceEnum%20%3F;histology_result_text:string%20%3F;histology_result_numeric:decimal%20%3F;histology_result_unit:HistologyResultUnitEnum%20%3F;histology_grade:HistologyGradeEnum%20%3F;mature_glial_implants:NoNotreportedUnknownYesEnum%20%3F;somatic_malignancy_type:SomaticMalignancyTypeEnum%20%3F;somatic_malignancy_type_other:string%20%3F;course_timepoint:CourseTimepointEnum%20%3F;revised_inpc:RevisedInpcEnum%20%3F;mki:MkiEnum%20%3F;histology_other:string%20%3F;tumor_site:TumorSiteEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[Histology],[Thing]^-[Histology])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_hist_assessment](age_at_hist_assessment.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the time of this histological assessment.
     * Range: [Integer](types/Integer.md)
 * [time_periods](time_periods.md)  <sub>0..1</sub>
     * Range: [TimePeriod](TimePeriod.md)
 * [morph_code](morph_code.md)  <sub>0..1</sub>
     * Description: The code for the morphology of the subsequent tumor
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
 * [top_code_system](top_code_system.md)  <sub>0..1</sub>
     * Description: The coding system for the code used in TOP_CODE
     * Range: [TopCodeSystemEnum](TopCodeSystemEnum.md)
 * [top_code_system_version](top_code_system_version.md)  <sub>0..1</sub>
     * Description: The version of the coding system indicated in TOP_CODE_SYSTEM
     * Range: [String](types/String.md)
 * [all_type](all_type.md)  <sub>0..1</sub>
     * Description: Leukemia with an acute onset, characterized by the presence of lymphoblasts in the bone marrow and the peripheral blood. It includes the acute B lymphoblastic leukemia and acute T lymphoblastic leukemia.
     * Range: [AllTypeEnum](AllTypeEnum.md)
 * [fab_type](fab_type.md)  <sub>0..1</sub>
     * Description: A classification system for acute myeloid leukemias, acute lymphoblastic leukemias, and myelodysplastic syndromes. It is based on the morphologic and cytochemical evaluation of bone marrow and peripheral blood smears.
     * Range: [FabTypeEnum](FabTypeEnum.md)
 * [who_aml](who_aml.md)  <sub>0..1</sub>
     * Description: A classification of acute myeloid leukemia tumors by the World Health Organization (WHO).
     * Range: [WhoAmlEnum](WhoAmlEnum.md)
 * [mpal](mpal.md)  <sub>0..1</sub>
     * Description: An acute leukemia of ambiguous lineage. It is characterized by the presence of either separate populations of blasts of more than one lineage, or one population of blasts co-expressing markers of more than one lineage.
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [mlds](mlds.md)  <sub>0..1</sub>
     * Description: Acute myeloid leukemia or myelodysplastic syndrome occurring in children with Down syndrome. The acute myeloid leukemia is usually an acute megakaryoblastic leukemia, and is associated with GATA1 gene mutation.
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [tam](tam.md)  <sub>0..1</sub>
     * Description: A myeloid proliferation occurring in newborns with Down syndrome. It is clinically and morphologically indistinguishable from acute myeloid leukemia and is associated with GATA1 mutations. The blasts display morphologic and immunophenotypic features of megakaryocytic lineage. In the majority of patients the myeloid proliferation undergoes spontaneous remission.
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [secondary_aml](secondary_aml.md)  <sub>0..1</sub>
     * Description: Secondary Acute Myeloid Leukemia
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [histology](histology.md)  <sub>0..1</sub>
     * Description: The study of tissues and cells under a microscope (Source: NCI Dictionary of Cancer Terms)
     * Range: [HistologyEnum](HistologyEnum.md)
 * [molecular_classification](molecular_classification.md)  <sub>0..1</sub>
     * Range: [MolecularClassificationEnum](MolecularClassificationEnum.md)
 * [molecular_classification_other](molecular_classification_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" MOLECULAR_CLASSIFICATION
     * Range: [String](types/String.md)
 * [determination_source](determination_source.md)  <sub>0..1</sub>
     * Range: [DeterminationSourceEnum](DeterminationSourceEnum.md)
 * [method](method.md)  <sub>0..1</sub>
     * Description: A systematic course of action that is performed in order to complete a laboratory test.
     * Range: [MethodEnum](MethodEnum.md)
 * [morph_code_txt](morph_code_txt.md)  <sub>0..1</sub>
     * Description: The display text for MORPH_CODE 
     * Range: [String](types/String.md)
 * [review_source](review_source.md)  <sub>0..1</sub>
     * Description: The type of assessment that was used to review.
     * Range: [ReviewSourceEnum](ReviewSourceEnum.md)
 * [histology_result_text](histology_result_text.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [histology_result_numeric](histology_result_numeric.md)  <sub>0..1</sub>
     * Description: The numeric value for the histology result.
     * Range: [Decimal](types/Decimal.md)
 * [histology_result_unit](histology_result_unit.md)  <sub>0..1</sub>
     * Description: The unit being used as the measurement for the histology test.
     * Range: [HistologyResultUnitEnum](HistologyResultUnitEnum.md)
 * [histology_grade](histology_grade.md)  <sub>0..1</sub>
     * Description: A description of a tumor based on how abnormal the cancer cells and tissue look under a microscope and how quickly the cancer cells are likely to grow and spread
     * Range: [HistologyGradeEnum](HistologyGradeEnum.md)
 * [mature_glial_implants](mature_glial_implants.md)  <sub>0..1</sub>
     * Description: A nodule of mature glial tissue that develops in the peritoneum. It is usually accompanied by mature or immature ovarian teratoma.
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [somatic_malignancy_type](somatic_malignancy_type.md)  <sub>0..1</sub>
     * Description: A malignant non-germ cell component that typically develops secondarily within a germ cell tumor. The malignant cellular component is usually sarcomatous or carcinomatous.
     * Range: [SomaticMalignancyTypeEnum](SomaticMalignancyTypeEnum.md)
 * [somatic_malignancy_type_other](somatic_malignancy_type_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" SOMATIC_MALIGNANCY_TYPE
     * Range: [String](types/String.md)
 * [course_timepoint](course_timepoint.md)  <sub>0..1</sub>
     * Description: This variable gives more precise granularity to when an observation occured during the period of the indicated "Course" TIME_PERIOD
     * Range: [CourseTimepointEnum](CourseTimepointEnum.md)
 * [revised_inpc](revised_inpc.md)  <sub>0..1</sub>
     * Description: Revised INPC Prognostic Group (2003)
     * Range: [RevisedInpcEnum](RevisedInpcEnum.md)
 * [mki](mki.md)  <sub>0..1</sub>
     * Description: MKI (Revised INPC)
     * Range: [MkiEnum](MkiEnum.md)
 * [histology_other](histology_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" HISTOLOGY
     * Range: [String](types/String.md)
 * [tumor_site](tumor_site.md)  <sub>0..1</sub>
     * Range: [TumorSiteEnum](TumorSiteEnum.md)
 * [subjects](subjects.md)  <sub>1..1</sub>
     * Range: [Subject](Subject.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
