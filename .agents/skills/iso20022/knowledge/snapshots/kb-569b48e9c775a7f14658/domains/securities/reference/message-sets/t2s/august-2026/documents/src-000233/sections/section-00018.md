---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["2 admi.005.001.02 ReportQueryRequestV02", "2.4 Message Building Blocks", "2.4.2 ReportQueryCriteria <RptQryCrit>", "2.4.2.2 SearchCriteria <SchCrit>", "2.4.2.2.2 Balance <Bal>", "2.4.2.2.2.4 ValueDate <ValDt>", "2.4.2.2.2.4.2 Date <Dt>", "2.4.2.2.2.4.2.3 FromToDate <FrToDt>"]
file_pages: [49]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.005.001.02"]
---

# 2.4.2.2.2.4.2.3 FromToDate <FrToDt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 49 to 49.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 49

```text
Datatype: "ISODate" on page 3319
2.4.2.2.2.4.2.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 2908 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 2908
   ToDate <ToDt> [1..1] Date 2908
2.4.2.2.2.4.2.4  EqualDate <EQDt>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODate" on page 3319
2.4.2.2.2.4.2.5  NotEqualDate <NEQDt>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODate" on page 3319
2.4.2.2.2.5  ProcessingDate <PrcgDt>
Presence: [0..1]
Definition: Date or date time when the balance was last updated following an entry posted to the
account, in the books of the account servicing institution.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
admi.005.001.02 ReportQueryRequestV02
Target2-Securities 49 August 2026
```

