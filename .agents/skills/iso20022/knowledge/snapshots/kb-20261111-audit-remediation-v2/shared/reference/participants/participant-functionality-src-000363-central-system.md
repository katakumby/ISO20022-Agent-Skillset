---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "shared"
domains: ["securities"]
participant_id: "participant-functionality-src-000363-central-system"
title: "central system — T2S LimitUtilisationJournal Functionality"
source_ids: ["src-000363"]
source_editions: ["february-2025"]
source_labels: ["central system"]
aliases: []
role_type: "functional participant explicitly named in message Functionality"
message_sets: ["t2s-limit-utilisation-journal"]
message_ids: ["camt.064.001.01", "camt.065.001.01"]
message_families: ["camt.064", "camt.065"]
source_locations: [{"source_id": "src-000363", "heading": "2 camt.064.001.01 LimitUtilisationJournalQueryV01", "file_pages": [4], "evidence_id": "src-000363-camt.064.001.01-p4-c001"}, {"source_id": "src-000363", "heading": "3 camt.065.001.01 LimitUtilisationJournalReportV01", "file_pages": [9], "evidence_id": "src-000363-camt.065.001.01-p9-c001"}]
identifier_schemes: []
limitations: ["Meaning is scoped to these exact quoted message contexts; a generic role label does not identify one institution across messages.", "A separate formal business-role definition or identifier scheme is not supplied in these Functionality clauses.", "Mention in an example, routing clause or alternative is not automatically an independent sender or receiver."]
---

# central system — T2S LimitUtilisationJournal Functionality

[src-000363](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`

## Definition and business context

System-side counterparty in the LimitUtilisationJournalQuery and LimitUtilisationJournalReport exchanges. Source messages separately identify the CSD or directly connected participant/party at the other side.

This record collects the literal role within this publication. It does not equate that function with a particular institution or with a differently scoped role having the same name.

## Responsibilities, actions and relationships

The complete evidence below preserves who acts, the counterparties, alternatives and conditions. Only explicit clauses establish directions; quoted examples remain examples.

### src-000363-camt.064.001.01-p4-c001

src-000363, file page 4; 2 camt.064.001.01 LimitUtilisationJournalQueryV01.

> The LimitUtilisationJournalQuery message is exchanged between a central securities depository or a directly connected system participant (the central securities depository participant granted direct access, like a bank or a central counter party) and the central system.

### src-000363-camt.065.001.01-p9-c001

src-000363, file page 9; 3 camt.065.001.01 LimitUtilisationJournalReportV01.

> The LimitUtilisationJournalReport message is exchanged between the central system and a central securities depository or a directly connected system party (the central securities depository participant granted direct access, like a bank or central counter party) and is used to return information about the limit.

## Applicable exact messages


- [camt.064.001.01](../../../domains/securities/reference/messages/camt.064.001.01/roles.md)
- [camt.065.001.01](../../../domains/securities/reference/messages/camt.065.001.01/roles.md)

## Identity and unresolved scope

Source labels: central system. No identifier scheme or institution equivalence is inferred. The quoted clauses define the available actions; no absent duty, flow or business condition is invented.
