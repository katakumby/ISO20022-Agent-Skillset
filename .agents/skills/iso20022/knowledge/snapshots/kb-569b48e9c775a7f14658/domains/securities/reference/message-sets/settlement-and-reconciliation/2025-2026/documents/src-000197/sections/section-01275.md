---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.21 Quantity", "35.1.21.10 QuantityAndAvailability3", "35.1.21.10.1 Quantity <Qty>"]
file_pages: [1732]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.21.10.1 Quantity <Qty>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1732 to 1732.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1732

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity <Qty> [1..1] ± C12 1732
   AvailabilityIndicator <AvlbtyInd> [1..1] Indicator 1732
35.1.21.10.1  Quantity <Qty>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance.
Impacted by: C12 "DigitalTokenUnitUsageRule"
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
35.1.21.10.2  AvailabilityIndicator <AvlbtyInd>
Presence: [1..1]
Definition: Indicates whether the quantity of securities on the sub-balance is available.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.21.11  QuantityBreakdown60
Definition: Details of breakdown of a quantity.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [1..1] ± 1732
   LotQuantity <LotQty> [0..1] ± C12 1733
35.1.21.11.1  LotNumber <LotNb>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1732 March 2026
```

