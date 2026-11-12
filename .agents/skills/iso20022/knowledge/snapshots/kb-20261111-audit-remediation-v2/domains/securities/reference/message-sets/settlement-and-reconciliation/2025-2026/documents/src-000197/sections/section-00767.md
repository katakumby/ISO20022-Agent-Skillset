---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.3 Constraints"]
file_pages: [1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.3 Constraints

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1143 to 1152.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1143

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}           NetworkFeeQuantity <NtwkFeeQty> [1..1] Quantity 1291
         CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  1291
{Or           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1292
Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C8 1292
Or}           LEI <LEI> [1..1] IdentifierSet 1292
       OtherBusinessParties <OthrBizPties> [0..1]  C28,
C56
1292
         Investor <Invstr> [0..*] ± C25,
C60,
C66
1293
         QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± C61,
C67
1294
         StockExchange <StockXchg> [0..1] ± 1295
         TradeRegulator <TradRgltr> [0..1] ± 1295
         TripartyAgent <TrptyAgt> [0..1] ± C61,
C67
1295
         Broker <Brkr> [0..1] ± C61,
C67
1296
       AdditionalPhysicalOrRegistrationDetails
<AddtlPhysOrRegnDtls>
[0..1]  1297
         CertificationIdentification <CertfctnId> [0..1] Text 1297
         CertificationDateTime <CertfctnDtTm> [0..1] ± 1298
         RegistrarAccount <RegarAcct> [0..1] Text 1298
         CertificateNumber <CertNb> [0..*] ± C31 1298
       SupplementaryData <SplmtryData> [0..*] ± C78 1298
32.3 Constraints
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
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1143 March 2026
```

## File page 1144

```text
C3 AdditionalDetailsRule
Unless bilaterally agreed between the sender and receiver, if FXAdditionalDetails and/or
SettlementInstructionProcessingAdditionalDetails are present, then they must not contain
information that can be provided in a structured field.
C4 AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if
FinancialInstrumentAttributeAdditionalDetails is present, then it must not contain information
that can be provided in a structured field.
C5 AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if DeclarationlDetails and/or
PartyContactDetails are present, then they must not contain information that can be provided in
a structured field.
C6 AdditionalDetailsRule
Unless bilaterally agreed between the sender and receiver, if FXAdditionalDetails and/or
SettlementInstructionProcessingAdditionalDetails are present, then they must not contain
information that can be provided in a structured field.
C7 AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails,
RegistrationDetails and PartyContactDetails must not contain information that can be provided
in a structured field.
C8 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C9 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C10 BookTransferGuideline
In case of own account internal transfer, own account external transfer, portfolio transfer and in
specie transfer (see SecuritiesTransactionType), the account of (delivering) Party2 at
(delivering) Party1 must be provided.
For more details, see the relevant market practice document on www.smpg.info.
C11 BookTransferGuideline
In case of own account internal transfer, own account external transfer, portfolio transfer and in
specie transfer (see SecuritiesTransactionType), the account of (delivering) Party2 at
(delivering) Party1 must be provided.
For more details, see the relevant market practice document on www.smpg.info.
C12 CashSettlementSystemUsageRule
Cash settlement system codes are to be used only by agents directly involved in the settlement
process, such as local settlement agents, CSDs and central banks.
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1144 March 2026
```

## File page 1145

```text
C13 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C14 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C15 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C16 CurrencyToBuyOrSellRule
CurrencyToBuy and CurrencyToSell in the TradeDetails message component, provides an
instruction to the account servicer to execute a foreign exchange deal on behalf of the account
owner. The purpose of the forex deal is to fund the purchase of securities. This field is not to be
used when standing instructions have been established.
If CurrencyToSell is used, then it implies the following:
- the instruction is a receive.
- the currency required for funding a purchase of securities, for example, the currency to be
purchased, is the currency of the settlement amount. The currency to be sold to obtain
settlement currency is provided by the currency to sell message element. Normally, this is the
base currency of the portfolio.
- the amount of currency to be bought is equal to the settlement amount of the transaction. This
implies the forex will not be used for other transactions and that a bulk forex deal must be
instructed by other means.
- a forex deal to fund the purchase of securities should be executed in time for the currency to
be available on the settlement date of the securities transaction.
- a bilateral agreement regarding the use of this field has been established.
If CurrencyToBuy is used, then it implies the following:
- the instruction is a delivery
- the currency received as proceeds from the sale of securities, for example, the currency to be
sold, is the currency of the settlement amount. The currency to be bought is provided by the
currency to buy message element. If proceeds are repatriated, this is in the base currency of
the portfolio.
- the amount of currency to be sold is equal to the settlement amount of the transaction. This
implies a bulk forex deal must be instructed by other means.
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1145 March 2026
```

## File page 1146

```text
- a forex deal to repatriate proceeds after the sale of securities should be executed for the
soonest possible value date after settlement of the securities, as permitted by market
convention.
- a bilateral agreement regarding the use of this field has been established.
C17 CurrencyToBuyOrSellRule
CurrencyToBuy and CurrencyToSell in the TradeDetails message component, provides an
instruction to the account servicer to execute a foreign exchange deal on behalf of the account
owner. The purpose of the forex deal is to fund the purchase of securities. This field is not to be
used when standing instructions have been established.
If CurrencyToSell is used, then it implies the following:
- the instruction is a receive.
- the currency required for funding a purchase of securities, for example, the currency to be
purchased, is the currency of the settlement amount. The currency to be sold to obtain
settlement currency is provided by the currency to sell message element. Normally, this is the
base currency of the portfolio.
- the amount of currency to be bought is equal to the settlement amount of the transaction. This
implies the forex will not be used for other transactions and that a bulk forex deal must be
instructed by other means.
- a forex deal to fund the purchase of securities should be executed in time for the currency to
be available on the settlement date of the securities transaction.
- a bilateral agreement regarding the use of this field has been established.
If CurrencyToBuy is used, then it implies the following:
- the instruction is a delivery
- the currency received as proceeds from the sale of securities, for example, the currency to be
sold, is the currency of the settlement amount. The currency to be bought is provided by the
currency to buy message element. If proceeds are repatriated, this is in the base currency of
the portfolio.
- the amount of currency to be sold is equal to the settlement amount of the transaction. This
implies a bulk forex deal must be instructed by other means.
- a forex deal to repatriate proceeds after the sale of securities should be executed for the
soonest possible value date after settlement of the securities, as permitted by market
convention.
- a bilateral agreement regarding the use of this field has been established.
C18 DenominationRule
Unless bilaterally agreed between the account owner and servicer, if DenominationChoice is
used, it must not contain information that can be provided in a structured field.
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1146 March 2026
```

## File page 1147

```text
C19 DenominationRule
Unless bilaterally agreed between the account owner and servicer, if DenominationChoice is
used, it must not contain information that can be provided in a structured field.
C20 DepositoryGuideline
In a delivery, the receiving depository is to be understood as the requested depository of the
receiving counterparty.
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
C21 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C22 DescriptionUsageRule
Description must be used alone as the last resort.
C23 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C24 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C25 IdentificationNationalityOfInvestorRule
Identification and/or Nationality must be present.
C26 InvestorCapacityRule
If InvestorCapacity is used, then the use of the codes needs to be bi-laterally agreed.
C27 InvestorCapacityRule
If InvestorCapacity is used, then the use of the codes needs to be bi-laterally agreed.
C28 InvestorCountryCodeRule
If Investor is used with a country code, then the country code specifies the nationality of the
investor, for example, for the settlement of certain securities (that is, airlines, defence
manufacturers) under the EU legislation.
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1147 March 2026
```

## File page 1148

```text
C29 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C30 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C31 ISO8532AndIssuerSchemeNameRule
If Number is ISO 8532 (Format for transmission of certificate numbers), then Issuer and
SchemeName must not be used.
C32 LateDeliveryDateRule
If LateDeliveryDate is used, then the transaction must be a pool trade that results from the
original TBA (To Be Announced). The original TBA would be offset by an opposite transaction
and replaced by buys or sells of individual pools. It is a date greater than the settlement date
stated in the trade, for pools designed as settling late.
C33 LateDeliveryDateRule
If LateDeliveryDate is used, then the transaction must be a pool trade that results from the
original TBA (To Be Announced). The original TBA would be offset by an opposite transaction
and replaced by buys or sells of individual pools. It is a date greater than the settlement date
stated in the trade, for pools designed as settling late.
C34 LinkagesUsageRule
The linkages can only be used when modifying the Paired or Turned Quantity. For the changes
of linking and unlinking messages this must be done with the
SecuritiesSettlementConditionsModificationRequest.
This constraint is defined at the MessageDefinition level.
C35 LinkedQuantityRule
If linked quantity for partial pair-off and turned quantity for partial turns is used, then its usage
must be pre-agreed between the message account owner and account servicer.
C36 MarketTypeAndIdentificationRule
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
C37 NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, then the
AccountOwnerTransactionIdentification must be NONREF.
C38 NumberRule
If Number is negative, then Sign must be present.
C39 OpeningClosingUsageRule
For settlement of two parts transactions (Securities Financing, buy-sell back, sell buy-back), the
opening/initiation and closing/return of the transaction will be confirmed by sending the below
combination of ReceiveDelivery codes and SettlementTransactionType codes:
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1148 March 2026
```

## File page 1149

```text
Repo Opening
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
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1149 March 2026
```

## File page 1150

```text
ReceiveDelivery: Receive (RECE)
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
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1150 March 2026
```

## File page 1151

```text
SettlementTransactionType: CollateralIn (COLI)
Collateral (taker) In Return
ReceiveDelivery: Delivery (DELI)
SettlementTransactionType: CollateralIn (COLI).
C40 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C41 Party2PresenceRule
If Party2 is present, then Party1 must be present.
C42 Party2PresenceRule
If Party2 is present, then Party1 must be present.
C43 Party3PresenceRule
If Party3 is present, then Party2 must be present.
C44 Party3PresenceRule
If Party3 is present, then Party2 must be present.
C45 Party3PresenceRule
If Party3 is present, then Party2 must be present.
C46 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C47 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C48 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C49 Party5PresenceRule
If Party5 is present, then Party4 must be present.
C50 Party5PresenceRule
If Party5 is present, then Party4 must be present.
C51 Party5PresenceRule
If Party5 is present, then Party4 must be present.
C52 PhysicalInstructionDetailsUsageRule
AdditionalPhysicalOrRegistrationDetails can only be used with free of payment instructions.
This constraint is defined at the MessageDefinition level.
C53 PlaceOfListingRule
If PlaceOfListing is used and an ISO 10383 MIC exists for the market to be identified, the ISO
10383 Market Identifier Code (MIC) must be used.
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1151 March 2026
```

## File page 1152

```text
C54 PlaceOfTradeRule
If PlaceOfTrade is used and an ISO 10383 MIC exists for the market to be identified, then the
ISO 10383 Market Identifier Code (MIC) must be used.
C55 PlaceOfTradeRule
If PlaceOfTrade is used and an ISO 10383 MIC exists for the market to be identified, then the
ISO 10383 Market Identifier Code (MIC) must be used.
C56 QualifiedForeignIntermediaryRule
If Qualified Foreign Intermediary is used, then the instruction must be a delivery.
C57 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C58 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C59 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C60 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C61 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C62 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C63 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C64 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C65 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C66 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C67 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C68 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C69 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1152 March 2026
```

