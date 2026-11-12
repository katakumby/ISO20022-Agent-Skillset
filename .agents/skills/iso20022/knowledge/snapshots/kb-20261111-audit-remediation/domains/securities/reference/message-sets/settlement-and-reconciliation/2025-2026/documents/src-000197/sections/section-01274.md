---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.21 Quantity", "35.1.21.9 SubBalanceQuantity8Choice", "35.1.21.9.2 Proprietary <Prtry>"]
file_pages: [1731]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.21.9.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1731 to 1731.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1731

```text
Quantity <Qty> contains one of the following elements (see "FinancialInstrumentQuantity33Choice" on
page 1726 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1726
Or   FaceAmount <FaceAmt> [1..1] Amount 1726
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1726
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1727
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
35.1.21.9.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance.
Proprietary <Prtry> contains the following elements (see "GenericIdentification56" on page 1505 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1505
   Issuer <Issr> [1..1] Text 1505
   SchemeName <SchmeNm> [0..1] Text 1505
   Balance <Bal> [1..1] Quantity 1506
35.1.21.9.3  QuantityAndAvailability <QtyAndAvlbty>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance and whether the balance is available.
QuantityAndAvailability <QtyAndAvlbty> contains the following elements (see
"QuantityAndAvailability3" on page 1731 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity <Qty> [1..1] ± C12 1732
   AvailabilityIndicator <AvlbtyInd> [1..1] Indicator 1732
35.1.21.10  QuantityAndAvailability3
Definition: Net position of a segregated holding of a single security within the overall position held in the
securities account, for example, sub-balance per status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1731 March 2026
```

