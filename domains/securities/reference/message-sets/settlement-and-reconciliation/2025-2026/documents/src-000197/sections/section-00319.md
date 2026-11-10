---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["14 sese.020.001.09 SecuritiesTransactionCancellationRequestV09", "14.4 Message Building Blocks", "14.4.9 TransactionDetails <TxDtls>", "14.4.9.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [466]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.020.001.09"]
---

# 14.4.9.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 466 to 466.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 466

```text
TransactionDetails <TxDtls> contains the following TransactionDetails180 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C7, C8,
C10,
C11,
C13
466
   TradeDate <TradDt> [0..1] ± 467
   SettlementDate <SttlmDt> [1..1] ± 468
   SettlementQuantity <SttlmQty> [1..1] ± 468
   SettlementAmount <SttlmAmt> [0..1] ± 468
   DigitalPaymentSettlement <DgtlPmtSttlm> [0..1]  469
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C7, C8,
C10,
C11,
C13
469
     ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 470
     CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  471
{Or       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 471
Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 471
Or}       LEI <LEI> [1..1] IdentifierSet 471
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C14,
C15,
C16,
C17
471
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C14,
C15,
C16,
C17
472
   Investor <Invstr> [0..1] ± 473
14.4.9.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C7 "DescriptionPresenceRule", C8 "DescriptionUsageRule", C10 "ISINGuideline", C11
"ISINPresenceRule", C13 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 sese.020.001.09
SecuritiesTransactionCancellationRequestV09
Settlement And Reconciliation - Maintenance 2025 - 2026 466 March 2026
```

