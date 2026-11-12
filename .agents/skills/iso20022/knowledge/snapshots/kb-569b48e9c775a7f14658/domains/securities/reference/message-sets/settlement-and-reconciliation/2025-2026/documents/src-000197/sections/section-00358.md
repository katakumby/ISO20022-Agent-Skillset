---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "17.4 Message Building Blocks", "17.4.9 SettlementParameters <SttlmParams>"]
file_pages: [531, 532, 533, 534]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.023.001.13"]
---

# 17.4.9 SettlementParameters <SttlmParams>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 531 to 534.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 531

```text
17.4.9 SettlementParameters <SttlmParams>
Presence: [1..1]
Definition: Parameters which explicitly state the conditions that must be fulfilled before a particular
transaction of a financial instrument can be settled. These parameters are defined by the instructing
party in compliance with settlement rules in the market the transaction will settle in.
Impacted by: C14 "CashClearingSystemRule", C29 "FXStandingInstructionPresenceRule", C71
"SettlementDetailsRule", C72 "SettlementParametersGuideline"
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 531 March 2026
```

## File page 532

```text
SettlementParameters <SttlmParams> contains the following elements (see "SettlementDetails220"
on page 1781 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldIndicator <HldInd> [0..1] ± 1784
   Priority <Prty> [0..1] ± 1784
   SecuritiesTransactionType <SctiesTxTp> [1..1] ± 1784
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1784
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 1785
   BeneficialOwnership <BnfclOwnrsh> [0..1] ± 1785
   BlockTrade <BlckTrad> [0..1] ± 1785
   CCPEligibility <CCPElgblty> [0..1] ± 1786
   DeliveryReturnReason <DlvryRtrRsn> [0..1] ± 1786
   CashClearingSystem <CshClrSys> [0..1] ± 1786
   ExposureType <XpsrTp> [0..1] ± 1786
   FXStandingInstruction <FxStgInstr> [0..1] ± 1787
   MarketClientSide <MktClntSd> [0..1] ± 1787
   NettingEligibility <NetgElgblty> [0..1] ± 1787
   Registration <Regn> [0..1] ± 1787
   RepurchaseType <RpTp> [0..1] ± 1788
   LegalRestrictions <LglRstrctns> [0..1] ± 1788
   SecuritiesRTGS <SctiesRTGS> [0..1] ± 1788
   SettlingCapacity <SttlgCpcty> [0..1] ± 1788
   SettlementSystemMethod <SttlmSysMtd> [0..1] ± 1789
   TaxCapacity <TaxCpcty> [0..1] ± 1789
   StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 1789
   Tracking <Trckg> [0..1] ± 1789
   AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 1790
   LetterOfGuarantee <LttrOfGrnt> [0..1] ± 1790
   ReturnLeg <RtrLeg> [0..1] Indicator 1790
   ModificationCancellationAllowed <ModCxlAllwd> [0..1] ± 1790
   EligibleForCollateral <ElgblForColl> [0..1] Indicator 1791
   DeliveringSecuritiesSubBalanceType
<DlvrgSctiesSubBalTp>
[0..1] ± 1791
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 532 March 2026
```

## File page 533

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReceivingSecuritiesSubBalanceType
<RcvgSctiesSubBalTp>
[0..1] ± 1791
   CashSubBalanceType <CshSubBalTp> [0..1] ± 1792
Constraints
• CashClearingSystemRule
The CashSettlementSystem codes are to be used only by agents directly involved in the settlement
process, such as local settlement agents, CSDs and central banks.
• FXStandingInstructionPresenceRule
If HoldIndicator is present and is value TRUE (Yes), then FXStandingInstruction must not be present.
In ISO 15022,
and therefore in ISO 20022, the FXStandingInstruction indicator can only be used when the
transation is instructed
in a released mode.
On Condition
    /HoldIndicator is present
 And    /HoldIndicator/Indicator is equal to value 'true'
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
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 533 March 2026
```

## File page 534

```text
The use of SecuritiesTransactionTypes OWNI, OWNE, INSP and PORT and other booktransfer
related fields is governed by a market practice document.
• Block Trades:
The parent transaction must be identified using the Block Trade field with code BLPA. The children
transactions must be identified using the code BLCH.
For more details, see the relevant market practice document on www.smpg.info.
17.4.10 StandingSettlementInstructionDetails
<StgSttlmInstrDtls>
Presence: [0..1]
Definition: Specifies what settlement standing instruction database is to be used to derive the
settlement parties involved in the transaction.
Impacted by: C79 "VendorPresenceRule"
StandingSettlementInstructionDetails <StgSttlmInstrDtls> contains the following
StandingSettlementInstruction20 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementStandingInstructionDatabase
<SttlmStgInstrDB>
[1..1] ± 535
   Counterparty <CtrPty> [1..1] ± 535
   Vendor <Vndr> [0..1] ± 535
   OtherDeliveringSettlementParties
<OthrDlvrgSttlmPties>
[0..1] ± C11,
C25,
C45,
C46,
C47,
C48,
C70
535
   OtherReceivingSettlementParties
<OthrRcvgSttlmPties>
[0..1] ± C11,
C25,
C45,
C46,
C47,
C48,
C70
537
Constraints
• VendorPresenceRule
If the settlement standing instruction database is a vendor database, then the vendor must be
identified.
On Condition
    /SettlementStandingInstructionDatabase/Code is equal to value 'VendorDatabase'
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 534 March 2026
```

