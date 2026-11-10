---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.4 Message Building Blocks", "9.4.6 Status <Sts>", "9.4.7.9 CommonIdentification <CmonId>"]
file_pages: [331, 332, 333, 334, 335]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.4.7.9 CommonIdentification <CmonId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 331 to 335.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 331

```text
9.4.7.9  CommonIdentification <CmonId>
Presence: [0..1]
Definition: Unique reference agreed upon by the two trade counterparties to identify the trade.
Datatype: "Max35Text" on page 2192
9.4.7.10  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [0..1]
Definition: Identification assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 2192
9.4.7.11  TripartyAgentServiceProviderCollateralTransactionIdentification
<TrptyAgtSvcPrvdrCollTxId>
Presence: [0..1]
Definition: Unique identification identifying the triparty collateral management transaction from the
triparty-agent's/service-provider's point of view.
Datatype: "Max35Text" on page 2192
9.4.7.12  ClientTripartyCollateralTransactionIdentification <ClntTrptyCollTxId>
Presence: [0..1]
Definition: Unique reference identifying the triparty collateral management transaction from the client's
point of view.
Datatype: "Max35Text" on page 2192
9.4.7.13  ClientCollateralInstructionIdentification <ClntCollInstrId>
Presence: [0..1]
Definition: Unique identification assigned to the instruction by the client.
Datatype: "Max35Text" on page 2192
9.4.7.14  TripartyAgentServiceProviderCollateralInstructionIdentification
<TrptyAgtSvcPrvdrCollInstrId>
Presence: [0..1]
Definition: Unique identification assigned to the instruction by the triparty-agent/service-provider.
Datatype: "Max35Text" on page 2192
9.4.7.15  TransactionDetails <TxDtls>
Presence: [0..1]
Definition: Identifies the details of the transaction.
Impacted by: C3 "AdditionalDetailsRule", C10 "DeliveringParty1Rule", C17 "LateDeliveryDateRule",
C28 "PostingAmountRule", C29 "ReceivingParty1Rule", C41
"TwoLegTransactionOpeningClosing1Rule", C42 "TwoLegTransactionOpeningClosing2Rule"
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 331 March 2026
```

## File page 332

```text
TransactionDetails <TxDtls> contains the following TransactionDetails185 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionActivity <TxActvty> [1..1] ± 336
   SettlementTransactionOrCorporateActionEventType
<SttlmTxOrCorpActnEvtTp>
[0..1] ± 336
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 336
   Payment <Pmt> [1..1] CodeSet 337
   SettlementParameters <SttlmParams> [0..1] ± C6, C38 337
   PlaceOfTrade <PlcOfTrad> [0..1] ± 338
   SafekeepingPlace <SfkpgPlc> [0..1] ± C36 339
   PlaceOfClearing <PlcOfClr> [0..1] ± 339
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C15,
C16,
C21
339
   PostingQuantity <PstngQty> [1..1] ± 340
   PartiallyReleasedQuantity <PrtlyRlsdQty> [0..1] ± 341
   PostingAmount <PstngAmt> [0..1] ± 341
   DigitalPaymentSettlement <DgtlPmtSttlm> [0..1]  341
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C15,
C16,
C21
342
     ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 343
     CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  343
{Or       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 343
Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C5 343
Or}       LEI <LEI> [1..1] IdentifierSet 344
   TradeDate <TradDt> [0..1] ± 344
   ExpectedSettlementDate <XpctdSttlmDt> [0..1] ± 344
   SettlementDate <SttlmDt> [1..1] ± 344
   LateDeliveryDate <LateDlvryDt> [0..1] ± 345
   ExpectedValueDate <XpctdValDt> [0..1] ± 345
   AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 345
   MatchedStatusTimeStamp <MtchdStsTmStmp> [0..1] DateTime 345
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 332 March 2026
```

## File page 333

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C22,
C23,
C24,
C25
345
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C22,
C23,
C24,
C25
347
   TransactionAdditionalDetails <TxAddtlDtls> [0..1] Text 348
   SupplementaryData <SplmtryData> [0..*] ± C40 348
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
Settlement And Reconciliation - Maintenance 2025 - 2026 333 March 2026
```

## File page 334

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
Settlement And Reconciliation - Maintenance 2025 - 2026 334 March 2026
```

## File page 335

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
Settlement And Reconciliation - Maintenance 2025 - 2026 335 March 2026
```

