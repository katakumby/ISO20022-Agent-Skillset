---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.11 RemittanceInformation <RmtInf>", "4.4.3.27.11.2 Structured <Strd>", "4.4.3.27.11.2.1 ReferredDocumentInformation <RfrdDocInf>", "4.4.3.27.11.2.1.4 LineDetails <LineDtls>", "4.4.3.27.11.2.1.4.3 Amount <Amt>", "4.4.3.27.11.2.1.4.3.1 RemittanceAmountAndType <RmtAmtAndTp>"]
file_pages: [406]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.11.2.1.4.3.1 RemittanceAmountAndType <RmtAmtAndTp>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 406 to 406.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 406

```text
Amount <Amt> contains the following RemittanceAmount4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceAmountAndType <RmtAmtAndTp> [0..*]  406
     Type <Tp> [1..1]  406
{Or       Code <Cd> [1..1] CodeSet 407
Or}       Proprietary <Prtry> [1..1] Text 407
     Amount <Amt> [1..1] Amount C2, C12 407
   AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  407
     Amount <Amt> [1..1] Amount C2, C12 407
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 408
     Reason <Rsn> [0..1] Text 408
     AdditionalInformation <AddtlInf> [0..1] Text 408
Constraints
• RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
4.4.3.27.11.2.1.4.3.1  RemittanceAmountAndType <RmtAmtAndTp>
Presence: [0..*]
Definition: Type and amount of money for the referred document.
RemittanceAmountAndType <RmtAmtAndTp> contains the following DocumentAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  406
{Or     Code <Cd> [1..1] CodeSet 407
Or}     Proprietary <Prtry> [1..1] Text 407
   Amount <Amt> [1..1] Amount C2, C12 407
4.4.3.27.11.2.1.4.3.1.1  Type <Tp>
Presence: [1..1]
Definition: Defines the type of amount.
Type <Tp> contains one of the following DocumentAmountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 407
Or}   Proprietary <Prtry> [1..1] Text 407
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
406 March 2026
```

