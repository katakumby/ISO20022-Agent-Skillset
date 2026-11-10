---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["14 sese.020.001.09 SecuritiesTransactionCancellationRequestV09", "14.4 Message Building Blocks", "14.4.9 TransactionDetails <TxDtls>", "14.4.9.6 DigitalPaymentSettlement <DgtlPmtSttlm>"]
file_pages: [469]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.020.001.09"]
---

# 14.4.9.6 DigitalPaymentSettlement <DgtlPmtSttlm>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 469 to 469.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 469

```text
SettlementAmount <SttlmAmt> contains the following elements (see "AmountAndDirection51" on
page 1387 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C9 1387
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 1387
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C8 1388
14.4.9.6  DigitalPaymentSettlement <DgtlPmtSttlm>
Presence: [0..1]
Definition: Amount of digital asset that is to be/was posted to the account as a means of payment.
DigitalPaymentSettlement <DgtlPmtSttlm> contains the following DigitalPaymentSettlement2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C7, C8,
C10,
C11,
C13
469
   ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 470
   CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  471
{Or     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 471
Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C3 471
Or}     LEI <LEI> [1..1] IdentifierSet 471
14.4.9.6.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C7 "DescriptionPresenceRule", C8 "DescriptionUsageRule", C10 "ISINGuideline", C11
"ISINPresenceRule", C13 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 sese.020.001.09
SecuritiesTransactionCancellationRequestV09
Settlement And Reconciliation - Maintenance 2025 - 2026 469 March 2026
```

