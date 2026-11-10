---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.3 SettlementDetails232", "35.1.26.3.1 HoldIndicator <HldInd>"]
file_pages: [1796]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.3.1 HoldIndicator <HldInd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1796 to 1796.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1796

```text
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
35.1.26.3.1  HoldIndicator <HldInd>
Presence: [0..1]
Definition: Specifies whether the transaction is on hold/blocked/frozen.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1796 March 2026
```

