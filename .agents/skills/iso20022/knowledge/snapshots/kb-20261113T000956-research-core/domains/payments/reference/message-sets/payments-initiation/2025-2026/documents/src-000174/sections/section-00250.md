---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.8 TransactionInformation <TxInf>", "4.4.3.8.9 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.8.9.11 RemittanceInformation <RmtInf>", "4.4.3.8.9.11.2 Structured <Strd>", "4.4.3.8.9.11.2.2 ReferredDocumentAmount <RfrdDocAmt>", "4.4.3.8.9.11.2.2.1 RemittanceAmountAndType <RmtAmtAndTp>"]
file_pages: [364]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.8.9.11.2.2.1 RemittanceAmountAndType <RmtAmtAndTp>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 364 to 364.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 364

```text
ReferredDocumentAmount <RfrdDocAmt> contains the following RemittanceAmount4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceAmountAndType <RmtAmtAndTp> [0..*]  364
     Type <Tp> [1..1]  364
{Or       Code <Cd> [1..1] CodeSet 365
Or}       Proprietary <Prtry> [1..1] Text 365
     Amount <Amt> [1..1] Amount C2, C9 365
   AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  365
     Amount <Amt> [1..1] Amount C2, C9 365
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 366
     Reason <Rsn> [0..1] Text 366
     AdditionalInformation <AddtlInf> [0..1] Text 366
Constraints
• RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
4.4.3.8.9.11.2.2.1  RemittanceAmountAndType <RmtAmtAndTp>
Presence: [0..*]
Definition: Type and amount of money for the referred document.
RemittanceAmountAndType <RmtAmtAndTp> contains the following DocumentAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  364
{Or     Code <Cd> [1..1] CodeSet 365
Or}     Proprietary <Prtry> [1..1] Text 365
   Amount <Amt> [1..1] Amount C2, C9 365
4.4.3.8.9.11.2.2.1.1  Type <Tp>
Presence: [1..1]
Definition: Defines the type of amount.
Type <Tp> contains one of the following DocumentAmountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 365
Or}   Proprietary <Prtry> [1..1] Text 365
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 364 March 2026
```

