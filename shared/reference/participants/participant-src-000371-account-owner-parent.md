---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
participant_id: "participant-src-000371-account-owner-parent"
title: "Account owner Parent"
domain: "shared"
domains: ["securities"]
message_sets: ["t2s-securities-account-reference-data"]
source_ids: ["src-000371"]
source_editions: ["december-2019"]
source_labels: ["Account owner Parent"]
aliases: []
role_kind: "scoped reference-data or audit role"
source_locations: [{"source_id": "src-000371", "locator": "P332/P355–P359; P531/P562–P566"}]
identifier_schemes: ["BIC in the source example. XML containment is not used to infer business ownership."]
limitations: ["The role is described in narrative/examples and is not a separate actor lane in the source process diagrams. No general sender/receiver responsibility is inferred from data-field presence."]
flow_ids: ["flow-src-000371-p152-create-securities-account", "flow-src-000371-p156-query"]
message_ids: ["reda.018.001.01", "reda.019.001.01", "reda.020.001.01", "reda.021.001.01", "reda.036.001.01", "reda.037.001.01"]
---

# Account owner Parent

The source example calls CSDAXXYYAAA the Account owner Parent BIC and places it in AcctOwnr/RspnsblPtyId. The owner itself has separate Party BIC CSDPXXYYAAA.

[src-000371](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`; P332/P355–P359; P531/P562–P566.

## Responsibilities and identifiers

BIC in the source example. XML containment is not used to infer business ownership.

These source passages describe account identification, search or audit responsibility; they do not assign an independent message exchange to this role. The process actor diagrams intentionally show only instructing and executing/servicing roles.

## Applicable reference flows

- [Create a securities account](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p152-create-securities-account.md)
- [Query securities account data or audit trail](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p156-query.md)
