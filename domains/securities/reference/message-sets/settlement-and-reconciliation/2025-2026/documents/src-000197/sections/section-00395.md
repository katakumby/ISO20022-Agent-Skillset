---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "18.4 Message Building Blocks", "18.4.4 InferredMatchingStatus <IfrrdMtchgSts>", "18.4.7.31 ReceivingSettlementParties <RcvgSttlmPties>"]
file_pages: [594, 595]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.024.001.14"]
---

# 18.4.7.31 ReceivingSettlementParties <RcvgSttlmPties>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 594 to 595.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 594

```text
SettlementParameters <SttlmParams> contains the following elements (see "SettlementDetails222"
on page 1843 for details)
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
18.4.7.31  ReceivingSettlementParties <RcvgSttlmPties>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 594 March 2026
```

## File page 595

```text
Definition: Identifies the chain of receiving settlement parties.
Impacted by: C20 "Party2PresenceRule", C21 "Party3PresenceRule", C22 "Party4PresenceRule", C23
"Party5PresenceRule"
ReceivingSettlementParties <RcvgSttlmPties> contains the following elements (see
"SettlementParties125" on page 1751 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1] ± 1752
   Party1 <Pty1> [0..1] ± C18,
C20
1752
   Party2 <Pty2> [0..1] ± C18,
C20
1753
   Party3 <Pty3> [0..1] ± C18,
C20
1753
   Party4 <Pty4> [0..1] ± C18,
C20
1754
   Party5 <Pty5> [0..1] ± C18,
C20
1755
Constraints
• Party2PresenceRule
If Party2 is present, then Party1 must be present.
On Condition
    /Party2 is present
Following Must be True
    /Party1 Must be present
• Party3PresenceRule
If Party3 is present, then Party2 must be present.
On Condition
    /Party3 is present
Following Must be True
    /Party2 Must be present
• Party4PresenceRule
If Party4 is present, then Party3 must be present.
On Condition
    /Party4 is present
Following Must be True
    /Party3 Must be present
• Party5PresenceRule
If Party5 is present, then Party4 must be present.
On Condition
    /Party5 is present
Following Must be True
    /Party4 Must be present
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 595 March 2026
```

