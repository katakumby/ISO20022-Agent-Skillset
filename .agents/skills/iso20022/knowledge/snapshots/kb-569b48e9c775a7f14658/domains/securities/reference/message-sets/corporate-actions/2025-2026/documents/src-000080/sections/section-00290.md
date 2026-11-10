---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.10 CorporateActionGeneralInformation <CorpActnGnlInf>", "7.4.10.7 UnderlyingSecurity <UndrlygScty>", "7.4.10.7.18 PercentageOfDebtClaim <PctgOfDebtClm>"]
file_pages: [400]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.10.7.18 PercentageOfDebtClaim <PctgOfDebtClm>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 400 to 400.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 400

```text
Definition: Interest rate applicable to the next interest payment period in relation to variable rate
instruments.
NextInterestRate <NxtIntrstRate> contains one of the following elements (see "RateFormat24Choice"
on page 1098 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1098
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1098
7.4.10.7.18  PercentageOfDebtClaim <PctgOfDebtClm>
Presence: [0..1]
Definition: Percentage of the underlying assets of a fund that represents a debt, for example, in the
context of the EU Savings directive.
PercentageOfDebtClaim <PctgOfDebtClm> contains one of the following elements (see
"RateFormat24Choice" on page 1098 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1098
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1098
7.4.10.7.19  PreviousFactor <PrvsFctr>
Presence: [0..1]
Definition: Factor used to calculate the value of the outstanding principal of the financial instrument (for
factored securities) until the next redemption (factor) date.
PreviousFactor <PrvsFctr> contains one of the following elements (see "RateFormat12Choice" on
page 971 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 971
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 971
7.4.10.7.20  NextFactor <NxtFctr>
Presence: [0..1]
Definition: Factor used to calculate the value of the outstanding principal of the financial instrument (for
factored securities) that will applicable after the redemption (factor) date.
NextFactor <NxtFctr> contains one of the following elements (see "RateFormat12Choice" on
page 971 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 971
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 971
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 400 February 2026
```

