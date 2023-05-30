
# Class: Patient Reported Outcomes Metadata




URI: [https://w3id.org/pcdc/model/PatientReportedOutcomesMetadata](https://w3id.org/pcdc/model/PatientReportedOutcomesMetadata)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Subject],[Subject]<subjects%201..1-++[PatientReportedOutcomesMetadata&#124;study_id:StudyIdEnum%20%3F;pro_measures:ProMeasuresEnum%20%3F;pro_measures_other:string%20%3F;pro_measurement_type:ProMeasurementTypeEnum%20%3F;pro_measurement_type_other:string%20%3F;raters:RatersEnum%20%3F;raters_other:string%20%3F;eligible_age_lower:integer%20%3F;eligible_age_upper:integer%20%3F;time_point:TimePointEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[PatientReportedOutcomesMetadata])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Subject],[Subject]<subjects%201..1-++[PatientReportedOutcomesMetadata&#124;study_id:StudyIdEnum%20%3F;pro_measures:ProMeasuresEnum%20%3F;pro_measures_other:string%20%3F;pro_measurement_type:ProMeasurementTypeEnum%20%3F;pro_measurement_type_other:string%20%3F;raters:RatersEnum%20%3F;raters_other:string%20%3F;eligible_age_lower:integer%20%3F;eligible_age_upper:integer%20%3F;time_point:TimePointEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[PatientReportedOutcomesMetadata])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [study_id](study_id.md)  <sub>0..1</sub>
     * Description: A sequence of characters used to identify, name, or characterize the study.
     * Range: [StudyIdEnum](StudyIdEnum.md)
 * [pro_measures](pro_measures.md)  <sub>0..1</sub>
     * Description: Survey measures that are completed by the patient which help assess patient status with regards to pain, mobility, quality of life, ability to perform daily tasks or notable events in a clinical study.
     * Range: [ProMeasuresEnum](ProMeasuresEnum.md)
 * [pro_measures_other](pro_measures_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other"
     * Range: [String](types/String.md)
 * [pro_measurement_type](pro_measurement_type.md)  <sub>0..1</sub>
     * Description: The type of patient reported outcome measurement.
     * Range: [ProMeasurementTypeEnum](ProMeasurementTypeEnum.md)
 * [pro_measurement_type_other](pro_measurement_type_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" PRO_MEASUREMENT_TYPE
     * Range: [String](types/String.md)
 * [raters](raters.md)  <sub>0..1</sub>
     * Description: Raters are allowed to report the patient reported outcomes.
     * Range: [RatersEnum](RatersEnum.md)
 * [raters_other](raters_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" RATERS
     * Range: [String](types/String.md)
 * [eligible_age_lower](eligible_age_lower.md)  <sub>0..1</sub>
     * Description: The low age range of the child for an evaluation tool.
     * Range: [Integer](types/Integer.md)
 * [eligible_age_upper](eligible_age_upper.md)  <sub>0..1</sub>
     * Description: The upper age range of the child for an evaluation tool.
     * Range: [Integer](types/Integer.md)
 * [time_point](time_point.md)  <sub>0..1</sub>
     * Description: The point in time that acts as a fixed reference point to an event.
     * Range: [TimePointEnum](TimePointEnum.md)
 * [subjects](subjects.md)  <sub>1..1</sub>
     * Range: [Subject](Subject.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
