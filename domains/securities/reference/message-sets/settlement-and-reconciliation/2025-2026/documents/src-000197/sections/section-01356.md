---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.6 SettlementDetails227", "35.1.26.6.14 CCPEligibility <CCPElgblty>"]
file_pages: [1821, 1822, 1823]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.6.14 CCPEligibility <CCPElgblty>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1821 to 1823.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1821

```text
35.1.26.6.14  CCPEligibility <CCPElgblty>
Presence: [0..1]
Definition: Specifies whether the settlement transaction is CCP (Central Counterparty) eligible.
CCPEligibility <CCPElgblty> contains one of the following elements (see
"CentralCounterPartyEligibility4Choice" on page 1546 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1546
Or}   Proprietary <Prtry> [1..1] ± 1546
35.1.26.6.15  PartialSettlementIndicator <PrtlSttlmInd>
Presence: [0..1]
Definition: Specifies whether partial settlement is allowed.
Datatype: "SettlementTransactionCondition5Code" on page 2170
CodeName Name Definition
PART PartialAllowed Partial settlement is allowed.
NPAR PartialNotAllowed Partial settlement is not allowed.
PARC PartialSettlementCashThresholdAllowed Partial settlement is allowed but must
satisfy a cash value minimum (value
defined in static data).
PARQ PartialSettlementQuantityThresholdAllowed Partial settlement is allowed but must
satisfy a minimum quantity of securities
(quantity defined in static data).
35.1.26.6.16  EligibleForCollateral <ElgblForColl>
Presence: [0..1]
Definition: Specifies whether securities should be included in the pool of securities eligible for collateral
purposes.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.26.7  SettlementDetails225
Definition: Details of settlement of a transaction.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1821 March 2026
```

## File page 1822

```text
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1822 March 2026
```

## File page 1823

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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1823 March 2026
```

