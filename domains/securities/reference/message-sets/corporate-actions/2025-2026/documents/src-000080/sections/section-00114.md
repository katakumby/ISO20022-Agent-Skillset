---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.23 SecuritiesQuantity <SctiesQty>", "3.4.11.23.6 FrontEndOddLotQuantity <FrntEndOddLotQty>"]
file_pages: [170]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.23.6 FrontEndOddLotQuantity <FrntEndOddLotQty>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 170 to 170.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 170

```text
NewDenominationQuantity <NewDnmtnQty> contains one of the following elements (see
"FinancialInstrumentQuantity35Choice" on page 1092 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1093
Or   FaceAmount <FaceAmt> [1..1] Amount 1093
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1093
Or   Code <Cd> [1..1] CodeSet 1093
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1093
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
3.4.11.23.6  FrontEndOddLotQuantity <FrntEndOddLotQty>
Presence: [0..1]
Definition: Specifies that if an order is prorated holders of odd lots who tender their full position will not
have tendered position prorated but rather accepted in full.
Impacted by: C27 "DigitalTokenUnitUsageRule"
FrontEndOddLotQuantity <FrntEndOddLotQty> contains one of the following elements (see
"FinancialInstrumentQuantity35Choice" on page 1092 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1093
Or   FaceAmount <FaceAmt> [1..1] Amount 1093
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1093
Or   Code <Cd> [1..1] CodeSet 1093
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1093
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
3.4.11.23.7  BackEndOddLotQuantity <BckEndOddLotQty>
Presence: [0..1]
Definition: Represents the presence of a back end odd lot provision and the quantity of equity required
after proration to be eligible for this privilege.
Impacted by: C27 "DigitalTokenUnitUsageRule"
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 170 February 2026
```

