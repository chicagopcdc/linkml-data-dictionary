
# Class: Person




URI: [https://w3id.org/pcdc/model/Person](https://w3id.org/pcdc/model/Person)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Subject]++-%20persons%201..1>[Person&#124;sex:SexEnum%20%3F;race:RaceEnum%20%3F;race_other:string%20%3F;ethnicity:EthnicityEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[Person],[Subject])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Subject]++-%20persons%201..1>[Person&#124;sex:SexEnum%20%3F;race:RaceEnum%20%3F;race_other:string%20%3F;ethnicity:EthnicityEnum%20%3F;submitter_id(i):string;type(i):string],[Thing]^-[Person],[Subject])

## Parents

 *  is_a: [Thing](Thing.md)

## Referenced by Class

 *  **None** *[➞persons](subject__persons.md)*  <sub>1..1</sub>  **[Person](Person.md)**

## Attributes


### Own

 * [sex](sex.md)  <sub>0..1</sub>
     * Description: The biological sex of the subject.
     * Range: [SexEnum](SexEnum.md)
 * [race](race.md)  <sub>0..1</sub>
     * Description: A group of people who share physical characteristics, such as skin color and facial features. They may also share similar social or cultural identities and ancestral backgrounds. There are many racial groups, and a person may belong to or identify with more than one group. Some diseases, such as cancer, may be more common in certain races than in others. (Source: NCI Dictionary of Cancer Terms)
     * Range: [RaceEnum](RaceEnum.md)
 * [race_other](race_other.md)  <sub>0..1</sub>
     * Description: Specify the "Other" RACE
     * Range: [String](types/String.md)
 * [ethnicity](ethnicity.md)  <sub>0..1</sub>
     * Description: The social and cultural characteristics, backgrounds, or experiences shared by a group of people. These include language, religion, beliefs, values, and behaviors that are often handed down from one generation to the next. Some conditions or diseases, such as cancer, may be more common in certain ethnic groups than in others. (Source: NCI Dictionary of Cancer Terms)
     * Range: [EthnicityEnum](EthnicityEnum.md)

### Inherited from Thing:

 * [submitter_id](submitter_id.md)  <sub>1..1</sub>
     * Description: PCDC internal event ID
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>1..1</sub>
     * Description: Default system-assigned property for each node
     * Range: [String](types/String.md)
