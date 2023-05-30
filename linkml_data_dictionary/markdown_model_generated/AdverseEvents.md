
# Class: Adverse Events




URI: [https://w3id.org/pcdc/model/AdverseEvents](https://w3id.org/pcdc/model/AdverseEvents)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..1-++[AdverseEvents&#124;age_at_ae:integer%20%3F;ae_code:string%20%3F;ae_code_system:AeCodeSystemEnum%20%3F;ae_code_system_version:string%20%3F;grade:GradeEnum%20%3F;grade_system:GradeSystemEnum%20%3F;grade_system_version:string%20%3F;attribution:AttributionEnum%20%3F;avn_joint:AvnJointEnum%20%3F;avn_joint_other:string%20%3F;avn_joint_laterality:BilateralLeftMidlineNotreportedRightUnknownEnum%20%3F;avn_method:AvnMethodEnum%20%3F;orthopedic_procedure:OrthopedicProcedureEnum%20%3F;orthopedic_procedure_other:string%20%3F;ae_pathogen:AePathogenEnum%20%3F;ae_pathogen_other:string%20%3F;infection_classification:InfectionClassificationEnum%20%3F;age_at_ae_resolved:integer%20%3F;adverse_event:AdverseEventEnum%20%3F;adverse_event_other:string%20%3F;icu:NoNotreportedUnknownYesEnum%20%3F;supportive_medication:NoNotreportedUnknownYesEnum%20%3F;intervention_status:NoNotreportedUnknownYesEnum%20%3F;intervention:InterventionEnum%20%3F;intervention_other:string%20%3F;ae_pathogen_confirmation:ConfirmedNotreportedSuspectedUnknownEnum%20%3F;gvhd_acuity:GvhdAcuityEnum%20%3F;gvhd_organ:GvhdOrganEnum%20%3F;gvhd_organ_other:string%20%3F;ae_outcome:AeOutcomeEnum%20%3F;modification_required:NoNotreportedUnknownYesEnum%20%3F;tox_delay:NoNotreportedUnknownYesEnum%20%3F;tox_high_grade_events:integer%20%3F;tox_dose_reductions:integer%20%3F;ae_immune:NoNotreportedUnknownYesEnum%20%3F;ae_infusion:NoNotreportedUnknownYesEnum%20%3F;reported:NoNotreportedUnknownYesEnum%20%3F;as_expected:NoNotreportedUnknownYesEnum%20%3F;hospitalization:NoNotreportedUnknownYesEnum%20%3F;ae_pathogen_status:ConfirmedNotreportedSuspectedUnknownEnum%20%3F;tumor_site:TumorSiteEnum%20%3F;ae_hospitalization_reason_other:string%20%3F;ae_hospitalization:NoNotreportedUnknownYesEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[AdverseEvents],[Thing]^-[AdverseEvents])](https://yuml.me/diagram/nofunky;dir:TB/class/[TimePeriod],[Thing],[Subject],[Subject]<subjects%201..1-++[AdverseEvents&#124;age_at_ae:integer%20%3F;ae_code:string%20%3F;ae_code_system:AeCodeSystemEnum%20%3F;ae_code_system_version:string%20%3F;grade:GradeEnum%20%3F;grade_system:GradeSystemEnum%20%3F;grade_system_version:string%20%3F;attribution:AttributionEnum%20%3F;avn_joint:AvnJointEnum%20%3F;avn_joint_other:string%20%3F;avn_joint_laterality:BilateralLeftMidlineNotreportedRightUnknownEnum%20%3F;avn_method:AvnMethodEnum%20%3F;orthopedic_procedure:OrthopedicProcedureEnum%20%3F;orthopedic_procedure_other:string%20%3F;ae_pathogen:AePathogenEnum%20%3F;ae_pathogen_other:string%20%3F;infection_classification:InfectionClassificationEnum%20%3F;age_at_ae_resolved:integer%20%3F;adverse_event:AdverseEventEnum%20%3F;adverse_event_other:string%20%3F;icu:NoNotreportedUnknownYesEnum%20%3F;supportive_medication:NoNotreportedUnknownYesEnum%20%3F;intervention_status:NoNotreportedUnknownYesEnum%20%3F;intervention:InterventionEnum%20%3F;intervention_other:string%20%3F;ae_pathogen_confirmation:ConfirmedNotreportedSuspectedUnknownEnum%20%3F;gvhd_acuity:GvhdAcuityEnum%20%3F;gvhd_organ:GvhdOrganEnum%20%3F;gvhd_organ_other:string%20%3F;ae_outcome:AeOutcomeEnum%20%3F;modification_required:NoNotreportedUnknownYesEnum%20%3F;tox_delay:NoNotreportedUnknownYesEnum%20%3F;tox_high_grade_events:integer%20%3F;tox_dose_reductions:integer%20%3F;ae_immune:NoNotreportedUnknownYesEnum%20%3F;ae_infusion:NoNotreportedUnknownYesEnum%20%3F;reported:NoNotreportedUnknownYesEnum%20%3F;as_expected:NoNotreportedUnknownYesEnum%20%3F;hospitalization:NoNotreportedUnknownYesEnum%20%3F;ae_pathogen_status:ConfirmedNotreportedSuspectedUnknownEnum%20%3F;tumor_site:TumorSiteEnum%20%3F;ae_hospitalization_reason_other:string%20%3F;ae_hospitalization:NoNotreportedUnknownYesEnum%20%3F;submitter_id(i):string;type(i):string],[TimePeriod]<time_periods%200..1-++[AdverseEvents],[Thing]^-[AdverseEvents])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_ae](age_at_ae.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject at the onset of this adverse event
     * Range: [Integer](types/Integer.md)
 * [ae_code](ae_code.md)  <sub>0..1</sub>
     * Description: The code of the adverse event.
     * Range: [String](types/String.md)
 * [ae_code_system](ae_code_system.md)  <sub>0..1</sub>
     * Description: The coding system used for the AE_CODE
     * Range: [AeCodeSystemEnum](AeCodeSystemEnum.md)
 * [ae_code_system_version](ae_code_system_version.md)  <sub>0..1</sub>
     * Description: The version of the adverse event grading system.
     * Range: [String](types/String.md)
 * [grade](grade.md)  <sub>0..1</sub>
     * Description: A numeric value corresponding to the degree of severity of an adverse event.
     * Range: [GradeEnum](GradeEnum.md)
 * [grade_system](grade_system.md)  <sub>0..1</sub>
     * Description: The grading system used to refer to the severity of the adverse event.
     * Range: [GradeSystemEnum](GradeSystemEnum.md)
 * [grade_system_version](grade_system_version.md)  <sub>0..1</sub>
     * Description: The version of the adverse event grading system.
     * Range: [String](types/String.md)
 * [attribution](attribution.md)  <sub>0..1</sub>
     * Description: A specific identifiable level (defined qualitatively or quantitatively) of probability of adverse event being caused or associated with the product or procedure administration to a patient.
     * Range: [AttributionEnum](AttributionEnum.md)
 * [avn_joint](avn_joint.md)  <sub>0..1</sub>
     * Description: Death of bone tissue in a joint due to temporary or permanent interruption of blood flow.
     * Range: [AvnJointEnum](AvnJointEnum.md)
 * [avn_joint_other](avn_joint_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" AVN_JOINT
     * Range: [String](types/String.md)
 * [avn_joint_laterality](avn_joint_laterality.md)  <sub>0..1</sub>
     * Description: A finding descriptive of the laterality of the avascular necrosis in the joints.
     * Range: [BilateralLeftMidlineNotreportedRightUnknownEnum](BilateralLeftMidlineNotreportedRightUnknownEnum.md)
 * [avn_method](avn_method.md)  <sub>0..1</sub>
     * Description: The method used to determine the diagnosis of the avascular necrosis.
     * Range: [AvnMethodEnum](AvnMethodEnum.md)
 * [orthopedic_procedure](orthopedic_procedure.md)  <sub>0..1</sub>
     * Description: Orthopedic procedures to repair avascular necrosis.
     * Range: [OrthopedicProcedureEnum](OrthopedicProcedureEnum.md)
 * [orthopedic_procedure_other](orthopedic_procedure_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" ORTHOPEDIC_PROCEDURE
     * Range: [String](types/String.md)
 * [ae_pathogen](ae_pathogen.md)  <sub>0..1</sub>
     * Description: The pathogen identified as the agent causing the adverse event.
     * Range: [AePathogenEnum](AePathogenEnum.md)
 * [ae_pathogen_other](ae_pathogen_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" AE_PATHOGEN
     * Range: [String](types/String.md)
 * [infection_classification](infection_classification.md)  <sub>0..1</sub>
     * Description: The type of evidence regarding the infection type.
     * Range: [InfectionClassificationEnum](InfectionClassificationEnum.md)
 * [age_at_ae_resolved](age_at_ae_resolved.md)  <sub>0..1</sub>
     * Description: The age (in days) of the subject when this adverse event was resolved
     * Range: [Integer](types/Integer.md)
 * [time_periods](time_periods.md)  <sub>0..1</sub>
     * Range: [TimePeriod](TimePeriod.md)
 * [adverse_event](adverse_event.md)  <sub>0..1</sub>
     * Description: An unexpected medical problem that happens during treatment with a drug or other therapy. Adverse events may be mild, moderate, or severe, and may be caused by something other than the drug or therapy being given. Also called adverse effect. (Source: NCI Dictionary of Cancer Terms)
     * Range: [AdverseEventEnum](AdverseEventEnum.md)
 * [adverse_event_other](adverse_event_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" ADVERSE_EVENT
     * Range: [String](types/String.md)
 * [icu](icu.md)  <sub>0..1</sub>
     * Description: Admitted to ICU
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [supportive_medication](supportive_medication.md)  <sub>0..1</sub>
     * Description: Adverse Event Supportive Care Medication
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [intervention_status](intervention_status.md)  <sub>0..1</sub>
     * Description: Adverse Event Intervention
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [intervention](intervention.md)  <sub>0..1</sub>
     * Description: Intervention or Medication Detail
     * Range: [InterventionEnum](InterventionEnum.md)
 * [intervention_other](intervention_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" INTERVENTION_DETAIL
     * Range: [String](types/String.md)
 * [ae_pathogen_confirmation](ae_pathogen_confirmation.md)  <sub>0..1</sub>
     * Description: Pathogen Confirmation Indicator
     * Range: [ConfirmedNotreportedSuspectedUnknownEnum](ConfirmedNotreportedSuspectedUnknownEnum.md)
 * [gvhd_acuity](gvhd_acuity.md)  <sub>0..1</sub>
     * Description: Graft Versus Host Disease Acuity
     * Range: [GvhdAcuityEnum](GvhdAcuityEnum.md)
 * [gvhd_organ](gvhd_organ.md)  <sub>0..1</sub>
     * Description: Graft Versus Host Disease Organ
     * Range: [GvhdOrganEnum](GvhdOrganEnum.md)
 * [gvhd_organ_other](gvhd_organ_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" GVHD_ORGAN
     * Range: [String](types/String.md)
 * [ae_outcome](ae_outcome.md)  <sub>0..1</sub>
     * Description: A condition or event that is attributed to the adverse event and is the result or conclusion of the adverse event.
     * Range: [AeOutcomeEnum](AeOutcomeEnum.md)
 * [modification_required](modification_required.md)  <sub>0..1</sub>
     * Description: An indication that a change in treatment or a change to a device will be required following an adverse event.
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [tox_delay](tox_delay.md)  <sub>0..1</sub>
     * Description: Were there treatment delays due to toxicity?
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [tox_high_grade_events](tox_high_grade_events.md)  <sub>0..1</sub>
     * Description: The number of grade III-IV (CTCAE) toxicity events
     * Range: [Integer](types/Integer.md)
 * [tox_dose_reductions](tox_dose_reductions.md)  <sub>0..1</sub>
     * Description: The number of chemotherapy dose reductions due to toxicity
     * Range: [Integer](types/Integer.md)
 * [ae_immune](ae_immune.md)  <sub>0..1</sub>
     * Description: An adverse event affecting the immune system.
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [ae_infusion](ae_infusion.md)  <sub>0..1</sub>
     * Description: An adverse event that can be related to an infusion.
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [reported](reported.md)  <sub>0..1</sub>
     * Description: SAE Reported to Sponsor
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [as_expected](as_expected.md)  <sub>0..1</sub>
     * Description: Specifies whether the nature, frequency, or severity of an adverse event is consistent with the applicable study documentation (e.g., investigator's brochure, protocol document, or consent document) or product labeling (package insert).
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [hospitalization](hospitalization.md)  <sub>0..1</sub>
     * Description: An indication or description that an adverse event is associated with or prolongs hospitalization.
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [ae_pathogen_status](ae_pathogen_status.md)  <sub>0..1</sub>
     * Description: An indication that the reported pathogen was confirmed or suspected as the cause of an infection.
     * Range: [ConfirmedNotreportedSuspectedUnknownEnum](ConfirmedNotreportedSuspectedUnknownEnum.md)
 * [tumor_site](tumor_site.md)  <sub>0..1</sub>
     * Range: [TumorSiteEnum](TumorSiteEnum.md)
 * [ae_hospitalization_reason_other](ae_hospitalization_reason_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" AE_HOSPITALIZATION_REASON
     * Range: [String](types/String.md)
 * [ae_hospitalization](ae_hospitalization.md)  <sub>0..1</sub>
     * Description: An indication or description that an adverse event is associated with or prolongs hospitalization.
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [subjects](subjects.md)  <sub>1..1</sub>
     * Range: [Subject](Subject.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
