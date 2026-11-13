---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.15 RemittanceInformation <RmtInf>", "3.4.2.15.18.2.15.2 Structured <Strd>", "3.4.2.15.18.2.15.2.1 ReferredDocumentInformation <RfrdDocInf>", "3.4.2.15.18.2.15.2.1.4 LineDetails <LineDtls>", "3.4.2.15.18.2.15.2.1.4.3 Amount <Amt>", "3.4.2.15.18.2.15.2.1.4.3.1 RemittanceAmountAndType <RmtAmtAndTp>"]
file_pages: [441]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.15.2.1.4.3.1 RemittanceAmountAndType <RmtAmtAndTp>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 441 to 441.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 441

```text
Amount <Amt> contains the following RemittanceAmount4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceAmountAndType <RmtAmtAndTp> [0..*]  441
     Type <Tp> [1..1]  441
{Or       Code <Cd> [1..1] CodeSet 442
Or}       Proprietary <Prtry> [1..1] Text 442
     Amount <Amt> [1..1] Amount C2, C6 442
   AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  442
     Amount <Amt> [1..1] Amount C2, C6 442
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 443
     Reason <Rsn> [0..1] Text 443
     AdditionalInformation <AddtlInf> [0..1] Text 443
Constraints
• RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
3.4.2.15.18.2.15.2.1.4.3.1  RemittanceAmountAndType <RmtAmtAndTp>
Presence: [0..*]
Definition: Type and amount of money for the referred document.
RemittanceAmountAndType <RmtAmtAndTp> contains the following DocumentAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  441
{Or     Code <Cd> [1..1] CodeSet 442
Or}     Proprietary <Prtry> [1..1] Text 442
   Amount <Amt> [1..1] Amount C2, C6 442
3.4.2.15.18.2.15.2.1.4.3.1.1  Type <Tp>
Presence: [1..1]
Definition: Defines the type of amount.
Type <Tp> contains one of the following DocumentAmountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 442
Or}   Proprietary <Prtry> [1..1] Text 442
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
441 March 2026
```

