---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.25 CashMovementDetails <CshMvmntDtls>", "3.4.11.25.6 OtherIncomeType <OthrIncmTp>"]
file_pages: [207]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.25.6 OtherIncomeType <OthrIncmTp>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 207 to 207.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 207

```text
IncomeType <IncmTp> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
3.4.11.25.6  OtherIncomeType <OthrIncmTp>
Presence: [0..*]
Definition: Type of income to be used under another tax regime.
OtherIncomeType <OthrIncmTp> contains the following elements (see "GenericIdentification30" on
page 879 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
3.4.11.25.7  ExemptionType <XmptnTp>
Presence: [0..*]
Definition: Specifies the basis for the reduced rate of withholding.
ExemptionType <XmptnTp> contains the following elements (see "GenericIdentification30" on
page 879 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
3.4.11.25.8  PriceCalculationMethod <PricClctnMtd>
Presence: [0..1]
Definition: Specifies the method applied for the calculation of the price.
PriceCalculationMethod <PricClctnMtd> contains one of the following
PriceCalculationMethod2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 208
Or}   Proprietary <Prtry> [1..1] ± 208
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 207 February 2026
```

