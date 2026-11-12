---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.4 SettlementDetails231", "35.1.26.4.1 SettlementTransactionCondition <SttlmTxCond>"]
file_pages: [1802]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.4.1 SettlementTransactionCondition <SttlmTxCond>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1802 to 1802.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1802

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1802
   SettlingCapacity <SttlgCpcty> [0..1] ± 1803
   StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 1803
   SecuritiesRTGS <SctiesRTGS> [0..1] ± 1803
   Registration <Regn> [0..1] ± 1803
   BeneficialOwnership <BnfclOwnrsh> [0..1] ± 1804
   CashClearingSystem <CshClrSys> [0..1] ± 1804
   TaxCapacity <TaxCpcty> [0..1] ± 1804
   RepurchaseType <RpTp> [0..1] ± 1804
   MarketClientSide <MktClntSd> [0..1] ± 1805
   BlockTrade <BlckTrad> [0..1] ± 1805
   LegalRestrictions <LglRstrctns> [0..1] ± 1805
   SettlementSystemMethod <SttlmSysMtd> [0..1] ± 1805
   NettingEligibility <NetgElgblty> [0..1] ± 1806
   CCPEligibility <CCPElgblty> [0..1] ± 1806
   LetterOfGuarantee <LttrOfGrnt> [0..1] ± 1806
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 1807
Constraints
• CashClearingSystemRule
The CashSettlementSystem codes are to be used only by agents directly involved in the settlement
process, such as local settlement agents, CSD's and central banks.
• SettlementDetailsRule
If SettlementDetails elements are used, then their conditions of use must be pre-agreed between
account owner and account servicer.
35.1.26.4.1  SettlementTransactionCondition <SttlmTxCond>
Presence: [0..*]
Definition: Conditions under which the order/trade is to be settled.
SettlementTransactionCondition <SttlmTxCond> contains one of the following elements (see
"SettlementTransactionCondition41Choice" on page 1641 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1641
Or}   Proprietary <Prtry> [1..1] ± 1642
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1802 March 2026
```

