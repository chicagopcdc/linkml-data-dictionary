
# Class: Staging




URI: [https://w3id.org/pcdc/model/Staging](https://w3id.org/pcdc/model/Staging)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..1-++[Staging&#124;age_at_staging:integer%20%3F;stage_system:StageSystemEnum%20%3F;stage:StageEnum%20%3F;stage_other:string%20%3F;ann_arbor_mod_ab:AnnArborModAbEnum%20%3F;ann_arbor_mod_e:NoNotreportedUnknownYesEnum%20%3F;ann_arbor_mod_s:NoNotreportedUnknownYesEnum%20%3F;course_timepoint:CourseTimepointEnum%20%3F;site:SiteEnum%20%3F;stage_system_category:StageSystemCategoryEnum%20%3F;stage_type:StageTypeEnum%20%3F;h_stage:HStageEnum%20%3F;group_system:GroupSystemEnum%20%3F;group:GroupEnum%20%3F;tnm_finding:TnmFindingEnum%20%3F;irs_group:IrsGroupEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[Staging],[Thing]^-[Staging])](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..1-++[Staging&#124;age_at_staging:integer%20%3F;stage_system:StageSystemEnum%20%3F;stage:StageEnum%20%3F;stage_other:string%20%3F;ann_arbor_mod_ab:AnnArborModAbEnum%20%3F;ann_arbor_mod_e:NoNotreportedUnknownYesEnum%20%3F;ann_arbor_mod_s:NoNotreportedUnknownYesEnum%20%3F;course_timepoint:CourseTimepointEnum%20%3F;site:SiteEnum%20%3F;stage_system_category:StageSystemCategoryEnum%20%3F;stage_type:StageTypeEnum%20%3F;h_stage:HStageEnum%20%3F;group_system:GroupSystemEnum%20%3F;group:GroupEnum%20%3F;tnm_finding:TnmFindingEnum%20%3F;irs_group:IrsGroupEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[Staging],[Thing]^-[Staging])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_staging](age_at_staging.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the time of this staging assessment.
     * Range: [Integer](types/Integer.md)
 * [time_periods](time_periods.md)  <sub>0..1</sub>
     * Range: [TimePeriod](TimePeriod.md)
 * [stage_system](stage_system.md)  <sub>0..1</sub>
     * Description: A systematic method for clinicopathologic evaluation of tumors.
     * Range: [StageSystemEnum](StageSystemEnum.md)
 * [stage](stage.md)  <sub>0..1</sub>
     * Description: The extent of a cancer in the body. Staging is usually based on the size of the tumor, whether lymph nodes contain cancer, and whether the cancer has spread from the original site to other parts of the body (Source: NCI Dictionary of Cancer Terms)
     * Range: [StageEnum](StageEnum.md)
 * [stage_other](stage_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" STAGE
     * Range: [String](types/String.md)
 * [ann_arbor_mod_ab](ann_arbor_mod_ab.md)  <sub>0..1</sub>
     * Description: HL Ann Arbor A vs B Staging Designation
     * Range: [AnnArborModAbEnum](AnnArborModAbEnum.md)
 * [ann_arbor_mod_e](ann_arbor_mod_e.md)  <sub>0..1</sub>
     * Description: HL Ann Arbor E Staging Designation
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [ann_arbor_mod_s](ann_arbor_mod_s.md)  <sub>0..1</sub>
     * Description: HL Ann Arbor S Staging Designation
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [course_timepoint](course_timepoint.md)  <sub>0..1</sub>
     * Description: This variable gives more precise granularity to when an observation occured during the period of the indicated "Course" TIME_PERIOD
     * Range: [CourseTimepointEnum](CourseTimepointEnum.md)
 * [site](site.md)  <sub>0..1</sub>
     * Description: Specifies the anatomic site of a localized pathological or traumatic structural change, damage, deformity, or discontinuity of tissue, organ, or body part.
     * Range: [SiteEnum](SiteEnum.md)
 * [stage_system_category](stage_system_category.md)  <sub>0..1</sub>
     * Range: [StageSystemCategoryEnum](StageSystemCategoryEnum.md)
 * [stage_type](stage_type.md)  <sub>0..1</sub>
     * Range: [StageTypeEnum](StageTypeEnum.md)
 * [h_stage](h_stage.md)  <sub>0..1</sub>
     * Range: [HStageEnum](HStageEnum.md)
 * [group_system](group_system.md)  <sub>0..1</sub>
     * Range: [GroupSystemEnum](GroupSystemEnum.md)
 * [group](group.md)  <sub>0..1</sub>
     * Range: [GroupEnum](GroupEnum.md)
 * [tnm_finding](tnm_finding.md)  <sub>0..1</sub>
     * Range: [TnmFindingEnum](TnmFindingEnum.md)
 * [irs_group](irs_group.md)  <sub>0..1</sub>
     * Description: IRS Surgical-Pathologic Grouping System
     * Range: [IrsGroupEnum](IrsGroupEnum.md)
 * [subjects](subjects.md)  <sub>1..1</sub>
     * Range: [Subject](Subject.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
