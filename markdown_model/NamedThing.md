
# Class: NamedThing




URI: [https://w3id.org/pcdc/model/NamedThing](https://w3id.org/pcdc/model/NamedThing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Subject],[Person],[NamedThing&#124;submitter_id:string;type:string%20%3F]^-[Timing],[NamedThing]^-[Subject],[NamedThing]^-[Person],[NamedThing]^-[FamilyMedicalHistory],[FamilyMedicalHistory])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Subject],[Person],[NamedThing&#124;submitter_id:string;type:string%20%3F]^-[Timing],[NamedThing]^-[Subject],[NamedThing]^-[Person],[NamedThing]^-[FamilyMedicalHistory],[FamilyMedicalHistory])

## Children

 * [FamilyMedicalHistory](FamilyMedicalHistory.md) - prior cancer information of a first-degree relative
 * [Person](Person.md) - demographic information about an individual
 * [Subject](Subject.md)
 * [Timing](Timing.md)

## Referenced by Class


## Attributes


### Own

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>0..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
