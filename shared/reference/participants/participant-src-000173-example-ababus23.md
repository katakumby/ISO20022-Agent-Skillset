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
participant_id: "participant-src-000173-example-ababus23"
title: "ABABUS23"
source_labels: ["ABABUS23"]
role_type: "Named participant in supplied business example"
aliases: []
source_locations: [{"source_id": "src-000173", "locator": "P579; T26"}]
identifier_schemes: ["AnyBIC: ABABUS23"]
example_paths: ["domains/payments/reference/message-sets/payments-initiation/2025-2026/examples/example-03-pain.002.001.15.md"]
message_ids: ["pain.002.001.15"]
limitations: ["Identity is scoped to supplied examples. No real-world institution identity, present-day service or source-independent role equivalence is asserted."]
review_evidence: {"date": "2026-11-09", "scope": "Source scenario, table and original XML example inspected."}
---

# ABABUS23

[src-000173](../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx)

## Example context and responsibilities

Correspondent of AAAAUS29 sends FIToFIPaymentStatusReport rejecting previously sent interbank direct debit. T26 status-reason originator contains this AnyBIC. (P579; T26)

## Functional roles in these examples



The source establishes correspondent status; it does not explicitly assign one of the listed functional role names to this party.

## Identifiers as supplied

- AnyBIC: ABABUS23

## Supplied examples

- [Example 3](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/examples/example-03-pain.002.001.15.md)
