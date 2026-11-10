---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.2.47 RemittanceInformation <RmtInf>", "6.4.2.47.2 Structured <Strd>", "6.4.2.47.2.1 ReferredDocumentInformation <RfrdDocInf>", "6.4.2.47.2.1.4 LineDetails <LineDtls>", "6.4.2.47.2.1.4.3 Amount <Amt>", "6.4.2.47.2.1.4.3.1 RemittanceAmountAndType <RmtAmtAndTp>"]
file_pages: [802]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.2.47.2.1.4.3.1 RemittanceAmountAndType <RmtAmtAndTp>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 802 to 802.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 802

```text
Amount <Amt> contains the following RemittanceAmount4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceAmountAndType <RmtAmtAndTp> [0..*]  802
     Type <Tp> [1..1]  802
{Or       Code <Cd> [1..1] CodeSet 803
Or}       Proprietary <Prtry> [1..1] Text 803
     Amount <Amt> [1..1] Amount C2, C12 803
   AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  803
     Amount <Amt> [1..1] Amount C2, C12 803
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 804
     Reason <Rsn> [0..1] Text 804
     AdditionalInformation <AddtlInf> [0..1] Text 804
Constraints
• RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
6.4.2.47.2.1.4.3.1  RemittanceAmountAndType <RmtAmtAndTp>
Presence: [0..*]
Definition: Type and amount of money for the referred document.
RemittanceAmountAndType <RmtAmtAndTp> contains the following DocumentAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  802
{Or     Code <Cd> [1..1] CodeSet 803
Or}     Proprietary <Prtry> [1..1] Text 803
   Amount <Amt> [1..1] Amount C2, C12 803
6.4.2.47.2.1.4.3.1.1  Type <Tp>
Presence: [1..1]
Definition: Defines the type of amount.
Type <Tp> contains one of the following DocumentAmountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 803
Or}   Proprietary <Prtry> [1..1] Text 803
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
802 March 2026
```

