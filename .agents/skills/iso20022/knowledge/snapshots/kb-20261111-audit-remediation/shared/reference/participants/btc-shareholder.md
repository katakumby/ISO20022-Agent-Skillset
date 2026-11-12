---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "participant"
participant_id: "btc-shareholder"
source_labels: ["shareholders"]
aliases: []
source_locations: ["T40 row 6; Corporate Action & Custody Sub-Families codes", "T40 row 12; Corporate Action & Custody Sub-Families codes", "T40 row 13; Corporate Action & Custody Sub-Families codes", "T40 row 25; Corporate Action & Custody Sub-Families codes", "T40 row 28; Corporate Action & Custody Sub-Families codes", "T40 row 29; Corporate Action & Custody Sub-Families codes"]
domains: ["securities"]
message_sets: ["external-code-sets"]
flows: []
relationships: ["btc-securities-issuer", "btc-tender-offeror"]
identifier_schemes: []
limitations: ["The publication describes this scoped role through transaction-code definitions; it does not provide a formal participant model or map it to exact message definitions.", "No equivalence with same-named MDR roles, institutions or product-specific roles is asserted."]
---

# shareholders — Bank Transaction Code context

## Definition, role and business context

Receives cash dividends proportional to equity holdings; for Dividend Option can choose shares or cash; may receive capital gains, equity premium reserve payments or an offer to tender/exchange equities.

This is a contextual business-role description from the supplied code publication. Its functional actions are limited to those in the cited evidence; an institution may occupy different roles in different relationships. The document does not formally classify business-role versus functional-participant types.

## Responsibilities and source evidence

- [T40 row 6](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0040.md): Capital Gains Distribution Distribution of profits resulting from the sale of company assets eg Shareholders of Mutual Funds, Unit Trusts, or Sicavs are recipients of capital gains distributions which are often reinvested in additional shares of the fund.
- [T40 row 12](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0040.md): Cash Dividend Distribution of cash to shareholders, in proportion to their equity holding. Ordinary dividends are recurring and regular.  Shareholder must take cash and may be offered a choice of currency.
- [T40 row 13](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0040.md): Dividend Option Distribution of a dividend to shareholders with a choice of benefit to receive. Shareholders may choose to receive shares or cash. To be distinguished from DRIP as the company creates new share capital in exchange for the dividend rather than investing the dividend in the market.
- [T40 row 25](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0040.md): Priority Issue Form of open or public offer where, due to a limited amount of securities available, priority is given to existing shareholders.
- [T40 row 28](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0040.md): Equity Premium Reserve Shareholders receive an amount in cash issued from the equity premium reserve. This event is similar to a dividend but has different tax implications.
- [T40 row 29](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0040.md): Tender Cash movement related to an offer made to shareholders, normally by a third party, requesting them to sell (tender) or exchange their equities.

## Relationships and reuse

- [issuer](btc-securities-issuer.md).
- [third party](btc-tender-offeror.md).

## Flows, messages and identifiers

The cited code definitions do not supply a complete message-exchange flow for this scoped participant.

No exact message identifier, role identifier scheme or source-supported alias is specified in the cited evidence. The role is usable in the External code sets collection; applicability to a particular message must be checked in that exact message reference.

## Review boundary

Definition, actions and source row/paragraph locators checked against the complete supplied Word rendering on 2026-11-09. This reviews the scoped description; it does not fill unavailable business context or resolve publication issues 2 and 33.
