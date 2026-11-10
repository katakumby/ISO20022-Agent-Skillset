---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.13 SubBalanceQuantity6Choice", "82.1.5.13.2 Proprietary <Prtry>"]
file_pages: [2862]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.13.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2862 to 2862.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2862

```text
82.1.5.13.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance.
Proprietary <Prtry> contains the following elements (see "GenericIdentification56" on page 2968 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2968
   Issuer <Issr> [1..1] Text 2968
   SchemeName <SchmeNm> [0..1] Text 2968
   Balance <Bal> [1..1] Quantity 2968
82.1.5.13.3  QuantityAndAvailability <QtyAndAvlbty>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance and whether the balance is available.
QuantityAndAvailability <QtyAndAvlbty> contains the following QuantityAndAvailability1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity <Qty> [1..1] ± 2862
   AvailabilityIndicator <AvlbtyInd> [1..1] Indicator 2862
82.1.5.13.3.1  Quantity <Qty>
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
82.1.5.13.3.2  AvailabilityIndicator <AvlbtyInd>
Presence: [1..1]
Definition: Indicates whether the quantity of securities on the sub-balance is available.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2862 August 2026
```

