
# Class: DiseaseCharacteristics




URI: [https://w3id.org/pcdc/model/DiseaseCharacteristics](https://w3id.org/pcdc/model/DiseaseCharacteristics)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[DiseaseCharacteristics&#124;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;risk_group_system:RiskGroupSystemEnum%20%3F;risk_group:RiskGroupEnum%20%3F;mki:MkiEnum%20%3F;disease_site:DiseaseSiteEnum%20%3F;detection_method:DetectionMethodEnum%20%3F;cns_disease_status:CnsDiseaseStatusEnum%20%3F;performance_score:PerformanceScoreEnum%20%3F;performance_score_system:PerformanceScoreSystemEnum%20%3F;gpoh_score:GpohScoreEnum%20%3F;prior_steroids_week:NoNotreportedUnknownYesEnum%20%3F;prior_steroids_month:NoNotreportedUnknownYesEnum%20%3F;bulk_disease:NoNotreportedUnknownYesEnum%20%3F;bulk_nodal_aggregate:NoNotreportedUnknownYesEnum%20%3F;bulk_med_mass:NoNotreportedUnknownYesEnum%20%3F;med_ratio:integer%20%3F;fever:NoNotreportedUnknownYesEnum%20%3F;night_sweats:NoNotreportedUnknownYesEnum%20%3F;weight_loss:NoNotreportedUnknownYesEnum%20%3F;nodular_splenic:NoNotreportedUnknownYesEnum%20%3F;initial_treatment_category:InitialTreatmentCategoryEnum%20%3F;myeloid_sarcoma:NoNotreportedUnknownYesEnum%20%3F;myeloid_sarcoma_site:MyeloidSarcomaSiteEnum%20%3F;gts:NoNotreportedUnknownYesEnum%20%3F;gts_treatment:GtsTreatmentEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[DiseaseCharacteristics])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Thing],[Timing]<timings%200..1-++[DiseaseCharacteristics&#124;disease_phase:DiseasePhaseEnum%20%3F;disease_phase_number:integer%20%3F;course:CourseEnum%20%3F;course_number:integer%20%3F;risk_group_system:RiskGroupSystemEnum%20%3F;risk_group:RiskGroupEnum%20%3F;mki:MkiEnum%20%3F;disease_site:DiseaseSiteEnum%20%3F;detection_method:DetectionMethodEnum%20%3F;cns_disease_status:CnsDiseaseStatusEnum%20%3F;performance_score:PerformanceScoreEnum%20%3F;performance_score_system:PerformanceScoreSystemEnum%20%3F;gpoh_score:GpohScoreEnum%20%3F;prior_steroids_week:NoNotreportedUnknownYesEnum%20%3F;prior_steroids_month:NoNotreportedUnknownYesEnum%20%3F;bulk_disease:NoNotreportedUnknownYesEnum%20%3F;bulk_nodal_aggregate:NoNotreportedUnknownYesEnum%20%3F;bulk_med_mass:NoNotreportedUnknownYesEnum%20%3F;med_ratio:integer%20%3F;fever:NoNotreportedUnknownYesEnum%20%3F;night_sweats:NoNotreportedUnknownYesEnum%20%3F;weight_loss:NoNotreportedUnknownYesEnum%20%3F;nodular_splenic:NoNotreportedUnknownYesEnum%20%3F;initial_treatment_category:InitialTreatmentCategoryEnum%20%3F;myeloid_sarcoma:NoNotreportedUnknownYesEnum%20%3F;myeloid_sarcoma_site:MyeloidSarcomaSiteEnum%20%3F;gts:NoNotreportedUnknownYesEnum%20%3F;gts_treatment:GtsTreatmentEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[DiseaseCharacteristics])

## Parents

 *  is_a: [Thing](Thing.md)

## Attributes


### Own

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
 * [risk_group_system](risk_group_system.md)  <sub>0..1</sub>
     * Description: MaGIC Risk Group
     * Range: [RiskGroupSystemEnum](RiskGroupSystemEnum.md)
 * [risk_group](risk_group.md)  <sub>0..1</sub>
     * Range: [RiskGroupEnum](RiskGroupEnum.md)
 * [mki](mki.md)  <sub>0..1</sub>
     * Description: Mitosis Karyorrhexis Index as revised by the International Neuroblastoma Pathology Classification (INPC)
     * Range: [MkiEnum](MkiEnum.md)
 * [disease_site](disease_site.md)  <sub>0..1</sub>
     * Description: Disease Involvement Site
     * Range: [DiseaseSiteEnum](DiseaseSiteEnum.md)
 * [detection_method](detection_method.md)  <sub>0..1</sub>
     * Description: The method used to detect the extent of the disease involvement.
     * Range: [DetectionMethodEnum](DetectionMethodEnum.md)
 * [cns_disease_status](cns_disease_status.md)  <sub>0..1</sub>
     * Description: CNS Involvement Status
     * Range: [CnsDiseaseStatusEnum](CnsDiseaseStatusEnum.md)
 * [performance_score](performance_score.md)  <sub>0..1</sub>
     * Description: A standard way of measuring the ability of cancer patients to perform ordinary tasks. Scores range from 0 to 100. A higher score means the patient is better able to carry out daily activities. May be used to determine a patient's prognosis, to measure changes in a patient’s ability to function, or to decide if a patient could be included in a clinical trial. (Source: NCI Dictionary of Cancer Terms)
     * Range: [PerformanceScoreEnum](PerformanceScoreEnum.md)
 * [performance_score_system](performance_score_system.md)  <sub>0..1</sub>
     * Range: [PerformanceScoreSystemEnum](PerformanceScoreSystemEnum.md)
 * [gpoh_score](gpoh_score.md)  <sub>0..1</sub>
     * Range: [GpohScoreEnum](GpohScoreEnum.md)
 * [prior_steroids_week](prior_steroids_week.md)  <sub>0..1</sub>
     * Description: Received Steroids within One Week Prior to Diagnosis
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [prior_steroids_month](prior_steroids_month.md)  <sub>0..1</sub>
     * Description: Received Steroids within One Month Prior to Diagnosis
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [bulk_disease](bulk_disease.md)  <sub>0..1</sub>
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [bulk_nodal_aggregate](bulk_nodal_aggregate.md)  <sub>0..1</sub>
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [bulk_med_mass](bulk_med_mass.md)  <sub>0..1</sub>
     * Description: Bulky Mediastinal Mass
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [med_ratio](med_ratio.md)  <sub>0..1</sub>
     * Description: Mediastinal Ratio
     * Range: [Integer](types/Integer.md)
 * [fever](fever.md)  <sub>0..1</sub>
     * Description: An increase in body temperature above normal (98.6 degrees F), usually caused by disease. (Source: NCI Dictionary of Cancer Terms)
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [night_sweats](night_sweats.md)  <sub>0..1</sub>
     * Description: Episodes of excessive sweating that occur during sleep. Night sweats can be severe and soak a person’s bedclothes and bed sheets, which may cause the person to wake up. Night sweats are a common symptom of menopause. They may also be caused by illness or medical conditions, such as infection, cancer, low blood sugar, hormone disorders, and neurologic conditions. They may also be a side effect of certain medicines, cancer treatment, too much caffeine or alcohol, or tobacco or drug use. (Source: NCI Dictionary of Cancer Terms)
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [weight_loss](weight_loss.md)  <sub>0..1</sub>
     * Description: Surgery done to help people who are obese lose weight. There are different types of weight loss surgery, and each type changes the way the digestive system works. Some types make the stomach smaller, which decreases the amount of food that it can hold so the person feels full sooner and eats less. Other types make changes to the stomach and the small intestine, which decreases the nutrients and calories that are absorbed from food. Weight loss surgery can improve many obesity-related health problems, such as diabetes, high blood pressure, unhealthy cholesterol levels, sleep apnea, and knee, hip, or other body pain. Having weight loss surgery may also decrease the risk of some cancers, including endometrial cancer. Also called bariatric surgery. (Source: NCI Dictionary of Cancer Terms)
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [nodular_splenic](nodular_splenic.md)  <sub>0..1</sub>
     * Description: Nodular Splenic Involvement
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [initial_treatment_category](initial_treatment_category.md)  <sub>0..1</sub>
     * Description: The category of initial treatment that the patient receive for their disease.
     * Range: [InitialTreatmentCategoryEnum](InitialTreatmentCategoryEnum.md)
 * [myeloid_sarcoma](myeloid_sarcoma.md)  <sub>0..1</sub>
     * Description: A rare type of cancer that is made up of myeloblasts (a type of immature white blood cell) and forms outside the bone marrow and blood. The tumor cells may look green when viewed under a microscope. Myeloid sarcomas can occur anywhere in the body. They most commonly occur in people with acute myeloid leukemia or a myeloproliferative disorder. Also called chloroma, extramedullary myeloid tumor, and granulocytic sarcoma. (Source: NCI Dictionary of Cancer Terms)
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [myeloid_sarcoma_site](myeloid_sarcoma_site.md)  <sub>0..1</sub>
     * Range: [MyeloidSarcomaSiteEnum](MyeloidSarcomaSiteEnum.md)
 * [gts](gts.md)  <sub>0..1</sub>
     * Range: [NoNotreportedUnknownYesEnum](NoNotreportedUnknownYesEnum.md)
 * [gts_treatment](gts_treatment.md)  <sub>0..1</sub>
     * Description: Growing Teratoma Syndrome Treatment
     * Range: [GtsTreatmentEnum](GtsTreatmentEnum.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
