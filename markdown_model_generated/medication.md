
# Class: Medication




URI: [https://w3id.org/pcdc/model/Medication](https://w3id.org/pcdc/model/Medication)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[Medication&#124;age_at_medication_start:integer%20%3F;age_at_medication_end:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;administration_status:AdministrationStatusEnum%20%3F;medication:MedicationEnum%20%3F;protocol_medication:NoNotreportedUnknownYesEnum%20%3F;non_protocol_timing:NonProtocolTimingEnum%20%3F;non_protocol_reason:NonProtocolReasonEnum%20%3F;cycle_number:integer%20%3F;route:RouteEnum%20%3F;route_detail:RouteDetailEnum%20%3F;normalization_basis:NormalizationBasisEnum%20%3F;number_doses:integer%20%3F;total_dose_administered:integer%20%3F;total_dose_intended:integer%20%3F;total_dose_units:TotalDoseUnitsEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[Medication])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[Medication&#124;age_at_medication_start:integer%20%3F;age_at_medication_end:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;administration_status:AdministrationStatusEnum%20%3F;medication:MedicationEnum%20%3F;protocol_medication:NoNotreportedUnknownYesEnum%20%3F;non_protocol_timing:NonProtocolTimingEnum%20%3F;non_protocol_reason:NonProtocolReasonEnum%20%3F;cycle_number:integer%20%3F;route:RouteEnum%20%3F;route_detail:RouteDetailEnum%20%3F;normalization_basis:NormalizationBasisEnum%20%3F;number_doses:integer%20%3F;total_dose_administered:integer%20%3F;total_dose_intended:integer%20%3F;total_dose_units:TotalDoseUnitsEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[Medication])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_medication_start](age_at_medication_start.md)  <sub>0..1</sub>
     * Description: Age in Days at Start of Total Dose Calculation
     * Range: [Integer](types/Integer.md)
 * [age_at_medication_end](age_at_medication_end.md)  <sub>0..1</sub>
     * Description: Age in Days at End of Total Dose Calculation
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
 * [administration_status](administration_status.md)  <sub>0..1</sub>
     * Description: Medication Administration Status
     * Range: [AdministrationStatusEnum](AdministrationStatusEnum.md)
 * [medication](medication.md)  <sub>0..1</sub>
     * Description: A dosage form that contains one or more active and/or inactive ingredients. Medications come in many dosage forms, including tablets, capsules, liquids, creams, and patches. They can also be given in different ways, such as by mouth, by infusion into a vein, or by drops that are put into the ear or eye. The form with the active ingredient is used to prevent, diagnose, treat, or relieve symptoms of a disease or abnormal condition. A medication that does not contain an active ingredient and is used in research studies is called a placebo. Also called drug product. (Source: NCI Dictionary of Cancer Terms)
     * Range: [MedicationEnum](MedicationEnum.md)
 * [protocol_medication](protocol_medication.md)  <sub>0..1</sub>
     * Description: Was this medication part of the treatment protocol?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [non_protocol_timing](non_protocol_timing.md)  <sub>0..1</sub>
     * Description: If a non-protocol medication, when was this medication administered?
     * Range: [NonProtocolTimingEnum](NonProtocolTimingEnum.md)
 * [non_protocol_reason](non_protocol_reason.md)  <sub>0..1</sub>
     * Description: If a non-protocol medication, why was this medication administered?
     * Range: [NonProtocolReasonEnum](NonProtocolReasonEnum.md)
 * [cycle_number](cycle_number.md)  <sub>0..1</sub>
     * Description: This variable indicates the ordinal numbering of cycles of treatment therapy administered to the subject.
     * Range: [Integer](types/Integer.md)
 * [route](route.md)  <sub>0..1</sub>
     * Description: Route of Administration
     * Range: [RouteEnum](RouteEnum.md)
 * [route_detail](route_detail.md)  <sub>0..1</sub>
     * Description: Route of Administration Detail
     * Range: [RouteDetailEnum](RouteDetailEnum.md)
 * [normalization_basis](normalization_basis.md)  <sub>0..1</sub>
     * Description: Normalization Basis
     * Range: [NormalizationBasisEnum](NormalizationBasisEnum.md)
 * [number_doses](number_doses.md)  <sub>0..1</sub>
     * Description: Number of times a dose of the medication was administered between the AGE_AT_MEDICATION_START and AGE_AT_MEDICATION_END values.
     * Range: [Integer](types/Integer.md)
 * [total_dose_administered](total_dose_administered.md)  <sub>0..1</sub>
     * Description: Total amount of medication administered between the AGE_AT_MEDICATION_START and AGE_AT_MEDICATION values. Assuming all doses administered are the same amount of medication, this value should be equal to the amount of medication given at each dose multiplied by the number of doses.
     * Range: [Integer](types/Integer.md)
 * [total_dose_intended](total_dose_intended.md)  <sub>0..1</sub>
     * Description: This is the total amount of medication that was intended to be administered either by trial protocol, by prescription, or other indicator at the time point of AGE_AT_MEDICATION_START. Often, this will be equal to TOTAL_DOSE_ADMINISTERED. If TOTAL_DOSE_ADMINISTERED and TOTAL_DOSE_INTENDED are different, this indicates a deviation from the protocol or plan and may be due to a variety of factors including patient intolerance, patient non-adherence, etc.
     * Range: [Integer](types/Integer.md)
 * [total_dose_units](total_dose_units.md)  <sub>0..1</sub>
     * Description: Total Dose Units
     * Range: [TotalDoseUnitsEnum](TotalDoseUnitsEnum.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
