---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["BusinessRoles and Participants"]
content_origin: "source-transcription"
---

# BusinessRoles and Participants

Source: [src-000374](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`. Locator: heading path BusinessRoles and Participants.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P198** BusinessRoles and Participants

**P199** A BusinessRole represents an entity (or a class of entities) of the real world, physical or legal, a person, a group of persons, a corporation. Examples of BusinessRoles: “Financial Institution”, “Automated Clearing House”, “Central Securities Depository”.

**P200** A Participant is a functional role performed by a BusinessRole in a particular BusinessProcess or BusinessTransaction. Examples of Participants: the “user” of a system, “debtor”, “creditor”, “investor”. 

**P201** The relationship between BusinessRoles and Participants is many-to-many. One BusinessRole can be involved as different Participants at different moments in time or at the same time. Examples of BusinessRoles:  "user", "debtor”, "creditor", "investor". Different BusinessRoles can be involved as the same Participant.

**P202** In the context of the Securities Settlement, the high-level BusinessArea, Processes, BusinessRoles and typical Participants can be represented as follows:

[fig-0004 - original figure evidence](../diagrams/fig-0004.md)

**P205** The Settlement Queries Responses and Report message set only covers the reporting processes in green. The other processes are included for completeness.

