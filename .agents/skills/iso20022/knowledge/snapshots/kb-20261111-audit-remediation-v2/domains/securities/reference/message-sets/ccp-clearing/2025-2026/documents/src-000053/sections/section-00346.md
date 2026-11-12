---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.13 Miscellaneous", "12.1.13.1 Statement86", "12.1.13.1.3 UpdateType <UpdTp>"]
file_pages: [439]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.13.1.3 UpdateType <UpdTp>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 439 to 439.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 439

```text
StatementDateAndTime <StmtDtAndTm> contains one of the following elements (see
DateAndDateTime2Choice on page 390 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 390
Or}   DateTime <DtTm> [1..1] DateTime 390
12.1.13.1.3  UpdateType <UpdTp>
Presence: [1..1]
Definition: Indicates whether the statement is complete or contains changes only.
Datatype: StatementUpdateType1Code on page 483
CodeName Name Definition
COMP Complete Statement is complete.
DELT Delta Statement contains changes only.
12.1.13.1.4  Frequency <Frqcy>
Presence: [1..1]
Definition: Frequency of the statement.
Datatype: EventFrequency6Code on page 477
CodeName Name Definition
DAIL Daily Event takes place every day.
INDA IntraDay Event takes place several times a day.
ONDE OnDemand Event takes place on demand.
12.1.13.1.5  ReportNumber <RptNb>
Presence: [0..1]
Definition: Sequential number of the statement.
Datatype: Exact5NumericText on page 492
12.1.13.1.6  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see YesNoIndicator on page 490):
• Meaning When True: Yes
• Meaning When False: No
12.1.13.2  Pagination1
Definition: Number used to sequence pages when it is not possible for data to be conveyed in a single
message and the data has to be split across several pages (messages).
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 439
```

