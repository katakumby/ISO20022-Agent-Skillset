---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "participant"
participant_id: "btc-security-holder"
source_labels: ["holder"]
aliases: []
source_locations: ["T40 row 4; Corporate Action & Custody Sub-Families codes", "T40 row 5; Corporate Action & Custody Sub-Families codes", "T40 row 10; Corporate Action & Custody Sub-Families codes", "T40 row 21; Corporate Action & Custody Sub-Families codes", "T40 row 27; Corporate Action & Custody Sub-Families codes"]
domains: ["securities"]
message_sets: ["external-code-sets"]
flows: []
relationships: ["btc-securities-issuer", "btc-acquiring-party"]
identifier_schemes: []
limitations: ["The publication describes this scoped role through transaction-code definitions; it does not provide a formal participant model or map it to exact message definitions.", "No equivalence with same-named MDR roles, institutions or product-specific roles is asserted."]
---

# holder — Bank Transaction Code context

## Definition, role and business context

Receives bonus assets proportional to holding; can elect put redemption, retain or reinvest dividends and initiate odd-lot sale/purchase, subject to the event terms described in the source.

This is a contextual business-role description from the supplied code publication. Its functional actions are limited to those in the cited evidence; an institution may occupy different roles in different relationships. The document does not formally classify business-role versus functional-participant types.

## Responsibilities and source evidence

- [T40 row 4](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0040.md): Bonus Issue/Capitalisation Issue Bonus, scrip or capitalisation issue. Security holders receive additional assets free of payment from the issuer, in proportion to their holding.
- [T40 row 5](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0040.md): Put Redemption Early redemption of a security at the election of the holder subject to the terms and condition of the issue.
- [T40 row 10](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0040.md): Dividend Reinvestment Dividend payment where holders can keep cash or have the cash reinvested in the market by the issuer into additional shares in the issuing company. To be distinguished from DVOP as the company invests the dividend in the market rather than creating new share capital in exchange for the dividend.
- [T40 row 21](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0040.md): Odd Lot Sale/Purchase Sale or purchase of odd-lots to/from the issuing company, initiated either by the holder of the security or through an offer made by the issuer.
- [T40 row 27](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0040.md): Rights Issue/Subscription Rights/Rights Offer Distribution of a security or privilege that gives the holder an entitlement or right to take part in a future event.

## Relationships and reuse

- [issuer](btc-securities-issuer.md).
- [acquiring party](btc-acquiring-party.md).

## Flows, messages and identifiers

The cited code definitions do not supply a complete message-exchange flow for this scoped participant.

No exact message identifier, role identifier scheme or source-supported alias is specified in the cited evidence. The role is usable in the External code sets collection; applicability to a particular message must be checked in that exact message reference.

## Review boundary

Definition, actions and source row/paragraph locators checked against the complete supplied Word rendering on 2026-11-09. This reviews the scoped description; it does not fill unavailable business context or resolve publication issues 2 and 33.
