---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.5 Portfolio <Prtfl>", "36.4.15.5.1 TaxEfficientProduct <TaxEffcntPdct>", "36.4.15.5.1.3 CashComponentIndicator <CshCmpntInd>"]
file_pages: [1156]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.5.1.3 CashComponentIndicator <CshCmpntInd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1156 to 1156.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1156

```text
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
36.4.15.5.1.3  CashComponentIndicator <CshCmpntInd>
Presence: [0..1]
Definition: Indicates whether, for the current year, the product contains a cash asset for transfer.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
36.4.15.5.1.4  PreviousYears <PrvsYrs>
Presence: [0..1]
Definition: Investment plans issued during previous years.
Impacted by: C49 "SpecificPreviousYearsGuideline"
PreviousYears <PrvsYrs> contains the following PreviousYear4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PreviousYears <PrvsYrs> [1..1]  1156
{Or     AllPreviousYears <AllPrvsYrs> [1..1] Text 1156
Or}     SpecificPreviousYears <SpcfcPrvsYrs> [1..*] Year 1157
   CashComponentIndicator <CshCmpntInd> [0..1] Indicator 1157
Constraints
• SpecificPreviousYearsGuideline
SpecificPreviousYears must not contain the current year.
36.4.15.5.1.4.1  PreviousYears <PrvsYrs>
Presence: [1..1]
Definition: Investment plans issued during previous years.
PreviousYears <PrvsYrs> contains one of the following PreviousYear1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AllPreviousYears <AllPrvsYrs> [1..1] Text 1156
Or}   SpecificPreviousYears <SpcfcPrvsYrs> [1..*] Year 1157
36.4.15.5.1.4.1.1  AllPreviousYears <AllPrvsYrs>
Presence: [1..1]
Definition: Selection of all investment plans.
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1156 May 2026
```

