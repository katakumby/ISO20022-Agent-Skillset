---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.25 AdditionalInformationUKMarket <AddtlInfUKMkt>"]
file_pages: [359]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.25 AdditionalInformationUKMarket <AddtlInfUKMkt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 359 to 359.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 359

```text
Definition: Costs and charges associated with the distribution of selling of the financial instrument.
These may be one-off or recurring. These may be ex ante (intended) or post ante (actual).
Impacted by: C16 "ExAnteReferenceDateGuideline", C19 "IndividualCostAndCharge1Guideline"
CostsAndCharges <CostsAndChrgs> contains the following elements (see "CostsAndCharges2" on
page 4441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ExAnteReferenceDate <ExAnteRefDt> [0..1] Date 4442
   IndividualCostOrCharge <IndvCostOrChrg> [1..*]  C14,
C15,
C31,
C32
4442
     CostType <CostTp> [1..1]  4443
{Or       Code <Cd> [1..1] CodeSet 4443
Or}       Proprietary <Prtry> [1..1] ± 4448
     ExAnteOrExPost <ExAnteOrExPst> [1..1] CodeSet 4448
     Amount <Amt> [0..1] Amount C1 4449
     Sign <Sgn> [0..1] Indicator 4449
     Rate <Rate> [0..1] Rate 4449
     ReferencePeriod <RefPrd> [0..1]  4449
       StartDate <StartDt> [1..1] Date 4450
       EndDate <EndDt> [1..1] Date 4450
     AdditionalInformation <AddtlInf> [0..1] ± 4450
   AdditionalInformation <AddtlInf> [0..1] ± 4450
Constraints
• ExAnteReferenceDateGuideline
The ex-ante reference date should not be confused with the reporting date as specified in the
European MiFID Template (EMT) reference 00050.
• IndividualCostAndCharge1Guideline
If ExAnteReferenceDate is present, then all repetitions of IndividualCostOrCharge must specify Ex
Ante costs
15.4.5.25  AdditionalInformationUKMarket <AddtlInfUKMkt>
Presence: [0..1]
Definition: Additional information required for distribution in the UK market.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 359 May 2026
```

