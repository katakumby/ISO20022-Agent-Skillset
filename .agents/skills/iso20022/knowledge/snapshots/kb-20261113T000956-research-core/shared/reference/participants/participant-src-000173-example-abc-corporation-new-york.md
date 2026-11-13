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
participant_id: "participant-src-000173-example-abc-corporation-new-york"
title: "ABC Corporation, New York"
source_labels: ["ABC Corporation, New York"]
role_type: "Named participant in supplied business example"
aliases: []
source_locations: [{"source_id": "src-000173", "locator": "P322–331; P544–546; T24; T25"}]
identifier_schemes: ["Other account identification: 00125574999"]
example_paths: ["domains/payments/reference/message-sets/payments-initiation/2025-2026/examples/example-01-pain.001.001.13.md", "domains/payments/reference/message-sets/payments-initiation/2025-2026/examples/example-02-pain.002.001.15.md"]
message_ids: ["pain.001.001.13", "pain.002.001.15"]
limitations: ["Identity is scoped to supplied examples. No real-world institution identity, present-day service or source-independent role equivalence is asserted."]
review_evidence: {"date": "2026-11-09", "scope": "Source scenario, table and original XML example inspected."}
---

# ABC Corporation, New York

[src-000173](../../../evidence/omitted/baf7abf3460122a33db6052d.md)

## Example context and responsibilities

Holds account 00125574999 and instructs BBBB Bank New York to pay three invoices; receives technical/customer-profile acceptance status. (P322–331; P544–546; T24; T25)

## Functional roles in these examples

- [debtor](participant-src-000173-debtor.md)
- [initiating party](participant-src-000173-initiating-party.md)
- [account owner](participant-src-000173-account-owner.md)

These roles apply to the cited example relationships, not permanently to the named institution/person.

## Identifiers as supplied

- Other account identification: 00125574999

## Supplied examples

- [Example 1](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/examples/example-01-pain.001.001.13.md)
- [Example 2](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/examples/example-02-pain.002.001.15.md)
