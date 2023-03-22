
# Class: Staging




URI: [https://w3id.org/pcdc/model/Staging](https://w3id.org/pcdc/model/Staging)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[Staging&#124;age_at_staging:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;stage_system:StageSystemEnum%20%3F;stage:StageEnum%20%3F;ann_arbor_mod_ab:AnnArborModAbEnum%20%3F;ann_arbor_mod_e:NoNotreportedUnknownYesEnum%20%3F;ann_arbor_mod_s:NoNotreportedUnknownYesEnum%20%3F;tnm_finding:TnmFindingEnum%20%3F;irs_group:IrsGroupEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[Staging])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[Staging&#124;age_at_staging:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;stage_system:StageSystemEnum%20%3F;stage:StageEnum%20%3F;ann_arbor_mod_ab:AnnArborModAbEnum%20%3F;ann_arbor_mod_e:NoNotreportedUnknownYesEnum%20%3F;ann_arbor_mod_s:NoNotreportedUnknownYesEnum%20%3F;tnm_finding:TnmFindingEnum%20%3F;irs_group:IrsGroupEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[Staging])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_staging](age_at_staging.md)  <sub>0..1</sub>
     * Description: Age in Days of Staging Assessment
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
 * [stage_system](stage_system.md)  <sub>0..1</sub>
     * Description: A systematic method for clinicopathologic evaluation of tumors.
     * Range: [StageSystemEnum](StageSystemEnum.md)
 * [stage](stage.md)  <sub>0..1</sub>
     * Description: The extent of a cancer in the body. Staging is usually based on the size of the tumor, whether lymph nodes contain cancer, and whether the cancer has spread from the original site to other parts of the body (Source: NCI Dictionary of Cancer Terms)
     * Range: [StageEnum](StageEnum.md)
 * [ann_arbor_mod_ab](ann_arbor_mod_ab.md)  <sub>0..1</sub>
     * Description: HL Ann Arbor A vs B Staging Designation
     * Range: [AnnArborModAbEnum](AnnArborModAbEnum.md)
 * [ann_arbor_mod_e](ann_arbor_mod_e.md)  <sub>0..1</sub>
     * Description: HL Ann Arbor E Staging Designation
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [ann_arbor_mod_s](ann_arbor_mod_s.md)  <sub>0..1</sub>
     * Description: HL Ann Arbor S Staging Designation
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [tnm_finding](tnm_finding.md)  <sub>0..1</sub>
     * Range: [TnmFindingEnum](TnmFindingEnum.md)
 * [irs_group](irs_group.md)  <sub>0..1</sub>
     * Description: IRS Surgical-Pathologic Grouping System
     * Range: [IrsGroupEnum](IrsGroupEnum.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
