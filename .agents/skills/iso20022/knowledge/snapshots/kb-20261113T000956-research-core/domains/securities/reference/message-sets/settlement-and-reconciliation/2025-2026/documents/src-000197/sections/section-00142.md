---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "7.4 Message Building Blocks", "7.4.6 FinancialInstrument <FinInstrm>", "7.4.6.3 SubBalance <SubBal>", "7.4.6.3.3 IntraPositionMovement <IntraPosMvmnt>", "7.4.6.3.3.2 SettledQuantity <SttldQty>"]
file_pages: [194]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.016.001.10"]
---

# 7.4.6.3.3.2 SettledQuantity <SttldQty>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 194 to 194.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 194

```text
7.4.6.3.3.2  SettledQuantity <SttldQty>
Presence: [1..1]
Definition: Quantity of financial instrument effectively settled.
Impacted by: C12 "DigitalTokenUnitUsageRule"
SettledQuantity <SttldQty> contains one of the following elements (see
"FinancialInstrumentQuantity33Choice" on page 1726 for details)
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
7.4.6.3.3.3  PreviouslySettledQuantity <PrevslySttldQty>
Presence: [0..1]
Definition: Quantity of financial instrument previously settled.
Impacted by: C12 "DigitalTokenUnitUsageRule"
PreviouslySettledQuantity <PrevslySttldQty> contains one of the following elements (see
"FinancialInstrumentQuantity33Choice" on page 1726 for details)
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
7.4.6.3.3.4  RemainingToBeSettledQuantity <RmngToBeSttldQty>
Presence: [0..1]
Definition: Quantity of financial instrument remaining to be settled.
Impacted by: C12 "DigitalTokenUnitUsageRule"
Approved by the Securities SEG on 27 January 2026 semt.016.001.10
IntraPositionMovementPostingReportV10
Settlement And Reconciliation - Maintenance 2025 - 2026 194 March 2026
```

