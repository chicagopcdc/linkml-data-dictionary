
# Class: Laboratory Test




URI: [https://w3id.org/pcdc/model/LaboratoryTest](https://w3id.org/pcdc/model/LaboratoryTest)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..1-++[LaboratoryTest&#124;age_at_lab:integer%20%3F;category:CategoryEnum%20%3F;test:TestEnum%20%3F;specimen:SpecimenEnum%20%3F;specimen_other:string%20%3F;method:MethodEnum%20%3F;method_other:string%20%3F;result_text:string%20%3F;result_numeric:decimal%20%3F;result_unit:ResultUnitEnum%20%3F;traumatic_tap:NoNotreportedUnknownYesEnum%20%3F;bm_morphology:BmMorphologyEnum%20%3F;result:NegativeNotreportedPositiveUnknownEnum%20%3F;threshold_level:ThresholdLevelEnum%20%3F;threshold_high:decimal%20%3F;thredhold_low:decimal%20%3F;seq_method:SeqMethodEnum%20%3F;threshold_low:decimal%20%3F;pmid_ref:decimal%20%3F;malignant_cells:AbsentNotreportedPresentUnknownEnum%20%3F;course_timepoint:CourseTimepointEnum%20%3F;test_other:string%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[LaboratoryTest],[Thing]^-[LaboratoryTest])](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..1-++[LaboratoryTest&#124;age_at_lab:integer%20%3F;category:CategoryEnum%20%3F;test:TestEnum%20%3F;specimen:SpecimenEnum%20%3F;specimen_other:string%20%3F;method:MethodEnum%20%3F;method_other:string%20%3F;result_text:string%20%3F;result_numeric:decimal%20%3F;result_unit:ResultUnitEnum%20%3F;traumatic_tap:NoNotreportedUnknownYesEnum%20%3F;bm_morphology:BmMorphologyEnum%20%3F;result:NegativeNotreportedPositiveUnknownEnum%20%3F;threshold_level:ThresholdLevelEnum%20%3F;threshold_high:decimal%20%3F;thredhold_low:decimal%20%3F;seq_method:SeqMethodEnum%20%3F;threshold_low:decimal%20%3F;pmid_ref:decimal%20%3F;malignant_cells:AbsentNotreportedPresentUnknownEnum%20%3F;course_timepoint:CourseTimepointEnum%20%3F;test_other:string%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[LaboratoryTest],[Thing]^-[LaboratoryTest])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_lab](age_at_lab.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the time of the laboratory test.
     * Range: [Integer](types/Integer.md)
 * [time_periods](time_periods.md)  <sub>0..1</sub>
     * Range: [TimePeriod](TimePeriod.md)
 * [category](category.md)  <sub>0..1</sub>
     * Description: The category of laboratory test performed on the subject.
     * Range: [CategoryEnum](CategoryEnum.md)
 * [test](test.md)  <sub>0..1</sub>
     * Description: A medical procedure that involves testing a sample of blood, urine, or other substance from the body. Laboratory tests can help determine a diagnosis, plan treatment, check to see if treatment is working, or monitor the disease over time Source: NCI Dictionary of Cancer Terms)
     * Range: [TestEnum](TestEnum.md)
 * [specimen](specimen.md)  <sub>0..1</sub>
     * Description: The type of specimen analyzed.
     * Range: [SpecimenEnum](SpecimenEnum.md)
 * [specimen_other](specimen_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" SPECIMEN
     * Range: [String](types/String.md)
 * [method](method.md)  <sub>0..1</sub>
     * Description: A systematic course of action that is performed in order to complete a laboratory test.
     * Range: [MethodEnum](MethodEnum.md)
 * [method_other](method_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" LAB_METHOD
     * Range: [String](types/String.md)
 * [result_text](result_text.md)  <sub>0..1</sub>
     * Description: The string/text result of the laboratory test.
     * Range: [String](types/String.md)
 * [result_numeric](result_numeric.md)  <sub>0..1</sub>
     * Description: The numeric result of the laboratory test.
     * Range: [Decimal](types/Decimal.md)
 * [result_unit](result_unit.md)  <sub>0..1</sub>
     * Description: The units used for the numeric result of the laboratory test.
     * Range: [ResultUnitEnum](ResultUnitEnum.md)
 * [traumatic_tap](traumatic_tap.md)  <sub>0..1</sub>
     * Description: Contamination of a cerebrospinal fluid sample by red blood cells greater than 10/mm3.
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [bm_morphology](bm_morphology.md)  <sub>0..1</sub>
     * Description: The morphology of bone marrow blasts.
     * Range: [BmMorphologyEnum](BmMorphologyEnum.md)
 * [result](result.md)  <sub>0..1</sub>
     * Description: The text result of the laboratory test.
     * Range: [NegativeNotreportedPositiveUnknownEnum](NegativeNotreportedPositiveUnknownEnum.md)
 * [threshold_level](threshold_level.md)  <sub>0..1</sub>
     * Description: The point at which a psychological or physiological effect begins to be produced.
     * Range: [ThresholdLevelEnum](ThresholdLevelEnum.md)
 * [threshold_high](threshold_high.md)  <sub>0..1</sub>
     * Description: The maximum level that must be exceeded for a certain reaction to occur or be manifested.
     * Range: [Decimal](types/Decimal.md)
 * [thredhold_low](thredhold_low.md)  <sub>0..1</sub>
     * Description: The minimum level that must be attained for a certain reaction to occur or be manifested.
     * Range: [Decimal](types/Decimal.md)
 * [seq_method](seq_method.md)  <sub>0..1</sub>
     * Description: Quantitative Sequencing Method
     * Range: [SeqMethodEnum](SeqMethodEnum.md)
 * [threshold_low](threshold_low.md)  <sub>0..1</sub>
     * Description: The minimum level that must be attained for a certain reaction to occur or be manifested.
     * Range: [Decimal](types/Decimal.md)
 * [pmid_ref](pmid_ref.md)  <sub>0..1</sub>
     * Description: A globally unique identifier for a biomedical article, as assigned by PubMed.
     * Range: [Decimal](types/Decimal.md)
 * [malignant_cells](malignant_cells.md)  <sub>0..1</sub>
     * Description: A term used to describe cancer. Malignant cells grow in an uncontrolled way and can invade nearby tissues and spread to other parts of the body through the blood and lymph system (Source: NCI Dictionary of Cancer Terms)
     * Range: [AbsentNotreportedPresentUnknownEnum](AbsentNotreportedPresentUnknownEnum.md)
 * [course_timepoint](course_timepoint.md)  <sub>0..1</sub>
     * Description: This variable gives more precise granularity to when an observation occured during the period of the indicated "Course" TIME_PERIOD
     * Range: [CourseTimepointEnum](CourseTimepointEnum.md)
 * [test_other](test_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" LAB_TEST
     * Range: [String](types/String.md)
 * [subjects](subjects.md)  <sub>1..1</sub>
     * Range: [Subject](Subject.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
