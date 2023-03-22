
# Class: AdverseEvents




URI: [https://w3id.org/pcdc/model/AdverseEvents](https://w3id.org/pcdc/model/AdverseEvents)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[AdverseEvents&#124;age_at_ae:integer%20%3F;age_at_ae_resolved:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;adverse_event:AdverseEventEnum%20%3F;ae_immune:NoNotreportedUnknownYesEnum%20%3F;ae_infusion:NoNotreportedUnknownYesEnum%20%3F;ae_code:string%20%3F;ae_grade_system:AeGradeSystemEnum%20%3F;ae_system_version:string%20%3F;ae_grade:AeGradeEnum%20%3F;ae_reported:NoNotreportedUnknownYesEnum%20%3F;ae_attribution:AeAttributionEnum%20%3F;ae_outcome:AeOutcomeEnum%20%3F;avn_joint:AvnJointEnum%20%3F;avn_joint_laterality:AvnJointLateralityEnum%20%3F;avn_method:AvnMethodEnum%20%3F;orthopedic_procedure:OrthopedicProcedureEnum%20%3F;ae_expected:AeExpectedEnum%20%3F;ae_tx_mod:NoNotreportedUnknownYesEnum%20%3F;ae_hospitalization:NoNotreportedUnknownYesEnum%20%3F;ae_icu:NoNotreportedUnknownYesEnum%20%3F;ae_medication:NoNotreportedUnknownYesEnum%20%3F;ae_intervention:NoNotreportedUnknownYesEnum%20%3F;ae_intervention_detail:AeInterventionDetailEnum%20%3F;ae_pathogen:AePathogenEnum%20%3F;ae_pathogen_confirmation:AePathogenConfirmationEnum%20%3F;infection_classification:InfectionClassificationEnum%20%3F;gvhd_acuity:GvhdAcuityEnum%20%3F;gvhd_organ:GvhdOrganEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[AdverseEvents])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[AdverseEvents&#124;age_at_ae:integer%20%3F;age_at_ae_resolved:integer%20%3F;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;adverse_event:AdverseEventEnum%20%3F;ae_immune:NoNotreportedUnknownYesEnum%20%3F;ae_infusion:NoNotreportedUnknownYesEnum%20%3F;ae_code:string%20%3F;ae_grade_system:AeGradeSystemEnum%20%3F;ae_system_version:string%20%3F;ae_grade:AeGradeEnum%20%3F;ae_reported:NoNotreportedUnknownYesEnum%20%3F;ae_attribution:AeAttributionEnum%20%3F;ae_outcome:AeOutcomeEnum%20%3F;avn_joint:AvnJointEnum%20%3F;avn_joint_laterality:AvnJointLateralityEnum%20%3F;avn_method:AvnMethodEnum%20%3F;orthopedic_procedure:OrthopedicProcedureEnum%20%3F;ae_expected:AeExpectedEnum%20%3F;ae_tx_mod:NoNotreportedUnknownYesEnum%20%3F;ae_hospitalization:NoNotreportedUnknownYesEnum%20%3F;ae_icu:NoNotreportedUnknownYesEnum%20%3F;ae_medication:NoNotreportedUnknownYesEnum%20%3F;ae_intervention:NoNotreportedUnknownYesEnum%20%3F;ae_intervention_detail:AeInterventionDetailEnum%20%3F;ae_pathogen:AePathogenEnum%20%3F;ae_pathogen_confirmation:AePathogenConfirmationEnum%20%3F;infection_classification:InfectionClassificationEnum%20%3F;gvhd_acuity:GvhdAcuityEnum%20%3F;gvhd_organ:GvhdOrganEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[AdverseEvents])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

 * [age_at_ae](age_at_ae.md)  <sub>0..1</sub>
     * Description: Age in Days at Onset Adverse Event
     * Range: [Integer](types/Integer.md)
 * [age_at_ae_resolved](age_at_ae_resolved.md)  <sub>0..1</sub>
     * Description: Age in Days at Resolved Adverse Event
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
 * [adverse_event](adverse_event.md)  <sub>0..1</sub>
     * Description: An unexpected medical problem that happens during treatment with a drug or other therapy. Adverse events may be mild, moderate, or severe, and may be caused by something other than the drug or therapy being given. Also called adverse effect. (Source: NCI Dictionary of Cancer Terms)
     * Range: [AdverseEventEnum](AdverseEventEnum.md)
 * [ae_immune](ae_immune.md)  <sub>0..1</sub>
     * Description: Immune Related Adverse Event
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [ae_infusion](ae_infusion.md)  <sub>0..1</sub>
     * Description: Infusion Related Adverse Event
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [ae_code](ae_code.md)  <sub>0..1</sub>
     * Description: Adverse Event Coded
     * Range: [String](types/String.md)
 * [ae_grade_system](ae_grade_system.md)  <sub>0..1</sub>
     * Description: Adverse Event Grading System
     * Range: [AeGradeSystemEnum](AeGradeSystemEnum.md)
 * [ae_system_version](ae_system_version.md)  <sub>0..1</sub>
     * Description: Adverse Event Grading System Version
     * Range: [String](types/String.md)
 * [ae_grade](ae_grade.md)  <sub>0..1</sub>
     * Description: Adverse Event Severity Grade
     * Range: [AeGradeEnum](AeGradeEnum.md)
 * [ae_reported](ae_reported.md)  <sub>0..1</sub>
     * Description: SAE Reported to Sponsor
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [ae_attribution](ae_attribution.md)  <sub>0..1</sub>
     * Description: Adverse Event Attribution to Product or Procedure
     * Range: [AeAttributionEnum](AeAttributionEnum.md)
 * [ae_outcome](ae_outcome.md)  <sub>0..1</sub>
     * Description: Adverse Event Outcome
     * Range: [AeOutcomeEnum](AeOutcomeEnum.md)
 * [avn_joint](avn_joint.md)  <sub>0..1</sub>
     * Description: Avascular Necrosis Joint Involvement
     * Range: [AvnJointEnum](AvnJointEnum.md)
 * [avn_joint_laterality](avn_joint_laterality.md)  <sub>0..1</sub>
     * Description: Avascular Necrosis Joint Laterality
     * Range: [AvnJointLateralityEnum](AvnJointLateralityEnum.md)
 * [avn_method](avn_method.md)  <sub>0..1</sub>
     * Description: Avascular Necrosis Method of Evaluation
     * Range: [AvnMethodEnum](AvnMethodEnum.md)
 * [orthopedic_procedure](orthopedic_procedure.md)  <sub>0..1</sub>
     * Description: Avascular Necrosis Orthopedic Procedures
     * Range: [OrthopedicProcedureEnum](OrthopedicProcedureEnum.md)
 * [ae_expected](ae_expected.md)  <sub>0..1</sub>
     * Description: Adverse Event Expected
     * Range: [AeExpectedEnum](AeExpectedEnum.md)
 * [ae_tx_mod](ae_tx_mod.md)  <sub>0..1</sub>
     * Description: Protocol Treatment Modifications
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [ae_hospitalization](ae_hospitalization.md)  <sub>0..1</sub>
     * Description: Adverse Event Associated with Hospitalization
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [ae_icu](ae_icu.md)  <sub>0..1</sub>
     * Description: Admitted to ICU
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [ae_medication](ae_medication.md)  <sub>0..1</sub>
     * Description: Adverse Event Supportive Care Medication
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [ae_intervention](ae_intervention.md)  <sub>0..1</sub>
     * Description: Adverse Event Intervention
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [ae_intervention_detail](ae_intervention_detail.md)  <sub>0..1</sub>
     * Description: Intervention or Medication Detail
     * Range: [AeInterventionDetailEnum](AeInterventionDetailEnum.md)
 * [ae_pathogen](ae_pathogen.md)  <sub>0..1</sub>
     * Description: Pathogen Causing Infection
     * Range: [AePathogenEnum](AePathogenEnum.md)
 * [ae_pathogen_confirmation](ae_pathogen_confirmation.md)  <sub>0..1</sub>
     * Description: Pathogen Confirmation Indicator
     * Range: [AePathogenConfirmationEnum](AePathogenConfirmationEnum.md)
 * [infection_classification](infection_classification.md)  <sub>0..1</sub>
     * Description: Infection Site Classification
     * Range: [InfectionClassificationEnum](InfectionClassificationEnum.md)
 * [gvhd_acuity](gvhd_acuity.md)  <sub>0..1</sub>
     * Description: Graft Versus Host Disease Acuity
     * Range: [GvhdAcuityEnum](GvhdAcuityEnum.md)
 * [gvhd_organ](gvhd_organ.md)  <sub>0..1</sub>
     * Description: Graft Versus Host Disease Organ
     * Range: [GvhdOrganEnum](GvhdOrganEnum.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
