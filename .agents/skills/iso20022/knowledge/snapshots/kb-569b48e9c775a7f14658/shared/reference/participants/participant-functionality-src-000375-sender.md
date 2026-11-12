---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "shared"
domains: ["securities"]
participant_id: "participant-functionality-src-000375-sender"
title: "sender — T2S SecuritiesAndPenaltyReporting Functionality"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
source_labels: ["sender"]
aliases: []
role_type: "functional participant explicitly named in message Functionality"
message_sets: ["t2s-securities-and-penalty-reporting"]
message_ids: ["semt.040.001.01"]
message_families: ["semt.040"]
source_locations: [{"source_id": "src-000375", "heading": "5 semt.040.001.01 SecuritiesAccountPositionResponseV01", "file_pages": [166], "evidence_id": "src-000375-semt.040.001.01-p166-c004"}]
identifier_schemes: []
limitations: ["Meaning is scoped to these exact quoted message contexts; a generic role label does not identify one institution across messages.", "A separate formal business-role definition or identifier scheme is not supplied in these Functionality clauses.", "Mention in an example, routing clause or alternative is not automatically an independent sender or receiver."]
---

# sender — T2S SecuritiesAndPenaltyReporting Functionality

[src-000375](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`

## Definition and business context

Generic sender function explicitly named in this publication’s quoted message Functionality. Its precise capacity and counterparties are retained per clause rather than being inferred from the generic label.

This record collects the literal role within this publication. It does not equate that function with a particular institution or with a differently scoped role having the same name.

## Responsibilities, actions and relationships

The complete evidence below preserves who acts, the counterparties, alternatives and conditions. Only explicit clauses establish directions; quoted examples remain examples.

### src-000375-semt.040.001.01-p166-c004

src-000375, file page 166; 5 semt.040.001.01 SecuritiesAccountPositionResponseV01.

> The free position Unless otherwise specified by the sender in the Securities Balance Query, T2S will only return non-zero securities positions in the accounts.

## Applicable exact messages


- [semt.040.001.01](../../../domains/securities/reference/messages/semt.040.001.01/roles.md)

## Identity and unresolved scope

Source labels: sender. No identifier scheme or institution equivalence is inferred. The quoted clauses define the available actions; no absent duty, flow or business condition is invented.
