
# Class: Protocol Treatment Modifications




URI: [https://w3id.org/pcdc/model/ProtocolTreatmentModifications](https://w3id.org/pcdc/model/ProtocolTreatmentModifications)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..*-++[ProtocolTreatmentModifications&#124;age_at_modification:integer%20%3F;modification:ModificationEnum%20%3F;modification_other:string%20%3F;modification_basis:ModificationBasisEnum%20%3F;reason:ReasonEnum%20%3F;reason_other:string%20%3F;toxicity_detail:ToxicityDetailEnum%20%3F;toxicity_detail_other:string%20%3F;toxicity_immune:NoNotreportedUnknownYesEnum%20%3F;toxicity_infusion:NoNotreportedUnknownYesEnum%20%3F;original_agent:BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum%20%3F;original_agent_other:string%20%3F;sub_agent:BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum%20%3F;sub_agent_other:string%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[ProtocolTreatmentModifications],[Thing]^-[ProtocolTreatmentModifications])](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..*-++[ProtocolTreatmentModifications&#124;age_at_modification:integer%20%3F;modification:ModificationEnum%20%3F;modification_other:string%20%3F;modification_basis:ModificationBasisEnum%20%3F;reason:ReasonEnum%20%3F;reason_other:string%20%3F;toxicity_detail:ToxicityDetailEnum%20%3F;toxicity_detail_other:string%20%3F;toxicity_immune:NoNotreportedUnknownYesEnum%20%3F;toxicity_infusion:NoNotreportedUnknownYesEnum%20%3F;original_agent:BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum%20%3F;original_agent_other:string%20%3F;sub_agent:BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum%20%3F;sub_agent_other:string%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[ProtocolTreatmentModifications],[Thing]^-[ProtocolTreatmentModifications])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_modification](age_at_modification.md)  <sub>0..1</sub>
     * Description: The age (in days) of subject since the protocol treatment modification.
     * Range: [Integer](types/Integer.md)
 * [time_periods](time_periods.md)  <sub>0..1</sub>
     * Range: [TimePeriod](TimePeriod.md)
 * [modification](modification.md)  <sub>0..1</sub>
     * Description: The type of modification used.
     * Range: [ModificationEnum](ModificationEnum.md)
 * [modification_other](modification_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" MODIFICATION
     * Range: [String](types/String.md)
 * [modification_basis](modification_basis.md)  <sub>0..1</sub>
     * Description: The rationale for why an entity or event is changed.	
     * Range: [ModificationBasisEnum](ModificationBasisEnum.md)
 * [reason](reason.md)  <sub>0..1</sub>
     * Description: The reasoning behind a treatment modification.	
     * Range: [ReasonEnum](ReasonEnum.md)
 * [reason_other](reason_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" REASON
     * Range: [String](types/String.md)
 * [toxicity_detail](toxicity_detail.md)  <sub>0..1</sub>
     * Description: Information about the conditions surrounding the toxicity.	
     * Range: [ToxicityDetailEnum](ToxicityDetailEnum.md)
 * [toxicity_detail_other](toxicity_detail_other.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [toxicity_immune](toxicity_immune.md)  <sub>0..1</sub>
     * Description: Toxicity that impairs or damages the immune system.	
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [toxicity_infusion](toxicity_infusion.md)  <sub>0..1</sub>
     * Description: Toxicity related to an infusion.	
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [original_agent](original_agent.md)  <sub>0..1</sub>
     * Description: The first agent planned for a therapy.	
     * Range: [BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum](BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum.md)
 * [original_agent_other](original_agent_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" ORIGINAL_AGENT
     * Range: [String](types/String.md)
 * [sub_agent](sub_agent.md)  <sub>0..1</sub>
     * Description: A medication was substituted with another.	
     * Range: [BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum](BendamustineBleomycinBrentuximabvedotinBusulfanCarboplatinCarmustineCisplatinCyclophosphamideCytarabEnum.md)
 * [sub_agent_other](sub_agent_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" SUB_AGENT
     * Range: [String](types/String.md)
 * [subjects](subjects.md)  <sub>1..\*</sub>
     * Range: [Subject](Subject.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
