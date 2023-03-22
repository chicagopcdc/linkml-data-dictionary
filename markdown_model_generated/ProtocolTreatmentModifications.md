
# Class: ProtocolTreatmentModifications




URI: [https://w3id.org/pcdc/model/ProtocolTreatmentModifications](https://w3id.org/pcdc/model/ProtocolTreatmentModifications)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[ProtocolTreatmentModifications&#124;age_at_mod:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;mod_type:ModTypeEnum%20%3F;mod_rationale:ModRationaleEnum%20%3F;mod_reason:ModReasonEnum%20%3F;toxicity_detail:ToxicityDetailEnum%20%3F;toxicity_immune:NoNotreportedUnknownYesEnum%20%3F;toxicity_infusion:NoNotreportedUnknownYesEnum%20%3F;original_agent:BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum%20%3F;sub_agent:BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[ProtocolTreatmentModifications])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[ProtocolTreatmentModifications&#124;age_at_mod:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;mod_type:ModTypeEnum%20%3F;mod_rationale:ModRationaleEnum%20%3F;mod_reason:ModReasonEnum%20%3F;toxicity_detail:ToxicityDetailEnum%20%3F;toxicity_immune:NoNotreportedUnknownYesEnum%20%3F;toxicity_infusion:NoNotreportedUnknownYesEnum%20%3F;original_agent:BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum%20%3F;sub_agent:BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[ProtocolTreatmentModifications])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_mod](age_at_mod.md)  <sub>0..1</sub>
     * Description: Age in Days of Protocol Treatment Modification
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
 * [mod_type](mod_type.md)  <sub>0..1</sub>
     * Description: Modification Type
     * Range: [ModTypeEnum](ModTypeEnum.md)
 * [mod_rationale](mod_rationale.md)  <sub>0..1</sub>
     * Description: Treatment Modification Rationale
     * Range: [ModRationaleEnum](ModRationaleEnum.md)
 * [mod_reason](mod_reason.md)  <sub>0..1</sub>
     * Description: Treatment Modification Reason
     * Range: [ModReasonEnum](ModReasonEnum.md)
 * [toxicity_detail](toxicity_detail.md)  <sub>0..1</sub>
     * Description: Toxicity Detail
     * Range: [ToxicityDetailEnum](ToxicityDetailEnum.md)
 * [toxicity_immune](toxicity_immune.md)  <sub>0..1</sub>
     * Description: Immune Related Toxicity
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [toxicity_infusion](toxicity_infusion.md)  <sub>0..1</sub>
     * Description: Infusion Related Toxicity
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [original_agent](original_agent.md)  <sub>0..1</sub>
     * Description: Original Agent
     * Range: [BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum](BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum.md)
 * [sub_agent](sub_agent.md)  <sub>0..1</sub>
     * Description: Substitution Agent
     * Range: [BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum](BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
