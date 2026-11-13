---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "participant"
participant_id: "btc-securities-issuer"
source_labels: ["issuer"]
aliases: []
source_locations: ["T40 row 3; Corporate Action & Custody Sub-Families codes", "T40 row 4; Corporate Action & Custody Sub-Families codes", "T40 row 10; Corporate Action & Custody Sub-Families codes", "T40 row 19; Corporate Action & Custody Sub-Families codes", "T40 row 20; Corporate Action & Custody Sub-Families codes", "T40 row 21; Corporate Action & Custody Sub-Families codes", "T40 row 26; Corporate Action & Custody Sub-Families codes"]
domains: ["securities"]
message_sets: ["external-code-sets"]
flows: []
relationships: ["btc-security-holder", "btc-shareholder"]
identifier_schemes: []
limitations: ["The publication describes this scoped role through transaction-code definitions; it does not provide a formal participant model or map it to exact message definitions.", "No equivalence with same-named MDR roles, institutions or product-specific roles is asserted."]
---

# issuer — Bank Transaction Code context

## Definition, role and business context

Provides bonus assets, reinvests dividends, redeems issues, initiates mergers and may make odd-lot offers in the respective source corporate-action definitions.

This is a contextual business-role description from the supplied code publication. Its functional actions are limited to those in the cited evidence; an institution may occupy different roles in different relationships. The document does not formally classify business-role versus functional-participant types.

## Responsibilities and source evidence

- [T40 row 3](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0040.md): Repurchase offer/Issuer Bid/Reverse Rights. Offer to existing shareholders by the issuing company to repurchase equity or other securities convertible into equity. The objective of the offer is to reduce the number of outstanding equities.
- [T40 row 4](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0040.md): Bonus Issue/Capitalisation Issue Bonus, scrip or capitalisation issue. Security holders receive additional assets free of payment from the issuer, in proportion to their holding.
- [T40 row 10](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0040.md): Dividend Reinvestment Dividend payment where holders can keep cash or have the cash reinvested in the market by the issuer into additional shares in the issuing company. To be distinguished from DVOP as the company invests the dividend in the market rather than creating new share capital in exchange for the dividend.
- [T40 row 19](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0040.md): Full Call / Early Redemption Redemption of an entire issue outstanding of bonds/preferred equity by the issuer before final maturity.
- [T40 row 20](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0040.md): Merger Exchange of outstanding securities, initiated by the issuer which may include options, as the result of two or more companies combining assets ie an external, third party company. Cash payments may accompany share exchange.
- [T40 row 21](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0040.md): Odd Lot Sale/Purchase Sale or purchase of odd-lots to/from the issuing company, initiated either by the holder of the security or through an offer made by the issuer.
- [T40 row 26](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0040.md): Final Maturity Redemption of an entire issue outstanding of bonds/preferred equities by the issuer at final maturity.

## Relationships and reuse

- [holder](btc-security-holder.md).
- [shareholders](btc-shareholder.md).

## Flows, messages and identifiers

The cited code definitions do not supply a complete message-exchange flow for this scoped participant.

No exact message identifier, role identifier scheme or source-supported alias is specified in the cited evidence. The role is usable in the External code sets collection; applicability to a particular message must be checked in that exact message reference.

## Review boundary

Definition, actions and source row/paragraph locators checked against the complete supplied Word rendering on 2026-11-09. This reviews the scoped description; it does not fill unavailable business context or resolve publication issues 2 and 33.
