---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.15 AggregateBalancePerSafekeepingPlace44", "7.1.5.15.6 NotAvailableBalance <NotAvlblBal>"]
file_pages: [310]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.15.6 NotAvailableBalance <NotAvlblBal>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 310 to 310.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 310

```text
7.1.5.15.6  NotAvailableBalance <NotAvlblBal>
Presence: [0..1]
Definition: Total quantity of financial instruments of the balance that is not available.
NotAvailableBalance <NotAvlblBal> contains one of the following elements (see
"BalanceQuantity8Choice" on page 387 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 387
Or}   Proprietary <Prtry> [1..1] ± 388
7.1.5.15.7  PriceDetails <PricDtls>
Presence: [0..*]
Definition: Price of the financial instrument in one or more currencies.
Impacted by: C41 "ValueRule"
PriceDetails <PricDtls> contains the following elements (see "PriceInformation20" on page 447 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 447
   Value <Val> [1..1] ± 447
   ValueType <ValTp> [1..1] ± 448
   SourceOfPrice <SrcOfPric> [0..1] ± 448
   QuotationDate <QtnDt> [0..1] ± 448
Constraints
• ValueRule
If TypeOfPriceCode is not MRKT, then Value may not be expressed with UnknownIndicator.
7.1.5.15.8  ForeignExchangeDetails <FXDtls>
Presence: [0..*]
Definition: Information needed to process a currency exchange or conversion.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 310 March 2026
```

