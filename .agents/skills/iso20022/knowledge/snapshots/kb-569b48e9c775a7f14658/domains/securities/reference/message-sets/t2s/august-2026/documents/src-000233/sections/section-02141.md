---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.17 AggregateBalancePerSafekeepingPlace44", "82.1.5.17.6 NotAvailableBalance <NotAvlblBal>"]
file_pages: [2902]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.17.6 NotAvailableBalance <NotAvlblBal>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2902 to 2902.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2902

```text
82.1.5.17.6  NotAvailableBalance <NotAvlblBal>
Presence: [0..1]
Definition: Total quantity of financial instruments of the balance that is not available.
NotAvailableBalance <NotAvlblBal> contains one of the following elements (see
"BalanceQuantity8Choice" on page 3027 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 3027
Or}   Proprietary <Prtry> [1..1] ± 3027
82.1.5.17.7  PriceDetails <PricDtls>
Presence: [0..*]
Definition: Price of the financial instrument in one or more currencies.
Impacted by: C41 "ValueRule"
PriceDetails <PricDtls> contains the following elements (see "PriceInformation20" on page 3104 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 3104
   Value <Val> [1..1] ± 3105
   ValueType <ValTp> [1..1] ± 3105
   SourceOfPrice <SrcOfPric> [0..1] ± 3105
   QuotationDate <QtnDt> [0..1] ± 3105
Constraints
• ValueRule
If TypeOfPriceCode is not MRKT, then Value may not be expressed with UnknownIndicator.
82.1.5.17.8  ForeignExchangeDetails <FXDtls>
Presence: [0..*]
Definition: Information needed to process a currency exchange or conversion.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2902 August 2026
```

