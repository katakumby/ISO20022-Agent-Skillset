---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.10 CorporateActionGeneralInformation <CorpActnGnlInf>", "7.4.10.7 UnderlyingSecurity <UndrlygScty>", "7.4.10.7.21 WarrantParity <WarrtParity>"]
file_pages: [401]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.10.7.21 WarrantParity <WarrtParity>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 401 to 401.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 401

```text
7.4.10.7.21  WarrantParity <WarrtParity>
Presence: [0..1]
Definition: Provides the ratio between the quantity of warrants and the quantity of underlying securities.
WarrantParity <WarrtParity> contains the following elements (see "QuantityToQuantityRatio1" on
page 871 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity1 <Qty1> [1..1] Quantity 871
   Quantity2 <Qty2> [1..1] Quantity 871
7.4.10.7.22  MinimumNominalQuantity <MinNmnlQty>
Presence: [0..1]
Definition: Minimum nominal quantity of financial instrument.
Impacted by: C19 "DigitalTokenUnitUsageRule"
MinimumNominalQuantity <MinNmnlQty> contains one of the following elements (see
"FinancialInstrumentQuantity33Choice" on page 1091 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1092
Or   FaceAmount <FaceAmt> [1..1] Amount 1092
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1092
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1092
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
7.4.10.7.23  ContractSize <CtrctSz>
Presence: [0..1]
Definition: Ratio or multiplying factor used to convert one contract into a financial instrument quantity.
Impacted by: C19 "DigitalTokenUnitUsageRule"
ContractSize <CtrctSz> contains one of the following elements (see
"FinancialInstrumentQuantity33Choice" on page 1091 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1092
Or   FaceAmount <FaceAmt> [1..1] Amount 1092
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1092
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1092
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 401 February 2026
```

