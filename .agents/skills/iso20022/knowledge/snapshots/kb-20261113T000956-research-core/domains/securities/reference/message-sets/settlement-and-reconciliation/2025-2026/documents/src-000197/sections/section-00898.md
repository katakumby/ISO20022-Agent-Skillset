---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06", "34.4 Message Building Blocks", "34.4.3 TransactionDetails <TxDtls>", "34.4.3.8 DigitalPaymentSettlement <DgtlPmtSttlm>"]
file_pages: [1333]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.040.001.06"]
---

# 34.4.3.8 DigitalPaymentSettlement <DgtlPmtSttlm>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1333 to 1333.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1333

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
34.4.3.8  DigitalPaymentSettlement <DgtlPmtSttlm>
Presence: [0..1]
Definition: Total quantity of digital asset to be paid or received in exchange for the securities token.
DigitalPaymentSettlement <DgtlPmtSttlm> contains the following DigitalPaymentSettlement2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C7, C8,
C10,
C11,
C12
1333
   ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 1334
   CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  1335
{Or     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1335
Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1335
Or}     LEI <LEI> [1..1] IdentifierSet 1335
34.4.3.8.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C7 "DescriptionPresenceRule", C8 "DescriptionUsageRule", C10 "ISINGuideline", C11
"ISINPresenceRule", C12 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 sese.040.001.06
SecuritiesSettlementTransactionCounterpartyRespo
nseV06
Settlement And Reconciliation - Maintenance 2025 - 2026 1333 March 2026
```

