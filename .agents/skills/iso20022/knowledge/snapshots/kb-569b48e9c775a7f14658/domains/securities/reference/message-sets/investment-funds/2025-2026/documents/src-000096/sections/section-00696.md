---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.22 OtherDrawdownInformation <OthrDrwdwnInf>", "34.4.4.22.1 EmploymentDetails <MplymntDtls>", "34.4.4.22.1.1 TaxCode <TaxCd>"]
file_pages: [938]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.22.1.1 TaxCode <TaxCd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 938 to 938.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 938

```text
EmploymentDetails <MplymntDtls> contains the following EmploymentDetails1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxCode <TaxCd> [0..1] ± 938
   OtherTaxCodeIndicator <OthrTaxCdInd> [0..1] Indicator 938
   CumulativeTaxIndicator <CmltvTaxInd> [0..1] Indicator 938
   PreviousPay <PrvsPay> [0..1] Amount C1, C10 939
   PreviousTax <PrvsTax> [0..1] Amount C1, C10 939
   StartDate <StartDt> [0..1] ± 939
   EndDate <EndDt> [0..1] ± 940
   AdditionalInformation <AddtlInf> [0..*] ± 940
34.4.4.22.1.1  TaxCode <TaxCd>
Presence: [0..1]
Definition: Current tax code.
TaxCode <TaxCd> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
34.4.4.22.1.2  OtherTaxCodeIndicator <OthrTaxCdInd>
Presence: [0..1]
Definition: Indicates whether or not another tax code exists.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
34.4.4.22.1.3  CumulativeTaxIndicator <CmltvTaxInd>
Presence: [0..1]
Definition: Indicates whether tax is cumulative or non-cumulative. In the UK, this is known as the W1M1
indicator.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 938 May 2026
```

