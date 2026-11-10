---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.12 Balance9", "82.1.5.12.2 Quantity <Qty>"]
file_pages: [2861]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.12.2 Quantity <Qty>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2861 to 2861.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2861

```text
CodeName Name Definition
LONG Long Position is long, that is, the balance is
positive.
82.1.5.12.2  Quantity <Qty>
Presence: [1..1]
Definition: Total quantity of financial instruments of the balance.
Quantity <Qty> contains one of the following elements (see "SubBalanceQuantity6Choice" on
page 2861 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 2861
Or   Proprietary <Prtry> [1..1] ± 2862
Or}   QuantityAndAvailability <QtyAndAvlbty> [1..1]  2862
     Quantity <Qty> [1..1] ± 2862
     AvailabilityIndicator <AvlbtyInd> [1..1] Indicator 2862
82.1.5.13  SubBalanceQuantity6Choice
Definition: Choice between formats for the balance information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 2861
Or   Proprietary <Prtry> [1..1] ± 2862
Or}   QuantityAndAvailability <QtyAndAvlbty> [1..1]  2862
     Quantity <Qty> [1..1] ± 2862
     AvailabilityIndicator <AvlbtyInd> [1..1] Indicator 2862
82.1.5.13.1  Quantity <Qty>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance.
Quantity <Qty> contains one of the following elements (see "FinancialInstrumentQuantity1Choice" on
page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2861 August 2026
```

