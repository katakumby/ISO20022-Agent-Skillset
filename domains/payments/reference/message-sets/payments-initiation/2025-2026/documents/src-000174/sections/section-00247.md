---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.8 TransactionInformation <TxInf>", "4.4.3.8.9 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.8.9.11 RemittanceInformation <RmtInf>", "4.4.3.8.9.11.2 Structured <Strd>", "4.4.3.8.9.11.2.1 ReferredDocumentInformation <RfrdDocInf>", "4.4.3.8.9.11.2.1.4 LineDetails <LineDtls>", "4.4.3.8.9.11.2.1.4.3 Amount <Amt>", "4.4.3.8.9.11.2.1.4.3.1 RemittanceAmountAndType <RmtAmtAndTp>"]
file_pages: [361]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.8.9.11.2.1.4.3.1 RemittanceAmountAndType <RmtAmtAndTp>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 361 to 361.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 361

```text
Amount <Amt> contains the following RemittanceAmount4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceAmountAndType <RmtAmtAndTp> [0..*]  361
     Type <Tp> [1..1]  361
{Or       Code <Cd> [1..1] CodeSet 362
Or}       Proprietary <Prtry> [1..1] Text 362
     Amount <Amt> [1..1] Amount C2, C9 362
   AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  362
     Amount <Amt> [1..1] Amount C2, C9 362
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 363
     Reason <Rsn> [0..1] Text 363
     AdditionalInformation <AddtlInf> [0..1] Text 363
Constraints
• RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
4.4.3.8.9.11.2.1.4.3.1  RemittanceAmountAndType <RmtAmtAndTp>
Presence: [0..*]
Definition: Type and amount of money for the referred document.
RemittanceAmountAndType <RmtAmtAndTp> contains the following DocumentAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  361
{Or     Code <Cd> [1..1] CodeSet 362
Or}     Proprietary <Prtry> [1..1] Text 362
   Amount <Amt> [1..1] Amount C2, C9 362
4.4.3.8.9.11.2.1.4.3.1.1  Type <Tp>
Presence: [1..1]
Definition: Defines the type of amount.
Type <Tp> contains one of the following DocumentAmountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 362
Or}   Proprietary <Prtry> [1..1] Text 362
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 361 March 2026
```

