---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.5 PreviousYear2Choice"]
file_pages: [4818]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.5 PreviousYear2Choice

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4818 to 4818.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4818

```text
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
66.1.28.5  PreviousYear2Choice
Definition: Choice between selected investment plans issued during previous years or all investment
plans.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AllPreviousYears <AllPrvsYrs> [1..1] Text 4818
Or}   SpecificPreviousYears <SpcfcPrvsYrs> [1..*] Year 4818
Constraints
• SpecificPreviousYearsGuideline
SpecificPreviousYears must not contain the current year.
66.1.28.5.1  AllPreviousYears <AllPrvsYrs>
Presence: [1..1]
Definition: Selection of all investment plans.
Datatype: "PreviousAll" on page 5405
66.1.28.5.2  SpecificPreviousYears <SpcfcPrvsYrs>
Presence: [1..*]
Definition: Selection of investment plans issued during previous years.
Datatype: "ISOYear" on page 5405
66.1.28.6  MarketPracticeVersion1
Definition: Identifies the implementation and version.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 4818
   Date <Dt> [0..1] YearMonth 4819
   Number <Nb> [0..1] Text 4819
66.1.28.6.1  Name <Nm>
Presence: [1..1]
Definition: Market practice, for example, "UKTRANSFERS", "FINDELSLT".
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4818 May 2026
```

