---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.3 Modification <Mod>", "32.4.2.3.6 QuantityAndAccountDetails <QtyAndAcctDtls>", "32.4.2.3.6.8 QuantityBreakdown <QtyBrkdwn>"]
file_pages: [1274, 1275, 1276, 1277]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.3.6.8 QuantityBreakdown <QtyBrkdwn>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1274 to 1277.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1274

```text
SafekeepingPlace <SfkpgPlc> contains the following elements (see "SafeKeepingPlace5" on
page 1749 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceFormat <SfkpgPlcFrmt> [0..1] ± 1749
   LEI <LEI> [0..1] IdentifierSet 1750
Constraints
• SafekeepingPlaceFormatOrLEIRule
SafekeepingPlaceFormat must be present or LEI must be present.
Following Must be True
    /SafekeepingPlaceFormat Must be present
 Or    /LEI Must be present
32.4.2.3.6.8  QuantityBreakdown <QtyBrkdwn>
Presence: [0..*]
Definition: Breakdown of a quantity into lots such as tax lots, instrument series.
QuantityBreakdown <QtyBrkdwn> contains the following elements (see "QuantityBreakdown62" on
page 1733 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 1733
   LotQuantity <LotQty> [0..1] ± C12 1734
   LotDateTime <LotDtTm> [0..1] ± 1734
   LotPrice <LotPric> [0..1] ± 1734
   TypeOfPrice <TpOfPric> [0..1] ± 1735
32.4.2.3.7  SettlementParameters <SttlmParams>
Presence: [0..1]
Definition: Parameters which explicitly state the conditions that must be fulfilled before a particular
transaction of a financial instrument can be settled. These parameters are defined by the instructing
party in compliance with settlement rules in the market the transaction will settle in.
Impacted by: C12 "CashSettlementSystemUsageRule", C39 "OpeningClosingUsageRule", C76
"SettlementDetailsElementsUsageRule"
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1274 March 2026
```

## File page 1275

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
Settlement And Reconciliation - Maintenance 2025 - 2026 1275 March 2026
```

## File page 1276

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
Settlement And Reconciliation - Maintenance 2025 - 2026 1276 March 2026
```

## File page 1277

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
Settlement And Reconciliation - Maintenance 2025 - 2026 1277 March 2026
```

