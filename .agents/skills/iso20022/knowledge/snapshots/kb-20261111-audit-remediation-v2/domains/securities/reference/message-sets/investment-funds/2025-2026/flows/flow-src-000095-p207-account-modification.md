---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p207-account-modification"
title: "Account Modification"
source_locations: [{"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Account Administration", "Account Modification"], "locator": "/w:document/w:body/w:p[207]", "paragraph_id": "P207", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Account Administration", "Account Modification"], "locator": "/w:document/w:body/w:p[208]", "paragraph_id": "P208", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Account Administration", "Account Modification"], "locator": "/w:document/w:body/w:tbl[38]", "paragraph_id": null, "table_id": "T38"}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party", "participant-src-000095-executing-party-registering-party"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Account Management"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000096", "locator": "file page 20; 2 acmt.001.001.08 AccountOpeningInstructionV08"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Account Management"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000096", "locator": "file page 57; 4 acmt.003.001.08 AccountModificationInstructionV08"}]
message_ids: []
message_families: ["acmt.001", "acmt.003"]
search_terms: ["Account Modification", "Executing Party / Registering Party", "Instructing Party", "Executing Party", "acmt.001", "acmt.003"]
limitations: ["The source draws no connector between Provide Status and Provide Confirmation. T38 Status Received text literally says account opening instruction despite the account-modification context; preserve that wording in the source table.", "Unlabelled plain source connectors are retained as undirected lines; business direction established by the activity table is described separately. Blank start/end and control symbols remain blank. Mermaid swimlanes preserve responsibility labels but not the exact source geometry."]
manual_curated: true
participant_ids: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party", "participant-src-000095-executing-party-registering-party"]
related_diagrams: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0010.md"]
updated: "2026-11-09"
diagram_review: {"status": "pass", "date": "2026-11-09", "reviewer": "shared-evidence agent", "scope": "Original extracted picture and complete Word-rendered source page compared with rendered Mermaid PNG; checked actor occurrences, source labels, endpoints, arrowheads/plain lines, lane/control boundaries and alternatives. Complete-page composition checked in contact sheets; original pictures inspected at readable size.", "source_page": 27, "result_notes": ["All source edges and labels compared; plain-line connectors not promoted to inferred direction."]}
issue_ids: ["issue-000041"]
---



# Account Modification Flow

[src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md); Description of BusinessActivities / Account Administration / Account Modification; direct-body paragraph P208; T38.

## Purpose, trigger and conditions

[Source business-process conditions T21](../documents/src-000095/tables/tbl-0021.md)

| Item | Description |
| --- | --- |
| Definition | The account servicer creates and maintains an accounting record for the account owner/intermediary with the fund and records static information relating to the account owner/intermediary, for example, name, address, credit limit, anti-money laundering checks, tax and residency status, income distribution instructions, settlement instructions and terms and intermediary. |
| Trigger | investor wants to make an investment in a fund<br>account owner wants to open, maintain or close its account |
| Pre-conditions | formal demand from the account owner to open, maintain or close an account<br>if the account is to be closed, then a zero balance in the account |
| Post-conditions | anti-money laundering, legal documentation or other documentation is available <br>credit limit is set<br>account identification is attributed<br>direct debit mandates are set up<br>power of attorney is added<br>reporting is defined<br>commission schedule is defined<br>confirmation of account details is provided to the account owner or its intermediary<br>relevant tax authorities are informed<br>account is open, updated or closed |
| Role | Account servicer |


## Participants and responsibilities

- [instructing party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)
- [executing party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md)
- [executing party registering party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party-registering-party.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Instruct Account Modification | The account modification instruction is sent to the executing party. The executing party may also be known as the registering party. | Instructing Party |
| Validate/Provide Status | The account modification instruction is validated and processed. The executing party can send one or more status messages to the instructing party to keep it updated on progress so far. | Executing Party / Registering Party |
| Status Received | The instructing party receives an intermediate status to confirm receipt or updates of the account opening instruction. | Instructing Party |
| Provide Confirmation | If the instruction is accepted by the executing party, the details of the successfully modified account are sent by the executing party to the instructing party. | Executing Party / Registering Party |


## Ordered paths, messages and alternatives

[Complete source reconstruction, connector list and decision paths](../diagrams/funds-processes/fig-0010.md)

Follow the source graph for connected activities; the source table lists responsibilities rather than a universal execution order. Source-labelled exchange types are retained; this high-level activity view does not establish exact message versions.

## Source qualifications and omissions

- The source draws no connector between Provide Status and Provide Confirmation. T38 Status Received text literally says account opening instruction despite the account-modification context; preserve that wording in the source table.
- Unlabelled plain source connectors are retained as undirected lines; business direction established by the activity table is described separately. Blank start/end and control symbols remain blank. Mermaid swimlanes preserve responsibility labels but not the exact source geometry.
