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
participant_id: "participant-src-000173-example-bbbb-bank-new-york"
title: "BBBB Bank, New York"
source_labels: ["BBBB Bank, New York"]
role_type: "Named participant in supplied business example"
aliases: []
source_locations: [{"source_id": "src-000173", "locator": "P329–331; P544–546; T24–T25"}]
identifier_schemes: ["BICFI: BBBBUS33"]
example_paths: ["domains/payments/reference/message-sets/payments-initiation/2025-2026/examples/example-01-pain.001.001.13.md", "domains/payments/reference/message-sets/payments-initiation/2025-2026/examples/example-02-pain.002.001.15.md"]
message_ids: ["pain.001.001.13", "pain.002.001.15"]
limitations: ["Identity is scoped to supplied examples. No real-world institution identity, present-day service or source-independent role equivalence is asserted."]
review_evidence: {"date": "2026-11-09", "scope": "Source scenario, table and original XML example inspected."}
---

# BBBB Bank, New York

[src-000173](../../../evidence/omitted/baf7abf3460122a33db6052d.md)

## Example context and responsibilities

Receives ABC Corporation initiation and sends CustomerPaymentStatusReport after technical validation/customer-profile acceptance. (P329–331; P544–546; T24–T25)

## Functional roles in these examples

- [debtor agent](participant-src-000173-debtor-agent.md)
- [account servicer](participant-src-000173-account-servicer.md)

These roles apply to the cited example relationships, not permanently to the named institution/person.

## Identifiers as supplied

- BICFI: BBBBUS33

## Supplied examples

- [Example 1](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/examples/example-01-pain.001.001.13.md)
- [Example 2](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/examples/example-02-pain.002.001.15.md)
