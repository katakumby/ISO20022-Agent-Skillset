---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.6 InvestmentFundsOrderBreakdown2"]
file_pages: [4733]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.6 InvestmentFundsOrderBreakdown2

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4733 to 4733.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4733

```text
Note: The decimal separator is a dot.
66.1.26.6  InvestmentFundsOrderBreakdown2
Definition: An investor's instruction to either subscribe or redeem an amount of money or its equivalent,
for example, other assets, into or out of an investment fund.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OrderBreakdownType <OrdrBrkdwnTp> [1..1]  4733
{Or     Code <Cd> [1..1] CodeSet 4733
Or}     Proprietary <Prtry> [1..1] ± 4733
   Amount <Amt> [1..1] Amount C1, C13 4734
66.1.26.6.1  OrderBreakdownType <OrdrBrkdwnTp>
Presence: [1..1]
Definition: Type of order breakdown.
OrderBreakdownType <OrdrBrkdwnTp> contains one of the following
OrderBreakdownType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4733
Or}   Proprietary <Prtry> [1..1] ± 4733
66.1.26.6.1.1  Code <Cd>
Presence: [1..1]
Definition: Order breakdown type expressed as a code.
Datatype: "FundOrderType5Code" on page 5306
CodeName Name Definition
NSPN NormalStaffPortion That part of an investment fund order
attributed to a normal staff portion.
NCPN NormalClientPortion That part of an investment fund order
attributed to a normal client portion.
SWSP StaffWithSavingsPlan That part of an investment fund order
attributed to a staff member with a
savings plan.
CWSP ClientWithSavingsPlan That part of an investment fund order
attributed to a client with a savings plan.
66.1.26.6.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Order breakdown type expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4733 May 2026
```

