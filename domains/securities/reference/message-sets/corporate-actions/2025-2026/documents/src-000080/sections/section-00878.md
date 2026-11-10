---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.21 Quantity", "16.1.21.6 SignedQuantityFormat11", "16.1.21.6.2 QuantityChoice <QtyChc>", "16.1.21.6.2.2 ProprietaryQuantity <PrtryQty>", "16.1.21.6.2.2.4 SchemeName <SchmeNm>"]
file_pages: [1096]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.21.6.2.2.4 SchemeName <SchmeNm>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1096 to 1096.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1096

```text
Definition: Provides information related to issuer in free format.
Datatype: "Max35Text" on page 1251
16.1.21.6.2.2.4  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Datatype: "Max35Text" on page 1251
16.1.21.7  FinancialInstrumentQuantity34Choice
Definition: Choice between formats for the quantity of security.
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
16.1.21.7.1  Unit <Unit>
Presence: [1..1]
Definition: Quantity expressed as a number, for example, a number of shares.
Datatype: "DecimalNumber" on page 1246
16.1.21.7.2  FaceAmount <FaceAmt>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the face amount, that is, the principal, of a
debt instrument.
Datatype: "ImpliedCurrencyAndAmount" on page 1157
16.1.21.7.3  AmortisedValue <AmtsdVal>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the current amortised face amount of a bond,
for example, a periodic reduction/increase of a bond's principal amount.
Datatype: "ImpliedCurrencyAndAmount" on page 1157
16.1.21.7.4  Code <Cd>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1096 February 2026
```

