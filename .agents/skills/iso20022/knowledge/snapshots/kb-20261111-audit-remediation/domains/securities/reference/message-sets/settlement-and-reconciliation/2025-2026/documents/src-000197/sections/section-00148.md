---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "8.3 Constraints"]
file_pages: [204, 205, 206, 207, 208, 209, 210, 211, 212, 213]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.017.001.14"]
topic_continuations: [{"constraint_ids": ["C47"], "until_heading": "8.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 214, "topic": "8.3 Constraints", "reference_path": "domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00149.md"}]
---

# 8.3 Constraints

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 204 to 213.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 8.3 Constraints topic continues in [Constraints continuation C47 (file p214)](section-00149.md#file-page-214). Read the text before **8.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 204

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C19 265
           PostingAmount <PstngAmt> [0..1] ± 265
           DigitalPaymentPostingSettlement <DgtlPmtPstngSttlm> [0..1]  265
             FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C8, C9,
C14,
C15,
C20
266
             ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 267
             CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  267
{Or               DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 267
Or               AnyBIC <AnyBIC> [1..1] IdentifierSet C4 267
Or}               LEI <LEI> [1..1] IdentifierSet 268
           AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 268
           TradeDate <TradDt> [0..1] ± 268
           EffectiveSettlementDate <FctvSttlmDt> [1..1] ± 268
           SettlementDate <SttlmDt> [0..1] ± 269
           ValueDate <ValDt> [0..1] ± 269
           AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 269
           MatchedStatusTimeStamp <MtchdStsTmStmp> [0..1] DateTime 269
           DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C21,
C22,
C23,
C24
269
           ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C21,
C22,
C23,
C24
270
           ReversalIndicator <RvslInd> [0..1] Indicator 272
           TransactionAdditionalDetails <TxAddtlDtls> [0..1] Text 272
         SupplementaryData <SplmtryData> [0..*] ± C42 272
8.3 Constraints
C1 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 204 March 2026
```

## File page 205

```text
C2 AdditionalDetailsRule
Unless bilaterally agreed between the sender and receiver, if TransactionAdditionalDetails is
present, then it must not contain information that can be provided in a structured field.
C3 AdditionalDetailsRule
Unless bilaterally agreed between the sender and receiver, if TransactionAdditionalDetails is
present, then it must not contain information that can be provided in a structured field.
C4 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C5 CashClearingSystemRule
The CashSettlementSystem codes are to be used only by agents directly involved in the
settlement process, such as local settlement agents, CSD's and central banks.
C6 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C7 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C8 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C9 DescriptionUsageRule
Description must be used alone as the last resort.
C10 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C11 EventTypeRule
The use of a specific corporate action event type code is allowed only if this specific event
triggers a securities movement as per the Event Interpretation Grid published by the Securities
Market Practice Group (SMPG).
The corporate action event indicator code OTHR must only be used in case no other corporate
action event code is appropriate.
The corporate action event indicator code CHAN must only be used in case no other corporate
action event code is appropriate and only for an event which relates to a change.
The corporate action event indicator code REDM must only be used when the redemption is
decided by the issuer and not by the holders.
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 205 March 2026
```

## File page 206

```text
C12 FinancialInstrumentDetailsOrSubAccountDetailsRule
If StatementGeneralDetails/ActivityIndicator is FALSE (No), then FinancialInstrumentDetails
and SubAccountDetails must be absent.
On Condition
    /StatementGeneralDetails/ActivityIndicator is equal to value 'false'
Following Must be True
    /SubAccountDetails[*] Must be absent
 And    /FinancialInstrumentDetails[*] Must be absent
This constraint is defined at the MessageDefinition level.
C13 FinancialInstrumentDetailsReportingRule
If StatementGeneralDetails/ActivityIndicator is TRUE (Yes) and SubAccountIndicator is FALSE
(No), then FinancialInstrumentDetails must be present and Sub Account Details must be
absent.
On Condition
    /StatementGeneralDetails/SubAccountIndicator is equal to value 'false'
 And    /StatementGeneralDetails/ActivityIndicator is equal to value 'true'
Following Must be True
    /SubAccountDetails[*] Must be absent
 And    /FinancialInstrumentDetails[*] Must be present
This constraint is defined at the MessageDefinition level.
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
C17 NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be
NONREF.
C18 NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be
NONREF.
C19 NumberRule
If Number is negative, then Sign must be present.
C20 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 206 March 2026
```

## File page 207

```text
C21 Party2PresenceRule
If Party2 is present, then Party1 must be present.
C22 Party3PresenceRule
If Party3 is present, then Party2 must be present.
C23 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C24 Party5PresenceRule
If Party5 is present, then Party4 must be present.
C25 PostingAmountRule
If the instruction is against payment, PostingAmount must be present.
C26 PostingAmountRule
If the instruction is against payment, PostingAmount must be present.
C27 ReportNumberRule
If ReportNumber/Long number (Exact5NumericTest) is used, then the report must be a delta
reports (UpdateType: DELT).
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the
same safekeeping account must have different ReportNumbers. For example, a daily report
sent on day 1 would have ReportNumber 001, on day 2, 002.
C28 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
This constraint is defined at the MessageDefinition level.
C29 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C30 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C31 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
This constraint is defined at the MessageDefinition level.
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 207 March 2026
```

## File page 208

```text
C32 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C33 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C34 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
This constraint is defined at the MessageDefinition level.
C35 SafekeepingPlaceFormatOrLEIRule
SafekeepingPlaceFormat must be present or LEI must be present.
C36 SecuritiesMarketPracticeGroupGuideline
The Securities Market Practice Group (SMPG) has published market practice
recommendations on the use of this message.
These market practices are available on www.smpg.info.
This constraint is defined at the MessageDefinition level.
C37 SettlementDetailsRule
If SettlementDetails elements are used, then their conditions of use must be pre-agreed
between account owner and account servicer.
C38 ShortLongDefaultRule
If Shortlong is absent, then the default is long, that is, balance is positive.
C39 ShortLongDefaultRule
If Shortlong is absent, then the default is long, that is, balance is positive.
C40 SmartContractAutomatedPricingRule
When Type/Code does not equal SmartContractAutomatedPricingSystem (SCAS) then
Identification/Description length must be maximum 35 characters.
C41 SubAccountDetailsFinancialInstrumentPresenceRule
If StatementGeneralDetails/ActivityIndicator is TRUE (Yes) and SubAccountIndicator is TRUE
(YES), then SubAccountDetails must be present and FinancialInstrumentDetails must be
absent.
On Condition
    /StatementGeneralDetails/SubAccountIndicator is equal to value 'true'
 And    /StatementGeneralDetails/ActivityIndicator is equal to value 'true'
Following Must be True
    /SubAccountDetails[*] Must be present
 And    /FinancialInstrumentDetails[*] Must be absent
This constraint is defined at the MessageDefinition level.
C42 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 208 March 2026
```

## File page 209

```text
C43 TwoLegTransactionOpeningClosing1Rule
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
TriParty Reverse Repo Closing
SecuritiesMovementType: Delivery (DELI)
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 209 March 2026
```

## File page 210

```text
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
C44 TwoLegTransactionOpeningClosing1Rule
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
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 210 March 2026
```

## File page 211

```text
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
SecuritiesMovementType: Delivery (DELI)
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 211 March 2026
```

## File page 212

```text
SettlementParameters/SecuritiesTransactionType: SecuritiesBorrowing (SECB).
C45 TwoLegTransactionOpeningClosing2Rule
For settlement of two part transactions (buy-sell back, sell buy-back, collateral in and out), the
opening/initiation and closing/return of the transaction is confirmed by sending the following
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
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 212 March 2026
```

## File page 213

```text
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: CollateralIn (COLI).
C46 TwoLegTransactionOpeningClosing2Rule
For settlement of two part transactions (buy-sell back, sell buy-back, collateral in and out), the
opening/initiation and closing/return of the transaction is confirmed by sending the following
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
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 213 March 2026
```

