---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.17 RemittanceInformation <RmtInf>", "5.4.2.18.17.2 Structured <Strd>", "5.4.2.18.17.2.2 ReferredDocumentAmount <RfrdDocAmt>", "5.4.2.18.17.2.2.1 RemittanceAmountAndType <RmtAmtAndTp>"]
file_pages: [502]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.17.2.2.1 RemittanceAmountAndType <RmtAmtAndTp>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 502 to 502.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 502

```text
ReferredDocumentAmount <RfrdDocAmt> contains the following RemittanceAmount4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceAmountAndType <RmtAmtAndTp> [0..*]  502
     Type <Tp> [1..1]  502
{Or       Code <Cd> [1..1] CodeSet 503
Or}       Proprietary <Prtry> [1..1] Text 503
     Amount <Amt> [1..1] Amount C2, C12 503
   AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  503
     Amount <Amt> [1..1] Amount C2, C12 503
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 504
     Reason <Rsn> [0..1] Text 504
     AdditionalInformation <AddtlInf> [0..1] Text 504
Constraints
• RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
5.4.2.18.17.2.2.1  RemittanceAmountAndType <RmtAmtAndTp>
Presence: [0..*]
Definition: Type and amount of money for the referred document.
RemittanceAmountAndType <RmtAmtAndTp> contains the following DocumentAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  502
{Or     Code <Cd> [1..1] CodeSet 503
Or}     Proprietary <Prtry> [1..1] Text 503
   Amount <Amt> [1..1] Amount C2, C12 503
5.4.2.18.17.2.2.1.1  Type <Tp>
Presence: [1..1]
Definition: Defines the type of amount.
Type <Tp> contains one of the following DocumentAmountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 503
Or}   Proprietary <Prtry> [1..1] Text 503
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 502 March 2026
```

