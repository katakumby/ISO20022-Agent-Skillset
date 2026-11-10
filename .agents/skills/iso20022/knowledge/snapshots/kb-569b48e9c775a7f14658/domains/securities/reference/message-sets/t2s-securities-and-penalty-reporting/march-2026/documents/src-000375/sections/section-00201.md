---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.11 SubBalanceQuantity6Choice", "7.1.5.11.2 Proprietary <Prtry>"]
file_pages: [270]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.11.2 Proprietary <Prtry>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 270 to 270.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 270

```text
7.1.5.11.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance.
Proprietary <Prtry> contains the following elements (see "GenericIdentification56" on page 353 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 354
   Issuer <Issr> [1..1] Text 354
   SchemeName <SchmeNm> [0..1] Text 354
   Balance <Bal> [1..1] Quantity 354
7.1.5.11.3  QuantityAndAvailability <QtyAndAvlbty>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance and whether the balance is available.
QuantityAndAvailability <QtyAndAvlbty> contains the following QuantityAndAvailability1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity <Qty> [1..1] ± 270
   AvailabilityIndicator <AvlbtyInd> [1..1] Indicator 270
7.1.5.11.3.1  Quantity <Qty>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance.
Quantity <Qty> contains one of the following elements (see "FinancialInstrumentQuantity1Choice" on
page 342 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 342
Or   FaceAmount <FaceAmt> [1..1] Amount 342
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 342
7.1.5.11.3.2  AvailabilityIndicator <AvlbtyInd>
Presence: [1..1]
Definition: Indicates whether the quantity of securities on the sub-balance is available.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 553):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 270 March 2026
```

