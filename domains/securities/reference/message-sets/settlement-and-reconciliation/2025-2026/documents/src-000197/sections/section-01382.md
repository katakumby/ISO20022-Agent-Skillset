---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.10 SettlementDetails222", "35.1.26.10.21 EligibleForCollateral <ElgblForColl>"]
file_pages: [1850, 1851]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.10.21 EligibleForCollateral <ElgblForColl>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1850 to 1851.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1850

```text
CodeName Name Definition
PARC PartialSettlementCashThresholdAllowed Partial settlement is allowed but must
satisfy a cash value minimum (value
defined in static data).
PARQ PartialSettlementQuantityThresholdAllowed Partial settlement is allowed but must
satisfy a minimum quantity of securities
(quantity defined in static data).
35.1.26.10.21  EligibleForCollateral <ElgblForColl>
Presence: [0..1]
Definition: Specifies whether securities should be included in the pool of securities eligible for collateral
purposes.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.26.11  SettlementDetails221
Definition: Details of settlement of a transaction.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1850 March 2026
```

## File page 1851

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Priority <Prty> [0..1] ± 1852
   SecuritiesTransactionType <SctiesTxTp> [1..1] ± 1852
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1852
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 1852
   BeneficialOwnership <BnfclOwnrsh> [0..1] ± 1853
   BlockTrade <BlckTrad> [0..1] ± 1853
   CCPEligibility <CCPElgblty> [0..1] ± 1853
   CashClearingSystem <CshClrSys> [0..1] ± 1853
   ExposureType <XpsrTp> [0..1] ± 1854
   MarketClientSide <MktClntSd> [0..1] ± 1854
   NettingEligibility <NetgElgblty> [0..1] ± 1854
   Registration <Regn> [0..1] ± 1854
   RepurchaseType <RpTp> [0..1] ± 1855
   LegalRestrictions <LglRstrctns> [0..1] ± 1855
   SecuritiesRTGS <SctiesRTGS> [0..1] ± 1855
   SettlingCapacity <SttlgCpcty> [0..1] ± 1855
   SettlementSystemMethod <SttlmSysMtd> [0..1] ± 1856
   TaxCapacity <TaxCpcty> [0..1] ± 1856
   StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 1856
   AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 1857
   LetterOfGuarantee <LttrOfGrnt> [0..1] ± 1857
   EligibleForCollateral <ElgblForColl> [0..1] Indicator 1857
   SecuritiesSubBalanceType <SctiesSubBalTp> [0..1] ± 1857
   CashSubBalanceType <CshSubBalTp> [0..1] ± 1858
Constraints
• CashClearingSystemRule
The CashSettlementSystem codes are to be used only by agents directly involved in the settlement
process, such as local settlement agents, CSDs and central banks.
• SettlementDetailsRule
If SettlementDetails elements are used, then their conditions of use must be pre-agreed between
account owner and account servicer.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1851 March 2026
```

