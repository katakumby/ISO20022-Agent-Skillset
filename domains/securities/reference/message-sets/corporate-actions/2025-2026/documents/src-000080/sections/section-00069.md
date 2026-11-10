---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.5 SecuritiesQuantity <SctiesQty>", "3.4.10.5.2 MinimumQuantitySought <MinQtySght>"]
file_pages: [115]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.5.2 MinimumQuantitySought <MinQtySght>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 115 to 115.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 115

```text
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
3.4.10.5.2  MinimumQuantitySought <MinQtySght>
Presence: [0..1]
Definition: Minimum quantity of securities the offeror/issuer is ready to purchase or redeem under the
terms of the event. This can be a number or the term "any and all".
Impacted by: C26 "DigitalTokenUnitUsageRule"
MinimumQuantitySought <MinQtySght> contains one of the following elements (see
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
3.4.10.5.3  NewBoardLotQuantity <NewBrdLotQty>
Presence: [0..1]
Definition: Quantity of equity that makes up the new board lot.
Impacted by: C27 "DigitalTokenUnitUsageRule"
NewBoardLotQuantity <NewBrdLotQty> contains one of the following elements (see
"FinancialInstrumentQuantity35Choice" on page 1092 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1093
Or   FaceAmount <FaceAmt> [1..1] Amount 1093
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1093
Or   Code <Cd> [1..1] CodeSet 1093
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1093
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 115 February 2026
```

