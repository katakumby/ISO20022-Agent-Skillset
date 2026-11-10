---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.18 Financial Instrument", "66.1.18.5 TaxEfficientProduct6", "66.1.18.5.4 PreviousYears <PrvsYrs>"]
file_pages: [4503]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.18.5.4 PreviousYears <PrvsYrs>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4503 to 4503.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4503

```text
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.18.5.4  PreviousYears <PrvsYrs>
Presence: [0..1]
Definition: Investment plans issued during previous years.
Impacted by: C42 "SpecificPreviousYearsGuideline"
PreviousYears <PrvsYrs> contains the following PreviousYear4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PreviousYears <PrvsYrs> [1..1]  4503
{Or     AllPreviousYears <AllPrvsYrs> [1..1] Text 4503
Or}     SpecificPreviousYears <SpcfcPrvsYrs> [1..*] Year 4503
   CashComponentIndicator <CshCmpntInd> [0..1] Indicator 4504
Constraints
• SpecificPreviousYearsGuideline
SpecificPreviousYears must not contain the current year.
66.1.18.5.4.1  PreviousYears <PrvsYrs>
Presence: [1..1]
Definition: Investment plans issued during previous years.
PreviousYears <PrvsYrs> contains one of the following PreviousYear1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AllPreviousYears <AllPrvsYrs> [1..1] Text 4503
Or}   SpecificPreviousYears <SpcfcPrvsYrs> [1..*] Year 4503
66.1.18.5.4.1.1  AllPreviousYears <AllPrvsYrs>
Presence: [1..1]
Definition: Selection of all investment plans.
Datatype: "PreviousAll" on page 5405
66.1.18.5.4.1.2  SpecificPreviousYears <SpcfcPrvsYrs>
Presence: [1..*]
Definition: Selection of investment plans issued during previous years.
Datatype: "ISOYear" on page 5405
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4503 May 2026
```

