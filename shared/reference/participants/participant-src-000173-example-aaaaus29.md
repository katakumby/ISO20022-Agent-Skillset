---
template: false
document_kind: "participant"
review_status: "reviewed"
manual_curated: true
domain: "shared"
domains: ["payments"]
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
participant_id: "participant-src-000173-example-aaaaus29"
title: "AAAAUS29"
source_labels: ["AAAAUS29"]
role_type: "Named participant in supplied business example"
aliases: []
source_locations: [{"source_id": "src-000173", "locator": "P579–581; P765; T26; T28"}]
identifier_schemes: ["BICFI: AAAAUS29"]
example_paths: ["domains/payments/reference/message-sets/payments-initiation/2025-2026/examples/example-03-pain.002.001.15.md", "domains/payments/reference/message-sets/payments-initiation/2025-2026/examples/example-05-pain.008.001.12.md"]
message_ids: ["pain.002.001.15", "pain.008.001.12"]
limitations: ["Identity is scoped to supplied examples. No real-world institution identity, present-day service or source-independent role equivalence is asserted."]
review_evidence: {"date": "2026-11-09", "scope": "Source scenario, table and original XML example inspected."}
---

# AAAAUS29

[src-000173](../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx)

## Example context and responsibilities

Services Virgay and receives direct-debit initiation; receives correspondent rejection and informs Virgay before crediting its account in the rejection example. (P579–581; P765; T26; T28)

## Functional roles in these examples

- [creditor agent](participant-src-000173-creditor-agent.md)
- [account servicer](participant-src-000173-account-servicer.md)

These roles apply to the cited example relationships, not permanently to the named institution/person.

## Identifiers as supplied

- BICFI: AAAAUS29

## Supplied examples

- [Example 3](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/examples/example-03-pain.002.001.15.md)
- [Example 5](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/examples/example-05-pain.008.001.12.md)
