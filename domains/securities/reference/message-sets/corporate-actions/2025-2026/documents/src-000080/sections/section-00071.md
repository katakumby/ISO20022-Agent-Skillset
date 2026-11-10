---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.5 SecuritiesQuantity <SctiesQty>", "3.4.10.5.6 IncrementalDenomination <IncrmtlDnmtn>"]
file_pages: [117]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.5.6 IncrementalDenomination <IncrmtlDnmtn>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 117 to 117.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 117

```text
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
3.4.10.5.6  IncrementalDenomination <IncrmtlDnmtn>
Presence: [0..1]
Definition: Amount used when the called amount is not met by running the lottery with the base
denomination.
Impacted by: C27 "DigitalTokenUnitUsageRule"
IncrementalDenomination <IncrmtlDnmtn> contains one of the following elements (see
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
3.4.10.5.7  SecurityCalledQuantity <SctyClldQty>
Presence: [0..1]
Definition: Total quantity of the underlying securities called, either held or not held at the depository.
Impacted by: C27 "DigitalTokenUnitUsageRule"
SecurityCalledQuantity <SctyClldQty> contains one of the following elements (see
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
Corporate Actions - Maintenance 2025 - 2026 117 February 2026
```

