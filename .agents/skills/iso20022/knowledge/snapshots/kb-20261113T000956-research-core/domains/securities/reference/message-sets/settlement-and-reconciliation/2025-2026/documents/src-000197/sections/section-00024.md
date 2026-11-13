---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 semt.002.001.12 SecuritiesBalanceCustodyReportV12", "2.4 Message Building Blocks", "2.4.8 BalanceForAccount <BalForAcct>", "2.4.8.18 BalanceAtSafekeepingPlace <BalAtSfkpgPlc>", "2.4.8.18.6 NotAvailableBalance <NotAvlblBal>"]
file_pages: [47]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.12"]
---

# 2.4.8.18.6 NotAvailableBalance <NotAvlblBal>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 47 to 47.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 47

```text
2.4.8.18.6  NotAvailableBalance <NotAvlblBal>
Presence: [0..1]
Definition: Total quantity of financial instruments of the balance that is not available.
NotAvailableBalance <NotAvlblBal> contains one of the following elements (see
"BalanceQuantity14Choice" on page 1735 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C12 1735
Or}   Proprietary <Prtry> [1..1] ± 1736
2.4.8.18.7  PriceDetails <PricDtls>
Presence: [0..*]
Definition: Price of the financial instrument in one or more currencies.
Impacted by: C44 "ValueRule"
PriceDetails <PricDtls> contains the following elements (see "PriceInformation29" on page 1716 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 1716
   Value <Val> [1..1] ± 1717
   ValueType <ValTp> [1..1] ± 1717
   SourceOfPrice <SrcOfPric> [0..1] ± C35 1717
   QuotationDate <QtnDt> [0..1] ± 1718
Constraints
• ValueRule
If TypeOfPriceCode is not MRKT, then Value may not be expressed with UnknownIndicator.
2.4.8.18.8  ForeignExchangeDetails <FXDtls>
Presence: [0..*]
Definition: Information needed to process a currency exchange or conversion.
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 47 March 2026
```

