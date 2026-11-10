---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["27 sese.033.001.13 SecuritiesFinancingInstructionV13", "27.4 Message Building Blocks", "27.4.9 SecuritiesFinancingDetails <SctiesFincgDtls>", "27.4.9.27 TerminationAmountPerPieceOfCollateral <TermntnAmtPerPcOfColl>"]
file_pages: [923, 924]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.033.001.13"]
---

# 27.4.9.27 TerminationAmountPerPieceOfCollateral <TermntnAmtPerPcOfColl>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 923 to 924.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 923

```text
27.4.9.27  TerminationAmountPerPieceOfCollateral <TermntnAmtPerPcOfColl>
Presence: [0..1]
Definition: Amount of money to be settled per piece of collateral to terminate the transaction.
TerminationAmountPerPieceOfCollateral <TermntnAmtPerPcOfColl> contains the following
elements (see "AmountAndDirection21" on page 1377 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1377
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1377
27.4.9.28  TerminationTransactionAmount <TermntnTxAmt>
Presence: [0..1]
Definition: Total amount of money to be settled to terminate the transaction.
TerminationTransactionAmount <TermntnTxAmt> contains the following elements (see
"AmountAndDirection21" on page 1377 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1377
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1377
27.4.9.29  SecondLegNarrative <ScndLegNrrtv>
Presence: [0..1]
Definition: Provides additional information about the second leg in narrative form.
Datatype: "Max140Text" on page 2191
27.4.10 SettlementParameters <SttlmParams>
Presence: [0..1]
Definition: Parameters which explicitly state the conditions that must be fulfilled before a particular
transaction of a financial instrument can be settled. These parameters are defined by the instructing
party in compliance with settlement rules in the market the transaction will settle in.
Impacted by: C13 "CashClearingSystemRule", C27 "FXStandingInstructionPresenceRule", C64
"SettlementDetailsRule"
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 923 March 2026
```

## File page 924

```text
SettlementParameters <SttlmParams> contains the following SettlementDetails226 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldIndicator <HldInd> [0..1] Indicator 925
   Priority <Prty> [0..1] ± 925
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 925
   SettlingCapacity <SttlgCpcty> [0..1] ± 925
   StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 925
   SecuritiesRTGS <SctiesRTGS> [0..1] ± 926
   BeneficialOwnership <BnfclOwnrsh> [0..1] ± 926
   CashClearingSystem <CshClrSys> [0..1] ± 926
   TaxCapacity <TaxCpcty> [0..1] ± 927
   MarketClientSide <MktClntSd> [0..1] ± 927
   FXStandingInstruction <FxStgInstr> [0..1] ± 927
   BlockTrade <BlckTrad> [0..1] ± 927
   LegalRestrictions <LglRstrctns> [0..1] ± 928
   SettlementSystemMethod <SttlmSysMtd> [0..1] ± 928
   NettingEligibility <NetgElgblty> [0..1] ± 928
   CCPEligibility <CCPElgblty> [0..1] ± 928
   Tracking <Trckg> [0..1] ± 929
   AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 929
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 929
   EligibleForCollateral <ElgblForColl> [0..1] Indicator 930
Constraints
• CashClearingSystemRule
The CashSettlementSystem codes are to be used only by agents directly involved in the settlement
process, such as local settlement agents, CSD's and central banks.
• FXStandingInstructionPresenceRule
If HoldIndicator is present and is value TRUE (Yes), then FXStandingInstruction must be absent.
On Condition
    /HoldIndicator is present
 And    /HoldIndicator is equal to value 'true'
Following Must be True
    /FXStandingInstruction Must be absent
• SettlementDetailsRule
If SettlementDetails elements are used, then their conditions of use must be pre-agreed between
account owner and account servicer.
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 924 March 2026
```

