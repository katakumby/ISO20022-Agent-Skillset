---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.9 Date Time", "7.1.9.3 SettlementDate17Choice", "7.1.9.3.2 DateCode <DtCd>"]
file_pages: [320]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.9.3.2 DateCode <DtCd>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 320 to 320.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 320

```text
Date <Dt> contains one of the following elements (see "DateAndDateTime2Choice" on page 321 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 321
Or}   DateTime <DtTm> [1..1] DateTime 321
7.1.9.3.2  DateCode <DtCd>
Presence: [1..1]
Definition: Date and time at which the securities are to be delivered or received.
DateCode <DtCd> contains one of the following elements (see "SettlementDateCode7Choice" on
page 320 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 321
Or}   Proprietary <Prtry> [1..1] ± 321
7.1.9.4  DateAndDateTime1Choice
Definition: Choice between a date or a date and time format.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 320
Or}   DateTime <DtTm> [1..1] DateTime 320
7.1.9.4.1  Date <Dt>
Presence: [1..1]
Definition: Numeric representation of the day of the month and year.
Datatype: "ISODate" on page 550
7.1.9.4.2  DateTime <DtTm>
Presence: [1..1]
Definition: Numeric representation of time of the day and the day of the month and year.
Datatype: "ISODateTime" on page 551
7.1.9.5  SettlementDateCode7Choice
Definition: Choice of format for the settlement date code.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 321
Or}   Proprietary <Prtry> [1..1] ± 321
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 320 March 2026
```

