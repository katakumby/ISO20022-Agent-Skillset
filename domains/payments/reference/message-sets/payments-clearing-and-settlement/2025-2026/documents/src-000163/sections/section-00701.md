---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.40 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "7.4.2.40.30 RemittanceInformation <RmtInf>", "7.4.2.40.30.2 Structured <Strd>", "7.4.2.40.30.2.1 ReferredDocumentInformation <RfrdDocInf>", "7.4.2.40.30.2.1.4 LineDetails <LineDtls>", "7.4.2.40.30.2.1.4.3 Amount <Amt>", "7.4.2.40.30.2.1.4.3.1 RemittanceAmountAndType <RmtAmtAndTp>"]
file_pages: [956]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.40.30.2.1.4.3.1 RemittanceAmountAndType <RmtAmtAndTp>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 956 to 956.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 956

```text
Amount <Amt> contains the following RemittanceAmount4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceAmountAndType <RmtAmtAndTp> [0..*]  956
     Type <Tp> [1..1]  956
{Or       Code <Cd> [1..1] CodeSet 957
Or}       Proprietary <Prtry> [1..1] Text 957
     Amount <Amt> [1..1] Amount C2, C9 957
   AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  957
     Amount <Amt> [1..1] Amount C2, C9 957
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 958
     Reason <Rsn> [0..1] Text 958
     AdditionalInformation <AddtlInf> [0..1] Text 958
Constraints
• RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
7.4.2.40.30.2.1.4.3.1  RemittanceAmountAndType <RmtAmtAndTp>
Presence: [0..*]
Definition: Type and amount of money for the referred document.
RemittanceAmountAndType <RmtAmtAndTp> contains the following DocumentAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  956
{Or     Code <Cd> [1..1] CodeSet 957
Or}     Proprietary <Prtry> [1..1] Text 957
   Amount <Amt> [1..1] Amount C2, C9 957
7.4.2.40.30.2.1.4.3.1.1  Type <Tp>
Presence: [1..1]
Definition: Defines the type of amount.
Type <Tp> contains one of the following DocumentAmountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 957
Or}   Proprietary <Prtry> [1..1] Text 957
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
956 March 2026
```

