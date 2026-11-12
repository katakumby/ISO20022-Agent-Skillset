---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.11 ModificationScope41", "66.1.26.11.2 InvestmentPlan <InvstmtPlan>", "66.1.26.11.2.1 Frequency <Frqcy>"]
file_pages: [4746]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.11.2.1 Frequency <Frqcy>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4746 to 4746.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4746

```text
Following Must be True
    /GrossAmountIndicator Must be absent
66.1.26.11.2.1  Frequency <Frqcy>
Presence: [1..1]
Definition: Frequency of the investment or divestment.
Frequency <Frqcy> contains one of the following elements (see "Frequency20Choice" on page 4535
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4536
Or}   Proprietary <Prtry> [1..1] ± 4536
66.1.26.11.2.2  StartDate <StartDt>
Presence: [0..1]
Definition: Date the investment plan starts.
Datatype: "ISODate" on page 5388
66.1.26.11.2.3  EndDate <EndDt>
Presence: [0..1]
Definition: Date the investment plan stops.
Datatype: "ISODate" on page 5388
66.1.26.11.2.4  Quantity <Qty>
Presence: [1..1]
Definition: Amount of the periodical payments.
Quantity <Qty> contains one of the following elements (see "UnitsOrAmount1Choice" on page 4528
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1, C13 4529
Or}   Unit <Unit> [1..1] Quantity 4529
66.1.26.11.2.5  GrossAmountIndicator <GrssAmtInd>
Presence: [0..1]
Definition: Indicates whether an ordered amount is a gross amount (including transaction overhead). If it
is not a gross amount, the ordered amount is a net amount (amount to be invested or redeemed from
the fund to which other elements will be added).
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4746 May 2026
```

