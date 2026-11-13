---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.1 ModifiedTransactionDetails <ModfdTxDtls>", "32.4.1.9 TransactionDetails <TxDtls>", "32.4.1.9.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [1160]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.1.9.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1160 to 1160.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1160

```text
TransactionDetails <TxDtls> contains the following TransactionDetails180 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C21,
C22,
C29,
C30,
C40
1160
   TradeDate <TradDt> [0..1] ± 1161
   SettlementDate <SttlmDt> [1..1] ± 1162
   SettlementQuantity <SttlmQty> [1..1] ± 1162
   SettlementAmount <SttlmAmt> [0..1] ± 1162
   DigitalPaymentSettlement <DgtlPmtSttlm> [0..1]  1163
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C21,
C22,
C29,
C30,
C40
1163
     ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 1164
     CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  1164
{Or       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1164
Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C8 1165
Or}       LEI <LEI> [1..1] IdentifierSet 1165
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C41,
C43,
C46,
C49
1165
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C41,
C43,
C46,
C49
1166
   Investor <Invstr> [0..1] ± 1167
32.4.1.9.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C21 "DescriptionPresenceRule", C22 "DescriptionUsageRule", C29 "ISINGuideline", C30
"ISINPresenceRule", C40 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1160 March 2026
```

