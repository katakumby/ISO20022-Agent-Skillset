---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p266-intermediary"
title: "Account Management / Account Modification / Intermediary"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Account Management", "Account Modification", "Intermediary"], "locator": "/w:document/w:body/w:p[266]", "paragraph_id": "P266", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Account Management", "Account Modification", "Intermediary"], "locator": "/w:document/w:body/w:p[267]", "paragraph_id": "P267", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Account Management", "Account Modification", "Intermediary"], "locator": "/w:document/w:body/w:p[268]", "paragraph_id": "P268", "table_id": null}]
participants: ["participant-src-000095-account-owner", "participant-src-000095-account-servicer", "participant-src-000095-custodian", "participant-src-000095-designated-agent", "participant-src-000095-intermediary", "participant-src-000095-investor", "participant-src-000095-registrar", "participant-src-000095-transfer-agent"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Account Management"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000096", "locator": "file page 38; 3 acmt.002.001.08 AccountDetailsConfirmationV08"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Account Management"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000096", "locator": "file page 57; 4 acmt.003.001.08 AccountModificationInstructionV08"}]
message_ids: []
message_families: ["acmt.002", "acmt.003"]
search_terms: ["Intermediary", "Intermediary", "acmt.002", "acmt.003"]
limitations: ["Arrow direction and order follow the literal picture. Mermaid uses standard solid arrowheads rather than source open-head geometry; no additional synchrony, timing or network guarantee is inferred.", "Part1 message names/families do not establish exact versions; use maintained Part2/schema references.", "Source bank icons denote named participants, not institutional identity of a functional role. Repeated instructing-party occurrences are distinct parties using the same role definition."]
manual_curated: true
participant_ids: ["participant-src-000095-account-owner", "participant-src-000095-account-servicer", "participant-src-000095-custodian", "participant-src-000095-designated-agent", "participant-src-000095-intermediary", "participant-src-000095-investor", "participant-src-000095-registrar", "participant-src-000095-transfer-agent"]
related_diagrams: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0025.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Complete source-delimited narrative and literal diagram messages/directions checked; institutional examples retained separately."}
---

# Account Management / Account Modification / Intermediary

[src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md); source heading P266, direct-body paragraph P268.

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

**P267** In the scenario involving an intermediary, the account owner sends an AccountModificationInstruction message to an intermediary. The intermediary either forwards the message to another intermediary, or to the account servicer. The account servicer sends an AccountDetailsConfirmation message to the intermediary from which the AccountModificationInstruction message was received. This intermediary then forwards the AccountDetailsConfirmation message to the previous intermediary in the chain, or to the account owner.

### fig-0025

[Literal source sequence and visual review](../diagrams/funds-processes/fig-0025.md) (Word file page 43).

| Step | Sender | Receiver | Source message label |
| --- | --- | --- | --- |
| 1 | [Account Owner](../../../../../../../shared/reference/participants/participant-src-000095-account-owner.md) | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | AccountModificationInstruction |
| 2 | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | [Account Servicer](../../../../../../../shared/reference/participants/participant-src-000095-account-servicer.md) | AccountModificationInstruction |
| 3 | [Account Servicer](../../../../../../../shared/reference/participants/participant-src-000095-account-servicer.md) | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | AccountDetailsConfirmation (ACCM) |
| 4 | [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | [Account Owner](../../../../../../../shared/reference/participants/participant-src-000095-account-owner.md) | AccountDetailsConfirmation (ACCM) |



## Message definitions and related paths

| Family | Supplied exact definition | Scope |
| --- | --- | --- |
| acmt.002 | [acmt.002.001.08](../../../../messages/acmt.002.001.08/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| acmt.003 | [acmt.003.001.08](../../../../messages/acmt.003.001.08/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |


## Outcomes and source qualifications

- Arrow direction and order follow the literal picture. Mermaid uses standard solid arrowheads rather than source open-head geometry; no additional synchrony, timing or network guarantee is inferred.
- Part1 message names/families do not establish exact versions; use maintained Part2/schema references.
- Source bank icons denote named participants, not institutional identity of a functional role. Repeated instructing-party occurrences are distinct parties using the same role definition.

The narrative gives each outcome: execution confirmation, accepted/pending status, reporting/replacement, rejection or cancellation as applicable. These outcomes are not interchanged. For cancellation, CAND concerns completion of the requested cancellation; order acceptance (PACK) does not assert execution.

## Review

Source narrative, participant roles and every depicted message direction were compared with the original picture and Word-rendered page on 2026-11-09. The bounded flow scope is reviewed; referenced schemas and tables retain their own statuses.
