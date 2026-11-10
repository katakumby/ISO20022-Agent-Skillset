---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
participant_id: "participant-src-000368-recipient-party"
title: "Recipient Party"
domain: "shared"
domains: ["securities"]
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_sets: ["t2s-party-reference-data"]
source_labels: ["Recipient Party"]
aliases: []
role_kind: "functional receiving role in the statement process"
source_locations: [{"source_id": "src-000368", "table_id": "T12", "row": 2, "column": 2, "heading_path": ["BusinessProcess Description"], "xml_path": "/w:document/w:body/w:tbl[12]"}]
limitations: ["The statement table uses Recipient Party while diagrams/narrative say Instructing Party. They are retained separately; no general role equivalence is inferred.", "No identifier scheme for this receiving role is specified in the cited process table."]
flow_ids: ["flow-src-000368-p128-statement"]
message_ids: ["reda.041.001.02"]
---

# Recipient Party

T12 defines the recipient as receiving a Party Activity Advice statement automatically produced by the Executing/Servicing Party. A standing instruction is required.

[src-000368](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`; [T12 rows2–6](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/documents/src-000368/tables/tbl-0012.md)

<!-- PARTY-FLOWS -->
## Curated flows and responsibilities

- [Receive an unsolicited party activity statement](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p128-statement.md)
