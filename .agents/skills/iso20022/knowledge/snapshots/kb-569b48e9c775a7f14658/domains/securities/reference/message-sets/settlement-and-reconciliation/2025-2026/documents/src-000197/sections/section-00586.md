---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["27 sese.033.001.13 SecuritiesFinancingInstructionV13", "27.3 Constraints"]
file_pages: [886, 887, 888, 889, 890, 891, 892, 893, 894]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.033.001.13"]
---

# 27.3 Constraints

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 886 to 894.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 886

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
   OtherAmounts <OthrAmts> [0..1] ± 940
   DigitalPaymentSettlement <DgtlPmtSttlm> [0..2]  941
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C24,
C25,
C32,
C33,
C37
942
     Quantity <Qty> [1..1]  943
{Or       ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 943
Or}       NetworkFeeQuantity <NtwkFeeQty> [1..1] Quantity 943
     CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  943
{Or       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 944
Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C7 944
Or}       LEI <LEI> [1..1] IdentifierSet 944
   OtherBusinessParties <OthrBizPties> [0..1]  C31,
C44
944
     Investor <Invstr> [0..*] ± C29,
C49,
C53
945
     QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± C50,
C54
946
     StockExchange <StockXchg> [0..1] ± 947
     TradeRegulator <TradRgltr> [0..1] ± 947
     TripartyAgent <TrptyAgt> [0..1] ± C50,
C54
947
     Broker <Brkr> [0..1] ± C50,
C54
948
   SupplementaryData <SplmtryData> [0..*] ± C67 949
27.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 886 March 2026
```

## File page 887

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C3 AdditionalDetailsRule
Unless bilaterally agreed between the sender and receiver, if FXAdditionalDetails and/or
SettlementInstructionProcessingAdditionalDetails are present, then they must not contain
information that can be provided in a structured element.
C4 AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if
FinancialInstrumentAttributeAdditionalDetails is present, then it must not contain information
that can be provided in a structured field.
C5 AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if DeclarationlDetails and/or
PartyContactDetails are present, then they must not contain information that can be provided in
a structured field.
C6 AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails,
RegistrationDetails and PartyContactDetails must not contain information that can be provided
in a structured field.
C7 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C8 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C9 BlockTradeGuideline
In a block trade instruction, the total number of children must be provided using
TotalOfLinkedInstructions.
The CurrentInstructionNumber of the parent must be 000000. The children must have an
incremental CurrentInstructionNumber from 1 to 999999.
For more details, see the relevant market practice document on www.smpg.info.
C10 BookTransferGuideline
In case of own account internal transfer, own account external transfer, portfolio transfer and in
specie transfer (see SecuritiesTransactionType), the account of (delivering) Party2 at
(delivering) Party1 must be provided.
For more details, see the relevant market practice document on www.smpg.info.
C11 BuyerSSI1Rule
If standing settlement instruction applies and the transaction is a repo, then Buyer must be
present.
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 887 March 2026
```

## File page 888

```text
On Condition
    /TransactionTypeAndAdditionalParameters/
SecuritiesFinancingTransactionType is equal to value 'Repo'
 And    /StandingSettlementInstructionDetails is present
Following Must be True
    /StandingSettlementInstructionDetails/Counterparty/Buyer Must be present
This constraint is defined at the MessageDefinition level.
C12 BuyerSSI2Rule
If standing settlement instruction applies and the transaction is a securities lending, then Buyer
must be present.
On Condition
    /TransactionTypeAndAdditionalParameters/
SecuritiesFinancingTransactionType is equal to value 'SecuritiesLending'
 And    /StandingSettlementInstructionDetails is present
Following Must be True
    /StandingSettlementInstructionDetails/Counterparty/Buyer Must be present
This constraint is defined at the MessageDefinition level.
C13 CashClearingSystemRule
The CashSettlementSystem codes are to be used only by agents directly involved in the
settlement process, such as local settlement agents, CSD's and central banks.
C14 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C15 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C16 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
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
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 888 March 2026
```

## File page 889

```text
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
C18 CurrentInstructionNumberRule
If the Sender wants to indicate that this instruction is linked to one or more settlement
instruction, then the CurrentInstructionNumber must be specified.
C19 CurrentInstructionNumberRule
If the Sender wants to indicate that this instruction is linked to one or more settlement
instruction, then the CurrentInstructionNumber must be specified.
C20 DeliveringDepositoryAndParty1Part1Rule
If the transaction is a reverse repo and no standing settlement instruction applies, then
DeliveringDepository and Party1 must be present.
On Condition
    /TransactionTypeAndAdditionalParameters/
SecuritiesFinancingTransactionType is equal to value 'ReverseRepo'
 And    /StandingSettlementInstructionDetails is absent
Following Must be True
    /DeliveringSettlementParties/Depository Must be present
 And    /DeliveringSettlementParties/Party1 Must be present
This constraint is defined at the MessageDefinition level.
C21 DeliveringDepositoryAndParty1Part2Rule
If the transaction is a securities borrowing and no standing settlement instruction applies, then
DeliveringDepository and Party1 must be present.
On Condition
    /TransactionTypeAndAdditionalParameters/
SecuritiesFinancingTransactionType is equal to value 'SecuritiesBorrowing'
 And    /StandingSettlementInstructionDetails is absent
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 889 March 2026
```

## File page 890

```text
Following Must be True
    /DeliveringSettlementParties/Depository Must be present
 And    /DeliveringSettlementParties/Party1 Must be present
This constraint is defined at the MessageDefinition level.
C22 DenominationRule
Unless bilaterally agreed between the account owner and servicer, if DenominationChoice is
used, it must not contain information that can be provided in a structured field.
C23 DepositoryGuideline
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
C24 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C25 DescriptionUsageRule
Description must be used alone as the last resort.
C26 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C27 FXStandingInstructionPresenceRule
If HoldIndicator is present and is value TRUE (Yes), then FXStandingInstruction must be
absent.
C28 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C29 IdentificationNationalityOfInvestorRule
Identification and/or Nationality must be present.
C30 InvestorCapacityRule
If InvestorCapacity is used, then the use of the codes needs to be bi-laterally agreed.
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 890 March 2026
```

## File page 891

```text
C31 InvestorCountryCodeRule
If Investor is used with a country code, then the country code specifies the nationality of the
investor, for example, for the settlement of certain securities (that is, airlines, defence
manufacturers) under the EU legislation.
C32 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C33 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C34 LinkedQuantityRule
If linked quantity for partial pair-off and turned quantity for partial turns is used, then its usage
must be pre-agreed between the message account owner and account servicer.
C35 MarketTypeAndIdentificationRule
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
C36 NumberRule
If Number is negative, then Sign must be present.
C37 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C38 Party2PresenceRule
If Party2 is present, then Party1 must be present.
C39 Party3PresenceRule
If Party3 is present, then Party2 must be present.
C40 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C41 Party5PresenceRule
If Party5 is present, then Party4 must be present.
C42 PlaceOfListingRule
If PlaceOfListing is used and an ISO 10383 MIC exists for the market to be identified, the ISO
10383 Market Identifier Code (MIC) must be used.
C43 PlaceOfTradeRule
If PlaceOfTrade is used and an ISO 10383 MIC exists for the market to be identified, then the
ISO 10383 Market Identifier Code (MIC) must be used.
C44 QualifiedForeignIntermediaryRule
If Qualified Foreign Intermediary is used, then the instruction must be a delivery.
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 891 March 2026
```

## File page 892

```text
C45 ReceivingDepositoryAndParty1Part1Rule
If the transaction is a repo and no standing settlement instruction applies, then
ReceivingDepository and Party1 must be present.
On Condition
    /TransactionTypeAndAdditionalParameters/
SecuritiesFinancingTransactionType is equal to value 'Repo'
 And    /StandingSettlementInstructionDetails is absent
Following Must be True
    /ReceivingSettlementParties/Depository Must be present
 And    /ReceivingSettlementParties/Party1 Must be present
This constraint is defined at the MessageDefinition level.
C46 ReceivingDepositoryAndParty1Part2Rule
If the transaction is a securities lending and no standing settlement instruction applies, then
ReceivingDepository and Party1 must be present.
On Condition
    /TransactionTypeAndAdditionalParameters/
SecuritiesFinancingTransactionType is equal to value 'SecuritiesLending'
 And    /StandingSettlementInstructionDetails is absent
Following Must be True
    /ReceivingSettlementParties/Depository Must be present
 And    /ReceivingSettlementParties/Party1 Must be present
This constraint is defined at the MessageDefinition level.
C47 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C48 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C49 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C50 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C51 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C52 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C53 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C54 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C55 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
C56 SafekeepingPlaceFormatOrLEIRule
SafekeepingPlaceFormat must be present or LEI must be present.
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 892 March 2026
```

## File page 893

```text
C57 SafekeepingPlaceGuideline
When used (see usage rule SafekeepingPlaceRule), unless special arrangements exist
between the account servicer and the account owner, it is recommended to use the place of
safekeeping field following the market practice described below:
• SafekeepingPlaceType/SharesHeldAtNCSD: a NCSD's BIC will be used for domestic and
NCSD to NCSD settlement instructions.
• SafekeepingPlaceType/SharesHeldAtICSD: an ICSD's BIC will be used for ICSD internal,
ICSD/local and ICSD to ICSD settlement instructions.
• SafekeepingPlaceType/SharesHeldAtLoaclCustodian: applicable, for instance, when the
account servicer is a global custodian and provides the account owner with a position reporting
at global custodian's agents' level. When instructing, the fund manager would therefore
mention, as a place of safekeeping, the BIC of the global custodian's agent on the market.
Absence of SafekeepingPlace means that:
• The SafekeepingPlace information is kept by the account servicer (SLA, account structure,
ETC.) and should not be provided by the account owner.
• The SafekeepingPlace is the counterparty's Depository. The transaction is therefore domestic
(to an NCSD) or internal to an ICSD.
For more details, see the relevant market practice document on www.smpg.info.
C58 SafekeepingPlaceRule
The SafekeepingPlace functionality in the settlement instructions is only to be used for global
custodians that allow their clients to specify where the securities are to be held, for example, in
an ICSD account versus an account at the local CSD.
C59 SecuritiesMarketPracticeGroupGuideline
The Securities Market Practice Group (SMPG) has published market practice
recommendations on the use of this message.
These market practices are available on www.smpg.info.
This constraint is defined at the MessageDefinition level.
C60 SellerSSI1Rule
If standing settlement instruction applies and the transaction is a reverse repo, then Seller must
be present.
On Condition
    /TransactionTypeAndAdditionalParameters/
SecuritiesFinancingTransactionType is equal to value 'ReverseRepo'
 And    /StandingSettlementInstructionDetails is present
Following Must be True
    /StandingSettlementInstructionDetails/Counterparty/Seller Must be present
This constraint is defined at the MessageDefinition level.
C61 SellerSSI2Rule
If standing settlement instruction applies and the transaction is a securities borrowing, then
Seller must be present.
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 893 March 2026
```

## File page 894

```text
On Condition
    /TransactionTypeAndAdditionalParameters/
SecuritiesFinancingTransactionType is equal to value 'SecuritiesBorrowing'
 And    /StandingSettlementInstructionDetails is present
Following Must be True
    /StandingSettlementInstructionDetails/Counterparty/Seller Must be present
This constraint is defined at the MessageDefinition level.
C62 SettlementAmountRule
If the Transaction is against payment, then OpeningSettlementAmount must be present.
On Condition
    /TransactionTypeAndAdditionalParameters/Payment is equal to value 
'AgainstPaymentSettlement'
Following Must be True
    /OpeningSettlementAmount Must be present
This constraint is defined at the MessageDefinition level.
C63 SettlementChainGuideline
SMPG recommends that at least three settlement parties be instructed in equity or fixed income
receive
free or against payment settlement instructions; the depository, the participant of the depository
(Party1) and the client of Party1 (Party2).
The data format for the identification of Party1 depends on the market. If no country specific
requirement is available, BIC is recommended.
For more details, see the relevant market practice document on www.smpg.info.
C64 SettlementDetailsRule
If SettlementDetails elements are used, then their conditions of use must be pre-agreed
between account owner and account servicer.
C65 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C66 SignRule
When Sign is present, rate must not be zero.
C67 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C68 TradeDateTimeUTCRule
If Trade Date/Time is used with a time or a time + UTC indicator, then it must be the local time
of the place of trade, for example, of the stock exchange, or of the selling broker for OTC.
C69 VendorPresenceRule
If the settlement standing instruction database is a vendor database, then the vendor must be
identified.
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 894 March 2026
```

