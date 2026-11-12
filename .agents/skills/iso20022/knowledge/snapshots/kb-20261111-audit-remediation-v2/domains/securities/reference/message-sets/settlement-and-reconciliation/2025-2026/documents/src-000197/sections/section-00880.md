---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08", "33.4 Message Building Blocks", "33.4.7 TransactionDetails <TxDtls>", "33.4.7.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [1313]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.039.001.08"]
---

# 33.4.7.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1313 to 1313.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1313

```text
TransactionDetails <TxDtls> contains the following TransactionDetails182 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C9, C10,
C12,
C13,
C15
1313
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 1314
   Payment <Pmt> [1..1] CodeSet 1315
   SettlementQuantity <SttlmQty> [1..1] ± 1315
   SettlementAmount <SttlmAmt> [0..1] ± 1315
   DigitalPaymentSettlement <DgtlPmtSttlm> [0..1]  1316
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C9, C10,
C12,
C13,
C15
1316
     ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 1317
     CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  1317
{Or       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1317
Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1318
Or}       LEI <LEI> [1..1] IdentifierSet 1318
   SettlementDate <SttlmDt> [1..1] ± 1318
   TradeDate <TradDt> [0..1] ± 1318
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C16,
C17,
C18,
C19
1319
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C16,
C17,
C18,
C19
1320
   Investor <Invstr> [0..1] ± 1321
33.4.7.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instruments representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C9 "DescriptionPresenceRule", C10 "DescriptionUsageRule", C12 "ISINGuideline", C13
"ISINPresenceRule", C15 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 sese.039.001.08
SecuritiesSettlementTransactionModificationReques
tStatusAdviceV08
Settlement And Reconciliation - Maintenance 2025 - 2026 1313 March 2026
```

