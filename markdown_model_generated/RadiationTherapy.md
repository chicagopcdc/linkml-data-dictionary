
# Class: RadiationTherapy




URI: [https://w3id.org/pcdc/model/RadiationTherapy](https://w3id.org/pcdc/model/RadiationTherapy)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[RadiationTherapy&#124;age_at_rt_start:integer%20%3F;age_at_rt_end:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;protocol_radiation_therapy:NoNotreportedUnknownYesEnum%20%3F;non_protocol_timing:NonProtocolTimingEnum%20%3F;tumor_classification:TumorClassificationEnum%20%3F;tumor_tissue_type:BoneNotreportedSofttissueUnknownEnum%20%3F;rt_site:RtSiteEnum%20%3F;laterality:LateralityEnum%20%3F;energy_type:EnergyTypeEnum%20%3F;rt_dose:integer%20%3F;rt_unit:RtUnitEnum%20%3F;boost:NoNotreportedUnknownYesEnum%20%3F;boost_dose:integer%20%3F;num_fraction:integer%20%3F;transposition_organ:TranspositionOrganEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[RadiationTherapy])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[RadiationTherapy&#124;age_at_rt_start:integer%20%3F;age_at_rt_end:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;protocol_radiation_therapy:NoNotreportedUnknownYesEnum%20%3F;non_protocol_timing:NonProtocolTimingEnum%20%3F;tumor_classification:TumorClassificationEnum%20%3F;tumor_tissue_type:BoneNotreportedSofttissueUnknownEnum%20%3F;rt_site:RtSiteEnum%20%3F;laterality:LateralityEnum%20%3F;energy_type:EnergyTypeEnum%20%3F;rt_dose:integer%20%3F;rt_unit:RtUnitEnum%20%3F;boost:NoNotreportedUnknownYesEnum%20%3F;boost_dose:integer%20%3F;num_fraction:integer%20%3F;transposition_organ:TranspositionOrganEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[RadiationTherapy])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_rt_start](age_at_rt_start.md)  <sub>0..1</sub>
     * Description: Age in Days at Start of Radiation Therapy
     * Range: [Integer](types/Integer.md)
 * [age_at_rt_end](age_at_rt_end.md)  <sub>0..1</sub>
     * Description: Age in Days at End of Radiation Therapy
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
 * [protocol_radiation_therapy](protocol_radiation_therapy.md)  <sub>0..1</sub>
     * Description: Was this radiation therapy administration part of the treatment protocol?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [non_protocol_timing](non_protocol_timing.md)  <sub>0..1</sub>
     * Description: If a non-protocol medication, when was this medication administered?
     * Range: [NonProtocolTimingEnum](NonProtocolTimingEnum.md)
 * [tumor_classification](tumor_classification.md)  <sub>0..1</sub>
     * Description: Tumor Classification
     * Range: [TumorClassificationEnum](TumorClassificationEnum.md)
 * [tumor_tissue_type](tumor_tissue_type.md)  <sub>0..1</sub>
     * Description: Radiation Therapy Tissue Type
     * Range: [BoneNotreportedSofttissueUnknownEnum](BoneNotreportedSofttissueUnknownEnum.md)
 * [rt_site](rt_site.md)  <sub>0..1</sub>
     * Description: Radiation Therapy Site
     * Range: [RtSiteEnum](RtSiteEnum.md)
 * [laterality](laterality.md)  <sub>0..1</sub>
     * Range: [LateralityEnum](LateralityEnum.md)
 * [energy_type](energy_type.md)  <sub>0..1</sub>
     * Description: Energy Type
     * Range: [EnergyTypeEnum](EnergyTypeEnum.md)
 * [rt_dose](rt_dose.md)  <sub>0..1</sub>
     * Description: Total Radiation Dose
     * Range: [Integer](types/Integer.md)
 * [rt_unit](rt_unit.md)  <sub>0..1</sub>
     * Description: Radiation Dose Unit
     * Range: [RtUnitEnum](RtUnitEnum.md)
 * [boost](boost.md)  <sub>0..1</sub>
     * Description: Boost Given
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [boost_dose](boost_dose.md)  <sub>0..1</sub>
     * Description: Boost Dose
     * Range: [Integer](types/Integer.md)
 * [num_fraction](num_fraction.md)  <sub>0..1</sub>
     * Description: Number of Fractions
     * Range: [Integer](types/Integer.md)
 * [transposition_organ](transposition_organ.md)  <sub>0..1</sub>
     * Description: Surgical Transposition of Organs
     * Range: [TranspositionOrganEnum](TranspositionOrganEnum.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
