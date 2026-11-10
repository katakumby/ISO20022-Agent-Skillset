---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.13 AccountingStatementOfHoldings2", "66.1.5.13.5 TotalValues <TtlVals>"]
file_pages: [4407]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.13.5 TotalValues <TtlVals>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4407 to 4407.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4407

```text
66.1.5.13.5  TotalValues <TtlVals>
Presence: [0..1]
Definition: Value of total holdings reported.
TotalValues <TtlVals> contains the following elements (see "TotalValueInPageAndStatement" on
page 4390 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalHoldingsValueOfPage <TtlHldgsValOfPg> [0..1] Amount C1, C13 4391
   TotalHoldingsValueOfStatement <TtlHldgsValOfStmt> [1..1] Amount C1, C13 4391
66.1.5.13.6  Extension <Xtnsn>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C16 "ExtensionRule"
Extension <Xtnsn> contains the following elements (see "Extension1" on page 4835 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [1..1] Text 4836
   Text <Txt> [1..1] Text 4836
Constraints
• ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
66.1.6 Cancellation Right
66.1.6.1  DateFormat1Choice
Definition: Choice between the formats to express a date.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4407
Or   Code <Cd> [1..1] CodeSet 4408
Or}   DateTime <DtTm> [1..1] DateTime 4408
66.1.6.1.1  Date <Dt>
Presence: [1..1]
Definition: Date expressed as a calendar date.
Datatype: "ISODate" on page 5388
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4407 May 2026
```

