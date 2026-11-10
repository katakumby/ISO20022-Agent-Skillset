---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.10 SettlementDetails222", "35.1.26.10.1 HoldIndicator <HldInd>"]
file_pages: [1844]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.10.1 HoldIndicator <HldInd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1844 to 1844.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1844

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldIndicator <HldInd> [0..1] ± 1844
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1845
   SecuritiesTransactionType <SctiesTxTp> [1..1] ± 1845
   SettlingCapacity <SttlgCpcty> [0..1] ± 1845
   StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 1845
   SecuritiesRTGS <SctiesRTGS> [0..1] ± 1846
   Registration <Regn> [0..1] ± 1846
   BeneficialOwnership <BnfclOwnrsh> [0..1] ± 1846
   ExposureType <XpsrTp> [0..1] ± 1847
   CashClearingSystem <CshClrSys> [0..1] ± 1847
   TaxCapacity <TaxCpcty> [0..1] ± 1847
   RepurchaseType <RpTp> [0..1] ± 1847
   MarketClientSide <MktClntSd> [0..1] ± 1848
   BlockTrade <BlckTrad> [0..1] ± 1848
   LegalRestrictions <LglRstrctns> [0..1] ± 1848
   SettlementSystemMethod <SttlmSysMtd> [0..1] ± 1848
   NettingEligibility <NetgElgblty> [0..1] ± 1849
   CCPEligibility <CCPElgblty> [0..1] ± 1849
   LetterOfGuarantee <LttrOfGrnt> [0..1] ± 1849
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 1849
   EligibleForCollateral <ElgblForColl> [0..1] Indicator 1850
Constraints
• CashClearingSystemRule
The CashSettlementSystem codes are to be used only by agents directly involved in the settlement
process, such as local settlement agents, CSDs and central banks.
• SettlementDetailsRule
If SettlementDetails elements are used, then their conditions of use must be pre-agreed between
account owner and account servicer.
35.1.26.10.1  HoldIndicator <HldInd>
Presence: [0..1]
Definition: Specifies whether the transaction is on hold/blocked/frozen.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1844 March 2026
```

