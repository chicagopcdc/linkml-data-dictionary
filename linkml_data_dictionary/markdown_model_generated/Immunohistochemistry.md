
# Class: Immunohistochemistry




URI: [https://w3id.org/pcdc/model/Immunohistochemistry](https://w3id.org/pcdc/model/Immunohistochemistry)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..*-++[Immunohistochemistry&#124;age_at_ihc:integer%20%3F;review_source:ReviewSourceEnum%20%3F;test:TestEnum%20%3F;result:NegativeNotreportedPositiveUnknownEnum%20%3F;result_text:string%20%3F;result_numeric:decimal%20%3F;specimen:SpecimenEnum%20%3F;result_unit:ResultUnitEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[Immunohistochemistry],[Thing]^-[Immunohistochemistry])](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..*-++[Immunohistochemistry&#124;age_at_ihc:integer%20%3F;review_source:ReviewSourceEnum%20%3F;test:TestEnum%20%3F;result:NegativeNotreportedPositiveUnknownEnum%20%3F;result_text:string%20%3F;result_numeric:decimal%20%3F;specimen:SpecimenEnum%20%3F;result_unit:ResultUnitEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[Immunohistochemistry],[Thing]^-[Immunohistochemistry])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_ihc](age_at_ihc.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the immunohistochemical test.
     * Range: [Integer](types/Integer.md)
 * [time_periods](time_periods.md)  <sub>0..1</sub>
     * Range: [TimePeriod](TimePeriod.md)
 * [review_source](review_source.md)  <sub>0..1</sub>
     * Description: The type of assessment that was used to review.
     * Range: [ReviewSourceEnum](ReviewSourceEnum.md)
 * [test](test.md)  <sub>0..1</sub>
     * Description: A medical procedure that involves testing a sample of blood, urine, or other substance from the body. Laboratory tests can help determine a diagnosis, plan treatment, check to see if treatment is working, or monitor the disease over time Source: NCI Dictionary of Cancer Terms)
     * Range: [TestEnum](TestEnum.md)
 * [result](result.md)  <sub>0..1</sub>
     * Description: The text result of the laboratory test.
     * Range: [NegativeNotreportedPositiveUnknownEnum](NegativeNotreportedPositiveUnknownEnum.md)
 * [result_text](result_text.md)  <sub>0..1</sub>
     * Description: The string/text result of the laboratory test.
     * Range: [String](types/String.md)
 * [result_numeric](result_numeric.md)  <sub>0..1</sub>
     * Description: The numeric result of the laboratory test.
     * Range: [Decimal](types/Decimal.md)
 * [specimen](specimen.md)  <sub>0..1</sub>
     * Description: The type of specimen analyzed.
     * Range: [SpecimenEnum](SpecimenEnum.md)
 * [result_unit](result_unit.md)  <sub>0..1</sub>
     * Description: The units used for the numeric result of the laboratory test.
     * Range: [ResultUnitEnum](ResultUnitEnum.md)
 * [subjects](subjects.md)  <sub>1..\*</sub>
     * Range: [Subject](Subject.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
