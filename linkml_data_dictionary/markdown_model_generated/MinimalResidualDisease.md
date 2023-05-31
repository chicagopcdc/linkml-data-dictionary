
# Class: Minimal Residual Disease




URI: [https://w3id.org/pcdc/model/MinimalResidualDisease](https://w3id.org/pcdc/model/MinimalResidualDisease)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..1-++[MinimalResidualDisease&#124;age_at_mrd_assessment:integer%20%3F;method:MethodEnum%20%3F;result_text:string%20%3F;result_numeric:decimal%20%3F;result_unit:ResultUnitEnum%20%3F;sensitivity:decimal%20%3F;sample_source:SampleSourceEnum%20%3F;method_other:string%20%3F;molecular_markers:MolecularMarkersEnum%20%3F;molecular_markers_other:string%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[MinimalResidualDisease],[Thing]^-[MinimalResidualDisease])](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..1-++[MinimalResidualDisease&#124;age_at_mrd_assessment:integer%20%3F;method:MethodEnum%20%3F;result_text:string%20%3F;result_numeric:decimal%20%3F;result_unit:ResultUnitEnum%20%3F;sensitivity:decimal%20%3F;sample_source:SampleSourceEnum%20%3F;method_other:string%20%3F;molecular_markers:MolecularMarkersEnum%20%3F;molecular_markers_other:string%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[MinimalResidualDisease],[Thing]^-[MinimalResidualDisease])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_mrd_assessment](age_at_mrd_assessment.md)  <sub>0..1</sub>
     * Description: Age in Days at Minimal Residual Disease Assessment
     * Range: [Integer](types/Integer.md)
 * [method](method.md)  <sub>0..1</sub>
     * Description: A systematic course of action that is performed in order to complete a laboratory test.
     * Range: [MethodEnum](MethodEnum.md)
 * [result_text](result_text.md)  <sub>0..1</sub>
     * Description: The string/text result of the laboratory test.
     * Range: [String](types/String.md)
 * [result_numeric](result_numeric.md)  <sub>0..1</sub>
     * Description: The numeric result of the laboratory test.
     * Range: [Decimal](types/Decimal.md)
 * [result_unit](result_unit.md)  <sub>0..1</sub>
     * Description: The units used for the numeric result of the laboratory test.
     * Range: [ResultUnitEnum](ResultUnitEnum.md)
 * [sensitivity](sensitivity.md)  <sub>0..1</sub>
     * Description: Sensitivity of modality used to determine minimal residual disease.
     * Range: [Decimal](types/Decimal.md)
 * [sample_source](sample_source.md)  <sub>0..1</sub>
     * Description: Minimal Residual Disease Sample Source
     * Range: [SampleSourceEnum](SampleSourceEnum.md)
 * [time_periods](time_periods.md)  <sub>0..1</sub>
     * Range: [TimePeriod](TimePeriod.md)
 * [method_other](method_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" LAB_METHOD
     * Range: [String](types/String.md)
 * [molecular_markers](molecular_markers.md)  <sub>0..1</sub>
     * Description: Minimal residual disease molecular markers
     * Range: [MolecularMarkersEnum](MolecularMarkersEnum.md)
 * [molecular_markers_other](molecular_markers_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" MRD_MOLECULAR_MARKERS
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
