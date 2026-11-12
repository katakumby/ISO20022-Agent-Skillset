---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.11 SubBalanceQuantity1Choice", "66.1.5.11.2 QuantityAsDSS <QtyAsDSS>"]
file_pages: [4399]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.11.2 QuantityAsDSS <QtyAsDSS>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4399 to 4399.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4399

```text
Quantity <Qty> contains one of the following elements (see "FinancialInstrumentQuantityChoice" on
page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 5142
Or   FaceAmount <FaceAmt> [1..1] Amount 5142
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 5142
66.1.5.11.2  QuantityAsDSS <QtyAsDSS>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance.
QuantityAsDSS <QtyAsDSS> contains the following elements (see "GenericIdentification6" on
page 4553 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Issuer <Issr> [1..1] Text 4553
   Information <Inf> [1..1] Text 4553
   Balance <Bal> [1..1] Quantity 4553
66.1.5.11.3  QuantityAndAvailability <QtyAndAvlbty>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance and whether the balance is available.
QuantityAndAvailability <QtyAndAvlbty> contains the following QuantityAndAvailability elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity <Qty> [1..1] ± 4399
   AvailabilityIndicator <AvlbtyInd> [1..1] Indicator 4400
66.1.5.11.3.1  Quantity <Qty>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance.
Quantity <Qty> contains one of the following elements (see "FinancialInstrumentQuantityChoice" on
page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 5142
Or   FaceAmount <FaceAmt> [1..1] Amount 5142
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 5142
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4399 May 2026
```

