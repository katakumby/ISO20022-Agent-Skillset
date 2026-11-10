---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.20 Price", "35.1.20.9 Price7", "35.1.20.9.1 Type <Tp>"]
file_pages: [1716]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.20.9.1 Type <Tp>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1716 to 1716.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1716

```text
35.1.20.9.1  Type <Tp>
Presence: [1..1]
Definition: Specification of the price type.
Type <Tp> contains one of the following elements (see "YieldedOrValueType1Choice" on page 1591
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Yielded <Yldd> [1..1] Indicator 1591
Or}   ValueType <ValTp> [1..1] CodeSet 1591
35.1.20.9.2  Value <Val>
Presence: [1..1]
Definition: Value of the price, for example, as a currency and value.
Value <Val> contains one of the following elements (see "PriceRateOrAmount3Choice" on page 1710
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1710
Or}   Amount <Amt> [1..1] Amount C2 1710
35.1.20.10  PriceInformation29
Definition: Amount of money for which goods or services are offered, sold, or bought.
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
35.1.20.10.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of price and information about the price.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1716 March 2026
```

