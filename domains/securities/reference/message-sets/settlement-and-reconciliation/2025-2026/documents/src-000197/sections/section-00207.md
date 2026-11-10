---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.4 Message Building Blocks", "9.4.6 Status <Sts>", "9.4.6.2 Transaction <Tx>", "9.4.6.2.15 TransactionDetails <TxDtls>"]
file_pages: [309, 310, 311, 312, 313]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.4.6.2.15 TransactionDetails <TxDtls>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 309 to 313.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 309

```text
9.4.6.2.15  TransactionDetails <TxDtls>
Presence: [0..1]
Definition: Identifies the details of the transaction.
Impacted by: C3 "AdditionalDetailsRule", C10 "DeliveringParty1Rule", C17 "LateDeliveryDateRule",
C28 "PostingAmountRule", C29 "ReceivingParty1Rule", C41
"TwoLegTransactionOpeningClosing1Rule", C42 "TwoLegTransactionOpeningClosing2Rule"
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 309 March 2026
```

## File page 310

```text
TransactionDetails <TxDtls> contains the following TransactionDetails185 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionActivity <TxActvty> [1..1] ± 314
   SettlementTransactionOrCorporateActionEventType
<SttlmTxOrCorpActnEvtTp>
[0..1] ± 314
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 314
   Payment <Pmt> [1..1] CodeSet 315
   SettlementParameters <SttlmParams> [0..1] ± C6, C38 315
   PlaceOfTrade <PlcOfTrad> [0..1] ± 316
   SafekeepingPlace <SfkpgPlc> [0..1] ± C36 317
   PlaceOfClearing <PlcOfClr> [0..1] ± 317
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C15,
C16,
C21
317
   PostingQuantity <PstngQty> [1..1] ± 318
   PartiallyReleasedQuantity <PrtlyRlsdQty> [0..1] ± 319
   PostingAmount <PstngAmt> [0..1] ± 319
   DigitalPaymentSettlement <DgtlPmtSttlm> [0..1]  319
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C15,
C16,
C21
320
     ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 321
     CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  321
{Or       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 321
Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C5 321
Or}       LEI <LEI> [1..1] IdentifierSet 322
   TradeDate <TradDt> [0..1] ± 322
   ExpectedSettlementDate <XpctdSttlmDt> [0..1] ± 322
   SettlementDate <SttlmDt> [1..1] ± 322
   LateDeliveryDate <LateDlvryDt> [0..1] ± 323
   ExpectedValueDate <XpctdValDt> [0..1] ± 323
   AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 323
   MatchedStatusTimeStamp <MtchdStsTmStmp> [0..1] DateTime 323
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 310 March 2026
```

## File page 311

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C22,
C23,
C24,
C25
323
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C22,
C23,
C24,
C25
324
   TransactionAdditionalDetails <TxAddtlDtls> [0..1] Text 326
   SupplementaryData <SplmtryData> [0..*] ± C40 326
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the sender and receiver, if TransactionAdditionalDetails is present,
then it must not contain information that can be provided in a structured field.
• DeliveringParty1Rule
If the instruction is a receive, then DeliveringParty1 must be present.
On Condition
    /SecuritiesMovementType is equal to value 'Receive'
Following Must be True
    /DeliveringSettlementParties/Party1 Must be present
• LateDeliveryDateRule
If LateDeliveryDate is present then the transaction must be a pool trade that results from the original
TBA (To Be Announced). The original TBA would be offset by an opposite transaction and replaced
by buys or sells of individual pools. It is a date greater than the settlement date stated in the trade,
for pools designed as settling late.
• PostingAmountRule
If the instruction is against payment, PostingAmount must be present.
On Condition
    /Payment is equal to value 'AgainstPaymentSettlement'
Following Must be True
    /PostingAmount Must be present
• ReceivingParty1Rule
If the instruction is a delivery, then ReceivingParty 1 must be present.
On Condition
    /SecuritiesMovementType is equal to value 'Delivery'
Following Must be True
    /ReceivingSettlementParties/Party1 Must be present
• TwoLegTransactionOpeningClosing1Rule
For settlement of two part transactions (Securities Financing), the opening/initiation and closing/
return of the transaction is confirmed by sending the following combination of
TransactionIdentificationDetails/SecuritiesMovementType codes and SettlementParameters/
SecuritiesTransactionType codes:
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 311 March 2026
```

## File page 312

```text
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
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 312 March 2026
```

## File page 313

```text
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
opening/initiation and closing/return of the transaction is identified by the providing of the following
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
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 313 March 2026
```

