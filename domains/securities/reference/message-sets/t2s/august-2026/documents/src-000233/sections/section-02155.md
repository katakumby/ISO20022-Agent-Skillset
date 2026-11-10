---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.10 Date Time Period", "82.1.10.1 DateAndPeriod3Choice", "82.1.10.1.2 StatementPeriod <StmtPrd>"]
file_pages: [2916]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.10.1.2 StatementPeriod <StmtPrd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2916 to 2916.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2916

```text
StatementDate <StmtDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
82.1.10.1.2  StatementPeriod <StmtPrd>
Presence: [1..1]
Definition: Period for the statement.
StatementPeriod <StmtPrd> contains one of the following elements (see "Period7Choice" on
page 2909 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTimeToDateTime <FrDtTmToDtTm> [1..1] ± 2909
Or}   FromDateToDate <FrDtToDt> [1..1] ± 2909
82.1.10.2  DateTimePeriod1
Definition: Time span defined by a start date and time, and an end date and time.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 2916
   ToDateTime <ToDtTm> [1..1] DateTime 2916
82.1.10.2.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Date and time at which the period starts.
Datatype: "ISODateTime" on page 3320
82.1.10.2.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: Date and time at which the period ends.
Datatype: "ISODateTime" on page 3320
82.1.11 Document
82.1.11.1  DocumentNumber5Choice
Definition: Choice between a short document number, a long document number or a proprietary
document number.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2916 August 2026
```

