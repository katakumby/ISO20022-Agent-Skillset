---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.31 InvestmentPlan17", "66.1.26.31.1 Frequency <Frqcy>"]
file_pages: [4793]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.31.1 Frequency <Frqcy>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4793 to 4793.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4793

```text
Constraints
• AmountRule
If Quantity/Amount is not present, then GrossAmountIndicator is not allowed.
On Condition
    /Quantity/Amount is absent
Following Must be True
    /GrossAmountIndicator Must be absent
66.1.26.31.1  Frequency <Frqcy>
Presence: [1..1]
Definition: Frequency of the investment or divestment.
Frequency <Frqcy> contains one of the following elements (see "Frequency20Choice" on page 4535
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4536
Or}   Proprietary <Prtry> [1..1] ± 4536
66.1.26.31.2  StartDate <StartDt>
Presence: [0..1]
Definition: Date the investment plan starts.
Datatype: "ISODate" on page 5388
66.1.26.31.3  EndDate <EndDt>
Presence: [0..1]
Definition: Date the investment plan stops.
Datatype: "ISODate" on page 5388
66.1.26.31.4  Quantity <Qty>
Presence: [1..1]
Definition: Amount of the periodical payments.
Quantity <Qty> contains one of the following elements (see "UnitsOrAmount1Choice" on page 4528
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1, C13 4529
Or}   Unit <Unit> [1..1] Quantity 4529
66.1.26.31.5  GrossAmountIndicator <GrssAmtInd>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4793 May 2026
```

