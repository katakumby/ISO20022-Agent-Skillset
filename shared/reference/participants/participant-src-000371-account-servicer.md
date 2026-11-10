---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
participant_id: "participant-src-000371-account-servicer"
title: "Account servicer"
domain: "shared"
domains: ["securities"]
message_sets: ["t2s-securities-account-reference-data"]
source_ids: ["src-000371"]
source_editions: ["december-2019"]
source_labels: ["Account servicer"]
aliases: []
role_kind: "scoped reference-data or audit role"
source_locations: [{"source_id": "src-000371", "locator": "P111; P516–P520"}]
identifier_schemes: ["BIC in the cited example. This does not establish equivalence with the functional Executing/Servicing Party."]
limitations: ["The role is described in narrative/examples and is not a separate actor lane in the source process diagrams. No general sender/receiver responsibility is inferred from data-field presence."]
flow_ids: ["flow-src-000371-p156-query"]
message_ids: ["reda.019.001.01", "reda.021.001.01", "reda.036.001.01", "reda.037.001.01"]
---

# Account servicer

The account-servicer criterion used to select securities accounts in a query. The source example selects CSDAXXYYAAA through AcctSvcr/Id/AnyBIC.

[src-000371](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`; P111; P516–P520.

## Responsibilities and identifiers

BIC in the cited example. This does not establish equivalence with the functional Executing/Servicing Party.

These source passages describe account identification, search or audit responsibility; they do not assign an independent message exchange to this role. The process actor diagrams intentionally show only instructing and executing/servicing roles.

## Applicable reference flows

- [Query securities account data or audit trail](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p156-query.md)
