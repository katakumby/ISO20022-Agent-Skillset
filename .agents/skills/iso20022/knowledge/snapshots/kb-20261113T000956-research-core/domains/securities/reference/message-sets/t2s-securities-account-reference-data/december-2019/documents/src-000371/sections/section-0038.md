---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["BusinessTransactions", "Modification Process", "Confirmation Scenario"]
content_origin: "source-transcription"
---

# Confirmation Scenario

Source: [src-000371](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`. Locator: heading path BusinessTransactions / Modification Process / Confirmation Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P217** Confirmation Scenario

**P218** Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing party

**P220** Securities Account Modification Request (reda.023)Modification processSecurities Account Status Advice (reda.020): QUEUEDSecurities Account Status Advice (reda.020): COMPLETED

[fig-0014 - original figure evidence](../diagrams/fig-0014.md)

**P221** Securities Account Maintenance Request

**P222** The Instruction Party sends an instruction to the Executing/Servicing Party to modify data for a securities account. This instruction contains information that uniquely identify the securities account. 

**P223** In this case, this instruction contains details of the restriction like the restriction type and timeframe.

**P224** Securities Account Status Advice

**P225** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P227** Queued

**P228** The Executing/Servicing Party might inform the Instructing party that the processing of the Modify Securities Account instruction has been delayed. In case of e.g. a night-time cycle is running

**P229**  

**P230** Completed

**P231** The Executing/Servicing Party informs the Instructing party that the Modify Securities Account instruction has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the securities account that has been processed.

