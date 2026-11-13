---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.3 TransactionInformation <TxInf>", "5.4.3.21 OriginalTransactionReference <OrgnlTxRef>", "5.4.3.21.11 RemittanceInformation <RmtInf>", "5.4.3.21.11.2 Structured <Strd>", "5.4.3.21.11.2.1 ReferredDocumentInformation <RfrdDocInf>", "5.4.3.21.11.2.1.4 LineDetails <LineDtls>", "5.4.3.21.11.2.1.4.3 Amount <Amt>", "5.4.3.21.11.2.1.4.3.1 RemittanceAmountAndType <RmtAmtAndTp>"]
file_pages: [660]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.3.21.11.2.1.4.3.1 RemittanceAmountAndType <RmtAmtAndTp>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 660 to 660.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 660

```text
Amount <Amt> contains the following RemittanceAmount4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceAmountAndType <RmtAmtAndTp> [0..*]  660
     Type <Tp> [1..1]  660
{Or       Code <Cd> [1..1] CodeSet 661
Or}       Proprietary <Prtry> [1..1] Text 661
     Amount <Amt> [1..1] Amount C2, C11 661
   AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  661
     Amount <Amt> [1..1] Amount C2, C11 661
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 662
     Reason <Rsn> [0..1] Text 662
     AdditionalInformation <AddtlInf> [0..1] Text 662
Constraints
• RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
5.4.3.21.11.2.1.4.3.1  RemittanceAmountAndType <RmtAmtAndTp>
Presence: [0..*]
Definition: Type and amount of money for the referred document.
RemittanceAmountAndType <RmtAmtAndTp> contains the following DocumentAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  660
{Or     Code <Cd> [1..1] CodeSet 661
Or}     Proprietary <Prtry> [1..1] Text 661
   Amount <Amt> [1..1] Amount C2, C11 661
5.4.3.21.11.2.1.4.3.1.1  Type <Tp>
Presence: [1..1]
Definition: Defines the type of amount.
Type <Tp> contains one of the following DocumentAmountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 661
Or}   Proprietary <Prtry> [1..1] Text 661
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
660 March 2026
```

