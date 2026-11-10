---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.2 Deletion <Deltn>", "32.4.2.2.6 SettlementParameters <SttlmParams>"]
file_pages: [1229, 1230, 1231, 1232]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.2.6 SettlementParameters <SttlmParams>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1229 to 1232.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1229

```text
Constraints
• DenominationRule
Unless bilaterally agreed between the account owner and servicer, if DenominationChoice is used, it
must not contain information that can be provided in a structured field.
• SafekeepingPlaceGuideline
When used (see usage rule SafekeepingPlaceRule), unless special arrangements exist between the
account servicer and the account owner, it is recommended to use the place of safekeeping field
following the market practice described below:
• SafekeepingPlaceType/SharesHeldAtNCSD: a NCSD's BIC will be used for domestic and NCSD to
NCSD settlement instructions.
• SafekeepingPlaceType/SharesHeldAtICSD: an ICSD's BIC will be used for ICSD internal, ICSD/
local and ICSD to ICSD settlement instructions.
• SafekeepingPlaceType/SharesHeldAtLoaclCustodian: applicable, for instance, when the account
servicer is a global custodian and provides the account owner with a position reporting at global
custodian's agents' level. When instructing, the fund manager would therefore mention, as a place of
safekeeping, the BIC of the global custodian's agent on the market.
Absence of SafekeepingPlace means that:
• The SafekeepingPlace information is kept by the account servicer (SLA, account structure, ETC.)
and should not be provided by the account owner.
• The SafekeepingPlace is the counterparty's Depository. The transaction is therefore domestic (to
an NCSD) or internal to an ICSD.
For more details, see the relevant market practice document on www.smpg.info.
32.4.2.2.6  SettlementParameters <SttlmParams>
Presence: [0..1]
Definition: Parameters which explicitly state the conditions that must be fulfilled before a particular
transaction of a financial instrument can be settled. These parameters are defined by the instructing
party in compliance with settlement rules in the market the transaction will settle in.
Impacted by: C12 "CashSettlementSystemUsageRule", C39 "OpeningClosingUsageRule", C76
"SettlementDetailsElementsUsageRule"
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1229 March 2026
```

## File page 1230

```text
SettlementParameters <SttlmParams> contains the following elements (see "SettlementDetails230"
on page 1807 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesTransactionType <SctiesTxTp> [0..1] ± 1811
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1811
   BeneficialOwnership <BnfclOwnrsh> [0..1] ± 1811
   CCPEligibility <CCPElgblty> [0..1] ± 1811
   DeliveryReturnReason <DlvryRtrRsn> [0..1] ± 1812
   CashClearingSystem <CshClrSys> [0..1] ± 1812
   ExposureType <XpsrTp> [0..1] ± 1812
   FXStandingInstruction <FxStgInstr> [0..1] ± 1812
   MarketClientSide <MktClntSd> [0..1] ± 1813
   NettingEligibility <NetgElgblty> [0..1] ± 1813
   Registration <Regn> [0..1] ± 1813
   LegalRestrictions <LglRstrctns> [0..1] ± 1813
   SettlingCapacity <SttlgCpcty> [0..1] ± 1814
   TaxCapacity <TaxCpcty> [0..1] ± 1814
   StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 1814
   Tracking <Trckg> [0..1] ± 1814
   LetterOfGuarantee <LttrOfGrnt> [0..1] ± 1815
   ReturnLeg <RtrLeg> [0..1] Indicator 1815
   ModificationCancellationAllowed <ModCxlAllwd> [0..1] ± 1815
   EligibleForCollateral <ElgblForColl> [0..1] Indicator 1815
   SecuritiesSubBalanceType <SctiesSubBalTp> [0..1] ± 1816
   CashSubBalanceType <CshSubBalTp> [0..1] ± 1816
Constraints
• CashSettlementSystemUsageRule
Cash settlement system codes are to be used only by agents directly involved in the settlement
process, such as local settlement agents, CSDs and central banks.
• OpeningClosingUsageRule
For settlement of two parts transactions (Securities Financing, buy-sell back, sell buy-back), the
opening/initiation and closing/return of the transaction will be confirmed by sending the below
combination of ReceiveDelivery codes and SettlementTransactionType codes:
Repo Opening
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1230 March 2026
```

## File page 1231

```text
ReceiveDelivery: Delivery (DELI)
SettlementTransactionType: Repo (REPU)
Repo Closing
ReceiveDelivery: Receive (RECE)
SettlementTransactionType: Repo (REPU)
Reverse Repo Opening
ReceiveDelivery: Receive (RECE)
SettlementTransactionType: ReverseRepo (RVPO)
Reverse Repo Closing
ReceiveDelivery: Delivery (DELI)
SettlementTransactionType: ReverseRepo (RVPO)
TriParty Repo Opening
ReceiveDelivery: Delivery (DELI)
SettlementTransactionType: TriPartyRepo (TRPO)
TriParty Repo Closing
ReceiveDelivery: Receive (RECE)
SettlementTransactionType: TriPartyRepo (TRPO)
TriParty Reverse Repo Opening
ReceiveDelivery: Receive (RECE)
SettlementTransactionType: TriPartyReverseRepo (TRVO)
TriParty Reverse Repo Closing
ReceiveDelivery: Delivery (DELI)
SettlementTransactionType: TriPartyReverseRepo (TRVO)
Securities Lending Initiation
ReceiveDelivery: Delivery (DELI)
SettlementTransactionType: SecuritiesLending (SECL)
Securities Lending Return
ReceiveDelivery: Receive (RECE)
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1231 March 2026
```

## File page 1232

```text
SettlementTransactionType: SecuritiesLending (SECL)
Securities Borrowing Initiation
ReceiveDelivery: Receive (RECE)
SettlementTransactionType: SecuritiesBorrowing (SECB)
Securities Borrowing Return
ReceiveDelivery: Delivery (DELI)
SettlementTransactionType: SecuritiesBorrowing (SECB)
Sell-Buy Back: Sell
ReceiveDelivery: Delivery (DELI)
SettlementTransactionType: SellBuyBack (SBBK)
Sell-Buy Back: Buy Back
ReceiveDelivery: Receive (RECE)
SettlementTransactionType: SellBuyBack (SBBK)
Buy-Sell Back: Buy
ReceiveDelivery: Receive (RECE)
SettlementTransactionType: BuySellBack (BSBK)
Buy-Sell Back: Sell Back
ReceiveDelivery: Delivery (DELI)
SettlementTransactionType: BuySellBack (BSBK)
Collateral (giver) Out Initiation
ReceiveDelivery: Delivery (DELI)
SettlementTransactionType: CollateralOut (COLO)
Collateral (giver) Out Return
ReceiveDelivery: Receive (RECE)
SettlementTransactionType: CollateralOut (COLO)
Collateral (taker) In Initiation
ReceiveDelivery: Receive (RECE)
SettlementTransactionType: CollateralIn (COLI)
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1232 March 2026
```

