---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000356"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["BusinessRoles and Participants"]
content_origin: "source-transcription"
---

# BusinessRoles and Participants

Source: [src-000356](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralReporting_2023_2024_v2.docx`. Locator: heading path BusinessRoles and Participants.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P99** BusinessRoles and Participants

**P100** A BusinessRole represents an entity (or a class of entities) of the real world, physical or legal, a person, a group of persons, a corporation. Examples of BusinessRoles: “Financial Institution”, “Automated Clearing House”, “Central Securities Depository”.

**P101** A Participant is a functional role performed by a BusinessRole in a particular BusinessProcess or BusinessTransaction. Examples of Participants: the “user” of a system, “debtor”, “creditor”, “investor”. 

**P102** The relationship between BusinessRoles and Participants is many-to-many. One BusinessRole can be involved as different Participants at different moments in time or at the same time. Examples of BusinessRoles:  "user", "debtor”, "creditor", "investor". Different BusinessRoles can be involved as the same Participant.

**P103** A business actor represents an entity (or a class of entities) of the real world, physical or legal, a person, a group of persons, a corporation. E.g. of business actors: “Financial Institution”, “ACH”, “CSD”, NCB. 

**P104** A business role is a role performed by a business actor in a specific business context and process: e.g. the “user” of a system, “debtor”, “creditor”, “investor” etc. 

**P105** Relationship between business roles and actors is many-to-many. One business actor (i.e. a person) can play different roles at different moments in time or at the same time: "user", "debtor, "creditor", "investor" etc. One role can also be played by different actors. 

**P107** In the context of Collateral Reporting, the high-level business roles and typical actors can be represented as follows, based on the hierarchy of Roles defined in T2S as a securities settlement engine: 

**P108**  

[fig-0001 - original figure evidence](../diagrams/fig-0001.md)

**P110** T2S supports a hierarchical model of roles and access rights to ensure the segregation of both functions and data. The area of the slide shaded in grey represents the data set-up for T2S dedicated cash accounts required in the static data of T2S. An NCB, acting as a CSD in its home country and providing dedicated cash accounts in T2S, will have the role of NCB and CSD and will exist in T2S as both a CSD and an NCB.

