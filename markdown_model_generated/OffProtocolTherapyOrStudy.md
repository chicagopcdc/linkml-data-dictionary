
# Class: OffProtocolTherapyOrStudy




URI: [https://w3id.org/pcdc/model/OffProtocolTherapyOrStudy](https://w3id.org/pcdc/model/OffProtocolTherapyOrStudy)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[OffProtocolTherapyOrStudy&#124;age_off:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;off_type:OffTypeEnum%20%3F;reason_off:ReasonOffEnum%20%3F;reason_off_other:string%20%3F;another_study:NoNotreportedUnknownYesEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[OffProtocolTherapyOrStudy])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[OffProtocolTherapyOrStudy&#124;age_off:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;off_type:OffTypeEnum%20%3F;reason_off:ReasonOffEnum%20%3F;reason_off_other:string%20%3F;another_study:NoNotreportedUnknownYesEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[OffProtocolTherapyOrStudy])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_off](age_off.md)  <sub>0..1</sub>
     * Description: The age (in days) when the subject went off of the protocol therapy or study.
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
 * [off_type](off_type.md)  <sub>0..1</sub>
     * Description: Did the subject go off of a study or off of a certain protocol therapy?
     * Range: [OffTypeEnum](OffTypeEnum.md)
 * [reason_off](reason_off.md)  <sub>0..1</sub>
     * Description: What was the reason that the subject went off of a study or off of a certain protocol therapy?
     * Range: [ReasonOffEnum](ReasonOffEnum.md)
 * [reason_off_other](reason_off_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" REASON_OFF
     * Range: [String](types/String.md)
 * [another_study](another_study.md)  <sub>0..1</sub>
     * Description: Did the subject enroll in another study after they went off of the study indicated by OFF_TYPE?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
