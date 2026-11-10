---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.15 RemittanceInformation <RmtInf>", "3.4.2.15.18.2.15.2 Structured <Strd>", "3.4.2.15.18.2.15.2.1 ReferredDocumentInformation <RfrdDocInf>", "3.4.2.15.18.2.15.2.1.2 Number <Nb>"]
file_pages: [437]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.15.2.1.2 Number <Nb>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 437 to 437.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 437

```text
3.4.2.15.18.2.15.2.1.2  Number <Nb>
Presence: [0..1]
Definition: Unique and unambiguous identification of the referred document.
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.15.2.1.3  RelatedDate <RltdDt>
Presence: [0..1]
Definition: Date and date type associated with the referred document.
RelatedDate <RltdDt> contains the following DateAndType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  437
{Or     Code <Cd> [1..1] CodeSet 437
Or}     Proprietary <Prtry> [1..1] Text 437
   Date <Dt> [1..1] Date 437
3.4.2.15.18.2.15.2.1.3.1  Type <Tp>
Presence: [1..1]
Definition: Type of date associated with the referred document.
Type <Tp> contains one of the following DateType2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 437
Or}   Proprietary <Prtry> [1..1] Text 437
3.4.2.15.18.2.15.2.1.3.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the date type, as published in an external date type code set.
Datatype: "ExternalDateType1Code" on page 896
3.4.2.15.18.2.15.2.1.3.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the date type, in a free-text form.
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.15.2.1.3.2  Date <Dt>
Presence: [1..1]
Definition: Date associated with the referred document.
Datatype: "ISODate" on page 908
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
437 March 2026
```

