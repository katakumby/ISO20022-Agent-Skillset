---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.27 Settlement Details"]
file_pages: [569, 570, 571]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.27 Settlement Details

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 569 to 571.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 569

```text
Datatype: "Max35Text" on page 669
7.1.27 Settlement Details
7.1.27.1  SettlementDetails213
Definition: Parameters which explicitly state the conditions that must be fulfilled before a particular
transaction of a financial instrument can be settled. These parameters are defined by the instructing
party in compliance with settlement rules in the market the transaction will settle in.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 569 February 2025
```

## File page 570

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementTransactionType <SttlmTxTp> [1..1]  572
{Or     Code <Cd> [1..1] CodeSet 572
Or}     Proprietary <Prtry> [1..1] ± 574
   HoldIndicator <HldInd> [0..1] Indicator 574
   Priority <Prty> [0..1] ± 574
   SettlementInstructionGeneration <SttlmInstrGnrtn> [0..1]  575
{Or     Code <Cd> [1..1] CodeSet 575
Or}     Proprietary <Prtry> [1..1] ± 575
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 576
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] Indicator 576
   BeneficialOwnership <BnfclOwnrsh> [0..1] ± 576
   BlockTrade <BlckTrad> [0..1] ± 576
   CCPEligibility <CCPElgblty> [0..1] ± 576
   CashClearingSystem <CshClrSys> [0..1] ± 577
   ExposureType <XpsrTp> [0..1] ± 577
   FXStandingInstruction <FxStgInstr> [0..1] ± 577
   CurrencyToBuyOrSell <CcyToBuyOrSell> [0..1] ± 577
   MarketClientSide <MktClntSd> [0..1] ± 578
   NettingEligibility <NetgElgblty> [0..1] ± 578
   Registration <Regn> [0..1] ± 578
   RepurchaseType <RpTp> [0..1] ± 579
   LegalRestrictions <LglRstrctns> [0..1] ± 579
   SecuritiesRTGS <SctiesRTGS> [0..1] ± 579
   SettlingCapacity <SttlgCpcty> [0..1] ± 579
   SettlementSystemMethod <SttlmSysMtd> [0..1] ± 580
   TaxCapacity <TaxCpcty> [0..1] ± 580
   StampDutyIndicator <StmpDtyInd> [0..1] Indicator 580
   StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 580
   Tracking <Trckg> [0..1] ± 581
   AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 581
   LetterOfGuarantee <LttrOfGrnt> [0..1] ± 581
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 570 February 2025
```

## File page 571

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReturnLeg <RtrLeg> [0..1] Indicator 581
   ModificationCancellationAllowed <ModCxlAllwd> [0..1] ± 582
   EligibleForCollateral <ElgblForColl> [0..1] Indicator 582
Constraints
• CashClearingSystemRule
The CashClearingSystem codes are to be used only by agents directly involved in the settlement
process, such as local settlement agents, CSD's and central banks.
• FXStandingInstructionPresenceRule
If HoldIndicator is present and is value TRUE (Yes), then FXStandingInstruction must not be present.
In ISO 15022, and therefore in ISO 20022, the FXStandingInstruction indicator can only be used
when the transation is instructed in a released mode.
On Condition
    /HoldIndicator is present
 And    /HoldIndicator is equal to value 'true'
Following Must be True
    /FXStandingInstruction Must be absent
• SettlementDetailsRule
If SettlementDetails elements are used, then their conditions of use must be pre-agreed between
account owner and account servicer.
• SettlementParametersGuideline
• Physical settlement:
In case of physical receipt at local agent level, the receiving agent must receive a receipt free
instruction
for reconciliation purposes. If the final beneficiary of the securities uses a global custodian, the
receipt free
instruction will be sent to the global custodian that will forward it to his receiving agent on the market.
For physical settlement, SettlementTransactionCondition/Physical must be used.
• Partial settlement:
This market practice only applies in markets where partial settlement is allowed.
If an account owner wants to specify in its original instruction that partial settlement is allowed or not,
they
must use the PartialSettlementIndicator.
• Book Transfer:
The use of SecuritiesTransactionTypes OWNI, OWNE, INSP and PORT and other booktransfer
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 571 February 2025
```

