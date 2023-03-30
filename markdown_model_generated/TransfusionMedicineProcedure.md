
# Class: TransfusionMedicineProcedure




URI: [https://w3id.org/pcdc/model/TransfusionMedicineProcedure](https://w3id.org/pcdc/model/TransfusionMedicineProcedure)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing]<timings%200..1-++[TransfusionMedicineProcedure&#124;age_at_tmp_start:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;protocol_transfusion:NoNotreportedUnknownYesEnum%20%3F;non_protocol_timing:NonProtocolTimingEnum%20%3F;tmp_type:TmpTypeEnum%20%3F;tmp_product:TmpProductEnum%20%3F;tmp_product_type:TmpProductTypeEnum%20%3F;tmp_number_units:integer%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[TransfusionMedicineProcedure],[Timing],[Thing])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing]<timings%200..1-++[TransfusionMedicineProcedure&#124;age_at_tmp_start:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;protocol_transfusion:NoNotreportedUnknownYesEnum%20%3F;non_protocol_timing:NonProtocolTimingEnum%20%3F;tmp_type:TmpTypeEnum%20%3F;tmp_product:TmpProductEnum%20%3F;tmp_product_type:TmpProductTypeEnum%20%3F;tmp_number_units:integer%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[TransfusionMedicineProcedure],[Timing],[Thing])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_tmp_start](age_at_tmp_start.md)  <sub>0..1</sub>
     * Description: Age in Days at Start of Transfusion Medicine Procedure
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
 * [protocol_transfusion](protocol_transfusion.md)  <sub>0..1</sub>
     * Description: Was this transfusion part of the treatment protocol?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [non_protocol_timing](non_protocol_timing.md)  <sub>0..1</sub>
     * Description: If a non-protocol medication, when was this medication administered?
     * Range: [NonProtocolTimingEnum](NonProtocolTimingEnum.md)
 * [tmp_type](tmp_type.md)  <sub>0..1</sub>
     * Description: Transfusion Medicine Procedure Type
     * Range: [TmpTypeEnum](TmpTypeEnum.md)
 * [tmp_product](tmp_product.md)  <sub>0..1</sub>
     * Description: Transfusion Medicine Procedure Product
     * Range: [TmpProductEnum](TmpProductEnum.md)
 * [tmp_product_type](tmp_product_type.md)  <sub>0..1</sub>
     * Description: Transfusion Medicine Procedure Product Type
     * Range: [TmpProductTypeEnum](TmpProductTypeEnum.md)
 * [tmp_number_units](tmp_number_units.md)  <sub>0..1</sub>
     * Description: Number of Units of Product Transfused
     * Range: [Integer](types/Integer.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
