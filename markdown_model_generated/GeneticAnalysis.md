
# Class: GeneticAnalysis




URI: [https://w3id.org/pcdc/model/GeneticAnalysis](https://w3id.org/pcdc/model/GeneticAnalysis)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[GeneticAnalysis&#124;age_at_genetic_analysis:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;lesion_classification:LesionClassificationEnum%20%3F;method:MethodEnum%20%3F;specimen:SpecimenEnum%20%3F;genomic_source_class:GenomicSourceClassEnum%20%3F;common_name:CommonNameEnum%20%3F;status:StatusEnum%20%3F;gene:string%20%3F;chromosome:string%20%3F;mutation_type:MutationTypeEnum%20%3F;mutation_type_other:string%20%3F;expression_consequence:ExpressionConsequenceEnum%20%3F;chromosomal_consequence:ChromosomalConsequenceEnum%20%3F;genomic_region:GenomicRegionEnum%20%3F;allelic_state:AllelicStateEnum%20%3F;inheritance_pattern:InheritancePatternEnum%20%3F;parental_status:ParentalStatusEnum%20%3F;hgvs_coding:string%20%3F;hgvs_protein:string%20%3F;iscn:string%20%3F;clingen_id:string%20%3F;copy_number_variation:CopyNumberVariationEnum%20%3F;copy_number:integer%20%3F;amplification:NoNotreportedUnknownYesEnum%20%3F;allelic_frequency:integer%20%3F;gene2:string%20%3F;mosaicism:NoNotreportedUnknownYesEnum%20%3F;mosaicism_percent:integer%20%3F;alt_status:AltStatusEnum%20%3F;total_chromosomes:integer%20%3F;independent_aberations:integer%20%3F;cells_in_metaphase:integer%20%3F;karyotype_status:KaryotypeStatusEnum%20%3F;dna_index:DnaIndexEnum%20%3F;dna_index_numeric:integer%20%3F;cytodifferentiation:CytodifferentiationEnum%20%3F;mitotic_rate:MitoticRateEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[GeneticAnalysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[GeneticAnalysis&#124;age_at_genetic_analysis:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;lesion_classification:LesionClassificationEnum%20%3F;method:MethodEnum%20%3F;specimen:SpecimenEnum%20%3F;genomic_source_class:GenomicSourceClassEnum%20%3F;common_name:CommonNameEnum%20%3F;status:StatusEnum%20%3F;gene:string%20%3F;chromosome:string%20%3F;mutation_type:MutationTypeEnum%20%3F;mutation_type_other:string%20%3F;expression_consequence:ExpressionConsequenceEnum%20%3F;chromosomal_consequence:ChromosomalConsequenceEnum%20%3F;genomic_region:GenomicRegionEnum%20%3F;allelic_state:AllelicStateEnum%20%3F;inheritance_pattern:InheritancePatternEnum%20%3F;parental_status:ParentalStatusEnum%20%3F;hgvs_coding:string%20%3F;hgvs_protein:string%20%3F;iscn:string%20%3F;clingen_id:string%20%3F;copy_number_variation:CopyNumberVariationEnum%20%3F;copy_number:integer%20%3F;amplification:NoNotreportedUnknownYesEnum%20%3F;allelic_frequency:integer%20%3F;gene2:string%20%3F;mosaicism:NoNotreportedUnknownYesEnum%20%3F;mosaicism_percent:integer%20%3F;alt_status:AltStatusEnum%20%3F;total_chromosomes:integer%20%3F;independent_aberations:integer%20%3F;cells_in_metaphase:integer%20%3F;karyotype_status:KaryotypeStatusEnum%20%3F;dna_index:DnaIndexEnum%20%3F;dna_index_numeric:integer%20%3F;cytodifferentiation:CytodifferentiationEnum%20%3F;mitotic_rate:MitoticRateEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[GeneticAnalysis])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_genetic_analysis](age_at_genetic_analysis.md)  <sub>0..1</sub>
     * Description: The age, in days, of the subject at the time of this analysis.
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
 * [lesion_classification](lesion_classification.md)  <sub>0..1</sub>
     * Description: The classification of a lesion of interest.
     * Range: [LesionClassificationEnum](LesionClassificationEnum.md)
 * [method](method.md)  <sub>0..1</sub>
     * Description: The testing method/technique used to generate the observed results.
     * Range: [MethodEnum](MethodEnum.md)
 * [specimen](specimen.md)  <sub>0..1</sub>
     * Description: The biological specimen of the subject used for the laboratory test. 
     * Range: [SpecimenEnum](SpecimenEnum.md)
 * [genomic_source_class](genomic_source_class.md)  <sub>0..1</sub>
     * Description: The genomic class of the specimen being analyzed, for example, germline for inherited genome and somatic for cancer genome.
     * Range: [GenomicSourceClassEnum](GenomicSourceClassEnum.md)
 * [common_name](common_name.md)  <sub>0..1</sub>
     * Description: The non-standardized name of the mutation represented by this observation.
     * Range: [CommonNameEnum](CommonNameEnum.md)
 * [status](status.md)  <sub>0..1</sub>
     * Description: Is this mutation/abnormality present in this subject?
     * Range: [StatusEnum](StatusEnum.md)
 * [gene](gene.md)  <sub>0..1</sub>
     * Description: A gene targeted for mutation analysis, identified in HUGO Gene Nomenclature Committee (HGNC) notation.
     * Range: [String](types/String.md)
 * [chromosome](chromosome.md)  <sub>0..1</sub>
     * Description: One of the bodies in the cell nucleus that is the bearer of genes, has the form of a delicate chromatin filament during interphase, contracts to form a compact cylinder segmented into two arms by the centromere during metaphase and anaphase stages of cell division, and is capable of reproducing its physical and chemical structure through successive cell divisions.
     * Range: [String](types/String.md)
 * [mutation_type](mutation_type.md)  <sub>0..1</sub>
     * Description: The type of mutation detected by this genetic analysis.
     * Range: [MutationTypeEnum](MutationTypeEnum.md)
 * [mutation_type_other](mutation_type_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" MUTATION_TYPE
     * Range: [String](types/String.md)
 * [expression_consequence](expression_consequence.md)  <sub>0..1</sub>
     * Range: [ExpressionConsequenceEnum](ExpressionConsequenceEnum.md)
 * [chromosomal_consequence](chromosomal_consequence.md)  <sub>0..1</sub>
     * Range: [ChromosomalConsequenceEnum](ChromosomalConsequenceEnum.md)
 * [genomic_region](genomic_region.md)  <sub>0..1</sub>
     * Range: [GenomicRegionEnum](GenomicRegionEnum.md)
 * [allelic_state](allelic_state.md)  <sub>0..1</sub>
     * Description: The genetic condition of a zygote, especially with respect to its being a homozygote or a heterozygote.
     * Range: [AllelicStateEnum](AllelicStateEnum.md)
 * [inheritance_pattern](inheritance_pattern.md)  <sub>0..1</sub>
     * Range: [InheritancePatternEnum](InheritancePatternEnum.md)
 * [parental_status](parental_status.md)  <sub>0..1</sub>
     * Range: [ParentalStatusEnum](ParentalStatusEnum.md)
 * [hgvs_coding](hgvs_coding.md)  <sub>0..1</sub>
     * Description: If this mutation is described at the sequence/chromosome level, this is its representation in HGVS nomenclature (cHGVS).
     * Range: [String](types/String.md)
 * [hgvs_protein](hgvs_protein.md)  <sub>0..1</sub>
     * Description: If this mutation is described at the translational product level, this is its representation in HGVS nomenclature (pHGVS)
     * Range: [String](types/String.md)
 * [iscn](iscn.md)  <sub>0..1</sub>
     * Description: If this mutation is described by the structure of the resulting chromosomes, this is its representation in ISCN nomenclature.
     * Range: [String](types/String.md)
 * [clingen_id](clingen_id.md)  <sub>0..1</sub>
     * Description: This ID will allow users to find the most current clinical significance classification for this instance of variation
     * Range: [String](types/String.md)
 * [copy_number_variation](copy_number_variation.md)  <sub>0..1</sub>
     * Description: If there was a change in the number of gene copies, this variable specifies the type of change.
     * Range: [CopyNumberVariationEnum](CopyNumberVariationEnum.md)
 * [copy_number](copy_number.md)  <sub>0..1</sub>
     * Description: The number of gene copies resulting from this mutation.
     * Range: [Integer](types/Integer.md)
 * [amplification](amplification.md)  <sub>0..1</sub>
     * Description: Was the copy number gain high enough to be reported as a gene amplification?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [allelic_frequency](allelic_frequency.md)  <sub>0..1</sub>
     * Description: The incidence of this mutation in a population (%).
     * Range: [Integer](types/Integer.md)
 * [gene2](gene2.md)  <sub>0..1</sub>
     * Description: This should be used for mutations that span two gene locations (fusion, translocation, inversion, etc.). The gene name should be identified in HUGO Gene Nomenclature Committee (HGNC) notation.
     * Range: [String](types/String.md)
 * [mosaicism](mosaicism.md)  <sub>0..1</sub>
     * Description: Does this subject have two or more genetically different sets of cells in their body?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [mosaicism_percent](mosaicism_percent.md)  <sub>0..1</sub>
     * Description: The numeric level of mosaicism in this subject.
     * Range: [Integer](types/Integer.md)
 * [alt_status](alt_status.md)  <sub>0..1</sub>
     * Description: Activitation of the Alternative Lengthening of Telomeres (ALT) pathway.
     * Range: [AltStatusEnum](AltStatusEnum.md)
 * [total_chromosomes](total_chromosomes.md)  <sub>0..1</sub>
     * Description: The number of chromosomes detected on the karyotype through which this abnormality was detected.
     * Range: [Integer](types/Integer.md)
 * [independent_aberations](independent_aberations.md)  <sub>0..1</sub>
     * Description: The total number of aberrations / mutations / abnormalities detected on the karyotype through which this abnormality was detected.
     * Range: [Integer](types/Integer.md)
 * [cells_in_metaphase](cells_in_metaphase.md)  <sub>0..1</sub>
     * Description: The number of cells in the sample that were arrested in the metaphase stage of the cell cycle and used for the karyotype through which this abnormality was detected.
     * Range: [Integer](types/Integer.md)
 * [karyotype_status](karyotype_status.md)  <sub>0..1</sub>
     * Description: Karyotype Status
     * Range: [KaryotypeStatusEnum](KaryotypeStatusEnum.md)
 * [dna_index](dna_index.md)  <sub>0..1</sub>
     * Range: [DnaIndexEnum](DnaIndexEnum.md)
 * [dna_index_numeric](dna_index_numeric.md)  <sub>0..1</sub>
     * Description: The ratio of the DNA content or chromosome number in a tumor sample compared to that in a normal sample.
     * Range: [Integer](types/Integer.md)
 * [cytodifferentiation](cytodifferentiation.md)  <sub>0..1</sub>
     * Description: Cytodifferentiation Score
     * Range: [CytodifferentiationEnum](CytodifferentiationEnum.md)
 * [mitotic_rate](mitotic_rate.md)  <sub>0..1</sub>
     * Description: Mitoses Count
     * Range: [MitoticRateEnum](MitoticRateEnum.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
