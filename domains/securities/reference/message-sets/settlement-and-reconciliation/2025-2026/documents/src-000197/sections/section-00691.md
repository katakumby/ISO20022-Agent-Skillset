---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["29 sese.035.001.13 SecuritiesFinancingConfirmationV13", "29.4 Message Building Blocks", "29.4.9 SettlementParameters <SttlmParams>"]
file_pages: [1038]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.035.001.13"]
---

# 29.4.9 SettlementParameters <SttlmParams>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1038 to 1038.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1038

```text
29.4.9 SettlementParameters <SttlmParams>
Presence: [0..1]
Definition: Parameters which explicitly state the conditions that must be fulfilled before a particular
transaction of a financial instrument can be settled. These parameters are defined by the instructing
party in compliance with settlement rules in the market the transaction will settle in.
Impacted by: C11 "CashClearingSystemRule", C52 "SettlementDetailsRule"
SettlementParameters <SttlmParams> contains the following SettlementDetails228 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Priority <Prty> [0..1] ± 1038
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1039
   SettlingCapacity <SttlgCpcty> [0..1] ± 1039
   StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 1039
   SecuritiesRTGS <SctiesRTGS> [0..1] ± 1040
   BeneficialOwnership <BnfclOwnrsh> [0..1] ± 1040
   CashClearingSystem <CshClrSys> [0..1] ± 1040
   TaxCapacity <TaxCpcty> [0..1] ± 1040
   MarketClientSide <MktClntSd> [0..1] ± 1041
   BlockTrade <BlckTrad> [0..1] ± 1041
   LegalRestrictions <LglRstrctns> [0..1] ± 1041
   SettlementSystemMethod <SttlmSysMtd> [0..1] ± 1041
   NettingEligibility <NetgElgblty> [0..1] ± 1042
   CCPEligibility <CCPElgblty> [0..1] ± 1042
   AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 1042
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 1043
   EligibleForCollateral <ElgblForColl> [0..1] Indicator 1043
Constraints
• CashClearingSystemRule
The CashSettlementSystem codes are to be used only by agents directly involved in the settlement
process, such as local settlement agents, CSD's and central banks.
• SettlementDetailsRule
If SettlementDetails elements are used, then their conditions of use must be pre-agreed between
account owner and account servicer.
29.4.9.1  Priority <Prty>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 1038 March 2026
```

