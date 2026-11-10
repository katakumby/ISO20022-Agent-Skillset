---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.10 SecuritiesMovementDetails <SctiesMvmntDtls>", "8.4.12.10.7 OtherIncomeType <OthrIncmTp>"]
file_pages: [599]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.10.7 OtherIncomeType <OthrIncmTp>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 599 to 599.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 599

```text
Definition: Specifies the type of income.
The lists of income type codes to be used, are available on the SMPG website at www.smpg.info.
IncomeType <IncmTp> contains the following elements (see "GenericIdentification30" on page 879
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
8.4.12.10.7  OtherIncomeType <OthrIncmTp>
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
8.4.12.10.8  ExemptionType <XmptnTp>
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
8.4.12.10.9  CountryOfIncomeSource <CtryOfIncmSrc>
Presence: [0..1]
Definition: Indicates the country from which the income originates.
Impacted by: C11 "Country"
Datatype: "CountryCode" on page 1205
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 599 February 2026
```

