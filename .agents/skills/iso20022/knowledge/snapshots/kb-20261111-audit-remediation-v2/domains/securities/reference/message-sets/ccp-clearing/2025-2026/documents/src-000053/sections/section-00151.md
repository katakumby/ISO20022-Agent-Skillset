---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["5 MX secl.004.001.04 NetPositionV04", "5.4 Message Building Blocks", "5.4.1 ReportParameters <RptParams>", "5.4.1.1 NetPositionIdentification <NetPosId>"]
file_pages: [199]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.004.001.04"]
---

# 5.4.1.1 NetPositionIdentification <NetPosId>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 199 to 199.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 199

```text
Constraints
• ReportNumberRule
(Rule)
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the same
safekeeping account must have different ReportNumbers. For example, a daily report sent on day 1
would have ReportNumber 001, on day 2, 002, etc.
5.4.1.1  NetPositionIdentification <NetPosId>
Presence: [1..1]
Definition: After netting, reference that is common to a net transaction to settle and all its underlying
trades.
Datatype: Max35Text on page 493
5.4.1.2  ReportDateAndTime <RptDtAndTm>
Presence: [1..1]
Definition: Date and time of the net position report.
ReportDateAndTime <RptDtAndTm> contains one of the following elements (see
DateAndDateTime2Choice on page 390 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 390
Or}   DateTime <DtTm> [1..1] DateTime 390
5.4.1.3  UpdateType <UpdTp>
Presence: [1..1]
Definition: Indicates whether the statement is complete or contains changes only.
Datatype: StatementUpdateType1Code on page 483
CodeName Name Definition
COMP Complete Statement is complete.
DELT Delta Statement contains changes only.
5.4.1.4  Frequency <Frqcy>
Presence: [1..1]
Definition: Frequency of the report.
Datatype: EventFrequency6Code on page 477
CodeName Name Definition
DAIL Daily Event takes place every day.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 199
```

