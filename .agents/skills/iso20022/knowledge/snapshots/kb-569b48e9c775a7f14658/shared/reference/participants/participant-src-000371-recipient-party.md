---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
participant_id: "participant-src-000371-recipient-party"
title: "Recipient Party"
domain: "shared"
domains: ["securities"]
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
source_labels: ["Recipient Party"]
aliases: []
role_kind: "functional receiving role"
source_locations: [{"source_id": "src-000371", "table_id": "T12", "row": 2, "column": 2, "rendered_file_page": 15}]
limitations: ["No general equivalence with Instructing Party or particular institution inferred.", "No identifier scheme is specified for this receiving role by T12."]
flow_ids: ["flow-src-000371-p157-generate-statement"]
message_ids: ["reda.035.001.01"]
---

# Recipient Party

T12 says this participant receives the automatically produced Securities Account Activity Advice. A standing instruction must exist at the Executing/Servicing Party. The picture labels the receiving actor Instructing Party; these source scopes are retained separately.

[src-000371](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`; [T12](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000371/tables/tbl-0012.md)

<!-- SECACCOUNT-FLOWS -->
## Flows and responsibilities

- [Receive unsolicited securities account activity](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p157-generate-statement.md)
