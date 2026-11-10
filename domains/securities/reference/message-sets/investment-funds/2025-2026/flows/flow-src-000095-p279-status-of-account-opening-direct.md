---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p279-status-of-account-opening-direct"
title: "Account Management / Status of Account Opening - Direct"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Account Management", "Status of Account Opening - Direct"], "locator": "/w:document/w:body/w:p[279]", "paragraph_id": "P279", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Account Management", "Status of Account Opening - Direct"], "locator": "/w:document/w:body/w:p[280]", "paragraph_id": "P280", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Account Management", "Status of Account Opening - Direct"], "locator": "/w:document/w:body/w:p[281]", "paragraph_id": "P281", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Account Management", "Status of Account Opening - Direct"], "locator": "/w:document/w:body/w:p[282]", "paragraph_id": "P282", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Account Management", "Status of Account Opening - Direct"], "locator": "/w:document/w:body/w:p[283]", "paragraph_id": "P283", "table_id": null}]
participants: ["participant-src-000095-account-owner", "participant-src-000095-account-servicer", "participant-src-000095-custodian", "participant-src-000095-designated-agent", "participant-src-000095-investor", "participant-src-000095-registrar", "participant-src-000095-transfer-agent"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Account Management"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000096", "locator": "file page 20; 2 acmt.001.001.08 AccountOpeningInstructionV08"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Account Management"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000096", "locator": "file page 38; 3 acmt.002.001.08 AccountDetailsConfirmationV08"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Account Management"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000096", "locator": "file page 77; 5 acmt.005.001.06 RequestForAccountManagementStatusReportV06"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Account Management"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[6]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000096", "locator": "file page 86; 6 acmt.006.001.07 AccountManagementStatusReportV07"}]
message_ids: []
message_families: ["acmt.001", "acmt.002", "acmt.005", "acmt.006"]
search_terms: ["Status of Account Opening - Direct", "acmt.001", "acmt.002", "acmt.005", "acmt.006"]
limitations: ["Arrow direction and order follow the literal picture. Mermaid uses standard solid arrowheads rather than source open-head geometry; no additional synchrony, timing or network guarantee is inferred.", "Literal picture shows closure, but heading Status of Account Opening and P280–282 describe an opening-status request. Both source claims are retained under issue-000041.", "Part1 message names/families do not establish exact versions; use maintained Part2/schema references.", "Source bank icons denote named participants, not institutional identity of a functional role. Repeated instructing-party occurrences are distinct parties using the same role definition."]
manual_curated: true
participant_ids: ["participant-src-000095-account-owner", "participant-src-000095-account-servicer", "participant-src-000095-custodian", "participant-src-000095-designated-agent", "participant-src-000095-investor", "participant-src-000095-registrar", "participant-src-000095-transfer-agent"]
related_diagrams: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0030.md"]
issue_ids: ["issue-000041"]
review_evidence: {"date": "2026-11-09", "scope": "Complete source-delimited narrative and literal diagram messages/directions checked; institutional examples retained separately."}
---

# Account Management / Status of Account Opening - Direct

[src-000095](../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx); source heading P279, direct-body paragraph P283.

## Purpose, trigger and common conditions

**P237** This message flow section illustrates the use of the account management messages in typical message sequencing scenarios. The account management messages are exchanged between an account owner and an account servicer. There may be one or more intermediaries between the account owner and the account servicer.

**P238** The account owner is, for example, an investor or its designated agent. The account servicer is, for example, a registrar, transfer agent or custodian.

**P239** Account Opening

The source-specific trigger, acceptance conditions, outcomes and optional/failure paths are preserved in the ordered narrative below. A separate formal precondition/postcondition is asserted only where the source supplies one.

## Participants and responsibilities

| Scoped participant | Participation evidence |
| --- | --- |
| [account owner](../../../../../../../shared/reference/participants/participant-src-000095-account-owner.md) | Explicit figure sender/receiver; see step table. |
| [account servicer](../../../../../../../shared/reference/participants/participant-src-000095-account-servicer.md) | Explicit figure sender/receiver; see step table. |
| [custodian](../../../../../../../shared/reference/participants/participant-src-000095-custodian.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [designated agent](../../../../../../../shared/reference/participants/participant-src-000095-designated-agent.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [investor](../../../../../../../shared/reference/participants/participant-src-000095-investor.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [registrar](../../../../../../../shared/reference/participants/participant-src-000095-registrar.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [transfer agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |


## Ordered activities and source-defined alternatives

**P280** The account owner sends a RequestForAccountManagementStatusReport message to the account servicer to request the processing status of a previously sent AccountOpeningInstruction message for which an AccountDetailsConfirmation message has not yet been received.

**P281** The account servicer sends an AccountManagementStatusReport message to the account owner with the appropriate status code. More than one AccountManagementStatusReport message may sent to reflect the status as the status changes.

**P282** Once the AccountOpeningInstruction message has been successfully processed, the account servicer sends the AccountDetailsConfirmation message to the account owner.

### fig-0030

[Literal source sequence and visual review](../diagrams/funds-processes/fig-0030.md) (Word file page 45).

| Step | Sender | Receiver | Source message label |
| --- | --- | --- | --- |
| 1 | [Account Owner](../../../../../../../shared/reference/participants/participant-src-000095-account-owner.md) | [Account Servicer](../../../../../../../shared/reference/participants/participant-src-000095-account-servicer.md) | AccountModificationInstruction (CLOS) |
| 2 | [Account Servicer](../../../../../../../shared/reference/participants/participant-src-000095-account-servicer.md) | [Account Owner](../../../../../../../shared/reference/participants/participant-src-000095-account-owner.md) | AccountManagementStatusReport &lt;RECE&gt; |
| 3 | [Account Servicer](../../../../../../../shared/reference/participants/participant-src-000095-account-servicer.md) | [Account Owner](../../../../../../../shared/reference/participants/participant-src-000095-account-owner.md) | AccountDetailsConfirmation (ACCM) + &lt;Clsd&gt; |



## Message definitions and related paths

| Family | Supplied exact definition | Scope |
| --- | --- | --- |
| acmt.001 | [acmt.001.001.08](../../../../messages/acmt.001.001.08/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| acmt.002 | [acmt.002.001.08](../../../../messages/acmt.002.001.08/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| acmt.005 | [acmt.005.001.06](../../../../messages/acmt.005.001.06/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| acmt.006 | [acmt.006.001.07](../../../../messages/acmt.006.001.07/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |


## Outcomes and source qualifications

- Arrow direction and order follow the literal picture. Mermaid uses standard solid arrowheads rather than source open-head geometry; no additional synchrony, timing or network guarantee is inferred.
- Literal picture shows closure, but heading Status of Account Opening and P280–282 describe an opening-status request. Both source claims are retained under issue-000041.
- Part1 message names/families do not establish exact versions; use maintained Part2/schema references.
- Source bank icons denote named participants, not institutional identity of a functional role. Repeated instructing-party occurrences are distinct parties using the same role definition.

The narrative gives each outcome: execution confirmation, accepted/pending status, reporting/replacement, rejection or cancellation as applicable. These outcomes are not interchanged. For cancellation, CAND concerns completion of the requested cancellation; order acceptance (PACK) does not assert execution.

## Review

Source narrative, participant roles and every depicted message direction were compared with the original picture and Word-rendered page on 2026-11-09. Unresolved source conflict: issue-000041.
