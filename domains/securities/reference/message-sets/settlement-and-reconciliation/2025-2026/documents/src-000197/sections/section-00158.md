---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "8.4 Message Building Blocks", "8.4.6 IntermediaryInformation <IntrmyInf>", "8.4.7.7 Transaction <Tx>", "8.4.7.7.15 MasterReference <MstrRef>"]
file_pages: [227, 228, 229, 230, 231]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.017.001.14"]
---

# 8.4.7.7.15 MasterReference <MstrRef>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 227 to 231.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 227

```text
8.4.7.7.15  MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual orders, as assigned by the
instructing party. This identifier links the individual orders together.
Datatype: "Max35Text" on page 2192
8.4.7.7.16  ClientReference <ClntRef>
Presence: [0..1]
Definition: Unique and unambiguous investor's identification of an order. This reference can typically be
used in a hub scenario to give the reference of the order as assigned by the underlying client.
ClientReference <ClntRef> contains the following elements (see "AdditionalReference10" on
page 1487 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 1487
   ReferenceIssuer <RefIssr> [0..1] ± 1487
   MessageName <MsgNm> [0..1] Text 1488
8.4.7.7.17  AccountOwnerLegIdentification <AcctOwnrLegId>
Presence: [0..1]
Definition: Unique technical identifier for the instance of the leg within a switch.
Datatype: "Max35Text" on page 2192
8.4.7.7.18  AccountServicerLegIdentification <AcctSvcrLegId>
Presence: [0..1]
Definition: Unique identifier for the instance of the leg execution within a switch confirmation.
Datatype: "Max35Text" on page 2192
8.4.7.7.19  TransactionDetails <TxDtls>
Presence: [0..1]
Definition: Identifies the details of the transaction.
Impacted by: C2 "AdditionalDetailsRule", C25 "PostingAmountRule", C43
"TwoLegTransactionOpeningClosing1Rule", C45 "TwoLegTransactionOpeningClosing2Rule"
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 227 March 2026
```

## File page 228

```text
TransactionDetails <TxDtls> contains the following TransactionDetails186 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionActivity <TxActvty> [1..1] ± 232
   SettlementTransactionOrCorporateActionEventType
<SttlmTxOrCorpActnEvtTp>
[0..1] ± 232
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 232
   Payment <Pmt> [1..1] CodeSet 232
   SettlementParameters <SttlmParams> [0..1] ± C5, C37 233
   PlaceOfTrade <PlcOfTrad> [0..1] ± 234
   SafekeepingPlace <SfkpgPlc> [0..1] ± C35 234
   PlaceOfClearing <PlcOfClr> [0..1] ± 234
   PostingQuantity <PstngQty> [1..1] ± 235
   NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C19 235
   PostingAmount <PstngAmt> [0..1] ± 235
   DigitalPaymentSettlement <DgtlPmtSttlm> [0..1]  235
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C8, C9,
C14,
C15,
C20
236
     ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 237
     CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  237
{Or       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 237
Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C4 237
Or}       LEI <LEI> [1..1] IdentifierSet 238
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 238
   TradeDate <TradDt> [0..1] ± 238
   EffectiveSettlementDate <FctvSttlmDt> [1..1] ± 238
   SettlementDate <SttlmDt> [0..1] ± 239
   ValueDate <ValDt> [0..1] ± 239
   AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 239
   MatchedStatusTimeStamp <MtchdStsTmStmp> [0..1] DateTime 239
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C21,
C22,
C23,
C24
239
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C21,
C22,
240
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 228 March 2026
```

## File page 229

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
C23,
C24
   ReversalIndicator <RvslInd> [0..1] Indicator 242
   TransactionAdditionalDetails <TxAddtlDtls> [0..1] Text 242
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the sender and receiver, if TransactionAdditionalDetails is present,
then it must not contain information that can be provided in a structured field.
• PostingAmountRule
If the instruction is against payment, PostingAmount must be present.
On Condition
    /Payment is equal to value 'AgainstPaymentSettlement'
Following Must be True
    /PostingAmount Must be present
• TwoLegTransactionOpeningClosing1Rule
For settlement of two part transactions (Securities Financing), the opening/initiation and closing/
return of the transaction is confirmed by sending the following combination of
TransactionIdentificationDetails/SecuritiesMovementType codes and SettlementParameters/
SecuritiesTransactionType codes:
Repo Opening
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: Repo (REPU)
Repo Closing
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: Repo (REPU)
Reverse Repo Opening
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: ReverseRepo (RVPO)
Reverse Repo Closing
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: ReverseRepo (RVPO)
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 229 March 2026
```

## File page 230

```text
TriParty Repo Opening
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: TriPartyRepo (TRPO)
TriParty Repo Closing
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: TriPartyRepo (TRPO)
TriParty Reverse Repo Opening
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: TriPartyReverseRepo (TRVO)
TriParty Reverse Repo Closing
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: TriPartyReverseRepo (TRVO)
Securities Lending Initiation
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: SecuritiesLending (SECL)
Securities Lending Return
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: SecuritiesLending (SECL)
Securities Borrowing Initiation
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: SecuritiesBorrowing (SECB)
Securities Borrowing Return
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: SecuritiesBorrowing (SECB).
• TwoLegTransactionOpeningClosing2Rule
For settlement of two part transactions (buy-sell back, sell buy-back, collateral in and out), the
opening/initiation and closing/return of the transaction is confirmed by sending the following
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 230 March 2026
```

## File page 231

```text
combination of SecuritiesMovementType codes and SettlementParameters/
SecuritiesTransactionType codes:
Sell-Buy Back: Sell
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: SellBuyBack (SBBK)
Sell-Buy Back: Buy Back
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: SellBuyBack (SBBK)
Buy-Sell Back: Buy
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: BuySellBack (BSBK)
Buy-Sell Back: Sell Back
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: BuySellBack (BSBK)
Collateral (giver) Out Initiation
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: CollateralOut (COLO)
Collateral (giver) Out Return
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: CollateralOut (COLO)
Collateral (taker) In Initiation
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: CollateralIn (COLI)
Collateral (taker) In Return
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: CollateralIn (COLI).
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 231 March 2026
```

