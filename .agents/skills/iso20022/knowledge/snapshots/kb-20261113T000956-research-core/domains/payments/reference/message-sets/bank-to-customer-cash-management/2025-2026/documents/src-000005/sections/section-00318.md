---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.16 RelatedDates <RltdDts>", "3.4.2.15.18.2.16.6 EndDate <EndDt>"]
file_pages: [469]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.16.6 EndDate <EndDt>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 469 to 469.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 469

```text
Definition: Start date of the underlying transaction, such as a treasury transaction, an investment plan.
Datatype: "ISODate" on page 908
3.4.2.15.18.2.16.6  EndDate <EndDt>
Presence: [0..1]
Definition: End date of the underlying transaction, such as a treasury transaction, an investment plan.
Datatype: "ISODate" on page 908
3.4.2.15.18.2.16.7  TransactionDateTime <TxDtTm>
Presence: [0..1]
Definition: Date and time of the underlying transaction.
Datatype: "ISODateTime" on page 908
3.4.2.15.18.2.16.8  Proprietary <Prtry>
Presence: [0..*]
Definition: Proprietary date related to the underlying transaction.
Proprietary <Prtry> contains the following ProprietaryDate3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] Text 469
   Date <Dt> [1..1] ± 469
3.4.2.15.18.2.16.8.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of date.
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.16.8.2  Date <Dt>
Presence: [1..1]
Definition: Date in ISO format.
Date <Dt> contains one of the following elements (see "DateAndDateTime2Choice" on page 826 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 826
Or}   DateTime <DtTm> [1..1] DateTime 826
3.4.2.15.18.2.17  RelatedPrice <RltdPric>
Presence: [0..1]
Definition: Set of elements used to identify the price information related to the underlying transaction.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
469 March 2026
```

