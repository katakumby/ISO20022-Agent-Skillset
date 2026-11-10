---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>", "3.4.3.7.12 OriginalTransactionReference <OrgnlTxRef>", "3.4.3.7.12.11 RemittanceInformation <RmtInf>", "3.4.3.7.12.11.2 Structured <Strd>", "3.4.3.7.12.11.2.1 ReferredDocumentInformation <RfrdDocInf>", "3.4.3.7.12.11.2.1.4 LineDetails <LineDtls>", "3.4.3.7.12.11.2.1.4.3 Amount <Amt>", "3.4.3.7.12.11.2.1.4.3.1 RemittanceAmountAndType <RmtAmtAndTp>"]
file_pages: [230]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.7.12.11.2.1.4.3.1 RemittanceAmountAndType <RmtAmtAndTp>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 230 to 230.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 230

```text
Amount <Amt> contains the following RemittanceAmount4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceAmountAndType <RmtAmtAndTp> [0..*]  230
     Type <Tp> [1..1]  230
{Or       Code <Cd> [1..1] CodeSet 231
Or}       Proprietary <Prtry> [1..1] Text 231
     Amount <Amt> [1..1] Amount C2, C8 231
   AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  231
     Amount <Amt> [1..1] Amount C2, C8 231
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 232
     Reason <Rsn> [0..1] Text 232
     AdditionalInformation <AddtlInf> [0..1] Text 232
Constraints
• RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
3.4.3.7.12.11.2.1.4.3.1  RemittanceAmountAndType <RmtAmtAndTp>
Presence: [0..*]
Definition: Type and amount of money for the referred document.
RemittanceAmountAndType <RmtAmtAndTp> contains the following DocumentAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  230
{Or     Code <Cd> [1..1] CodeSet 231
Or}     Proprietary <Prtry> [1..1] Text 231
   Amount <Amt> [1..1] Amount C2, C8 231
3.4.3.7.12.11.2.1.4.3.1.1  Type <Tp>
Presence: [1..1]
Definition: Defines the type of amount.
Type <Tp> contains one of the following DocumentAmountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 231
Or}   Proprietary <Prtry> [1..1] Text 231
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 230 March 2026
```

