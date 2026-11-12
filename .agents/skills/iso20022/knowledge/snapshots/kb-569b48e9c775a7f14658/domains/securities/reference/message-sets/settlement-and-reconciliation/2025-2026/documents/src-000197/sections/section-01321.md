---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details"]
file_pages: [1781, 1782, 1783]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26 Settlement Details

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1781 to 1783.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1781

```text
Party5 <Pty5> contains the following elements (see "PartyIdentificationAndAccount196" on page 1667
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1668
   LEI <LEI> [0..1] IdentifierSet 1668
   AlternateIdentification <AltrnId> [0..1] ± 1668
   SafekeepingAccount <SfkpgAcct> [0..1] ± 1669
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1669
   ProcessingDate <PrcgDt> [0..1] ± 1669
   ProcessingIdentification <PrcgId> [0..1] Text 1669
   AdditionalInformation <AddtlInf> [0..1] ± C5 1669
Constraints
• SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
• SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
35.1.26 Settlement Details
35.1.26.1  SettlementDetails220
Definition: Details of settlement of a transaction.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1781 March 2026
```

## File page 1782

```text
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
   ReceivingSecuritiesSubBalanceType
<RcvgSctiesSubBalTp>
[0..1] ± 1791
   CashSubBalanceType <CshSubBalTp> [0..1] ± 1792
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1782 March 2026
```

## File page 1783

```text
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
The use of SecuritiesTransactionTypes OWNI, OWNE, INSP and PORT and other booktransfer
related fields is governed by a market practice document.
• Block Trades:
The parent transaction must be identified using the Block Trade field with code BLPA. The children
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1783 March 2026
```

