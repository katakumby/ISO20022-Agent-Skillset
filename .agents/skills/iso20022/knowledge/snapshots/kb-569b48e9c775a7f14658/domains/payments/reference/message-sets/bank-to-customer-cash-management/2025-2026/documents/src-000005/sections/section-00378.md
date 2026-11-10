---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.6 CreationDateTime <CreDtTm>"]
file_pages: [563]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.6 CreationDateTime <CreDtTm>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 563 to 563.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 563

```text
4.4.2.6  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the notification was created.
Datatype: "ISODateTime" on page 908
4.4.2.7  FromToDate <FrToDt>
Presence: [0..1]
Definition: Range of time between a start date and an end date for which the account notification is
issued.
FromToDate <FrToDt> contains the following elements (see "DateTimePeriod1" on page 828 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 828
   ToDateTime <ToDtTm> [1..1] DateTime 828
4.4.2.8  CopyDuplicateIndicator <CpyDplctInd>
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
4.4.2.9  ReportingSource <RptgSrc>
Presence: [0..1]
Definition: Specifies the application used to generate the reporting.
ReportingSource <RptgSrc> contains one of the following elements (see "ReportingSource1Choice"
on page 845 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 845
Or}   Proprietary <Prtry> [1..1] Text 845
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
563 March 2026
```

