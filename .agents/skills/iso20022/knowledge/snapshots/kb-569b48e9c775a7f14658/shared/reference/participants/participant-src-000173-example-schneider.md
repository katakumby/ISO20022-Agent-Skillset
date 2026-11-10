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
participant_id: "participant-src-000173-example-schneider"
title: "Schneider"
source_labels: ["Schneider"]
role_type: "Named participant in supplied business example"
aliases: []
source_locations: [{"source_id": "src-000173", "locator": "P666; T27"}]
identifier_schemes: ["IBAN: DE89370400440332014000"]
example_paths: ["domains/payments/reference/message-sets/payments-initiation/2025-2026/examples/example-04-pain.007.001.13.md"]
message_ids: ["pain.007.001.13"]
limitations: ["Identity is scoped to supplied examples. No real-world institution identity, present-day service or source-independent role equivalence is asserted."]
review_evidence: {"date": "2026-11-09", "scope": "Source scenario, table and original XML example inspected."}
---

# Schneider

[src-000173](../../../evidence/omitted/baf7abf3460122a33db6052d.md)

## Example context and responsibilities

Debtor in Ritcom duplicate-direct-debit reversal example; original/reversed amount EUR286 and account data appear in T27. (P666; T27)

## Functional roles in these examples

- [debtor](participant-src-000173-debtor.md)
- [account owner](participant-src-000173-account-owner.md)

These roles apply to the cited example relationships, not permanently to the named institution/person.

## Identifiers as supplied

- IBAN: DE89370400440332014000

## Supplied examples

- [Example 4](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/examples/example-04-pain.007.001.13.md)
