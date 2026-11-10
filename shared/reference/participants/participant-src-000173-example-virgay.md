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
participant_id: "participant-src-000173-example-virgay"
title: "Virgay"
source_labels: ["Virgay"]
role_type: "Named participant in supplied business example"
aliases: []
source_locations: [{"source_id": "src-000173", "locator": "P579–581; P765–771; T26; T28"}]
identifier_schemes: ["Other account identification: 789123"]
example_paths: ["domains/payments/reference/message-sets/payments-initiation/2025-2026/examples/example-03-pain.002.001.15.md", "domains/payments/reference/message-sets/payments-initiation/2025-2026/examples/example-05-pain.008.001.12.md"]
message_ids: ["pain.002.001.15", "pain.008.001.12"]
limitations: ["Identity is scoped to supplied examples. No real-world institution identity, present-day service or source-independent role equivalence is asserted."]
review_evidence: {"date": "2026-11-09", "scope": "Source scenario, table and original XML example inspected."}
---

# Virgay

[src-000173](../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx)

## Example context and responsibilities

Insurance company sends two direct-debit collections under VERPA-1; in a separate rejection example receives status before original creditor account was credited. Contactdetails names J. Thompson. (P579–581; P765–771; T26; T28)

## Functional roles in these examples

- [creditor](participant-src-000173-creditor.md)
- [initiating party](participant-src-000173-initiating-party.md)
- [account owner](participant-src-000173-account-owner.md)

These roles apply to the cited example relationships, not permanently to the named institution/person.

## Identifiers as supplied

- Other account identification: 789123

## Supplied examples

- [Example 3](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/examples/example-03-pain.002.001.15.md)
- [Example 5](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/examples/example-05-pain.008.001.12.md)
