---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.3 Date Period", "22.1.3.1 Period4Choice", "22.1.3.1.2 FromDate <FrDt>"]
file_pages: [323]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.3.1.2 FromDate <FrDt>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 323 to 323.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 323

```text
22.1.3.1.2  FromDate <FrDt>
Presence: [1..1]
Definition: Date at which the date period range starts.
Datatype: "ISODate" on page 449
22.1.3.1.3  ToDate <ToDt>
Presence: [1..1]
Definition: Date which the range date period ends.
Datatype: "ISODate" on page 449
22.1.3.1.4  FromDateToDate <FrDtToDt>
Presence: [1..1]
Definition: Time span defined by a start date, and an end date.
FromDateToDate <FrDtToDt> contains the following elements (see "Period2" on page 323 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 323
   ToDate <ToDt> [1..1] Date 323
22.1.4 Date Time
22.1.4.1  Period2
Definition: Time span defined by a start date and time, and an end date and time.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 323
   ToDate <ToDt> [1..1] Date 323
22.1.4.1.1  FromDate <FrDt>
Presence: [1..1]
Definition: Date and time at which the range starts.
Datatype: "ISODate" on page 449
22.1.4.1.2  ToDate <ToDt>
Presence: [1..1]
Definition: Date and time at which the range ends.
Datatype: "ISODate" on page 449
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
323 July 2025
```

