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
participant_id: "participant-src-000173-example-ghi-semiconductors"
title: "GHI Semiconductors, Brussels"
source_labels: ["GHI Semiconductors, Brussels"]
role_type: "Named participant in supplied business example"
aliases: []
source_locations: [{"source_id": "src-000173", "locator": "P326; T24"}]
identifier_schemes: ["IBAN: BE30001216371411"]
example_paths: ["domains/payments/reference/message-sets/payments-initiation/2025-2026/examples/example-01-pain.001.001.13.md"]
message_ids: ["pain.001.001.13"]
limitations: ["Identity is scoped to supplied examples. No real-world institution identity, present-day service or source-independent role equivalence is asserted."]
review_evidence: {"date": "2026-11-09", "scope": "Source scenario, table and original XML example inspected."}
---

# GHI Semiconductors, Brussels

[src-000173](../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx)

## Example context and responsibilities

Creditor for EUR500000 invoice ABC-13679, bears transaction charges; accounts-receivable department is to be advised after credit. (P326; T24)

## Functional roles in these examples

- [creditor](participant-src-000173-creditor.md)
- [account owner](participant-src-000173-account-owner.md)

These roles apply to the cited example relationships, not permanently to the named institution/person.

## Identifiers as supplied

- IBAN: BE30001216371411

## Supplied examples

- [Example 1](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/examples/example-01-pain.001.001.13.md)
