
# Class: Genetic Analysis




URI: [https://w3id.org/pcdc/model/GeneticAnalysis](https://w3id.org/pcdc/model/GeneticAnalysis)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..1-++[GeneticAnalysis&#124;age_at_genetic_analysis:integer%20%3F;method:MethodEnum%20%3F;specimen:SpecimenEnum%20%3F;common_name:CommonNameEnum%20%3F;karyotype_status:KaryotypeStatusEnum%20%3F;status:StatusEnum%20%3F;iscn:string%20%3F;total_chromosomes:decimal%20%3F;chromosome:string%20%3F;gene:string%20%3F;gene2:string%20%3F;variation_type:VariationTypeEnum%20%3F;variation_type_other:string%20%3F;copy_number_variation:CopyNumberVariationEnum%20%3F;copy_number:decimal%20%3F;hgvs_coding:string%20%3F;hgvs_protein:string%20%3F;dna_index_numeric:decimal%20%3F;method_other:string%20%3F;independent_aberations:decimal%20%3F;cells_in_metaphase:decimal%20%3F;common_name_other:string%20%3F;mutant_allele_fraction:decimal%20%3F;genomic_source_class:GenomicSourceClassEnum%20%3F;expression_consequence:ExpressionConsequenceEnum%20%3F;chromosomal_consequence:ChromosomalConsequenceEnum%20%3F;allelic_state:AllelicStateEnum%20%3F;allelic_frequency:decimal%20%3F;external_ref_id:string%20%3F;external_ref_id_system:ExternalRefIdSystemEnum%20%3F;mosaicism_percent:decimal%20%3F;variation_effect:VariationEffectEnum%20%3F;inheritance_pattern:InheritancePatternEnum%20%3F;parental_status:ParentalStatusEnum%20%3F;hgvs_coding_transcript:string%20%3F;hgvs_protein_transcript:string%20%3F;reported_significance:ReportedSignificanceEnum%20%3F;associated_condition:AssociatedConditionEnum%20%3F;associated_condition_other:string%20%3F;review_source:ReviewSourceEnum%20%3F;tumor_classification:TumorClassificationEnum%20%3F;course_timepoint:CourseTimepointEnum%20%3F;specimen_other:string%20%3F;biological_analyte:BiologicalAnalyteEnum%20%3F;biological_analyte_other:string%20%3F;source_pct:SourcePctEnum%20%3F;source_pct_numeric:decimal%20%3F;tkd_involvement:NoNotreportedUnknownYesEnum%20%3F;maf:MafEnum%20%3F;maf_numeric:decimal%20%3F;clonal_status:ClonalStatusEnum%20%3F;dna_index:DnaIndexEnum%20%3F;cytodifferentiation:CytodifferentiationEnum%20%3F;mitotic_rate:MitoticRateEnum%20%3F;mutated_allele_frequency:integer%20%3F;cascade_testing:NoNotreportedUnknownYesEnum%20%3F;alt_status:AltStatusEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[GeneticAnalysis],[Thing]^-[GeneticAnalysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..1-++[GeneticAnalysis&#124;age_at_genetic_analysis:integer%20%3F;method:MethodEnum%20%3F;specimen:SpecimenEnum%20%3F;common_name:CommonNameEnum%20%3F;karyotype_status:KaryotypeStatusEnum%20%3F;status:StatusEnum%20%3F;iscn:string%20%3F;total_chromosomes:decimal%20%3F;chromosome:string%20%3F;gene:string%20%3F;gene2:string%20%3F;variation_type:VariationTypeEnum%20%3F;variation_type_other:string%20%3F;copy_number_variation:CopyNumberVariationEnum%20%3F;copy_number:decimal%20%3F;hgvs_coding:string%20%3F;hgvs_protein:string%20%3F;dna_index_numeric:decimal%20%3F;method_other:string%20%3F;independent_aberations:decimal%20%3F;cells_in_metaphase:decimal%20%3F;common_name_other:string%20%3F;mutant_allele_fraction:decimal%20%3F;genomic_source_class:GenomicSourceClassEnum%20%3F;expression_consequence:ExpressionConsequenceEnum%20%3F;chromosomal_consequence:ChromosomalConsequenceEnum%20%3F;allelic_state:AllelicStateEnum%20%3F;allelic_frequency:decimal%20%3F;external_ref_id:string%20%3F;external_ref_id_system:ExternalRefIdSystemEnum%20%3F;mosaicism_percent:decimal%20%3F;variation_effect:VariationEffectEnum%20%3F;inheritance_pattern:InheritancePatternEnum%20%3F;parental_status:ParentalStatusEnum%20%3F;hgvs_coding_transcript:string%20%3F;hgvs_protein_transcript:string%20%3F;reported_significance:ReportedSignificanceEnum%20%3F;associated_condition:AssociatedConditionEnum%20%3F;associated_condition_other:string%20%3F;review_source:ReviewSourceEnum%20%3F;tumor_classification:TumorClassificationEnum%20%3F;course_timepoint:CourseTimepointEnum%20%3F;specimen_other:string%20%3F;biological_analyte:BiologicalAnalyteEnum%20%3F;biological_analyte_other:string%20%3F;source_pct:SourcePctEnum%20%3F;source_pct_numeric:decimal%20%3F;tkd_involvement:NoNotreportedUnknownYesEnum%20%3F;maf:MafEnum%20%3F;maf_numeric:decimal%20%3F;clonal_status:ClonalStatusEnum%20%3F;dna_index:DnaIndexEnum%20%3F;cytodifferentiation:CytodifferentiationEnum%20%3F;mitotic_rate:MitoticRateEnum%20%3F;mutated_allele_frequency:integer%20%3F;cascade_testing:NoNotreportedUnknownYesEnum%20%3F;alt_status:AltStatusEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[GeneticAnalysis],[Thing]^-[GeneticAnalysis])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_genetic_analysis](age_at_genetic_analysis.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the time of this analysis.
     * Range: [Integer](types/Integer.md)
 * [method](method.md)  <sub>0..1</sub>
     * Description: A systematic course of action that is performed in order to complete a laboratory test.
     * Range: [MethodEnum](MethodEnum.md)
 * [specimen](specimen.md)  <sub>0..1</sub>
     * Description: The type of specimen analyzed.
     * Range: [SpecimenEnum](SpecimenEnum.md)
 * [common_name](common_name.md)  <sub>0..1</sub>
     * Description: The non-standardized name of the mutation represented by this observation.
     * Range: [CommonNameEnum](CommonNameEnum.md)
 * [karyotype_status](karyotype_status.md)  <sub>0..1</sub>
     * Description: The status of the subject's karyotype.
     * Range: [KaryotypeStatusEnum](KaryotypeStatusEnum.md)
 * [status](status.md)  <sub>0..1</sub>
     * Description: Is this mutation/abnormality present in this subject?
     * Range: [StatusEnum](StatusEnum.md)
 * [iscn](iscn.md)  <sub>0..1</sub>
     * Description: If this mutation is described by the structure of the resulting chromosomes, this is its representation in ISCN nomenclature.
     * Range: [String](types/String.md)
 * [total_chromosomes](total_chromosomes.md)  <sub>0..1</sub>
     * Description: The number of chromosomes detected on the karyotype through which this abnormality was detected.
     * Range: [Decimal](types/Decimal.md)
 * [chromosome](chromosome.md)  <sub>0..1</sub>
     * Description: A structure found in cells that is comprised of a strand of linearized double-stranded DNA plus proteins that package the DNA in a condensed coil form and regulate chromosomal function.
     * Range: [String](types/String.md)
 * [gene](gene.md)  <sub>0..1</sub>
     * Description: A gene targeted for mutation analysis, identified in HUGO Gene Nomenclature Committee (HGNC) notation.
     * Range: [String](types/String.md)
 * [gene2](gene2.md)  <sub>0..1</sub>
     * Description: This should be used for mutations that span two gene locations (fusion, translocation, inversion, etc.). The gene name should be identified in HUGO Gene Nomenclature Committee (HGNC) notation.
     * Range: [String](types/String.md)
 * [variation_type](variation_type.md)  <sub>0..1</sub>
     * Description: The type of variation detected by this genetic analysis.
     * Range: [VariationTypeEnum](VariationTypeEnum.md)
 * [variation_type_other](variation_type_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" MUTATION_TYPE
     * Range: [String](types/String.md)
 * [copy_number_variation](copy_number_variation.md)  <sub>0..1</sub>
     * Description: If there was a change in the number of gene copies, this variable specifies the type of change.
     * Range: [CopyNumberVariationEnum](CopyNumberVariationEnum.md)
 * [copy_number](copy_number.md)  <sub>0..1</sub>
     * Description: The number of gene copies resulting from this mutation.
     * Range: [Decimal](types/Decimal.md)
 * [hgvs_coding](hgvs_coding.md)  <sub>0..1</sub>
     * Description: If this mutation is described at the sequence/chromosome level, this is its representation in HGVS nomenclature (cHGVS).
     * Range: [String](types/String.md)
 * [hgvs_protein](hgvs_protein.md)  <sub>0..1</sub>
     * Description: If this mutation is described at the translational product level, this is its representation in HGVS nomenclature (pHGVS)
     * Range: [String](types/String.md)
 * [dna_index_numeric](dna_index_numeric.md)  <sub>0..1</sub>
     * Description: The ratio of the DNA content or chromosome number in a tumor sample compared to that in a normal sample.
     * Range: [Decimal](types/Decimal.md)
 * [time_periods](time_periods.md)  <sub>0..1</sub>
     * Range: [TimePeriod](TimePeriod.md)
 * [method_other](method_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" LAB_METHOD
     * Range: [String](types/String.md)
 * [independent_aberations](independent_aberations.md)  <sub>0..1</sub>
     * Description: The total number of aberrations / mutations / abnormalities detected on the karyotype through which this abnormality was detected.
     * Range: [Decimal](types/Decimal.md)
 * [cells_in_metaphase](cells_in_metaphase.md)  <sub>0..1</sub>
     * Description: The number of cells in the sample that were arrested in the metaphase stage of the cell cycle and used for the karyotype through which this abnormality was detected.
     * Range: [Decimal](types/Decimal.md)
 * [common_name_other](common_name_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" COMMON_NAME
     * Range: [String](types/String.md)
 * [mutant_allele_fraction](mutant_allele_fraction.md)  <sub>0..1</sub>
     * Description: A measure of the percentage of mutant alleles within the totality of alleles in any given sample
     * Range: [Decimal](types/Decimal.md)
 * [genomic_source_class](genomic_source_class.md)  <sub>0..1</sub>
     * Description: The genomic class of the specimen being analyzed, for example, germline for inherited genome and somatic for cancer genome.
     * Range: [GenomicSourceClassEnum](GenomicSourceClassEnum.md)
 * [expression_consequence](expression_consequence.md)  <sub>0..1</sub>
     * Range: [ExpressionConsequenceEnum](ExpressionConsequenceEnum.md)
 * [chromosomal_consequence](chromosomal_consequence.md)  <sub>0..1</sub>
     * Description: Chromosomal abnormalities can have many different effects, depending on the specific abnormality. For example, an extra copy of chromosome 21 causes Down syndrome (trisomy 21). Chromosomal abnormalities can also cause miscarriage, disease, or problems in growth or development.
     * Range: [ChromosomalConsequenceEnum](ChromosomalConsequenceEnum.md)
 * [allelic_state](allelic_state.md)  <sub>0..1</sub>
     * Description: The level of occurrence of a single DNA Marker within a set of chromosomes. Heterozygous indicates the DNA Marker is only present in one of the two genes contained in homologous chromosomes. Homozygous indicates the DNA Marker is present in both genes contained in homologous chromosomes. Hemizygous indicates the DNA Marker exists in the only single copy of a gene in a non-homologous chromosome (The male X and Y chromosome are non-homologous). Hemiplasmic indicates that the DNA Marker is present in some but not all of the copies of mitochondrial DNA. Homoplasmic indicates that the DNA Maker is present in all of the copies of mitochondrial DNA. (Source: LOINC)
     * Range: [AllelicStateEnum](AllelicStateEnum.md)
 * [allelic_frequency](allelic_frequency.md)  <sub>0..1</sub>
     * Description: The incidence of this mutation in the tumor (%).
     * Range: [Decimal](types/Decimal.md)
 * [external_ref_id](external_ref_id.md)  <sub>0..1</sub>
     * Description: An ID to an external knowledge base that holds additional information about this genetic variant.
     * Range: [String](types/String.md)
 * [external_ref_id_system](external_ref_id_system.md)  <sub>0..1</sub>
     * Description: The name of the external knowledge base from which the EXTERNAL_REF_ID is drawn.
     * Range: [ExternalRefIdSystemEnum](ExternalRefIdSystemEnum.md)
 * [mosaicism_percent](mosaicism_percent.md)  <sub>0..1</sub>
     * Description: The numeric level of mosaicism in this subject.
     * Range: [Decimal](types/Decimal.md)
 * [variation_effect](variation_effect.md)  <sub>0..1</sub>
     * Range: [VariationEffectEnum](VariationEffectEnum.md)
 * [inheritance_pattern](inheritance_pattern.md)  <sub>0..1</sub>
     * Range: [InheritancePatternEnum](InheritancePatternEnum.md)
 * [parental_status](parental_status.md)  <sub>0..1</sub>
     * Range: [ParentalStatusEnum](ParentalStatusEnum.md)
 * [hgvs_coding_transcript](hgvs_coding_transcript.md)  <sub>0..1</sub>
     * Description: This is the transcript used in the HGVS expression for this mutation.
     * Range: [String](types/String.md)
 * [hgvs_protein_transcript](hgvs_protein_transcript.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [reported_significance](reported_significance.md)  <sub>0..1</sub>
     * Description: The reported ACMG clinical significance of this genetic variation
     * Range: [ReportedSignificanceEnum](ReportedSignificanceEnum.md)
 * [associated_condition](associated_condition.md)  <sub>0..1</sub>
     * Description: A condition associated with the reported genetic mutation 
     * Range: [AssociatedConditionEnum](AssociatedConditionEnum.md)
 * [associated_condition_other](associated_condition_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" ASSOCIATED_CONDITION
     * Range: [String](types/String.md)
 * [review_source](review_source.md)  <sub>0..1</sub>
     * Description: The type of assessment that was used to review.
     * Range: [ReviewSourceEnum](ReviewSourceEnum.md)
 * [tumor_classification](tumor_classification.md)  <sub>0..1</sub>
     * Description: The classification of a tumor based primarily on histopathological characteristics.
     * Range: [TumorClassificationEnum](TumorClassificationEnum.md)
 * [course_timepoint](course_timepoint.md)  <sub>0..1</sub>
     * Description: This variable gives more precise granularity to when an observation occured during the period of the indicated "Course" TIME_PERIOD
     * Range: [CourseTimepointEnum](CourseTimepointEnum.md)
 * [specimen_other](specimen_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" SPECIMEN
     * Range: [String](types/String.md)
 * [biological_analyte](biological_analyte.md)  <sub>0..1</sub>
     * Description: A biological substance of interest that needs detection.
     * Range: [BiologicalAnalyteEnum](BiologicalAnalyteEnum.md)
 * [biological_analyte_other](biological_analyte_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" BIOLOGICAL_ANALYTE
     * Range: [String](types/String.md)
 * [source_pct](source_pct.md)  <sub>0..1</sub>
     * Description: Percent of tumor cells in the sample (categorical)
     * Range: [SourcePctEnum](SourcePctEnum.md)
 * [source_pct_numeric](source_pct_numeric.md)  <sub>0..1</sub>
     * Description: Percent of tumor cells in the sample (numeric)
     * Range: [Decimal](types/Decimal.md)
 * [tkd_involvement](tkd_involvement.md)  <sub>0..1</sub>
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [maf](maf.md)  <sub>0..1</sub>
     * Range: [MafEnum](MafEnum.md)
 * [maf_numeric](maf_numeric.md)  <sub>0..1</sub>
     * Description: A measure of the percentage of mutant alleles within the totality of alleles in any given sample
     * Range: [Decimal](types/Decimal.md)
 * [clonal_status](clonal_status.md)  <sub>0..1</sub>
     * Range: [ClonalStatusEnum](ClonalStatusEnum.md)
 * [dna_index](dna_index.md)  <sub>0..1</sub>
     * Description: The categorical result of the DNA index for this subject
     * Range: [DnaIndexEnum](DnaIndexEnum.md)
 * [cytodifferentiation](cytodifferentiation.md)  <sub>0..1</sub>
     * Description: Cytodifferentiation Score
     * Range: [CytodifferentiationEnum](CytodifferentiationEnum.md)
 * [mitotic_rate](mitotic_rate.md)  <sub>0..1</sub>
     * Description: Mitoses Count
     * Range: [MitoticRateEnum](MitoticRateEnum.md)
 * [mutated_allele_frequency](mutated_allele_frequency.md)  <sub>0..1</sub>
     * Description: The incidence of this mutation in the tumor (%).
     * Range: [Integer](types/Integer.md)
 * [cascade_testing](cascade_testing.md)  <sub>0..1</sub>
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [alt_status](alt_status.md)  <sub>0..1</sub>
     * Description: Activitation of the Alternative Lengthening of Telomeres (ALT) pathway.
     * Range: [AltStatusEnum](AltStatusEnum.md)
 * [subjects](subjects.md)  <sub>1..1</sub>
     * Range: [Subject](Subject.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
