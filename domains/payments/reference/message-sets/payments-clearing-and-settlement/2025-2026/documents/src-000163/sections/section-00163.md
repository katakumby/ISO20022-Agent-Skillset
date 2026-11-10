---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.2 DirectDebitTransactionInformation <DrctDbtTxInf>", "3.4.2.35 RemittanceInformation <RmtInf>", "3.4.2.35.2 Structured <Strd>", "3.4.2.35.2.2 ReferredDocumentAmount <RfrdDocAmt>", "3.4.2.35.2.2.1 RemittanceAmountAndType <RmtAmtAndTp>"]
file_pages: [221]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.2.35.2.2.1 RemittanceAmountAndType <RmtAmtAndTp>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 221 to 221.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 221

```text
ReferredDocumentAmount <RfrdDocAmt> contains the following RemittanceAmount4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceAmountAndType <RmtAmtAndTp> [0..*]  221
     Type <Tp> [1..1]  221
{Or       Code <Cd> [1..1] CodeSet 222
Or}       Proprietary <Prtry> [1..1] Text 222
     Amount <Amt> [1..1] Amount C2, C11 222
   AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  222
     Amount <Amt> [1..1] Amount C2, C11 222
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 223
     Reason <Rsn> [0..1] Text 223
     AdditionalInformation <AddtlInf> [0..1] Text 223
Constraints
• RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
3.4.2.35.2.2.1  RemittanceAmountAndType <RmtAmtAndTp>
Presence: [0..*]
Definition: Type and amount of money for the referred document.
RemittanceAmountAndType <RmtAmtAndTp> contains the following DocumentAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  221
{Or     Code <Cd> [1..1] CodeSet 222
Or}     Proprietary <Prtry> [1..1] Text 222
   Amount <Amt> [1..1] Amount C2, C11 222
3.4.2.35.2.2.1.1  Type <Tp>
Presence: [1..1]
Definition: Defines the type of amount.
Type <Tp> contains one of the following DocumentAmountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 222
Or}   Proprietary <Prtry> [1..1] Text 222
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
221 March 2026
```

