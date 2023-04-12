
# Class: Medication




URI: [https://w3id.org/pcdc/model/Medication](https://w3id.org/pcdc/model/Medication)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..*-++[Medication&#124;age_at_medication_start:integer%20%3F;age_at_medication_end:integer%20%3F;route:RouteEnum%20%3F;medication:MedicationEnum%20%3F;administration_status:AdministrationStatusEnum%20%3F;number_doses:decimal%20%3F;total_dose_administered:decimal%20%3F;total_dose_intended:decimal%20%3F;total_dose_unit:TotalDoseUnitEnum%20%3F;protocol_medication:NoNotreportedUnknownYesEnum%20%3F;non_protocol_timing:NonProtocolTimingEnum%20%3F;non_protocol_reason:NonProtocolReasonEnum%20%3F;medication_other:string%20%3F;category:CategoryEnum%20%3F;concomitant_reason:ConcomitantReasonEnum%20%3F;concomitant_reason_other:string%20%3F;route_detail:RouteDetailEnum%20%3F;normalization_basis:NormalizationBasisEnum%20%3F;cycle_number:integer%20%3F;cycles_planned:integer%20%3F;session_number:integer%20%3F;tumor_site:TumorSiteEnum%20%3F;administration_site:AdministrationSiteEnum%20%3F;total_dose_given:NoNotreportedUnknownYesEnum%20%3F;delivery_status:NoNotreportedUnknownYesEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[Medication],[Thing]^-[Medication])](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..*-++[Medication&#124;age_at_medication_start:integer%20%3F;age_at_medication_end:integer%20%3F;route:RouteEnum%20%3F;medication:MedicationEnum%20%3F;administration_status:AdministrationStatusEnum%20%3F;number_doses:decimal%20%3F;total_dose_administered:decimal%20%3F;total_dose_intended:decimal%20%3F;total_dose_unit:TotalDoseUnitEnum%20%3F;protocol_medication:NoNotreportedUnknownYesEnum%20%3F;non_protocol_timing:NonProtocolTimingEnum%20%3F;non_protocol_reason:NonProtocolReasonEnum%20%3F;medication_other:string%20%3F;category:CategoryEnum%20%3F;concomitant_reason:ConcomitantReasonEnum%20%3F;concomitant_reason_other:string%20%3F;route_detail:RouteDetailEnum%20%3F;normalization_basis:NormalizationBasisEnum%20%3F;cycle_number:integer%20%3F;cycles_planned:integer%20%3F;session_number:integer%20%3F;tumor_site:TumorSiteEnum%20%3F;administration_site:AdministrationSiteEnum%20%3F;total_dose_given:NoNotreportedUnknownYesEnum%20%3F;delivery_status:NoNotreportedUnknownYesEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[Medication],[Thing]^-[Medication])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_medication_start](age_at_medication_start.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the start of this medication treatment.
     * Range: [Integer](types/Integer.md)
 * [age_at_medication_end](age_at_medication_end.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the end of this medication treatment.
     * Range: [Integer](types/Integer.md)
 * [time_periods](time_periods.md)  <sub>0..1</sub>
     * Range: [TimePeriod](TimePeriod.md)
 * [route](route.md)  <sub>0..1</sub>
     * Description: Route of Administration
     * Range: [RouteEnum](RouteEnum.md)
 * [medication](medication.md)  <sub>0..1</sub>
     * Description: A dosage form that contains one or more active and/or inactive ingredients. Medications come in many dosage forms, including tablets, capsules, liquids, creams, and patches. They can also be given in different ways, such as by mouth, by infusion into a vein, or by drops that are put into the ear or eye. The form with the active ingredient is used to prevent, diagnose, treat, or relieve symptoms of a disease or abnormal condition. A medication that does not contain an active ingredient and is used in research studies is called a placebo. Also called drug product.
     * Range: [MedicationEnum](MedicationEnum.md)
 * [administration_status](administration_status.md)  <sub>0..1</sub>
     * Description: The status of the medication administration.
     * Range: [AdministrationStatusEnum](AdministrationStatusEnum.md)
 * [number_doses](number_doses.md)  <sub>0..1</sub>
     * Description: Number of times a dose of the medication was administered between the AGE_AT_MEDICATION_START and AGE_AT_MEDICATION_END values.
     * Range: [Decimal](types/Decimal.md)
 * [total_dose_administered](total_dose_administered.md)  <sub>0..1</sub>
     * Description: Total amount of medication administered between the AGE_AT_MEDICATION_START and AGE_AT_MEDICATION values. Assuming all doses administered are the same amount of medication, this value should be equal to the amount of medication given at each dose multiplied by the number of doses.
     * Range: [Decimal](types/Decimal.md)
 * [total_dose_intended](total_dose_intended.md)  <sub>0..1</sub>
     * Description: This is the total amount of medication that was intended to be administered either by trial protocol, by prescription, or other indicator at the time point of AGE_AT_MEDICATION_START. Often, this will be equal to TOTAL_DOSE_ADMINISTERED. If TOTAL_DOSE_ADMINISTERED and TOTAL_DOSE_INTENDED are different, this indicates a deviation from the protocol or plan and may be due to a variety of factors including patient intolerance, patient non-adherence, etc.
     * Range: [Decimal](types/Decimal.md)
 * [total_dose_unit](total_dose_unit.md)  <sub>0..1</sub>
     * Description: A unit of measurement of the dose of radiation received or absorbed.
     * Range: [TotalDoseUnitEnum](TotalDoseUnitEnum.md)
 * [protocol_medication](protocol_medication.md)  <sub>0..1</sub>
     * Description: Was this medication part of the treatment protocol?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [non_protocol_timing](non_protocol_timing.md)  <sub>0..1</sub>
     * Description: If a non-protocol radiation therapy, when was this radiation therapy administered?
     * Range: [NonProtocolTimingEnum](NonProtocolTimingEnum.md)
 * [non_protocol_reason](non_protocol_reason.md)  <sub>0..1</sub>
     * Description: If a non-protocol medication, why was this medication administered?
     * Range: [NonProtocolReasonEnum](NonProtocolReasonEnum.md)
 * [medication_other](medication_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" MEDICATION
     * Range: [String](types/String.md)
 * [category](category.md)  <sub>0..1</sub>
     * Description: The category of laboratory test performed on the subject.
     * Range: [CategoryEnum](CategoryEnum.md)
 * [concomitant_reason](concomitant_reason.md)  <sub>0..1</sub>
     * Description: If a non-protocol medication, why was this medication administered?
     * Range: [ConcomitantReasonEnum](ConcomitantReasonEnum.md)
 * [concomitant_reason_other](concomitant_reason_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" CONCOMITANT_REASON
     * Range: [String](types/String.md)
 * [route_detail](route_detail.md)  <sub>0..1</sub>
     * Description: Designation of the part of the body through which or into which, or the way in which, the medicinal product is intended to be introduced. In some cases a medicinal product can be intended for more than one route and/or method of administration.
     * Range: [RouteDetailEnum](RouteDetailEnum.md)
 * [normalization_basis](normalization_basis.md)  <sub>0..1</sub>
     * Description: An indication of what method was used to normalize the data.
     * Range: [NormalizationBasisEnum](NormalizationBasisEnum.md)
 * [cycle_number](cycle_number.md)  <sub>0..1</sub>
     * Description: The number of the individual chemotherapeutic cycle.
     * Range: [Integer](types/Integer.md)
 * [cycles_planned](cycles_planned.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
 * [session_number](session_number.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
 * [tumor_site](tumor_site.md)  <sub>0..1</sub>
     * Range: [TumorSiteEnum](TumorSiteEnum.md)
 * [administration_site](administration_site.md)  <sub>0..1</sub>
     * Range: [AdministrationSiteEnum](AdministrationSiteEnum.md)
 * [total_dose_given](total_dose_given.md)  <sub>0..1</sub>
     * Description: Was the full dose of this cycle or session administered?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [delivery_status](delivery_status.md)  <sub>0..1</sub>
     * Description: Was this cycle or session delivered successfully?
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
