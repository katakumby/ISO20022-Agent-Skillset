---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.21 SecuritiesQuantity <SctiesQty>", "7.4.13.21.6 FrontEndOddLotQuantity <FrntEndOddLotQty>"]
file_pages: [453]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.21.6 FrontEndOddLotQuantity <FrntEndOddLotQty>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 453 to 453.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 453

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
7.4.13.21.6  FrontEndOddLotQuantity <FrntEndOddLotQty>
Presence: [0..1]
Definition: Specifies that if an order is prorated holders of odd lots who tender their full position will not
have tendered position prorated but rather accepted in full.
Impacted by: C20 "DigitalTokenUnitUsageRule"
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
7.4.13.21.7  BackEndOddLotQuantity <BckEndOddLotQty>
Presence: [0..1]
Definition: Represents the presence of a back end odd lot provision and the quantity of equity required
after proration to be eligible for this privilege.
Impacted by: C20 "DigitalTokenUnitUsageRule"
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 453 February 2026
```

