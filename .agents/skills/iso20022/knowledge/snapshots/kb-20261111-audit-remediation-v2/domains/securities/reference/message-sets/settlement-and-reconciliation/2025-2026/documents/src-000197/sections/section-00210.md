---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.4 Message Building Blocks", "9.4.6 Status <Sts>", "9.4.6.2 Transaction <Tx>", "9.4.6.2.15 TransactionDetails <TxDtls>", "9.4.6.2.15.6 PlaceOfTrade <PlcOfTrad>"]
file_pages: [316]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.4.6.2.15.6 PlaceOfTrade <PlcOfTrad>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 316 to 316.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 316

```text
SettlementParameters <SttlmParams> contains the following elements (see "SettlementDetails232"
on page 1795 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldIndicator <HldInd> [0..1] ± 1796
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1797
   SettlingCapacity <SttlgCpcty> [0..1] ± 1797
   StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 1797
   SecuritiesRTGS <SctiesRTGS> [0..1] ± 1797
   Registration <Regn> [0..1] ± 1798
   BeneficialOwnership <BnfclOwnrsh> [0..1] ± 1798
   CashClearingSystem <CshClrSys> [0..1] ± 1798
   TaxCapacity <TaxCpcty> [0..1] ± 1799
   RepurchaseType <RpTp> [0..1] ± 1799
   MarketClientSide <MktClntSd> [0..1] ± 1799
   BlockTrade <BlckTrad> [0..1] ± 1799
   LegalRestrictions <LglRstrctns> [0..1] ± 1800
   SettlementSystemMethod <SttlmSysMtd> [0..1] ± 1800
   NettingEligibility <NetgElgblty> [0..1] ± 1800
   CCPEligibility <CCPElgblty> [0..1] ± 1800
   LetterOfGuarantee <LttrOfGrnt> [0..1] ± 1801
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 1801
Constraints
• CashClearingSystemRule
The CashSettlementSystem codes are to be used only by agents directly involved in the settlement
process, such as local settlement agents, CSD's and central banks.
• SettlementDetailsRule
If SettlementDetails elements are used, then their conditions of use must be pre-agreed between
account owner and account servicer.
9.4.6.2.15.6  PlaceOfTrade <PlcOfTrad>
Presence: [0..1]
Definition: Market in which a trade transaction has been executed.
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 316 March 2026
```

