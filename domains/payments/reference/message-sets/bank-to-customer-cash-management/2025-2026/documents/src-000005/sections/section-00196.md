---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.6 CreationDateTime <CreDtTm>"]
file_pages: [303]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.6 CreationDateTime <CreDtTm>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 303 to 303.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 303

```text
Usage: Where a paper statement is a legal requirement, it may have a number different from the
electronic sequential number. Paper statements could for instance only be sent if movement on the
account has taken place, whereas electronic statements could be sent at the end of each reporting
period, regardless of whether movements have taken place or not.
Datatype: "Number" on page 912
3.4.2.6  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the statement was created.
Datatype: "ISODateTime" on page 908
3.4.2.7  FromToDate <FrToDt>
Presence: [0..1]
Definition: Range of time between a start date and an end date for which the account statement is
issued.
FromToDate <FrToDt> contains the following elements (see "DateTimePeriod1" on page 828 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 828
   ToDateTime <ToDtTm> [1..1] DateTime 828
3.4.2.8  CopyDuplicateIndicator <CpyDplctInd>
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
3.4.2.9  ReportingSource <RptgSrc>
Presence: [0..1]
Definition: Specifies the application used to generate the reporting.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
303 March 2026
```

