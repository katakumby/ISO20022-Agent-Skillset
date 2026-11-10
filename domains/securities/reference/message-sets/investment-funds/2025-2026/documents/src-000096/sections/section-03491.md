---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.8 FundOrderType4Choice", "66.1.26.8.1 Code <Cd>"]
file_pages: [4741]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.8.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4741 to 4741.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4741

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4741
Or}   Proprietary <Prtry> [1..1] ± 4741
66.1.26.8.1  Code <Cd>
Presence: [1..1]
Definition: Type of the investment fund order expressed as a code.
Datatype: "FundOrderType8Code" on page 5306
CodeName Name Definition
BEDB BedAndBreakfast Investment fund order is part of a bed
and breakfast transaction.
INVP InvestmentPlan Investment fund order is related to an
investment plan (only applicable to a
subscription).
PREA PreAdvice Investment fund order is executed with
specific pre-advice conditions.
RGSV RegularSavingsPlan Investment fund order is a regular
savings plan (only applicable to a
subscription).
RGSU RegularSavingsPlanUpdate Investment fund order is paying extra
money into to an existing plan (only
applicable to a subscription).
RDIV ReinvestmentOfDividend Investment fund order is a dividend
reinvestment (only applicable to a
subscription).
STAF StaffOrder Investment fund order is a staff order.
WIDP Withdrawal Investment fund order is for a withdrawal
investment plan (only applicable to a
redemption).
66.1.26.8.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of the investment fund order expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.26.9  PensionOrder1
Definition: Order attached to a pension.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4741 May 2026
```

