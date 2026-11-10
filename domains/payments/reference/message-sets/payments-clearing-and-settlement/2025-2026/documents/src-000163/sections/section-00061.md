---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.3 TransactionInformationAndStatus <TxInfAndSts>", "2.4.3.18 OriginalTransactionReference <OrgnlTxRef>", "2.4.3.18.11 RemittanceInformation <RmtInf>", "2.4.3.18.11.2 Structured <Strd>", "2.4.3.18.11.2.2 ReferredDocumentAmount <RfrdDocAmt>", "2.4.3.18.11.2.2.1 RemittanceAmountAndType <RmtAmtAndTp>"]
file_pages: [93]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.4.3.18.11.2.2.1 RemittanceAmountAndType <RmtAmtAndTp>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 93 to 93.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 93

```text
ReferredDocumentAmount <RfrdDocAmt> contains the following RemittanceAmount4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceAmountAndType <RmtAmtAndTp> [0..*]  93
     Type <Tp> [1..1]  93
{Or       Code <Cd> [1..1] CodeSet 94
Or}       Proprietary <Prtry> [1..1] Text 94
     Amount <Amt> [1..1] Amount C2, C8 94
   AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  94
     Amount <Amt> [1..1] Amount C2, C8 94
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 95
     Reason <Rsn> [0..1] Text 95
     AdditionalInformation <AddtlInf> [0..1] Text 95
Constraints
• RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
2.4.3.18.11.2.2.1  RemittanceAmountAndType <RmtAmtAndTp>
Presence: [0..*]
Definition: Type and amount of money for the referred document.
RemittanceAmountAndType <RmtAmtAndTp> contains the following DocumentAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  93
{Or     Code <Cd> [1..1] CodeSet 94
Or}     Proprietary <Prtry> [1..1] Text 94
   Amount <Amt> [1..1] Amount C2, C8 94
2.4.3.18.11.2.2.1.1  Type <Tp>
Presence: [1..1]
Definition: Defines the type of amount.
Type <Tp> contains one of the following DocumentAmountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 94
Or}   Proprietary <Prtry> [1..1] Text 94
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
93 March 2026
```

