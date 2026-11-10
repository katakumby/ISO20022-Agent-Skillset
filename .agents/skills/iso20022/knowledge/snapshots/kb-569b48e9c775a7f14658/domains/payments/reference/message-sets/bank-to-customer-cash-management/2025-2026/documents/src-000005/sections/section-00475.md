---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.15 RemittanceInformation <RmtInf>", "4.4.2.14.18.2.15.2 Structured <Strd>", "4.4.2.14.18.2.15.2.2 ReferredDocumentAmount <RfrdDocAmt>", "4.4.2.14.18.2.15.2.2.1 RemittanceAmountAndType <RmtAmtAndTp>"]
file_pages: [702]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.15.2.2.1 RemittanceAmountAndType <RmtAmtAndTp>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 702 to 702.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 702

```text
ReferredDocumentAmount <RfrdDocAmt> contains the following RemittanceAmount4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceAmountAndType <RmtAmtAndTp> [0..*]  702
     Type <Tp> [1..1]  702
{Or       Code <Cd> [1..1] CodeSet 703
Or}       Proprietary <Prtry> [1..1] Text 703
     Amount <Amt> [1..1] Amount C2, C6 703
   AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  703
     Amount <Amt> [1..1] Amount C2, C6 703
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 704
     Reason <Rsn> [0..1] Text 704
     AdditionalInformation <AddtlInf> [0..1] Text 704
Constraints
• RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
4.4.2.14.18.2.15.2.2.1  RemittanceAmountAndType <RmtAmtAndTp>
Presence: [0..*]
Definition: Type and amount of money for the referred document.
RemittanceAmountAndType <RmtAmtAndTp> contains the following DocumentAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  702
{Or     Code <Cd> [1..1] CodeSet 703
Or}     Proprietary <Prtry> [1..1] Text 703
   Amount <Amt> [1..1] Amount C2, C6 703
4.4.2.14.18.2.15.2.2.1.1  Type <Tp>
Presence: [1..1]
Definition: Defines the type of amount.
Type <Tp> contains one of the following DocumentAmountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 703
Or}   Proprietary <Prtry> [1..1] Text 703
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
702 March 2026
```

