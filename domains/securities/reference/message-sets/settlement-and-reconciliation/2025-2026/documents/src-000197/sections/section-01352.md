---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.6 SettlementDetails227", "35.1.26.6.1 HoldIndicator <HldInd>"]
file_pages: [1817]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.6.1 HoldIndicator <HldInd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1817 to 1817.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1817

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldIndicator <HldInd> [0..1] Indicator 1817
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1817
   SettlingCapacity <SttlgCpcty> [0..1] ± 1818
   StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 1818
   SecuritiesRTGS <SctiesRTGS> [0..1] ± 1818
   BeneficialOwnership <BnfclOwnrsh> [0..1] ± 1819
   CashClearingSystem <CshClrSys> [0..1] ± 1819
   TaxCapacity <TaxCpcty> [0..1] ± 1819
   MarketClientSide <MktClntSd> [0..1] ± 1819
   BlockTrade <BlckTrad> [0..1] ± 1820
   LegalRestrictions <LglRstrctns> [0..1] ± 1820
   SettlementSystemMethod <SttlmSysMtd> [0..1] ± 1820
   NettingEligibility <NetgElgblty> [0..1] ± 1820
   CCPEligibility <CCPElgblty> [0..1] ± 1821
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 1821
   EligibleForCollateral <ElgblForColl> [0..1] Indicator 1821
Constraints
• CashClearingSystemRule
The CashSettlementSystem codes are to be used only by agents directly involved in the settlement
process, such as local settlement agents, CSDs and central banks.
• SettlementDetailsRule
If SettlementDetails elements are used, then their conditions of use must be pre-agreed between
account owner and account servicer.
35.1.26.6.1  HoldIndicator <HldInd>
Presence: [0..1]
Definition: Indicates whether the transaction is on hold/blocked/frozen.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.26.6.2  SettlementTransactionCondition <SttlmTxCond>
Presence: [0..*]
Definition: Conditions under which the order/trade is to be settled.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1817 March 2026
```

