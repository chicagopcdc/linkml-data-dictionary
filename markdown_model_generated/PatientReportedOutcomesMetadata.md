
# Class: PatientReportedOutcomesMetadata




URI: [https://w3id.org/pcdc/model/PatientReportedOutcomesMetadata](https://w3id.org/pcdc/model/PatientReportedOutcomesMetadata)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[PatientReportedOutcomesMetadata&#124;study_id:StudyIdEnum%20%3F;pro_measures:ProMeasuresEnum%20%3F;pro_measurement_type:ProMeasurementTypeEnum%20%3F;raters:RatersEnum%20%3F;eligible_age_lower:integer%20%3F;eligible_age_upper:integer%20%3F;time_point:TimePointEnum%20%3F;submitter_id(i):string;type(i):string])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[PatientReportedOutcomesMetadata&#124;study_id:StudyIdEnum%20%3F;pro_measures:ProMeasuresEnum%20%3F;pro_measurement_type:ProMeasurementTypeEnum%20%3F;raters:RatersEnum%20%3F;eligible_age_lower:integer%20%3F;eligible_age_upper:integer%20%3F;time_point:TimePointEnum%20%3F;submitter_id(i):string;type(i):string])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [study_id](study_id.md)  <sub>0..1</sub>
     * Description: A sequence of characters used to identify, name, or characterize the study.
     * Range: [StudyIdEnum](StudyIdEnum.md)
 * [pro_measures](pro_measures.md)  <sub>0..1</sub>
     * Description: PRO Measures
     * Range: [ProMeasuresEnum](ProMeasuresEnum.md)
 * [pro_measurement_type](pro_measurement_type.md)  <sub>0..1</sub>
     * Description: PRO Measurement Type
     * Range: [ProMeasurementTypeEnum](ProMeasurementTypeEnum.md)
 * [raters](raters.md)  <sub>0..1</sub>
     * Description: Raters Allowed to Report
     * Range: [RatersEnum](RatersEnum.md)
 * [eligible_age_lower](eligible_age_lower.md)  <sub>0..1</sub>
     * Description: Lower Age Range of Child Rater
     * Range: [Integer](types/Integer.md)
 * [eligible_age_upper](eligible_age_upper.md)  <sub>0..1</sub>
     * Description: Upper Age Range of Child Rater
     * Range: [Integer](types/Integer.md)
 * [time_point](time_point.md)  <sub>0..1</sub>
     * Description: PRO Measures Assessment Time Point
     * Range: [TimePointEnum](TimePointEnum.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
