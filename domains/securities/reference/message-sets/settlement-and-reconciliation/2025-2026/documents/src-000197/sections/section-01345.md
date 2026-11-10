---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.4 SettlementDetails231", "35.1.26.4.17 PartialSettlementIndicator <PrtlSttlmInd>"]
file_pages: [1807, 1808, 1809, 1810]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.4.17 PartialSettlementIndicator <PrtlSttlmInd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1807 to 1810.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1807

```text
35.1.26.4.17  PartialSettlementIndicator <PrtlSttlmInd>
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
35.1.26.5  SettlementDetails230
Definition: Details of settlement of a transaction.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1807 March 2026
```

## File page 1808

```text
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
ReceiveDelivery: Delivery (DELI)
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1808 March 2026
```

## File page 1809

```text
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
SettlementTransactionType: SecuritiesLending (SECL)
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1809 March 2026
```

## File page 1810

```text
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
Collateral (taker) In Return
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1810 March 2026
```

