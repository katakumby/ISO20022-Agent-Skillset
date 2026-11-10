---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.18 Financial Instrument", "66.1.18.2 TaxEfficientProduct4", "66.1.18.2.1 TaxEfficientProductType <TaxEffcntPdctTp>"]
file_pages: [4492]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.18.2.1 TaxEfficientProductType <TaxEffcntPdctTp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4492 to 4492.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4492

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxEfficientProductType <TaxEffcntPdctTp> [1..1] ± 4492
   CurrentYear <CurYr> [0..1] Indicator 4492
   PreviousYears <PrvsYrs> [0..1] ± C23 4492
   AdditionalInformation <AddtlInf> [0..*] ± 4493
66.1.18.2.1  TaxEfficientProductType <TaxEffcntPdctTp>
Presence: [1..1]
Definition: Type of tax efficient product, for example, an individual savings account (ISA) in the UK.
TaxEfficientProductType <TaxEffcntPdctTp> contains one of the following elements (see
"TaxEfficientProductType2Choice" on page 4505 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4506
Or}   Proprietary <Prtry> [1..1] ± 4507
66.1.18.2.2  CurrentYear <CurYr>
Presence: [0..1]
Definition: Indicates that all the current fiscal year's products are to be included.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.18.2.3  PreviousYears <PrvsYrs>
Presence: [0..1]
Definition: Investment plans issued during previous years.
Impacted by: C23 "SpecificPreviousYearsGuideline"
PreviousYears <PrvsYrs> contains one of the following elements (see "PreviousYear2Choice" on
page 4818 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AllPreviousYears <AllPrvsYrs> [1..1] Text 4818
Or}   SpecificPreviousYears <SpcfcPrvsYrs> [1..*] Year 4818
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4492 May 2026
```

