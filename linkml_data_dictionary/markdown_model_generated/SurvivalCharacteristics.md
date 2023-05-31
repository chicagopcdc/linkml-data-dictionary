
# Class: Survival Characteristics




URI: [https://w3id.org/pcdc/model/SurvivalCharacteristics](https://w3id.org/pcdc/model/SurvivalCharacteristics)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject]<subjects%201..1-++[SurvivalCharacteristics&#124;age_at_lkss:integer%20%3F;lkss:AliveDeadNotreportedUnknownEnum%20%3F;lkss_with_disease:NoNotreportedUnknownYesEnum%20%3F;age_lost_to_follow_up:integer%20%3F;cause_of_death:CauseOfDeathEnum%20%3F;cause_of_death_other:string%20%3F;trm_type:TrmTypeEnum%20%3F;trm_type_other:string%20%3F;cause_of_death_detail:CauseOfDeathDetailEnum%20%3F;cause_of_death_detail_other:string%20%3F;cause_of_death_ranking:CauseOfDeathRankingEnum%20%3F;course_timepoint:CourseTimepointEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[SurvivalCharacteristics],[Thing]^-[SurvivalCharacteristics],[Subject])](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject]<subjects%201..1-++[SurvivalCharacteristics&#124;age_at_lkss:integer%20%3F;lkss:AliveDeadNotreportedUnknownEnum%20%3F;lkss_with_disease:NoNotreportedUnknownYesEnum%20%3F;age_lost_to_follow_up:integer%20%3F;cause_of_death:CauseOfDeathEnum%20%3F;cause_of_death_other:string%20%3F;trm_type:TrmTypeEnum%20%3F;trm_type_other:string%20%3F;cause_of_death_detail:CauseOfDeathDetailEnum%20%3F;cause_of_death_detail_other:string%20%3F;cause_of_death_ranking:CauseOfDeathRankingEnum%20%3F;course_timepoint:CourseTimepointEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[SurvivalCharacteristics],[Thing]^-[SurvivalCharacteristics],[Subject])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_lkss](age_at_lkss.md)  <sub>0..1</sub>
     * Description: The age (in days) when the last known survival status of the subject was captured.
     * Range: [Integer](types/Integer.md)
 * [time_periods](time_periods.md)  <sub>0..1</sub>
     * Range: [TimePeriod](TimePeriod.md)
 * [lkss](lkss.md)  <sub>0..1</sub>
     * Description: The last known survival status of the subject.
     * Range: [AliveDeadNotreportedUnknownEnum](AliveDeadNotreportedUnknownEnum.md)
 * [lkss_with_disease](lkss_with_disease.md)  <sub>0..1</sub>
     * Description: Did the subject still have measurable/evaluable disease at the LKSS?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [age_lost_to_follow_up](age_lost_to_follow_up.md)  <sub>0..1</sub>
     * Description: The age (in days) when the subject was lost to follow-up.
     * Range: [Integer](types/Integer.md)
 * [cause_of_death](cause_of_death.md)  <sub>0..1</sub>
     * Description: The circumstance or condition that results in the death of a living being.
     * Range: [CauseOfDeathEnum](CauseOfDeathEnum.md)
 * [cause_of_death_other](cause_of_death_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" CAUSE_OF_DEATH
     * Range: [String](types/String.md)
 * [trm_type](trm_type.md)  <sub>0..1</sub>
     * Description: If the mortality is treatment related, what type of treatment was involved?
     * Range: [TrmTypeEnum](TrmTypeEnum.md)
 * [trm_type_other](trm_type_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" TRM_TYPE
     * Range: [String](types/String.md)
 * [cause_of_death_detail](cause_of_death_detail.md)  <sub>0..1</sub>
     * Description: The more granular reason for the CAUSE_OF_DEATH of the subject.
     * Range: [CauseOfDeathDetailEnum](CauseOfDeathDetailEnum.md)
 * [cause_of_death_detail_other](cause_of_death_detail_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" CAUSE_OF_DEATH_DETAIL
     * Range: [String](types/String.md)
 * [cause_of_death_ranking](cause_of_death_ranking.md)  <sub>0..1</sub>
     * Description: Assigning a weighted relevance to the cause of death.
     * Range: [CauseOfDeathRankingEnum](CauseOfDeathRankingEnum.md)
 * [course_timepoint](course_timepoint.md)  <sub>0..1</sub>
     * Description: This variable gives more precise granularity to when an observation occured during the period of the indicated "Course" TIME_PERIOD
     * Range: [CourseTimepointEnum](CourseTimepointEnum.md)
 * [subjects](subjects.md)  <sub>1..1</sub>
     * Range: [Subject](Subject.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
