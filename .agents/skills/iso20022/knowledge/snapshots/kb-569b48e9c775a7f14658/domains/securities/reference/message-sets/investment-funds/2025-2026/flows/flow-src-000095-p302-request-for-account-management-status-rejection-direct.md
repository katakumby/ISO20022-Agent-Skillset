---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p302-request-for-account-management-status-rejection-direct"
title: "Account Management / Request for Account Management Status Rejection - Direct"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Account Management", "Request for Account Management Status Rejection - Direct"], "locator": "/w:document/w:body/w:p[302]", "paragraph_id": "P302", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Account Management", "Request for Account Management Status Rejection - Direct"], "locator": "/w:document/w:body/w:p[303]", "paragraph_id": "P303", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Account Management", "Request for Account Management Status Rejection - Direct"], "locator": "/w:document/w:body/w:p[304]", "paragraph_id": "P304", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Account Management", "Request for Account Management Status Rejection - Direct"], "locator": "/w:document/w:body/w:p[305]", "paragraph_id": "P305", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Account Management", "Request for Account Management Status Rejection - Direct"], "locator": "/w:document/w:body/w:p[306]", "paragraph_id": "P306", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Account Management", "Request for Account Management Status Rejection - Direct"], "locator": "/w:document/w:body/w:p[307]", "paragraph_id": "P307", "table_id": null}]
participants: ["participant-src-000095-account-owner", "participant-src-000095-account-servicer", "participant-src-000095-custodian", "participant-src-000095-designated-agent", "participant-src-000095-investor", "participant-src-000095-registrar", "participant-src-000095-transfer-agent"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Account Management"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000096", "locator": "file page 77; 5 acmt.005.001.06 RequestForAccountManagementStatusReportV06"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Account Management"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[6]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000096", "locator": "file page 86; 6 acmt.006.001.07 AccountManagementStatusReportV07"}, {"source_id": "src-000096", "locator": "file page 371; 17 semt.001.001.03 SecuritiesMessageRejectionV03"}]
message_ids: []
message_families: ["acmt.005", "acmt.006", "semt.001"]
search_terms: ["Request for Account Management Status Rejection - Direct", "Intermediary", "acmt.005", "acmt.006", "semt.001"]
limitations: ["Arrow direction and order follow the literal picture. Mermaid uses standard solid arrowheads rather than source open-head geometry; no additional synchrony, timing or network guarantee is inferred.", "P303: request violates SLA or account cannot be uniquely identified; rejected status includes a reason.", "P305: no SLA or unrecognised reference. P307 describes intermediaries forwarding rejection although this picture is direct.", "Part1 message names/families do not establish exact versions; use maintained Part2/schema references.", "Source bank icons denote named participants, not institutional identity of a functional role. Repeated instructing-party occurrences are distinct parties using the same role definition."]
manual_curated: true
participant_ids: ["participant-src-000095-account-owner", "participant-src-000095-account-servicer", "participant-src-000095-custodian", "participant-src-000095-designated-agent", "participant-src-000095-investor", "participant-src-000095-registrar", "participant-src-000095-transfer-agent"]
related_diagrams: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0034.md", "domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0035.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Complete source-delimited narrative and literal diagram messages/directions checked; institutional examples retained separately."}
---

# Account Management / Request for Account Management Status Rejection - Direct

[src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md); source heading P302, direct-body paragraph P304, direct-body paragraph P306.

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

**P303** If a RequestForAccountManagementStatusReport message is not compliant with an agreed SLA or if the account cannot be uniquely identified by the account servicer, then an AccountManagementStatusReport message with a rejected status and reason code is sent by the account servicer to the account owner.

**P305** If there is no SLA between the account owner and servicer or the linked reference is not recognised, a SecuritiesMessageRejection message is sent by the account servicer to the account owner.

**P307** For scenarios involving an intermediary, the AccountManagementStatusReport message or the SecuritiesMessageRejection message is forwarded by the intermediary to the account owner.

### fig-0034

[Literal source sequence and visual review](../diagrams/funds-processes/fig-0034.md) (Word file page 48).

| Step | Sender | Receiver | Source message label |
| --- | --- | --- | --- |
| 1 | [Account Owner](../../../../../../../shared/reference/participants/participant-src-000095-account-owner.md) | [Account Servicer](../../../../../../../shared/reference/participants/participant-src-000095-account-servicer.md) | AccountOpeningInstruction |
| 2 | [Account Owner](../../../../../../../shared/reference/participants/participant-src-000095-account-owner.md) | [Account Servicer](../../../../../../../shared/reference/participants/participant-src-000095-account-servicer.md) | RequestForAccountManagementStatusReport |
| 3 | [Account Servicer](../../../../../../../shared/reference/participants/participant-src-000095-account-servicer.md) | [Account Owner](../../../../../../../shared/reference/participants/participant-src-000095-account-owner.md) | AccountManagementStatusReport &lt;Rjctd&gt; |


### fig-0035

[Literal source sequence and visual review](../diagrams/funds-processes/fig-0035.md) (Word file page 48).

| Step | Sender | Receiver | Source message label |
| --- | --- | --- | --- |
| 1 | [Account Owner](../../../../../../../shared/reference/participants/participant-src-000095-account-owner.md) | [Account Servicer](../../../../../../../shared/reference/participants/participant-src-000095-account-servicer.md) | AccountOpeningInstruction |
| 2 | [Account Owner](../../../../../../../shared/reference/participants/participant-src-000095-account-owner.md) | [Account Servicer](../../../../../../../shared/reference/participants/participant-src-000095-account-servicer.md) | RequestForAccountManagementStatusReport |
| 3 | [Account Servicer](../../../../../../../shared/reference/participants/participant-src-000095-account-servicer.md) | [Account Owner](../../../../../../../shared/reference/participants/participant-src-000095-account-owner.md) | SecuritiesMessageRejection |



## Message definitions and related paths

| Family | Supplied exact definition | Scope |
| --- | --- | --- |
| acmt.005 | [acmt.005.001.06](../../../../messages/acmt.005.001.06/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| acmt.006 | [acmt.006.001.07](../../../../messages/acmt.006.001.07/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |
| semt.001 | [semt.001.001.03](../../../../messages/semt.001.001.03/index.md) | Same-set Part2/schema reference; this Part1 flow uses names/families. |


## Outcomes and source qualifications

- Arrow direction and order follow the literal picture. Mermaid uses standard solid arrowheads rather than source open-head geometry; no additional synchrony, timing or network guarantee is inferred.
- P303: request violates SLA or account cannot be uniquely identified; rejected status includes a reason.
- P305: no SLA or unrecognised reference. P307 describes intermediaries forwarding rejection although this picture is direct.
- Part1 message names/families do not establish exact versions; use maintained Part2/schema references.
- Source bank icons denote named participants, not institutional identity of a functional role. Repeated instructing-party occurrences are distinct parties using the same role definition.

The narrative gives each outcome: execution confirmation, accepted/pending status, reporting/replacement, rejection or cancellation as applicable. These outcomes are not interchanged. For cancellation, CAND concerns completion of the requested cancellation; order acceptance (PACK) does not assert execution.

## Review

Source narrative, participant roles and every depicted message direction were compared with the original picture and Word-rendered page on 2026-11-09. The bounded flow scope is reviewed; referenced schemas and tables retain their own statuses.
