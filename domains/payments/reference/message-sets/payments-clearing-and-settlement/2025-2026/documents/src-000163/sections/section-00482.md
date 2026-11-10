---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.3 TransactionInformation <TxInf>", "5.4.3.21 OriginalTransactionReference <OrgnlTxRef>", "5.4.3.21.11 RemittanceInformation <RmtInf>", "5.4.3.21.11.2 Structured <Strd>", "5.4.3.21.11.2.2 ReferredDocumentAmount <RfrdDocAmt>", "5.4.3.21.11.2.2.1 RemittanceAmountAndType <RmtAmtAndTp>"]
file_pages: [663]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.3.21.11.2.2.1 RemittanceAmountAndType <RmtAmtAndTp>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 663 to 663.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 663

```text
ReferredDocumentAmount <RfrdDocAmt> contains the following RemittanceAmount4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceAmountAndType <RmtAmtAndTp> [0..*]  663
     Type <Tp> [1..1]  663
{Or       Code <Cd> [1..1] CodeSet 664
Or}       Proprietary <Prtry> [1..1] Text 664
     Amount <Amt> [1..1] Amount C2, C11 664
   AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  664
     Amount <Amt> [1..1] Amount C2, C11 664
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 665
     Reason <Rsn> [0..1] Text 665
     AdditionalInformation <AddtlInf> [0..1] Text 665
Constraints
• RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
5.4.3.21.11.2.2.1  RemittanceAmountAndType <RmtAmtAndTp>
Presence: [0..*]
Definition: Type and amount of money for the referred document.
RemittanceAmountAndType <RmtAmtAndTp> contains the following DocumentAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  663
{Or     Code <Cd> [1..1] CodeSet 664
Or}     Proprietary <Prtry> [1..1] Text 664
   Amount <Amt> [1..1] Amount C2, C11 664
5.4.3.21.11.2.2.1.1  Type <Tp>
Presence: [1..1]
Definition: Defines the type of amount.
Type <Tp> contains one of the following DocumentAmountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 664
Or}   Proprietary <Prtry> [1..1] Text 664
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
663 March 2026
```

