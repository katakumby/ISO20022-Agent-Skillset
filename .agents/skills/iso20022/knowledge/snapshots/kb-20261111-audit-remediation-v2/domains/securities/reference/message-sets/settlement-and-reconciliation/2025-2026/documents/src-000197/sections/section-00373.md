---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "18.3 Constraints"]
file_pages: [560, 561, 562, 563, 564, 565]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.024.001.14"]
---

# 18.3 Constraints

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 560 to 565.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 560

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 590
Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C4 590
Or}         LEI <LEI> [1..1] IdentifierSet 591
     LateDeliveryDate <LateDlvryDt> [0..1] ± 591
     ExpectedSettlementDate <XpctdSttlmDt> [0..1] ± 591
     ExpectedValueDate <XpctdValDt> [0..1] ± 591
     SettlementDate <SttlmDt> [1..1] ± 592
     TradeDate <TradDt> [0..1] ± 592
     AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 592
     MatchedStatusTimeStamp <MtchdStsTmStmp> [0..1] DateTime 592
     SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 593
     Payment <Pmt> [1..1] CodeSet 593
     SettlementParameters <SttlmParams> [1..1] ± C5, C33 593
     ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C20,
C21,
C22,
C23
594
     DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C20,
C21,
C22,
C23
596
     Investor <Invstr> [0..1] ± 597
     QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± 597
     SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
[0..1] Text 597
   SupplementaryData <SplmtryData> [0..*] ± C36 0
18.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 560 March 2026
```

## File page 561

```text
C3 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C4 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C5 CashClearingSystemRule
The CashSettlementSystem codes are to be used only by agents directly involved in the
settlement process, such as local settlement agents, CSDs and central banks.
C6 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C7 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C8 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C9 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C10 DescriptionUsageRule
Description must be used alone as the last resort.
C11 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C12 InferredMatchingStatusStatusPresenceRule
If ProcessingStatus, MatchingStatus and SettlementStatus are absent, then
InferredMatchingStatus must be present.
On Condition
    /ProcessingStatus is absent
 And    /MatchingStatus is absent
 And    /SettlementStatus is absent
Following Must be True
    /InferredMatchingStatus Must be present
This constraint is defined at the MessageDefinition level.
C13 InvestorCountryCodeRule
If Investor is present with a country code, then the country code specifies the nationality of the
investor, for example, for the settlement of certain securities (that is, airlines, defence
manufacturers) under the EU legislation.
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 561 March 2026
```

## File page 562

```text
C14 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C15 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C16 MarketTypeAndIdentificationRule
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
C17 MatchingStatusPresenceRule
If ProcessingStatus, InferredMatchingStatus and SettlementStatus are absent, then
MatchingStatus must be present.
On Condition
    /ProcessingStatus is absent
 And    /SettlementStatus is absent
 And    /InferredMatchingStatus is absent
Following Must be True
    /MatchingStatus Must be present
This constraint is defined at the MessageDefinition level.
C18 NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be
NONREF.
C19 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C20 Party2PresenceRule
If Party2 is present, then Party1 must be present.
C21 Party3PresenceRule
If Party3 is present, then Party2 must be present.
C22 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C23 Party5PresenceRule
If Party5 is present, then Party4 must be present.
C24 PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
C25 ProcessingStatusPresenceRule
If InferredMatchingStatus, MatchingStatus and SettlementStatus are absent, then
ProcessingStatus must be present.
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 562 March 2026
```

## File page 563

```text
On Condition
    /MatchingStatus is absent
 And    /SettlementStatus is absent
 And    /InferredMatchingStatus is absent
Following Must be True
    /ProcessingStatus Must be present
This constraint is defined at the MessageDefinition level.
C26 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C27 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C28 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C29 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C30 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
C31 SafekeepingPlaceFormatOrLEIRule
SafekeepingPlaceFormat must be present or LEI must be present.
C32 SecuritiesMarketPracticeGroupGuideline
The Securities Market Practice Group (SMPG) has published market practice
recommendations on the use of this message.
These market practices are available on www.smpg.info.
This constraint is defined at the MessageDefinition level.
C33 SettlementDetailsRule
If SettlementDetails elements are used, then their conditions of use must be pre-agreed
between account owner and account servicer.
C34 SettlementStatusAndMatchedRule
If settlement status/reason is present alone, then it means that the transaction is matched (if a
matching process exists in the concerned market or at the concerned account servicer).
This constraint is defined at the MessageDefinition level.
C35 SettlementStatusPresenceRule
If ProcessingStatus, InferredMatchingStatus and MatchingStatus are absent, then
SettlementStatus must be present.
On Condition
    /ProcessingStatus is absent
 And    /MatchingStatus is absent
 And    /InferredMatchingStatus is absent
Following Must be True
    /SettlementStatus Must be present
This constraint is defined at the MessageDefinition level.
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 563 March 2026
```

## File page 564

```text
C36 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C37 TwoLegTransactionOpeningClosing1Rule
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
TriParty Repo Opening
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: TriPartyRepo (TRPO)
TriParty Repo Closing
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: TriPartyRepo (TRPO)
TriParty Reverse Repo Opening
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: TriPartyReverseRepo (TRVO)
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 564 March 2026
```

## File page 565

```text
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
C38 TwoLegTransactionOpeningClosing2Rule
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
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 565 March 2026
```

