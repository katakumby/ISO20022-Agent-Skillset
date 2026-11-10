---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.9 ConfirmationParties <ConfPties>", "3.4.9.13 AffirmingParty <AffrmgPty>"]
file_pages: [112, 113, 114]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.9.13 AffirmingParty <AffrmgPty>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 112 to 114.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 112

```text
3.4.9.13  AffirmingParty <AffrmgPty>
Presence: [0..1]
Definition: Party (buyer or seller) that positively affirms the details of a previously agreed security trade
confirmation.
AffirmingParty <AffrmgPty> contains the following elements (see "ConfirmationPartyDetails8" on
page 481 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 481
   AlternateIdentification <AltrnId> [0..1] ± 482
   ProcessingIdentification <PrcgId> [0..1] Text 482
   AdditionalInformation <AddtlInf> [0..1] ± C1 482
3.4.9.14  TradeBeneficiaryParty <TradBnfcryPty>
Presence: [0..1]
Definition: Party involved in a legal proceeding, agreement or other transaction.
TradeBeneficiaryParty <TradBnfcryPty> contains the following elements (see
"ConfirmationPartyDetails10" on page 478 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 478
   SafekeepingAccount <SfkpgAcct> [0..1] ± 479
   CashDetails <CshDtls> [0..1] ± 479
   AlternateIdentification <AltrnId> [0..1] ± 480
   ProcessingIdentification <PrcgId> [0..1] Text 480
   AdditionalInformation <AddtlInf> [0..1] ± C1 480
   PartyCapacity <PtyCpcty> [0..1] ± 481
3.4.10 SettlementParameters <SttlmParams>
Presence: [0..1]
Definition: Parameters which explicitly state the conditions that must be fulfilled before a particular
transaction of a financial instrument can be settled. These parameters are defined by the instructing
party in compliance with settlement rules in the market the transaction will settle in.
Impacted by: C11 "CashClearingSystemRule", C21 "FXStandingInstructionPresenceRule", C45
"SettlementDetailsRule", C46 "SettlementParametersGuideline"
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 112 February 2025
```

## File page 113

```text
SettlementParameters <SttlmParams> contains the following elements (see "SettlementDetails213"
on page 569 for details)
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
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 113 February 2025
```

## File page 114

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LetterOfGuarantee <LttrOfGrnt> [0..1] ± 581
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
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 114 February 2025
```

