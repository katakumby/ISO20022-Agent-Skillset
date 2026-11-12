---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.10 CorporateActionGeneralInformation <CorpActnGnlInf>", "7.4.10.7 UnderlyingSecurity <UndrlygScty>", "7.4.10.7.11 IssueDate <IsseDt>"]
file_pages: [399]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.10.7.11 IssueDate <IsseDt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 399 to 399.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 399

```text
Datatype: "ISODate" on page 1243
7.4.10.7.11  IssueDate <IsseDt>
Presence: [0..1]
Definition: Date on which the financial instrument is issued.
Datatype: "ISODate" on page 1243
7.4.10.7.12  NextCallableDate <NxtCllblDt>
Presence: [0..1]
Definition: Date on which a financial instrument is called away/redeemed before its scheduled maturity.
Datatype: "ISODate" on page 1243
7.4.10.7.13  PutableDate <PutblDt>
Presence: [0..1]
Definition: Date on which a holder of a financial instrument has the right to request redemption of the
principal amount prior to its scheduled maturity date.
Datatype: "ISODate" on page 1243
7.4.10.7.14  DatedDate <DtdDt>
Presence: [0..1]
Definition: Date on which an interest bearing financial instrument begins to accrue interest.
Datatype: "ISODate" on page 1243
7.4.10.7.15  ConversionDate <ConvsDt>
Presence: [0..1]
Definition: Deadline by which a convertible security must be converted, according to the terms of the
issue.
Datatype: "ISODate" on page 1243
7.4.10.7.16  InterestRate <IntrstRate>
Presence: [0..1]
Definition: Annualised interest rate of a financial instrument used to calculate the actual interest rate of
the coupon or the accrued interest.
InterestRate <IntrstRate> contains one of the following elements (see "RateFormat24Choice" on
page 1098 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1098
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1098
7.4.10.7.17  NextInterestRate <NxtIntrstRate>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 399 February 2026
```

