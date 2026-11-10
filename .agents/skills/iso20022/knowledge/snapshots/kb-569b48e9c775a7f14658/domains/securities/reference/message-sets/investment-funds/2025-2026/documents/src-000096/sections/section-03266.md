---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.18 Financial Instrument", "66.1.18.5 TaxEfficientProduct6", "66.1.18.5.1 TaxEfficientProductType <TaxEffcntPdctTp>"]
file_pages: [4502]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.18.5.1 TaxEfficientProductType <TaxEffcntPdctTp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4502 to 4502.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4502

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxEfficientProductType <TaxEffcntPdctTp> [1..1] ± 4502
   CurrentYear <CurYr> [0..1] Indicator 4502
   CashComponentIndicator <CshCmpntInd> [0..1] Indicator 4502
   PreviousYears <PrvsYrs> [0..1]  C42 4503
     PreviousYears <PrvsYrs> [1..1]  4503
{Or       AllPreviousYears <AllPrvsYrs> [1..1] Text 4503
Or}       SpecificPreviousYears <SpcfcPrvsYrs> [1..*] Year 4503
     CashComponentIndicator <CshCmpntInd> [0..1] Indicator 4504
   CurrentYearSubscriptionDetails <CurYrSbcptDtls> [0..1]  C45 4504
     DateOfFirstSubscription <DtOfFrstSbcpt> [1..1] Date 4504
     EquityComponent <EqtyCmpnt> [0..1] Amount C1 4504
     CashComponent <CshCmpnt> [0..1] Amount C1 4505
     TotalAmountYearToDate <TtlAmtYrToDt> [1..1] Amount C1 4505
   AdditionalInformation <AddtlInf> [0..*] ± 4505
66.1.18.5.1  TaxEfficientProductType <TaxEffcntPdctTp>
Presence: [1..1]
Definition: Type of tax efficient product, for example, an individual savings account (ISA) in the UK.
TaxEfficientProductType <TaxEffcntPdctTp> contains one of the following elements (see
"TaxEfficientProductType2Choice" on page 4505 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4506
Or}   Proprietary <Prtry> [1..1] ± 4507
66.1.18.5.2  CurrentYear <CurYr>
Presence: [0..1]
Definition: Indicates that all the current fiscal year's products are to be included.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.18.5.3  CashComponentIndicator <CshCmpntInd>
Presence: [0..1]
Definition: Indicates whether the product contains a cash asset for transfer.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4502 May 2026
```

