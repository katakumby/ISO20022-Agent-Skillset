---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["28 sese.034.001.11 SecuritiesFinancingStatusAdviceV11", "28.4 Message Building Blocks", "28.4.6 RepoCallRequestStatus <RepoCallReqSts>", "28.4.7.32 StockLoanMargin <StockLnMrgn>"]
file_pages: [987]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.034.001.11"]
---

# 28.4.7.32 StockLoanMargin <StockLnMrgn>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 987 to 987.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 987

```text
Constraints
• SignRule
When Sign is present, rate must not be zero.
28.4.7.32  StockLoanMargin <StockLnMrgn>
Presence: [0..1]
Definition: Percentage mark-up on a loan consideration used to reflect the lender's risk.
Impacted by: C35 "SignRule"
StockLoanMargin <StockLnMrgn> contains the following elements (see "Rate2" on page 1748 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Sign <Sgn> [0..1] Indicator 1748
   Rate <Rate> [1..1] Rate 1749
Constraints
• SignRule
When Sign is present, rate must not be zero.
28.4.7.33  SecuritiesHaircut <SctiesHrcut>
Presence: [0..1]
Definition: Haircut or valuation factor on the security expressed as a percentage.
Impacted by: C35 "SignRule"
SecuritiesHaircut <SctiesHrcut> contains the following elements (see "Rate2" on page 1748 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Sign <Sgn> [0..1] Indicator 1748
   Rate <Rate> [1..1] Rate 1749
Constraints
• SignRule
When Sign is present, rate must not be zero.
28.4.7.34  PricingRate <PricgRate>
Presence: [0..1]
Definition: Interest rate to be paid on the transaction amount, as agreed between the counterparties.
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 987 March 2026
```

