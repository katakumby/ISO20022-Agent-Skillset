---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.22 SecuritiesMovementDetails <SctiesMvmntDtls>", "7.4.13.22.8 OtherIncomeType <OthrIncmTp>"]
file_pages: [469]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.22.8 OtherIncomeType <OthrIncmTp>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 469 to 469.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 469

```text
Definition: Specifies the type of income.
The lists of income type codes to be used, are available on the SMPG website at www.smpg.info.
IncomeType <IncmTp> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
7.4.13.22.8  OtherIncomeType <OthrIncmTp>
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
7.4.13.22.9  ExemptionType <XmptnTp>
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
7.4.13.22.10  EntitledQuantity <EntitldQty>
Presence: [0..1]
Definition: Quantity of securities based on the terms of the corporate action event and balance of
underlying securities entitled to the account owner. (This quantity can be positive or negative).
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 469 February 2026
```

