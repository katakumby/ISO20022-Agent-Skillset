---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
participant_id: "participant-src-000371-account-owner"
title: "Account owner"
domain: "shared"
domains: ["securities"]
message_sets: ["t2s-securities-account-reference-data"]
source_ids: ["src-000371"]
source_editions: ["december-2019"]
source_labels: ["Account owner"]
aliases: []
role_kind: "scoped reference-data or audit role"
source_locations: [{"source_id": "src-000371", "locator": "P94; P112; P332–P333/P349–P360"}]
identifier_schemes: ["BIC in the source-authored examples; no institution-wide ownership is inferred."]
limitations: ["The role is described in narrative/examples and is not a separate actor lane in the source process diagrams. No general sender/receiver responsibility is inferred from data-field presence."]
flow_ids: ["flow-src-000371-p152-create-securities-account", "flow-src-000371-p156-query"]
message_ids: ["reda.018.001.01", "reda.019.001.01", "reda.020.001.01", "reda.021.001.01", "reda.036.001.01", "reda.037.001.01"]
---

# Account owner

The party identified as account owner in securities-account reference data; it is also a supported query criterion. In the source example its Party BIC is CSDPXXYYAAA, while its Parent BIC is CSDAXXYYAAA.

[src-000371](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`; P94; P112; P332–P333/P349–P360.

## Responsibilities and identifiers

BIC in the source-authored examples; no institution-wide ownership is inferred.

These source passages describe account identification, search or audit responsibility; they do not assign an independent message exchange to this role. The process actor diagrams intentionally show only instructing and executing/servicing roles.

## Applicable reference flows

- [Create a securities account](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p152-create-securities-account.md)
- [Query securities account data or audit trail](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p156-query.md)
