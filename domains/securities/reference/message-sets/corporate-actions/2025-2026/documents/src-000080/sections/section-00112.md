---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.23 SecuritiesQuantity <SctiesQty>", "3.4.11.23.2 MinimumQuantityToInstruct <MinQtyToInst>"]
file_pages: [168]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.23.2 MinimumQuantityToInstruct <MinQtyToInst>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 168 to 168.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 168

```text
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
3.4.11.23.2  MinimumQuantityToInstruct <MinQtyToInst>
Presence: [0..1]
Definition: Minimum quantity of financial instrument that may be instructed.
Impacted by: C26 "DigitalTokenUnitUsageRule"
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
3.4.11.23.3  MinimumMultipleQuantityToInstruct <MinMltplQtyToInst>
Presence: [0..1]
Definition: Minimum multiple quantity of financial instrument that may be instructed.
Impacted by: C27 "DigitalTokenUnitUsageRule"
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 168 February 2026
```

