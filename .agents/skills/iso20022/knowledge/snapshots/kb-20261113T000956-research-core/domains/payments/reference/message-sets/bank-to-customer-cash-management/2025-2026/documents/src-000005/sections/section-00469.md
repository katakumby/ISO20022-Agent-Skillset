---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.15 RemittanceInformation <RmtInf>", "4.4.2.14.18.2.15.2 Structured <Strd>", "4.4.2.14.18.2.15.2.1 ReferredDocumentInformation <RfrdDocInf>", "4.4.2.14.18.2.15.2.1.4 LineDetails <LineDtls>"]
file_pages: [696]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.15.2.1.4 LineDetails <LineDtls>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 696 to 696.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 696

```text
4.4.2.14.18.2.15.2.1.4  LineDetails <LineDtls>
Presence: [0..*]
Definition: Set of elements used to provide the content of the referred document line.
LineDetails <LineDtls> contains the following DocumentLineInformation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..*]  696
     Type <Tp> [0..1]  697
       CodeOrProprietary <CdOrPrtry> [1..1]  697
{Or         Code <Cd> [1..1] CodeSet 697
Or}         Proprietary <Prtry> [1..1] Text 697
       Issuer <Issr> [0..1] Text 698
     Number <Nb> [0..1] Text 698
     RelatedDate <RltdDt> [0..1] Date 698
   Description <Desc> [0..1] Text 698
   Amount <Amt> [0..1]  C26 698
     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  699
       Type <Tp> [1..1]  699
{Or         Code <Cd> [1..1] CodeSet 700
Or}         Proprietary <Prtry> [1..1] Text 700
       Amount <Amt> [1..1] Amount C2, C6 700
     AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  700
       Amount <Amt> [1..1] Amount C2, C6 700
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 701
       Reason <Rsn> [0..1] Text 701
       AdditionalInformation <AddtlInf> [0..1] Text 701
4.4.2.14.18.2.15.2.1.4.1  Identification <Id>
Presence: [1..*]
Definition: Provides identification of the document line.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
696 March 2026
```

