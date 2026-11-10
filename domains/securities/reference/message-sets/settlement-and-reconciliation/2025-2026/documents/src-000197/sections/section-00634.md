---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["28 sese.034.001.11 SecuritiesFinancingStatusAdviceV11", "28.3 Constraints"]
file_pages: [955, 956, 957, 958, 959]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.034.001.11"]
---

# 28.3 Constraints

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 955 to 959.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 955

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     TradeDate <TradDt> [0..1] ± 982
     ExpectedSettlementDate <XpctdSttlmDt> [0..1] ± 983
     ExpectedValueDate <XpctdValDt> [0..1] ± 983
     LateDeliveryDate <LateDlvryDt> [0..1] ± 983
     RateChangeDate <RateChngDt> [0..1] ± 984
     SecuritiesFinancingTransactionType <SctiesFincgTxTp> [1..1] CodeSet 984
     SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 984
     Payment <Pmt> [1..1] CodeSet 984
     SettlementParameters <SttlmParams> [0..1] ± C8, C33 985
     RateType <RateTp> [0..1] ± 986
     VariableRateSupport <VarblRateSpprt> [0..1] ± 986
     RepurchaseRate <RpRate> [0..1] ± C35 986
     StockLoanMargin <StockLnMrgn> [0..1] ± C35 987
     SecuritiesHaircut <SctiesHrcut> [0..1] ± C35 987
     PricingRate <PricgRate> [0..1] ± 987
     Spread <Sprd> [0..1] ± C35 988
     DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C7, C12,
C21,
C22,
C23,
C24,
C32
988
     ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C7, C12,
C21,
C22,
C23,
C24,
C32
990
     Investor <Invstr> [0..1] ± 992
     SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
[0..1] Text 993
   SupplementaryData <SplmtryData> [0..*] ± C36 0
28.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 955 March 2026
```

## File page 956

```text
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C3 AdditionalDetailsRule
Unless bilaterally agreed between the sender and receiver, if
SettlementInstructionProcessingAdditionalDetails is present, then it must not contain
information that can be provided in a structured field.
C4 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C5 AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails,
RegistrationDetails and PartyContactDetails must not contain information that can be provided
in a structured field.
C6 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C7 BookTransferGuideline
In case of own account internal transfer, own account external transfer, portfolio transfer and in
specie transfer (see SecuritiesTransactionType), the account of (delivering) Party2 at
(delivering) Party1 must be provided.
For more details, see the relevant market practice document on www.smpg.info.
C8 CashClearingSystemRule
The CashSettlementSystem codes are to be used only by agents directly involved in the
settlement process, such as local settlement agents, CSDs and central banks.
C9 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C10 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C11 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C12 DepositoryGuideline
In a delivery, the receiving depository is to be understood as the requested depository of the
receiving counterparty.
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 956 March 2026
```

## File page 957

```text
In a receive, the delivering depository is to be understood as the requested depository of the
delivering counterparty.
The field must be populated with the BIC of a national or international CSD. When no CSD
exists in a particular market, the stock exchange BIC is to be used.
Country code should be used for settlement taking place outside of an institution published in
the PSET's BIC list. This includes physical deliveries and investment funds not settling at a
CSD.
The format and content of the settlement party sequences will comply with the market practices
published for the counterparty depository included in the message.
For more details, see the relevant market practice document on www.smpg.info.
C13 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C14 DescriptionUsageRule
Description must be used alone as the last resort.
C15 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C16 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C17 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C18 MarketTypeAndIdentificationRule
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
C19 NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be
NONREF.
C20 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C21 Party2PresenceRule
If Party2 is present, then Party1 must be present.
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 957 March 2026
```

## File page 958

```text
C22 Party3PresenceRule
If Party3 is present, then Party2 must be present.
C23 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C24 Party5PresenceRule
If Party5 is present, then Party4 must be present.
C25 PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
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
C32 SettlementChainGuideline
SMPG recommends that at least three settlement parties be instructed in equity or fixed income
receive
free or against payment settlement instructions; the depository, the participant of the depository
(Party1) and the client of Party1 (Party2).
The data format for the identification of Party1 depends on the market. If no country specific
requirement is available, BIC is recommended.
For more details, see the relevant market practice document on www.smpg.info.
C33 SettlementDetailsRule
If SettlementDetails elements are used, then their conditions of use must be pre-agreed
between account owner and account servicer.
C34 SettlementStatusAndMatchedRule
If SettlementStatus is present alone, then it means that the transaction is matched (if a
matching process exists in the concerned market or at the concerned account servicer).
This constraint is defined at the MessageDefinition level.
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 958 March 2026
```

## File page 959

```text
C35 SignRule
When Sign is present, rate must not be zero.
C36 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C37 TwoLegTransactionOpeningClosingRule
For transactions settling in two legs (Securities Financing), the opening/initiation and closing/
return information of the transaction is provided by sending the following combination of
SecuritiesMovementType codes and SecuritiesFinancingTransactionType codes:
Repo Opening
SecuritiesMovementType: Delivery (DELI)
SecuritiesFinancingTransactionType: Repo (REPU)
Repo Closing
SecuritiesMovementType: Receive (RECE)
SecuritiesFinancingTransactionType: Repo (REPU)
Reverse Repo Opening
SecuritiesMovementType: Receive (RECE)
SecuritiesFinancingTransactionType: ReverseRepo (RVPO)
Reverse Repo Closing
SecuritiesMovementType: Delivery (DELI)
SecuritiesFinancingTransactionType: ReverseRepo (RVPO)
Securities Lending Initiation
SecuritiesMovementType: Delivery (DELI)
SecuritiesFinancingTransactionType: SecuritiesLending (SECL)
Securities Lending Return
SecuritiesMovementType: Receive (RECE)
SecuritiesFinancingTransactionType: SecuritiesLending (SECL)
Securities Borrowing Initiation
SecuritiesMovementType: Receive (RECE)
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 959 March 2026
```

