---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.15 RemittanceInformation <RmtInf>", "3.4.2.15.18.2.15.2 Structured <Strd>", "3.4.2.15.18.2.15.2.1 ReferredDocumentInformation <RfrdDocInf>", "3.4.2.15.18.2.15.2.1.4 LineDetails <LineDtls>"]
file_pages: [438]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.15.2.1.4 LineDetails <LineDtls>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 438 to 438.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 438

```text
3.4.2.15.18.2.15.2.1.4  LineDetails <LineDtls>
Presence: [0..*]
Definition: Set of elements used to provide the content of the referred document line.
LineDetails <LineDtls> contains the following DocumentLineInformation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..*]  438
     Type <Tp> [0..1]  439
       CodeOrProprietary <CdOrPrtry> [1..1]  439
{Or         Code <Cd> [1..1] CodeSet 439
Or}         Proprietary <Prtry> [1..1] Text 439
       Issuer <Issr> [0..1] Text 440
     Number <Nb> [0..1] Text 440
     RelatedDate <RltdDt> [0..1] Date 440
   Description <Desc> [0..1] Text 440
   Amount <Amt> [0..1]  C27 440
     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  441
       Type <Tp> [1..1]  441
{Or         Code <Cd> [1..1] CodeSet 442
Or}         Proprietary <Prtry> [1..1] Text 442
       Amount <Amt> [1..1] Amount C2, C6 442
     AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  442
       Amount <Amt> [1..1] Amount C2, C6 442
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 443
       Reason <Rsn> [0..1] Text 443
       AdditionalInformation <AddtlInf> [0..1] Text 443
3.4.2.15.18.2.15.2.1.4.1  Identification <Id>
Presence: [1..*]
Definition: Provides identification of the document line.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
438 March 2026
```

