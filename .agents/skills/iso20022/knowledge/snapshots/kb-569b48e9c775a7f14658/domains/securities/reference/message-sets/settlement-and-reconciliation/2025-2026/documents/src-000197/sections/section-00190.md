---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.3 Constraints"]
file_pages: [280, 281, 282, 283, 284, 285, 286]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.3 Constraints

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 280 to 286.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 280

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or       MatchingStatus <MtchgSts> [1..1] ± 350
Or       InferredMatchingStatus <IfrrdMtchgSts> [1..1] ± 350
Or       SettlementStatus <SttlmSts> [1..1] ± C27 351
Or}       InstructionProcessingStatus <InstrPrcgSts> [1..1]  351
{Or         PendingProcessing <PdgPrcg> [1..1]  352
{Or           NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 353
Or}           Reason <Rsn> [1..*]  353
             Code <Cd> [1..1]  353
{Or               Code <Cd> [1..1] CodeSet 354
Or}               Proprietary <Prtry> [1..1] ± 355
             AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 355
Or         CancellationRequested <CxlReqd> [1..1] ± C4 355
Or         AcknowledgedAccepted <AckdAccptd> [1..1] ± 356
Or         Cancelled <Canc> [1..1] ± 356
Or         Generated <Gnrtd> [1..1]  356
{Or           NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 357
Or}           Reason <Rsn> [1..*] ± 357
Or         Repair <Rpr> [1..1] ± 357
Or         PendingCancellation <PdgCxl> [1..1]  357
{Or           NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 358
Or}           Reason <Rsn> [1..*]  358
             Code <Cd> [1..1]  358
{Or               Code <Cd> [1..1] CodeSet 359
Or}               Proprietary <Prtry> [1..1] ± 359
             AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 359
Or}         ModificationRequested <ModReqd> [1..1] ± C4 360
9.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 280 March 2026
```

## File page 281

```text
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C3 AdditionalDetailsRule
Unless bilaterally agreed between the sender and receiver, if TransactionAdditionalDetails is
present, then it must not contain information that can be provided in a structured field.
C4 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C5 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C6 CashClearingSystemRule
The CashSettlementSystem codes are to be used only by agents directly involved in the
settlement process, such as local settlement agents, CSD's and central banks.
C7 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C8 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C9 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C10 DeliveringParty1Rule
If the instruction is a receive, then DeliveringParty1 must be present.
C11 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C12 DescriptionUsageRule
Description must be used alone as the last resort.
C13 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 281 March 2026
```

## File page 282

```text
C14 EventTypeRule
The use of a specific corporate action event type code is allowed only if this specific event
triggers a securities movement as per the Event Interpretation Grid published by the Securities
Market Practice Group (SMPG).
The corporate action event indicator code OTHR must only be used in case no other corporate
action event code is appropriate.
The corporate action event indicator code CHAN must only be used in case no other corporate
action event code is appropriate and only for an event which relates to a change.
The corporate action event indicator code REDM must only be used when the redemption is
decided by the issuer and not by the holders.
C15 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C16 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C17 LateDeliveryDateRule
If LateDeliveryDate is present then the transaction must be a pool trade that results from the
original TBA (To Be Announced). The original TBA would be offset by an opposite transaction
and replaced by buys or sells of individual pools. It is a date greater than the settlement date
stated in the trade, for pools designed as settling late.
C18 MarketTypeAndIdentificationRule
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
C19 NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be
NONREF.
C20 NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be
NONREF.
C21 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C22 Party2PresenceRule
If Party2 is present, then Party1 must be present.
C23 Party3PresenceRule
If Party3 is present, then Party2 must be present.
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 282 March 2026
```

## File page 283

```text
C24 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C25 Party5PresenceRule
If Party5 is present, then Party4 must be present.
C26 PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
C27 PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
C28 PostingAmountRule
If the instruction is against payment, PostingAmount must be present.
C29 ReceivingParty1Rule
If the instruction is a delivery, then ReceivingParty 1 must be present.
C30 ReportNumberRule
If Long number (Exact5NumericTest) is used, then the report must be a delta reports
(UpdateType: DELT).
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the
same safekeeping account must have different ReportNumbers. For example, a daily report
sent on day 1 would have ReportNumber 001, on day 2, 002.
C31 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
This constraint is defined at the MessageDefinition level.
C32 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C33 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
This constraint is defined at the MessageDefinition level.
C34 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 283 March 2026
```

## File page 284

```text
C35 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
This constraint is defined at the MessageDefinition level.
C36 SafekeepingPlaceFormatOrLEIRule
SafekeepingPlaceFormat must be present or LEI must be present.
C37 SecuritiesMarketPracticeGroupGuideline
The Securities Market Practice Group (SMPG) has published market practice
recommendations on the use of this message.
These market practices are available on www.smpg.info.
This constraint is defined at the MessageDefinition level.
C38 SettlementDetailsRule
If SettlementDetails elements are used, then their conditions of use must be pre-agreed
between account owner and account servicer.
C39 SettlementStatusAndMatchedRule
If settlement status/reason is used alone, then it means that the transaction is matched (if a
matching process exists in the concerned market or at the concerned account servicer).
C40 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C41 TwoLegTransactionOpeningClosing1Rule
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
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 284 March 2026
```

## File page 285

```text
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
SettlementParameters/SecuritiesTransactionType: SecuritiesLending (SECL)
Securities Lending Return
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: SecuritiesLending (SECL)
Securities Borrowing Initiation
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: SecuritiesBorrowing (SECB)
Securities Borrowing Return
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 285 March 2026
```

## File page 286

```text
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: SecuritiesBorrowing (SECB).
C42 TwoLegTransactionOpeningClosing2Rule
For settlement of two part transactions (buy-sell back, sell buy-back, collateral in and out), the
opening/initiation and closing/return of the transaction is identified by the providing of the
following combination of SecuritiesMovementType codes and SettlementParameters/
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
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 286 March 2026
```

