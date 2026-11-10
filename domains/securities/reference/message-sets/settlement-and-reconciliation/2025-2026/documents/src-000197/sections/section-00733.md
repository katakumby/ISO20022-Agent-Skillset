---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10", "30.4 Message Building Blocks", "30.4.10 OpeningDigitalSettlementAmount <OpngDgtlSttlmAmt>"]
file_pages: [1090]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.036.001.10"]
---

# 30.4.10 OpeningDigitalSettlementAmount <OpngDgtlSttlmAmt>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1090 to 1090.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1090

```text
OpeningSettlementAmount <OpngSttlmAmt> contains the following elements (see
"AmountAndDirection49" on page 1360 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C9 1360
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1360
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C8 1361
   ForeignExchangeDetails <FXDtls> [0..1] ± 1361
30.4.10 OpeningDigitalSettlementAmount
<OpngDgtlSttlmAmt>
Presence: [0..1]
Definition: Amount of digital asset that is to be/was posted to the account as a means of payment.
OpeningDigitalSettlementAmount <OpngDgtlSttlmAmt> contains the following
DigitalPaymentSettlement2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C12,
C13,
C17,
C18,
C20
1090
   ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 1091
   CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  1092
{Or     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1092
Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1092
Or}     LEI <LEI> [1..1] IdentifierSet 1092
30.4.10.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C12 "DescriptionPresenceRule", C13 "DescriptionUsageRule", C17 "ISINGuideline", C18
"ISINPresenceRule", C20 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 sese.036.001.10
SecuritiesFinancingModificationInstructionV10
Settlement And Reconciliation - Maintenance 2025 - 2026 1090 March 2026
```

