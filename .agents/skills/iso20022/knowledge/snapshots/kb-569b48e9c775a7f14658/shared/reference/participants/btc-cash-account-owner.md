---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "participant"
participant_id: "btc-cash-account-owner"
source_labels: ["account owner"]
aliases: []
source_locations: ["P92 and P101; §3.1.1; rendered file/printed page 5", "T5 row 3; Payments Families definition", "T5 row 4; Payments Families definition", "T5 row 7; Payments Families definition", "T5 row 8; Payments Families definition"]
domains: ["payments"]
message_sets: ["external-code-sets"]
flows: ["btc-cash-reporting-and-reconciliation", "btc-standing-order-processing"]
relationships: ["btc-cash-account-servicer", "btc-debtor", "btc-creditor"]
identifier_schemes: []
limitations: ["The publication describes this scoped role through transaction-code definitions; it does not provide a formal participant model or map it to exact message definitions.", "No equivalence with same-named MDR roles, institutions or product-specific roles is asserted."]
---

# account owner — Bank Transaction Code context

## Definition, role and business context

Uses reported bank transaction information for cash management and reconciliation. Receives credit-transfer transactions, sends payable credit-transfer instructions, receives debit instructions and sends collection instructions in the respective families.

This is a contextual business-role description from the supplied code publication. Its functional actions are limited to those in the cited evidence; an institution may occupy different roles in different relationships. The document does not formally classify business-role versus functional-participant types.

## Responsibilities and source evidence

[src-000003](../../../evidence/omitted/1dcbe16191b6c8898a146b17.md), P92 and P101, §3.1.1, rendered page 5: bank-to-customer cash reporting supports the servicer reporting and the owner cash-management/reconciliation activities, including reconciliation to a sub-ledger or routing to an adequate customer processing system.

- [T5 row 3](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0005.md): Received Credit Transfers  Receivable Credit Transfers are instructions to receive an amount of money from a debtor by the account owner. The receivable credit transfers are related to transactions received by the account owner.
- [T5 row 4](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0005.md): Issued Credit Transfers Payable Credit Transfers are instructions to transfer an amount of money by the account owner to a creditor. The payable credit transfers are related to instructions sent by the account owner.
- [T5 row 7](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0005.md): Received Direct Debits  The Received Direct Debit transactions are related to instructions received by the account owner to debit the account.
- [T5 row 8](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0005.md): Issued Direct Debits The Issued Direct Debit transactions are related to instructions sent by the account owner to collect an amount of money that is due to the account owner.

## Relationships and reuse

- [account servicer](btc-cash-account-servicer.md).
- [debtor](btc-debtor.md).
- [creditor](btc-creditor.md).

## Flows, messages and identifiers

- [btc-cash-reporting-and-reconciliation](../code-sets/bank-transaction-codes/november-2025-v8.0/flows/btc-cash-reporting-and-reconciliation.md).
- [btc-standing-order-processing](../code-sets/bank-transaction-codes/november-2025-v8.0/flows/btc-standing-order-processing.md).

No exact message identifier, role identifier scheme or source-supported alias is specified in the cited evidence. The role is usable in the External code sets collection; applicability to a particular message must be checked in that exact message reference.

## Review boundary

Definition, actions and source row/paragraph locators checked against the complete supplied Word rendering on 2026-11-09. This reviews the scoped description; it does not fill unavailable business context or resolve publication issues 2 and 33.
