---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.4 Portfolio <Prtfl>", "38.4.15.4.1 TaxEfficientProduct <TaxEffcntPdct>", "38.4.15.4.1.3 CashComponentIndicator <CshCmpntInd>"]
file_pages: [1348]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.4.1.3 CashComponentIndicator <CshCmpntInd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1348 to 1348.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1348

```text
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
38.4.15.4.1.3  CashComponentIndicator <CshCmpntInd>
Presence: [0..1]
Definition: Indicates whether, for the current year, the product contains a cash asset for transfer.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
38.4.15.4.1.4  PreviousYears <PrvsYrs>
Presence: [0..1]
Definition: Investment plans issued during previous years.
Impacted by: C42 "SpecificPreviousYearsGuideline"
PreviousYears <PrvsYrs> contains the following PreviousYear4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PreviousYears <PrvsYrs> [1..1]  1348
{Or     AllPreviousYears <AllPrvsYrs> [1..1] Text 1348
Or}     SpecificPreviousYears <SpcfcPrvsYrs> [1..*] Year 1349
   CashComponentIndicator <CshCmpntInd> [0..1] Indicator 1349
Constraints
• SpecificPreviousYearsGuideline
SpecificPreviousYears must not contain the current year.
38.4.15.4.1.4.1  PreviousYears <PrvsYrs>
Presence: [1..1]
Definition: Investment plans issued during previous years.
PreviousYears <PrvsYrs> contains one of the following PreviousYear1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AllPreviousYears <AllPrvsYrs> [1..1] Text 1348
Or}   SpecificPreviousYears <SpcfcPrvsYrs> [1..*] Year 1349
38.4.15.4.1.4.1.1  AllPreviousYears <AllPrvsYrs>
Presence: [1..1]
Definition: Selection of all investment plans.
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1348 May 2026
```

