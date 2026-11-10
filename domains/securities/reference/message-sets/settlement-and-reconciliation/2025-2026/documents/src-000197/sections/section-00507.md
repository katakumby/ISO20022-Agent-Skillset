---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["23 sese.029.001.08 SecuritiesSettlementAllegementRemovalAdviceV08", "23.4 Message Building Blocks", "23.4.7 TransactionDetails <TxDtls>", "23.4.7.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [774]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.029.001.08"]
---

# 23.4.7.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 774 to 774.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 774

```text
TransactionDetails <TxDtls> contains the following TransactionDetails179 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C7, C8,
C10,
C11,
C12
774
   TradeDate <TradDt> [0..1] ± 775
   SettlementDate <SttlmDt> [1..1] ± 776
   SettlementQuantity <SttlmQty> [1..1] ± 776
   SettlementAmount <SttlmAmt> [0..1] ± 776
   DigitalPaymentSettlement <DgtlPmtSttlm> [0..1]  777
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C7, C8,
C10,
C11,
C12
777
     ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 778
     CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  779
{Or       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 779
Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 779
Or}       LEI <LEI> [1..1] IdentifierSet 779
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C13,
C14,
C15,
C16
779
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C13,
C14,
C15,
C16
780
   Investor <Invstr> [0..1] ± 781
23.4.7.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instruments representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C7 "DescriptionPresenceRule", C8 "DescriptionUsageRule", C10 "ISINGuideline", C11
"ISINPresenceRule", C12 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 sese.029.001.08
SecuritiesSettlementAllegementRemovalAdviceV08
Settlement And Reconciliation - Maintenance 2025 - 2026 774 March 2026
```

