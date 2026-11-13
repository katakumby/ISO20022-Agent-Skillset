---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "26.4 Message Building Blocks", "26.4.8 SettlementParameters <SttlmParams>"]
file_pages: [852, 853, 854, 855, 856, 857, 858]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.032.001.13"]
---

# 26.4.8 SettlementParameters <SttlmParams>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 852 to 858.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 852

```text
26.4.8 SettlementParameters <SttlmParams>
Presence: [1..1]
Definition: Parameters which explicitly state the conditions that must be fulfilled before a particular
transaction of a financial instrument can be settled. These parameters are defined by the instructing
party in compliance with settlement rules in the market the transaction will settle in.
Impacted by: C13 "CashClearingSystemRule", C28 "FXStandingInstructionPresenceRule", C65
"SettlementDetailsRule", C66 "SettlementParametersGuideline"
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 852 March 2026
```

## File page 853

```text
SettlementParameters <SttlmParams> contains the following elements (see "SettlementDetails225"
on page 1821 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldIndicator <HldInd> [0..1] ± 1824
   Priority <Prty> [0..1] ± 1824
   SecuritiesTransactionType <SctiesTxTp> [1..1] ± 1824
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1824
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 1825
   BeneficialOwnership <BnfclOwnrsh> [0..1] ± 1825
   BlockTrade <BlckTrad> [0..1] ± 1825
   CCPEligibility <CCPElgblty> [0..1] ± 1826
   DeliveryReturnReason <DlvryRtrRsn> [0..1] ± 1826
   CashClearingSystem <CshClrSys> [0..1] ± 1826
   ExposureType <XpsrTp> [0..1] ± 1826
   FXStandingInstruction <FxStgInstr> [0..1] ± 1827
   MarketClientSide <MktClntSd> [0..1] ± 1827
   NettingEligibility <NetgElgblty> [0..1] ± 1827
   Registration <Regn> [0..1] ± 1827
   RepurchaseType <RpTp> [0..1] ± 1828
   LegalRestrictions <LglRstrctns> [0..1] ± 1828
   SecuritiesRTGS <SctiesRTGS> [0..1] ± 1828
   SettlingCapacity <SttlgCpcty> [0..1] ± 1828
   SettlementSystemMethod <SttlmSysMtd> [0..1] ± 1829
   TaxCapacity <TaxCpcty> [0..1] ± 1829
   StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 1829
   Tracking <Trckg> [0..1] ± 1829
   AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 1830
   LetterOfGuarantee <LttrOfGrnt> [0..1] ± 1830
   ReturnLeg <RtrLeg> [0..1] Indicator 1830
   ModificationCancellationAllowed <ModCxlAllwd> [0..1] ± 1830
   EligibleForCollateral <ElgblForColl> [0..1] Indicator 1831
   SecuritiesSubBalanceType <SctiesSubBalTp> [0..1] ± 1831
   CashSubBalanceType <CshSubBalTp> [0..1] ± 1831
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 853 March 2026
```

## File page 854

```text
Constraints
• CashClearingSystemRule
The CashSettlementSystem codes are to be used only by agents directly involved in the settlement
process, such as local settlement agents, CSDs and central banks.
• FXStandingInstructionPresenceRule
If HoldIndicator is present and is value TRUE (Yes), then FXStandingInstruction must not be present.
In ISO 15022, and therefore in ISO 20022, the FXStandingInstruction indicator can only be used
when the transaction is instructed in a released mode.
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
The parent transaction must be identified using the BloclTrade field with code BLPA. The children
transactions must be identified using the code BLCH.
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 854 March 2026
```

## File page 855

```text
For more details, see the relevant market practice document on www.smpg.info.
26.4.9 DeliveringSettlementParties <DlvrgSttlmPties>
Presence: [0..1]
Definition: Identifies the chain of delivering settlement parties.
Impacted by: C12 "BookTransferGuideline", C24 "DepositoryGuideline", C42 "Party2PresenceRule",
C43 "Party3PresenceRule", C44 "Party4PresenceRule", C45 "Party5PresenceRule", C64
"SettlementChainGuideline"
DeliveringSettlementParties <DlvrgSttlmPties> contains the following elements (see
"SettlementParties126" on page 1767 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1] ± 1769
   Party1 <Pty1> [0..1] ± C29,
C31
1770
   Party2 <Pty2> [0..1] ± C29,
C31
1771
   Party3 <Pty3> [0..1] ± C29,
C31
1771
   Party4 <Pty4> [0..1] ± C29,
C31
1772
   Party5 <Pty5> [0..1] ± C29,
C31
1773
Constraints
• BookTransferGuideline
In case of own account internal transfer, own account external transfer, portfolio transfer and in
specie transfer (see SecuritiesTransactionType), the account of (delivering) Party2 at (delivering)
Party1 must be provided.
For more details, see the relevant market practice document on www.smpg.info.
• DepositoryGuideline
In a delivery, the receiving depository is to be understood as the requested depository of the
receiving counterparty.
In a receive, the delivering depository is to be understood as the requested depository of the
delivering counterparty.
The field must be populated with the BIC of a national or international CSD. When no CSD exists in a
particular market, the stock exchange BIC is to be used.
Country code should be used for settlement taking place outside of an institution published in the
PSET's BIC list. This includes physical deliveries and investment funds not settling at a CSD.
The format and content of the settlement party sequences will comply with the market practices
published for the counterparty depository included in the message.
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 855 March 2026
```

## File page 856

```text
For more details, see the relevant market practice document on www.smpg.info.
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
• SettlementChainGuideline
SMPG recommends that at least three settlement parties be instructed in equity or fixed income
receive
free or against payment settlement instructions; the depository, the participant of the depository
(Party1) and the client of Party1 (Party2).
The data format for the identification of Party1 depends on the market. If no country specific
requirement is available, BIC is recommended.
For more details, see the relevant market practice document on www.smpg.info.
26.4.10 ReceivingSettlementParties <RcvgSttlmPties>
Presence: [0..1]
Definition: Identifies the chain of receiving settlement parties.
Impacted by: C12 "BookTransferGuideline", C24 "DepositoryGuideline", C42 "Party2PresenceRule",
C43 "Party3PresenceRule", C44 "Party4PresenceRule", C45 "Party5PresenceRule", C64
"SettlementChainGuideline"
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 856 March 2026
```

## File page 857

```text
ReceivingSettlementParties <RcvgSttlmPties> contains the following elements (see
"SettlementParties126" on page 1767 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1] ± 1769
   Party1 <Pty1> [0..1] ± C29,
C31
1770
   Party2 <Pty2> [0..1] ± C29,
C31
1771
   Party3 <Pty3> [0..1] ± C29,
C31
1771
   Party4 <Pty4> [0..1] ± C29,
C31
1772
   Party5 <Pty5> [0..1] ± C29,
C31
1773
Constraints
• BookTransferGuideline
In case of own account internal transfer, own account external transfer, portfolio transfer and in
specie transfer (see SecuritiesTransactionType), the account of (delivering) Party2 at (delivering)
Party1 must be provided.
For more details, see the relevant market practice document on www.smpg.info.
• DepositoryGuideline
In a delivery, the receiving depository is to be understood as the requested depository of the
receiving counterparty.
In a receive, the delivering depository is to be understood as the requested depository of the
delivering counterparty.
The field must be populated with the BIC of a national or international CSD. When no CSD exists in a
particular market, the stock exchange BIC is to be used.
Country code should be used for settlement taking place outside of an institution published in the
PSET's BIC list. This includes physical deliveries and investment funds not settling at a CSD.
The format and content of the settlement party sequences will comply with the market practices
published for the counterparty depository included in the message.
For more details, see the relevant market practice document on www.smpg.info.
• Party2PresenceRule
If Party2 is present, then Party1 must be present.
On Condition
    /Party2 is present
Following Must be True
    /Party1 Must be present
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 857 March 2026
```

## File page 858

```text
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
• SettlementChainGuideline
SMPG recommends that at least three settlement parties be instructed in equity or fixed income
receive
free or against payment settlement instructions; the depository, the participant of the depository
(Party1) and the client of Party1 (Party2).
The data format for the identification of Party1 depends on the market. If no country specific
requirement is available, BIC is recommended.
For more details, see the relevant market practice document on www.smpg.info.
26.4.11 CashParties <CshPties>
Presence: [0..1]
Definition: Cash parties involved in the transaction if different from the securities settlement parties.
CashParties <CshPties> contains the following elements (see "CashParties41" on page 1698 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Debtor <Dbtr> [0..1] ± 1698
   DebtorAgent <DbtrAgt> [0..1] ± 1698
   Creditor <Cdtr> [0..1] ± 1699
   CreditorAgent <CdtrAgt> [0..1] ± 1699
   Intermediary <Intrmy> [0..1] ± 1700
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 858 March 2026
```

