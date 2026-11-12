---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10", "30.4 Message Building Blocks", "30.4.5 SecuritiesFinancingAdditionalDetails <SctiesFincgAddtlDtls>", "30.4.5.28 TerminationAmountPerPieceOfCollateral <TermntnAmtPerPcOfColl>"]
file_pages: [1079, 1080]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.036.001.10"]
---

# 30.4.5.28 TerminationAmountPerPieceOfCollateral <TermntnAmtPerPcOfColl>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1079 to 1080.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1079

```text
Definition: Difference between the amount of money of the first leg and the amount of the second leg of
the transaction.
PremiumAmount <PrmAmt> contains the following elements (see "AmountAndDirection21" on
page 1377 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1377
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1377
30.4.5.28  TerminationAmountPerPieceOfCollateral <TermntnAmtPerPcOfColl>
Presence: [0..1]
Definition: Amount of money to be settled per piece of collateral to terminate the transaction.
TerminationAmountPerPieceOfCollateral <TermntnAmtPerPcOfColl> contains the following
elements (see "AmountAndDirection21" on page 1377 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1377
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1377
30.4.5.29  TerminationTransactionAmount <TermntnTxAmt>
Presence: [0..1]
Definition: Total amount of money to be settled to terminate the transaction.
TerminationTransactionAmount <TermntnTxAmt> contains the following elements (see
"AmountAndDirection21" on page 1377 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1377
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1377
30.4.5.30  SecondLegNarrative <ScndLegNrrtv>
Presence: [0..1]
Definition: Provides additional information about the second leg in narrative form.
Datatype: "Max140Text" on page 2191
30.4.6 SettlementParameters <SttlmParams>
Presence: [0..1]
Definition: Parameters which explicitly state the conditions that must be fulfilled before a particular
transaction of a financial instrument can be settled. These parameters are defined by the instructing
party in compliance with settlement rules in the market the transaction will settle in.
Impacted by: C7 "CashClearingSystemRule", C15 "FXStandingInstructionPresenceRule", C33
"SettlementDetailsRule"
Approved by the Securities SEG on 27 January 2026 sese.036.001.10
SecuritiesFinancingModificationInstructionV10
Settlement And Reconciliation - Maintenance 2025 - 2026 1079 March 2026
```

## File page 1080

```text
SettlementParameters <SttlmParams> contains the following SettlementDetails226 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldIndicator <HldInd> [0..1] Indicator 1081
   Priority <Prty> [0..1] ± 1081
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1081
   SettlingCapacity <SttlgCpcty> [0..1] ± 1081
   StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 1081
   SecuritiesRTGS <SctiesRTGS> [0..1] ± 1082
   BeneficialOwnership <BnfclOwnrsh> [0..1] ± 1082
   CashClearingSystem <CshClrSys> [0..1] ± 1082
   TaxCapacity <TaxCpcty> [0..1] ± 1083
   MarketClientSide <MktClntSd> [0..1] ± 1083
   FXStandingInstruction <FxStgInstr> [0..1] ± 1083
   BlockTrade <BlckTrad> [0..1] ± 1083
   LegalRestrictions <LglRstrctns> [0..1] ± 1084
   SettlementSystemMethod <SttlmSysMtd> [0..1] ± 1084
   NettingEligibility <NetgElgblty> [0..1] ± 1084
   CCPEligibility <CCPElgblty> [0..1] ± 1084
   Tracking <Trckg> [0..1] ± 1085
   AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 1085
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 1085
   EligibleForCollateral <ElgblForColl> [0..1] Indicator 1086
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
Approved by the Securities SEG on 27 January 2026 sese.036.001.10
SecuritiesFinancingModificationInstructionV10
Settlement And Reconciliation - Maintenance 2025 - 2026 1080 March 2026
```

