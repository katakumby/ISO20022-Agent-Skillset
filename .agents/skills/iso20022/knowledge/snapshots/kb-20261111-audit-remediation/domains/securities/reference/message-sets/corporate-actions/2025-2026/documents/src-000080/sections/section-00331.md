---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.21 SecuritiesQuantity <SctiesQty>", "7.4.13.21.1 MaximumQuantityToInstruct <MaxQtyToInst>"]
file_pages: [451]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.21.1 MaximumQuantityToInstruct <MaxQtyToInst>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 451 to 451.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 451

```text
7.4.13.21.1  MaximumQuantityToInstruct <MaxQtyToInst>
Presence: [0..1]
Definition: Maximum quantity of financial instrument that may be instructed.
Impacted by: C21 "DigitalTokenUnitUsageRule"
MaximumQuantityToInstruct <MaxQtyToInst> contains one of the following elements (see
"FinancialInstrumentQuantity34Choice" on page 1096 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1096
Or   FaceAmount <FaceAmt> [1..1] Amount 1096
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1096
Or   Code <Cd> [1..1] CodeSet 1096
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1097
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
7.4.13.21.2  MinimumQuantityToInstruct <MinQtyToInst>
Presence: [0..1]
Definition: Minimum quantity of financial instrument that may be instructed.
Impacted by: C21 "DigitalTokenUnitUsageRule"
MinimumQuantityToInstruct <MinQtyToInst> contains one of the following elements (see
"FinancialInstrumentQuantity34Choice" on page 1096 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1096
Or   FaceAmount <FaceAmt> [1..1] Amount 1096
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1096
Or   Code <Cd> [1..1] CodeSet 1096
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1097
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
7.4.13.21.3  MinimumMultipleQuantityToInstruct <MinMltplQtyToInst>
Presence: [0..1]
Definition: Minimum multiple quantity of financial instrument that may be instructed.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 451 February 2026
```

