---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["8 camt.009.001.08 GetLimitV08", "8.4 Message Building Blocks", "8.4.2 LimitQueryDefinition <LmtQryDef>", "8.4.2.2 LimitCriteria <LmtCrit>", "8.4.2.2.2 NewCriteria <NewCrit>", "8.4.2.2.2.2 SearchCriteria <SchCrit>", "8.4.2.2.2.2.11 LimitValidAsOfDate <LmtVldAsOfDt>", "8.4.2.2.2.2.11.1 Date <Dt>"]
file_pages: [388]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.009.001.08"]
---

# 8.4.2.2.2.2.11.1 Date <Dt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 388 to 388.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 388

```text
LimitValidAsOfDate <LmtVldAsOfDt> contains one of the following DateAndPeriod2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 388
Or   Period <Prd> [1..1] ± 388
Or   FromDate <FrDt> [1..1] Date 388
Or}   ToDate <ToDt> [1..1] Date 388
8.4.2.2.2.2.11.1  Date <Dt>
Presence: [1..1]
Definition: Specific date within a period.
Datatype: "ISODate" on page 883
8.4.2.2.2.2.11.2  Period <Prd>
Presence: [1..1]
Definition: Time span defined by a start date and an end date.
Period <Prd> contains the following elements (see "Period2" on page 800 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 801
   ToDate <ToDt> [1..1] Date 801
8.4.2.2.2.2.11.3  FromDate <FrDt>
Presence: [1..1]
Definition: Date at which the range starts.
Datatype: "ISODate" on page 883
8.4.2.2.2.2.11.4  ToDate <ToDt>
Presence: [1..1]
Definition: Date at which the range ends.
Datatype: "ISODate" on page 883
8.4.2.2.2.3  ReturnCriteria <RtrCrit>
Presence: [0..1]
Definition: Defines the expected limit report.
Approved by the Payments SEG on 04 February 2025 camt.009.001.08 GetLimitV08
Cash Management - Maintenance 2024 - 2025 388 February 2025
```

