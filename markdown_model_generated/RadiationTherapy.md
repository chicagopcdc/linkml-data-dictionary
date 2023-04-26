
# Class: Radiation Therapy




URI: [https://w3id.org/pcdc/model/RadiationTherapy](https://w3id.org/pcdc/model/RadiationTherapy)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..*-++[RadiationTherapy&#124;age_at_rt_start:integer%20%3F;age_at_rt_end:integer%20%3F;protocol_radiation_therapy:NoNotreportedUnknownYesEnum%20%3F;non_protocol_timing:NonProtocolTimingEnum%20%3F;site:SiteEnum%20%3F;site_other:string%20%3F;total_dose:decimal%20%3F;total_dose_unit:TotalDoseUnitEnum%20%3F;technique:TechniqueEnum%20%3F;energy_type:EnergyTypeEnum%20%3F;margin:MarginEnum%20%3F;rt_data_source:RtDataSourceEnum%20%3F;fraction_dose:decimal%20%3F;fraction_dose_unit:CgeNotreportedUnknownCgyEnum%20%3F;num_fraction:decimal%20%3F;target_volume:TargetVolumeEnum%20%3F;boost:NoNotreportedUnknownYesEnum%20%3F;boost_dose:decimal%20%3F;boost_unit:CgeNotreportedUnknownCgyEnum%20%3F;boost_target_volume:BoostTargetVolumeEnum%20%3F;classification:ClassificationEnum%20%3F;tissue_type:TissueTypeEnum%20%3F;laterality:BilateralLeftMidlineNotreportedRightUnknownEnum%20%3F;technique_other:string%20%3F;transposition_organ:TranspositionOrganEnum%20%3F;boost_dose_unit:BoostDoseUnitEnum%20%3F;energy_type_other:string%20%3F;indication:IndicationEnum%20%3F;indication_other:string%20%3F;proton_delivery_mode:ProtonDeliveryModeEnum%20%3F;plaque_size:PlaqueSizeEnum%20%3F;apex_dose:decimal%20%3F;rt_completed:NoNotreportedUnknownYesEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[RadiationTherapy],[Thing]^-[RadiationTherapy])](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..*-++[RadiationTherapy&#124;age_at_rt_start:integer%20%3F;age_at_rt_end:integer%20%3F;protocol_radiation_therapy:NoNotreportedUnknownYesEnum%20%3F;non_protocol_timing:NonProtocolTimingEnum%20%3F;site:SiteEnum%20%3F;site_other:string%20%3F;total_dose:decimal%20%3F;total_dose_unit:TotalDoseUnitEnum%20%3F;technique:TechniqueEnum%20%3F;energy_type:EnergyTypeEnum%20%3F;margin:MarginEnum%20%3F;rt_data_source:RtDataSourceEnum%20%3F;fraction_dose:decimal%20%3F;fraction_dose_unit:CgeNotreportedUnknownCgyEnum%20%3F;num_fraction:decimal%20%3F;target_volume:TargetVolumeEnum%20%3F;boost:NoNotreportedUnknownYesEnum%20%3F;boost_dose:decimal%20%3F;boost_unit:CgeNotreportedUnknownCgyEnum%20%3F;boost_target_volume:BoostTargetVolumeEnum%20%3F;classification:ClassificationEnum%20%3F;tissue_type:TissueTypeEnum%20%3F;laterality:BilateralLeftMidlineNotreportedRightUnknownEnum%20%3F;technique_other:string%20%3F;transposition_organ:TranspositionOrganEnum%20%3F;boost_dose_unit:BoostDoseUnitEnum%20%3F;energy_type_other:string%20%3F;indication:IndicationEnum%20%3F;indication_other:string%20%3F;proton_delivery_mode:ProtonDeliveryModeEnum%20%3F;plaque_size:PlaqueSizeEnum%20%3F;apex_dose:decimal%20%3F;rt_completed:NoNotreportedUnknownYesEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[RadiationTherapy],[Thing]^-[RadiationTherapy])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_rt_start](age_at_rt_start.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the start of this radiation treatment.
     * Range: [Integer](types/Integer.md)
 * [age_at_rt_end](age_at_rt_end.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the end of this radiation treatment.
     * Range: [Integer](types/Integer.md)
 * [protocol_radiation_therapy](protocol_radiation_therapy.md)  <sub>0..1</sub>
     * Description: Was this radiation therapy administration part of the treatment protocol?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [non_protocol_timing](non_protocol_timing.md)  <sub>0..1</sub>
     * Description: If a non-protocol radiation therapy, when was this radiation therapy administered?
     * Range: [NonProtocolTimingEnum](NonProtocolTimingEnum.md)
 * [site](site.md)  <sub>0..1</sub>
     * Description: Specifies the anatomic site of a localized pathological or traumatic structural change, damage, deformity, or discontinuity of tissue, organ, or body part.
     * Range: [SiteEnum](SiteEnum.md)
 * [time_periods](time_periods.md)  <sub>0..1</sub>
     * Range: [TimePeriod](TimePeriod.md)
 * [site_other](site_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" TUMOR_SITE
     * Range: [String](types/String.md)
 * [total_dose](total_dose.md)  <sub>0..1</sub>
     * Description: The total radiation dose administered.
     * Range: [Decimal](types/Decimal.md)
 * [total_dose_unit](total_dose_unit.md)  <sub>0..1</sub>
     * Description: A unit of measurement of the dose of radiation received or absorbed.
     * Range: [TotalDoseUnitEnum](TotalDoseUnitEnum.md)
 * [technique](technique.md)  <sub>0..1</sub>
     * Description: Treatment of a disease by means of exposure of the target or the whole body to radiation. Radiation therapy is often used as part of curative therapy and occasionally as a component of palliative treatment for cancer. Other uses include total body irradiation prior to transplantation.
     * Range: [TechniqueEnum](TechniqueEnum.md)
 * [energy_type](energy_type.md)  <sub>0..1</sub>
     * Description: Treatment of a disease by means of exposure of the target or the whole body to radiation. Radiation therapy is often used as part of curative therapy and occasionally as a component of palliative treatment for cancer. Other uses include total body irradiation prior to transplantation.
     * Range: [EnergyTypeEnum](EnergyTypeEnum.md)
 * [margin](margin.md)  <sub>0..1</sub>
     * Range: [MarginEnum](MarginEnum.md)
 * [rt_data_source](rt_data_source.md)  <sub>0..1</sub>
     * Description: Whether radiation data was obtained from a protocol-defined dose, or 
     * Range: [RtDataSourceEnum](RtDataSourceEnum.md)
 * [fraction_dose](fraction_dose.md)  <sub>0..1</sub>
     * Range: [Decimal](types/Decimal.md)
 * [fraction_dose_unit](fraction_dose_unit.md)  <sub>0..1</sub>
     * Description: A unit of measurement of the dose of radiation received or absorbed.
     * Range: [CgeNotreportedUnknownCgyEnum](CgeNotreportedUnknownCgyEnum.md)
 * [num_fraction](num_fraction.md)  <sub>0..1</sub>
     * Description: The number of divided radiation doses received per day.
     * Range: [Decimal](types/Decimal.md)
 * [target_volume](target_volume.md)  <sub>0..1</sub>
     * Description: The intended target volume for this radiation therapy.
     * Range: [TargetVolumeEnum](TargetVolumeEnum.md)
 * [boost](boost.md)  <sub>0..1</sub>
     * Description: One or more extra radiation treatments targeted at the tumor bed, given after the regular sessions of radiation are complete.
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [boost_dose](boost_dose.md)  <sub>0..1</sub>
     * Description: The dose amount of the radiation boost.
     * Range: [Decimal](types/Decimal.md)
 * [boost_unit](boost_unit.md)  <sub>0..1</sub>
     * Range: [CgeNotreportedUnknownCgyEnum](CgeNotreportedUnknownCgyEnum.md)
 * [boost_target_volume](boost_target_volume.md)  <sub>0..1</sub>
     * Range: [BoostTargetVolumeEnum](BoostTargetVolumeEnum.md)
 * [classification](classification.md)  <sub>0..1</sub>
     * Description: The classification of a tumor based primarily on histopathological characteristics.
     * Range: [ClassificationEnum](ClassificationEnum.md)
 * [tissue_type](tissue_type.md)  <sub>0..1</sub>
     * Description: A piece of tissue removed from an organism for examination, analysis, or propagation.
     * Range: [TissueTypeEnum](TissueTypeEnum.md)
 * [laterality](laterality.md)  <sub>0..1</sub>
     * Description: A qualifier for the side of the body the tumor findings assessment is performed.
     * Range: [BilateralLeftMidlineNotreportedRightUnknownEnum](BilateralLeftMidlineNotreportedRightUnknownEnum.md)
 * [technique_other](technique_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" TECHNIQUE
     * Range: [String](types/String.md)
 * [transposition_organ](transposition_organ.md)  <sub>0..1</sub>
     * Description: A procedure to move organs out of the range of the damaging effects of radiation.
     * Range: [TranspositionOrganEnum](TranspositionOrganEnum.md)
 * [boost_dose_unit](boost_dose_unit.md)  <sub>0..1</sub>
     * Description: A unit of measurement of the dose of radiation received or absorbed.
     * Range: [BoostDoseUnitEnum](BoostDoseUnitEnum.md)
 * [energy_type_other](energy_type_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" ENERGY_TYPE
     * Range: [String](types/String.md)
 * [indication](indication.md)  <sub>0..1</sub>
     * Range: [IndicationEnum](IndicationEnum.md)
 * [indication_other](indication_other.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [proton_delivery_mode](proton_delivery_mode.md)  <sub>0..1</sub>
     * Range: [ProtonDeliveryModeEnum](ProtonDeliveryModeEnum.md)
 * [plaque_size](plaque_size.md)  <sub>0..1</sub>
     * Description: Size of the plaque holding the radiation source
     * Range: [PlaqueSizeEnum](PlaqueSizeEnum.md)
 * [apex_dose](apex_dose.md)  <sub>0..1</sub>
     * Range: [Decimal](types/Decimal.md)
 * [rt_completed](rt_completed.md)  <sub>0..1</sub>
     * Description: Radiation Therapy Completed as Planned
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [subjects](subjects.md)  <sub>1..\*</sub>
     * Range: [Subject](Subject.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
