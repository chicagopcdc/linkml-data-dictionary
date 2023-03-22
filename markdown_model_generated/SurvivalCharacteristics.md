
# Class: SurvivalCharacteristics




URI: [https://w3id.org/pcdc/model/SurvivalCharacteristics](https://w3id.org/pcdc/model/SurvivalCharacteristics)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[SurvivalCharacteristics&#124;age_at_lkss:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;lkss:LkssEnum%20%3F;lkss_with_disease:NoNotreportedUnknownYesEnum%20%3F;age_lost_to_follow_up:integer%20%3F;cause_of_death:CauseOfDeathEnum%20%3F;trm_type:TrmTypeEnum%20%3F;trm_type_other:string%20%3F;cause_of_death_detail:CauseOfDeathDetailEnum%20%3F;cause_of_death_detail_other:string%20%3F;cause_of_death_ranking:CauseOfDeathRankingEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[SurvivalCharacteristics])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[SurvivalCharacteristics&#124;age_at_lkss:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;lkss:LkssEnum%20%3F;lkss_with_disease:NoNotreportedUnknownYesEnum%20%3F;age_lost_to_follow_up:integer%20%3F;cause_of_death:CauseOfDeathEnum%20%3F;trm_type:TrmTypeEnum%20%3F;trm_type_other:string%20%3F;cause_of_death_detail:CauseOfDeathDetailEnum%20%3F;cause_of_death_detail_other:string%20%3F;cause_of_death_ranking:CauseOfDeathRankingEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[SurvivalCharacteristics])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_lkss](age_at_lkss.md)  <sub>0..1</sub>
     * Description: The age (in days) when the last known survival status of the subject was captured.
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
 * [lkss](lkss.md)  <sub>0..1</sub>
     * Description: The last known survival status of the subject.
     * Range: [LkssEnum](LkssEnum.md)
 * [lkss_with_disease](lkss_with_disease.md)  <sub>0..1</sub>
     * Description: Did the subject still have measurable/evaluable disease at the LKSS?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [age_lost_to_follow_up](age_lost_to_follow_up.md)  <sub>0..1</sub>
     * Description: The age (in days) when the subject was lost to follow-up
     * Range: [Integer](types/Integer.md)
 * [cause_of_death](cause_of_death.md)  <sub>0..1</sub>
     * Description: The circumstance or condition that results in the death of a living being.
     * Range: [CauseOfDeathEnum](CauseOfDeathEnum.md)
 * [trm_type](trm_type.md)  <sub>0..1</sub>
     * Description: If the mortality is treatment related, what type of treatment was involved?
     * Range: [TrmTypeEnum](TrmTypeEnum.md)
 * [trm_type_other](trm_type_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" TRM_TYPE
     * Range: [String](types/String.md)
 * [cause_of_death_detail](cause_of_death_detail.md)  <sub>0..1</sub>
     * Description: More granular causes for the death of the subject than what is permissible in CAUSE_OF_DEATH.
     * Range: [CauseOfDeathDetailEnum](CauseOfDeathDetailEnum.md)
 * [cause_of_death_detail_other](cause_of_death_detail_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" CAUSE_OF_DEATH_DETAIL
     * Range: [String](types/String.md)
 * [cause_of_death_ranking](cause_of_death_ranking.md)  <sub>0..1</sub>
     * Description: Assigning a weighted relevance to the cause of death.
     * Range: [CauseOfDeathRankingEnum](CauseOfDeathRankingEnum.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
