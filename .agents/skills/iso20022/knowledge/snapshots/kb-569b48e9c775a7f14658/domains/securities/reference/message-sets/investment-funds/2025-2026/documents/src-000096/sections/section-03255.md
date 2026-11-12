---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.18 Financial Instrument", "66.1.18.1 FinancialInstrument96", "66.1.18.1.25 RDRCompliant <RDRCmplnt>"]
file_pages: [4491]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.18.1.25 RDRCompliant <RDRCmplnt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4491 to 4491.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4491

```text
66.1.18.1.25  RDRCompliant <RDRCmplnt>
Presence: [0..1]
Definition: Indicates whether the fund is compliant with the Retail Distribution Review (RDR).
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.18.1.26  ManagementFeeSource <MgmtFeeSrc>
Presence: [0..1]
Definition: Specifies from where the management fee is taken.
Datatype: "AnnualChargePaymentType1Code" on page 5276
CodeName Name Definition
CAPL Capital Annual charge is deducted from the fund
capital.
INCO Income Annual charge is deducted from the fund
income.
66.1.18.1.27  PerformanceFee <PrfrmncFee>
Presence: [0..1]
Definition: Indicates whether there is a performance fee feature or carried interest. When used in
reference to MiFID, this is in the scope of the European MiFID Template (EMT) reference 00045.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.18.1.28  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the fund.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
66.1.18.2  TaxEfficientProduct4
Definition: Characteristics of a tax efficient product.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4491 May 2026
```

