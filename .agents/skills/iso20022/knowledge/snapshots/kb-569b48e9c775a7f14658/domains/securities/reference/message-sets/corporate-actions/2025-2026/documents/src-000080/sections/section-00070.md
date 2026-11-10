---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.5 SecuritiesQuantity <SctiesQty>", "3.4.10.5.4 NewDenominationQuantity <NewDnmtnQty>"]
file_pages: [116]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.5.4 NewDenominationQuantity <NewDnmtnQty>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 116 to 116.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 116

```text
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
3.4.10.5.4  NewDenominationQuantity <NewDnmtnQty>
Presence: [0..1]
Definition: New denomination of the equity following, for example, an increase or decrease in nominal
value.
Impacted by: C27 "DigitalTokenUnitUsageRule"
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
3.4.10.5.5  BaseDenomination <BaseDnmtn>
Presence: [0..1]
Definition: Minimum integral amount of securities that each account owner must have remaining after
the called amounts are applied.
Impacted by: C27 "DigitalTokenUnitUsageRule"
BaseDenomination <BaseDnmtn> contains one of the following elements (see
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
Corporate Actions - Maintenance 2025 - 2026 116 February 2026
```

