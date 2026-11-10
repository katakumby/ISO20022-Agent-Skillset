---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.26 RemittanceInformation <RmtInf>", "2.4.2.19.26.2 Structured <Strd>", "2.4.2.19.26.2.2 ReferredDocumentAmount <RfrdDocAmt>", "2.4.2.19.26.2.2.1 RemittanceAmountAndType <RmtAmtAndTp>"]
file_pages: [105]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.26.2.2.1 RemittanceAmountAndType <RmtAmtAndTp>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 105 to 105.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 105

```text
ReferredDocumentAmount <RfrdDocAmt> contains the following RemittanceAmount4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceAmountAndType <RmtAmtAndTp> [0..*]  105
     Type <Tp> [1..1]  105
{Or       Code <Cd> [1..1] CodeSet 106
Or}       Proprietary <Prtry> [1..1] Text 106
     Amount <Amt> [1..1] Amount C2, C19 106
   AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  106
     Amount <Amt> [1..1] Amount C2, C19 106
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 107
     Reason <Rsn> [0..1] Text 107
     AdditionalInformation <AddtlInf> [0..1] Text 107
Constraints
• RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
2.4.2.19.26.2.2.1  RemittanceAmountAndType <RmtAmtAndTp>
Presence: [0..*]
Definition: Type and amount of money for the referred document.
RemittanceAmountAndType <RmtAmtAndTp> contains the following DocumentAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  105
{Or     Code <Cd> [1..1] CodeSet 106
Or}     Proprietary <Prtry> [1..1] Text 106
   Amount <Amt> [1..1] Amount C2, C19 106
2.4.2.19.26.2.2.1.1  Type <Tp>
Presence: [1..1]
Definition: Defines the type of amount.
Type <Tp> contains one of the following DocumentAmountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 106
Or}   Proprietary <Prtry> [1..1] Text 106
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 105 March 2026
```

