
# Class: Off Protocol Therapy Or Study




URI: [https://w3id.org/pcdc/model/OffProtocolTherapyOrStudy](https://w3id.org/pcdc/model/OffProtocolTherapyOrStudy)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..*-++[OffProtocolTherapyOrStudy&#124;age_off:integer%20%3F;off_type:OffTypeEnum%20%3F;reason_off:ReasonOffEnum%20%3F;reason_off_other:string%20%3F;another_study:NoNotreportedUnknownYesEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[OffProtocolTherapyOrStudy],[Thing]^-[OffProtocolTherapyOrStudy])](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..*-++[OffProtocolTherapyOrStudy&#124;age_off:integer%20%3F;off_type:OffTypeEnum%20%3F;reason_off:ReasonOffEnum%20%3F;reason_off_other:string%20%3F;another_study:NoNotreportedUnknownYesEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[OffProtocolTherapyOrStudy],[Thing]^-[OffProtocolTherapyOrStudy])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_off](age_off.md)  <sub>0..1</sub>
     * Description: The age (in days) when the subject went off of the protocol therapy or study.
     * Range: [Integer](types/Integer.md)
 * [time_periods](time_periods.md)  <sub>0..1</sub>
     * Range: [TimePeriod](TimePeriod.md)
 * [off_type](off_type.md)  <sub>0..1</sub>
     * Description: The code used to designate that the subject went off therapy or off the study.
     * Range: [OffTypeEnum](OffTypeEnum.md)
 * [reason_off](reason_off.md)  <sub>0..1</sub>
     * Description: The reason a subject went off the therapy or study.
     * Range: [ReasonOffEnum](ReasonOffEnum.md)
 * [reason_off_other](reason_off_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" REASON_OFF
     * Range: [String](types/String.md)
 * [another_study](another_study.md)  <sub>0..1</sub>
     * Description: Did the subject enroll in another study after they went off of the study indicated by OFF_TYPE?
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
