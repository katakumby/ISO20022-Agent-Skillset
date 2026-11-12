---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "shared"
domains: ["securities"]
participant_id: "participant-functionality-src-000233-sender"
title: "sender — TARGET2-Securities Functionality"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
source_labels: ["sender"]
aliases: []
role_type: "functional participant explicitly named in message Functionality"
message_sets: ["t2s"]
message_ids: ["head.002.001.01", "semt.040.001.01"]
message_families: ["head.002", "semt.040"]
source_locations: [{"source_id": "src-000233", "heading": "26 head.002.001.01 BusinessFileHeaderV01", "file_pages": [614], "evidence_id": "src-000233-head.002.001.01-p614-c002"}, {"source_id": "src-000233", "heading": "80 semt.040.001.01 SecuritiesAccountPositionResponseV01", "file_pages": [2748], "evidence_id": "src-000233-semt.040.001.01-p2748-c004"}]
identifier_schemes: []
limitations: ["Meaning is scoped to these exact quoted message contexts; a generic role label does not identify one institution across messages.", "A separate formal business-role definition or identifier scheme is not supplied in these Functionality clauses.", "Mention in an example, routing clause or alternative is not automatically an independent sender or receiver."]
---

# sender — TARGET2-Securities Functionality

[src-000233](../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md)

## Definition and business context

Generic sender function explicitly named in this publication’s quoted message Functionality. Its precise capacity and counterparties are retained per clause rather than being inferred from the generic label.

This record collects the literal role within this publication. It does not equate that function with a particular institution or with a differently scoped role having the same name.

## Responsibilities, actions and relationships

The complete evidence below preserves who acts, the counterparties, alternatives and conditions. Only explicit clauses establish directions; quoted examples remain examples.

### src-000233-head.002.001.01-p614-c002

src-000233, file page 614; 26 head.002.001.01 BusinessFileHeaderV01.

> Provides information about the sender of the file.

### src-000233-semt.040.001.01-p2748-c004

src-000233, file page 2748; 80 semt.040.001.01 SecuritiesAccountPositionResponseV01.

> The free position Unless otherwise specified by the sender in the Securities Balance Query, T2S will only return non-zero securities positions in the accounts.

## Applicable exact messages


- [head.002.001.01](../messages/head.002.001.01/roles.md)
- [semt.040.001.01](../../../domains/securities/reference/messages/semt.040.001.01/roles.md)

## Identity and unresolved scope

Source labels: sender. No identifier scheme or institution equivalence is inferred. The quoted clauses define the available actions; no absent duty, flow or business condition is invented.
