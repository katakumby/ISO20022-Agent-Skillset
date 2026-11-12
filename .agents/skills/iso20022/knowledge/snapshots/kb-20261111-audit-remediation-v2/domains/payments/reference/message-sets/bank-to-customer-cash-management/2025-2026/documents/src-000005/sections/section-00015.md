---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.6 CreationDateTime <CreDtTm>"]
file_pages: [44]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.6 CreationDateTime <CreDtTm>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 44 to 44.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 44

```text
2.4.2.6  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the report was created.
Datatype: "ISODateTime" on page 908
2.4.2.7  FromToDate <FrToDt>
Presence: [0..1]
Definition: Range of time between a start date and an end date for which the account report is issued.
FromToDate <FrToDt> contains the following elements (see "DateTimePeriod1" on page 828 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 828
   ToDateTime <ToDtTm> [1..1] DateTime 828
2.4.2.8  CopyDuplicateIndicator <CpyDplctInd>
Presence: [0..1]
Definition: Indicates whether the document is a copy, a duplicate, or a duplicate of a copy.
Datatype: "CopyDuplicate1Code" on page 891
CodeName Name Definition
CODU CopyDuplicate Message is being sent as a copy to a
party other than the account owner, for
information purposes and the message
is a duplicate of a message previously
sent.
COPY Copy Message is being sent as a copy to a
party other than the account owner, for
information purposes.
DUPL Duplicate Message is for information/confirmation
purposes. It is a duplicate of a message
previously sent.
2.4.2.9  ReportingSource <RptgSrc>
Presence: [0..1]
Definition: Specifies the application used to generate the reporting.
ReportingSource <RptgSrc> contains one of the following elements (see "ReportingSource1Choice"
on page 845 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 845
Or}   Proprietary <Prtry> [1..1] Text 845
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
44 March 2026
```

