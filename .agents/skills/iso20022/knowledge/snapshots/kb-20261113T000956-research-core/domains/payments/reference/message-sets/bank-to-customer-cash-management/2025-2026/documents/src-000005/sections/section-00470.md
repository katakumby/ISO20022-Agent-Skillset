---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.15 RemittanceInformation <RmtInf>", "4.4.2.14.18.2.15.2 Structured <Strd>", "4.4.2.14.18.2.15.2.1 ReferredDocumentInformation <RfrdDocInf>", "4.4.2.14.18.2.15.2.1.4 LineDetails <LineDtls>", "4.4.2.14.18.2.15.2.1.4.1 Identification <Id>", "4.4.2.14.18.2.15.2.1.4.1.1 Type <Tp>"]
file_pages: [697]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.15.2.1.4.1.1 Type <Tp>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 697 to 697.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 697

```text
Identification <Id> contains the following DocumentLineIdentification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  697
     CodeOrProprietary <CdOrPrtry> [1..1]  697
{Or       Code <Cd> [1..1] CodeSet 697
Or}       Proprietary <Prtry> [1..1] Text 697
     Issuer <Issr> [0..1] Text 698
   Number <Nb> [0..1] Text 698
   RelatedDate <RltdDt> [0..1] Date 698
4.4.2.14.18.2.15.2.1.4.1.1  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of referred document line identification.
Type <Tp> contains the following DocumentLineType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  697
{Or     Code <Cd> [1..1] CodeSet 697
Or}     Proprietary <Prtry> [1..1] Text 697
   Issuer <Issr> [0..1] Text 698
4.4.2.14.18.2.15.2.1.4.1.1.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Provides the type details of the referred document line identification.
CodeOrProprietary <CdOrPrtry> contains one of the following DocumentLineType1Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 697
Or}   Proprietary <Prtry> [1..1] Text 697
4.4.2.14.18.2.15.2.1.4.1.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Line identification type in a coded form.
Datatype: "ExternalDocumentLineType1Code" on page 896
4.4.2.14.18.2.15.2.1.4.1.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
697 March 2026
```

