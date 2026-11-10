---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["BusinessRoles and Participants"]
content_origin: "source-transcription"
---

# BusinessRoles and Participants

Source: [src-000365](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`. Locator: heading path BusinessRoles and Participants.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P98** BusinessRoles and Participants

**P99** A BusinessRole represents an entity (or a class of entities) of the real world, physical or legal, a person, a group of persons, a corporation. Examples of BusinessRoles: “Financial Institution”, “Automated Clearing House”, “Central Securities Depository”.

**P100** A Participant is a functional role performed by a BusinessRole in a particular BusinessProcess or BusinessTransaction. Examples of Participants: the “user” of a system, “debtor”, “creditor”, “investor”. 

**P101** The relationship between BusinessRoles and Participants is many-to-many. One BusinessRole can be involved as different Participants at different moments in time or at the same time. Examples of BusinessRoles:  "user", "debtor”, "creditor", "investor". Different BusinessRoles can be involved as the same Participant.

**P102** In the context of the Party Reference Data, the high-level BusinessRoles and typical Participants can be represented as follows:

[fig-0001 - original figure evidence](../diagrams/fig-0001.md)

