
# Class: LaboratoryTest




URI: [https://w3id.org/pcdc/model/LaboratoryTest](https://w3id.org/pcdc/model/LaboratoryTest)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[LaboratoryTest&#124;age_at_lab:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;lab_category:LabCategoryEnum%20%3F;lab_test:LabTestEnum%20%3F;lab_test_other:string%20%3F;specimen:SpecimenEnum%20%3F;specimen_other:string%20%3F;lab_result:string%20%3F;lab_result_categorical:LabResultCategoricalEnum%20%3F;lab_result_numeric:integer%20%3F;lab_result_unit:LabResultUnitEnum%20%3F;lab_method:LabMethodEnum%20%3F;lab_seq_method:LabSeqMethodEnum%20%3F;threshold_high:integer%20%3F;threshold_low:integer%20%3F;pmid_ref:integer%20%3F;bm_morphology:BmMorphologyEnum%20%3F;traumatic_tap:NoNotreportedUnknownYesEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[LaboratoryTest])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[LaboratoryTest&#124;age_at_lab:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;lab_category:LabCategoryEnum%20%3F;lab_test:LabTestEnum%20%3F;lab_test_other:string%20%3F;specimen:SpecimenEnum%20%3F;specimen_other:string%20%3F;lab_result:string%20%3F;lab_result_categorical:LabResultCategoricalEnum%20%3F;lab_result_numeric:integer%20%3F;lab_result_unit:LabResultUnitEnum%20%3F;lab_method:LabMethodEnum%20%3F;lab_seq_method:LabSeqMethodEnum%20%3F;threshold_high:integer%20%3F;threshold_low:integer%20%3F;pmid_ref:integer%20%3F;bm_morphology:BmMorphologyEnum%20%3F;traumatic_tap:NoNotreportedUnknownYesEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[LaboratoryTest])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_lab](age_at_lab.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the time of the laboratory test.
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
 * [lab_category](lab_category.md)  <sub>0..1</sub>
     * Description: The category of laboratory test performed on the subject.
     * Range: [LabCategoryEnum](LabCategoryEnum.md)
 * [lab_test](lab_test.md)  <sub>0..1</sub>
     * Description: A medical procedure that involves testing a sample of blood, urine, or other substance from the body. Laboratory tests can help determine a diagnosis, plan treatment, check to see if treatment is working, or monitor the disease over time Source: NCI Dictionary of Cancer Terms)
     * Range: [LabTestEnum](LabTestEnum.md)
 * [lab_test_other](lab_test_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" LAB_TEST
     * Range: [String](types/String.md)
 * [specimen](specimen.md)  <sub>0..1</sub>
     * Description: The biological specimen of the subject used for the laboratory test. 
     * Range: [SpecimenEnum](SpecimenEnum.md)
 * [specimen_other](specimen_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" SPECIMEN
     * Range: [String](types/String.md)
 * [lab_result](lab_result.md)  <sub>0..1</sub>
     * Description: The string/text result of the laboratory test.
     * Range: [String](types/String.md)
 * [lab_result_categorical](lab_result_categorical.md)  <sub>0..1</sub>
     * Range: [LabResultCategoricalEnum](LabResultCategoricalEnum.md)
 * [lab_result_numeric](lab_result_numeric.md)  <sub>0..1</sub>
     * Description: The numeric result of the laboratory test.
     * Range: [Integer](types/Integer.md)
 * [lab_result_unit](lab_result_unit.md)  <sub>0..1</sub>
     * Description: The units used for the numeric result of the laboratory test,
     * Range: [LabResultUnitEnum](LabResultUnitEnum.md)
 * [lab_method](lab_method.md)  <sub>0..1</sub>
     * Description: A systematic course of action that is performed in order to complete a laboratory test.
     * Range: [LabMethodEnum](LabMethodEnum.md)
 * [lab_seq_method](lab_seq_method.md)  <sub>0..1</sub>
     * Description: The number of molecules of a particular type on or in a cell or part of a cell. Usually applied to specific genes or to plasmids within a bacterium.
     * Range: [LabSeqMethodEnum](LabSeqMethodEnum.md)
 * [threshold_high](threshold_high.md)  <sub>0..1</sub>
     * Description: The maximum level that must be exceeded for a certain reaction to occur or be manifested.
     * Range: [Integer](types/Integer.md)
 * [threshold_low](threshold_low.md)  <sub>0..1</sub>
     * Description: The minimum level that must be attained for a certain reaction to occur or be manifested.
     * Range: [Integer](types/Integer.md)
 * [pmid_ref](pmid_ref.md)  <sub>0..1</sub>
     * Description: A globally unique identifier for a biomedical article, as assigned by PubMed.
     * Range: [Integer](types/Integer.md)
 * [bm_morphology](bm_morphology.md)  <sub>0..1</sub>
     * Description: The morphology of bone marrow blasts 
     * Range: [BmMorphologyEnum](BmMorphologyEnum.md)
 * [traumatic_tap](traumatic_tap.md)  <sub>0..1</sub>
     * Description: Was the lumbar puncture artifically contaminated by peripheral blood?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
