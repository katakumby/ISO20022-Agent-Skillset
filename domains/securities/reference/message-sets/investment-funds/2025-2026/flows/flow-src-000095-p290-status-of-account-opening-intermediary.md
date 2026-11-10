---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p290-status-of-account-opening-intermediary"
title: "Account Management / Status of Account Opening - Intermediary"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Account Management", "Status of Account Opening - Intermediary"], "locator": "/w:document/w:body/w:p[290]", "paragraph_id": "P290", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Account Management", "Status of Account Opening - Intermediary"], "locator": "/w:document/w:body/w:p[291]", "paragraph_id": "P291", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Account Management", "Status of Account Opening - Intermediary"], "locator": "/w:document/w:body/w:p[292]", "paragraph_id": "P292", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Account Management", "Status of Account Opening - Intermediary"], "locator": "/w:document/w:body/w:p[293]", "paragraph_id": "P293", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Account Management", "Status of Account Opening - Intermediary"], "locator": "/w:document/w:body/w:p[294]", "paragraph_id": "P294", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Account Management", "Status of Account Opening - Intermediary"], "locator": "/w:document/w:body/w:p[295]", "paragraph_id": "P295", "table_id": null}]
participants: ["participant-src-000095-account-owner", "participant-src-000095-account-servicer", "participant-src-000095-custodian", "participant-src-000095-designated-agent", "participant-src-000095-intermediary", "participant-src-000095-investor", "participant-src-000095-registrar", "participant-src-000095-transfer-agent"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Account Management"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000096", "locator": "file page 20; 2 acmt.001.001.08 AccountOpeningInstructionV08"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Account Management"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000096", "locator": "file page 38; 3 acmt.002.001.08 AccountDetailsConfirmationV08"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Account Management"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000096", "locator": "file page 77; 5 acmt.005.001.06 RequestForAccountManagementStatusReportV06"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Account Management"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[6]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000096", "locator": "file page 86; 6 acmt.006.001.07 AccountManagementStatusReportV07"}]
message_ids: []
message_families: ["acmt.001", "acmt.002", "acmt.005", "acmt.006"]
search_terms: ["Status of Account Opening - Intermediary", "Intermediary", "acmt.001", "acmt.002", "acmt.005", "acmt.006"]
limitations: ["Arrow direction and order follow the literal picture. Mermaid uses standard solid arrowheads rather than source open-head geometry; no additional synchrony, timing or network guarantee is inferred.", "Part1 message names/families do not establish exact versions; use maintained Part2/schema references.", "Source bank icons denote named participants, not institutional identity of a functional role. Repeated instructing-party occurrences are distinct parties using the same role definition."]
manual_curated: true
participant_ids: ["participant-src-000095-account-owner", "participant-src-000095-account-servicer", "participant-src-000095-custodian", "participant-src-000095-designated-agent", "participant-src-000095-intermediary", "participant-src-000095-investor", "participant-src-000095-registrar", "participant-src-000095-transfer-agent"]
related_diagrams: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0032.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Complete source-delimited narrative and literal diagram messages/directions checked; institutional examples retained separately."}
---

# Account Management / Status of Account Opening - Intermediary

[src-000095](../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx); source heading P290, direct-body paragraph P295.

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
| [intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | Explicit figure sender/receiver; see step table. |
| [investor](../../../../../../../shared/reference/participants/participant-src-000095-investor.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [registrar](../../../../../../../shared/reference/participants/participant-src-000095-registrar.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |
| [transfer agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | Narrative institutional/example participant; not separately drawn in these sequences. Functional role depends on the cited relationship. |


## Ordered activities and source-defined alternatives

**P291** In a scenario involving an intermediary, the account owner sends a RequestForAccountManagementStatusReport message to an intermediary to request the processing status of a previously sent AccountOpeningInstruction message for which an AccountDetailsConfirmation message has not yet been received. The intermediary either forwards the message to another intermediary, or to the account servicer.

**P292** The intermediary may also send an AccountManagementStatusReport message with the status SentToNextParty (STNP) to the account owner.

**P293** After the receipt of the RequestForAccountManagementStatusReport message, the account servicer sends an AccountManagementStatusReport message, with the appropriate status, to the intermediary. This intermediary in turn forwards the AccountManagementStatusReport message to the previous intermediary in the chain, or to the account owner.

**P294** Once the AccountOpeningInstruction message has been successfully processed, the account servicer sends the AccountDetailsConfirmation message to the intermediary. The intermediary either forwards the message to another intermediary in the chain, or to the account owner.

### fig-0032

[Literal source sequence and visual review](../diagrams/funds-processes/fig-0032.md) (Word file page 46).

| Step | Sender | Receiver | Source message label |
| --- | --- | --- | --- |
| 1 | [Account Owner](../../../../../../../shared/reference/participants/participant-src-000095-account-owner.md) | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | AccountOpeningInstruction |
| 2 | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | [Account Servicer](../../../../../../../shared/reference/participants/participant-src-000095-account-servicer.md) | AccountOpeningInstruction |
| 3 | [Account Owner](../../../../../../../shared/reference/participants/participant-src-000095-account-owner.md) | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | RequestForAccountManagementStatusReport |
| 4 | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | [Account Servicer](../../../../../../../shared/reference/participants/participant-src-000095-account-servicer.md) | RequestForAccountManagementStatusReport |
| 5 | [Account Servicer](../../../../../../../shared/reference/participants/participant-src-000095-account-servicer.md) | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | AccountManagementStatusReport |
| 6 | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | [Account Owner](../../../../../../../shared/reference/participants/participant-src-000095-account-owner.md) | AccountManagementStatusReport |
| 7 | [Account Servicer](../../../../../../../shared/reference/participants/participant-src-000095-account-servicer.md) | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | AccountDetailsConfirmation (ACCO) |
| 8 | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | [Account Owner](../../../../../../../shared/reference/participants/participant-src-000095-account-owner.md) | AccountDetailsConfirmation (ACCO) |



## Message definitions and related paths

| Family | Supplied exact definition | Scope |
| --- | --- | --- |
| acmt.001 | [acmt.001.001.08](../../../../messages/acmt.001.001.08/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| acmt.002 | [acmt.002.001.08](../../../../messages/acmt.002.001.08/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| acmt.005 | [acmt.005.001.06](../../../../messages/acmt.005.001.06/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| acmt.006 | [acmt.006.001.07](../../../../messages/acmt.006.001.07/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |


## Outcomes and source qualifications

- Arrow direction and order follow the literal picture. Mermaid uses standard solid arrowheads rather than source open-head geometry; no additional synchrony, timing or network guarantee is inferred.
- Part1 message names/families do not establish exact versions; use maintained Part2/schema references.
- Source bank icons denote named participants, not institutional identity of a functional role. Repeated instructing-party occurrences are distinct parties using the same role definition.

The narrative gives each outcome: execution confirmation, accepted/pending status, reporting/replacement, rejection or cancellation as applicable. These outcomes are not interchanged. For cancellation, CAND concerns completion of the requested cancellation; order acceptance (PACK) does not assert execution.

## Review

Source narrative, participant roles and every depicted message direction were compared with the original picture and Word-rendered page on 2026-11-09. The bounded flow scope is reviewed; referenced schemas and tables retain their own statuses.
