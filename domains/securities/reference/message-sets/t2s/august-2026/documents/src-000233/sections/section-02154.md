---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.9 Date Time", "82.1.9.8 Period2"]
file_pages: [2915]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.9.8 Period2

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2915 to 2915.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2915

```text
DateCode <DtCd> contains one of the following elements (see "SettlementDateCode8Choice" on
page 2911 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2911
Or}   Proprietary <Prtry> [1..1] ± 2911
82.1.9.8  Period2
Definition: Time span defined by a start date and time, and an end date and time.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 2915
   ToDate <ToDt> [1..1] Date 2915
82.1.9.8.1  FromDate <FrDt>
Presence: [1..1]
Definition: Date and time at which the range starts.
Datatype: "ISODate" on page 3319
82.1.9.8.2  ToDate <ToDt>
Presence: [1..1]
Definition: Date and time at which the range ends.
Datatype: "ISODate" on page 3319
82.1.10 Date Time Period
82.1.10.1  DateAndPeriod3Choice
Definition: Choice between a date and period.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   StatementDate <StmtDt> [1..1] ± 2915
Or}   StatementPeriod <StmtPrd> [1..1] ± 2916
82.1.10.1.1  StatementDate <StmtDt>
Presence: [1..1]
Definition: Date of the statement.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2915 August 2026
```

